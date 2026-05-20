#!/usr/bin/env python3
"""
LLM-based review of the 120 query proposals in eval/review.html.

For each article triplet (specific / broad / negative), reads the full article
body and asks Groq to flag inconsistencies.

Outputs a Markdown report to eval/reports/query_review.md.
"""

from __future__ import annotations

import json
import os
import re
import sys
import time
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).parent.parent
ARTICLES_DIR = BASE_DIR / "articles"
EVAL_DIR = BASE_DIR / "eval"
REVIEW_HTML = EVAL_DIR / "review.html"
REPORT_PATH = EVAL_DIR / "reports" / "query_review.md"

load_dotenv(BASE_DIR / ".env")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
GROQ_MODEL = "llama-3.3-70b-versatile"

REVIEW_PROMPT = """\
You are an expert evaluator auditing search query quality for a research archive.

You will be given:
- A full article from the NIC Informatics newsletter (India's national e-governance publication)
- Three search queries generated for that article:
  1. SPECIFIC — should ONLY match this article (high precision)
  2. BROAD — should match this article + other thematically related articles
  3. NEGATIVE — plausible-sounding but should NOT match this article at all

Your job: identify problems with any of the three queries. Flag:
- SPECIFIC is too generic (would match many articles, not just this one)
- SPECIFIC is just a rephrasing of the title
- SPECIFIC would miss the article (wrong terminology/framing)
- BROAD is too narrow (effectively the same as SPECIFIC)
- BROAD is too vague to be useful as a test query
- NEGATIVE would actually match this article (false negative)
- NEGATIVE is too obviously unrelated (no surface-level plausibility — trivially wrong)
- Any query is poorly worded, confusing, or untestable

Article:
Title: {title}
Date: {issue_date}
Section: {section}
Full body:
{body}

Queries:
SPECIFIC: "{specific}"
BROAD: "{broad}"
NEGATIVE: "{negative}"

Respond with a concise JSON object only (no markdown fences, no explanation outside JSON):
{{
  "ok": true/false,
  "issues": [
    {{"query": "specific|broad|negative", "problem": "brief description"}}
  ],
  "verdict": "one sentence summary — either 'All queries look good' or what needs fixing"
}}

If there are no issues, return {{"ok": true, "issues": [], "verdict": "All queries look good."}}
"""


def _groq_client():
    from groq import Groq
    return Groq(api_key=GROQ_API_KEY)


def _groq_call(client, prompt: str, retries: int = 3) -> str:
    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model=GROQ_MODEL,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.1,
            )
            return response.choices[0].message.content
        except Exception as exc:
            if attempt == retries - 1:
                raise
            wait = 2 ** attempt
            print(f"  Groq error (attempt {attempt + 1}): {exc}. Retry in {wait}s...")
            time.sleep(wait)
    return ""


def load_proposals() -> dict[str, dict]:
    """Returns {slug: {specific, broad, negative, title, issue_date, section}}"""
    content = REVIEW_HTML.read_text()
    m = re.search(r"const P=(\[[\s\S]+?\]);\n", content)
    if not m:
        sys.exit("Could not find P= array in review.html")
    proposals = json.loads(m.group(1))

    by_article: dict[str, dict] = {}
    for p in proposals:
        slug = p["source_article"]
        entry = by_article.setdefault(slug, {
            "slug": slug,
            "title": p["title"],
            "issue_date": p["issue_date"],
            "section": p["section"],
            "decade": p.get("decade", ""),
        })
        entry[p["type"]] = p["query"]
    return by_article


def load_article_body(slug: str) -> str:
    path = ARTICLES_DIR / f"{slug}.md"
    if not path.exists():
        return ""
    text = path.read_text()
    parts = text.split("---", 2)
    return parts[2].strip() if len(parts) >= 3 else text.strip()


def review_triplet(client, article: dict) -> dict:
    body = load_article_body(article["slug"])
    if not body:
        return {"ok": False, "issues": [{"query": "all", "problem": "Article file not found"}], "verdict": "File missing"}

    prompt = REVIEW_PROMPT.format(
        title=article["title"],
        issue_date=article["issue_date"],
        section=article["section"],
        body=body[:4000],
        specific=article.get("specific", ""),
        broad=article.get("broad", ""),
        negative=article.get("negative", ""),
    )

    raw = _groq_call(client, prompt)
    # Strip markdown fences if present
    raw = re.sub(r"^```(?:json)?\s*", "", raw.strip())
    raw = re.sub(r"\s*```$", "", raw.strip())
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {"ok": False, "issues": [{"query": "all", "problem": f"LLM returned unparseable response: {raw[:200]}"}], "verdict": "Parse error"}


def main() -> None:
    if not GROQ_API_KEY:
        sys.exit("GROQ_API_KEY not set")

    articles = load_proposals()
    client = _groq_client()

    print(f"Reviewing {len(articles)} article triplets with {GROQ_MODEL}...")

    results: list[dict] = []
    flagged: list[dict] = []

    for i, (slug, article) in enumerate(sorted(articles.items()), 1):
        print(f"  [{i:02d}/{len(articles)}] {article['title'][:60]}", end="", flush=True)
        review = review_triplet(client, article)
        record = {**article, "review": review}
        results.append(record)
        if not review.get("ok", True):
            flagged.append(record)
            print(f"  ⚠ {len(review.get('issues', []))} issue(s)")
        else:
            print("  ✓")
        time.sleep(0.5)  # be nice to rate limits

    # Write report
    lines = [
        "# Query Review Report",
        f"\nReviewed: {len(results)} articles | Flagged: {len(flagged)} | OK: {len(results) - len(flagged)}",
        f"\nModel: {GROQ_MODEL}\n",
    ]

    if flagged:
        lines.append("## Flagged Triplets\n")
        for r in flagged:
            lines.append(f"### {r['title']} ({r['issue_date']})")
            lines.append(f"- Slug: `{r['slug']}`")
            lines.append(f"- SPECIFIC: `{r.get('specific', '')}`")
            lines.append(f"- BROAD: `{r.get('broad', '')}`")
            lines.append(f"- NEGATIVE: `{r.get('negative', '')}`")
            lines.append(f"\n**Verdict:** {r['review'].get('verdict', '')}\n")
            for issue in r["review"].get("issues", []):
                lines.append(f"- **{issue['query'].upper()}**: {issue['problem']}")
            lines.append("")

    lines.append("\n---\n## All Results\n")
    lines.append("| Decade | Title | S | B | N | Issues |")
    lines.append("|--------|-------|---|---|---|--------|")
    for r in sorted(results, key=lambda x: (x.get("decade", ""), x["title"])):
        rev = r["review"]
        issues_by_type = {iss["query"]: iss["problem"] for iss in rev.get("issues", [])}
        s = "✓" if "specific" not in issues_by_type else "⚠"
        b = "✓" if "broad" not in issues_by_type else "⚠"
        n = "✓" if "negative" not in issues_by_type else "⚠"
        issue_text = "; ".join(f"{k}: {v}" for k, v in issues_by_type.items()) or ""
        title = r["title"][:45].replace("|", "/")
        lines.append(f"| {r.get('decade','')} | {title} | {s} | {b} | {n} | {issue_text} |")

    REPORT_PATH.write_text("\n".join(lines))
    print(f"\n{'='*60}")
    print(f"Flagged: {len(flagged)}/{len(results)} triplets need attention")
    print(f"Report: {REPORT_PATH}")

    # Also print flagged summary to stdout
    if flagged:
        print("\nFlagged articles:")
        for r in flagged:
            print(f"\n  {r['title']} ({r['issue_date']})")
            for issue in r["review"].get("issues", []):
                print(f"    [{issue['query'].upper()}] {issue['problem']}")
            print(f"  → {r['review'].get('verdict', '')}")


if __name__ == "__main__":
    main()
