# NIC Archives — Project Rules

## What this project does
Converts ~120 NIC Informatics newsletter PDFs (1992–2026) into a searchable static website. Each article gets its own page. Pagefind handles search. GitHub Pages hosts it.

## Pipeline order (never skip steps)
```
Archives/*.pdf
  → classify_pdfs.py       → classified.json
  → extract_born_digital.py  (born_digital entries)  → raw_text/{slug}.json
  → extract_scanned.py       (scanned + corrupt_encoding entries) → raw_text/{slug}.json
  → segment_articles.py    → articles/{article-slug}.md
  → generate_site.py       → docs/
  → npx pagefind --site docs/
```

## APIs
- `MISTRAL_API_KEY` — scanned OCR only (`mistral-ocr-2512`)
- `GEMINI_API_KEY` — article segmentation only (`gemini-2.0-flash`)
- Keys are in `.env`. Load with `python-dotenv`. Never hardcode. Never commit `.env`.

## PDF types (from classified.json)
- `born_digital` — pdftotext works, clean text
- `scanned` — needs Mistral OCR (pre-1997, 2007–2010, some 2013–2015, 2018–2019, 2022, 2025)
- `corrupt_encoding` — pdftotext produces garbage (2011–2012); treat as scanned, route through Mistral OCR

## Robustness rules (non-negotiable)
- **Idempotent**: if output file already exists, skip — never reprocess
- **Never crash on one bad file** — catch exceptions, write to `pipeline/errors.json`, continue
- **Cost guard** — before any Mistral OCR batch, print estimated cost and require user confirmation if > $1
- **Rate limit** — 1s delay between Mistral API calls; exponential backoff on retry (max 3 retries)

## Intermediate data format (`raw_text/{slug}.json`)
```json
[{"page": 1, "text": "..."}, {"page": 2, "text": "..."}]
```
Page text from born-digital uses pdftotext -layout. Page text from scanned uses Mistral markdown output.

## Article output format (`articles/{slug}.md`)
```markdown
---
title: "Article Title"
publication: "Informatics"
issue_date: "April 1995"
pages: [4, 5]
author: null
section: "Cover Story"
---

## Article Title

Body text...
```
Match this exactly. `parse_frontmatter()` in `generate_site.py` depends on this format.

## Pilot-first rule
Always test on `Apr-1995.pdf` (scanned) and `April-2003.pdf` (born-digital) before running on all 120 issues. Manually inspect `raw_text/` and `articles/` output before proceeding to full run.

## Existing files — do not break
- `generate_site.py` — working static site generator. Don't modify unless explicitly asked.
- `split_articles.py` — 1992 issue only, uses metadata JSON. Don't touch.
- `articles/` — existing 1992 article files are the reference format.
- `docs/` — generated output. Never edit manually.

## What NOT to do
- Don't use pdftotext on scanned or corrupt_encoding files — it produces garbage
- Don't run the full 120-issue pipeline before pilot passes
- Don't add features not asked for (no summarization, no tagging, no embeddings)
- Don't modify `generate_site.py` or `split_articles.py` during pipeline work
- Don't commit `.env`
- Don't use PyMuPDF — not installable in this environment (externally-managed Python)
- Don't ask for confirmation on every file — batch the cost check, not per-file
