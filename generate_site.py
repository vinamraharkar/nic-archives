#!/usr/bin/env python3
"""Generate a static HTML site from NIC Archives 1992 newsletter articles."""

import json
import os
import re
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARTICLES_DIR = os.path.join(BASE_DIR, 'articles')
METADATA_DIR = os.path.join(BASE_DIR, 'metadata')
DOCS_DIR = os.path.join(BASE_DIR, 'docs')
DOCS_ARTICLES_DIR = os.path.join(DOCS_DIR, 'articles')

CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }

body {
    background: #1a0f07;
    color: #1e1408;
    font-family: Georgia, "Times New Roman", serif;
    font-size: 17px;
    line-height: 1.7;
    min-height: 100vh;
    padding: 3rem 1.5rem 5rem;
}

/* ── Page card (cream vellum sheet on dark leather) ── */
.page {
    max-width: 720px;
    margin: 0 auto;
    padding: 3.5rem 4rem;
    background: #f7f0d8;
    box-shadow: 0 6px 60px rgba(0,0,0,0.75), 0 2px 8px rgba(0,0,0,0.5);
}

/* ── Double-border masthead frame ── */
.book-frame {
    border: 3px solid #b8892a;
    padding: 4px;
    margin-bottom: 2.5rem;
}
.book-frame-inner {
    border: 1px solid #b8892a;
    padding: 2.5rem 2rem;
    text-align: center;
}
.masthead-title {
    font-size: 2.6rem;
    font-weight: 900;
    letter-spacing: 0.25em;
    color: #7a1f1f;
    text-transform: uppercase;
    line-height: 1;
    white-space: nowrap;
}
.masthead-ornament {
    color: #b8892a;
    font-size: 1.1rem;
    margin: 0.6rem 0;
    letter-spacing: 0.4em;
}
.masthead-sub {
    font-size: 0.95rem;
    font-style: italic;
    color: #8a7355;
    margin-top: 0.2rem;
}
.masthead-meta {
    font-size: 0.82rem;
    letter-spacing: 0.08em;
    color: #8a7355;
    margin-top: 0.3rem;
}

/* ── PDF link ── */
.pdf-link {
    display: inline-block;
    margin: 0.5rem 0 0;
    padding: 0.5rem 1.4rem;
    border: 1px solid #b8892a;
    color: #7a1f1f;
    text-decoration: none;
    font-size: 0.85rem;
    letter-spacing: 0.06em;
}
.pdf-link:hover { background: #ede6c0; }

/* ── Table of Contents heading ── */
.toc-heading {
    font-size: 0.72rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    font-variant: small-caps;
    color: #1e1408;
    border-bottom: 2px solid #b8892a;
    padding-bottom: 0.35rem;
    margin-bottom: 0.5rem;
}

/* ── TOC list ── */
.toc {
    list-style: none;
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
}
.toc-section-label {
    font-size: 0.65rem;
    letter-spacing: 0.12em;
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
    font-size: 1.02rem;
}
.toc a:hover { color: #7a1f1f; text-decoration: underline; }
.toc-meta {
    font-size: 0.78rem;
    color: #8a7355;
    font-style: italic;
    margin-top: 0.3rem;
}

/* ── Back link (sits on dark background above page card) ── */
.back-wrap {
    max-width: 720px;
    margin: 0 auto 1rem;
}
.back-link {
    display: inline-block;
    color: #c9a96e;
    text-decoration: none;
    font-size: 0.85rem;
    letter-spacing: 0.04em;
}
.back-link:hover { color: #f7f0d8; text-decoration: underline; }

/* ── Article page header ── */
.article-header {
    padding-bottom: 1rem;
    margin-bottom: 1.8rem;
}
.article-section-badge {
    font-size: 0.68rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #7a1f1f;
    border: 1px solid #7a1f1f;
    padding: 0.1rem 0.35rem;
    display: inline-block;
    margin-bottom: 0.6rem;
}
h1.article-title {
    font-size: 2.1rem;
    font-weight: 800;
    line-height: 1.25;
    color: #7a1f1f;
    margin-bottom: 0.5rem;
}
hr.title-rule {
    border: none;
    border-top: 1px solid #b8892a;
    margin: 0.7rem 0;
}
.article-byline {
    font-size: 0.85rem;
    color: #8a7355;
    font-style: italic;
}

/* ── Article body ── */
.article-body p {
    margin-bottom: 1rem;
    text-align: justify;
    hyphens: auto;
}

/* Drop cap on first paragraph */
.article-body p.first-para::first-letter {
    font-size: 3.8em;
    float: left;
    line-height: 0.82;
    color: #7a1f1f;
    font-weight: 900;
    margin: 0.05em 0.12em 0 0;
}

/* Section headings with gold ornamental prefix */
.article-body h3.section-heading {
    font-size: 0.9rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #7a1f1f;
    margin: 2rem 0 0.7rem;
}
.article-body h3.section-heading::before {
    content: '\2014 ';
    color: #b8892a;
}

/* Ornamental section divider */
.ornament {
    text-align: center;
    color: #b8892a;
    font-size: 1rem;
    letter-spacing: 0.5em;
    margin: 1.5rem 0;
}

/* ── Figure / image ── */
figure.article-image {
    margin: 1.5rem 0;
    border: 1px solid #b8892a;
    background: #ede6c0;
    padding: 0.75rem;
}
figure.article-image img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 0 auto 0.6rem;
}
figure.article-image figcaption {
    font-size: 0.8rem;
    color: #8a7355;
    font-style: italic;
    line-height: 1.5;
}

/* ── Footnotes ── */
.footnote {
    font-size: 0.82rem;
    color: #8a7355;
    border-top: 1px solid #b8892a;
    padding-top: 0.6rem;
    margin-top: 2rem;
    font-style: italic;
}
.footnote sup {
    font-size: 0.7rem;
    vertical-align: super;
    margin-right: 0.2rem;
}
"""

ARTICLE_ORDER = [
    'cover-role-of-nic-in-the-election-process.md',   # p.1
    'misc.md',                                          # p.2 left col (editorial)
    'financial-management-informatics-project.md',      # p.2 right col
    'around-the-nic-world.md',                          # p.3 left col
    'all-set-for-tax-computerization.md',               # p.3 right col top
    'keeping-monkeys-at-bay.md',                        # p.3 right col bottom
    'nics-election-experience-a-rich-harvest.md',       # pp.4–5
    'products.md',                                      # p.6
    'projects.md',                                      # p.7
    'the-lakshadweeps-not-so-far-away.md',              # p.8
]


def roman(n):
    """Convert integer to Roman numeral string (supports 1–10)."""
    vals = [(10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    result = ''
    for v, s in vals:
        while n >= v:
            result += s
            n -= v
    return result


def extract_images():
    """Returns dict mapping normalized description text -> base64 string."""
    doc_path = os.path.join(BASE_DIR, 'document.md')
    with open(doc_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into page blocks on '\n---\n'
    pages = content.split('\n---\n')

    result = {}
    for page_idx, page_block in enumerate(pages):
        page_num = page_idx + 1

        # Find all base64 image data URIs on this page
        b64_list = re.findall(
            r'!\[Image\]\(data:image/jpeg;base64,([^)]+)\)',
            page_block
        )
        if not b64_list:
            continue

        meta_path = os.path.join(METADATA_DIR, f'page_00{page_num}.json')
        with open(meta_path, 'r', encoding='utf-8') as f:
            meta = json.load(f)

        image_blocks = [b for b in meta['blocks'] if b['layout_tag'] == 'image']
        image_blocks.sort(key=lambda b: b['reading_order'])

        for b64, block in zip(b64_list, image_blocks):
            normalized = re.sub(r'\s+', ' ', block['text']).strip()
            result[normalized] = b64

    return result


def parse_frontmatter(text):
    """Parse YAML-like frontmatter. Returns (meta_dict, body_text)."""
    if not text.startswith('---\n'):
        return {}, text

    parts = text.split('---\n', 2)
    if len(parts) < 3:
        return {}, text

    fm_text = parts[1]
    body = parts[2]
    meta = {}

    for line in fm_text.splitlines():
        m = re.match(r'^(\w+):\s*(.+)$', line)
        if not m:
            continue
        key = m.group(1)
        val = m.group(2).strip()
        if val == 'null':
            meta[key] = None
        elif val.startswith('"') and val.endswith('"'):
            meta[key] = val[1:-1]
        elif val.startswith('[') and val.endswith(']'):
            inner = val[1:-1]
            meta[key] = [int(x.strip()) for x in inner.split(',') if x.strip().isdigit()]
        else:
            try:
                meta[key] = int(val)
            except ValueError:
                meta[key] = val

    return meta, body


def html_escape(text):
    return (text
            .replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
            .replace('"', '&quot;'))


def inline_md(text):
    """Convert inline markdown (**bold**, *italic*) to HTML."""
    # Strip LaTeX-style subscript artifacts like $_{20}$
    text = re.sub(r'\$_\{[^}]+\}\$', '', text)
    # Bold: **text**
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # Italic: *text* (not ** and not inside bold)
    text = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<em>\1</em>', text)
    return text


def md_to_html(body, images):
    """Convert article markdown body to HTML string."""
    lines = body.splitlines()
    html_parts = []
    pending_para = []
    first_para_emitted = False

    # State for collecting multi-line image descriptions
    in_image = False
    image_desc_lines = []

    def flush_para():
        nonlocal first_para_emitted
        if pending_para:
            text = ' '.join(pending_para).strip()
            if text:
                if not first_para_emitted:
                    html_parts.append(f'<p class="first-para">{inline_md(html_escape(text))}</p>')
                    first_para_emitted = True
                else:
                    html_parts.append(f'<p>{inline_md(html_escape(text))}</p>')
            pending_para.clear()

    def render_image(desc_text):
        """Render a figure element for the given description."""
        normalized = re.sub(r'\s+', ' ', desc_text).strip()
        b64 = images.get(normalized, '')
        escaped_desc = html_escape(normalized)
        if b64:
            html_parts.append(
                f'<figure class="article-image">'
                f'<img src="data:image/jpeg;base64,{b64}" alt="{escaped_desc}">'
                f'<figcaption>{escaped_desc}</figcaption>'
                f'</figure>'
            )
        else:
            # No image data found; render as text callout
            html_parts.append(
                f'<figure class="article-image">'
                f'<figcaption>{escaped_desc}</figcaption>'
                f'</figure>'
            )

    for line in lines:
        # ── Collecting multi-line image description ──
        if in_image:
            stripped = line.rstrip()
            if stripped.endswith('*'):
                # End of description
                image_desc_lines.append(stripped.rstrip('*'))
                render_image(' '.join(image_desc_lines))
                in_image = False
                image_desc_lines = []
            else:
                image_desc_lines.append(stripped)
            continue

        # ── Skip ## article title ──
        if re.match(r'^## ', line):
            continue

        # ── ### Subheading ──
        m = re.match(r'^### (.+)$', line)
        if m:
            flush_para()
            heading = html_escape(m.group(1).strip())
            html_parts.append(f'<h3 class="section-heading">{heading}</h3>')
            continue

        # ── Image blockquote: > **[Image]** *desc* ──
        m = re.match(r'^> \*\*\[Image\]\*\* \*(.+)$', line)
        if m:
            flush_para()
            rest = m.group(1)
            if rest.rstrip().endswith('*'):
                # Single-line description
                render_image(rest.rstrip().rstrip('*'))
            else:
                # Multi-line: start collecting
                in_image = True
                image_desc_lines = [rest]
            continue

        # ── Footnote: [^N]: text ──
        m = re.match(r'^\[\^(\d+)\]: (.+)$', line)
        if m:
            flush_para()
            num = m.group(1)
            text = m.group(2)
            html_parts.append(
                f'<div class="footnote"><sup>{num}</sup> {inline_md(html_escape(text))}</div>'
            )
            continue

        # ── Blank line → flush paragraph ──
        if line.strip() == '':
            flush_para()
            continue

        # ── Normal text ──
        pending_para.append(line.strip())

    flush_para()
    return '\n'.join(html_parts)


def page_display(pages):
    """Format page list for display: [4, 5] → 'pp. 4–5', [3] → 'p. 3'"""
    if not pages:
        return ''
    if len(pages) == 1:
        return f'p. {pages[0]}'
    return f'pp. {pages[0]}–{pages[-1]}'


def render_article_page(meta, html_body, filename):
    """Return full self-contained HTML page string for an article."""
    title = html_escape(meta.get('title', 'Article'))
    author = meta.get('author')
    section = meta.get('section')
    pages = meta.get('pages', [])

    byline_parts = []
    if author:
        byline_parts.append(f'By {html_escape(author)}')
    if pages:
        byline_parts.append(page_display(pages))
    byline_html = ' &bull; '.join(byline_parts)

    section_badge = ''
    if section:
        section_badge = f'<div class="article-section-badge">{html_escape(section)}</div>'

    byline_block = ''
    if byline_html:
        byline_block = f'<p class="article-byline">{byline_html}</p>'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Informatics, Vol. 1 No. 2</title>
<style>{CSS}</style>
</head>
<body>
  <div class="back-wrap">
    <a class="back-link" href="../index.html">&larr; Back to Issue</a>
  </div>
  <div class="page">
    <div class="article-header">
      {section_badge}
      <h1 class="article-title">{title}</h1>
      <hr class="title-rule">
      {byline_block}
    </div>
    <div class="article-body">
      {html_body}
    </div>
  </div>
</body>
</html>"""


def render_index(articles):
    """Return full HTML index page string."""
    items_html = []
    for idx, (meta, filename) in enumerate(articles, start=1):
        title = html_escape(meta.get('title', 'Untitled'))
        author = meta.get('author')
        section = meta.get('section')
        pages = meta.get('pages', [])
        stem = filename.replace('.md', '.html')

        badge = ''
        if section:
            badge = f'<span class="toc-section-label">{html_escape(section)}</span>'

        meta_parts = []
        if author:
            meta_parts.append(f'By {html_escape(author)}')
        if pages:
            meta_parts.append(page_display(pages))
        meta_line = ''
        if meta_parts:
            meta_line = f'<div class="toc-meta">{" &bull; ".join(meta_parts)}</div>'

        items_html.append(
            f'<li>'
            f'<span class="toc-num">{roman(idx)}.</span>'
            f'<div>'
            f'{badge}'
            f'<a href="articles/{stem}">{title}</a>'
            f'{meta_line}'
            f'</div>'
            f'</li>'
        )

    items = '\n'.join(items_html)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Informatics — Vol. 1, No. 2 (October 1992)</title>
<style>{CSS}</style>
</head>
<body>
  <div class="page">
    <div class="book-frame">
      <div class="book-frame-inner">
        <div class="masthead-title">Informatics</div>
        <div class="masthead-ornament">&#10022; &#10022; &#10022;</div>
        <div class="masthead-sub">Quarterly Newsletter</div>
        <div class="masthead-meta">Vol.&nbsp;1, No.&nbsp;2 &nbsp;&bull;&nbsp; October 1992 &nbsp;&bull;&nbsp; National Informatics Centre</div>
        <div style="margin-top:1.2rem;">
          <a class="pdf-link" href="NIC Archives.pdf">&#10022;&nbsp; Download Original PDF</a>
        </div>
      </div>
    </div>

    <p class="toc-heading">Table of Contents</p>
    <ul class="toc">
      {items}
    </ul>
  </div>
</body>
</html>"""


def main():
    # Create output directories
    os.makedirs(DOCS_ARTICLES_DIR, exist_ok=True)

    # Copy PDF
    pdf_src = os.path.join(BASE_DIR, 'NIC Archives.pdf')
    pdf_dst = os.path.join(DOCS_DIR, 'NIC Archives.pdf')
    if os.path.exists(pdf_src):
        shutil.copy2(pdf_src, pdf_dst)
        print(f'Copied PDF → docs/NIC Archives.pdf')

    # Extract images from document.md
    print('Extracting images from document.md...')
    images = extract_images()
    print(f'  Found {len(images)} images')

    # Process articles
    articles_meta = []
    article_files = []

    # Use defined order, falling back to any remaining files
    md_files = set(os.listdir(ARTICLES_DIR))
    ordered = [f for f in ARTICLE_ORDER if f in md_files]
    remaining = sorted(md_files - set(ARTICLE_ORDER))
    all_files = ordered + remaining

    for filename in all_files:
        if not filename.endswith('.md'):
            continue
        filepath = os.path.join(ARTICLES_DIR, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()

        meta, body = parse_frontmatter(text)
        html_body = md_to_html(body, images)
        page_html = render_article_page(meta, html_body, filename)

        out_filename = filename.replace('.md', '.html')
        out_path = os.path.join(DOCS_ARTICLES_DIR, out_filename)
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(page_html)

        article_files.append(filename)
        articles_meta.append((meta, filename))
        title = meta.get('title', filename)
        print(f'  → articles/{out_filename}  ({title})')

    # Write index
    index_html = render_index(articles_meta)
    index_path = os.path.join(DOCS_DIR, 'index.html')
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_html)
    print(f'Written: docs/index.html')
    print(f'\nDone. Open docs/index.html in your browser.')


if __name__ == '__main__':
    main()
