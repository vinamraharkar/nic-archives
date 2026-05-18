#!/usr/bin/env python3
"""
Detect article layout regions on scanned newsletter pages using Gemini Vision.

Approach:
  1. Per page: send image to Gemini, ask for ALL article regions at once
     using Gemini's native 0-1000 normalized coordinate format.
  2. Store raw detected regions in docs/pages/{slug}/layout.json.
  3. Match detected regions to known article slugs by title similarity.
  4. Merge per-page matches into coords.json (same format as before,
     so generate_site.py works unchanged).

Why this is better than detect_article_coords_gemini.py:
  - Detects all articles simultaneously → Gemini knows where each ends
  - Uses 0-1000 normalized coords (Gemini's native spatial format)
  - Separates spatial detection from semantic title matching

Usage:
    python pipeline/detect_layout.py --issue october-1992
    python pipeline/detect_layout.py --issue october-1992 --page 3
    python pipeline/detect_layout.py --issue october-1992 --force
    python pipeline/detect_layout.py --issue october-1992 --poc
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

from pipeline.utils import ARTICLES_DIR

BASE_DIR = Path(__file__).parent.parent
DOCS_PAGES_DIR = BASE_DIR / "docs" / "pages"

MAX_RETRIES = 3

PAGE_PROMPT = """\
You are analyzing a scanned page from an Indian government newsletter called "Informatics" (NIC, 1990s–2000s).

Detect EVERY distinct article on this page. Articles are separated by headlines (large/bold text), horizontal rules, or whitespace.

For each article, return:
- "title": the exact headline text as printed (uppercase if printed uppercase)
- "bbox": [y_min, x_min, y_max, x_max] as NORMALIZED coordinates 0–1000
  where (0,0) = top-left corner, (1000,1000) = bottom-right corner
  INCLUDE the headline, all body text, photos, and captions belonging to this article
- "continued_to": page number if article says "Contd. on page N", else null
- "continued_from": page number if this text starts with "Contd. from page N", else null

Rules:
- Page headers/footers (issue name, date, page number) are NOT articles
- Section labels (COVER STORY, NEWS, etc.) are metadata on the article, NOT separate articles
- If a column is a pure continuation with no headline, set title=null

Return ONLY a valid JSON array, no other text:
[{"title": "string or null", "bbox": [y_min, x_min, y_max, x_max], "continued_to": null, "continued_from": null}]"""


# ── Gemini call ────────────────────────────────────────────────────────────────

def detect_page_layout(client, page_path: Path, page_n: int) -> list[dict] | None:
    """Send page image to Gemini, get all article regions with normalized bboxes."""
    from google.genai import types as gai_types

    img_bytes = page_path.read_bytes()

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=[
                    gai_types.Part.from_bytes(data=img_bytes, mime_type="image/jpeg"),
                    PAGE_PROMPT,
                ],
            )
            raw = response.text.strip()
            raw = re.sub(r"^```(?:json)?\s*", "", raw)
            raw = re.sub(r"\s*```$", "", raw)
            regions = json.loads(raw)
            if not isinstance(regions, list):
                raise ValueError("not a JSON array")
            return regions

        except (json.JSONDecodeError, ValueError) as e:
            if attempt < MAX_RETRIES:
                print(f"      [retry {attempt}] parse error: {e}")
                time.sleep(2 ** attempt)
            else:
                print(f"      FAILED page {page_n}: {e}")
                return None

        except Exception as e:
            if attempt < MAX_RETRIES:
                print(f"      [retry {attempt}] API error: {e} — retrying in {2**attempt}s")
                time.sleep(2 ** attempt)
            else:
                print(f"      FAILED page {page_n}: {e}")
                return None

    return None


# ── Coordinate helpers ─────────────────────────────────────────────────────────

def norm_to_pixels(bbox_norm: list, img_w: int, img_h: int) -> dict:
    """Convert [y_min, x_min, y_max, x_max] (0-1000) to pixel coords."""
    y0, x0, y1, x1 = bbox_norm
    return {
        "y_start": max(0, int(y0 / 1000 * img_h)),
        "x_start": max(0, int(x0 / 1000 * img_w)),
        "y_end":   min(img_h, int(y1 / 1000 * img_h)),
        "x_end":   min(img_w, int(x1 / 1000 * img_w)),
        "img_width":  img_w,
        "img_height": img_h,
    }


# ── Column detection ───────────────────────────────────────────────────────────

def detect_column_boundaries(
    img,
    dark_threshold: int = 150,
    gutter_ink_ratio: float = 0.02,
    min_gutter_width: int = 6,
    min_column_width: int = 60,
    margin_ink_ratio: float = 0.02,
    y_slice_frac: tuple[float, float] = (0.2, 0.8),
) -> list[tuple[int, int]]:
    """
    Find column x-boundaries using a vertical projection profile.

    Analyzes only the middle portion of the page (y_slice_frac) to avoid
    headers/footers skewing the projection. Uses a low ink threshold to
    correctly detect gutters that contain vertical rules or sparse ink.

    Returns sorted list of (x_start, x_end) for each detected column.
    Falls back to [(0, img_width-1)] if nothing is detected.
    """
    import numpy as np

    gray = np.array(img.convert("L"))   # shape (H, W)
    h, w = gray.shape

    # Use only the middle slice to avoid headers/footers
    y0 = int(h * y_slice_frac[0])
    y1 = int(h * y_slice_frac[1])
    gray_slice = gray[y0:y1, :]

    ink = (gray_slice < dark_threshold).astype(np.float32)
    v_proj = ink.mean(axis=0)           # fraction of dark pixels per x-column

    # Find content area (skip left/right margins)
    has_content = v_proj > margin_ink_ratio
    if not has_content.any():
        return [(0, w - 1)]
    x_left  = int(np.argmax(has_content))
    x_right = int(w - 1 - np.argmax(has_content[::-1]))

    # Find gutter valleys within content area
    proj_slice = v_proj[x_left : x_right + 1]
    is_gutter  = proj_slice < gutter_ink_ratio

    columns: list[tuple[int, int]] = []
    col_start = x_left
    i = 0
    n = len(is_gutter)

    while i < n:
        if is_gutter[i]:
            gutter_start = i
            while i < n and is_gutter[i]:
                i += 1
            gutter_width = i - gutter_start
            if gutter_width >= min_gutter_width:
                col_end = x_left + gutter_start
                if col_end - col_start >= min_column_width:
                    columns.append((col_start, col_end))
                col_start = x_left + i
        else:
            i += 1

    # Trailing column after last gutter
    if x_right - col_start >= min_column_width:
        columns.append((col_start, x_right))

    return columns if columns else [(x_left, x_right)]


def snap_x_to_columns(
    x_start: int,
    x_end: int,
    columns: list[tuple[int, int]],
) -> tuple[int, int]:
    """
    Expand an article's x-range to the exact boundaries of the column(s) it overlaps.

    Uses article centre + overlap fraction to determine which columns are covered,
    then returns the union of those columns' outer edges.
    """
    if not columns:
        return x_start, x_end

    article_center = (x_start + x_end) / 2
    article_width  = max(1, x_end - x_start)
    overlapping: list[tuple[int, int]] = []

    for col_x0, col_x1 in columns:
        col_width = max(1, col_x1 - col_x0)
        overlap = max(0, min(x_end, col_x1) - max(x_start, col_x0))
        # Normalize by the smaller of article or column width so a small bleed
        # into an adjacent column doesn't count as spanning it.
        denom = min(article_width, col_width)
        if col_x0 <= article_center <= col_x1 or overlap / denom > 0.45:
            overlapping.append((col_x0, col_x1))

    if not overlapping:
        # Fallback: nearest column by centre distance
        closest = min(columns, key=lambda c: abs((c[0] + c[1]) / 2 - article_center))
        return closest[0], closest[1]

    return min(c[0] for c in overlapping), max(c[1] for c in overlapping)


# ── Title matching ─────────────────────────────────────────────────────────────

def normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9 ]", " ", text.lower())


def match_score(detected_title: str, known_title: str) -> float:
    """Word-overlap fraction between detected and known title."""
    d_words = set(normalize(detected_title).split())
    k_words = [w for w in normalize(known_title).split() if len(w) > 2]
    if not k_words:
        return 0.0
    hits = sum(1 for w in k_words if w in d_words)
    return hits / len(k_words)


def match_regions_to_articles(
    regions: list[dict],
    articles: list[dict],
    threshold: float = 0.5,
) -> dict[str, dict]:
    """
    Match detected page regions to known article slugs.
    Returns {slug: region_dict} for matches above threshold.
    """
    matched: dict[str, dict] = {}
    for art in articles:
        best_score = 0.0
        best_region = None
        for region in regions:
            title = region.get("title") or ""
            if not title:
                continue
            score = match_score(title, art["title"])
            if score > best_score:
                best_score = score
                best_region = region
        if best_score >= threshold and best_region is not None:
            matched[art["slug"]] = best_region
    return matched


# ── Frontmatter helpers ────────────────────────────────────────────────────────

def parse_article_meta(md_path: Path) -> dict | None:
    text = md_path.read_text(encoding="utf-8")
    m_title = re.search(r'^title:\s*"([^"]+)"', text, re.MULTILINE)
    m_date  = re.search(r'^issue_date:\s*"([^"]+)"', text, re.MULTILINE)
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
        "issue_slug": issue_slug,
        "pages": [int(p) for p in raw_pages],
    }


def load_issue_articles(issue_slug: str) -> list[dict]:
    arts = []
    for md in ARTICLES_DIR.glob("*.md"):
        meta = parse_article_meta(md)
        if meta and meta["issue_slug"] == issue_slug:
            arts.append(meta)
    return arts


# ── Issue processing ───────────────────────────────────────────────────────────

def process_issue(
    client,
    issue_slug: str,
    force: bool = False,
    only_page: int | None = None,
) -> int:
    page_dir = DOCS_PAGES_DIR / issue_slug
    if not page_dir.exists():
        print(f"  No page images for {issue_slug}")
        return 0

    articles = load_issue_articles(issue_slug)
    if not articles:
        print(f"  No articles found for {issue_slug}")
        return 0

    layout_path = page_dir / "layout.json"
    coords_path = page_dir / "coords.json"

    # Load existing layout/coords to merge into
    existing_layout: dict[str, list] = {}
    if layout_path.exists() and not force:
        existing_layout = json.loads(layout_path.read_text())

    existing_coords: dict[str, dict] = {}
    if coords_path.exists() and not force:
        existing_coords = json.loads(coords_path.read_text())

    # Group articles by page
    page_to_articles: dict[int, list[dict]] = {}
    for art in articles:
        for pg in art["pages"]:
            page_to_articles.setdefault(pg, []).append(art)

    pages_to_run = sorted(page_to_articles.keys())
    if only_page is not None:
        pages_to_run = [p for p in pages_to_run if p == only_page]

    all_layout = dict(existing_layout)
    all_coords = dict(existing_coords)

    from PIL import Image as PILImage

    print(f"\n{issue_slug}  ({len(pages_to_run)} pages to process)")

    for page_n in pages_to_run:
        page_key = str(page_n)
        if page_key in all_layout and not force:
            print(f"  Page {page_n}: already in layout.json — skipping (use --force to redo)")
            continue

        page_path = page_dir / f"page-{page_n}.jpg"
        if not page_path.exists():
            print(f"  Page {page_n}: image not found — skipping")
            continue

        img = PILImage.open(page_path)
        img_w, img_h = img.size

        columns = detect_column_boundaries(img)
        col_str = "  ".join(f"[{x0}–{x1}]" for x0, x1 in columns)
        print(f"  Page {page_n} ({img_w}×{img_h}, {len(columns)} col{'s' if len(columns)!=1 else ''}: {col_str})...", end=" ", flush=True)

        regions = detect_page_layout(client, page_path, page_n)

        if regions is None:
            print("FAILED")
            continue

        titles = [r.get("title") or "(continuation)" for r in regions]
        print(f"{len(regions)} regions: {', '.join(t[:30] for t in titles[:4])}{'...' if len(titles) > 4 else ''}")

        # Store raw layout
        all_layout[page_key] = regions

        # Match to known articles and convert to pixel coords
        arts_on_page = page_to_articles.get(page_n, [])
        matched = match_regions_to_articles(regions, arts_on_page)

        for slug, region in matched.items():
            bbox_norm = region.get("bbox", [])
            if len(bbox_norm) != 4:
                continue
            bbox_px = norm_to_pixels(bbox_norm, img_w, img_h)
            # Snap x-coordinates to exact column boundaries
            snapped_x0, snapped_x1 = snap_x_to_columns(
                bbox_px["x_start"], bbox_px["x_end"], columns
            )
            bbox_px["x_start"] = snapped_x0
            bbox_px["x_end"]   = snapped_x1
            all_coords.setdefault(slug, {})[page_key] = bbox_px
            print(f"    ✓ {slug[:50]}  y={bbox_px['y_start']}→{bbox_px['y_end']}  x={bbox_px['x_start']}→{bbox_px['x_end']}")

        unmatched = [a["slug"] for a in arts_on_page if a["slug"] not in matched]
        for slug in unmatched:
            print(f"    ✗ NO MATCH: {slug[:60]}")

        # Save after each page
        layout_path.write_text(json.dumps(all_layout, indent=2))
        coords_path.write_text(json.dumps(all_coords, indent=2))

        time.sleep(0.5)

    found = sum(1 for pages in all_coords.values() if pages)
    print(f"\n  Done: {found} articles with coords in coords.json")
    print(f"  Layout regions saved to layout.json")
    return found


# ── CLI ────────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Detect article layout using Gemini normalized coords (all articles per page)"
    )
    parser.add_argument("--issue", metavar="SLUG", required=True)
    parser.add_argument("--page",  type=int, metavar="N", help="Process only this page")
    parser.add_argument("--force", action="store_true", help="Re-detect even if layout.json exists")
    parser.add_argument("--poc",   action="store_true", help="PoC mode: print coords without saving")
    args = parser.parse_args()

    from dotenv import load_dotenv
    from google import genai as gai

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("ERROR: GEMINI_API_KEY not set in .env")
        sys.exit(1)

    client = gai.Client(api_key=api_key)

    total = process_issue(
        client,
        args.issue,
        force=args.force,
        only_page=args.page,
    )
    print(f"\nTotal: {total} articles with bounding boxes")
    print("Next: python generate_site.py  (to rebuild crops)")


if __name__ == "__main__":
    main()
