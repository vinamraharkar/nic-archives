#!/usr/bin/env python3
"""
Segment each issue's raw text into individual articles using Gemini.

Usage:
    python pipeline/segment_articles.py                         # process all issues
    python pipeline/segment_articles.py --files Apr-1995.pdf April-2003.pdf  # pilot mode
    python pipeline/segment_articles.py --dry-run               # show prompt, no API call

Input:  raw_text/{slug}.json  →  [{page: N, text: "..."}]
Output: articles/{article-slug}.md  (one file per article)

Robustness:
  - Idempotent: skips issues where any article file already exists for that slug
  - Validates Gemini response is parseable JSON before writing any files
  - Logs failures to pipeline/errors.json without aborting the run
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from pipeline.utils import (
    ARTICLES_DIR,
    RAW_TEXT_DIR,
    load_classified,
    log_error,
    make_article_slug,
    make_frontmatter,
    slug_to_raw_text_path,
)

GEMINI_MODEL = "gemini-2.5-flash"

SYSTEM_PROMPT = """You are processing a page-extracted text of one issue of "Informatics", the quarterly newsletter of India's National Informatics Centre (NIC).

The text below contains all pages of one issue, with page markers like:
=== PAGE 1 ===
...text...
=== PAGE 2 ===
...text...

Your task: identify every distinct article in this issue and return them as a JSON array.

Rules:
1. Each article has a clear headline / title. Use that as the title.
2. Articles often span multiple pages. Merge them — do not split one article into parts.
3. If you see "Contd. on page X" or "Contd. from page X" or "Continued on page X", merge those continuation fragments into the same article.
4. Include ALL pages an article appears on in the "pages" list.
5. "section" is the section label if present (e.g. "Cover Story", "Feature", "News", "Products", "Projects", "In the Limelight"). Use null if not clear.
6. "author" is the byline if present ("By ...", name at end of article). Use null if not found.
7. Clean up the body: remove page headers/footers, remove page markers, fix obvious OCR line breaks mid-sentence.
8. Preserve all substantive content — do not summarize.
9. Include ALL content blocks as separate articles — editorial notes, photo caption pages (Phototalk), quote collections (Quotable Quotes), letter columns, and advisory notices — even if they are short or appear to be filler. Every named section or block in the newsletter is an article.
10. Do NOT treat the table of contents as an article. Blocks titled "This Issue Brings To You", "Contents", "In This Issue", or similar index/listing pages are navigation aids, not articles — skip them entirely.
11. If page 1 contains a short cover teaser or preview blurb for a longer article that continues on a later page (e.g. "Cover Story" with a few sentences followed by "Contd. on page X"), do NOT create a separate article for the teaser. Instead, merge the teaser text into the full article body found on those later pages.

Return ONLY a valid JSON array, no other text. Schema:
[
  {
    "title": "string",
    "author": "string or null",
    "section": "string or null",
    "pages": [list of integers],
    "body": "full article text as a single string"
  }
]"""


BOILERPLATE_TITLES = {
    "this issue brings to you",
    "contents",
    "in this issue",
}


def filter_boilerplate(articles: list[dict]) -> list[dict]:
    """Drop articles whose titles are known newsletter boilerplate (mastheads, TOC, etc.)."""
    out = []
    for art in articles:
        title_lower = art.get("title", "").strip().lower()
        if title_lower in BOILERPLATE_TITLES:
            continue
        out.append(art)
    return out


def build_issue_text(pages: list[dict]) -> str:
    """Concatenate pages with markers for Gemini context."""
    parts = []
    for p in pages:
        parts.append(f"=== PAGE {p['page']} ===\n{p['text']}")
    return "\n\n".join(parts)


def parse_gemini_response(response_text: str) -> list[dict] | None:
    """Extract and validate JSON array from Gemini response. Returns None if invalid."""
    # Gemini sometimes wraps JSON in ```json ... ``` fences
    text = response_text.strip()
    fence_match = re.search(r"```(?:json)?\s*([\s\S]+?)\s*```", text)
    if fence_match:
        text = fence_match.group(1).strip()

    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        return None

    if not isinstance(data, list):
        return None

    required_keys = {"title", "pages", "body"}
    for item in data:
        if not isinstance(item, dict):
            return None
        if not required_keys.issubset(item.keys()):
            return None

    return data


def write_articles(articles: list[dict], issue_slug: str, issue_date: str) -> int:
    """Write one .md file per article. Returns count of files written."""
    ARTICLES_DIR.mkdir(exist_ok=True)
    written = 0
    seen_slugs: dict[str, int] = {}

    for article in articles:
        title = article.get("title", "Untitled").strip()
        author = article.get("author") or None
        section = article.get("section") or None
        pages = article.get("pages", [])
        body = article.get("body", "").strip()

        if not title or not body:
            continue

        slug = make_article_slug(title, issue_date)
        # Deduplicate slugs within this issue by appending a counter
        if slug in seen_slugs:
            seen_slugs[slug] += 1
            slug = f"{slug}-{seen_slugs[slug]}"
        else:
            seen_slugs[slug] = 1
        out_path = ARTICLES_DIR / f"{slug}.md"

        frontmatter = make_frontmatter(
            title=title,
            issue_date=issue_date,
            pages=pages,
            author=author,
            section=section,
        )

        content = frontmatter + f"## {title}\n\n{body}\n"

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(content)

        written += 1
        print(f"    → {out_path.name}  ({len(body):,} chars)")

    return written


def issue_already_processed(issue_slug: str) -> bool:
    """Return True if any article file exists that starts with this issue slug pattern."""
    # Articles are named {title-slug}-{issue-date-slug}.md
    # We can't know the exact filenames, so we track via a sentinel file
    sentinel = RAW_TEXT_DIR / f"{issue_slug}.segmented"
    return sentinel.exists()


def mark_issue_processed(issue_slug: str) -> None:
    sentinel = RAW_TEXT_DIR / f"{issue_slug}.segmented"
    sentinel.touch()


LARGE_ISSUE_CHAR_THRESHOLD = 200_000  # issues above this get split into halves
API_TIMEOUT = 360  # seconds per Gemini call


def _call_gemini(client, prompt: str, filename: str, step_label: str) -> str | None:
    """Call Gemini with retries. Returns response text or None on permanent failure."""
    from google.genai import types as genai_types

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt,
                config=genai_types.GenerateContentConfig(
                    max_output_tokens=65536,
                    http_options=genai_types.HttpOptions(timeout=API_TIMEOUT * 1000),
                ),
            )
            return response.text
        except Exception as e:
            err_str = str(e)
            if "401" in err_str or "403" in err_str or "API_KEY" in err_str:
                log_error(filename, step_label, f"Auth error (not retrying): {err_str}")
                return None
            if "429" in err_str or "RESOURCE_EXHAUSTED" in err_str:
                wait = 60 * (attempt + 1)
            elif "timeout" in err_str.lower() or "timed out" in err_str.lower() or "deadline" in err_str.lower():
                wait = 30 * (attempt + 1)
            else:
                wait = 10 * (attempt + 1)
            if attempt < 2:
                print(f"  API error (attempt {attempt + 1}/3), retrying in {wait}s: {err_str[:80]}")
                time.sleep(wait)
            else:
                log_error(filename, step_label, err_str)
                return None
    return None


def segment_issue(client, filename: str, slug: str, issue_date: str, dry_run: bool) -> bool:
    """Segment one issue. Returns True on success.

    Large issues (>200k chars) are split into two halves and processed separately,
    then merged, to avoid Gemini DEADLINE_EXCEEDED on very long newsletters.
    """
    if issue_already_processed(slug):
        print(f"  [skip] {filename} — already segmented")
        return True

    raw_path = slug_to_raw_text_path(slug)
    if not raw_path.exists():
        log_error(filename, "segment", f"raw_text/{slug}.json not found — run extraction first")
        return False

    with open(raw_path, encoding="utf-8") as f:
        pages = json.load(f)

    issue_text = build_issue_text(pages)

    if dry_run:
        full_prompt = f"{SYSTEM_PROMPT}\n\nISSUE DATE: {issue_date}\n\nTEXT:\n{issue_text}"
        print(f"  [dry-run] {filename} — prompt is {len(full_prompt):,} chars")
        print(f"  First 500 chars of issue text:\n{issue_text[:500]}\n")
        return True

    print(f"  {filename} ({len(pages)} pages, {len(issue_text):,} chars)...")

    if len(issue_text) > LARGE_ISSUE_CHAR_THRESHOLD:
        articles = _segment_large_issue(client, filename, pages, issue_date)
    else:
        full_prompt = f"{SYSTEM_PROMPT}\n\nISSUE DATE: {issue_date}\n\nTEXT:\n{issue_text}"
        response_text = _call_gemini(client, full_prompt, filename, "segment_gemini")
        if response_text is None:
            return False
        articles = parse_gemini_response(response_text)
        if articles is None:
            log_error(filename, "segment_parse", f"Invalid JSON. Raw: {response_text[:300]}")
            return False

    before = len(articles)
    articles = filter_boilerplate(articles)
    if len(articles) < before:
        print(f"  Filtered {before - len(articles)} boilerplate article(s)")
    print(f"  Found {len(articles)} articles:")
    written = write_articles(articles, slug, issue_date)

    if written > 0:
        mark_issue_processed(slug)

    return written > 0


def _segment_large_issue(client, filename: str, pages: list[dict], issue_date: str) -> list[dict]:
    """Split a large issue into two halves, segment each, merge results."""
    mid = len(pages) // 2
    halves = [pages[:mid], pages[mid:]]
    all_articles: list[dict] = []

    for i, half_pages in enumerate(halves):
        label = f"part {i+1}/2"
        half_text = build_issue_text(half_pages)
        prompt = f"{SYSTEM_PROMPT}\n\nISSUE DATE: {issue_date}\n\nNOTE: This is {label} of the issue (pages {half_pages[0]['page']}–{half_pages[-1]['page']}).\n\nTEXT:\n{half_text}"
        print(f"  {filename} — sending {label} ({len(half_pages)} pages, {len(half_text):,} chars)...")
        response_text = _call_gemini(client, prompt, filename, f"segment_gemini_{label.replace(' ', '_')}")
        if response_text is None:
            print(f"  {filename} — {label} failed, skipping")
            continue
        articles = parse_gemini_response(response_text)
        if articles is None:
            log_error(filename, f"segment_parse_{label}", f"Invalid JSON. Raw: {response_text[:300]}")
            continue
        print(f"  {filename} — {label}: {len(articles)} articles")
        all_articles.extend(articles)

    return all_articles


def slug_to_issue_date(filename: str) -> str:
    """Derive a human-readable issue date from the PDF filename.

    "April-2003.pdf" → "April 2003"
    "Apr-1995.pdf"   → "April 1995"  (expand abbreviation)
    "Jan_2010.pdf"   → "January 2010"
    """
    stem = Path(filename).stem
    # Handle files with no separator between month and year: "October1997" → "October-1997"
    stem = re.sub(r"([A-Za-z]+)(\d{4})", r"\1-\2", stem)
    # Split on - or _
    parts = re.split(r"[-_]", stem)
    if len(parts) < 2:
        return stem

    month_raw = parts[0]
    year = parts[-1]

    abbreviations = {
        "Jan": "January", "Feb": "February", "Mar": "March",
        "Apr": "April", "Jun": "June", "Jul": "July",
        "Aug": "August", "Sep": "September", "Oct": "October",
        "Nov": "November", "Dec": "December",
    }
    month = abbreviations.get(month_raw, month_raw)
    return f"{month} {year}"


def main() -> None:
    parser = argparse.ArgumentParser(description="Segment articles using Gemini")
    parser.add_argument(
        "--files", nargs="+", metavar="FILENAME",
        help="Process specific files only (pilot mode)"
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Show prompt structure — do not call Gemini API"
    )
    args = parser.parse_args()

    classified = load_classified()
    if not classified:
        print("classified.json is empty. Run classify_pdfs.py first.")
        sys.exit(1)

    if args.files:
        target_names = set(args.files)
        entries = [e for e in classified if e["filename"] in target_names]
    else:
        entries = classified

    # Only process issues that have raw_text available
    entries = [e for e in entries if slug_to_raw_text_path(e["slug"]).exists()]
    print(f"Segmenting {len(entries)} issue(s)...\n")

    if not entries:
        print("No raw_text files found. Run extraction scripts first.")
        sys.exit(1)

    client = None
    if not args.dry_run:
        from dotenv import load_dotenv
        from google import genai

        load_dotenv()
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            print("ERROR: GEMINI_API_KEY not set in .env")
            sys.exit(1)

        client = genai.Client(api_key=api_key)

    ok = failed = 0
    counter_lock = threading.Lock()
    MAX_WORKERS = 1 if args.dry_run else 5

    def _process(entry: dict) -> bool:
        issue_date = slug_to_issue_date(entry["filename"])
        try:
            return segment_issue(client, entry["filename"], entry["slug"], issue_date, args.dry_run)
        except Exception as e:
            log_error(entry["filename"], "segment_thread", str(e))
            return False

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(_process, entry): entry for entry in entries}
        for future in as_completed(futures):
            entry = futures[future]
            try:
                success = future.result()
            except Exception as e:
                log_error(entry["filename"], "segment_future", str(e))
                success = False
            with counter_lock:
                if success:
                    ok += 1
                else:
                    failed += 1

    print(f"\nDone: {ok} succeeded, {failed} failed.")
    if failed:
        print("See pipeline/errors.json for details.")


if __name__ == "__main__":
    main()
