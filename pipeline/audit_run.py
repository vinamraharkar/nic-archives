#!/usr/bin/env python3
"""
Post-run audit: check every issue for article count and body length anomalies.

Usage:
    python pipeline/audit_run.py

Flags issues that need attention:
  NOT_PROCESSED  — no sentinel file; issue was never segmented (run segment_articles.py)
  ZERO_ARTICLES  — sentinel exists but no articles found (Gemini returned nothing)
  THIN           — only 1 article (Gemini may have merged everything)
  SHORT_BODIES   — average article body < 300 chars (possible truncation)
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from pipeline.segment_articles import slug_to_issue_date
from pipeline.utils import ARTICLES_DIR, RAW_TEXT_DIR, load_classified


MIN_BODY_CHARS = 300
THIN_THRESHOLD = 2


def issue_date_to_suffix(issue_date: str) -> str:
    """'April 2003' → 'april-2003' (matches tail of article slugs)."""
    slug = issue_date.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    return slug.strip("-")


def get_articles_for_issue(issue_date: str) -> list[Path]:
    suffix = f"-{issue_date_to_suffix(issue_date)}.md"
    return [p for p in ARTICLES_DIR.glob("*.md") if p.name.endswith(suffix)]


def avg_body_length(article_paths: list[Path]) -> float:
    if not article_paths:
        return 0.0
    total = 0
    for p in article_paths:
        text = p.read_text(encoding="utf-8")
        # Strip frontmatter (--- ... ---) to measure body only
        body = re.sub(r"^---[\s\S]+?---\s*", "", text).strip()
        total += len(body)
    return total / len(article_paths)


def main() -> None:
    classified = load_classified()
    if not classified:
        print("classified.json not found. Run classify_pdfs.py first.")
        sys.exit(1)

    issues_with_raw = [e for e in classified if (RAW_TEXT_DIR / f"{e['slug']}.json").exists()]
    total = len(issues_with_raw)

    print(f"Auditing {total} issue(s) that have raw_text...\n")
    print(f"{'ISSUE':<35} {'STATUS':<16} {'ARTICLES':>8} {'AVG BODY':>10}")
    print("-" * 72)

    flagged: list[tuple[str, str]] = []

    for entry in sorted(issues_with_raw, key=lambda e: e["filename"]):
        filename = entry["filename"]
        slug = entry["slug"]
        issue_date = slug_to_issue_date(filename)

        sentinel = RAW_TEXT_DIR / f"{slug}.segmented"
        articles = get_articles_for_issue(issue_date)
        n = len(articles)
        avg = avg_body_length(articles)

        if not sentinel.exists():
            status = "NOT_PROCESSED"
            flagged.append((filename, status))
        elif n == 0:
            status = "ZERO_ARTICLES"
            flagged.append((filename, status))
        elif n < THIN_THRESHOLD:
            status = "THIN"
            flagged.append((filename, status))
        elif avg < MIN_BODY_CHARS:
            status = "SHORT_BODIES"
            flagged.append((filename, status))
        else:
            status = "OK"

        marker = "  !" if status != "OK" else "   "
        print(f"{marker} {filename:<33} {status:<16} {n:>8} {avg:>10.0f}")

    print("-" * 72)
    print(f"\n{total - len(flagged)}/{total} issues OK")

    if flagged:
        print(f"\n{len(flagged)} issue(s) need attention:")
        for filename, status in flagged:
            print(f"  [{status}] {filename}")
        print("\nFor NOT_PROCESSED: re-run segment_articles.py")
        print("For ZERO_ARTICLES / THIN / SHORT_BODIES: inspect articles/ and re-run with --files")
    else:
        print("All issues look healthy.")


if __name__ == "__main__":
    main()
