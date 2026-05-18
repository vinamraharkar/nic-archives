#!/usr/bin/env python3
"""
Use Gemini Vision to detect precise article bounding boxes on page scan images.

Detects ONE article at a time using the article title as a text anchor.
Uses Gemini's normalized 0-1000 coordinate system for better accuracy.

Saves docs/pages/{issue_slug}/coords.json:
  {
    "article-slug": {
      "4": {"y_start": 118, "y_end": 1755, "x_start": 0, "x_end": 414,
            "img_width": 1242, "img_height": 1755}
    }
  }

Usage:
    python pipeline/detect_article_coords_gemini.py --issue october-1992
    python pipeline/detect_article_coords_gemini.py --issue october-1992 --force
    python pipeline/detect_article_coords_gemini.py --issue october-1992 --page 3
    python pipeline/detect_article_coords_gemini.py --issue october-1992 --slug keeping-monkeys-at-bay-october-1992
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from pipeline.utils import ARTICLES_DIR

BASE_DIR = Path(__file__).parent.parent
DOCS_PAGES_DIR = BASE_DIR / "docs" / "pages"

MAX_RETRIES = 3


# ── Frontmatter helpers ────────────────────────────────────────────────────────

def parse_article_meta(md_path: Path) -> dict | None:
    """Return {slug, title, issue_date, issue_slug, pages, body} or None."""
    text = md_path.read_text(encoding="utf-8")
    m_title = re.search(r'^title:\s*"([^"]+)"', text, re.MULTILINE)
    m_date = re.search(r'^issue_date:\s*"([^"]+)"', text, re.MULTILINE)
    m_pages = re.search(r'^pages:\s*\[([^\]]+)\]', text, re.MULTILINE)
    if not (m_title and m_date and m_pages):
        return None
    raw_pages = [p.strip() for p in m_pages.group(1).split(",") if p.strip().isdigit()]
    if not raw_pages:
        return None
    issue_date = m_date.group(1)
    issue_slug = re.sub(r"[^a-z0-9]+", "-", issue_date.lower()).strip("-")

    # Extract body text (after the second ---) for use as text anchor
    parts = text.split("---")
    body = parts[2].strip() if len(parts) >= 3 else ""
    # Take first 300 chars of body as a text snippet for matching
    body_snippet = body[:300].strip()

    return {
        "slug": md_path.stem,
        "title": m_title.group(1),
        "issue_date": issue_date,
        "issue_slug": issue_slug,
        "pages": [int(p) for p in raw_pages],
        "body_snippet": body_snippet,
    }


def load_issue_articles(issue_slug: str) -> list[dict]:
    """Return all article metas for the given issue_slug."""
    arts = []
    for md in ARTICLES_DIR.glob("*.md"):
        meta = parse_article_meta(md)
        if meta and meta["issue_slug"] == issue_slug:
            arts.append(meta)
    return arts


# ── Gemini Vision detection ────────────────────────────────────────────────────

def image_to_base64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode("utf-8")


def detect_one_article(
    client,
    page_n: int,
    page_path: Path,
    article: dict,
    img_w: int,
    img_h: int,
) -> dict | None:
    """
    Ask Gemini to find ONE article's bounding box on the page.

    Uses normalized 0-1000 coordinates (Gemini's native spatial format).
    Returns {y_start, y_end, x_start, x_end, img_width, img_height} or None.
    """
    from google.genai import types as gai_types
    from google import genai as gai

    title = article["title"]
    slug = article["slug"]
    body_snippet = article.get("body_snippet", "")

    # Trim body snippet to first few lines for context
    snippet_lines = [l for l in body_snippet.splitlines() if l.strip()][:4]
    snippet_hint = " ".join(snippet_lines)[:200] if snippet_lines else ""

    prompt = f"""You are analyzing page {page_n} of a scanned NIC Informatics newsletter.
Image dimensions: {img_w} x {img_h} pixels.

Find the article with headline: "{title.upper()}"
(It may also appear as "{title}" with mixed case.)
{"First lines of this article: " + snippet_hint if snippet_hint else ""}

Return the TIGHTEST bounding box that contains ONLY this article:
- y_start: pixel row of the TOP of the headline (not of neighboring articles above it)
- y_end: pixel row of the LAST line of this article's text (not the next article below)
- x_start: leftmost pixel of the column(s) this article occupies
- x_end: rightmost pixel of the column(s) this article occupies
- Include any photos or images that belong to this article within the box

Use PIXEL coordinates in the {img_w}x{img_h} image (NOT normalized).

If the article is not visible on this page, return: {{"not_found": true}}

Return ONLY valid JSON, no other text:
{{"y_start": <int>, "y_end": <int>, "x_start": <int>, "x_end": <int>}}"""

    img_bytes = page_path.read_bytes()

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

            # Strip markdown code fences if present
            raw = re.sub(r"^```(?:json)?\s*", "", raw)
            raw = re.sub(r"\s*```$", "", raw)

            parsed = json.loads(raw)

            if parsed.get("not_found"):
                return None

            x0 = max(0, int(parsed["x_start"]))
            y0 = max(0, int(parsed["y_start"]))
            x1 = min(img_w, int(parsed["x_end"]))
            y1 = min(img_h, int(parsed["y_end"]))

            if y1 <= y0 or x1 <= x0:
                print(f"      [invalid bbox] y={y0}→{y1} x={x0}→{x1} — skipping")
                return None

            return {
                "y_start": y0,
                "y_end": y1,
                "x_start": x0,
                "x_end": x1,
                "img_width": img_w,
                "img_height": img_h,
            }

        except json.JSONDecodeError as e:
            if attempt < MAX_RETRIES:
                print(f"      [retry {attempt}] JSON parse error: {e} — retrying...")
                time.sleep(2 ** attempt)
            else:
                print(f"      FAILED to parse JSON for {slug}")
                return None

        except Exception as e:
            err_str = str(e)
            if "429" in err_str or "RESOURCE_EXHAUSTED" in err_str:
                wait = 60 * attempt
            else:
                wait = 2 ** attempt
            if attempt < MAX_RETRIES:
                print(f"      [retry {attempt}] API error: {e} — retrying in {wait}s")
                time.sleep(wait)
            else:
                print(f"      FAILED: {e}")
                return None

    return None


def detect_coords_for_page(
    client,
    page_n: int,
    page_path: Path,
    articles_on_page: list[dict],
) -> dict[str, dict | None]:
    """
    Detect bounding boxes for each article on the page — one at a time.
    Returns {slug: bbox_dict | None}
    """
    from PIL import Image as PILImage
    img = PILImage.open(page_path)
    img_w, img_h = img.size

    results: dict[str, dict | None] = {}

    for art in articles_on_page:
        slug = art["slug"]
        print(f"      Detecting: {art['title'][:60]}...")

        bbox = detect_one_article(client, page_n, page_path, art, img_w, img_h)

        if bbox:
            results[slug] = bbox
            print(f"        → y={bbox['y_start']}→{bbox['y_end']} x={bbox['x_start']}→{bbox['x_end']}")
        else:
            results[slug] = None
            print(f"        → NOT FOUND")

        # Small delay between articles to avoid rate limiting
        time.sleep(0.5)

    return results


# ── Issue processing ───────────────────────────────────────────────────────────

def process_issue(
    client,
    issue_slug: str,
    force: bool = False,
    only_page: int | None = None,
    only_slug: str | None = None,
) -> int:
    """
    Process all pages for an issue using Gemini Vision.
    Saves coords.json. Returns number of articles with coords found.
    """
    articles = load_issue_articles(issue_slug)
    if not articles:
        print(f"  No articles found for {issue_slug}")
        return 0

    page_dir = DOCS_PAGES_DIR / issue_slug
    if not page_dir.exists():
        print(f"  No page images at {page_dir} — run extract_page_images.py first")
        return 0

    coords_path = page_dir / "coords.json"

    # Load existing coords to merge into (unless --force)
    if coords_path.exists() and not force:
        existing = json.loads(coords_path.read_text())
    else:
        existing = {}

    # Filter articles if --slug specified
    if only_slug:
        articles = [a for a in articles if a["slug"] == only_slug]
        if not articles:
            print(f"  No article found with slug '{only_slug}'")
            return 0

    print(f"\n{issue_slug}  ({len(articles)} articles to process)")

    # Group articles by page
    page_to_articles: dict[int, list[dict]] = {}
    for art in articles:
        for pg in art["pages"]:
            page_to_articles.setdefault(pg, []).append(art)

    all_coords: dict[str, dict[str, dict]] = dict(existing)

    pages_to_process = sorted(page_to_articles.keys())
    if only_page is not None:
        pages_to_process = [p for p in pages_to_process if p == only_page]

    for page_n in pages_to_process:
        page_path = page_dir / f"page-{page_n}.jpg"
        if not page_path.exists():
            print(f"    Page {page_n}: image not found, skipping")
            continue

        arts_on_page = page_to_articles[page_n]

        # Skip articles that already have coords for this page (unless --force or --slug)
        if not force and not only_slug:
            arts_on_page = [
                a for a in arts_on_page
                if str(page_n) not in all_coords.get(a["slug"], {})
            ]
            if not arts_on_page:
                print(f"\n  Page {page_n}: all articles already have coords, skipping")
                continue

        print(f"\n  Page {page_n} ({len(arts_on_page)} articles)...")

        page_results = detect_coords_for_page(client, page_n, page_path, arts_on_page)

        for slug, bbox in page_results.items():
            if bbox is not None:
                all_coords.setdefault(slug, {})[str(page_n)] = bbox

        # Save after each page so partial results are preserved
        coords_path.write_text(json.dumps(all_coords, indent=2))

    found = sum(1 for pages in all_coords.values() if pages)
    print(f"\n  Saved coords.json ({found} articles with coordinates)")
    return found


def discover_all_slugs() -> list[str]:
    """Return all issue slugs that have page images but incomplete coords."""
    slugs = []
    if not DOCS_PAGES_DIR.exists():
        return slugs
    for issue_dir in sorted(DOCS_PAGES_DIR.iterdir()):
        if not issue_dir.is_dir():
            continue
        if not any(issue_dir.glob("page-*.jpg")):
            continue
        coords_path = issue_dir / "coords.json"
        # Include if no coords yet, or coords exist (they will be merged/skipped per-article)
        slugs.append(issue_dir.name)
    return slugs


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Use Gemini Vision to detect article bounding boxes (one at a time)"
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--issue", metavar="SLUG",
                      help="Issue slug to process (e.g. october-1992)")
    mode.add_argument("--all", action="store_true",
                      help="Process all issues that have page images (5 parallel workers)")
    parser.add_argument("--force", action="store_true",
                        help="Re-detect all pages even if coords exist")
    parser.add_argument("--page", type=int, metavar="N",
                        help="Process only this page number (single --issue mode only)")
    parser.add_argument("--slug", metavar="SLUG",
                        help="Re-detect only this article slug (single --issue mode only)")
    args = parser.parse_args()

    from dotenv import load_dotenv
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("ERROR: GEMINI_API_KEY not set in .env")
        sys.exit(1)

    from google import genai as gai
    client = gai.Client(api_key=api_key)

    if args.issue:
        total = process_issue(
            client,
            args.issue,
            force=args.force,
            only_page=args.page,
            only_slug=args.slug,
        )
        print(f"\nDone: {total} articles with bounding boxes saved.")
        print("Next: python generate_site.py")
        return

    # --all mode
    slugs = discover_all_slugs()
    if not slugs:
        print("No issues with page images found. Run extract_page_images.py first.")
        sys.exit(1)

    print(f"Processing {len(slugs)} issues with 5 parallel workers...\n")

    ok = failed = 0
    counter_lock = threading.Lock()

    def _process(slug: str) -> int:
        try:
            return process_issue(client, slug, force=args.force)
        except Exception as exc:
            print(f"  ERROR [{slug}]: {exc}")
            return 0

    with ThreadPoolExecutor(max_workers=77) as executor:
        futures = {executor.submit(_process, slug): slug for slug in slugs}
        for future in as_completed(futures):
            slug = futures[future]
            try:
                count = future.result()
                with counter_lock:
                    if count > 0:
                        ok += 1
                    else:
                        failed += 1
            except Exception as exc:
                print(f"  ERROR [{slug}]: {exc}")
                with counter_lock:
                    failed += 1

    print(f"\nDone: {ok} issues succeeded, {failed} issues failed.")
    print("Next: python generate_site.py")


if __name__ == "__main__":
    main()
