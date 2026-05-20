"""
Upload docs/pages/**/*.jpg to Cloudflare R2 bucket 'nic-archives-pages'.

Uses wrangler CLI (OAuth session) — no credentials in this script.
Run from /tmp or any directory outside the project to avoid wrangler
auto-loading the project's .env (which holds a D1-only token).

Usage:
    python pipeline/upload_to_r2.py           # full upload
    python pipeline/upload_to_r2.py --retry   # retry only files missing from R2
"""

import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

BUCKET       = "nic-archives-pages"
DOCS_DIR     = Path(__file__).parent.parent / "docs"
PAGES_DIR    = DOCS_DIR / "pages"
WORKERS      = 6   # parallel wrangler processes; keep low to avoid CF rate limits
WORKERS_RETRY = 2  # fewer workers on retry to avoid SQLite lock contention

def upload(jpg: Path) -> tuple[str, bool, str]:
    key = jpg.relative_to(DOCS_DIR).as_posix()  # e.g. pages/april-1995/page-1.jpg
    result = subprocess.run(
        [
            "wrangler", "r2", "object", "put",
            f"{BUCKET}/{key}",
            "--file", str(jpg),
            "--content-type", "image/jpeg",
            "--remote",
        ],
        capture_output=True,
        text=True,
        cwd="/tmp",  # run from /tmp so wrangler uses OAuth, not project .env
    )
    ok = result.returncode == 0
    err = result.stderr.strip() if not ok else ""
    return key, ok, err


def main():
    # --retry FILE: retry only keys listed one-per-line in FILE (relative to docs/)
    retry_file = None
    for i, arg in enumerate(sys.argv[1:], 1):
        if arg == "--retry" and i < len(sys.argv):
            retry_file = sys.argv[i + 1] if i < len(sys.argv) - 1 else None

    if retry_file:
        keys = Path(retry_file).read_text().splitlines()
        jpgs = [DOCS_DIR / k for k in keys if k.strip()]
        workers = WORKERS_RETRY
        print(f"Retry mode: {len(jpgs)} files with {workers} workers...\n")
    else:
        jpgs = sorted(PAGES_DIR.rglob("*.jpg"))
        workers = WORKERS
        if not jpgs:
            print("No JPG files found in docs/pages/")
            sys.exit(1)
        print(f"Uploading {len(jpgs)} files to R2 bucket '{BUCKET}' with {workers} workers...")
        print("Progress shown below.\n")

    total = len(jpgs)
    if total == 0:
        print("Nothing to upload.")
        return

    done = 0
    failed = []

    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(upload, jpg): jpg for jpg in jpgs}
        for future in as_completed(futures):
            key, ok, err = future.result()
            done += 1
            if ok:
                if done % 100 == 0 or done == total:
                    print(f"  [{done}/{total}] uploaded {key}")
            else:
                failed.append((key, err))
                print(f"  [FAIL {done}/{total}] {key}: {err[:120]}")

    print(f"\nDone. {total - len(failed)}/{total} uploaded successfully.")
    if failed:
        print(f"\nFailed ({len(failed)}):")
        for key, err in failed:
            print(f"  {key}: {err[:200]}")
        sys.exit(1)


if __name__ == "__main__":
    main()
