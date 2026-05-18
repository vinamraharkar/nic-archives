#!/usr/bin/env python3
"""
Extract text from scanned and corrupt_encoding PDFs using Mistral OCR 3.

Usage:
    python pipeline/extract_scanned.py                        # process all scanned/corrupt
    python pipeline/extract_scanned.py --files Apr-1995.pdf   # pilot mode
    python pipeline/extract_scanned.py --dry-run              # estimate cost, don't call API

Strategy: upload entire PDF to Mistral Files API once → OCR all pages in one call → delete file.
This is simpler and more reliable than converting pages to images one-by-one.

Input:  classified.json (scanned + corrupt_encoding entries)
Output: raw_text/{slug}.json  →  [{page: N, text: "..."}]

Robustness:
  - Idempotent: skips files where raw_text/{slug}.json already exists
  - Cost guard: prints estimate and asks confirmation if batch > $1
  - Retry: up to 3 attempts with exponential backoff on transient errors
  - File cleanup: deletes uploaded file from Mistral even on failure
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from pipeline.utils import (
    ARCHIVES_DIR,
    RAW_TEXT_DIR,
    load_classified,
    log_error,
    slug_to_raw_text_path,
)

# Mistral OCR pricing: ~$1 per 1000 pages
COST_PER_PAGE = 0.001
COST_CONFIRM_THRESHOLD = 1.0  # ask user if estimated cost exceeds this

MAX_RETRIES = 3


def get_pdf_page_count(pdf_path: Path) -> int:
    """Return number of pages in the PDF using pdfinfo."""
    try:
        result = subprocess.run(
            ["pdfinfo", str(pdf_path)],
            capture_output=True, text=True, timeout=30,
        )
        for line in result.stdout.splitlines():
            if line.startswith("Pages:"):
                return int(line.split(":")[1].strip())
    except Exception:
        pass
    return 0


def ocr_pdf(client, pdf_path: Path, filename: str) -> list[dict] | None:
    """
    Upload PDF to Mistral Files API, OCR all pages, delete the file.
    Returns [{page: N, text: "..."}] or None on failure.
    """
    from mistralai import models

    # Read PDF bytes
    try:
        pdf_bytes = pdf_path.read_bytes()
    except OSError as e:
        log_error(filename, "ocr_read", str(e))
        return None

    file_id = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            # Step 1: Upload PDF to Files API
            print(f"    uploading ({len(pdf_bytes) / 1024:.0f} KB)...", end=" ", flush=True)
            upload_response = client.files.upload(
                file=models.File(file_name=filename, content=pdf_bytes),
                purpose="ocr",
            )
            file_id = upload_response.id
            print(f"uploaded (id={file_id[:8]}...)")

            # Step 2: OCR the uploaded file — all pages in one call
            print(f"    running OCR...", end=" ", flush=True)
            ocr_response = client.ocr.process(
                model="mistral-ocr-latest",
                document=models.FileChunk(file_id=file_id),
            )
            pages = [
                {"page": p.index + 1, "text": p.markdown}
                for p in ocr_response.pages
            ]
            print(f"done ({len(pages)} pages)")
            return pages

        except Exception as e:
            error_msg = str(e)
            if attempt < MAX_RETRIES:
                wait = 2 ** attempt  # 2s, 4s
                print(f"\n    [retry {attempt}/{MAX_RETRIES}] {error_msg} — waiting {wait}s")
                time.sleep(wait)
            else:
                log_error(filename, "ocr_api", error_msg)
                print(f"\n    FAILED: {error_msg}")
                return None
        finally:
            # Always clean up the uploaded file
            if file_id:
                try:
                    client.files.delete(file_id=file_id)
                except Exception:
                    pass  # Cleanup failure is non-fatal


def process_file(client, filename: str, slug: str) -> bool:
    """OCR one PDF. Returns True on success, False on failure."""
    out_path = slug_to_raw_text_path(slug)

    if out_path.exists():
        print(f"  [skip] {filename} — already extracted")
        return True

    pdf_path = ARCHIVES_DIR / filename
    if not pdf_path.exists():
        log_error(filename, "extract_scanned", f"File not found: {pdf_path}")
        return False

    page_count = get_pdf_page_count(pdf_path)
    print(f"  {filename} ({page_count} pages)")

    pages = ocr_pdf(client, pdf_path, filename)
    if pages is None:
        return False

    RAW_TEXT_DIR.mkdir(exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(pages, f, indent=2, ensure_ascii=False)

    total_chars = sum(len(p["text"]) for p in pages)
    print(f"  → saved {len(pages)} pages ({total_chars:,} chars) to {out_path.name}\n")
    return True


def estimate_cost(entries: list[dict]) -> tuple[float, int]:
    """Return (estimated_cost, total_pages) for the given entries."""
    total_pages = 0
    for entry in entries:
        pdf_path = ARCHIVES_DIR / entry["filename"]
        if pdf_path.exists():
            total_pages += get_pdf_page_count(pdf_path)
    return total_pages * COST_PER_PAGE, total_pages


def main() -> None:
    parser = argparse.ArgumentParser(description="OCR scanned PDFs with Mistral OCR 3")
    parser.add_argument(
        "--files", nargs="+", metavar="FILENAME",
        help="Process specific files only (pilot mode)"
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Estimate cost only — do not call the API"
    )
    args = parser.parse_args()

    classified = load_classified()
    if not classified:
        print("classified.json is empty. Run classify_pdfs.py first.")
        sys.exit(1)

    if args.files:
        target_names = set(args.files)
        entries = [
            e for e in classified
            if e["filename"] in target_names
            and e["type"] in ("scanned", "corrupt_encoding")
        ]
        not_found = target_names - {e["filename"] for e in entries}
        if not_found:
            print(f"WARNING: not in classified.json as scanned/corrupt: {not_found}")
    else:
        entries = [e for e in classified if e["type"] in ("scanned", "corrupt_encoding")]

    # Filter out already-extracted files
    pending = [e for e in entries if not slug_to_raw_text_path(e["slug"]).exists()]
    skipped = len(entries) - len(pending)

    print(f"Scanned/corrupt PDFs: {len(entries)} total, {skipped} already extracted, {len(pending)} to process")

    if not pending:
        print("Nothing to do.")
        return

    estimated_cost, total_pages = estimate_cost(pending)
    print(f"Estimated OCR cost: ${estimated_cost:.2f} ({total_pages} pages)\n")

    if args.dry_run:
        print("Dry run — no API calls made.")
        return

    if estimated_cost > COST_CONFIRM_THRESHOLD:
        confirm = input(f"Cost exceeds ${COST_CONFIRM_THRESHOLD:.0f}. Proceed? [y/N] ").strip().lower()
        if confirm != "y":
            print("Aborted.")
            return

    # Load Mistral client
    from dotenv import load_dotenv
    load_dotenv()
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print("ERROR: MISTRAL_API_KEY not set in .env")
        sys.exit(1)

    from mistralai import Mistral
    client = Mistral(api_key=api_key)

    ok = failed = 0
    for entry in pending:
        success = process_file(client, entry["filename"], entry["slug"])
        if success:
            ok += 1
        else:
            failed += 1

    print(f"\nDone: {ok} succeeded, {failed} failed.")
    if failed:
        print("See pipeline/errors.json for details.")


if __name__ == "__main__":
    main()
