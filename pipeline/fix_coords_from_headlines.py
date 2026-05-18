#!/usr/bin/env python3
"""
fix_coords_from_headlines.py

Corrects y_start/y_end coordinates in coords.json using pixel-level dark
headline bar detection. Gemini y-coordinates are off by 200-900px; this
replaces them with true headline positions.

Algorithm:
  1. Detect dark horizontal bands (dark-background headline boxes) on each page.
  2. Strip bands in the top/bottom decoration zones (y < 50 or y > 85% of page).
  3. If the number of reliable bands equals the number of articles on that page,
     assign them 1-to-1 in order (Gemini gets article ORDER right, not positions).
  4. Set y_start = band top, y_end = next band top - 1 (or page bottom for last).
  5. Skip pages where band count ≠ article count (too ambiguous).

Usage:
    python3 pipeline/fix_coords_from_headlines.py [--issue october-1992] [--dry-run]
    python3 pipeline/fix_coords_from_headlines.py          # all issues with coords.json
"""

import argparse
import json
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
COORDS_ROOT = REPO_ROOT / "docs" / "pages"

DARK_THRESHOLD = 140   # rows with mean pixel value < this are headline candidates
MIN_BAND_PX    = 3     # minimum consecutive dark rows to count as a band
TOP_MARGIN_PX  = 50    # ignore bands above this y (page decoration)
BOTTOM_FRAC    = 0.85  # ignore bands below img_h * this (footer decoration)


def _find_bands(img_array, x0: int, x1: int) -> list:
    """Return list of (y_start, y_end) for dark horizontal bands in column x0:x1."""
    col = img_array[:, x0:x1]
    row_avgs = col.mean(axis=(1, 2))
    bands = []
    in_band = False
    bs = 0
    for y, avg in enumerate(row_avgs):
        if avg < DARK_THRESHOLD and not in_band:
            in_band, bs = True, y
        elif avg >= DARK_THRESHOLD and in_band:
            in_band = False
            if y - bs >= MIN_BAND_PX:
                bands.append((bs, y - 1))
    if in_band and (len(row_avgs) - bs) >= MIN_BAND_PX:
        bands.append((bs, len(row_avgs) - 1))
    return bands


def fix_coords_for_issue(issue_slug, dry_run=False):
    try:
        import numpy as np
        from PIL import Image
    except ImportError:
        print("  numpy / Pillow not available — install them to use this script")
        return

    coords_path = COORDS_ROOT / issue_slug / "coords.json"
    if not coords_path.exists():
        print(f"  No coords.json found for {issue_slug}")
        return

    with open(coords_path) as f:
        original = json.load(f)

    # Deep copy for updates
    updated = {slug: {pg: dict(bbox) for pg, bbox in pages.items()}
               for slug, pages in original.items()}

    # Group articles by page
    by_page = {}
    for slug, pages in original.items():
        for page_str, bbox in pages.items():
            by_page.setdefault(int(page_str), []).append((slug, page_str, bbox))

    changes_made = False

    for page_n in sorted(by_page):
        articles = by_page[page_n]
        if len(articles) < 2:
            continue  # single article: whole page is unambiguous, skip

        page_img_path = COORDS_ROOT / issue_slug / f"page-{page_n}.jpg"
        if not page_img_path.exists():
            print(f"  [skip] page-{page_n}.jpg not found")
            continue

        img = np.array(Image.open(page_img_path).convert("RGB"))
        img_h, img_w = img.shape[:2]
        bottom_cutoff = int(img_h * BOTTOM_FRAC)

        x0 = max(0, min(b["x_start"] for _, _, b in articles))
        x1 = min(img_w, max(b["x_end"] for _, _, b in articles))

        all_bands = _find_bands(img, x0, x1)

        # Strip top/bottom decoration bands
        reliable = [(y0, y1) for y0, y1 in all_bands
                    if y0 >= TOP_MARGIN_PX and y0 < bottom_cutoff]

        n_art = len(articles)
        n_band = len(reliable)

        if n_band != n_art:
            print(f"  Page {page_n}: {n_band} reliable band(s) for {n_art} article(s) — skipping (ambiguous)")
            continue

        print(f"  Page {page_n}: {n_band} band(s) match {n_art} article(s) — applying fix")

        # Sort articles by Gemini y_start (Gemini gets ORDER right)
        articles_sorted = sorted(articles, key=lambda a: a[2]["y_start"])
        # Sort bands by y
        bands_sorted = sorted(reliable, key=lambda b: b[0])

        for i, ((slug, page_str, bbox), (band_y0, _)) in enumerate(zip(articles_sorted, bands_sorted)):
            new_y_start = band_y0
            if i + 1 < n_art:
                new_y_end = bands_sorted[i + 1][0] - 1
            else:
                new_y_end = img_h - 1

            old_ys, old_ye = bbox["y_start"], bbox["y_end"]
            if new_y_start != old_ys or new_y_end != old_ye:
                print(f"    {slug}: y_start {old_ys}→{new_y_start}, y_end {old_ye}→{new_y_end}")
                if not dry_run:
                    updated[slug][page_str]["y_start"] = new_y_start
                    updated[slug][page_str]["y_end"] = new_y_end
                changes_made = True
            else:
                print(f"    {slug}: unchanged")

    if changes_made and not dry_run:
        backup = coords_path.with_suffix(".json.bak")
        with open(backup, "w") as f:
            json.dump(original, f, indent=2)
        with open(coords_path, "w") as f:
            json.dump(updated, f, indent=2)
        print(f"  Backup → {backup.name}, updated {coords_path.name}")
    elif not changes_made:
        print("  No changes needed.")
    else:
        print("  [dry-run] no files written")


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--issue", help="Issue slug (e.g. october-1992). Omit to process all.")
    parser.add_argument("--dry-run", action="store_true", help="Print changes without writing files")
    args = parser.parse_args()

    if args.issue:
        issues = [args.issue]
    else:
        issues = sorted(d.name for d in COORDS_ROOT.iterdir()
                        if d.is_dir() and (d / "coords.json").exists())

    for slug in issues:
        print(f"\n=== {slug} ===")
        fix_coords_for_issue(slug, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
