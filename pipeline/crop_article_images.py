#!/usr/bin/env python3
"""
Detect per-article bounding boxes on scanned page images using tesseract.

Saves docs/pages/{issue_slug}/coords.json:
  {
    "article-slug": {
      "4": {"y_start": 118, "y_end": 1755, "x_start": 0, "x_end": 414,
            "img_width": 1242, "img_height": 1755}
    }
  }

generate_site.py reads coords.json and renders a CSS highlight overlay on
the full-page image so only the article's column is highlighted.

Usage:
    python pipeline/crop_article_images.py                      # all issues
    python pipeline/crop_article_images.py --issue october-1992 # one issue
    python pipeline/crop_article_images.py --issue october-1992 --force
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from pipeline.utils import ARTICLES_DIR

try:
    import pytesseract
    from PIL import Image
    pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"
except ImportError:
    print("ERROR: pip install pytesseract Pillow")
    sys.exit(1)

BASE_DIR = Path(__file__).parent.parent
DOCS_PAGES_DIR = BASE_DIR / "docs" / "pages"

# Column detection parameters
BUCKET_PX = 5          # x-histogram bucket size in pixels
MIN_GUTTER_PX = 15     # minimum gap width to count as a column gutter
MIN_COLUMN_PX = 100    # minimum column width to count as a column
COL_PADDING_PX = 8     # extra pixels added to each side of detected column

# Headline matching
HEADLINE_THRESHOLD = 0.65   # word-overlap fraction to accept a title match
HEADLINE_MARGIN_PX = 20     # pixels above the headline to include in highlight


# ── Frontmatter helpers ────────────────────────────────────────────────────────

def parse_article_meta(md_path: Path) -> dict | None:
    """Return {slug, title, issue_date, issue_slug, pages} or None."""
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
    return {
        "slug": md_path.stem,
        "title": m_title.group(1),
        "issue_date": issue_date,
        "issue_slug": issue_slug,
        "pages": [int(p) for p in raw_pages],
    }


def load_issue_articles(issue_slug: str) -> list[dict]:
    """Return all article metas for the given issue_slug."""
    arts = []
    for md in ARTICLES_DIR.glob("*.md"):
        meta = parse_article_meta(md)
        if meta and meta["issue_slug"] == issue_slug:
            arts.append(meta)
    return arts


# ── Text helpers ───────────────────────────────────────────────────────────────

def normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9 ]", " ", text.lower())


def words_to_lines(data: dict) -> list[dict]:
    """
    Group tesseract words into lines by approximate y-position.
    Each line: {top, height, text, x_start, x_end}
    """
    buckets: dict[int, dict] = {}
    for i in range(len(data["text"])):
        word = data["text"][i].strip()
        if not word or int(data["conf"][i]) < 20:
            continue
        top = int(data["top"][i])
        h = int(data["height"][i])
        left = int(data["left"][i])
        width = int(data["width"][i])
        key = (top // 12) * 12
        if key not in buckets:
            buckets[key] = {
                "top": top, "height": h, "words": [],
                "x_start": left, "x_end": left + width,
            }
        buckets[key]["words"].append(word)
        buckets[key]["height"] = max(buckets[key]["height"], h)
        buckets[key]["x_start"] = min(buckets[key]["x_start"], left)
        buckets[key]["x_end"] = max(buckets[key]["x_end"], left + width)
    lines = sorted(buckets.values(), key=lambda l: l["top"])
    for line in lines:
        line["text"] = " ".join(line["words"])
    return lines


# ── Column detection ───────────────────────────────────────────────────────────

def detect_columns(data: dict, img_width: int) -> list[tuple[int, int]]:
    """
    Find column x-ranges by locating vertical whitespace gutters.

    Strategy: build a histogram of word LEFT positions (where words start).
    Columns produce dense clusters; gutters between columns have near-zero
    density. Find contiguous zero-density runs >= MIN_GUTTER_PX wide.

    Returns list of (x_start, x_end) sorted left-to-right.
    Falls back to [(0, img_width)] if no multi-column structure found.
    """
    n_buckets = (img_width + BUCKET_PX - 1) // BUCKET_PX
    counts = [0] * n_buckets

    for i in range(len(data["text"])):
        if not data["text"][i].strip() or int(data["conf"][i]) < 20:
            continue
        left = int(data["left"][i])
        b = min(left // BUCKET_PX, n_buckets - 1)
        counts[b] += 1

    # Find runs of zero buckets that are long enough to be gutters
    min_gutter_buckets = max(1, MIN_GUTTER_PX // BUCKET_PX)
    min_col_buckets = max(1, MIN_COLUMN_PX // BUCKET_PX)

    gaps: list[tuple[int, int]] = []
    in_gap = True   # treat left edge as a gap
    gap_start = 0

    for b in range(n_buckets):
        if counts[b] == 0:
            if not in_gap:
                in_gap = True
                gap_start = b
        else:
            if in_gap:
                if b - gap_start >= min_gutter_buckets:
                    gaps.append((gap_start * BUCKET_PX, b * BUCKET_PX))
                in_gap = False

    # Right edge
    if in_gap and n_buckets - gap_start >= min_gutter_buckets:
        gaps.append((gap_start * BUCKET_PX, img_width))
    else:
        gaps.append((img_width, img_width))   # sentinel

    # Add left sentinel
    all_gaps = [(0, 0)] + gaps

    # Build columns from gap pairs
    columns: list[tuple[int, int]] = []
    for j in range(len(all_gaps) - 1):
        col_start = all_gaps[j][1]
        col_end = all_gaps[j + 1][0]
        if col_end - col_start >= min_col_buckets * BUCKET_PX:
            columns.append((col_start, col_end))

    return columns if len(columns) >= 2 else [(0, img_width)]


def column_for_x(x: int, columns: list[tuple[int, int]]) -> tuple[int, int]:
    """Return the column (x_start, x_end) that contains x, or full width."""
    for col_start, col_end in columns:
        if col_start <= x < col_end:
            return (col_start, col_end)
    # x is in a gutter — return nearest column
    best = min(columns, key=lambda c: min(abs(x - c[0]), abs(x - c[1])))
    return best


# ── Headline detection ─────────────────────────────────────────────────────────

def title_match_score(candidate: str, title: str) -> float:
    norm_c = normalize(candidate)
    norm_t = normalize(title)
    title_words = [w for w in norm_t.split() if len(w) > 2]
    if not title_words:
        return 0.0
    cand_words = set(norm_c.split())
    hits = sum(1 for w in title_words if w in cand_words)
    return hits / len(title_words)


def find_title_location(
    lines: list[dict], title: str, threshold: float = HEADLINE_THRESHOLD
) -> tuple[int, int, int] | None:
    """
    Find the title on the page. Returns (y, x_start, x_end) of the best
    matching line (or two-line combination), or None if no match found.
    """
    best_score = 0.0
    best: tuple[int, int, int] | None = None

    for i, line in enumerate(lines):
        score = title_match_score(line["text"], title)
        if score > best_score:
            best_score = score
            best = (line["top"], line["x_start"], line["x_end"])

        if i + 1 < len(lines):
            combined = line["text"] + " " + lines[i + 1]["text"]
            score2 = title_match_score(combined, title)
            if score2 > best_score:
                best_score = score2
                # Use the union x-range of both lines
                best = (
                    line["top"],
                    min(line["x_start"], lines[i + 1]["x_start"]),
                    max(line["x_end"], lines[i + 1]["x_end"]),
                )

    return best if best_score >= threshold else None


# ── Per-page processing ────────────────────────────────────────────────────────

def process_page(
    page_n: int,
    issue_slug: str,
    articles_on_this_page: list[dict],
) -> dict[str, dict | None]:
    """
    Detect bounding boxes for all articles on page_n.
    Returns {article_slug: {y_start, y_end, x_start, x_end, img_width, img_height} | None}
    """
    page_path = DOCS_PAGES_DIR / issue_slug / f"page-{page_n}.jpg"
    if not page_path.exists():
        return {art["slug"]: None for art in articles_on_this_page}

    img = Image.open(page_path)
    img_w, img_h = img.width, img.height

    print(f"    OCR page {page_n} ({img_w}×{img_h})...", end=" ", flush=True)
    data = pytesseract.image_to_data(
        img, output_type=pytesseract.Output.DICT, config="--psm 1"
    )
    lines = words_to_lines(data)
    print(f"{len(lines)} lines")

    # Detect column layout for this page
    columns = detect_columns(data, img_w)
    print(f"      Columns detected: {columns}")

    # Find each article's title location (y + x)
    located: list[tuple[int, int, int, str]] = []   # (y, x_start, x_end, slug)
    for art in articles_on_this_page:
        loc = find_title_location(lines, art["title"])
        if loc is not None:
            y, x_s, x_e = loc
            located.append((y, x_s, x_e, art["slug"]))

    located.sort(key=lambda t: t[0])   # sort by y
    print(f"      Found {len(located)}/{len(articles_on_this_page)} titles: "
          + ", ".join(slug[:30] for _, _, _, slug in located))

    results: dict[str, dict | None] = {}

    for art in articles_on_this_page:
        art_loc = next((t for t in located if t[3] == art["slug"]), None)

        if art_loc is not None:
            y_title, x_title_s, x_title_e, _ = art_loc

            # Determine the column this title lives in
            x_mid = (x_title_s + x_title_e) // 2
            col_x_start, col_x_end = column_for_x(x_mid, columns)

            # Add padding and clamp to image bounds
            x_start = max(0, col_x_start - COL_PADDING_PX)
            x_end = min(img_w, col_x_end + COL_PADDING_PX)

            # y ends at the next article's title on this page (same column),
            # or the page bottom
            next_y = next(
                (y for y, _, _, _ in located if y > y_title),
                img_h
            )
            y_start = max(0, y_title - HEADLINE_MARGIN_PX)
            y_end = next_y

            results[art["slug"]] = {
                "y_start": y_start, "y_end": y_end,
                "x_start": x_start, "x_end": x_end,
                "img_width": img_w, "img_height": img_h,
            }
            print(f"      [y={y_start}→{y_end} x={x_start}→{x_end}] {art['slug'][:50]}")

        else:
            # Continuation page — article flows from a previous page.
            # Use full column width and stop at first found title.
            first_other_y = next(
                (y for y, _, _, slug in located if slug != art["slug"]),
                img_h
            )
            # Use full page width since we don't know the column
            results[art["slug"]] = {
                "y_start": 0, "y_end": first_other_y,
                "x_start": 0, "x_end": img_w,
                "img_width": img_w, "img_height": img_h,
            }
            print(f"      [continuation y=0→{first_other_y} full-width] {art['slug'][:50]}")

    return results


def process_issue(issue_slug: str, force: bool = False) -> int:
    """
    Process all pages for an issue. Saves coords.json.
    Returns number of articles with coords found.
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
    if coords_path.exists() and not force:
        print(f"  {issue_slug}: coords.json already exists (use --force to redo)")
        return 0

    print(f"\n{issue_slug}  ({len(articles)} articles)")

    # Group articles by page
    page_to_articles: dict[int, list[dict]] = {}
    for art in articles:
        for pg in art["pages"]:
            page_to_articles.setdefault(pg, []).append(art)

    # Accumulate coords: {article_slug: {page_n: {...}}}
    all_coords: dict[str, dict[str, dict]] = {}

    for page_n in sorted(page_to_articles):
        page_results = process_page(page_n, issue_slug, page_to_articles[page_n])
        for slug, bbox in page_results.items():
            if bbox is not None:
                all_coords.setdefault(slug, {})[str(page_n)] = bbox

    coords_path.write_text(json.dumps(all_coords, indent=2))
    found = sum(1 for pages in all_coords.values() if pages)
    print(f"  Saved coords.json ({found} articles with coordinates)")
    return found


def main() -> None:
    parser = argparse.ArgumentParser(description="Detect article bounding boxes on page scans")
    parser.add_argument("--issue", metavar="SLUG", help="Process one issue (e.g. october-1992)")
    parser.add_argument("--force", action="store_true", help="Re-detect even if coords.json exists")
    args = parser.parse_args()

    if args.issue:
        issue_slugs = [args.issue]
    else:
        issue_slugs = sorted(p.name for p in DOCS_PAGES_DIR.iterdir() if p.is_dir())

    total = 0
    for slug in issue_slugs:
        total += process_issue(slug, force=args.force)

    print(f"\nDone: {total} articles with bounding boxes saved.")
    print("Next: python generate_site.py")


if __name__ == "__main__":
    main()
