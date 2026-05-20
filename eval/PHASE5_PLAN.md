# Phase 5: Semantic Search Evaluation System
## NIC Archives — Comprehensive Eval Plan

**Status:** Planning complete, implementation pending  
**Script:** `pipeline/eval_search.py`  
**Worker:** `https://nic-archives-search.nicarchives.workers.dev`  
**Last updated:** 2026-05-18

---

## Purpose

An **ongoing regression test suite** — not a one-time quality check. Re-run after every pipeline change, embedding model update, or worker prompt edit. Exits with code 0 (pass) or 1 (fail) — CI-ready.

**What it catches:**
- Embedding or model changes that silently degrade search quality
- Pipeline regressions where certain articles drop out of results
- `/ask` answers that drift from grounded to hallucinated
- Systemic failures (entire decade of articles disappearing from results)

---

## Directory Structure

```
eval/
├── PHASE5_PLAN.md           ← this file
├── config.json              ← seed, thresholds, worker URL
├── golden_set.json          ← human-approved queries + expected slugs (committed)
├── eval_judgments.json      ← cached LLM judge scores (committed, grows over time)
├── baseline.json            ← last known-good scores (committed, updated manually)
└── reports/
    └── YYYY-MM-DD.json      ← per-run output (NOT committed, gitignored)
pipeline/
└── eval_search.py           ← the script (all modes in one file)
```

---

## eval/config.json

```json
{
  "sample_seed": 42,
  "min_body_chars": 500,
  "articles_per_decade": 10,
  "worker_url": "https://nic-archives-search.nicarchives.workers.dev",
  "thresholds": {
    "precision_at_1": 0.85,
    "ndcg_at_10_warn": 0.70,
    "negative_max_score": 0.50
  }
}
```

**Notes:**
- `sample_seed: 42` ensures the same 40 articles are always selected on `--build-golden` rebuild
- `min_body_chars: 500` excludes 54 stub articles (< 300 chars exist; 500 is safe margin)
- `articles_per_decade: 10` × 4 decades = 40 articles total
- `precision_at_1: 0.85` = 34/40 queries must rank expected article #1 (hard gate)
- `ndcg_at_10_warn: 0.70` = soft warning only, does not block shipping
- `negative_max_score: 0.50` = any negative query returning a result with similarity > 0.50 is flagged

---

## Script Modes

```bash
# Step 1 (run once to build ground truth)
python pipeline/eval_search.py --build-golden

# Step 2 (run once to calibrate the LLM judge)
python pipeline/eval_search.py --calibrate-judge

# Step 3 (run every time before shipping a change)
python pipeline/eval_search.py --run

# After a passing run, update the baseline
python pipeline/eval_search.py --set-baseline

# When a run fails, inspect only the regressions
python pipeline/eval_search.py --review-failures
```

---

## Step 1: `--build-golden` (One-time setup)

### 1a. Stratified Sampling

Select 40 articles from `articles/*.md`:
- **10 per decade**: 1990s, 2000s, 2010s, 2020s
- **Filter**: body length ≥ 500 chars (skip stubs)
- **Seeded**: `random.seed(config["sample_seed"])` before sampling — same 40 every rebuild
- Decade is extracted from the filename date suffix (e.g., `april-1995` → 1990s)

Decade article counts (for reference):
- 1990s: 452 articles
- 2000s: 1,204 articles
- 2010s: 1,298 articles
- 2020s: 909 articles

### 1b. LLM Query Generation (Gemini per article)

For each of the 40 sampled articles, send to Gemini:

**Prompt:**
```
You are reading an article from the NIC Informatics newsletter, India's national e-governance publication.
Generate 3 search queries that a researcher might type to find this or related content.

Article details:
Title: {title}
Date: {issue_date}
Section: {section}
Body (first 2000 chars): {body[:2000]}
Slug: {slug}

Generate exactly 3 queries:

1. SPECIFIC — A precise query directly targeting this article's main topic.
   Must NOT be a rephrasing of the title. Should reflect real user intent.
   Expected: only this article should rank #1.

2. BROAD — A thematic query about the general topic area.
   This article should be one of several good results (not necessarily #1).
   Expected: this article + 1-2 other plausible articles from the archive.

3. NEGATIVE — A plausible tech/government query that sounds related but should NOT
   match this article. Tests that the system doesn't hallucinate relevance.
   Expected: no relevant results.

Return valid JSON only:
{{
  "specific": {{
    "query": "...",
    "expected_slugs": ["{slug}"]
  }},
  "broad": {{
    "query": "...",
    "expected_slugs": ["{slug}"]
  }},
  "negative": {{
    "query": "..."
  }}
}}
```

**Notes on broad queries:** The LLM only populates `expected_slugs` with the current article. During HTML review (step 1c), the human adds additional slugs they know should also match.

### 1c. HTML Review Interface

The script generates `eval/review.html` — a self-contained HTML file.

**What it shows per article (40 cards):**
- Article title, date, section (header)
- First 400 chars of body (context)
- Three query rows, each with:
  - Query type label (SPECIFIC / BROAD / NEGATIVE)
  - Editable query text field
  - Editable `expected_slugs` field (comma-separated; blank for NEGATIVE)
  - Approve / Reject toggle

**At the bottom:**
- "Download golden_set.json" button — triggers browser download of all approved queries as JSON
- Human saves downloaded file to `eval/golden_set.json`
- No server needed — pure client-side JS

**Human review tasks:**
1. For SPECIFIC queries: verify the query reflects real user intent, not just title keywords
2. For BROAD queries: add 1-2 additional slugs you know should also match (from memory or quick search)
3. For NEGATIVE queries: verify the query truly shouldn't match the article
4. Reject any query that seems too obvious, too obscure, or incorrectly framed
5. Edit query text freely — LLM suggestions are starting points

**Expected output:** ~80–100 approved entries (some rejected; negative queries have no expected_slugs).

### 1d. golden_set.json Format

```json
[
  {
    "id": "Q001",
    "type": "specific",
    "query": "how did NIC computerize income tax collection in the 1990s",
    "expected_slugs": ["all-set-for-tax-computerization-october-1992"],
    "source_article": "all-set-for-tax-computerization-october-1992",
    "decade": "1990s"
  },
  {
    "id": "Q002",
    "type": "broad",
    "query": "NIC role in financial sector computerization",
    "expected_slugs": [
      "all-set-for-tax-computerization-october-1992",
      "financial-management-informatics-project-october-1992"
    ],
    "source_article": "all-set-for-tax-computerization-october-1992",
    "decade": "1990s"
  },
  {
    "id": "Q003",
    "type": "negative",
    "query": "machine learning neural networks image classification",
    "expected_slugs": [],
    "source_article": "all-set-for-tax-computerization-october-1992",
    "decade": "1990s"
  }
]
```

---

## Step 2: `--calibrate-judge` (One-time calibration)

Before caching any LLM judge scores, verify the judge prompt produces scores that match human intuition.

**Process:**
1. Script selects 5 random queries from `golden_set.json`
2. POSTs each to the worker `/search`, takes top-4 results = 20 (query, result) pairs
3. Calls Gemini judge on all 20
4. Prints full context for human review:
   ```
   ─────────────────────────────────────────
   Query: "rural district computerization 1990s"
   Result slug: collectorate-gadchiroli-maharshtra-april-2003
   Title: Collectorate, Gadchiroli, Maharashtra
   Date: April 2003
   Snippet: "NIC established a district unit at Gadchiroli..."
   Judge score: 2 (highly relevant)
   Your assessment? [y/n/override]:
   ─────────────────────────────────────────
   ```
5. If ≥ 3 of 20 scores disagree with human: edit the judge prompt in the script and re-run calibration

**LLM Judge Prompt (Gemini):**
```
You are evaluating search results for an archive of NIC Informatics newsletter articles (1992–2026).
NIC is India's National Informatics Centre — the government body that built e-governance systems.

Query: {query}
Article title: {title}
Article date: {issue_date}
Article snippet (first 300 chars): {snippet}

Score the relevance of this article to the query:
0 = Not relevant (different topic, wrong era, or misleading match)
1 = Partially relevant (related area but not a strong match for this query)
2 = Highly relevant (directly answers or strongly addresses the query)

Return only the integer 0, 1, or 2. No explanation.
```

---

## Step 3: `--run` (Regression test — run repeatedly)

### 3a. Search Evaluation

For each query in `golden_set.json`:

1. POST `{"query": q["query"], "limit": 10}` to `{worker_url}/search`
2. Receive top-10 results: `[{slug, title, snippet, score}, ...]`
3. For each (query_id, result_slug) pair:
   - Check `eval_judgments.json` — use cached score if exists
   - If not cached: call Gemini judge, store result in cache, save file
4. Compute metrics (see below)

### 3b. Ask Evaluation

For BROAD queries only (~30 queries):

1. POST `{"query": q["query"]}` to `{worker_url}/ask`
2. Receive `{answer, sources: [{slug, title, snippet}]}`
3. Send to Gemini grounding judge:
   ```
   Answer: {answer}
   Sources cited: {sources as text}
   
   Does this answer contain ONLY claims supported by the cited sources?
   0 = Contains unsupported claims or hallucinations
   1 = Mostly grounded, minor extrapolation
   2 = Fully grounded in the cited sources
   
   Return only 0, 1, or 2.
   ```
4. Cache same as search judgments (key: `ask:{query_id}`)

### 3c. Negative Query Evaluation

For NEGATIVE queries:

1. POST to `/search`, receive results
2. Check: is `results[0].score > config.thresholds.negative_max_score`?
3. If yes: flag as "false positive" — system returned confident result for a query that should match nothing

### 3d. Metrics Computation

**Precision@1 (hard gate, ≥ 0.85):**
```
For each specific query:
  rank_1_slug = results[0].slug
  hit = 1 if rank_1_slug in expected_slugs else 0
Precision@1 = sum(hits) / len(specific_queries)
```

**nDCG@10 (soft warning, ≥ 0.70):**
```
For each non-negative query:
  relevance_grades = [judge_score(result) for result in top_10]  # 0, 1, or 2
  dcg = sum(grade / log2(rank+2) for rank, grade in enumerate(grades))
  ideal_grades = sorted(relevance_grades, reverse=True)
  idcg = sum(grade / log2(rank+2) for rank, grade in enumerate(ideal_grades))
  ndcg = dcg / idcg if idcg > 0 else 0
nDCG@10 = mean(ndcg across all non-negative queries)
```

**Ask grounding score:**
```
grounding = mean(grounding_judge_scores) across all broad queries
```

### 3e. Comparison vs Baseline

Load `eval/baseline.json`. Compute delta for each metric. Identify regressions:
- A specific query is a regression if: was in top-3 in baseline, now rank > 5 OR not in top 10
- A broad query is a regression if: nDCG dropped > 0.10 vs its individual baseline score

### 3f. Terminal Output

**Passing:**
```
NIC Archives Search Eval — 2026-05-18
══════════════════════════════════════
Precision@1   : 37/40  92.5%  ✓  (baseline: 90.0%  +2.5%)
nDCG@10       : 0.74          ✓  (baseline: 0.71   +0.03)
/ask grounding: 2.1/3         ✓
Negative      : 8/8 low score ✓

RESULT: PASS — safe to ship
Full report   : eval/reports/2026-05-18.json
```

**Failing:**
```
NIC Archives Search Eval — 2026-05-18
══════════════════════════════════════
Precision@1   : 33/40  82.5%  ✗  (baseline: 90.0%  -7.5%)
nDCG@10       : 0.68          ⚠  (baseline: 0.71   -0.03)
/ask grounding: 1.8/3         ✓

RESULT: FAIL — 2 regressions
  [Q014] "rural district computerization 1990s"
         expected: collectorate-gadchiroli-maharshtra-april-2003
         got rank: 8  (was rank 1 in baseline)
  [Q031] "NICNET satellite communication"
         expected: nicnet-backbone-april-1995
         got: not in top 10  (was rank 2 in baseline)

Run --review-failures for full context. Exit code: 1
```

### 3g. Report File (`eval/reports/YYYY-MM-DD.json`)

```json
{
  "run_date": "2026-05-18T14:32:00",
  "worker_url": "https://nic-archives-search.nicarchives.workers.dev",
  "metrics": {
    "precision_at_1": 0.925,
    "ndcg_at_10": 0.74,
    "ask_grounding": 2.1,
    "negative_false_positives": 0
  },
  "pass": true,
  "queries": [
    {
      "id": "Q001",
      "query": "how did NIC computerize income tax collection in the 1990s",
      "type": "specific",
      "expected_slugs": ["all-set-for-tax-computerization-october-1992"],
      "results": [
        {"rank": 1, "slug": "all-set-for-tax-computerization-october-1992", "score": 0.91, "judge": 2},
        {"rank": 2, "slug": "financial-management-informatics-april-1995", "score": 0.78, "judge": 1}
      ],
      "precision_at_1": 1,
      "ndcg_at_10": 0.89,
      "regression": false
    }
  ]
}
```

---

## Step 4: `--set-baseline`

After a passing `--run`:
1. Copies current scores from latest report into `eval/baseline.json`
2. Prints: `Baseline updated. Commit eval/baseline.json to lock in these scores.`
3. Human commits `eval/baseline.json` to git

**baseline.json format:**
```json
{
  "set_date": "2026-05-18",
  "metrics": {
    "precision_at_1": 0.925,
    "ndcg_at_10": 0.74,
    "ask_grounding": 2.1,
    "negative_false_positives": 0
  },
  "per_query": {
    "Q001": {"rank": 1, "ndcg": 0.89},
    "Q002": {"rank": 2, "ndcg": 0.74}
  }
}
```

---

## Step 5: `--review-failures`

Shows only queries that regressed vs baseline, with full context:
- Query text
- Expected slug(s)
- Current top-5 results with judge scores
- Baseline rank vs current rank
- Possible causes (scored low by judge = embedding issue; ranked lower but still relevant = ordering issue)

---

## Robustness Rules

| Scenario | Behaviour |
|---|---|
| Worker unreachable | Skip that query, mark as `skipped`, report count at end. Don't crash. |
| Gemini judge fails | Retry 3× with exponential backoff. If still failing, mark as `unscored`. Don't crash. |
| Gemini rate limit | 1s delay between judge calls. |
| Re-run same day | Append timestamp to report filename: `2026-05-18T14:32.json` |
| New query added to golden_set | No existing cache invalidated. New pairs judged fresh. |
| golden_set.json missing | Exit with clear error: "Run --build-golden first." |
| baseline.json missing | `--run` still works, but skips regression comparison. Reports scores only. |

---

## Human-in-the-Loop Touchpoints (Summary)

| Touchpoint | When | Time cost |
|---|---|---|
| HTML review of golden set | Once, during `--build-golden` | ~20 min for 40 articles × 3 queries |
| Judge calibration review | Once, during `--calibrate-judge` | ~10 min for 20 scored pairs |
| Regression investigation | On demand, after `--run` exits 1 | ~5–15 min per regression |
| Baseline update | After any deliberate quality improvement | 2 min |

---

## Metrics Reference

| Metric | Formula | Gate | Meaning |
|---|---|---|---|
| Precision@1 | hits@1 / n_specific | ≥ 0.85 (hard) | Did the right article rank #1? |
| nDCG@10 | DCG/IDCG using judge grades | ≥ 0.70 (soft) | Quality of full top-10 ranking |
| /ask grounding | mean judge score 0–2 | Reported only | Answer stays grounded in sources |
| Negative FP rate | n_false_positives / n_negative | 0 (hard) | System doesn't hallucinate relevance |

---

## Implementation Checklist

- [ ] Create `eval/config.json`
- [ ] Implement `--build-golden`: stratified sample → Gemini query gen → `review.html`
- [ ] Implement `--calibrate-judge`: sample 5 queries → judge 20 pairs → print for review
- [ ] Implement `--run`: full eval → metrics → compare baseline → terminal report → JSON report
- [ ] Implement `--set-baseline`: copy scores to `baseline.json`
- [ ] Implement `--review-failures`: show regression diffs
- [ ] Test `--build-golden` on 5 articles before running full 40
- [ ] Run `--calibrate-judge`, manually verify 20 scores
- [ ] Run `--build-golden`, review HTML, save `golden_set.json`
- [ ] Run `--run` (first time, no baseline yet)
- [ ] Run `--set-baseline`, commit `baseline.json` and `eval_judgments.json`
- [ ] Run `--run` again to confirm it passes against its own baseline
- [ ] Add `eval/reports/` to `.gitignore`

---

## Key Design Decisions (rationale)

- **Seeded random sampling** — reproducibility. Same 40 articles every rebuild means golden set stays stable.
- **LLM generates queries, human approves** — avoids cold-start problem (writing 40 queries from memory), avoids circularity (LLM reads body, not title), human catches bad suggestions.
- **Gemini as judge, not the worker** — keeps judge independent of the system under test. Worker uses Llama/Gemini for `/ask`; judge uses Gemini directly.
- **Cached judgments** — Gemini judge is called once per (query, slug) pair ever. Re-runs are fast and cheap. Cache grows as new queries are added.
- **HTML review, not terminal y/n** — reviewing 120 query proposals in terminal is exhausting. HTML shows article context alongside the query; editing is natural.
- **Broad queries test recall, specific test precision, negative test specificity** — three query types cover all failure modes.
- **nDCG not just Precision@1** — a system that returns the right article at rank 2 instead of rank 1 is still useful; nDCG captures this. Precision@1 alone would be too harsh for broad queries.
- **Exit code 0/1** — CI-ready from day one. `python pipeline/eval_search.py --run || exit 1` works in any CI system.
