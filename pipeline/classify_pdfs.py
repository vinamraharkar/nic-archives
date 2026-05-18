#!/usr/bin/env python3
"""
Classify all PDFs in Archives/ as scanned, born_digital, or corrupt_encoding.

Usage:
    python pipeline/classify_pdfs.py                    # classify all PDFs
    python pipeline/classify_pdfs.py --files Apr-1995.pdf April-2003.pdf  # pilot mode
    python pipeline/classify_pdfs.py --report           # print summary of classified.json

Output: classified.json (idempotent — existing entries are never overwritten)
"""

import argparse
import subprocess
import sys
from pathlib import Path

# Allow running from project root or pipeline/
sys.path.insert(0, str(Path(__file__).parent.parent))

from pipeline.utils import (
    ARCHIVES_DIR,
    CLASSIFIED_PATH,
    load_classified,
    log_error,
    save_classified,
    filename_to_slug,
)

# Garbage patterns produced by font-encoded PDFs (2011-2012 issues).
# These byte-shifted characters appear when pdftotext can't decode proprietary fonts.
CORRUPT_PATTERNS = [
    "IÀFLHQW",   # "Efficient" encoded
    "RYHUQDQFH",  # "Governance" encoded
    "\x00",       # null bytes
]

# Min chars for born_digital. Below this = scanned (image-only PDF).
BORN_DIGITAL_THRESHOLD = 100


def extract_text_sample(pdf_path: Path) -> str:
    """Run pdftotext on first 3 pages. Sampling more pages avoids misclassifying
    PDFs whose cover page is a scan/image but body is born-digital.
    """
    try:
        result = subprocess.run(
            ["pdftotext", "-f", "1", "-l", "3", str(pdf_path), "-"],
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.stdout
    except subprocess.TimeoutExpired:
        return ""
    except FileNotFoundError:
        print("ERROR: pdftotext not found. Install with: brew install poppler")
        sys.exit(1)


def classify_text(text: str) -> tuple[str, int]:
    """Return (classification, char_count) for the extracted text."""
    char_count = len(text.strip())

    if char_count < BORN_DIGITAL_THRESHOLD:
        return "scanned", char_count

    for pattern in CORRUPT_PATTERNS:
        if pattern in text:
            return "corrupt_encoding", char_count

    return "born_digital", char_count


def classify_pdfs(filenames: list[str]) -> list[dict]:
    """Classify a list of PDF filenames. Returns new entries only."""
    existing = load_classified()
    existing_names = {e["filename"] for e in existing}

    new_entries: list[dict] = []
    for filename in filenames:
        if filename in existing_names:
            print(f"  [skip] {filename} — already classified")
            continue

        pdf_path = ARCHIVES_DIR / filename
        if not pdf_path.exists():
            log_error(filename, "classify", f"File not found: {pdf_path}")
            continue

        text = extract_text_sample(pdf_path)
        classification, char_count = classify_text(text)

        entry = {
            "filename": filename,
            "slug": filename_to_slug(filename),
            "type": classification,
            "chars": char_count,
        }
        new_entries.append(entry)
        print(f"  {filename:<35} {classification:<20} ({char_count} chars)")

    return new_entries


def print_report() -> None:
    entries = load_classified()
    if not entries:
        print("classified.json is empty or missing.")
        return

    counts: dict[str, int] = {}
    for e in entries:
        counts[e["type"]] = counts.get(e["type"], 0) + 1

    print(f"\nTotal: {len(entries)} PDFs classified")
    for t, n in sorted(counts.items()):
        print(f"  {t:<20} {n}")

    print("\nScanned / corrupt issues:")
    for e in entries:
        if e["type"] in ("scanned", "corrupt_encoding"):
            print(f"  {e['filename']}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Classify NIC Archives PDFs")
    parser.add_argument(
        "--files", nargs="+", metavar="FILENAME",
        help="Classify specific files only (pilot mode)"
    )
    parser.add_argument(
        "--report", action="store_true",
        help="Print summary of existing classified.json"
    )
    args = parser.parse_args()

    if args.report:
        print_report()
        return

    if args.files:
        filenames = args.files
        print(f"Classifying {len(filenames)} file(s) (pilot mode)...")
    else:
        filenames = sorted(p.name for p in ARCHIVES_DIR.glob("*.pdf"))
        print(f"Classifying all {len(filenames)} PDFs in Archives/...")

    print()
    new_entries = classify_pdfs(filenames)

    if new_entries:
        existing = load_classified()
        all_entries = existing + new_entries
        save_classified(all_entries)
        print(f"\nSaved {len(new_entries)} new entries → classified.json")
    else:
        print("\nNo new entries to save.")


if __name__ == "__main__":
    main()
