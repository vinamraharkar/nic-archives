"""
Upload Archives/*.pdf to Cloudflare R2 as pdfs/{issue_slug}.pdf.
Uses wrangler CLI (OAuth session). Run from /tmp to avoid project .env.

Usage:
    python pipeline/upload_pdfs_to_r2.py
"""

import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

BUCKET    = "nic-archives-pages"
REPO_DIR  = Path(__file__).parent.parent
ARCHIVES  = REPO_DIR / "Archives"
WORKERS   = 4


def build_mapping() -> list[tuple[Path, str]]:
    """Return [(pdf_path, r2_key), ...] for all 131 issues."""
    classified = json.loads((REPO_DIR / "classified.json").read_text())
    issues = json.loads((REPO_DIR / "docs" / "api" / "issues.json").read_text())

    slug_map: dict[tuple[int, int], str] = {}
    for iss in issues:
        parts = iss["issue_slug"].rsplit("-", 1)
        if len(parts) == 2:
            try:
                m = datetime.strptime(parts[0], "%B").month
                slug_map[(int(parts[1]), m)] = iss["issue_slug"]
            except ValueError:
                pass

    pairs: list[tuple[Path, str]] = []
    for d in classified:
        s = d["slug"]
        month_str, year_str = s.rsplit("-", 1)
        for fmt in ("%b", "%B"):
            try:
                m = datetime.strptime(month_str, fmt).month
                break
            except ValueError:
                continue
        else:
            print(f"  SKIP (cannot parse month): {d['filename']}")
            continue
        issue_slug = slug_map.get((int(year_str), m))
        if not issue_slug:
            print(f"  SKIP (no issue slug): {d['filename']}")
            continue
        pdf_path = ARCHIVES / d["filename"]
        if not pdf_path.exists():
            print(f"  SKIP (file missing): {pdf_path}")
            continue
        pairs.append((pdf_path, f"pdfs/{issue_slug}.pdf"))
    return pairs


def upload(pdf_path: Path, key: str) -> tuple[str, bool, str]:
    result = subprocess.run(
        ["wrangler", "r2", "object", "put", f"{BUCKET}/{key}",
         "--file", str(pdf_path), "--content-type", "application/pdf", "--remote"],
        capture_output=True, text=True, cwd="/tmp",
    )
    ok = result.returncode == 0
    return key, ok, result.stderr.strip() if not ok else ""


def main() -> None:
    pairs = build_mapping()
    total = len(pairs)
    size_mb = sum(p.stat().st_size for p, _ in pairs) / 1_048_576
    print(f"Uploading {total} PDFs ({size_mb:.0f} MB) to R2 bucket '{BUCKET}' with {WORKERS} workers...")

    done = failed = 0
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futures = {pool.submit(upload, p, k): (p, k) for p, k in pairs}
        for fut in as_completed(futures):
            key, ok, err = fut.result()
            done += 1
            if ok:
                if done % 20 == 0 or done == total:
                    print(f"  [{done}/{total}] {key}")
            else:
                failed += 1
                print(f"  [FAIL {done}/{total}] {key}: {err[:120]}")

    print(f"\nDone. {total - failed}/{total} uploaded successfully.")
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
