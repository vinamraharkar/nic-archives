#!/usr/bin/env python3
"""
Visual-first article segmentation using Gemini Vision.

Instead of OCR-text → Gemini-text-segmentation, this does:
  page image → Gemini Vision (detects articles + reads text visually) → merge continuations

Writes to articles_visual/ so you can diff against articles/ without overwriting.

Usage:
    python pipeline/segment_visual.py
    python pipeline/segment_visual.py --issue october-1992
    python pipeline/segment_visual.py --issue april-1995 --force
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from pipeline.utils import make_article_slug, make_frontmatter

BASE_DIR = Path(__file__).parent.parent
DOCS_PAGES_DIR = BASE_DIR / "docs" / "pages"
ARTICLES_VISUAL_DIR = BASE_DIR / "articles_visual"

MAX_RETRIES = 3

KNOWN_ISSUES = {
    "october-1992": "October 1992",
    "april-1995": "April 1995",
    "april-2003": "April 2003",
}


# ── Per-page visual extraction ─────────────────────────────────────────────────

PAGE_PROMPT = """You are analyzing page {page_n} of a scanned NIC Informatics newsletter called "Informatics".

Extract every distinct article visible on this page. For each article:
- "title": the headline text, copied exactly as printed (keep uppercase if printed uppercase)
- "section": section label if printed near the headline (e.g. "COVER STORY", "NEWS", "PROJECTS", "FEATURES"). null if not visible.
- "body": the FULL body text of this article on THIS PAGE ONLY, in correct reading order across all columns
- "continues_to": page number if article says "Contd. on page X" or "Continued on page X", else null
- "continued_from": page number if this article begins with "Contd. from page X" or "Continued from page X", else null

Important:
- Section labels (COVER STORY, NEWS, etc.) are metadata on the article, NOT separate articles themselves
- Page headers/footers (issue name, page number, date) should NOT be included in body text
- If the entire page is a continuation of one article with no new headline, return one item with title=null and continued_from=<page>
- Read multi-column text in correct visual reading order (top-to-bottom within each column, left column before right column)

Return ONLY a valid JSON array, no other text:
[{{"title": "string or null", "section": "string or null", "body": "string", "continues_to": "int or null", "continued_from": "int or null"}}]"""


def extract_page(client, page_path: Path, page_n: int) -> list[dict] | None:
    """Call Gemini Vision on one page image. Returns list of article fragments or None."""
    from google.genai import types as gai_types

    img_bytes = page_path.read_bytes()
    prompt = PAGE_PROMPT.format(page_n=page_n)

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=[
                    gai_types.Part.from_bytes(data=img_bytes, mime_type="image/jpeg"),
                    prompt,
                ],
            )
            raw = response.text.strip()
            raw = re.sub(r"^```(?:json)?\s*", "", raw)
            raw = re.sub(r"\s*```$", "", raw)
            fragments = json.loads(raw)
            if not isinstance(fragments, list):
                raise ValueError("Response is not a JSON array")
            return fragments

        except (json.JSONDecodeError, ValueError) as e:
            if attempt < MAX_RETRIES:
                print(f"      [retry {attempt}] parse error: {e}")
                time.sleep(2 ** attempt)
            else:
                print(f"      FAILED to parse page {page_n}: {e}")
                return None

        except Exception as e:
            if attempt < MAX_RETRIES:
                print(f"      [retry {attempt}] API error: {e} — retrying in {2**attempt}s")
                time.sleep(2 ** attempt)
            else:
                print(f"      FAILED page {page_n}: {e}")
                return None

    return None


# ── Article merging ────────────────────────────────────────────────────────────

def merge_fragments(all_fragments: list[dict]) -> list[dict]:
    """
    Merge per-page article fragments into complete articles.

    all_fragments: [{page, title, section, body, continues_to, continued_from}]
    Returns: [{title, section, pages, body, author}]
    """
    # Titled fragments are article starts; untitled are pure continuations
    titled = [f for f in all_fragments if f.get("title")]

    # Build lookup: from_page → list of continuation fragments on the next page
    # A continuation fragment is any fragment (titled or not) with continued_from set
    cont_by_prev_page: dict[int, list[dict]] = {}
    for f in all_fragments:
        from_page = f.get("continued_from")
        if from_page is not None:
            cont_by_prev_page.setdefault(int(from_page), []).append(f)

    articles = []
    used_fragments: set[int] = set()  # avoid double-counting

    for frag in titled:
        frag_id = id(frag)
        if frag_id in used_fragments:
            continue
        used_fragments.add(frag_id)

        title = frag["title"].strip()
        section = frag.get("section")
        pages = [frag["page"]]
        body_parts = [frag["body"].strip()]

        # Follow continuation chain: current page → next page → ...
        current_page = frag["page"]
        continues_to = frag.get("continues_to")
        visited_pages: set[int] = {current_page}

        while continues_to is not None:
            next_page = int(continues_to)
            if next_page in visited_pages:
                break
            visited_pages.add(next_page)

            # Find the continuation fragment on next_page that came from current_page
            candidates = cont_by_prev_page.get(current_page, [])
            next_frag = next((c for c in candidates if c["page"] == next_page), None)

            if next_frag is None:
                break

            used_fragments.add(id(next_frag))
            pages.append(next_page)
            body_parts.append(next_frag["body"].strip())
            continues_to = next_frag.get("continues_to")
            current_page = next_page

        full_body = "\n\n".join(p for p in body_parts if p)
        author = _extract_author(full_body)

        articles.append({
            "title": title,
            "section": section,
            "author": author,
            "pages": sorted(set(pages)),
            "body": full_body,
        })

    return articles


def _extract_author(body: str) -> str | None:
    """Try to extract author byline from article body text."""
    # "By Name" at start
    m = re.match(r"^By\s+([A-Z][^\n]{2,50})\n", body)
    if m:
        return m.group(1).strip()
    # "— Name" or "- Name" at end of body
    m = re.search(r"[—\-]\s*([A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,3})\s*$", body)
    if m:
        return m.group(1).strip()
    return None


# ── Issue processing ───────────────────────────────────────────────────────────

def process_issue(client, issue_slug: str, issue_date: str, force: bool = False) -> int:
    page_dir = DOCS_PAGES_DIR / issue_slug
    if not page_dir.exists():
        print(f"  No page images for {issue_slug} — skipping")
        return 0

    out_dir = ARTICLES_VISUAL_DIR
    out_dir.mkdir(exist_ok=True)

    # Check if already done (sentinel file)
    sentinel = out_dir / f".{issue_slug}.done"
    if sentinel.exists() and not force:
        print(f"  [skip] {issue_slug} already processed (use --force to redo)")
        return 0

    page_paths = sorted(page_dir.glob("page-*.jpg"), key=lambda p: int(re.search(r"page-(\d+)", p.name).group(1)))
    print(f"\n{issue_slug}  ({len(page_paths)} pages)")

    all_fragments: list[dict] = []

    for page_path in page_paths:
        page_n = int(re.search(r"page-(\d+)", page_path.name).group(1))
        print(f"  Page {page_n}...", end=" ", flush=True)

        fragments = extract_page(client, page_path, page_n)

        if fragments is None:
            print("FAILED")
            continue

        for frag in fragments:
            frag["page"] = page_n
            # Normalise continues_to / continued_from to int or None
            for key in ("continues_to", "continued_from"):
                val = frag.get(key)
                if val is not None:
                    try:
                        frag[key] = int(val)
                    except (TypeError, ValueError):
                        frag[key] = None

        titles = [f.get("title") or "(continuation)" for f in fragments]
        print(f"{len(fragments)} fragment(s): {', '.join(titles[:3])}{'...' if len(titles) > 3 else ''}")
        all_fragments.extend(fragments)

        time.sleep(0.5)  # avoid rate limiting

    articles = merge_fragments(all_fragments)
    print(f"\n  Merged → {len(articles)} articles")

    written = 0
    for art in articles:
        title = art["title"]
        body = art["body"]
        if not title or not body:
            continue

        slug = make_article_slug(title, issue_date)
        fm = make_frontmatter(
            title=title,
            issue_date=issue_date,
            pages=art["pages"],
            author=art.get("author"),
            section=art.get("section"),
        )
        content = fm + f"## {title}\n\n{body}\n"
        out_path = out_dir / f"{slug}.md"
        out_path.write_text(content, encoding="utf-8")
        written += 1
        print(f"    → {out_path.name}  (pages {art['pages']}, {len(body):,} chars)")

    sentinel.touch()
    print(f"  Done: {written} articles written to articles_visual/")
    return written


# ── CLI ────────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description="Visual-first article segmentation via Gemini Vision")
    parser.add_argument("--issue", metavar="SLUG", help="Process only this issue (e.g. october-1992)")
    parser.add_argument("--force", action="store_true", help="Re-process even if already done")
    args = parser.parse_args()

    from dotenv import load_dotenv
    from google import genai as gai

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("ERROR: GEMINI_API_KEY not set in .env")
        sys.exit(1)

    client = gai.Client(api_key=api_key)

    issues = KNOWN_ISSUES
    if args.issue:
        if args.issue not in issues:
            print(f"Unknown issue '{args.issue}'. Known: {', '.join(issues)}")
            sys.exit(1)
        issues = {args.issue: issues[args.issue]}

    total = 0
    for slug, date in issues.items():
        total += process_issue(client, slug, date, force=args.force)

    print(f"\nTotal: {total} articles written to articles_visual/")
    print("Compare with articles/ using: diff articles/ articles_visual/")


if __name__ == "__main__":
    main()
