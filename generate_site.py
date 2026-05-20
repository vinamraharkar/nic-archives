#!/usr/bin/env python3
"""Generate a static HTML site from all NIC Archives newsletter articles.

Outputs:
  docs/index.html              — main index with all issues + Pagefind search
  docs/issues/{slug}.html      — per-issue table of contents
  docs/articles/{slug}.html    — individual article pages (Pagefind-indexed)
"""

import json
import os
import re
import shutil
from collections import defaultdict
from pathlib import Path

try:
    from PIL import Image as PILImage
    _PIL_AVAILABLE = True
except ImportError:
    _PIL_AVAILABLE = False

CROP_PADDING_PX = 12   # pixels of x-padding added around column in highlight view
CONTEXT_PX      = 150  # pixels of y-context shown above/below article in highlight view

BASE_DIR        = Path(__file__).parent
ARTICLES_DIR    = BASE_DIR / 'articles'
METADATA_DIR    = BASE_DIR / 'metadata'
DOCS_DIR        = BASE_DIR / 'docs'
DOCS_ARTICLES   = DOCS_DIR / 'articles'
DOCS_ISSUES     = DOCS_DIR / 'issues'
DOCS_PAGES_DIR  = DOCS_DIR / 'pages'
WORKER_URL      = 'https://nic-archives-search.nicarchives.workers.dev'
R2_PAGES_URL    = 'https://pub-aeebc89b75274bada82104943378de01.r2.dev'

MONTH_ORDER = {
    'January': 1, 'February': 2, 'March': 3, 'April': 4,
    'May': 5, 'June': 6, 'July': 7, 'August': 8,
    'September': 9, 'October': 10, 'November': 11, 'December': 12,
}

# ---------------------------------------------------------------------------
# CSS — Newspaper-archive aesthetic, full-width layout
# ---------------------------------------------------------------------------
CSS = """
@import url('https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400;1,500&family=Crimson+Text:ital,wght@0,400;0,600;0,700;1,400;1,600&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

body {
    background: #f7f0d8;
    color: #1e1408;
    font-family: 'Crimson Text', Georgia, serif;
    font-size: 18px;
    line-height: 1.75;
    min-height: 100vh;
    padding-top: 48px;
}

/* ── Slim fixed navbar ── */
.navbar {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    height: 48px;
    background: #1a0f07;
    border-bottom: 1px solid #b8892a;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 2rem;
    z-index: 100;
}
.navbar-brand {
    font-family: 'EB Garamond', Georgia, serif;
    font-size: 0.85rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    font-variant: small-caps;
    color: #b8892a;
    text-decoration: none;
    white-space: nowrap;
}
.navbar-brand:hover { color: #f7f0d8; }
.navbar-search-link {
    color: #b8892a;
    display: flex;
    align-items: center;
    text-decoration: none;
    padding: 0.25rem;
    transition: color 150ms;
}
.navbar-search-link:hover { color: #f7f0d8; }

/* ── Newspaper nameplate masthead ── */
.nameplate {
    border-bottom: 1px solid #b8892a;
    padding: 2rem 3rem 1.5rem;
    background: #f7f0d8;
}
.nameplate-rule-heavy {
    border: none;
    border-top: 4px solid #1a0f07;
    margin-bottom: 3px;
}
.nameplate-rule-thin {
    border: none;
    border-top: 1px solid #1a0f07;
    margin-bottom: 1.25rem;
}
.nameplate-grid {
    display: grid;
    grid-template-columns: 1fr auto 1fr;
    align-items: end;
    gap: 1rem;
}
.nameplate-side {
    font-size: 0.72rem;
    letter-spacing: 0.05em;
    color: #8a7355;
    font-family: 'Crimson Text', Georgia, serif;
    line-height: 1.65;
}
.nameplate-side.right { text-align: right; }
.nameplate-center { text-align: center; }
.nameplate-title {
    font-family: 'EB Garamond', Georgia, serif;
    font-size: clamp(2.5rem, 6vw, 5.5rem);
    font-weight: 800;
    letter-spacing: 0.12em;
    color: #7a1f1f;
    text-transform: uppercase;
    line-height: 1;
    white-space: nowrap;
}
.nameplate-subtitle {
    font-size: 0.75rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #8a7355;
    margin-top: 0.4rem;
    font-family: 'Crimson Text', Georgia, serif;
}
.nameplate-side a { color: #8a7355; text-decoration: none; }
.nameplate-side a:hover { color: #7a1f1f; }
.nameplate-rule-gold {
    border: none;
    border-top: 1px solid #b8892a;
    margin-top: 1.25rem;
}

/* Smaller nameplate variant for issue TOC pages */
.nameplate-sm .nameplate-title { font-size: clamp(1.8rem, 3.5vw, 3rem); }
.nameplate-sm .nameplate-side  { font-size: 0.68rem; }

/* ── Homepage content wrapper ── */
.home-content {
    max-width: 1400px;
    margin: 0 auto;
    padding: 0 2.5rem 4rem;
}

/* ── Archive blurb (plain text, no bordered box) ── */
.archive-blurb {
    max-width: 700px;
    margin: 1.5rem auto;
    font-size: 0.95rem;
    font-style: italic;
    color: #4a3820;
    line-height: 1.65;
    font-family: 'Crimson Text', Georgia, serif;
    text-align: center;
}
.archive-blurb strong { color: #7a1f1f; font-style: normal; }
.archive-blurb a { color: #7a1f1f; text-decoration: none; }
.archive-blurb a:hover { text-decoration: underline; }

/* ── Semantic search widget ── */
.search-wrap {
    max-width: 660px;
    margin: 1.5rem auto;
}
.sem-tabs {
    display: flex;
    border-bottom: 2px solid #b8892a;
    margin-bottom: 0.75rem;
    gap: 0;
}
.sem-tab {
    background: none;
    border: none;
    padding: 0.4rem 1.1rem;
    font-family: 'Crimson Text', Georgia, serif;
    font-size: 0.88rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #8a7355;
    cursor: pointer;
    border-bottom: 2px solid transparent;
    margin-bottom: -2px;
    transition: color 150ms, border-color 150ms;
}
.sem-tab.active { color: #7a1f1f; border-bottom-color: #7a1f1f; }
.sem-tab:hover:not(.active) { color: #1e1408; }
.sem-form {
    display: flex;
    gap: 0.5rem;
}
.sem-input {
    flex: 1;
    padding: 0.5rem 0.75rem;
    border: 1px solid #b8892a;
    background: #ede6c0;
    font-family: 'Crimson Text', Georgia, serif;
    font-size: 1rem;
    color: #1e1408;
    outline: none;
    border-radius: 2px;
}
.sem-input:focus { border-color: #7a1f1f; }
.sem-btn {
    padding: 0.5rem 1rem;
    background: #7a1f1f;
    color: #f7f0d8;
    border: none;
    font-family: 'Crimson Text', Georgia, serif;
    font-size: 0.9rem;
    letter-spacing: 0.08em;
    cursor: pointer;
    border-radius: 2px;
    transition: background 150ms;
    white-space: nowrap;
}
.sem-btn:hover { background: #5a1515; }
.sem-btn:disabled { opacity: 0.55; cursor: default; }
.sem-status {
    font-size: 0.82rem;
    font-style: italic;
    color: #8a7355;
    margin-top: 0.5rem;
    min-height: 1.2em;
    font-family: 'Crimson Text', Georgia, serif;
}
.sem-results { margin-top: 1rem; }
.sem-answer-box {
    background: #ede6c0;
    border: 1px solid #b8892a;
    border-left: 3px solid #7a1f1f;
    padding: 0.85rem 1rem;
    margin-bottom: 1rem;
    font-size: 0.95rem;
    line-height: 1.65;
    font-family: 'Crimson Text', Georgia, serif;
    color: #1e1408;
}
.sem-answer-label {
    font-size: 0.7rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #8a7355;
    margin-bottom: 0.4rem;
    font-family: 'Crimson Text', Georgia, serif;
}
.sem-card {
    border-bottom: 1px solid #d4c090;
    padding: 0.65rem 0;
    display: flex;
    gap: 0.75rem;
    align-items: flex-start;
}
.sem-card-thumb {
    width: 72px;
    height: 100px;
    object-fit: cover;
    flex-shrink: 0;
    border: 1px solid #d4c090;
    display: block;
}
.sem-card-num {
    font-size: 0.72rem;
    color: #8a7355;
    min-width: 1.4rem;
    font-family: 'Crimson Text', Georgia, serif;
    flex-shrink: 0;
}
.sem-card-body { flex: 1; min-width: 0; }
.sem-card-title {
    font-family: 'EB Garamond', Georgia, serif;
    font-weight: 600;
    font-size: 1rem;
    color: #7a1f1f;
    text-decoration: none;
    display: block;
    line-height: 1.3;
}
.sem-card-title:hover { text-decoration: underline; }
.sem-card-meta {
    font-size: 0.78rem;
    color: #8a7355;
    margin: 0.1rem 0 0.25rem;
    font-family: 'Crimson Text', Georgia, serif;
}
.sem-card-snippet {
    font-size: 0.87rem;
    color: #3a2a15;
    line-height: 1.55;
    font-family: 'Crimson Text', Georgia, serif;
}
.sem-citations-label {
    font-size: 0.72rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #8a7355;
    margin: 0.85rem 0 0.3rem;
    font-family: 'Crimson Text', Georgia, serif;
}
.sem-result-count {
    font-size: 0.75rem;
    color: #8a7355;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    font-family: 'Crimson Text', Georgia, serif;
    margin-bottom: 0.4rem;
}
.sem-more-btn {
    display: block;
    margin: 1rem auto 0;
    padding: 0.45rem 1.4rem;
    background: none;
    border: 1px solid #b8892a;
    color: #7a1f1f;
    font-family: 'Crimson Text', Georgia, serif;
    font-size: 0.88rem;
    letter-spacing: 0.08em;
    cursor: pointer;
    border-radius: 2px;
    transition: background 150ms, color 150ms;
}
.sem-more-btn:hover { background: #7a1f1f; color: #f7f0d8; }
.sem-error {
    color: #7a1f1f;
    font-size: 0.88rem;
    font-style: italic;
    font-family: 'Crimson Text', Georgia, serif;
}

/* ── Section rule ── */
.section-rule {
    font-size: 0.72rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    font-variant: small-caps;
    color: #1e1408;
    border-bottom: 2px solid #b8892a;
    padding-bottom: 0.35rem;
    margin: 2rem 0 1rem;
}

/* ── Year filter pills ── */
.filter-bar {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin: 0 0 1.5rem;
}
.filter-pill {
    padding: 0.25rem 0.8rem;
    border: 1px solid #c9a96e;
    background: transparent;
    color: #8a7355;
    font-size: 0.78rem;
    letter-spacing: 0.08em;
    cursor: pointer;
    font-family: 'Crimson Text', Georgia, serif;
    transition: all 150ms;
}
.filter-pill:hover, .filter-pill.active {
    background: #7a1f1f;
    border-color: #7a1f1f;
    color: #f7f0d8;
}

/* ── Issues grid — 4 columns desktop ── */
.issues-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1.5rem;
}
.issue-card {
    display: block;
    border: 1px solid #c9a96e;
    background: #ede6c0;
    text-decoration: none;
    color: inherit;
    transition: border-color 200ms, box-shadow 200ms, transform 200ms;
    cursor: pointer;
    overflow: hidden;
}
.issue-card:hover {
    border-color: #b8892a;
    box-shadow: 0 6px 24px rgba(0,0,0,0.2);
    transform: translateY(-2px);
}
.issue-card-cover {
    width: 100%;
    height: 220px;
    overflow: hidden;
    background: #d8cfac;
    border-bottom: 1px solid #c9a96e;
}
.issue-card-cover img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: top center;
    display: block;
    transition: opacity 200ms;
}
.issue-card:hover .issue-card-cover img { opacity: 0.88; }
.issue-card-info { padding: 0.75rem 0.85rem 0.75rem; }
.issue-card-date {
    font-family: 'EB Garamond', Georgia, serif;
    font-size: 1.05rem;
    font-weight: 700;
    color: #7a1f1f;
    line-height: 1.2;
}
.issue-card-count {
    font-size: 0.75rem;
    color: #8a7355;
    font-style: italic;
    margin-top: 0.2rem;
}

/* ── Page thumbnail strip (issue TOC page) ── */
.page-strip {
    display: flex;
    gap: 0.75rem;
    overflow-x: auto;
    padding: 0.5rem 0 1.25rem;
    margin-bottom: 1.5rem;
    border-bottom: 1px solid #c9a96e;
    scrollbar-width: thin;
    scrollbar-color: #b8892a #f7f0d8;
}
.page-strip::-webkit-scrollbar { height: 4px; }
.page-strip::-webkit-scrollbar-track { background: #f7f0d8; }
.page-strip::-webkit-scrollbar-thumb { background: #b8892a; border-radius: 2px; }
.page-thumb { flex: 0 0 auto; text-decoration: none; cursor: pointer; }
.page-thumb img {
    width: 140px;
    height: 197px;
    object-fit: cover;
    object-position: top;
    border: 1px solid #c9a96e;
    display: block;
    transition: border-color 150ms, box-shadow 150ms;
}
.page-thumb:hover img {
    border-color: #7a1f1f;
    box-shadow: 0 2px 10px rgba(0,0,0,0.2);
}
.page-thumb-label {
    font-size: 0.75rem;
    text-align: center;
    color: #8a7355;
    margin-top: 0.3rem;
    font-style: italic;
    font-family: 'Crimson Text', Georgia, serif;
}

/* ── Issue TOC page wrapper ── */
.issue-toc-page {
    max-width: 1400px;
    margin: 0 auto;
    padding: 0 2.5rem 4rem;
}

/* ── TOC list — two columns on desktop ── */
.toc { list-style: none; }
.toc-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0 3rem;
}
.toc li {
    padding: 0.65rem 0;
    border-bottom: 1px solid #c9a96e;
    display: flex;
    align-items: baseline;
    gap: 0.75rem;
}
.toc-num {
    color: #b8892a;
    font-style: italic;
    min-width: 2.5rem;
    flex-shrink: 0;
    font-family: 'EB Garamond', Georgia, serif;
}
.toc-section-label {
    font-size: 0.72rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #7a1f1f;
    border: 1px solid #7a1f1f;
    padding: 0.1rem 0.3rem;
    white-space: nowrap;
    flex-shrink: 0;
    margin-right: 0.4rem;
}
.toc a {
    color: #1e1408;
    text-decoration: none;
    font-size: 1.05rem;
    font-family: 'Crimson Text', Georgia, serif;
}
.toc a:hover { color: #7a1f1f; text-decoration: underline; }
.toc-meta {
    font-size: 0.78rem;
    color: #8a7355;
    font-style: italic;
    margin-top: 0.2rem;
}

/* ── Two-panel article layout — 50/50 full-width ── */
.article-container {
    width: 100%;
    display: grid;
    grid-template-columns: 1fr 1fr;
    align-items: start;
    min-height: calc(100vh - 48px);
}

/* ── Scan panel (left) — parchment background ── */
.scan-panel {
    background: #f7f0d8;
    padding: 2rem;
    position: sticky;
    top: 48px;
    max-height: calc(100vh - 48px);
    overflow-y: auto;
    border-right: 1px solid #c9a96e;
    scrollbar-width: thin;
    scrollbar-color: #b8892a #f7f0d8;
}
.scan-panel::-webkit-scrollbar { width: 4px; }
.scan-panel::-webkit-scrollbar-track { background: #f7f0d8; }
.scan-panel::-webkit-scrollbar-thumb { background: #b8892a; border-radius: 2px; }
.scan-panel-label {
    font-size: 0.68rem;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: #b8892a;
    margin-bottom: 0.6rem;
    font-family: 'Crimson Text', Georgia, serif;
}
.scan-panel-item { margin-bottom: 1.5rem; }
.scan-panel-item:last-child { margin-bottom: 0; }
.scan-panel-item a { display: block; text-decoration: none; cursor: pointer; }
.scan-panel-item img {
    width: 100%;
    height: auto;
    display: block;
    border: 1px solid #c9a96e;
    transition: border-color 150ms, box-shadow 150ms;
}
.scan-panel-item a:hover img {
    border-color: #b8892a;
    box-shadow: 0 2px 12px rgba(0,0,0,0.15);
}
.scan-panel-caption {
    font-size: 0.72rem;
    color: #8a7355;
    font-style: italic;
    margin-top: 0.35rem;
    text-align: center;
    font-family: 'Crimson Text', Georgia, serif;
}
.scan-panel-caption a { color: #b8892a; text-decoration: none; }
.scan-panel-caption a:hover { text-decoration: underline; }
.scan-divider {
    border: none;
    border-top: 1px solid #b8892a;
    margin: 1.5rem 0;
}

/* ── Text panel (right) ── */
.text-panel {
    padding: 3rem 3.5rem 4rem;
    background: #f7f0d8;
}
.text-panel-inner { max-width: 680px; }

/* ── Breadcrumb ── */
.breadcrumb {
    font-size: 0.78rem;
    color: #8a7355;
    font-family: 'Crimson Text', Georgia, serif;
    margin-bottom: 1.5rem;
    letter-spacing: 0.03em;
}
.breadcrumb a { color: #7a1f1f; text-decoration: none; }
.breadcrumb a:hover { text-decoration: underline; }
.breadcrumb-sep { margin: 0 0.35rem; color: #c9a96e; }

/* ── Article header ── */
.article-header {
    padding-bottom: 1rem;
    margin-bottom: 1.8rem;
    border-bottom: 1px solid #c9a96e;
}
.article-section-badge {
    font-size: 0.65rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #7a1f1f;
    border: 1px solid #7a1f1f;
    padding: 0.1rem 0.35rem;
    display: inline-block;
    margin-bottom: 0.6rem;
    font-family: 'Crimson Text', Georgia, serif;
}
h1.article-title {
    font-family: 'EB Garamond', Georgia, serif;
    font-size: 2.4rem;
    font-weight: 700;
    line-height: 1.2;
    color: #7a1f1f;
    margin-bottom: 0.5rem;
}
hr.title-rule {
    border: none;
    border-top: 1px solid #b8892a;
    margin: 0.7rem 0;
}
.article-byline {
    font-size: 0.9rem;
    color: #8a7355;
    font-style: italic;
    font-family: 'Crimson Text', Georgia, serif;
}
.article-issue-link {
    font-size: 0.85rem;
    color: #8a7355;
    margin-top: 0.3rem;
    font-family: 'Crimson Text', Georgia, serif;
}
.article-issue-link a { color: #7a1f1f; text-decoration: none; }
.article-issue-link a:hover { text-decoration: underline; }

/* ── Article body ── */
.article-body p {
    margin-bottom: 1.1rem;
    text-align: justify;
    hyphens: auto;
    font-family: 'Crimson Text', Georgia, serif;
    font-size: 1.05rem;
    line-height: 1.75;
}
.article-body p.first-para::first-letter {
    font-size: 3.8em;
    float: left;
    line-height: 0.82;
    color: #7a1f1f;
    font-weight: 700;
    margin: 0.05em 0.12em 0 0;
    font-family: 'EB Garamond', Georgia, serif;
}
.article-body h2.section-heading {
    font-family: 'EB Garamond', Georgia, serif;
    font-size: 1.05rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #7a1f1f;
    margin: 2rem 0 0.7rem;
}
.article-body h2.section-heading::before { content: '\\2014 '; color: #b8892a; }
.article-body ul, .article-body ol { margin: 0.75rem 0 1rem 1.5rem; }
.article-body li { margin-bottom: 0.35rem; font-family: 'Crimson Text', Georgia, serif; }
.ornament {
    text-align: center;
    color: #b8892a;
    font-size: 1rem;
    letter-spacing: 0.5em;
    margin: 1.5rem 0;
}

/* ── Prev/next article navigation ── */
.article-nav {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 1.5rem;
    margin-top: 3rem;
    padding-top: 1.5rem;
    border-top: 1px solid #c9a96e;
}
.article-nav-link {
    max-width: 45%;
    text-decoration: none;
    color: #8a7355;
    font-family: 'Crimson Text', Georgia, serif;
    transition: color 150ms;
}
.article-nav-link:hover { color: #7a1f1f; }
.article-nav-dir {
    font-size: 0.7rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    display: block;
    margin-bottom: 0.25rem;
    color: #b8892a;
}
.article-nav-title {
    font-family: 'EB Garamond', Georgia, serif;
    font-size: 1rem;
    color: #1e1408;
    line-height: 1.3;
    display: block;
}
.article-nav-link:hover .article-nav-title { color: #7a1f1f; }
.article-nav-link.next { text-align: right; margin-left: auto; }

/* ── Figure / image ── */
figure.article-image {
    margin: 1.5rem 0;
    border: 1px solid #b8892a;
    background: #ede6c0;
    padding: 0.75rem;
}
figure.article-image img { max-width: 100%; height: auto; display: block; margin: 0 auto 0.6rem; }
figure.article-image figcaption { font-size: 0.8rem; color: #8a7355; font-style: italic; line-height: 1.5; }

/* ── Footnotes ── */
.footnote {
    font-size: 0.82rem;
    color: #8a7355;
    border-top: 1px solid #b8892a;
    padding-top: 0.6rem;
    margin-top: 2rem;
    font-style: italic;
    font-family: 'Crimson Text', Georgia, serif;
}
.footnote sup { font-size: 0.7rem; vertical-align: super; margin-right: 0.2rem; }

/* ── Skip navigation ── */
.skip-link {
    position: absolute;
    left: -9999px;
    top: 0;
    z-index: 200;
    padding: 0.5rem 1rem;
    background: #b8892a;
    color: #1e1408;
    font-family: 'Crimson Text', Georgia, serif;
    font-size: 0.9rem;
    text-decoration: none;
}
.skip-link:focus { left: 0; }

/* ── Global focus ── */
:focus-visible { outline: 2px solid #b8892a; outline-offset: 2px; }

/* ── Responsive ── */
@media (max-width: 1200px) {
    .issues-grid { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 900px) {
    .toc-grid { grid-template-columns: 1fr; }
    .article-container { grid-template-columns: 1fr; }
    .scan-panel {
        position: static;
        max-height: none;
        overflow-y: visible;
        border-right: none;
        border-bottom: 1px solid #c9a96e;
        padding: 1.5rem;
    }
    .text-panel { padding: 2rem 1.5rem 3rem; }
    h1.article-title { font-size: 1.9rem; }
    .nameplate { padding: 1.5rem 1.5rem 1rem; }
    .home-content, .issue-toc-page { padding: 0 1.5rem 3rem; }
}
@media (max-width: 600px) {
    .issues-grid { grid-template-columns: 1fr; }
    .nameplate { padding: 1rem; }
    .nameplate-grid { grid-template-columns: 1fr; text-align: center; }
    .nameplate-side { display: none; }
    .home-content, .issue-toc-page { padding: 0 1rem 2rem; }
    .text-panel { padding: 1.5rem 1.25rem 2.5rem; }
    h1.article-title { font-size: 1.65rem; }
    .article-nav { flex-direction: column; }
    .article-nav-link, .article-nav-link.next { text-align: left; margin-left: 0; max-width: 100%; }
    .navbar { padding: 0 1rem; }
}
"""


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def roman(n: int) -> str:
    vals = [(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
    r = ''
    for v, s in vals:
        while n >= v:
            r += s; n -= v
    return r


def page_display(pages: list) -> str:
    if not pages: return ''
    if len(pages) == 1: return f'p. {pages[0]}'
    return f'pp. {pages[0]}–{pages[-1]}'


def html_escape(text: str) -> str:
    return (text
            .replace('&', '&amp;').replace('<', '&lt;')
            .replace('>', '&gt;').replace('"', '&quot;'))


def inline_md(text: str) -> str:
    text = re.sub(r'\$_\{[^}]+\}\$', '', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<em>\1</em>', text)
    return text


def parse_frontmatter(text: str) -> tuple:
    """Parse YAML-like frontmatter. Returns (meta_dict, body_text)."""
    if not text.startswith('---\n'):
        return {}, text
    parts = text.split('---\n', 2)
    if len(parts) < 3:
        return {}, text

    meta = {}
    for line in parts[1].splitlines():
        m = re.match(r'^(\w+):\s*(.+)$', line)
        if not m: continue
        key, val = m.group(1), m.group(2).strip()
        if val == 'null':
            meta[key] = None
        elif val.startswith('"') and val.endswith('"'):
            meta[key] = val[1:-1]
        elif val.startswith('[') and val.endswith(']'):
            inner = val[1:-1]
            meta[key] = [int(x.strip()) for x in inner.split(',') if x.strip().isdigit()]
        else:
            try: meta[key] = int(val)
            except ValueError: meta[key] = val
    return meta, parts[2]


def get_issue_date(meta: dict) -> str:
    """Normalise: new pipeline uses issue_date, 1992 articles use date."""
    return meta.get('issue_date') or meta.get('date') or 'Unknown'


def make_issue_slug(issue_date: str) -> str:
    return issue_date.lower().replace(' ', '-')


def issue_sort_key(issue_date: str) -> tuple:
    parts = issue_date.split()
    if len(parts) == 2:
        return (int(parts[1]), MONTH_ORDER.get(parts[0], 0))
    return (0, 0)


def extract_images() -> dict:
    """Extract base64 images from document.md (1992 issue only)."""
    doc_path = BASE_DIR / 'document.md'
    if not doc_path.exists():
        return {}
    with open(doc_path, encoding='utf-8') as f:
        content = f.read()

    pages = content.split('\n---\n')
    result = {}
    for page_idx, page_block in enumerate(pages):
        page_num = page_idx + 1
        b64_list = re.findall(r'!\[Image\]\(data:image/jpeg;base64,([^)]+)\)', page_block)
        if not b64_list: continue

        meta_path = METADATA_DIR / f'page_00{page_num}.json'
        if not meta_path.exists(): continue
        with open(meta_path, encoding='utf-8') as f:
            meta = json.load(f)

        image_blocks = [b for b in meta['blocks'] if b['layout_tag'] == 'image']
        image_blocks.sort(key=lambda b: b['reading_order'])
        for b64, block in zip(b64_list, image_blocks):
            normalized = re.sub(r'\s+', ' ', block['text']).strip()
            result[normalized] = b64
    return result


def md_to_html(body: str, images: dict) -> str:
    """Convert article markdown body to HTML."""
    lines = body.splitlines()
    html_parts = []
    pending_para = []
    first_para_emitted = False
    in_image = False
    image_desc_lines = []
    in_list = False
    list_tag = 'ul'

    def flush_para():
        nonlocal first_para_emitted
        if pending_para:
            text = ' '.join(pending_para).strip()
            if text:
                cls = '' if first_para_emitted else ' class="first-para"'
                html_parts.append(f'<p{cls}>{inline_md(html_escape(text))}</p>')
                first_para_emitted = True
            pending_para.clear()

    def flush_list():
        nonlocal in_list
        if in_list:
            html_parts.append(f'</{list_tag}>')
            in_list = False

    def render_image(desc_text):
        normalized = re.sub(r'\s+', ' ', desc_text).strip()
        b64 = images.get(normalized, '')
        escaped = html_escape(normalized)
        if b64:
            html_parts.append(
                f'<figure class="article-image">'
                f'<img src="data:image/jpeg;base64,{b64}" alt="{escaped}">'
                f'<figcaption>{escaped}</figcaption></figure>'
            )
        else:
            html_parts.append(
                f'<figure class="article-image"><figcaption>{escaped}</figcaption></figure>'
            )

    for line in lines:
        if in_image:
            stripped = line.rstrip()
            if stripped.endswith('*'):
                image_desc_lines.append(stripped.rstrip('*'))
                render_image(' '.join(image_desc_lines))
                in_image = False; image_desc_lines = []
            else:
                image_desc_lines.append(stripped)
            continue

        # Skip ## article title heading
        if re.match(r'^## ', line):
            continue

        # ### subheading → h2 for correct document outline (h1 is article title)
        m = re.match(r'^### (.+)$', line)
        if m:
            flush_para(); flush_list()
            html_parts.append(f'<h2 class="section-heading">{html_escape(m.group(1).strip())}</h2>')
            continue

        # Image blockquote
        m = re.match(r'^> \*\*\[Image\]\*\* \*(.+)$', line)
        if m:
            flush_para(); flush_list()
            rest = m.group(1)
            if rest.rstrip().endswith('*'):
                render_image(rest.rstrip().rstrip('*'))
            else:
                in_image = True; image_desc_lines = [rest]
            continue

        # Bullet list item: - text or * text
        m = re.match(r'^[-*]\s+(.+)$', line)
        if m:
            flush_para()
            if not in_list:
                html_parts.append('<ul class="article-list">'); in_list = True; list_tag = 'ul'
            html_parts.append(f'<li>{inline_md(html_escape(m.group(1).strip()))}</li>')
            continue

        # Numbered list item: N. text
        m = re.match(r'^\d+\.\s+(.+)$', line)
        if m:
            flush_para()
            if not in_list:
                html_parts.append('<ol class="article-list">'); in_list = True; list_tag = 'ol'
            html_parts.append(f'<li>{inline_md(html_escape(m.group(1).strip()))}</li>')
            continue

        # Footnote
        m = re.match(r'^\[\^(\d+)\]: (.+)$', line)
        if m:
            flush_para(); flush_list()
            html_parts.append(
                f'<div class="footnote"><sup>{m.group(1)}</sup> {inline_md(html_escape(m.group(2)))}</div>'
            )
            continue

        # Blank line
        if line.strip() == '':
            flush_para(); flush_list()
            continue

        # Normal text — if we were in a list, close it first
        if in_list:
            flush_list()
        pending_para.append(line.strip())

    flush_para(); flush_list()
    return '\n'.join(html_parts)


# ---------------------------------------------------------------------------
# Page renderers
# ---------------------------------------------------------------------------

_SEARCH_ICON = (
    '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
    'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
    '<circle cx="11" cy="11" r="8"/>'
    '<line x1="21" y1="21" x2="16.65" y2="16.65"/>'
    '</svg>'
)


def _base_html(title: str, body: str, depth: int = 0) -> str:
    """Wrap body in full HTML document. depth=0 for docs/, depth=1 for subdirs."""
    root_path = '../' * depth
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="worker-url" content="{WORKER_URL}">
<title>{html_escape(title)}</title>
<style>{CSS}</style>
</head>
<body>
<a class="skip-link" href="#main-content">Skip to content</a>
<nav class="navbar">
  <a class="navbar-brand" href="{root_path}index.html">Informatics Archive</a>
  <a class="navbar-search-link" href="{root_path}index.html" aria-label="Search">{_SEARCH_ICON}</a>
</nav>
{body}
</body>
</html>"""


def _search_widget_html(depth: int = 0) -> str:
    """Semantic search widget (search + ask tabs + results). depth=1 for docs subdirs."""
    root = '../' * depth
    return f"""<div class="search-wrap">
      <div class="sem-tabs" role="tablist">
        <button class="sem-tab active" id="tab-search" role="tab" aria-selected="true" onclick="semSwitchTab('search')">Search</button>
        <button class="sem-tab" id="tab-ask" role="tab" aria-selected="false" onclick="semSwitchTab('ask')">Ask</button>
      </div>
      <div class="sem-form">
        <input class="sem-input" id="sem-input" type="text" autocomplete="off"
               placeholder="Search 30 years of NIC Informatics\u2026"
               onkeydown="if(event.key==='Enter')semSubmit()">
        <button class="sem-btn" id="sem-btn" onclick="semSubmit()">Search</button>
      </div>
      <div class="sem-status" id="sem-status"></div>
      <div class="sem-results" id="sem-results"></div>
    </div>

  <script>
    const WORKER = document.querySelector('meta[name="worker-url"]').content;
    const _ROOT = '{root}';
    let _mode = 'search';

    function semSwitchTab(mode) {{
      _mode = mode;
      document.getElementById('tab-search').classList.toggle('active', mode === 'search');
      document.getElementById('tab-ask').classList.toggle('active', mode === 'ask');
      document.getElementById('tab-search').setAttribute('aria-selected', mode === 'search');
      document.getElementById('tab-ask').setAttribute('aria-selected', mode === 'ask');
      document.getElementById('sem-btn').textContent = mode === 'ask' ? 'Ask' : 'Search';
      document.getElementById('sem-input').placeholder = mode === 'ask'
        ? 'Ask anything about NIC\u2019s history\u2026'
        : 'Search 30 years of NIC Informatics\u2026';
      document.getElementById('sem-results').innerHTML = '';
      document.getElementById('sem-status').textContent = '';
    }}

    async function semSubmit() {{
      const q = document.getElementById('sem-input').value.trim();
      if (!q) return;
      const btn = document.getElementById('sem-btn');
      const status = document.getElementById('sem-status');
      const results = document.getElementById('sem-results');
      btn.disabled = true;
      status.textContent = _mode === 'ask' ? 'Searching sources and composing answer\u2026' : 'Searching\u2026';
      results.innerHTML = '';
      try {{
        const resp = await fetch(WORKER + '/' + _mode, {{
          method: 'POST',
          headers: {{ 'Content-Type': 'application/json' }},
          body: JSON.stringify({{ query: q, limit: 24 }})
        }});
        if (!resp.ok) throw new Error('Worker error ' + resp.status);
        const data = await resp.json();
        if (data.error) throw new Error(data.error);
        status.textContent = '';
        if (_mode === 'search') renderSearch(data);
        else renderAsk(data);
      }} catch(e) {{
        status.textContent = '';
        results.innerHTML = '<p class="sem-error">Search unavailable: ' + e.message + '</p>';
      }} finally {{
        btn.disabled = false;
      }}
    }}

    function esc(s) {{ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }}

    function relUrl(u) {{ return _ROOT + u.replace(/^\//, ''); }}

    function issueSlug(d) {{ return d.toLowerCase().replace(' ', '-'); }}

    function thumbImg(d) {{
      const slug = issueSlug(d);
      return `<img class="sem-card-thumb" src="{R2_PAGES_URL}/pages/${{slug}}/page-1.jpg" loading="lazy" alt="${{esc(d)}} cover" onerror="this.style.display='none'">`;
    }}

    let _allResults = [];
    const _PAGE = 8;

    function renderSearch(items) {{
      if (!items.length) {{ document.getElementById('sem-results').innerHTML = '<p class="sem-error">No results found.</p>'; return; }}
      _allResults = items;
      _renderVisible(_PAGE);
    }}

    function _renderVisible(upTo) {{
      const visible = _allResults.slice(0, upTo);
      const hasMore = upTo < _allResults.length;
      const countLine = `<div class="sem-result-count">Showing ${{visible.length}} of ${{_allResults.length}} result${{_allResults.length === 1 ? '' : 's'}}</div>`;
      const cards = visible.map(r => `
        <div class="sem-card">
          ${{thumbImg(r.issue_date)}}
          <div class="sem-card-body">
            <a class="sem-card-title" href="${{relUrl(esc(r.url))}}">${{esc(r.title)}}</a>
            <div class="sem-card-meta">${{esc(r.issue_date)}}</div>
            <div class="sem-card-snippet">${{esc((r.body_snippet||'').slice(0,350))}}&hellip;</div>
          </div>
        </div>`).join('');
      const btn = hasMore
        ? `<button class="sem-more-btn" onclick="_renderVisible(${{upTo + _PAGE}})">Show more results</button>`
        : '';
      document.getElementById('sem-results').innerHTML = countLine + cards + btn;
    }}

    function renderAsk(data) {{
      const cites = (data.citations || []).map((c, i) =>
        `<div class="sem-card">
           ${{thumbImg(c.issue_date)}}
           <div class="sem-card-body">
             <div class="sem-card-num">${{i+1}}.</div>
             <a class="sem-card-title" href="${{relUrl(esc(c.url))}}">${{esc(c.title)}}</a>
             <div class="sem-card-meta">${{esc(c.issue_date)}}</div>
           </div>
         </div>`).join('');
      document.getElementById('sem-results').innerHTML =
        `<div class="sem-answer-box"><div class="sem-answer-label">Answer</div>${{esc(data.answer)}}</div>` +
        (cites ? `<div class="sem-citations-label">Sources</div>${{cites}}` : '');
    }}
  </script>"""


def render_index(issues_data: list) -> str:
    """Main index: newspaper nameplate + search + year filter + issue card grid."""
    years = sorted({issue_sort_key(d['date'])[0] for d in issues_data})
    most_recent = issues_data[-1]['date'] if issues_data else ''
    total_issues = len(issues_data)
    total_articles = sum(d['count'] for d in issues_data)

    filter_pills = '<button class="filter-pill active" data-year="all" onclick="filterYear(this,\'all\')">All</button>'
    for y in years:
        filter_pills += f'<button class="filter-pill" data-year="{y}" onclick="filterYear(this,\'{y}\')">{y}</button>'

    cards = []
    for issue in issues_data:
        slug = make_issue_slug(issue['date'])
        year = issue_sort_key(issue['date'])[0]
        count = issue['count']
        cover_path = DOCS_PAGES_DIR / slug / 'page-1.jpg'
        cover_html = (
            f'<div class="issue-card-cover">'
            f'<img src="{R2_PAGES_URL}/pages/{slug}/page-1.jpg" alt="{html_escape(issue["date"])} cover" loading="lazy">'
            f'</div>'
        ) if cover_path.exists() else '<div class="issue-card-cover"></div>'
        cards.append(
            f'<a class="issue-card" href="issues/{slug}.html" data-year="{year}">'
            f'{cover_html}'
            f'<div class="issue-card-info">'
            f'<div class="issue-card-date">{html_escape(issue["date"])}</div>'
            f'<div class="issue-card-count">{count} article{"s" if count != 1 else ""}</div>'
            f'</div>'
            f'</a>'
        )

    grid = '\n'.join(cards)

    body = f"""
  <header class="nameplate">
    <hr class="nameplate-rule-heavy">
    <hr class="nameplate-rule-thin">
    <div class="nameplate-grid">
      <div class="nameplate-side">Est.&nbsp;1989<br>Quarterly Newsletter<br>New&nbsp;Delhi,&nbsp;India</div>
      <div class="nameplate-center">
        <div class="nameplate-title">Informatics</div>
        <div class="nameplate-subtitle">National Informatics Centre &bull; Government of India</div>
      </div>
      <div class="nameplate-side right">Most&nbsp;recent:&nbsp;{html_escape(most_recent)}<br>{total_issues}&nbsp;issues&nbsp;archived<br>{total_articles}&nbsp;articles</div>
    </div>
    <hr class="nameplate-rule-gold">
  </header>

  <main id="main-content" class="home-content">
    {_search_widget_html(depth=0)}

    <p class="archive-blurb">
      <strong>NIC Informatics</strong> is the quarterly newsletter of India's
      <a href="https://www.nic.in/" target="_blank" rel="noopener">National Informatics Centre</a>
      — the government body that has powered e-governance since 1975.
      This archive makes 30+ years of that history searchable for the first time.
    </p>

    <p class="section-rule">Browse by Issue</p>
    <div class="filter-bar">{filter_pills}</div>
    <div class="issues-grid" id="issues-grid">
      {grid}
    </div>
  </main>

  <script>
    function filterYear(btn, year) {{
      document.querySelectorAll('.filter-pill').forEach(p => p.classList.remove('active'));
      btn.classList.add('active');
      document.querySelectorAll('.issue-card').forEach(card => {{
        card.style.display = (year === 'all' || card.dataset.year === year) ? '' : 'none';
      }});
    }}
  </script>"""

    return _base_html('Informatics — NIC Archives', body, depth=0)


def render_issue_page(issue_date: str, articles: list, page_images: list = None) -> str:
    """Per-issue TOC page: smaller nameplate + thumbnail strip + two-column TOC."""
    slug = make_issue_slug(issue_date)

    strip_html = ''
    if page_images:
        thumbs = []
        for n in page_images:
            img_rel = f'{R2_PAGES_URL}/pages/{slug}/page-{n}.jpg'
            thumbs.append(
                f'<a class="page-thumb" href="{img_rel}" target="_blank" title="Open page {n}">'
                f'<img src="{img_rel}" alt="Page {n}" loading="lazy">'
                f'<div class="page-thumb-label">p.&thinsp;{n}</div>'
                f'</a>'
            )
        strip_html = f'<div class="page-strip">{"".join(thumbs)}</div>'

    items = []
    for idx, (meta, filename) in enumerate(articles, start=1):
        title = html_escape(meta.get('title', 'Untitled'))
        author = meta.get('author')
        section = meta.get('section')
        pages = meta.get('pages', [])
        stem = filename.replace('.md', '.html')

        badge = f'<span class="toc-section-label">{html_escape(section)}</span>' if section else ''
        meta_parts = []
        if author: meta_parts.append(f'By {html_escape(author)}')
        if pages: meta_parts.append(page_display(pages))
        meta_line = f'<div class="toc-meta">{" &bull; ".join(meta_parts)}</div>' if meta_parts else ''

        items.append(
            f'<li>'
            f'<span class="toc-num">{roman(idx)}.</span>'
            f'<div>{badge}<a href="../articles/{stem}">{title}</a>{meta_line}</div>'
            f'</li>'
        )

    items_html = '\n'.join(items)
    count = len(articles)

    body = f"""
  <header class="nameplate nameplate-sm">
    <hr class="nameplate-rule-heavy">
    <hr class="nameplate-rule-thin">
    <div class="nameplate-grid">
      <div class="nameplate-side"><a href="../index.html">&larr; All Issues</a></div>
      <div class="nameplate-center">
        <div class="nameplate-title">Informatics</div>
        <div class="nameplate-subtitle">{html_escape(issue_date)} &bull; {count} article{"s" if count != 1 else ""}</div>
      </div>
      <div class="nameplate-side right">National Informatics Centre<br>Government of India</div>
    </div>
    <hr class="nameplate-rule-gold">
  </header>

  <main id="main-content" class="issue-toc-page">
    {strip_html}
    <p class="section-rule">Table of Contents</p>
    <ul class="toc toc-grid">{items_html}</ul>
    <p class="section-rule">Search the Archive</p>
    {_search_widget_html(depth=1)}
  </main>"""

    return _base_html(f'Informatics — {issue_date}', body, depth=1)


def get_issue_pages(issue_slug: str) -> list:
    """Return sorted list of page numbers with images available for an issue."""
    page_dir = DOCS_PAGES_DIR / issue_slug
    if not page_dir.exists():
        return []
    pages = []
    for p in page_dir.glob('page-*.jpg'):
        m = re.search(r'page-(\d+)', p.name)
        if m:
            pages.append(int(m.group(1)))
    return sorted(pages)


def _load_coords(issue_slug: str) -> dict:
    """Load coords.json for an issue, or return {} if not found."""
    coords_path = DOCS_PAGES_DIR / issue_slug / 'coords.json'
    if coords_path.exists():
        return json.loads(coords_path.read_text())
    return {}


def _has_overlapping_y(article_slug: str, coords: dict, page_n: int) -> bool:
    """Return True if this article's bounding box overlaps another article in BOTH x and y.

    Articles in different columns legitimately share the same y-range, so a y-only check
    produces false positives for multi-column layouts. We require x-range overlap too:
    only articles that occupy the same column AND the same vertical band are truly
    conflicting (Gemini error). In that case the highlight would be misleading.
    """
    this = coords.get(article_slug, {}).get(str(page_n))
    if not this:
        return False
    for slug, pages in coords.items():
        if slug == article_slug:
            continue
        other = pages.get(str(page_n))
        if not other:
            continue
        y_overlap = this['y_start'] < other['y_end'] and this['y_end'] > other['y_start']
        x_overlap = this['x_start'] < other['x_end'] and this['x_end'] > other['x_start']
        if y_overlap and x_overlap:
            return True
    return False


def _make_crop(page_path: Path, bbox: dict, crop_path: Path) -> bool:
    """Crop page_path to the article bounding box and save to crop_path.

    Adds CROP_PADDING_PX of padding on all sides (clamped to image bounds).
    Returns True on success.
    """
    if not _PIL_AVAILABLE:
        return False
    try:
        img = PILImage.open(page_path)
        w, h = img.size
        x0 = max(0, bbox['x_start'] - CROP_PADDING_PX)
        y0 = max(0, bbox['y_start'] - CROP_PADDING_PX)
        x1 = min(w, bbox['x_end']   + CROP_PADDING_PX)
        y1 = min(h, bbox['y_end']   + CROP_PADDING_PX)
        cropped = img.crop((x0, y0, x1, y1))
        crop_path.parent.mkdir(parents=True, exist_ok=True)
        cropped.save(crop_path, 'JPEG', quality=88)
        return True
    except Exception as e:
        print(f'    [crop error] {crop_path.name}: {e}')
        return False


def _make_column_crop(page_path: Path, bbox: dict, crop_path: Path) -> bool:
    """Crop page to the article's column with CONTEXT_PX above/below for highlight display.

    The resulting image shows the article in context; a CSS overlay is drawn on top
    to highlight the exact article region. This avoids hard y-boundary errors from Gemini.
    """
    if not _PIL_AVAILABLE:
        return False
    try:
        img = PILImage.open(page_path)
        w, h = img.size
        x0 = max(0, bbox['x_start'] - CROP_PADDING_PX)
        x1 = min(w, bbox['x_end']   + CROP_PADDING_PX)
        y0 = max(0, bbox['y_start'] - CONTEXT_PX)
        y1 = min(h, bbox['y_end']   + CONTEXT_PX)
        col_crop = img.crop((x0, y0, x1, y1))
        crop_path.parent.mkdir(parents=True, exist_ok=True)
        col_crop.save(crop_path, 'JPEG', quality=88)
        return True
    except Exception as e:
        print(f'    [column crop error] {crop_path.name}: {e}')
        return False


def get_scan_panel_html(issue_slug: str, pages: list, article_slug: str = '') -> str:
    """Left-column scan panel: full-page JPGs on parchment background, no highlight overlay."""
    if not pages:
        return ''

    page_dir = DOCS_PAGES_DIR / issue_slug
    items = []
    for i, n in enumerate(pages):
        full_name = f'page-{n}.jpg'
        page_path = page_dir / full_name
        if not page_path.exists():
            continue

        full_rel = f'{R2_PAGES_URL}/pages/{issue_slug}/{full_name}'
        divider = '<hr class="scan-divider">' if i > 0 else ''
        items.append(
            f'{divider}'
            f'<div class="scan-panel-item">'
            f'<div class="scan-panel-label">Original scan &middot; Page&nbsp;{n}</div>'
            f'<a href="{full_rel}" target="_blank" title="Open full resolution">'
            f'<img src="{full_rel}" alt="Page {n}" loading="lazy">'
            f'</a>'
            f'<div class="scan-panel-caption">'
            f'<a href="{full_rel}" target="_blank">Open full resolution &nearr;</a>'
            f'</div>'
            f'</div>'
        )

    if not items:
        return ''

    return (
        f'<aside class="scan-panel">'
        f'{"".join(items)}'
        f'</aside>'
    )


def get_scan_viewer_html(issue_slug: str, pages: list, article_slug: str = '') -> str:
    """Return HTML for the original-page scan viewer, or '' if no images exist.

    When coords.json has a bounding box for this article, crops the page image
    to the exact article region and shows the crop. Falls back to the full-page
    image when no coords are available.
    """
    if not pages:
        return ''

    page_dir = DOCS_PAGES_DIR / issue_slug
    coords = _load_coords(issue_slug)
    art_coords = coords.get(article_slug, {}) if article_slug else {}

    items = []
    for n in pages:
        full_name = f'page-{n}.jpg'
        page_path = page_dir / full_name
        if not page_path.exists():
            continue

        bbox = art_coords.get(str(n))

        if bbox and article_slug:
            crop_name = f'{article_slug}-p{n}-crop.jpg'
            crop_path = page_dir / crop_name
            if not crop_path.exists():
                _make_crop(page_path, bbox, crop_path)

            if crop_path.exists():
                rel = f'{R2_PAGES_URL}/pages/{issue_slug}/{crop_name}'
                full_rel = f'{R2_PAGES_URL}/pages/{issue_slug}/{full_name}'
                caption = f'Page {n} scan &mdash; <a href="{full_rel}" target="_blank" style="color:#8a7355;">view full page</a>'
                items.append(
                    f'<div class="scan-page">'
                    f'<a href="{full_rel}" target="_blank" title="Open full page">'
                    f'<img src="{rel}" alt="Page {n} — article scan" loading="lazy" style="display:block;width:100%;border:1px solid #c9b870;">'
                    f'</a>'
                    f'<div class="scan-page-caption">{caption}</div>'
                    f'</div>'
                )
                continue

        rel = f'{R2_PAGES_URL}/pages/{issue_slug}/{full_name}'
        caption = f'Page {n} &mdash; click to enlarge'
        items.append(
            f'<div class="scan-page">'
            f'<a href="{rel}" target="_blank" title="Open full resolution">'
            f'<img src="{rel}" alt="Page {n}" loading="lazy" style="display:block;width:100%;">'
            f'</a>'
            f'<div class="scan-page-caption">{caption}</div>'
            f'</div>'
        )

    if not items:
        return ''

    pages_html = '\n'.join(items)
    return f'''
    <div class="scan-viewer">
      <div class="scan-viewer-label">Original Newsletter Pages</div>
      <div class="scan-pages">
        {pages_html}
      </div>
    </div>'''


def render_article_page(meta: dict, html_body: str, filename: str,
                         prev_article=None, next_article=None) -> str:
    """Individual article page: 50/50 scan+text split, breadcrumb, prev/next nav."""
    title = html_escape(meta.get('title', 'Article'))
    author = meta.get('author')
    section = meta.get('section')
    pages = meta.get('pages', [])
    issue_date = get_issue_date(meta)
    issue_slug = make_issue_slug(issue_date)
    article_slug = filename.replace('.md', '')

    byline_parts = []
    if author: byline_parts.append(f'By {html_escape(author)}')
    if pages: byline_parts.append(page_display(pages))
    byline_html = ' &bull; '.join(byline_parts)

    section_badge = f'<div class="article-section-badge">{html_escape(section)}</div>' if section else ''
    byline_block = f'<p class="article-byline">{byline_html}</p>' if byline_html else ''

    scan_panel = get_scan_panel_html(issue_slug, pages, article_slug=article_slug)

    breadcrumb = (
        f'<nav class="breadcrumb" aria-label="Breadcrumb">'
        f'<a href="../index.html">Informatics</a>'
        f'<span class="breadcrumb-sep">&rsaquo;</span>'
        f'<a href="../issues/{issue_slug}.html">{html_escape(issue_date)}</a>'
        f'<span class="breadcrumb-sep">&rsaquo;</span>'
        f'<span>{title}</span>'
        f'</nav>'
    )

    nav_links = []
    if prev_article:
        prev_title = html_escape(prev_article[0].get('title', 'Previous'))
        nav_links.append(
            f'<a class="article-nav-link prev" href="{prev_article[1]}">'
            f'<span class="article-nav-dir">&larr; Previous</span>'
            f'<span class="article-nav-title">{prev_title}</span>'
            f'</a>'
        )
    if next_article:
        next_title = html_escape(next_article[0].get('title', 'Next'))
        nav_links.append(
            f'<a class="article-nav-link next" href="{next_article[1]}">'
            f'<span class="article-nav-dir">Next &rarr;</span>'
            f'<span class="article-nav-title">{next_title}</span>'
            f'</a>'
        )
    article_nav = (
        f'<nav class="article-nav" aria-label="Article navigation">{"".join(nav_links)}</nav>'
        if nav_links else ''
    )

    body = f"""
  <div class="article-container" id="main-content">
    {scan_panel}
    <div class="text-panel">
      <div class="text-panel-inner">
        {breadcrumb}
        <div class="article-header">
          {section_badge}
          <h1 class="article-title">{title}</h1>
          <hr class="title-rule">
          {byline_block}
          <p class="article-issue-link">
            From <a href="../issues/{issue_slug}.html">{html_escape(issue_date)}</a>
            &nbsp;&bull;&nbsp; <em>Informatics</em>, National Informatics Centre
          </p>
        </div>
        <div class="article-body" id="article-body">
          {html_body}
        </div>
        {article_nav}
        <p class="section-rule">Search the Archive</p>
        {_search_widget_html(depth=1)}
      </div>
    </div>
  </div>"""

    return _base_html(f'{meta.get("title", "Article")} — Informatics {issue_date}', body, depth=1)


# ---------------------------------------------------------------------------
# API exports (Phase 1 of semantic search plan)
# ---------------------------------------------------------------------------

def _body_snippet(body: str, max_chars: int = 500) -> str:
    """Extract plain-text snippet from markdown body, stripping all markers."""
    # Strip image blockquotes, headings, list markers, footnotes
    text = re.sub(r'^> \*\*\[Image\]\*\*.*$', '', body, flags=re.MULTILINE)
    text = re.sub(r'^#+\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\[\^\d+\]:.*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'^[-*\d]+[.)]\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    text = re.sub(r'\*(.+?)\*', r'\1', text)
    text = ' '.join(text.split())
    return text[:max_chars]


def write_api_exports(all_articles: list, sorted_issues: list) -> None:
    """Write docs/api/articles.json and docs/api/issues.json."""
    api_dir = DOCS_DIR / 'api'
    api_dir.mkdir(parents=True, exist_ok=True)

    articles_out = []
    for meta, body, filename in all_articles:
        slug = filename.replace('.md', '')
        issue_date = get_issue_date(meta)
        articles_out.append({
            'slug': slug,
            'title': meta.get('title', ''),
            'issue_date': issue_date,
            'issue_slug': make_issue_slug(issue_date),
            'pages': meta.get('pages', []),
            'author': meta.get('author'),
            'section': meta.get('section'),
            'body_snippet': _body_snippet(body),
            'url': f'/articles/{slug}.html',
        })

    (api_dir / 'articles.json').write_text(
        json.dumps(articles_out, ensure_ascii=False, indent=2), encoding='utf-8'
    )
    print(f'  → api/articles.json  ({len(articles_out)} articles)')

    issues_out = []
    for issue_date, issue_articles in sorted_issues:
        slug = make_issue_slug(issue_date)
        article_slugs = [fn.replace('.md', '') for _, _, fn in issue_articles]
        issues_out.append({
            'issue_slug': slug,
            'issue_date': issue_date,
            'article_count': len(article_slugs),
            'article_slugs': article_slugs,
        })

    (api_dir / 'issues.json').write_text(
        json.dumps(issues_out, ensure_ascii=False, indent=2), encoding='utf-8'
    )
    print(f'  → api/issues.json  ({len(issues_out)} issues)')


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    # Clean stale generated files so old articles don't accumulate in the index
    if DOCS_ARTICLES.exists():
        for f in DOCS_ARTICLES.glob('*.html'):
            f.unlink()
    DOCS_ARTICLES.mkdir(parents=True, exist_ok=True)
    DOCS_ISSUES.mkdir(parents=True, exist_ok=True)

    print('Extracting images from document.md...')
    images = extract_images()
    print(f'  Found {len(images)} images')

    # Load all articles
    all_articles = []
    for md_path in sorted(ARTICLES_DIR.glob('*.md')):
        with open(md_path, encoding='utf-8') as f:
            text = f.read()
        meta, body = parse_frontmatter(text)
        all_articles.append((meta, body, md_path.name))

    print(f'Loaded {len(all_articles)} articles')

    # Group by issue date
    by_issue: dict = defaultdict(list)
    for meta, body, filename in all_articles:
        issue_date = get_issue_date(meta)
        by_issue[issue_date].append((meta, body, filename))

    # Sort issues chronologically
    sorted_issues = sorted(by_issue.items(), key=lambda x: issue_sort_key(x[0]))

    issues_data = []
    total_articles_count = 0

    print('\nGenerating pages...')
    for issue_date, issue_articles in sorted_issues:
        slug = make_issue_slug(issue_date)
        # Sort articles within issue by first page number
        sorted_arts = sorted(issue_articles, key=lambda x: (x[0].get('pages') or [999])[0])

        # Generate article pages with prev/next context from issue order
        for i, (meta, body, filename) in enumerate(sorted_arts):
            html_body = md_to_html(body, images)
            prev_art = None
            next_art = None
            if i > 0:
                prev_meta, _, prev_fn = sorted_arts[i - 1]
                prev_art = (prev_meta, prev_fn.replace('.md', '.html'))
            if i < len(sorted_arts) - 1:
                next_meta, _, next_fn = sorted_arts[i + 1]
                next_art = (next_meta, next_fn.replace('.md', '.html'))
            page_html = render_article_page(meta, html_body, filename, prev_art, next_art)
            out_path = DOCS_ARTICLES / filename.replace('.md', '.html')
            out_path.write_text(page_html, encoding='utf-8')
            print(f'  → articles/{out_path.name}')

        # Generate issue TOC page
        article_metas_files = [(m, fn) for m, _, fn in sorted_arts]
        issue_pages = get_issue_pages(slug)
        issue_html = render_issue_page(issue_date, article_metas_files, page_images=issue_pages)
        out_path = DOCS_ISSUES / f'{slug}.html'
        out_path.write_text(issue_html, encoding='utf-8')
        print(f'  → issues/{slug}.html  ({len(sorted_arts)} articles)')

        issues_data.append({
            'date': issue_date,
            'slug': slug,
            'count': len(sorted_arts),
            'articles': [m for m, _, _ in sorted_arts],
        })
        total_articles_count += len(sorted_arts)

    # Generate main index (issues_data is in chronological order)
    print('\nGenerating index...')
    index_html = render_index(issues_data)
    (DOCS_DIR / 'index.html').write_text(index_html, encoding='utf-8')
    print('  → index.html')

    print('\nGenerating API exports...')
    write_api_exports(all_articles, sorted_issues)

    print(f'\nDone. {total_articles_count} articles across {len(sorted_issues)} issues.')
    print('Then: open docs/index.html')


if __name__ == '__main__':
    main()
