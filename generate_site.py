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
    background: #f4efe4;
    color: #1c1208;
    font-family: Georgia, "Times New Roman", serif;
    font-size: 17px;
    line-height: 1.7;
}

.container {
    max-width: 700px;
    margin: 0 auto;
    padding: 2rem 1.5rem 4rem;
}

/* ── Masthead ── */
.masthead {
    border-bottom: 3px double #c4a882;
    padding-bottom: 1.2rem;
    margin-bottom: 1.5rem;
    text-align: center;
}
.masthead-title {
    font-size: 3rem;
    font-weight: 900;
    letter-spacing: 0.08em;
    color: #8b1a1a;
    text-transform: uppercase;
    line-height: 1;
}
.masthead-sub {
    font-size: 0.9rem;
    letter-spacing: 0.12em;
    color: #6b5a3e;
    margin-top: 0.3rem;
    text-transform: uppercase;
}

/* ── PDF link ── */
.pdf-link {
    display: inline-block;
    margin: 1rem 0 1.5rem;
    padding: 0.45rem 1rem;
    border: 1px solid #c4a882;
    border-radius: 2px;
    color: #8b1a1a;
    text-decoration: none;
    font-size: 0.85rem;
    letter-spacing: 0.05em;
}
.pdf-link:hover { background: #ede6d6; }

/* ── Article list ── */
.section-label {
    font-size: 0.7rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #8b1a1a;
    border: 1px solid #8b1a1a;
    padding: 0.15rem 0.4rem;
    margin-right: 0.5rem;
    vertical-align: middle;
    white-space: nowrap;
}

.article-list {
    list-style: none;
    border-top: 1px solid #c4a882;
}
.article-list li {
    border-bottom: 1px solid #c4a882;
    padding: 0.85rem 0;
}
.article-list a {
    color: #1c1208;
    text-decoration: none;
    font-size: 1.05rem;
}
.article-list a:hover { color: #8b1a1a; text-decoration: underline; }
.article-meta {
    font-size: 0.8rem;
    color: #7a6a52;
    margin-top: 0.2rem;
}

.articles-heading {
    font-size: 0.75rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #6b5a3e;
    margin-bottom: 0.5rem;
    margin-top: 0.5rem;
}

/* ── Back link ── */
.back-link {
    display: inline-block;
    color: #8b1a1a;
    text-decoration: none;
    font-size: 0.85rem;
    margin-bottom: 1.5rem;
    letter-spacing: 0.03em;
}
.back-link:hover { text-decoration: underline; }

/* ── Article page ── */
.article-header {
    border-bottom: 2px solid #c4a882;
    padding-bottom: 1rem;
    margin-bottom: 1.8rem;
}
.article-section-badge {
    font-size: 0.68rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #8b1a1a;
    border: 1px solid #8b1a1a;
    padding: 0.1rem 0.35rem;
    display: inline-block;
    margin-bottom: 0.6rem;
}
h1.article-title {
    font-size: 2rem;
    font-weight: 800;
    line-height: 1.25;
    color: #1c1208;
    margin-bottom: 0.5rem;
}
.article-byline {
    font-size: 0.85rem;
    color: #7a6a52;
    font-style: italic;
}

/* ── Article body ── */
.article-body p {
    margin-bottom: 1rem;
    text-align: justify;
    hyphens: auto;
}
.article-body h3.section-heading {
    font-size: 1rem;
    font-weight: 700;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    color: #8b1a1a;
    margin: 1.8rem 0 0.6rem;
    border-top: 1px solid #c4a882;
    padding-top: 0.8rem;
}

/* ── Figure / image ── */
figure.article-image {
    margin: 1.5rem 0;
    border: 1px solid #c4a882;
    background: #ede6d6;
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
    color: #6b5a3e;
    font-style: italic;
    line-height: 1.5;
}

/* ── Footnotes ── */
.footnote {
    font-size: 0.82rem;
    color: #6b5a3e;
    border-top: 1px solid #c4a882;
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
    'cover-role-of-nic-in-the-election-process.md',
    'nics-election-experience-a-rich-harvest.md',
    'financial-management-informatics-project.md',
    'the-lakshadweeps-not-so-far-away.md',
    'all-set-for-tax-computerization.md',
    'around-the-nic-world.md',
    'keeping-monkeys-at-bay.md',
    'products.md',
    'projects.md',
    'misc.md',
]


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

    # State for collecting multi-line image descriptions
    in_image = False
    image_desc_lines = []

    def flush_para():
        if pending_para:
            text = ' '.join(pending_para).strip()
            if text:
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
<div class="container">
  <a class="back-link" href="../index.html">&larr; Back to Issue</a>
  <div class="article-header">
    {section_badge}
    <h1 class="article-title">{title}</h1>
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
    for meta, filename in articles:
        title = html_escape(meta.get('title', 'Untitled'))
        author = meta.get('author')
        section = meta.get('section')
        pages = meta.get('pages', [])
        stem = filename.replace('.md', '.html')

        badge = ''
        if section:
            badge = f'<span class="section-label">{html_escape(section)}</span>'

        meta_parts = []
        if author:
            meta_parts.append(f'By {html_escape(author)}')
        if pages:
            meta_parts.append(page_display(pages))
        meta_line = ''
        if meta_parts:
            meta_line = f'<div class="article-meta">{" &bull; ".join(meta_parts)}</div>'

        items_html.append(
            f'<li>'
            f'{badge}<a href="articles/{stem}">{title}</a>'
            f'{meta_line}'
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
<div class="container">
  <div class="masthead">
    <div class="masthead-title">Informatics</div>
    <div class="masthead-sub">Vol.&nbsp;1, No.&nbsp;2 &nbsp;&bull;&nbsp; October 1992 &nbsp;&bull;&nbsp; National Informatics Centre</div>
  </div>

  <div style="text-align:center;">
    <a class="pdf-link" href="NIC Archives.pdf">&#128196; Download Original PDF</a>
  </div>

  <p class="articles-heading">Articles in this issue</p>
  <ul class="article-list">
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
