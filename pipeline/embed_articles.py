#!/usr/bin/env python3
"""Embed articles via Jina AI (jina-embeddings-v3) into Cloudflare Vectorize + D1.

Chunking:
  - 6000-char chunks with 200-char overlap, no per-article cap
  - Each chunk embedded as "{title}\\n\\n{chunk_text}", task=retrieval.passage
  - body_snippet stored in full (not truncated) — used by /ask for Gemini context
  - Vectorize upsert via wrangler CLI

Progress tracking:
  - D1 is the single source of truth — a slug is "done" only after its D1 row exists
  - D1 is written ONLY after Vectorize upsert succeeds (no false positives)
  - Interrupted runs resume cleanly on next invocation

Usage:
    python pipeline/embed_articles.py --reset         # FIRST RUN: wipe index + D1, start fresh
    python pipeline/embed_articles.py                 # resume: skips slugs already in D1
    python pipeline/embed_articles.py --issue april-1995
    python pipeline/embed_articles.py --limit 10      # smoke-test with 10 articles
"""

import argparse
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path
from typing import Optional

import requests
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_ID   = os.environ["CLOUDFLARE_ACCOUNT_ID"]
API_TOKEN    = os.environ["CLOUDFLARE_API_TOKEN"]
DATABASE_ID  = os.environ["CLOUDFLARE_D1_DATABASE_ID"]
JINA_API_KEY = os.environ["JINA_API_KEY"]

VECTORIZE_INDEX = "nic-archives-search"
BASE_DIR        = Path(__file__).parent.parent
ARTICLES_DIR    = BASE_DIR / "articles"
WORKERS_DIR     = BASE_DIR / "workers"
VECTORS_FILE    = Path(__file__).parent / "vectors.ndjson"

CF_HEADERS   = {"Authorization": f"Bearer {API_TOKEN}", "Content-Type": "application/json"}
JINA_HEADERS = {"Authorization": f"Bearer {JINA_API_KEY}", "Content-Type": "application/json"}

D1_QUERY_URL   = f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/d1/database/{DATABASE_ID}/query"
JINA_EMBED_URL = "https://api.jina.ai/v1/embeddings"

CHUNK_SIZE       = 6000  # chars (~1500 tokens, well within Jina's 8192-token limit)
OVERLAP          = 200   # char overlap between consecutive chunks
EMBED_BATCH_SIZE = 20    # texts per Jina call (20 * ~1500 tokens = 30K tokens/batch)
BATCH_DELAY      = 20    # seconds between batches (3 batches/min = 90K tokens/min < 100K TPM)
D1_CHUNK_SIZE    = 10    # rows per D1 INSERT (10 rows × 5 cols = 50 params < 100-param limit)
RETRY_MAX        = 3
RETRY_DELAY      = 30.0  # 30s/60s waits on retry — lets TPM window reset after a 429


# ---------------------------------------------------------------------------
# Text processing
# ---------------------------------------------------------------------------

def clean_body(body: str) -> str:
    text = re.sub(r"^> \*\*\[Image\]\*\*.*$", "", body, flags=re.MULTILINE)
    text = re.sub(r"^#+\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\[\^\d+\]:.*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"^[-*\d]+[.)]\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    return " ".join(text.split())


def chunk_body(body: str) -> list[str]:
    """Split body into overlapping chunks, preferring sentence boundaries."""
    text = clean_body(body)
    if not text:
        return []

    chunks = []
    start = 0
    while start < len(text):
        end = start + CHUNK_SIZE
        if end >= len(text):
            chunks.append(text[start:])
            break

        boundary = end
        for punct in (".", "!", "?"):
            pos = text.rfind(punct, end - 200, end)
            if pos != -1 and pos > start:
                boundary = pos + 1
                break

        chunks.append(text[start:boundary].strip())
        start = boundary - OVERLAP

    # Drop near-empty chunks (OCR artifacts, stub articles)
    return [c for c in chunks if len(c) >= 50]


def parse_frontmatter(text: str) -> tuple:
    if not text.startswith("---\n"):
        return {}, text
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        return {}, text
    meta = {}
    for line in parts[1].splitlines():
        m = re.match(r"^(\w+):\s*(.+)$", line)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if val == "null":
            meta[key] = None
        elif val.startswith('"') and val.endswith('"'):
            meta[key] = val[1:-1]
        elif val.startswith("[") and val.endswith("]"):
            inner = val[1:-1]
            meta[key] = [int(x.strip()) for x in inner.split(",") if x.strip().isdigit()]
        else:
            try:
                meta[key] = int(val)
            except ValueError:
                meta[key] = val
    return meta, parts[2]


def make_issue_slug(issue_date: str) -> str:
    return issue_date.lower().replace(" ", "-")


def get_issue_date(meta: dict) -> str:
    return meta.get("issue_date") or meta.get("date") or "Unknown"


def make_vector_id(slug: str, chunk_index: int) -> str:
    # Vectorize vector IDs have a 64-char limit; truncate slug to leave room for suffix
    safe_slug = slug[:55].rstrip("-")
    return f"{safe_slug}__c{chunk_index}"


# ---------------------------------------------------------------------------
# Cloudflare + Jina API
# ---------------------------------------------------------------------------

def _retry(fn, label: str):
    for attempt in range(1, RETRY_MAX + 1):
        try:
            return fn()
        except Exception as e:
            if attempt == RETRY_MAX:
                raise
            wait = RETRY_DELAY * attempt
            print(f"    [{label}] attempt {attempt} failed: {e}. Retrying in {wait:.0f}s...")
            time.sleep(wait)


def embed_texts(texts: list[str]) -> list[list[float]]:
    def call():
        resp = requests.post(
            JINA_EMBED_URL,
            headers=JINA_HEADERS,
            json={
                "model": "jina-embeddings-v3",
                "task": "retrieval.passage",
                "dimensions": 1024,
                "input": texts,
            },
            timeout=60,
        )
        resp.raise_for_status()
        items = resp.json()["data"]
        # Sort by index to guarantee order matches input
        items.sort(key=lambda x: x["index"])
        return [item["embedding"] for item in items]
    return _retry(call, "jina-embed")


def _d1_query(sql: str, params: list = None) -> list:
    body = {"sql": sql}
    if params:
        body["params"] = params
    def call():
        resp = requests.post(D1_QUERY_URL, headers=CF_HEADERS, json=body, timeout=60)
        resp.raise_for_status()
        return resp.json().get("result", [{}])[0].get("results", [])
    return _retry(call, "d1")


def d1_upsert_articles(rows: list[dict]) -> None:
    for i in range(0, len(rows), D1_CHUNK_SIZE):
        chunk = rows[i : i + D1_CHUNK_SIZE]
        placeholders = ", ".join(["(?, ?, ?, ?, ?)"] * len(chunk))
        sql = (
            "INSERT OR REPLACE INTO articles "
            "(slug, title, issue_date, issue_slug, url) "
            f"VALUES {placeholders}"
        )
        params = []
        for row in chunk:
            params.extend([row["slug"], row["title"], row["issue_date"], row["issue_slug"], row["url"]])
        _d1_query(sql, params)


def d1_clear_articles() -> None:
    _d1_query("DELETE FROM articles")


def get_embedded_slugs() -> set:
    rows = _d1_query("SELECT slug FROM articles")
    return {r["slug"] for r in rows}


def _wrangler_env() -> dict:
    """Return os.environ without CLOUDFLARE_API_TOKEN so wrangler uses its OAuth token."""
    env = os.environ.copy()
    env.pop("CLOUDFLARE_API_TOKEN", None)
    return env


def vectorize_upsert(ndjson_path: Path) -> None:
    print(f"  Running: wrangler vectorize upsert {VECTORIZE_INDEX} --file={ndjson_path}")
    result = subprocess.run(
        ["wrangler", "vectorize", "upsert", VECTORIZE_INDEX, f"--file={ndjson_path}", "--batch-size=500"],
        cwd=str(WORKERS_DIR),
        capture_output=True,
        text=True,
        env=_wrangler_env(),
    )
    if result.stdout:
        print(result.stdout)
    if result.returncode != 0:
        print(result.stderr)
        raise RuntimeError(f"wrangler vectorize upsert failed (exit {result.returncode})")
    print("  ✓ Vectorize upsert complete")


def reset_vectorize_index() -> None:
    """Delete and recreate the Vectorize index at 1024 dimensions (cosine metric)."""
    print("Resetting Vectorize index...")

    result = subprocess.run(
        ["wrangler", "vectorize", "delete", VECTORIZE_INDEX, "--force"],
        cwd=str(WORKERS_DIR),
        capture_output=True,
        text=True,
        env=_wrangler_env(),
    )
    combined = (result.stdout + result.stderr).lower()
    if result.returncode == 0 or "not found" in combined or "does not exist" in combined:
        print("  ✓ Old index deleted (or did not exist)")
    else:
        print(f"  Warning: delete returned exit {result.returncode}: {result.stderr.strip()}")

    time.sleep(3)  # brief pause before recreating

    result = subprocess.run(
        ["wrangler", "vectorize", "create", VECTORIZE_INDEX, "--dimensions=1024", "--metric=cosine"],
        cwd=str(WORKERS_DIR),
        capture_output=True,
        text=True,
        env=_wrangler_env(),
    )
    if result.returncode != 0:
        raise RuntimeError(f"Failed to create Vectorize index: {result.stderr}")
    print("  ✓ New 1024-dim cosine index created")


# ---------------------------------------------------------------------------
# Article loading
# ---------------------------------------------------------------------------

def load_articles(issue_filter: Optional[str]) -> list[dict]:
    articles = []
    for md_path in sorted(ARTICLES_DIR.glob("*.md")):
        slug = md_path.stem
        if issue_filter and issue_filter not in slug:
            continue
        text = md_path.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text)
        issue_date = get_issue_date(meta)
        articles.append({
            "slug": slug,
            "title": meta.get("title", ""),
            "issue_date": issue_date,
            "issue_slug": make_issue_slug(issue_date),
            "url": f"/articles/{slug}.html",
            "body": body,
        })
    return articles


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Embed NIC articles into Cloudflare Vectorize + D1")
    parser.add_argument("--reset", action="store_true",
                        help="Wipe Vectorize index (recreate at 1024-dim) and clear D1. Use on first run.")
    parser.add_argument("--issue", help="Only embed articles from this issue (e.g. april-1995)")
    parser.add_argument("--limit", type=int, help="Only embed first N articles (smoke testing)")
    parser.add_argument("--force", action="store_true",
                        help="Re-embed all articles (ignores D1 done-list, keeps index)")
    args = parser.parse_args()

    if args.reset:
        reset_vectorize_index()
        print("Clearing D1 articles table...")
        d1_clear_articles()
        print("  ✓ D1 cleared")
        VECTORS_FILE.unlink(missing_ok=True)
        print()

    print("Loading articles...")
    articles = load_articles(args.issue)
    if args.limit:
        articles = articles[: args.limit]
    print(f"  {len(articles)} articles loaded")

    if args.force or args.reset:
        already_done = set()
    else:
        print("Checking D1 for already-embedded slugs...")
        already_done = get_embedded_slugs()
        print(f"  {len(already_done)} already embedded — skipping")

    to_embed = [a for a in articles if a["slug"] not in already_done]
    print(f"  {len(to_embed)} articles to embed\n")

    if not to_embed:
        print("Nothing to do.")
        return

    # Pre-compute all chunks
    print("Chunking article bodies...")
    article_chunks = []
    article_meta = []

    for a in to_embed:
        raw_chunks = chunk_body(a["body"])
        if not raw_chunks:
            raw_chunks = [a["title"]]  # stub article: embed title only

        article_meta.append({
            "slug": a["slug"],
            "title": a["title"],
            "issue_date": a["issue_date"],
            "issue_slug": a["issue_slug"],
            "url": a["url"],
        })

        for ci, chunk_text in enumerate(raw_chunks):
            article_chunks.append({
                "vector_id":   make_vector_id(a["slug"], ci),
                "slug":        a["slug"],
                "chunk_index": ci,
                "title":       a["title"],
                "issue_date":  a["issue_date"],
                "url":         a["url"],
                "body_snippet": chunk_text,                    # full chunk — not truncated
                "embed_text":  f"{a['title']}\n\n{chunk_text}",
            })

    total_chunks = len(article_chunks)
    avg = total_chunks / len(to_embed)
    print(f"  {total_chunks} chunks across {len(to_embed)} articles (avg {avg:.1f}/article)\n")

    # Phase 1: Embed all chunks via Jina AI
    print("Phase 1: Embedding via Jina AI (jina-embeddings-v3, task=retrieval.passage)...")
    errors = []
    vectors_written = 0

    with VECTORS_FILE.open("w") as fh:
        for batch_start in range(0, total_chunks, EMBED_BATCH_SIZE):
            batch = article_chunks[batch_start : batch_start + EMBED_BATCH_SIZE]
            texts = [c["embed_text"] for c in batch]

            try:
                vectors = embed_texts(texts)
                for chunk, vec in zip(batch, vectors):
                    row = {
                        "id": chunk["vector_id"],
                        "values": vec,
                        "metadata": {
                            "slug":         chunk["slug"],
                            "chunk_index":  chunk["chunk_index"],
                            "title":        chunk["title"],
                            "issue_date":   chunk["issue_date"],
                            "url":          chunk["url"],
                            "body_snippet": chunk["body_snippet"],
                        },
                    }
                    fh.write(json.dumps(row) + "\n")
                    vectors_written += 1

                pct = vectors_written / total_chunks * 100
                print(f"  ✓ {vectors_written}/{total_chunks} ({pct:.0f}%)")

            except Exception as e:
                print(f"  ✗ batch {batch_start // EMBED_BATCH_SIZE + 1} failed: {e}")
                errors.extend(c["slug"] for c in batch)

            if batch_start + EMBED_BATCH_SIZE < total_chunks:
                time.sleep(BATCH_DELAY)

    print(f"\n  {vectors_written} vectors written to {VECTORS_FILE}")

    if vectors_written == 0:
        print("No vectors to upsert — all batches failed.")
        sys.exit(1)

    # Phase 2: Upsert vectors to Vectorize
    print("\nPhase 2: Upserting vectors to Vectorize via wrangler...")
    vectorize_upsert(VECTORS_FILE)

    # Phase 3: Mark completed articles in D1 (only slugs with no errors)
    error_slugs = set(errors)
    clean_meta = [m for m in article_meta if m["slug"] not in error_slugs]
    print(f"\nPhase 3: Marking {len(clean_meta)} articles done in D1...")
    d1_upsert_articles(clean_meta)
    print(f"  ✓ {len(clean_meta)} articles written to D1")

    print(f"\n✓ Done. {len(to_embed)} articles, {vectors_written} vectors upserted.")
    print("  Wait 60 seconds before querying — Vectorize has eventual consistency.\n")

    if errors:
        unique_errors = sorted(set(errors))
        print(f"✗ {len(unique_errors)} articles had embed errors: {unique_errors[:10]}")
        sys.exit(1)


if __name__ == "__main__":
    main()
