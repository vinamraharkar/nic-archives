#!/usr/bin/env python3
"""
Regenerate ONLY the negative queries in golden_set.json.
Preserves all specific and broad queries unchanged.

The old negatives were poorly constructed — many described NIC's actual work
(e-governance, state IT departments, queries containing "NIC").
New negatives are truly off-topic: consumer goods, weather, sports, etc.

Usage: python3 pipeline/regen_negatives.py
"""

from __future__ import annotations
import json
import re
import sys
import time
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
GOLDEN_SET_PATH = BASE_DIR / "eval/golden_set.json"

from dotenv import load_dotenv
load_dotenv(BASE_DIR / ".env")
import os
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
GROQ_MODEL = "llama-3.1-8b-instant"

NEGATIVE_PROMPT = """\
You are generating test queries for a search system that covers India's NIC Informatics newsletter (1992–2026).

The newsletter covers: e-governance, government IT projects, state IT departments, NIC activities,
digital India, district computerisation, software for government use, election systems, land records,
court management, tax systems, passport systems, etc.

I need a NEGATIVE test query — something a user might search that returns ZERO relevant results
because the topic is completely outside this newsletter's scope.

Context article (just for topic avoidance — the negative should be unrelated to this AND to NIC's entire domain):
Title: {title}
Date: {issue_date}
Section: {section}

Generate 1 negative query about a topic that is definitively NOT in the NIC newsletter.

Rules:
- Must NOT mention "NIC" or "e-governance" or "digital governance" or "government IT"
- Must NOT be about state IT departments, district computerisation, or Indian government technology
- Must be about a genuinely unrelated domain: consumer products, cooking, sports, weather,
  medical procedures, private sector companies, scientific research, entertainment, etc.
- Should sound like a plausible search query (3-10 words)

Return valid JSON only (no markdown):
{{"query": "..."}}"""


def _groq_call(client, prompt: str, retries: int = 3) -> str:
    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model=GROQ_MODEL,
                messages=[{"role": "user", "content": prompt}],
            )
            return response.choices[0].message.content
        except Exception as exc:
            if attempt == retries - 1:
                raise
            wait = 2 ** attempt
            print(f"  Groq error (attempt {attempt + 1}): {exc}. Retry in {wait}s...")
            time.sleep(wait)
    return ""


def is_bad_negative(query: str) -> bool:
    q = query.lower()
    bad_terms = [
        "nic", "e-governance", "e governance", "digital governance",
        "government it", "state it", "it department", "e-procurement",
        "digital india", "icт", "ict", "computeris", "computeriz",
    ]
    return any(t in q for t in bad_terms)


def main() -> None:
    from groq import Groq
    client = Groq(api_key=GROQ_API_KEY)

    with open(GOLDEN_SET_PATH) as f:
        golden = json.load(f)

    negatives = [q for q in golden if q["type"] == "negative"]
    non_negatives = [q for q in golden if q["type"] != "negative"]

    print(f"Golden set: {len(golden)} total, {len(negatives)} negatives to regenerate")
    print(f"Keeping {len(non_negatives)} specific + broad queries unchanged")
    print()

    # For each negative, we need the source article context
    source_by_slug: dict[str, dict] = {}
    for q in golden:
        if q["type"] == "specific" and "source_article" in q:
            source_by_slug[q["source_article"]] = {
                "title": q["title"],
                "issue_date": q["issue_date"],
                "section": q.get("section", ""),
            }

    new_negatives = []
    for i, neg in enumerate(negatives):
        source_slug = neg.get("source_article", "")
        meta = source_by_slug.get(source_slug, {
            "title": source_slug,
            "issue_date": neg.get("issue_date", ""),
            "section": neg.get("section", ""),
        })

        prompt = NEGATIVE_PROMPT.format(
            title=meta["title"],
            issue_date=meta["issue_date"],
            section=meta["section"],
        )

        for attempt in range(3):
            try:
                raw = _groq_call(client, prompt)
                raw = re.sub(r"^```(?:json)?\s*", "", raw.strip())
                raw = re.sub(r"\s*```$", "", raw.strip())
                parsed = json.loads(raw)
                new_query = parsed["query"].strip()

                if is_bad_negative(new_query):
                    print(f"  [{i+1}/{len(negatives)}] Bad negative generated, retrying: {new_query}")
                    continue

                new_neg = {**neg, "query": new_query}
                new_negatives.append(new_neg)
                print(f"  [{i+1}/{len(negatives)}] {source_slug[:40]:<40} → {new_query}")
                break
            except Exception as exc:
                print(f"  [{i+1}/{len(negatives)}] Error: {exc}")
                if attempt == 2:
                    new_negatives.append(neg)  # keep original on total failure
                continue

        time.sleep(0.3)  # small delay to avoid rate limits

    # Reconstruct golden set: non-negatives first (preserving order), then new negatives
    updated = non_negatives + new_negatives
    with open(GOLDEN_SET_PATH, "w") as f:
        json.dump(updated, f, indent=2, ensure_ascii=False)

    print()
    print(f"Updated golden_set.json: {len(updated)} entries ({len(new_negatives)} new negatives)")
    print()
    print("Sample new negatives:")
    for q in new_negatives[:5]:
        print(f"  {q['query']}")


if __name__ == "__main__":
    main()
