# NIC Archives — Semantic Search & MCP Build Plan

> **Purpose:** Replace keyword search (Pagefind) with semantic vector search, add an "Ask" RAG feature,
> and expose the archive via an MCP server for Claude Desktop. This document is the single source of
> truth for the entire build. Read this before touching any search-related code.

---

## Vision

Researchers and policy analysts should be able to search conceptually. Searching "election malpractices"
should surface articles *about* election malpractices even if those exact words never appear. The search
should find what the user came to find, with minimal friction.

**Two user goals:**
1. Easy browsing and searching of the archive
2. Researchers (human) and AI agents (MCP) can query the archive programmatically

---

## Architecture (Locked In)

```
Browser / MCP Client
        │
        ├─── GET /api/articles.json  ─── docs/api/articles.json  (static, GitHub Pages)
        ├─── GET /api/issues.json    ─── docs/api/issues.json     (static, GitHub Pages)
        │
        └─── POST /search  ─┐
             POST /ask     ─┤── Cloudflare Worker
                            │       │
                            │       ├── Workers AI (BGE base) — embed queries
                            │       ├── D1 database — vector store (3,865 article embeddings)
                            │       └── Gemini Flash — "Ask" synthesis only
                            │
        MCP Server (local Python process, no hosting)
            calls the same Cloudflare Worker as the browser
```

**Key decisions (do not revisit without good reason):**

| Decision | Choice | Why |
|----------|--------|-----|
| Embedding model | Cloudflare Workers AI (BGE base) | Free, no Gemini API cost |
| Vector store | Cloudflare D1 (SQLite) | Free tier 5GB, $0 at this scale |
| Keyword search | **Removed entirely** (Pagefind replaced) | Semantic search handles conceptual queries |
| Topic tags | **Skipped** | Semantic search makes them redundant |
| "Ask" feature | RAG: retrieve top 5 → Gemini Flash synthesis | Same infrastructure as search, one extra step |
| MCP hosting | None — local Python process | MCP runs inside Claude Desktop, calls Worker |
| Re-embedding new issues | Manual for now: `python pipeline/embed_articles.py --issue <slug>` | Automate via GitHub Actions post-pilot |
| Evals | 3-tier (automated + Gemini-as-judge + human spot-check) | Search must pass evals before MCP is built |

---

## Data Shapes

### `docs/api/articles.json` (all ~3,865 articles)
```json
[
  {
    "slug": "keeping-monkeys-at-bay-october-1992",
    "title": "Keeping Monkeys at Bay",
    "issue_date": "October 1992",
    "issue_slug": "october-1992",
    "pages": [8, 9],
    "author": "V.S. Ramamurthy",
    "section": "Feature",
    "body_snippet": "First 500 chars of article body...",
    "url": "/articles/keeping-monkeys-at-bay-october-1992.html"
  }
]
```

### `docs/api/issues.json` (all ~131 issues)
```json
[
  {
    "issue_slug": "october-1992",
    "issue_date": "October 1992",
    "article_count": 12,
    "article_slugs": ["keeping-monkeys-at-bay-october-1992", "..."]
  }
]
```

### D1 Schema (`articles_embeddings` table)
```sql
CREATE TABLE articles_embeddings (
  slug        TEXT PRIMARY KEY,
  title       TEXT NOT NULL,
  issue_date  TEXT NOT NULL,
  issue_slug  TEXT NOT NULL,
  body_snippet TEXT,
  url         TEXT NOT NULL,
  embedding   TEXT NOT NULL  -- JSON array of 768 floats (BGE base)
);
```

### Worker API
```
POST /search
  Body: { "query": "...", "limit": 10 }
  Returns: [{ slug, title, issue_date, url, score, body_snippet }]

POST /ask
  Body: { "query": "..." }
  Returns: {
    "answer": "...",
    "citations": [{ slug, title, issue_date, url }]
  }
```

---

## Phase-by-Phase Plan

### Phase 1 — Static JSON Exports (~1 day)
**No APIs needed. Purely additive to `generate_site.py`.**

**Goal:** Generate `docs/api/articles.json` and `docs/api/issues.json` at every site build.

**Steps:**
1. In `generate_site.py`, after all articles are parsed, add a `write_api_exports()` function
2. Create `docs/api/` directory
3. Build `articles.json` list: iterate `articles/*.md`, parse frontmatter, extract first 500 chars of body as `body_snippet`, add `url` field
4. Build `issues.json` list: group articles by `issue_slug`, count articles, list slugs
5. Write both files as pretty-printed JSON
6. Run `python generate_site.py` and verify:
   - `docs/api/articles.json` exists with correct count (~3,865 entries)
   - `docs/api/issues.json` exists with correct count (~131 entries)
   - Spot-check 3–4 entries for correctness
7. Commit

**Files to modify:** `generate_site.py` only

---

### Phase 2 — Cloudflare Setup + Embeddings (~1 day)
**One-time setup. Run once per article corpus.**

**Prerequisites:**
- Cloudflare account (free): https://dash.cloudflare.com
- `npm install -g wrangler` then `wrangler login`
- Add to `.env`: `CLOUDFLARE_ACCOUNT_ID=...`, `CLOUDFLARE_API_TOKEN=...`

**Steps:**
1. Create D1 database: `wrangler d1 create nic-archives`
2. Note the database ID from the output, add to `wrangler.toml`
3. Run schema migration: create `workers/schema.sql` and run `wrangler d1 execute nic-archives --file=workers/schema.sql`
4. Write `pipeline/embed_articles.py`:
   - Load all articles from `articles/*.md`
   - For each article: embed `title + " " + body_snippet` via Workers AI REST API (`POST /accounts/{id}/ai/run/@cf/baai/bge-base-en-v1.5`)
   - Upsert into D1 via Workers REST API
   - Skip slugs already in D1 (idempotent)
   - Batch 50 articles at a time, 0.5s delay between batches
   - Save progress to `pipeline/embed_progress.json` so reruns resume
5. Run: `python pipeline/embed_articles.py`
6. Verify: query D1 to confirm row count matches article count

**New files:**
- `pipeline/embed_articles.py`
- `workers/schema.sql`
- `workers/wrangler.toml`

**Cost:** $0 (Workers AI free tier: 10k neurons/day, ~$0 at this scale)

---

### Phase 3 — Cloudflare Worker API (~1 day)
**The backend. Deploy once.**

**Steps:**
1. Create `workers/src/index.js` (or TypeScript if preferred)
2. Implement `POST /search`:
   ```
   1. Embed the query via Workers AI (BGE base)
   2. Compute cosine similarity against all article embeddings in D1
   3. Return top-N results sorted by similarity score
   4. Add CORS headers for browser access
   ```
3. Implement `POST /ask`:
   ```
   1. Run /search to get top 5 articles
   2. Build prompt: "You are an expert on NIC's history. Answer using ONLY these sources..."
   3. Call Gemini Flash API with retrieved context
   4. Return { answer, citations } — citations are mandatory, never return answer without them
   5. If Gemini fails: return { error: "Ask unavailable, try Search instead" }
   ```
4. Add rate limiting (100 req/min per IP via Cloudflare's built-in rate limiting)
5. Deploy: `wrangler deploy`
6. Test manually with `curl`:
   ```bash
   curl -X POST https://your-worker.workers.dev/search \
     -H 'Content-Type: application/json' \
     -d '{"query": "election systems", "limit": 5}'
   ```
7. Verify responses are sensible

**New files:**
- `workers/src/index.js`
- `workers/package.json`
- `workers/wrangler.toml` (updated with routes)

**Cost:** $0 (Workers free: 100k req/day; Gemini Flash: ~$0.001/ask query)

---

### Phase 4 — Frontend Search UI (~1 day)
**Replace Pagefind. Update `generate_site.py`.**

**Steps:**
1. In `generate_site.py`:
   - Remove all Pagefind references (`pagefind/pagefind-ui.js`, `data-pagefind-body`, `data-pagefind-ignore` attributes)
   - Remove Pagefind script tags and CSS from HTML templates
2. Add new search UI to `docs/index.html` (and issue/article pages):
   ```
   [ Search Archive... ] [ Search ] [ Ask ]
   ↑ single text input   ↑ two buttons toggle mode
   ```
3. Wire up JavaScript:
   - `Search` button: `POST /search` → render result cards (title, issue date, snippet, link)
   - `Ask` button: `POST /ask` → render answer paragraph + citation list
   - Show loading spinner during fetch
   - Handle errors gracefully ("Search unavailable — try again later")
4. Store Worker URL as a JS constant (not hardcoded, set via a `<meta>` tag injected by `generate_site.py`)
5. Verify on mobile (responsive)
6. Run `python generate_site.py` and test in browser:
   - Search "NICNET" → relevant results appear
   - Ask "What role did NIC play in elections?" → answer with citations appears
   - Search with no results → graceful empty state

**Files to modify:** `generate_site.py` (CSS, JS, HTML templates)

**Do NOT run `npx pagefind` after this phase — Pagefind is gone.**

---

### Phase 5 — Evals (~1 day)
**Do not build the MCP until evals pass. Search quality is the foundation.**

**Success criteria:** Precision@5 ≥ 3/5 on known-answer queries (3 of top 5 results are relevant).

**Steps:**
1. Write `pipeline/eval_search.py` with 3 tiers:

   **Tier 1 — Known-answer queries (fully automated):**
   - 50 queries with ground-truth article slugs
   - Call `POST /search`, check if ground-truth slug appears in top 5
   - Compute Precision@5 score
   - Fail if score < 0.6

   **Tier 2 — Gemini-as-judge (automated):**
   - For queries where ground truth is uncertain, send (query + top 5 results) to Gemini
   - Prompt: "Are these results relevant to the query? Score 1–5 for each."
   - Flag any result scoring ≤ 2 for human review

   **Tier 3 — Human spot-check (~30 min):**
   - Print all Tier-2-flagged results to terminal
   - Human reads and marks pass/fail
   - Document failures for iteration

2. Write 50 test queries covering 5 types:
   - **Exact match** (e.g., "NICNET", "Aadhaar"): should be trivial
   - **Conceptual** (e.g., "election transparency", "rural connectivity"): tests semantic power
   - **Cross-decade** (e.g., "database systems 1990s"): tests temporal queries
   - **People** (e.g., "work by NIC scientists"): tests author/contributor queries
   - **Negative** (e.g., "artificial intelligence 2026"): should return no results or low scores

3. Save test queries to `pipeline/eval_queries.json`:
   ```json
   [
     {
       "query": "computerized election systems",
       "expected_slugs": ["nics-election-experience-a-rich-harvest-april-1995", "..."],
       "type": "exact"
     }
   ]
   ```

4. Run evals: `python pipeline/eval_search.py`
5. If Precision@5 < 0.6: iterate on embedding text (try different combinations of title/body/section) and re-embed
6. Document final scores in `pipeline/eval_results.json`

**New files:**
- `pipeline/eval_search.py`
- `pipeline/eval_queries.json`
- `pipeline/eval_results.json` (generated)

---

### Phase 6 — MCP Server (after evals pass)
**Only build this after Phase 5 passes. MCP quality = search quality.**

**Steps:**
1. Write `mcp_server.py` in the project root
2. Implement 6 tools:

   | Tool | Description |
   |------|-------------|
   | `search_articles(query, limit=10)` | Semantic search → returns ranked article list |
   | `ask_archive(question)` | RAG answer with mandatory citations |
   | `get_article(slug)` | Full article metadata + body snippet from `articles.json` |
   | `list_articles_in_issue(issue_slug)` | All articles in one issue from `issues.json` |
   | `articles_by_decade(decade)` | e.g., "1990s" → filter articles by year range |
   | `list_all_issues()` | All 131 issues with dates and article counts |

3. Implementation pattern:
   - `search_articles` and `ask_archive`: call Cloudflare Worker (`POST /search`, `POST /ask`)
   - `get_article`, `list_articles_in_issue`, `articles_by_decade`, `list_all_issues`: read from `docs/api/articles.json` and `docs/api/issues.json` (no API call needed — static files)
4. Test locally by running: `python mcp_server.py`
5. Configure in Claude Desktop: add to `~/Library/Application Support/Claude/claude_desktop_config.json`
6. Verify all 6 tools work in Claude Desktop

**New files:**
- `mcp_server.py`

---

## Running Order (Copy-Paste Reference)

```bash
# Phase 1
python generate_site.py
# Verify: ls docs/api/ → articles.json  issues.json

# Phase 2 — one-time setup
npm install -g wrangler
wrangler login
wrangler d1 create nic-archives
wrangler d1 execute nic-archives --file=workers/schema.sql
python pipeline/embed_articles.py

# Phase 3
cd workers
wrangler deploy
cd ..
curl -X POST https://your-worker.workers.dev/search -H 'Content-Type: application/json' -d '{"query":"test","limit":5}'

# Phase 4
python generate_site.py
open docs/index.html

# Phase 5
python pipeline/eval_search.py

# Phase 6
python mcp_server.py
# Then configure Claude Desktop

# Re-embedding new issues (after adding new articles)
python pipeline/embed_articles.py --issue <issue-slug>
```

---

## Cost Summary

| Item | Cost |
|------|------|
| Cloudflare Workers (100k req/day free) | $0 |
| Cloudflare D1 (5GB free) | $0 |
| Workers AI embeddings (10k neurons/day free) | $0 |
| Gemini Flash for "Ask" queries | ~$0.001/query |
| GitHub Pages hosting | $0 |
| **Total ongoing** | **~$0** |

---

## What NOT to Do

- Do not run `npx pagefind` after Phase 4 — Pagefind is fully removed
- Do not build the MCP (Phase 6) before evals pass (Phase 5)
- Do not hardcode the Cloudflare Worker URL — inject it via `generate_site.py` as a `<meta>` tag
- Do not add topic tagging — semantic search handles conceptual queries without it
- Do not embed articles using Gemini API — use Workers AI (free)
- Do not modify `generate_site.py` for anything other than adding the API exports and new search UI
- Do not commit `.env` (contains `CLOUDFLARE_API_TOKEN`, `CLOUDFLARE_ACCOUNT_ID`, `GEMINI_API_KEY`)

---

## Files This Plan Will Create

```
docs/api/
  articles.json               ← Phase 1
  issues.json                 ← Phase 1

workers/
  schema.sql                  ← Phase 2
  wrangler.toml               ← Phase 2
  src/index.js                ← Phase 3

pipeline/
  embed_articles.py           ← Phase 2
  embed_progress.json         ← Phase 2 (generated, gitignore)
  eval_search.py              ← Phase 5
  eval_queries.json           ← Phase 5
  eval_results.json           ← Phase 5 (generated)

mcp_server.py                 ← Phase 6
```

---

## Status

| Phase | Status |
|-------|--------|
| 1 — Static JSON exports | ✅ Done — 3,865 articles, 131 issues |
| 2 — Cloudflare setup + embeddings | ⬜ Not started |
| 3 — Worker API | ⬜ Not started |
| 4 — Frontend search UI | ⬜ Not started |
| 5 — Evals | ⬜ Not started |
| 6 — MCP server | ⬜ Not started |

Update status as each phase completes.
