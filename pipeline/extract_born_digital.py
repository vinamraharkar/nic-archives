#!/usr/bin/env python3
"""
Extract text from born_digital PDFs using pdftotext.

Usage:
    python pipeline/extract_born_digital.py                    # process all born_digital
    python pipeline/extract_born_digital.py --files April-2003.pdf  # pilot mode

Input:  classified.json (born_digital entries)
Output: raw_text/{slug}.json  →  [{page: N, text: "..."}]

Idempotent: skips files where raw_text/{slug}.json already exists.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from pipeline.utils import (
    ARCHIVES_DIR,
    RAW_TEXT_DIR,
    load_classified,
    log_error,
    slug_to_raw_text_path,
)


def extract_pages(pdf_path: Path) -> list[dict] | None:
    """Extract all pages from a born-digital PDF using pdftotext -layout.

    Returns list of {page: int, text: str} dicts, or None on failure.
    pdftotext uses form-feed (\f) as page separator.
    """
    try:
        result = subprocess.run(
            ["pdftotext", "-layout", str(pdf_path), "-"],
            capture_output=True,
            text=True,
            timeout=120,
        )
    except subprocess.TimeoutExpired:
        return None
    except FileNotFoundError:
        print("ERROR: pdftotext not found. Install with: brew install poppler")
        sys.exit(1)

    raw = result.stdout
    # pdftotext separates pages with form-feed character
    page_texts = raw.split("\f")

    pages = []
    for i, text in enumerate(page_texts, start=1):
        cleaned = text.strip()
        if cleaned:  # skip trailing empty pages
            pages.append({"page": i, "text": cleaned})

    return pages if pages else None


def process_file(filename: str, slug: str) -> bool:
    """Extract one PDF. Returns True on success, False on failure."""
    out_path = slug_to_raw_text_path(slug)

    if out_path.exists():
        print(f"  [skip] {filename} — already extracted")
        return True

    pdf_path = ARCHIVES_DIR / filename
    if not pdf_path.exists():
        log_error(filename, "extract_born_digital", f"File not found: {pdf_path}")
        return False

    pages = extract_pages(pdf_path)
    if not pages:
        log_error(filename, "extract_born_digital", "pdftotext returned no text")
        return False

    RAW_TEXT_DIR.mkdir(exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(pages, f, indent=2, ensure_ascii=False)

    total_chars = sum(len(p["text"]) for p in pages)
    print(f"  {filename:<35} {len(pages)} pages, {total_chars:,} chars → {out_path.name}")
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract text from born-digital PDFs")
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
        # Pilot mode: look up slugs from classified.json
        target_names = set(args.files)
        entries = [e for e in classified if e["filename"] in target_names and e["type"] == "born_digital"]
        not_found = target_names - {e["filename"] for e in entries}
        if not_found:
            print(f"WARNING: not in classified.json as born_digital: {not_found}")
    else:
        entries = [e for e in classified if e["type"] == "born_digital"]

    print(f"Extracting {len(entries)} born-digital PDF(s)...\n")

    ok = failed = 0
    for entry in entries:
        success = process_file(entry["filename"], entry["slug"])
        if success:
            ok += 1
        else:
            failed += 1

    print(f"\nDone: {ok} succeeded, {failed} failed.")
    if failed:
        print("See pipeline/errors.json for details.")


if __name__ == "__main__":
    main()
