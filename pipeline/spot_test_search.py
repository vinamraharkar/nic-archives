#!/usr/bin/env python3
"""
Quick spot-test for local search quality.
Tests only the 15 specific-query articles that ARE in vectors.ndjson.
Gives honest quality signal without misleading incompleteness failures.

Usage:  python3 pipeline/spot_test_search.py
"""

from __future__ import annotations
import json
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(Path(__file__).parent))

# Reuse local search from eval_search
from eval_search import _load_local_index, _jina_embed_query, local_search
from dotenv import load_dotenv
load_dotenv(BASE_DIR / ".env")


def run() -> None:
    # --- 1. Find which golden-set specific articles are in local index ----------
    local_slugs: set[str] = set()
    with open(BASE_DIR / "pipeline/vectors.ndjson") as f:
        for line in f:
            d = json.loads(line)
            slug = d.get("id", "")
            base = slug.rsplit("__c", 1)[0] if "__c" in slug else slug
            local_slugs.add(base)

    with open(BASE_DIR / "eval/golden_set.json") as f:
        golden = json.load(f)

    testable = [
        q for q in golden
        if q["type"] == "specific" and q["source_article"] in local_slugs
    ]
    broad = [q for q in golden if q["type"] == "broad"]
    negatives = [q for q in golden if q["type"] == "negative"]

    print(f"Local index: {len(local_slugs):,} articles")
    print(f"Specific queries testable locally: {len(testable)}/40")
    print(f"Broad queries: {len(broad)}")
    print(f"Negative queries: {len(negatives)}")
    print()

    # --- 2. Pre-load index once --------------------------------------------------
    print("Loading local index (embedding via Jina)...")
    _load_local_index()
    print()

    # --- 3. Specific queries -----------------------------------------------------
    print("=" * 70)
    print("SPECIFIC QUERIES — does target article appear in top results?")
    print("=" * 70)

    hits_at_1 = hits_at_3 = hits_at_5 = hits_at_10 = 0
    for q in testable:
        target = q["source_article"]
        results = local_search(q["query"], limit=10)
        slugs_returned = [r["slug"] for r in results]

        rank = None
        for i, s in enumerate(slugs_returned):
            if s == target:
                rank = i + 1
                break

        if rank == 1: hits_at_1 += 1
        if rank and rank <= 3: hits_at_3 += 1
        if rank and rank <= 5: hits_at_5 += 1
        if rank and rank <= 10: hits_at_10 += 1

        rank_str = f"rank {rank}" if rank else "NOT FOUND"
        top1_slug = slugs_returned[0] if slugs_returned else "(no results)"
        score1 = results[0]["score"] if results else 0.0
        flag = "✓" if rank == 1 else ("~" if rank and rank <= 5 else "✗")
        print(f"{flag} [{q['decade']}] {q['title'][:45]:<45}")
        print(f"   Query: {q['query'][:70]}")
        print(f"   Target: {target}")
        print(f"   Result: {rank_str} | top1: {top1_slug} (score={score1:.3f})")
        print()

    n = len(testable)
    print(f"Precision@1 : {hits_at_1}/{n} = {hits_at_1/n:.2%}")
    print(f"Recall@3    : {hits_at_3}/{n} = {hits_at_3/n:.2%}")
    print(f"Recall@5    : {hits_at_5}/{n} = {hits_at_5/n:.2%}")
    print(f"Recall@10   : {hits_at_10}/{n} = {hits_at_10/n:.2%}")
    print()

    # --- 4. Sample broad queries -------------------------------------------------
    print("=" * 70)
    print("SAMPLE BROAD QUERIES — do results look topically relevant?")
    print("=" * 70)
    import random; random.seed(42)
    sample_broad = random.sample(broad, min(8, len(broad)))
    for q in sample_broad:
        results = local_search(q["query"], limit=5)
        print(f"Query: {q['query']}")
        for i, r in enumerate(results[:5], 1):
            print(f"  {i}. [{r.get('issue_date','?')}] {r.get('title','?')[:60]} (score={r['score']:.3f})")
        print()

    # --- 5. Negative queries — should score LOW ----------------------------------
    print("=" * 70)
    print("NEGATIVE QUERIES — scores should be ≤ 0.50 (not NIC-related topics)")
    print("=" * 70)
    import random; random.seed(42)
    sample_neg = random.sample(negatives, min(8, len(negatives)))
    high_fp = 0
    for q in sample_neg:
        results = local_search(q["query"], limit=1)
        top_score = results[0]["score"] if results else 0.0
        flag = "✗ FP" if top_score > 0.50 else "✓"
        if top_score > 0.50: high_fp += 1
        top_slug = results[0]["slug"] if results else "(none)"
        print(f"{flag} score={top_score:.3f} | {q['query'][:60]}")
        print(f"      top: {top_slug}")
    print()
    print(f"False positives (score > 0.50): {high_fp}/{len(sample_neg)}")


if __name__ == "__main__":
    run()
