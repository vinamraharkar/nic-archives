#!/usr/bin/env python3
"""
Fix the 13 flagged query triplets identified by review_queries.py.

Uses llama-3.1-8b-instant with response_format=json_object to guarantee clean output.
Reads article bodies for context, fixes only flagged articles, merges with the 27
good originals from review.html, writes eval/golden_set.json.

Token cost: ~10k tokens total (13 calls × ~750 tokens each).
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
GOLDEN_SET_PATH = EVAL_DIR / "golden_set.json"

load_dotenv(BASE_DIR / ".env")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
GROQ_MODEL = "llama-3.1-8b-instant"

# ── Exact issues from review_queries.py output (no re-review needed) ──────────

FLAGGED: dict[str, dict[str, str]] = {
    "andhra-pradesh-empowering-through-innovation-driving-digital-transformation-with-it-july-2025": {
        "specific": "too generic — would match many AP IT articles",
        "broad": "too vague — 'India state government digital transformation' matches everything",
        "negative": "too obviously unrelated — healthcare has no surface plausibility",
    },
    "compose-comprehensive-operations-and-management-of-presses-over-secure-environment-april-2024": {
        "specific": "too generic — 'digital gazette publishing' matches many articles",
        "broad": "too vague — 'e-governance initiatives in kerala' is too wide",
        "negative": "too obviously unrelated — agriculture has no plausibility for a press system",
    },
    "computers-in-court-july-1992": {
        "specific": "too generic — 'Patna high court computerization' is a title paraphrase",
        "broad": "too vague — 'Indian judiciary system automation' is too wide",
        "negative": "too obviously unrelated — NIC network infrastructure has no plausibility for a court article",
    },
    "esajag-mobile-app-launched-by-district-collector-jaisalmer-rajasthan-july-2021": {
        "negative": "false negative — uses 'eSAJAG' which is the article's own app name; must use different app/system name entirely",
    },
    "getotp-a-smart-companion-for-reliable-otp-delivery-july-2025": {
        "specific": "too generic — 'reliable OTP delivery solutions for e-governance' matches many articles",
        "negative": "too obviously unrelated — blockchain land records has no plausibility for an OTP article",
    },
    "jhalawar-leading-ict-in-the-land-of-jhala-kings-april-2013": {
        "specific": "too generic — 'Jhalawar district e-governance projects' is a title paraphrase; need specific system names from the article",
        "negative": "too obviously unrelated — traditional crafts industry has no plausibility for an ICT governance article",
    },
    "national-voter-s-services-portal-april-2016": {
        "specific": "too generic — 'India election commission online voter services' matches many election articles",
        "negative": "too obviously unrelated — NIC newsletter subscription has no surface plausibility",
    },
    "nsic-october-1998": {
        "specific": "title paraphrase — need specific technical details like the IT system deployed or features described in the article",
        "negative": "too obviously unrelated — employee pension schemes has no plausibility for an NSIC IT article",
    },
    "pearl-suite-property-registration-for-government-of-kerala-july-2015": {
        "specific": "too generic — need specific features/modules of PEARL Suite mentioned in the article",
        "negative": "too obviously unrelated — Kerala tourism has no plausibility for a property registration system",
    },
    "sirmaur-ict-revolutionising-governance-october-2012": {
        "specific": "too generic — 'e-governance projects in Sirmaur district' is a title paraphrase; need specific system/scheme names",
        "broad": "too vague — 'ICT in rural governance' is too wide",
        "negative": "too obviously unrelated — cybersecurity/AI has no plausibility for a district ICT article",
    },
    "ullas-october-2025": {
        "specific": "too generic — 'digital platform for inclusive education' could match many articles; need ULLAS-specific program details",
        "negative": "nonsensical — 'ULLAS space exploration' uses the article's own acronym; must not use ULLAS at all",
    },
    "uttar-pradesh-striding-to-transform-into-uttam-pradesh-of-good-governance-january-2019": {
        "specific": "too generic — 'NIC Uttar Pradesh State Centre e-Governance services' is a title paraphrase",
        "negative": "too obviously unrelated — national cybersecurity policies has no plausibility for a UP e-governance article",
    },
    "webinar-series-of-nic-turns-2-january-2020": {
        "specific": "too generic — need the specific topics/themes covered in the NIC webinar series",
        "broad": "too vague — 'NIC training and development programs' is too wide",
        "negative": "too obviously unrelated — data center infrastructure has no plausibility for a webinar series article",
    },
}

SYSTEM_MSG = "You are a JSON API. Output only a valid JSON object with no surrounding text, no markdown fences, no explanation."

FIX_PROMPT = """\
Generate improved search queries for this NIC Informatics newsletter article (India e-governance, 1992-2026).

Article: {title} | {issue_date} | {section}
Slug: {slug}
Body:
{body}

Current queries and their problems:
- SPECIFIC "{specific_old}": {specific_issue}
- BROAD "{broad_old}": {broad_issue}
- NEGATIVE "{negative_old}": {negative_issue}

Rules:
SPECIFIC — Must use specific proper nouns, system names, or technical terms from the body above. Only this article should rank #1. Not a title paraphrase.
BROAD — A research-interest framing, narrow enough to return <20 results (e.g. "PEARL Suite property registration Kerala NIC" not "e-governance Kerala").
NEGATIVE — A plausible govt-IT query a researcher might actually type, but using a DIFFERENT system, department, or state than this article. Must not contain any names or acronyms from this article.

Return this JSON object (no other text):
{{"specific":{{"query":"...","expected_slugs":["{slug}"]}},"broad":{{"query":"...","expected_slugs":["{slug}"]}},"negative":{{"query":"..."}}}}"""


def _groq_call(client, slug: str, article: dict, body: str, issues: dict[str, str]) -> dict | None:
    specific_issue = issues.get("specific", "none — keep as is")
    broad_issue = issues.get("broad", "none — keep as is")
    negative_issue = issues.get("negative", "none — keep as is")

    prompt = FIX_PROMPT.format(
        title=article["title"],
        issue_date=article["issue_date"],
        section=article["section"],
        slug=slug,
        body=body[:1200],
        specific_old=article["specific"]["query"],
        broad_old=article["broad"]["query"],
        negative_old=article["negative"]["query"],
        specific_issue=specific_issue,
        broad_issue=broad_issue,
        negative_issue=negative_issue,
    )

    for attempt in range(3):
        try:
            response = client.chat.completions.create(
                model=GROQ_MODEL,
                messages=[
                    {"role": "system", "content": SYSTEM_MSG},
                    {"role": "user", "content": prompt},
                ],
                response_format={"type": "json_object"},
                max_tokens=400,
                temperature=0.2,
            )
            raw = response.choices[0].message.content
            return json.loads(raw)
        except json.JSONDecodeError as exc:
            print(f"\n    parse error attempt {attempt+1}: {exc} | raw: {raw[:120]}")
        except Exception as exc:
            if attempt == 2:
                raise
            wait = 2 ** attempt
            print(f"\n    API error attempt {attempt+1}: {exc}. Retry in {wait}s...")
            time.sleep(wait)
    return None


def load_proposals() -> dict[str, dict]:
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
        entry[p["type"]] = {"query": p["query"], "expected_slugs": p.get("expected_slugs", [])}
    return by_article


def load_body(slug: str) -> str:
    path = ARTICLES_DIR / f"{slug}.md"
    if not path.exists():
        return ""
    text = path.read_text()
    parts = text.split("---", 2)
    return parts[2].strip() if len(parts) >= 3 else text.strip()


def main() -> None:
    if not GROQ_API_KEY:
        sys.exit("GROQ_API_KEY not set")

    from groq import Groq
    client = Groq(api_key=GROQ_API_KEY)

    articles = load_proposals()
    failed: list[str] = []

    print(f"Fixing {len(FLAGGED)} flagged articles using {GROQ_MODEL} (JSON mode)...")

    for i, (slug, issues) in enumerate(FLAGGED.items(), 1):
        article = articles[slug]
        body = load_body(slug)
        print(f"  [{i:02d}/{len(FLAGGED)}] {article['title'][:55]}", end="", flush=True)

        result = _groq_call(client, slug, article, body, issues)

        if result and all(k in result for k in ("specific", "broad", "negative")):
            # Only replace the flagged query types; keep unflagged ones intact
            for qtype in ("specific", "broad", "negative"):
                if qtype in issues:
                    new_q = result[qtype]
                    if isinstance(new_q, dict):
                        articles[slug][qtype] = {
                            "query": new_q["query"],
                            "expected_slugs": new_q.get("expected_slugs", [slug] if qtype != "negative" else []),
                        }
                    else:
                        articles[slug][qtype] = {"query": str(new_q), "expected_slugs": []}
            print(f"  ✓ fixed: {', '.join(issues.keys())}")
        else:
            print(f"  ✗ failed — keeping original")
            failed.append(slug)

        time.sleep(0.3)

    # Build golden set
    golden = []
    for slug in sorted(articles.keys()):
        art = articles[slug]
        for qtype in ("specific", "broad", "negative"):
            q = art[qtype]
            golden.append({
                "id": f"{slug}:{qtype}",
                "type": qtype,
                "query": q["query"],
                "expected_slugs": q.get("expected_slugs", []),
                "source_article": slug,
                "title": art["title"],
                "issue_date": art["issue_date"],
                "section": art["section"],
                "decade": art.get("decade", ""),
            })

    GOLDEN_SET_PATH.write_text(json.dumps(golden, indent=2))

    print(f"\n{'='*60}")
    print(f"golden_set.json: {len(golden)} entries ({len(articles)} articles × 3 queries)")
    if failed:
        print(f"Failed (kept originals for): {failed}")
    else:
        print("All 13 fixed successfully.")
    print(f"\nNext: python pipeline/eval_search.py --calibrate-judge")


if __name__ == "__main__":
    main()
