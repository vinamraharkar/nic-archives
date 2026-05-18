#!/usr/bin/env python3
"""
Render PDF pages as JPEG images for the "View original page" feature.

Usage:
    python pipeline/extract_page_images.py                        # all PDFs in classified.json
    python pipeline/extract_page_images.py --files Apr-1995.pdf   # pilot mode

Input:  classified.json  +  articles/*.md  (to resolve issue_date per PDF)
Output: docs/pages/{issue_slug}/page-{n}.jpg

Resolution: 150 DPI  (good balance — A4 page ≈ 200–400 KB as JPEG)

Idempotent: skips PDFs whose docs/pages/{issue_slug}/ directory already exists.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from pipeline.utils import ARCHIVES_DIR, ARTICLES_DIR, load_classified

BASE_DIR = Path(__file__).parent.parent
DOCS_PAGES_DIR = BASE_DIR / "docs" / "pages"

DPI = 150

# Abbreviated month → full month (lowercase)
MONTH_ABBREVS: dict[str, str] = {
    "jan": "january", "feb": "february", "mar": "march", "apr": "april",
    "may": "may", "jun": "june", "jul": "july", "aug": "august",
    "sep": "september", "oct": "october", "nov": "november", "dec": "december",
}


def make_issue_slug(issue_date: str) -> str:
    """'April 1995' → 'april-1995'"""
    slug = issue_date.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    return slug.strip("-")


def discover_issue_dates() -> list[str]:
    """Return all unique issue_date values seen across articles/*.md."""
    seen: set[str] = set()
    for md_path in ARTICLES_DIR.glob("*.md"):
        text = md_path.read_text(encoding="utf-8")
        m = re.search(r'^issue_date:\s*"([^"]+)"', text, re.MULTILINE)
        if m:
            seen.add(m.group(1))
        else:
            # also check legacy `date:` field
            m2 = re.search(r'^date:\s*"([^"]+)"', text, re.MULTILINE)
            if m2:
                seen.add(m2.group(1))
    return sorted(seen)


def match_pdf_to_issue_date(pdf_slug: str, issue_dates: list[str]) -> str | None:
    """
    Map a filename slug (e.g. 'apr-1995') to an issue_date string ('April 1995').

    Strategy: extract year and month tokens from slug, match against issue_dates
    by year and (abbreviated or full) month name.
    """
    parts = pdf_slug.replace("-", " ").split()
    year_token: str | None = None
    month_token: str | None = None  # full lowercase month name

    for part in parts:
        if part.isdigit() and len(part) == 4:
            year_token = part
        elif part in MONTH_ABBREVS:
            month_token = MONTH_ABBREVS[part]
        elif part in MONTH_ABBREVS.values():
            month_token = part

    for issue_date in issue_dates:
        lower = issue_date.lower()
        year_ok = (year_token is None) or (year_token in lower)
        month_ok = (month_token is None) or (month_token in lower)
        if year_ok and month_ok:
            return issue_date

    return None


def render_pages(pdf_path: Path, out_dir: Path) -> int:
    """
    Render all pages of pdf_path as JPEGs into out_dir.
    Returns number of pages rendered, or 0 on failure.
    Uses pdftoppm (poppler), which is already required by this project.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    prefix = str(out_dir / "page")

    try:
        result = subprocess.run(
            [
                "pdftoppm",
                "-jpeg",
                "-r", str(DPI),
                str(pdf_path),
                prefix,
            ],
            capture_output=True,
            text=True,
            timeout=300,
        )
    except FileNotFoundError:
        print("ERROR: pdftoppm not found. Install with: brew install poppler")
        sys.exit(1)
    except subprocess.TimeoutExpired:
        print(f"  TIMEOUT rendering {pdf_path.name}")
        return 0

    if result.returncode != 0:
        print(f"  pdftoppm error: {result.stderr.strip()}")
        return 0

    # pdftoppm names files: page-001.jpg, page-002.jpg ...
    # Rename to page-1.jpg, page-2.jpg, ... for cleaner URLs
    rendered = sorted(out_dir.glob("page-*.jpg"))
    for img_path in rendered:
        # Extract number from e.g. "page-001.jpg" → 1
        m = re.search(r"page-0*(\d+)\.jpg$", img_path.name)
        if m:
            n = int(m.group(1))
            target = out_dir / f"page-{n}.jpg"
            if img_path.name != target.name:
                img_path.rename(target)

    return len(rendered)


def process_pdf(filename: str, pdf_slug: str, issue_dates: list[str]) -> bool:
    """Render one PDF's pages. Returns True on success."""
    issue_date = match_pdf_to_issue_date(pdf_slug, issue_dates)
    if not issue_date:
        print(f"  [skip] {filename} — cannot match to any issue_date in articles/")
        return False

    issue_slug = make_issue_slug(issue_date)
    out_dir = DOCS_PAGES_DIR / issue_slug

    if out_dir.exists() and any(out_dir.glob("page-*.jpg")):
        print(f"  [skip] {filename} — {out_dir.name}/ already has images")
        return True

    pdf_path = ARCHIVES_DIR / filename
    if not pdf_path.exists():
        print(f"  [skip] {filename} — PDF not found at {pdf_path}")
        return False

    print(f"  {filename} → docs/pages/{issue_slug}/", end=" ", flush=True)
    count = render_pages(pdf_path, out_dir)
    if count:
        print(f"({count} pages at {DPI} DPI)")
        return True
    else:
        # Clean up empty dir on failure
        if out_dir.exists() and not any(out_dir.iterdir()):
            out_dir.rmdir()
        return False


def main() -> None:
    parser = argparse.ArgumentParser(description="Render PDF pages as JPEG images")
    parser.add_argument(
        "--files", nargs="+", metavar="FILENAME",
        help="Process specific files only (pilot mode)"
    )
    args = parser.parse_args()

    classified = load_classified()
    if not classified:
        print("classified.json is empty. Run classify_pdfs.py first.")
        sys.exit(1)

    if args.files:
        target_names = set(args.files)
        entries = [e for e in classified if e["filename"] in target_names]
        not_found = target_names - {e["filename"] for e in entries}
        if not_found:
            print(f"WARNING: not in classified.json: {not_found}")
    else:
        entries = list(classified)

    issue_dates = discover_issue_dates()
    if not issue_dates:
        print("No issue_dates found in articles/. Run segment_articles.py first.")
        sys.exit(1)

    print(f"Found {len(issue_dates)} unique issue_dates: {issue_dates}")
    print(f"Rendering {len(entries)} PDF(s) at {DPI} DPI...\n")

    DOCS_PAGES_DIR.mkdir(parents=True, exist_ok=True)

    ok = failed = 0
    counter_lock = threading.Lock()

    def _process(entry: dict) -> bool:
        return process_pdf(entry["filename"], entry["slug"], issue_dates)

    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(_process, e): e for e in entries}
        for future in as_completed(futures):
            try:
                success = future.result()
            except Exception as exc:
                print(f"  ERROR: {futures[future]['filename']}: {exc}")
                success = False
            with counter_lock:
                if success:
                    ok += 1
                else:
                    failed += 1

    print(f"\nDone: {ok} succeeded, {failed} failed.")
    print("Next: python generate_site.py  (to pick up page images)")


if __name__ == "__main__":
    main()
