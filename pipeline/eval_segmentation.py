#!/usr/bin/env python3
"""
Eval harness: compare Gemini article segmentation against manually-verified ground truth.

Usage:
    python pipeline/eval_segmentation.py --issue october-1992
    python pipeline/eval_segmentation.py --issue october-1992 --dry-run   # skip Gemini call
    python pipeline/eval_segmentation.py --issue october-1992 --cached    # reuse eval_output/

Ground truth: articles/*-{issue-slug}.md  (hand-verified files)
Gemini output: eval_output/{issue-slug}/*.md  (never touches articles/)
Report: printed to stdout + saved to eval_output/{issue-slug}/report.txt
"""

from __future__ import annotations

import argparse
import difflib
import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from pipeline.utils import ARTICLES_DIR, RAW_TEXT_DIR, make_frontmatter, make_article_slug
from pipeline.segment_articles import (
    GEMINI_MODEL, SYSTEM_PROMPT, build_issue_text, parse_gemini_response, filter_boilerplate
)

EVAL_DIR = Path(__file__).parent.parent / "eval_output"


# ── Ground truth loading ──────────────────────────────────────────────────────

def load_ground_truth(issue_slug: str) -> list[dict]:
    """Load all hand-verified articles for this issue from articles/."""
    articles = []
    for md_path in sorted(ARTICLES_DIR.glob(f"*-{issue_slug}.md")):
        text = md_path.read_text(encoding="utf-8")
        m_title  = re.search(r'^title:\s*"([^"]+)"', text, re.MULTILINE)
        m_pages  = re.search(r'^pages:\s*\[([^\]]+)\]', text, re.MULTILINE)
        m_author = re.search(r'^author:\s*"?([^"\n]+)"?', text, re.MULTILINE)
        m_section= re.search(r'^section:\s*"?([^"\n]+)"?', text, re.MULTILINE)
        body_match = re.search(r'^---\s*\n.*?^---\s*\n(.+)', text, re.MULTILINE | re.DOTALL)

        if not m_title:
            continue

        pages = []
        if m_pages:
            pages = [int(p.strip()) for p in m_pages.group(1).split(",") if p.strip().isdigit()]

        author = None
        if m_author and m_author.group(1).strip().lower() not in ("null", "none", ""):
            author = m_author.group(1).strip()

        section = None
        if m_section and m_section.group(1).strip().lower() not in ("null", "none", ""):
            section = m_section.group(1).strip()

        body = body_match.group(1).strip() if body_match else ""

        articles.append({
            "slug": md_path.stem,
            "title": m_title.group(1),
            "pages": pages,
            "author": author,
            "section": section,
            "body_len": len(body),
        })

    return articles


# ── Gemini call ───────────────────────────────────────────────────────────────

def run_gemini(raw_slug: str, issue_date: str) -> list[dict] | None:
    """Call Gemini on raw_text/{issue_slug}.json. Returns parsed article list or None."""
    from dotenv import load_dotenv
    from google import genai

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("ERROR: GEMINI_API_KEY not set in .env")
        sys.exit(1)

    raw_path = RAW_TEXT_DIR / f"{raw_slug}.json"
    if not raw_path.exists():
        print(f"ERROR: {raw_path} not found")
        sys.exit(1)

    with open(raw_path, encoding="utf-8") as f:
        pages = json.load(f)

    issue_text = build_issue_text(pages)
    full_prompt = f"{SYSTEM_PROMPT}\n\nISSUE DATE: {issue_date}\n\nTEXT:\n{issue_text}"

    print(f"  Calling Gemini ({len(full_prompt):,} chars prompt)...")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(model=GEMINI_MODEL, contents=full_prompt)
    raw_response = response.text
    # Save raw response for debugging
    debug_path = EVAL_DIR / raw_slug / "raw_response.txt"
    debug_path.parent.mkdir(parents=True, exist_ok=True)
    debug_path.write_text(raw_response, encoding="utf-8")

    articles = parse_gemini_response(raw_response)
    if articles is None:
        print(f"ERROR: Gemini returned invalid JSON. Full response saved to {debug_path}")
        print(f"Raw (first 500 chars): {raw_response[:500]}")
        return None

    articles = filter_boilerplate(articles)
    return articles


def save_gemini_output(articles: list[dict], issue_slug: str, issue_date: str) -> Path:
    """Save Gemini articles to eval_output/{issue_slug}/. Returns output dir."""
    out_dir = EVAL_DIR / issue_slug
    out_dir.mkdir(parents=True, exist_ok=True)

    for article in articles:
        title = article.get("title", "Untitled").strip()
        body = article.get("body", "").strip()
        if not title:
            continue
        slug = make_article_slug(title, issue_date)
        fm = make_frontmatter(
            title=title,
            issue_date=issue_date,
            pages=article.get("pages", []),
            author=article.get("author"),
            section=article.get("section"),
        )
        (out_dir / f"{slug}.md").write_text(fm + f"## {title}\n\n{body}\n", encoding="utf-8")

    return out_dir


def load_gemini_output(issue_slug: str) -> list[dict]:
    """Load previously saved Gemini articles from eval_output/{issue_slug}/."""
    out_dir = EVAL_DIR / issue_slug
    articles = []
    for md_path in sorted(out_dir.glob("*.md")):
        if md_path.name == "report.txt":
            continue
        text = md_path.read_text(encoding="utf-8")
        m_title  = re.search(r'^title:\s*"([^"]+)"', text, re.MULTILINE)
        m_pages  = re.search(r'^pages:\s*\[([^\]]+)\]', text, re.MULTILINE)
        m_author = re.search(r'^author:\s*"?([^"\n]+)"?', text, re.MULTILINE)
        m_section= re.search(r'^section:\s*"?([^"\n]+)"?', text, re.MULTILINE)
        body_match = re.search(r'^---\s*\n.*?^---\s*\n(.+)', text, re.MULTILINE | re.DOTALL)

        if not m_title:
            continue
        pages = []
        if m_pages:
            pages = [int(p.strip()) for p in m_pages.group(1).split(",") if p.strip().isdigit()]
        author = None
        if m_author and m_author.group(1).strip().lower() not in ("null", "none", ""):
            author = m_author.group(1).strip()
        section = None
        if m_section and m_section.group(1).strip().lower() not in ("null", "none", ""):
            section = m_section.group(1).strip()
        body = body_match.group(1).strip() if body_match else ""

        articles.append({
            "slug": md_path.stem,
            "title": m_title.group(1),
            "pages": pages,
            "author": author,
            "section": section,
            "body_len": len(body),
        })
    return articles


# ── Comparison ────────────────────────────────────────────────────────────────

FUZZY_THRESHOLD = 0.55  # minimum similarity ratio to count as a match


def fuzzy_match(title_a: str, title_b: str) -> float:
    """Return similarity ratio between two titles (case-insensitive)."""
    return difflib.SequenceMatcher(None, title_a.lower(), title_b.lower()).ratio()


def best_match(gemini_title: str, gt_articles: list[dict]) -> tuple[dict | None, float]:
    """Find best matching ground truth article for a Gemini title."""
    best, best_score = None, 0.0
    for gt in gt_articles:
        score = fuzzy_match(gemini_title, gt["title"])
        if score > best_score:
            best, best_score = gt, score
    return best, best_score


def compare(gt: list[dict], gemini: list[dict]) -> dict:
    """Run full comparison. Returns structured result dict."""
    matched_gt_slugs: set[str] = set()
    matches = []       # (gt, gemini, score)
    hallucinated = []  # gemini articles with no GT match

    for g_art in gemini:
        gt_match, score = best_match(g_art["title"], gt)
        if score >= FUZZY_THRESHOLD and gt_match["slug"] not in matched_gt_slugs:
            matched_gt_slugs.add(gt_match["slug"])
            matches.append((gt_match, g_art, score))
        else:
            hallucinated.append(g_art)

    missed = [a for a in gt if a["slug"] not in matched_gt_slugs]

    # Per-match quality metrics
    page_correct = 0
    author_correct = 0
    section_correct = 0
    author_total = 0
    section_total = 0

    for gt_art, g_art, _ in matches:
        if set(gt_art["pages"]) == set(g_art["pages"]):
            page_correct += 1
        if gt_art["author"] is not None:
            author_total += 1
            if g_art["author"] and fuzzy_match(gt_art["author"], g_art["author"]) >= 0.7:
                author_correct += 1
        if gt_art["section"] is not None:
            section_total += 1
            if g_art["section"] and fuzzy_match(gt_art["section"], g_art["section"]) >= 0.7:
                section_correct += 1

    return {
        "gt_count": len(gt),
        "gemini_count": len(gemini),
        "matched": len(matches),
        "missed": missed,
        "hallucinated": hallucinated,
        "matches": matches,
        "page_correct": page_correct,
        "author_correct": author_correct,
        "author_total": author_total,
        "section_correct": section_correct,
        "section_total": section_total,
    }


# ── Report ────────────────────────────────────────────────────────────────────

def print_report(result: dict, issue_slug: str) -> str:
    lines = []
    lines.append(f"\n{'='*60}")
    lines.append(f"  EVAL REPORT: {issue_slug}")
    lines.append(f"{'='*60}\n")

    gt_n = result["gt_count"]
    gem_n = result["gemini_count"]
    matched = result["matched"]

    precision = matched / gem_n if gem_n else 0
    recall    = matched / gt_n  if gt_n  else 0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) else 0

    lines.append(f"Ground truth articles : {gt_n}")
    lines.append(f"Gemini found          : {gem_n}")
    lines.append(f"Matched               : {matched}")
    lines.append(f"Precision             : {precision:.0%}  ({matched}/{gem_n})")
    lines.append(f"Recall                : {recall:.0%}  ({matched}/{gt_n})")
    lines.append(f"F1                    : {f1:.2f}")

    pc = result["page_correct"]
    lines.append(f"\nPage accuracy         : {pc}/{matched}  ({pc/matched:.0%} of matched)" if matched else "\nPage accuracy: N/A")

    at = result["author_total"]
    ac = result["author_correct"]
    lines.append(f"Author accuracy       : {ac}/{at}  ({ac/at:.0%})" if at else "Author accuracy: N/A (no authors in GT)")

    st = result["section_total"]
    sc = result["section_correct"]
    lines.append(f"Section accuracy      : {sc}/{st}  ({sc/st:.0%})" if st else "Section accuracy: N/A")

    if result["missed"]:
        lines.append(f"\n{'─'*50}")
        lines.append(f"MISSED ({len(result['missed'])}) — in GT but not found by Gemini:")
        for a in result["missed"]:
            lines.append(f"  - \"{a['title']}\"  (pages {a['pages']})")

    if result["hallucinated"]:
        lines.append(f"\n{'─'*50}")
        lines.append(f"HALLUCINATED ({len(result['hallucinated'])}) — Gemini found, not in GT:")
        for a in result["hallucinated"]:
            lines.append(f"  + \"{a['title']}\"  (pages {a['pages']})")

    lines.append(f"\n{'─'*50}")
    lines.append("MATCHED PAIRS (GT title → Gemini title, score, pages match):")
    for gt_art, g_art, score in sorted(result["matches"], key=lambda x: -x[2]):
        page_ok = "✓" if set(gt_art["pages"]) == set(g_art["pages"]) else "✗"
        lines.append(f"  [{score:.2f}] {page_ok}  GT: \"{gt_art['title']}\"")
        if gt_art["title"].lower() != g_art["title"].lower():
            lines.append(f"            ↳  GM: \"{g_art['title']}\"")

    report = "\n".join(lines)
    print(report)
    return report


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description="Eval: compare Gemini segmentation vs. ground truth")
    parser.add_argument("--issue", required=True, help="Issue slug used in article filenames, e.g. october-1992")
    parser.add_argument("--raw-slug", help="Slug used in raw_text/ (defaults to --issue). E.g. oct-1992")
    parser.add_argument("--dry-run", action="store_true", help="Skip Gemini call, only load GT and report structure")
    parser.add_argument("--cached", action="store_true", help="Reuse existing eval_output/ instead of calling Gemini")
    args = parser.parse_args()

    issue_slug = args.issue
    raw_slug = args.raw_slug or issue_slug
    # Derive issue date from slug (e.g. october-1992 → October 1992)
    parts = issue_slug.split("-")
    issue_date = f"{parts[0].capitalize()} {parts[-1]}" if len(parts) >= 2 else issue_slug

    print(f"Loading ground truth for '{issue_slug}'...")
    gt = load_ground_truth(issue_slug)
    print(f"  Found {len(gt)} ground truth articles")

    if args.dry_run:
        print("\n[dry-run] Skipping Gemini call. Ground truth articles:")
        for a in gt:
            print(f"  - \"{a['title']}\"  pages={a['pages']}  author={a['author']}")
        return

    if args.cached:
        out_dir = EVAL_DIR / issue_slug
        if not out_dir.exists():
            print(f"ERROR: No cached output at {out_dir}. Run without --cached first.")
            sys.exit(1)
        print(f"Loading cached Gemini output from {out_dir}...")
        gemini_articles = load_gemini_output(issue_slug)
    else:
        print("Running Gemini segmentation...")
        raw_articles = run_gemini(raw_slug, issue_date)
        if raw_articles is None:
            sys.exit(1)
        out_dir = save_gemini_output(raw_articles, issue_slug, issue_date)
        print(f"  Saved {len(raw_articles)} articles to {out_dir}")
        gemini_articles = load_gemini_output(issue_slug)

    gemini_articles = filter_boilerplate(gemini_articles)
    print(f"  Gemini produced {len(gemini_articles)} articles (after boilerplate filter)\n")

    result = compare(gt, gemini_articles)
    report = print_report(result, issue_slug)

    report_path = EVAL_DIR / issue_slug / "report.txt"
    report_path.write_text(report, encoding="utf-8")
    print(f"\nReport saved → {report_path}")


if __name__ == "__main__":
    main()
