#!/usr/bin/env python3
"""
Split NIC Archives into 10 article .md files using metadata JSON as primary source.
Metadata provides authoritative reading_order, coordinates, and image descriptions.

Root cause of prior bugs: document.md does NOT follow metadata reading_order for
multi-column pages. This script ignores document.md entirely and reads blocks
directly from per-page JSON metadata files.
"""
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))

# ── Article definitions ──────────────────────────────────────────────────────
# constraint keys:
#   min_reading_order, max_reading_order — inclusive bounds on block.reading_order
#   min_x1, max_x1                       — inclusive bounds on block.coordinates.x1
ARTICLES = [
    {
        "file":    "cover-role-of-nic-in-the-election-process.md",
        "title":   "Role of NIC in the Election Process",
        "section": None, "author": None, "pages": [1],
        "constraint": {},
    },
    {
        "file":    "misc.md",
        "title":   "Miscellaneous",
        "section": None, "author": None, "pages": [2],
        "constraint": {"max_reading_order": 19},
    },
    {
        "file":    "financial-management-informatics-project.md",
        "title":   "Financial Management Informatics Project",
        "section": None, "author": "Rubaiyat Ali", "pages": [2],
        "constraint": {"min_reading_order": 20},
    },
    {
        "file":    "around-the-nic-world.md",
        "title":   "Around the NIC World",
        "section": None, "author": None, "pages": [3],
        "constraint": {"max_x1": 974},
    },
    {
        "file":    "all-set-for-tax-computerization.md",
        "title":   "All Set for Tax Computerization",
        "section": None, "author": None, "pages": [3],
        "constraint": {"min_x1": 975, "max_reading_order": 17},
    },
    {
        "file":    "keeping-monkeys-at-bay.md",
        "title":   "Keeping Monkeys at Bay",
        "section": None, "author": None, "pages": [3],
        "constraint": {"min_x1": 975, "min_reading_order": 18},
    },
    {
        "file":    "nics-election-experience-a-rich-harvest.md",
        "title":   "NIC's Election Experience: A Rich Harvest",
        "section": "Cover Story", "author": None, "pages": [4, 5],
        "constraint": {},
    },
    {
        "file":    "products.md",
        "title":   "Products",
        "section": "Products", "author": None, "pages": [6],
        "constraint": {},
    },
    {
        "file":    "projects.md",
        "title":   "Projects",
        "section": "Projects", "author": None, "pages": [7],
        "constraint": {},
    },
    {
        "file":    "the-lakshadweeps-not-so-far-away.md",
        "title":   "The Lakshadweeps: Not So Far Away",
        "section": "In the Limelight", "author": None, "pages": [8],
        "constraint": {},
    },
]

# layout_tags to skip entirely (navigation chrome, not article content)
SKIP_TAGS = {"header", "footer", "page-number"}

# layout_tags that carry article content
CONTENT_TAGS = {"headline", "section-title", "paragraph", "image", "footnote"}

# Texts that are page/section labels, not article content — suppress
SUPPRESS_TEXTS = {
    "COVER STORY",
    "ELECTION RESULTS NETWORK",
    "IN THE LIMELIGHT",
    "PRODUCTS",
    "PROJECTS",
    "Informatics NICNET",   # page 1 cover masthead title
}

# Article title headers — skip in body (title already prepended as ## at top)
TITLE_HEADERS = {
    "Financial Management Informatics Project",
    "KEEPING MONKEYS AT BAY",
    "NIC's Election Experience : A Rich Harvest",
    "THE LAKSHADWEEPS : NOT SO FAR AWAY",
}

# Section-title block that is a visual sidebar blurb, not a real heading
DEMOTE_TO_BODY_PREFIX = "The Analytics and Modelling"


# ── Helpers ──────────────────────────────────────────────────────────────────

def load_page(page_num):
    path = os.path.join(BASE, f"metadata/page_{page_num:03d}.json")
    with open(path) as f:
        return json.load(f)


def passes_constraint(block, constraint):
    ro = block["reading_order"]
    x1 = block["coordinates"]["x1"]
    if "min_reading_order" in constraint and ro < constraint["min_reading_order"]:
        return False
    if "max_reading_order" in constraint and ro > constraint["max_reading_order"]:
        return False
    if "min_x1" in constraint and x1 < constraint["min_x1"]:
        return False
    if "max_x1" in constraint and x1 > constraint["max_x1"]:
        return False
    return True


def format_block(block):
    tag  = block["layout_tag"]
    text = block["text"].strip()

    if tag in SKIP_TAGS:
        return ""
    if tag not in CONTENT_TAGS:
        return ""
    if text in SUPPRESS_TEXTS:
        return ""
    if text in TITLE_HEADERS:
        return ""

    if tag == "image":
        return f"\n> **[Image]** *{text}*\n\n"

    if tag == "footnote":
        return f"\n[^1]: {text}\n\n"

    if tag in ("headline", "section-title"):
        if text.startswith(DEMOTE_TO_BODY_PREFIX):
            return text + "\n\n"
        return f"\n### {text}\n\n"

    # paragraph
    return text + "\n\n"


def frontmatter(art):
    pages_yaml  = "[" + ", ".join(str(p) for p in art["pages"]) + "]"
    author_yaml = f'"{art["author"]}"' if art["author"] else "null"
    sect_yaml   = f'"{art["section"]}"' if art["section"] else "null"
    return (
        "---\n"
        f'title: "{art["title"]}"\n'
        'publication: "Informatics"\n'
        "volume: 1\n"
        "issue: 2\n"
        'date: "October 1992"\n'
        f"pages: {pages_yaml}\n"
        f"author: {author_yaml}\n"
        f"section: {sect_yaml}\n"
        "---\n\n"
    )


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    out_dir = os.path.join(BASE, "articles")
    os.makedirs(out_dir, exist_ok=True)

    for art in ARTICLES:
        blocks = []
        for page_num in art["pages"]:
            data = load_page(page_num)
            for block in sorted(data["blocks"], key=lambda b: b["reading_order"]):
                if not passes_constraint(block, art["constraint"]):
                    continue
                blocks.append(block)

        body = f"## {art['title']}\n\n"
        for block in blocks:
            body += format_block(block)

        content = frontmatter(art) + body
        dest = os.path.join(out_dir, art["file"])
        with open(dest, "w") as f:
            f.write(content)
        print(f"  {art['file']}  ({content.count(chr(10))} lines)")

    print("\nVerifying…")
    _verify(out_dir)
    print("All checks passed.")


def _verify(out_dir):
    def read(name):
        return open(os.path.join(out_dir, name)).read()

    files = sorted(os.listdir(out_dir))
    assert len(files) == 10, f"Expected 10 files, got {len(files)}"

    # 1. Monkey image must be in monkey article, not tax article
    monkey = read("keeping-monkeys-at-bay.md")
    tax    = read("all-set-for-tax-computerization.md")
    assert "> **[Image]**" in monkey, "monkey article missing image block"
    assert "> **[Image]**" not in tax, "tax article wrongly contains image block"

    # 2. Monkey footnote must be in monkey article, not around-the-nic-world
    around = read("around-the-nic-world.md")
    assert "[^1]:" not in around, "around-the-nic-world wrongly contains footnote"
    assert "[^1]:" in monkey, "monkey article missing footnote"

    # 3. Editorial content in misc, not financial-management
    misc = read("misc.md")
    fm   = read("financial-management-informatics-project.md")
    assert "EDITOR" in misc or "Informatics has been" in misc or \
           "INFORMATICS has been" in misc or "Rubaiyat Ali" in misc, \
        "misc.md missing editorial content"
    assert "EDITOR'S NOTE" not in fm, "financial-management wrongly contains EDITOR'S NOTE"

    # 4. Globe image in around-the-nic-world
    assert "> **[Image]**" in around, "around-the-nic-world missing globe image"

    # 5. No base64 strings in any file
    for fname in files:
        text = read(fname)
        assert "data:image/jpeg;base64," not in text, \
            f"base64 still present in {fname}"

    # 6. No ## headers in body except the article title ##
    for fname in files:
        text   = read(fname)
        body   = text.split("---\n\n", 1)[-1]
        title  = "## " + next(
            art["title"] for art in ARTICLES if art["file"] == fname
        )
        for line in body.splitlines():
            if line.startswith("## ") and line.strip() != title:
                raise AssertionError(
                    f"Unexpected ## header in {fname}: {line!r}"
                )

    # 7. Each file has valid YAML frontmatter
    for fname in files:
        text = read(fname)
        assert text.startswith("---\n"), f"{fname} missing frontmatter"


if __name__ == "__main__":
    main()
