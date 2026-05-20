#!/usr/bin/env python3
"""
Semantic search evaluation system for NIC Archives.

Modes:
    --build-golden      Sample 40 articles, generate queries via Groq, produce eval/review.html
    --calibrate-judge   Run judge on 20 sample pairs, print for human visual review
    --run               Full regression test against the live worker
    --set-baseline      After a passing run, update eval/baseline.json
    --review-failures   Show regressions vs baseline in detail

See eval/PHASE5_PLAN.md for full design documentation.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import random
import re
import sys
import time
from datetime import datetime
from pathlib import Path

import numpy as np
import requests
from dotenv import load_dotenv

# ── Paths ──────────────────────────────────────────────────────────────────────

LOCAL_SEARCH_URL = "local"

BASE_DIR = Path(__file__).parent.parent
ARTICLES_DIR = BASE_DIR / "articles"
EVAL_DIR = BASE_DIR / "eval"
CONFIG_PATH = EVAL_DIR / "config.json"
GOLDEN_SET_PATH = EVAL_DIR / "golden_set.json"
JUDGMENTS_PATH = EVAL_DIR / "eval_judgments.json"
BASELINE_PATH = EVAL_DIR / "baseline.json"
REPORTS_DIR = EVAL_DIR / "reports"
REVIEW_HTML_PATH = EVAL_DIR / "review.html"

EVAL_DIR.mkdir(exist_ok=True)
REPORTS_DIR.mkdir(exist_ok=True)

load_dotenv(BASE_DIR / ".env")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
GROQ_MODEL = "llama-3.1-8b-instant"
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_JUDGE_MODEL = "gemini-2.5-flash-lite"

DEFAULT_CONFIG: dict = {
    "sample_seed": 42,
    "min_body_chars": 500,
    "articles_per_decade": 10,
    "worker_url": "https://nic-archives-search.nicarchives.workers.dev",
    "thresholds": {
        "precision_at_1": 0.85,
        "ndcg_at_10_warn": 0.70,
        "negative_max_score": 0.50,
    },
}

# ── Config ────────────────────────────────────────────────────────────────────

def load_config() -> dict:
    if CONFIG_PATH.exists():
        stored = json.loads(CONFIG_PATH.read_text())
        merged = {**DEFAULT_CONFIG, **stored}
        merged["thresholds"] = {**DEFAULT_CONFIG["thresholds"], **stored.get("thresholds", {})}
        return merged
    CONFIG_PATH.write_text(json.dumps(DEFAULT_CONFIG, indent=2))
    print(f"Created {CONFIG_PATH} with defaults.")
    return DEFAULT_CONFIG.copy()


# ── Article parsing ───────────────────────────────────────────────────────────

def parse_article(path: Path) -> dict | None:
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    fm_text, body = parts[1], parts[2].strip()

    def field(key: str) -> str:
        m = re.search(rf'^{key}:\s*"?([^"\n]+)"?', fm_text, re.MULTILINE)
        return m.group(1).strip() if m else ""

    title = field("title")
    issue_date = field("issue_date")
    if not title or not issue_date:
        return None

    return {
        "slug": path.stem,
        "title": title,
        "issue_date": issue_date,
        "section": field("section") or "Unknown",
        "body": body,
        "body_len": len(body),
    }


def decade_from_date(issue_date: str) -> str | None:
    m = re.search(r"\b(\d{4})\b", issue_date)
    if not m:
        return None
    year = int(m.group(1))
    return f"{(year // 10) * 10}s"


# ── Stratified sampling ───────────────────────────────────────────────────────

def stratified_sample(config: dict) -> list[dict]:
    decades = ["1990s", "2000s", "2010s", "2020s"]
    by_decade: dict[str, list] = {d: [] for d in decades}

    for path in ARTICLES_DIR.glob("*.md"):
        art = parse_article(path)
        if not art or art["body_len"] < config["min_body_chars"]:
            continue
        d = decade_from_date(art["issue_date"])
        if d in by_decade:
            art["decade"] = d
            by_decade[d].append(art)

    rng = random.Random(config["sample_seed"])
    n = config["articles_per_decade"]
    sample = []
    for d in decades:
        pool = by_decade[d]
        picked = rng.sample(pool, min(n, len(pool)))
        sample.extend(picked)

    print(f"Sampled {len(sample)} articles:")
    for d in decades:
        cnt = sum(1 for a in sample if a.get("decade") == d)
        print(f"  {d}: {cnt}")
    return sample


# ── Groq utilities ────────────────────────────────────────────────────────────

def _groq_client():
    from groq import Groq
    return Groq(api_key=GROQ_API_KEY)


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


QUERY_GEN_PROMPT = """\
You are reading an article from the NIC Informatics newsletter, India's national e-governance publication (1992–2026).

Generate 3 search queries that a researcher might type to find this or related content.

Article:
Title: {title}
Date: {issue_date}
Section: {section}
Slug: {slug}
Body (first 2000 chars):
{body}

Generate exactly 3 queries:

1. SPECIFIC — A precise query directly targeting this article's main topic.
   Must NOT be a rephrasing of the title. Should reflect real user intent.
   Expected: only this article should rank #1.

2. BROAD — A thematic query about the general topic area.
   This article should be one of several good results.
   Expected: this article + potentially other related articles.

3. NEGATIVE — A query about a topic that does NOT appear in the NIC Informatics
   newsletter at all. Must be genuinely outside NIC's domain (no e-governance,
   no government IT, no state IT departments, no NIC-related work).
   Good examples: consumer products, weather, sports, entertainment, private sector
   companies, agricultural science, medical procedures, space missions, recipes.
   MUST NOT contain the word "NIC". MUST NOT be about e-governance or digital
   governance. Tests that the search correctly scores non-NIC queries low.

Return valid JSON only (no markdown, no explanation):
{{
  "specific": {{"query": "...", "expected_slugs": ["{slug}"]}},
  "broad":    {{"query": "...", "expected_slugs": ["{slug}"]}},
  "negative": {{"query": "..."}}
}}"""


def generate_queries(article: dict, client) -> dict | None:
    prompt = QUERY_GEN_PROMPT.format(
        title=article["title"],
        issue_date=article["issue_date"],
        section=article["section"],
        slug=article["slug"],
        body=article["body"][:2000],
    )
    try:
        raw = _groq_call(client, prompt)
        raw = re.sub(r"^```(?:json)?\s*", "", raw.strip())
        raw = re.sub(r"\s*```$", "", raw.strip())
        return json.loads(raw)
    except Exception as exc:
        print(f"  Query gen failed for {article['slug']}: {exc}")
        return None


JUDGE_PROMPT = """\
You are evaluating search results for an archive of NIC Informatics newsletter articles (1992–2026).
NIC is India's National Informatics Centre — the government agency that built India's e-governance systems.

Query: {query}
Article title: {title}
Article date: {issue_date}
Article snippet (first 300 chars): {snippet}

Score the relevance of this article to the query:
0 = Not relevant (different topic, wrong era, or misleading match)
1 = Partially relevant (related area but not a strong match for this query)
2 = Highly relevant (directly answers or strongly addresses the query)

Return only the integer 0, 1, or 2. No explanation."""

GROUNDING_PROMPT = """\
You are checking whether an AI answer is grounded in its cited sources.

Query: {query}
AI Answer: {answer}
Cited sources:
{sources_text}

Does this answer contain ONLY claims supported by the cited sources?
0 = Contains unsupported claims or hallucinations
1 = Mostly grounded, minor extrapolation
2 = Fully grounded in the cited sources

Return only the integer 0, 1, or 2. No explanation."""


# ── Judgments cache ───────────────────────────────────────────────────────────

def load_judgments() -> dict:
    if JUDGMENTS_PATH.exists():
        return json.loads(JUDGMENTS_PATH.read_text())
    return {}


def save_judgments(cache: dict) -> None:
    JUDGMENTS_PATH.write_text(json.dumps(cache, indent=2, ensure_ascii=False))


def _gemini_judge(prompt: str) -> str:
    from google import genai
    client = genai.Client(api_key=GEMINI_API_KEY)
    r = client.models.generate_content(model=GEMINI_JUDGE_MODEL, contents=prompt)
    return r.text or ""


def judge_relevance(
    query_id: str,
    query: str,
    result: dict,
    client,
    cache: dict,
) -> int:
    cache_key = f"{query_id}:{result.get('slug', '')}"
    if cache_key in cache:
        return cache[cache_key]

    snippet = (result.get("snippet") or result.get("title") or "")[:300]
    prompt = JUDGE_PROMPT.format(
        query=query,
        title=result.get("title", ""),
        issue_date=result.get("date", result.get("issue_date", "")),
        snippet=snippet,
    )
    try:
        time.sleep(0.3)
        raw = _gemini_judge(prompt)
        m = re.search(r"\b([012])\b", raw.strip())
        score = int(m.group(1)) if m else -1
    except Exception as exc:
        print(f"  Judge error ({cache_key}): {exc}")
        score = -1  # unscored

    cache[cache_key] = score
    return score


# ── Local vector search (Vectorize quota bypass) ──────────────────────────────

_local_index: dict | None = None  # loaded once, cached for the process lifetime

VECTORS_PATH = BASE_DIR / "pipeline" / "vectors.ndjson"
JINA_API_KEY = os.environ.get("JINA_API_KEY", "")


def _load_local_index() -> dict:
    global _local_index
    if _local_index is not None:
        return _local_index
    print(f"  Loading local vector index from {VECTORS_PATH} ...", flush=True)
    slugs, titles, issue_dates, urls, snippets, vectors = [], [], [], [], [], []
    with open(VECTORS_PATH) as f:
        for line in f:
            rec = json.loads(line)
            m = rec["metadata"]
            slugs.append(m["slug"])
            titles.append(m.get("title", ""))
            issue_dates.append(m.get("issue_date", ""))
            urls.append(m.get("url", ""))
            snippets.append(m.get("body_snippet", ""))
            vectors.append(rec["values"])
    mat = np.array(vectors, dtype=np.float64)
    # Scrub any non-finite values before normalisation
    mat = np.nan_to_num(mat, nan=0.0, posinf=0.0, neginf=0.0)
    norms = np.linalg.norm(mat, axis=1, keepdims=True)
    mat = mat / np.where(norms == 0, 1, norms)  # unit-normalise rows
    mat = np.nan_to_num(mat, nan=0.0, posinf=0.0, neginf=0.0)
    _local_index = {
        "mat": mat,
        "slugs": slugs,
        "titles": titles,
        "issue_dates": issue_dates,
        "urls": urls,
        "snippets": snippets,
    }
    print(f"  Loaded {len(slugs)} vectors.", flush=True)
    return _local_index


def _jina_embed_query(query: str) -> list[float]:
    resp = requests.post(
        "https://api.jina.ai/v1/embeddings",
        headers={"Authorization": f"Bearer {JINA_API_KEY}", "Content-Type": "application/json"},
        json={"model": "jina-embeddings-v3", "task": "retrieval.query", "dimensions": 1024, "input": [query]},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()["data"][0]["embedding"]


def _query_tokens(query: str) -> set[str]:
    return {t for t in re.split(r"[\s\-_.,;:!?()+]+", query.lower()) if len(t) > 3}


def _token_overlap(q_tokens: set[str], text: str) -> float:
    if not text or not q_tokens:
        return 0.0
    words = [t for t in re.split(r"[\s\-_.,;:!?()+]+", text.lower()) if len(t) > 3]
    return sum(1 for w in words if w in q_tokens) / len(q_tokens)


def local_search(query: str, limit: int = 10) -> list[dict]:
    idx = _load_local_index()
    qvec = np.array(_jina_embed_query(query), dtype=np.float64)
    qvec /= max(np.linalg.norm(qvec), 1e-9)

    with np.errstate(divide="ignore", over="ignore", invalid="ignore"):
        scores = idx["mat"] @ qvec  # cosine sim for each chunk
    scores = np.nan_to_num(scores, nan=0.0, posinf=0.0, neginf=0.0)

    # De-dupe by slug keeping best-scoring chunk
    by_slug: dict[str, dict] = {}
    for i, score in enumerate(scores):
        slug = idx["slugs"][i]
        if slug not in by_slug or float(score) > by_slug[slug]["score"]:
            by_slug[slug] = {
                "slug": slug,
                "title": idx["titles"][i],
                "issue_date": idx["issue_dates"][i],
                "url": idx["urls"][i],
                "body_snippet": idx["snippets"][i],
                "score": float(score),
            }

    # Token-overlap boost (mirrors workers/src/index.js)
    q_tokens = _query_tokens(query)
    articles = list(by_slug.values())
    for art in articles:
        art["score"] += 0.10 * _token_overlap(q_tokens, art["title"])
        art["score"] += 0.05 * _token_overlap(q_tokens, art["slug"].replace("-", " "))

    articles.sort(key=lambda a: a["score"], reverse=True)
    return articles[:limit]


# ── Worker utilities ──────────────────────────────────────────────────────────

def worker_search(query: str, url: str, limit: int = 10) -> list[dict] | None:
    if url == LOCAL_SEARCH_URL:
        try:
            return local_search(query, limit)
        except Exception as exc:
            print(f"  local_search error: {exc}")
            return None
    try:
        resp = requests.post(f"{url}/search", json={"query": query, "limit": limit}, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else data.get("results", [])
    except Exception as exc:
        print(f"  /search error: {exc}")
        return None


def worker_ask(query: str, url: str) -> dict | None:
    if url == LOCAL_SEARCH_URL:
        # /ask is not available locally; return a stub so grounding eval is skipped cleanly
        return None
    try:
        resp = requests.post(f"{url}/ask", json={"query": query}, timeout=60)
        resp.raise_for_status()
        return resp.json()
    except Exception as exc:
        print(f"  /ask error: {exc}")
        return None


# ── Metrics ───────────────────────────────────────────────────────────────────

def ndcg_at_k(grades: list[int], k: int = 10) -> float:
    grades = [g for g in grades[:k] if g >= 0]
    if not grades:
        return 0.0
    dcg = sum(g / math.log2(i + 2) for i, g in enumerate(grades))
    ideal_dcg = sum(g / math.log2(i + 2) for i, g in enumerate(sorted(grades, reverse=True)))
    return dcg / ideal_dcg if ideal_dcg > 0 else 0.0


# ── HTML review interface ─────────────────────────────────────────────────────

def generate_review_html(proposals: list[dict]) -> str:
    proposals_json = json.dumps(proposals, ensure_ascii=False, indent=2)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>NIC Archives — Golden Set Review</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:#f5f4ef;color:#1a1a1a;padding:20px;max-width:960px;margin:0 auto}}
h1{{font-size:1.4rem;margin-bottom:4px}}
.sub{{color:#666;font-size:.85rem;margin-bottom:16px}}
.stats{{display:flex;gap:20px;background:#fff;border:1px solid #ddd;border-radius:6px;padding:12px 20px;margin-bottom:20px}}
.stat{{text-align:center}}.stat-n{{font-size:1.8rem;font-weight:700}}.stat-l{{font-size:.75rem;color:#666}}
.block{{background:#fff;border:1px solid #ddd;border-radius:6px;margin-bottom:14px;overflow:hidden}}
.ah{{background:#f0ebe0;padding:10px 14px;border-bottom:1px solid #ddd}}
.at{{font-weight:700;font-size:.95rem;margin-bottom:2px}}
.am{{font-size:.75rem;color:#555;margin-bottom:5px}}
.ap{{font-size:.8rem;color:#444;line-height:1.5;font-style:italic}}
.qrow{{padding:10px 14px;border-bottom:1px solid #eee}}
.qrow:last-child{{border-bottom:none}}
.qrow.rej{{background:#fafafa;opacity:.55}}
.badge{{display:inline-block;font-size:.7rem;font-weight:700;letter-spacing:.06em;padding:2px 7px;border-radius:3px;margin-bottom:5px}}
.bs{{background:#dbeafe;color:#1d4ed8}}.bb{{background:#dcfce7;color:#166534}}.bn{{background:#fee2e2;color:#991b1b}}
.acts{{float:right}}
.btn{{border:none;border-radius:4px;padding:3px 10px;font-size:.78rem;cursor:pointer;margin-left:3px}}
.ba{{background:#22c55e;color:#fff}}.br{{background:#ef4444;color:#fff}}
.fl{{font-size:.72rem;color:#888;margin-top:5px;margin-bottom:2px}}
textarea,input{{width:100%;border:1px solid #d1d5db;border-radius:4px;padding:5px 8px;font-size:.83rem;font-family:inherit}}
textarea{{resize:vertical;min-height:54px}}
.footer{{position:sticky;bottom:0;background:#fff;border-top:2px solid #222;padding:12px 20px;display:flex;align-items:center;gap:16px;margin-top:20px}}
.dl{{background:#1a1a1a;color:#fff;border:none;border-radius:6px;padding:10px 22px;font-size:.95rem;font-weight:600;cursor:pointer}}
.dl:hover{{background:#333}}
#msg{{font-size:.85rem;color:#555}}
</style>
</head>
<body>
<h1>NIC Archives — Golden Set Review</h1>
<p class="sub">Review LLM-generated queries. Edit freely, approve/reject each query, then click Download. Save the file to <code>eval/golden_set.json</code>.</p>
<div class="stats">
  <div class="stat"><div class="stat-n" id="s-total">—</div><div class="stat-l">Total queries</div></div>
  <div class="stat"><div class="stat-n" id="s-approved">—</div><div class="stat-l">Approved</div></div>
  <div class="stat"><div class="stat-n" id="s-rejected">—</div><div class="stat-l">Rejected</div></div>
  <div class="stat"><div class="stat-n" id="s-arts">—</div><div class="stat-l">Articles</div></div>
</div>
<div id="cards"></div>
<div class="footer">
  <button class="dl" onclick="dl()">Download golden_set.json</button>
  <span id="msg">Review queries above, then download.</span>
</div>
<script>
const P={proposals_json};
const S={{}};
P.forEach(p=>{{S[p.id]={{approved:true,query:p.query,slugs:(p.expected_slugs||[]).join(', ')}}}});
function stats(){{
  const tot=P.length,app=Object.values(S).filter(s=>s.approved).length;
  document.getElementById('s-total').textContent=tot;
  document.getElementById('s-approved').textContent=app;
  document.getElementById('s-rejected').textContent=tot-app;
  document.getElementById('s-arts').textContent=new Set(P.map(p=>p.source_article)).size;
}}
function esc(s){{return String(s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;')}}
function setApp(id,v){{
  S[id].approved=v;
  const row=document.getElementById('r-'+id);
  row.className='qrow'+(v?'':' rej');
  row.querySelectorAll('.btn')[0].style.opacity=v?'0.3':'1';
  row.querySelectorAll('.btn')[1].style.opacity=v?'1':'0.3';
  stats();
}}
function render(){{
  const arts=[...new Map(P.map(p=>[p.source_article,p])).values()];
  document.getElementById('cards').innerHTML=arts.map(a=>{{
    const grp=P.filter(p=>p.source_article===a.source_article);
    const rows=grp.map(p=>{{
      const s=S[p.id],rej=!s.approved;
      const bc={{specific:'bs',broad:'bb',negative:'bn'}}[p.type]||'';
      const slugField=p.type!=='negative'?`<div class="fl">Expected slugs (comma-separated, add related slugs for BROAD):</div>
        <input value="${{esc(s.slugs)}}" oninput="S['${{p.id}}'].slugs=this.value" placeholder="slug-1, slug-2">`:
        `<div class="fl" style="color:#bbb">No expected slugs (negative query)</div>`;
      return `<div class="qrow${{rej?' rej':''}}" id="r-${{p.id}}">
        <div class="acts">
          <button class="btn ba" style="opacity:${{rej?1:.3}}" onclick="setApp('${{p.id}}',true)">✓ Approve</button>
          <button class="btn br" style="opacity:${{rej?.3:1}}" onclick="setApp('${{p.id}}',false)">✗ Reject</button>
        </div>
        <span class="badge ${{bc}}">${{p.type.toUpperCase()}}</span>
        <div class="fl">Query:</div>
        <textarea oninput="S['${{p.id}}'].query=this.value">${{esc(s.query)}}</textarea>
        ${{slugField}}
      </div>`;
    }}).join('');
    return `<div class="block">
      <div class="ah">
        <div class="at">${{esc(a.title)}}</div>
        <div class="am">${{esc(a.issue_date)}} &middot; ${{esc(a.section)}} &middot; ${{esc(a.decade)}} &middot; <code style="font-size:.72rem">${{esc(a.source_article)}}</code></div>
        <div class="ap">${{esc(a.body_preview)}}</div>
      </div>${{rows}}</div>`;
  }}).join('');
  stats();
}}
function dl(){{
  const out=[];let idx=1;
  P.forEach(p=>{{
    if(!S[p.id].approved)return;
    const slugs=p.type==='negative'?[]:S[p.id].slugs.split(',').map(x=>x.trim()).filter(Boolean);
    out.push({{id:'Q'+String(idx++).padStart(3,'0'),type:p.type,query:S[p.id].query,
      expected_slugs:slugs,source_article:p.source_article,decade:p.decade}});
  }});
  const a=document.createElement('a');
  a.href=URL.createObjectURL(new Blob([JSON.stringify(out,null,2)],{{type:'application/json'}}));
  a.download='golden_set.json';document.body.appendChild(a);a.click();document.body.removeChild(a);
  document.getElementById('msg').textContent=`Downloaded ${{out.length}} approved queries. Save to eval/golden_set.json.`;
}}
render();
</script>
</body>
</html>"""


# ── Mode: --build-golden ──────────────────────────────────────────────────────

def build_golden(config: dict) -> None:
    print("\n=== Building golden set ===")
    articles = stratified_sample(config)
    client = _groq_client()
    proposals = []

    for i, art in enumerate(articles, 1):
        print(f"\n[{i}/{len(articles)}] {art['slug']}")
        generated = generate_queries(art, client)
        if not generated:
            print("  Skipping (query generation failed)")
            continue

        base = {
            "source_article": art["slug"],
            "title": art["title"],
            "issue_date": art["issue_date"],
            "section": art["section"],
            "decade": art["decade"],
            "body_preview": art["body"][:400],
        }
        for qtype in ("specific", "broad", "negative"):
            qdata = generated.get(qtype, {})
            props_id = f"{art['slug']}:{qtype}"
            proposals.append({
                "id": props_id,
                "type": qtype,
                "query": qdata.get("query", ""),
                "expected_slugs": qdata.get("expected_slugs", []) if qtype != "negative" else [],
                **base,
            })
            print(f"  {qtype}: {qdata.get('query', '')[:70]}...")
        time.sleep(1.0)  # rate limit between articles

    html = generate_review_html(proposals)
    REVIEW_HTML_PATH.write_text(html, encoding="utf-8")
    print(f"\n✓ Review HTML written to: {REVIEW_HTML_PATH}")
    print("  1. Open eval/review.html in your browser")
    print("  2. Edit queries, approve/reject each one")
    print("  3. For BROAD queries: add related article slugs to the expected_slugs field")
    print("  4. Click 'Download golden_set.json' and save to eval/golden_set.json")
    print("  5. Then run: python pipeline/eval_search.py --calibrate-judge")


# ── Mode: --calibrate-judge ───────────────────────────────────────────────────

def calibrate_judge(config: dict) -> None:
    if not GOLDEN_SET_PATH.exists():
        sys.exit("golden_set.json not found. Run --build-golden first.")

    golden = json.loads(GOLDEN_SET_PATH.read_text())
    if len(golden) < 5:
        sys.exit("Need at least 5 queries in golden_set.json.")

    sample = random.sample(golden, min(5, len(golden)))
    client = _groq_client()
    cache = load_judgments()
    worker_url = config["worker_url"]

    print("\n=== Judge calibration — 20 sample pairs ===")
    print("Review these scores and check they match your intuition.\n")

    pair_num = 0
    for q in sample:
        results = worker_search(q["query"], worker_url, limit=4)
        if not results:
            print(f"  Skipping {q['id']} (worker unreachable)")
            continue
        for result in results[:4]:
            pair_num += 1
            score = judge_relevance(q["id"], q["query"], result, client, cache)
            score_label = ["✗ NOT RELEVANT", "~ PARTIAL", "✓ HIGHLY RELEVANT"][max(0, score)]
            print(f"── Pair {pair_num} ──────────────────────────────────────")
            print(f"Query  : {q['query']}")
            print(f"Result : {result.get('slug', '')}")
            print(f"Title  : {result.get('title', '')}")
            print(f"Snippet: {(result.get('snippet') or '')[:200]}")
            print(f"Judge  : {score}  {score_label}")
            print()

    save_judgments(cache)
    print("─" * 50)
    print(f"Printed {pair_num} pairs. Scores cached to eval/eval_judgments.json.")
    print("\nIf ≥ 3 scores look wrong: edit the JUDGE_PROMPT in eval_search.py and re-run.")
    print("If scores look right: proceed with --run.")


# ── Mode: --run ───────────────────────────────────────────────────────────────

def run_eval(config: dict) -> bool:
    if not GOLDEN_SET_PATH.exists():
        sys.exit("golden_set.json not found. Run --build-golden first.")

    golden = json.loads(GOLDEN_SET_PATH.read_text())
    cache = load_judgments()
    client = _groq_client()
    worker_url = config["worker_url"]
    thresholds = config["thresholds"]

    specific = [q for q in golden if q["type"] == "specific"]
    broad = [q for q in golden if q["type"] == "broad"]
    negative = [q for q in golden if q["type"] == "negative"]

    query_results: dict = {}
    skipped = 0

    # ── Search evaluation (specific + broad) ──
    print(f"\nRunning search evaluation ({len(specific)} specific, {len(broad)} broad)...")
    for q in specific + broad:
        print(f"  [{q['id']}] {q['type']}: {q['query'][:65]}...")
        results = worker_search(q["query"], worker_url, limit=10)
        if results is None:
            skipped += 1
            query_results[q["id"]] = {"skipped": True, "type": q["type"]}
            continue

        grades = []
        result_details = []
        for rank, res in enumerate(results):
            score = judge_relevance(q["id"], q["query"], res, client, cache)
            grades.append(score)
            result_details.append({
                "rank": rank + 1,
                "slug": res.get("slug", ""),
                "title": res.get("title", ""),
                "score": res.get("score", 0),
                "judge": score,
            })

        expected = q.get("expected_slugs", [])
        p1 = 1 if (result_details and result_details[0]["slug"] in expected) else 0
        ndcg = ndcg_at_k(grades)
        expected_rank = next(
            (r["rank"] for r in result_details if r["slug"] in expected), "—"
        )

        query_results[q["id"]] = {
            "type": q["type"],
            "query": q["query"],
            "expected_slugs": expected,
            "results": result_details,
            "precision_at_1": p1,
            "ndcg_at_10": ndcg,
            "skipped": False,
        }
        p1_icon = "✓" if p1 else "✗"
        print(f"    P@1:{p1_icon}  expected_rank:{expected_rank}  nDCG:{ndcg:.2f}")
        save_judgments(cache)
        time.sleep(0.3)

    # ── Negative evaluation ──
    print(f"\nRunning negative evaluation ({len(negative)} queries)...")
    neg_fp = 0
    for q in negative:
        results = worker_search(q["query"], worker_url, limit=5)
        if results is None:
            skipped += 1
            query_results[q["id"]] = {"skipped": True, "type": "negative"}
            continue
        max_score = max((r.get("score", 0) for r in results), default=0.0)
        fp = max_score > thresholds["negative_max_score"]
        if fp:
            neg_fp += 1
        query_results[q["id"]] = {
            "type": "negative",
            "query": q["query"],
            "max_similarity_score": max_score,
            "false_positive": fp,
            "skipped": False,
        }
        icon = "✗ FALSE POSITIVE" if fp else "✓"
        print(f"  [{q['id']}] max_score:{max_score:.2f}  {icon}")
        time.sleep(0.2)

    # ── /ask grounding (broad queries, capped at 10) ──
    print(f"\nRunning /ask grounding ({min(10, len(broad))} broad queries)...")
    grounding_scores: list[int] = []
    for q in broad[:10]:
        result = worker_ask(q["query"], worker_url)
        if not result:
            continue
        answer = result.get("answer", "")
        sources = result.get("citations", result.get("sources", result.get("results", [])))
        sources_text = "\n".join(
            f"- {s.get('title','')}: {(s.get('snippet') or '')[:200]}" for s in sources
        )
        prompt = GROUNDING_PROMPT.format(
            query=q["query"], answer=answer, sources_text=sources_text
        )
        try:
            time.sleep(0.5)
            raw = _groq_call(client, prompt)
            gs = max(0, min(2, int(raw.strip())))
            grounding_scores.append(gs)
            print(f"  [{q['id']}] grounding:{gs}/2")
        except Exception as exc:
            print(f"  [{q['id']}] grounding error: {exc}")

    # ── Aggregate metrics ──
    non_skip_specific = [
        q for q in specific if not query_results.get(q["id"], {}).get("skipped")
    ]
    p1_hits = sum(query_results[q["id"]]["precision_at_1"] for q in non_skip_specific)
    precision_at_1 = p1_hits / len(non_skip_specific) if non_skip_specific else 0.0

    all_ndcgs = [
        query_results[q["id"]]["ndcg_at_10"]
        for q in specific + broad
        if not query_results.get(q["id"], {}).get("skipped")
    ]
    ndcg_mean = sum(all_ndcgs) / len(all_ndcgs) if all_ndcgs else 0.0
    grounding_mean = sum(grounding_scores) / len(grounding_scores) if grounding_scores else 0.0

    n_neg_tested = sum(
        1 for q in negative if not query_results.get(q["id"], {}).get("skipped")
    )

    # ── Regression detection ──
    regressions: list[dict] = []
    baseline: dict = {}
    if BASELINE_PATH.exists():
        baseline = json.loads(BASELINE_PATH.read_text())
        bpq = baseline.get("per_query", {})
        for q in non_skip_specific:
            qr = query_results[q["id"]]
            cur_rank = next(
                (r["rank"] for r in qr.get("results", []) if r["slug"] in q.get("expected_slugs", [])),
                999,
            )
            base_rank = bpq.get(q["id"], {}).get("rank", 999)
            if base_rank <= 3 and cur_rank > 5:
                regressions.append({
                    "id": q["id"],
                    "query": q["query"],
                    "expected_slug": (q.get("expected_slugs") or [""])[0],
                    "baseline_rank": base_rank,
                    "current_rank": cur_rank,
                })

    # ── Pass/fail ──
    passed = (
        precision_at_1 >= thresholds["precision_at_1"]
        and neg_fp == 0
        and len(regressions) == 0
    )

    # ── Terminal report ──
    bm = baseline.get("metrics", {})

    def delta(cur: float, key: str) -> str:
        if key not in bm:
            return "(no baseline)"
        b = bm[key]
        d = cur - b
        arrow = "▲" if d > 0 else ("▼" if d < 0 else "=")
        return f"(baseline:{b:.2f}  {arrow}{d:+.2f})"

    print(f"\nNIC Archives Search Eval — {datetime.now().strftime('%Y-%m-%d')}")
    print("══════════════════════════════════════")
    p1_ok = precision_at_1 >= thresholds["precision_at_1"]
    print(f"Precision@1   : {p1_hits:.0f}/{len(non_skip_specific)}  {precision_at_1:.1%}  {'✓' if p1_ok else '✗'}  {delta(precision_at_1,'precision_at_1')}")
    ndcg_ok = ndcg_mean >= thresholds["ndcg_at_10_warn"]
    print(f"nDCG@10       : {ndcg_mean:.2f}          {'✓' if ndcg_ok else '⚠'}  {delta(ndcg_mean,'ndcg_at_10')}")
    print(f"/ask grounding: {grounding_mean:.1f}/2         {'✓' if grounding_mean >= 1.5 else '⚠'}  {delta(grounding_mean,'ask_grounding')}")
    print(f"Negative FP   : {neg_fp}/{n_neg_tested}          {'✓' if neg_fp == 0 else '✗'}")
    if skipped:
        print(f"\n⚠  {skipped} queries skipped (worker unreachable)")
    print()

    if passed:
        print("RESULT: PASS — safe to ship")
    else:
        print(f"RESULT: FAIL — {len(regressions)} regression(s)")
        for r in regressions:
            print(f"  [{r['id']}] \"{r['query']}\"")
            print(f"         expected: {r['expected_slug']}")
            print(f"         rank: {r['current_rank']}  (was {r['baseline_rank']} in baseline)")
        if not p1_ok:
            print(f"  Precision@1 {precision_at_1:.1%} < threshold {thresholds['precision_at_1']:.1%}")
        if neg_fp:
            print(f"  {neg_fp} negative query false positive(s)")
        print("\nRun --review-failures for full context.")

    # ── Save report ──
    ts = datetime.now().strftime("%Y-%m-%dT%H-%M")
    report_path = REPORTS_DIR / f"{ts}.json"
    report = {
        "run_date": datetime.now().isoformat(),
        "worker_url": worker_url,
        "metrics": {
            "precision_at_1": precision_at_1,
            "ndcg_at_10": ndcg_mean,
            "ask_grounding": grounding_mean,
            "negative_false_positives": neg_fp,
        },
        "pass": passed,
        "regressions": regressions,
        "skipped": skipped,
        "queries": query_results,
    }
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False))
    print(f"\nFull report   : eval/reports/{ts}.json")

    return passed


# ── Mode: --set-baseline ──────────────────────────────────────────────────────

def set_baseline() -> None:
    reports = sorted(REPORTS_DIR.glob("*.json"), reverse=True)
    if not reports:
        sys.exit("No reports found. Run --run first.")

    latest = json.loads(reports[0].read_text())
    if not latest.get("pass"):
        print(f"⚠  Latest run FAILED. Set as baseline anyway? [y/N] ", end="", flush=True)
        if input().strip().lower() != "y":
            print("Aborted.")
            return

    golden = json.loads(GOLDEN_SET_PATH.read_text())
    specific = [q for q in golden if q["type"] == "specific"]
    per_query: dict = {}
    for q in specific:
        qr = latest["queries"].get(q["id"], {})
        if qr.get("skipped"):
            continue
        expected = q.get("expected_slugs", [])
        rank = next(
            (r["rank"] for r in qr.get("results", []) if r["slug"] in expected), 999
        )
        per_query[q["id"]] = {"rank": rank, "ndcg": qr.get("ndcg_at_10", 0)}

    baseline = {
        "set_date": datetime.now().strftime("%Y-%m-%d"),
        "source_report": reports[0].name,
        "metrics": latest["metrics"],
        "per_query": per_query,
    }
    BASELINE_PATH.write_text(json.dumps(baseline, indent=2, ensure_ascii=False))
    m = latest["metrics"]
    print(f"Baseline set from {reports[0].name}")
    print(f"  Precision@1 : {m['precision_at_1']:.1%}")
    print(f"  nDCG@10     : {m['ndcg_at_10']:.2f}")
    print(f"  Grounding   : {m['ask_grounding']:.1f}/2")
    print(f"\nCommit eval/baseline.json and eval/eval_judgments.json to git.")


# ── Mode: --review-failures ───────────────────────────────────────────────────

def review_failures() -> None:
    reports = sorted(REPORTS_DIR.glob("*.json"), reverse=True)
    if not reports:
        sys.exit("No reports found. Run --run first.")

    latest = json.loads(reports[0].read_text())
    if latest.get("pass"):
        print(f"Latest run ({reports[0].name}) PASSED — no regressions.")
        return

    golden = json.loads(GOLDEN_SET_PATH.read_text())
    by_id = {q["id"]: q for q in golden}
    regressions = latest.get("regressions", [])

    print(f"\nRegressions in {reports[0].name}")
    print(f"Overall Precision@1: {latest['metrics']['precision_at_1']:.1%}")
    print(f"Overall nDCG@10    : {latest['metrics']['ndcg_at_10']:.2f}")
    print("═" * 60)

    for r in regressions:
        q = by_id.get(r["id"], {})
        print(f"\n[{r['id']}] {r['query']}")
        print(f"  Expected slug : {r['expected_slug']}")
        print(f"  Rank          : {r['current_rank']}  (was {r['baseline_rank']} in baseline)")
        qr = latest["queries"].get(r["id"], {})
        print("  Top 5 results:")
        for res in qr.get("results", [])[:5]:
            j = res.get("judge", -1)
            jlabel = ["✗", "~", "✓"][j] if 0 <= j <= 2 else "?"
            expected_mark = " ← EXPECTED" if res["slug"] in q.get("expected_slugs", []) else ""
            print(f"    {res['rank']}. [{jlabel}] {res['slug']}  (sim:{res.get('score',0):.2f}){expected_mark}")

    neg_fp = latest["metrics"].get("negative_false_positives", 0)
    if neg_fp:
        print(f"\n⚠  {neg_fp} negative query false positive(s) — check worker similarity threshold.")


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description="NIC Archives search evaluation")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--build-golden", action="store_true", help="Sample articles, generate queries, produce review HTML")
    group.add_argument("--calibrate-judge", action="store_true", help="Print 20 judge scores for human visual review")
    group.add_argument("--run", action="store_true", help="Full evaluation against live worker")
    group.add_argument("--set-baseline", action="store_true", help="Set current report as baseline")
    group.add_argument("--review-failures", action="store_true", help="Show regressions from latest report")
    parser.add_argument("--local", action="store_true", help="Use local vectors.ndjson instead of live worker (bypasses Vectorize quota)")
    args = parser.parse_args()

    config = load_config()
    if args.local:
        config["worker_url"] = LOCAL_SEARCH_URL

    if args.build_golden:
        build_golden(config)
    elif args.calibrate_judge:
        calibrate_judge(config)
    elif args.run:
        passed = run_eval(config)
        sys.exit(0 if passed else 1)
    elif args.set_baseline:
        set_baseline()
    elif args.review_failures:
        review_failures()


if __name__ == "__main__":
    main()
