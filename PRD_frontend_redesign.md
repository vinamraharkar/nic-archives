# PRD: NIC Archives Frontend Redesign
**Status:** Approved for implementation
**Date:** 2026-05-17
**Decided via:** Grill-me session (12 questions)

---

## 1. Product Vision

Transform the NIC Archives from a cramped 820px book-in-a-box into a full-width, desktop-first archive that feels like a serious research tool — with the visual identity of a historic newspaper, not a web page trying to look like a book.

**Primary user:** A researcher (academic, journalist, policy analyst) who arrives via search or a direct link. They want to find an article, read it, and verify it against the original scan. Desktop is the primary surface.

**Secondary experience:** A curious browser who wants to flip through a specific issue to see what was happening in Indian e-governance in, say, April 1995. This is a delight feature, not the primary flow.

---

## 2. What Changes (and What Stays)

### Changes
- Remove the 820px centered `.page` box — content goes edge-to-edge
- New newspaper nameplate masthead (elaborate, historic) on homepage
- Slim fixed navbar on all pages
- Article pages: 50/50 split (full-page scan left, article text right)
- Issue TOC pages: full-width redesign
- Fix search: rebuild Pagefind index + fix search icon overlap
- Homepage: full-width issue card grid replacing the current box layout

### Stays the same
- Color palette: parchment (#f7f0d8), dark brown (#1a0f07), gold (#b8892a), deep red (#7a1f1f)
- Fonts: EB Garamond (headings), Crimson Text (body)
- Drop cap on first paragraph
- Article metadata (section badge, byline, issue link)
- Pagefind for search (no backend needed)
- Static HTML/CSS/JS — no framework

---

## 3. Page Specifications

### 3.1 Global: Slim Navbar (all pages)

**Layout:** Fixed top bar, 48px tall, full-width, `#1a0f07` background with a 1px gold (`#b8892a`) bottom border.

**Left:** "INFORMATICS ARCHIVE" in small-caps, gold, EB Garamond — links to homepage.
**Right:** Search icon (SVG magnifying glass) — clicking opens search on the current page or navigates to homepage with search focused.

**Behaviour:** Sticky/fixed. All page content has `padding-top: 48px` to not hide behind it. The navbar does NOT contain the full newspaper nameplate — that only appears on the homepage.

---

### 3.2 Homepage (Index Page)

**Current:** Masthead → orientation text → search → issue thumbnail strip → TOC list — all inside an 820px box.

**New layout (top to bottom):**

#### A. Newspaper Nameplate Masthead
Full-width section below the slim navbar. Designed like a historic newspaper front page nameplate:
- Decorative horizontal rules (thick-thin) above and below the title
- "INFORMATICS" in large (5–6rem) EB Garamond, uppercase, heavy letter-spacing, deep red (#7a1f1f)
- Volume/issue/date line in small-caps beneath the title (e.g., "Established 1989 · National Informatics Centre, Government of India")
- Left and right of the title: small metadata columns in 0.75rem — publication number, issue date of most recent issue, "Est. 1989"
- Parchment (#f7f0d8) background — no box, no shadow, just the typography filling the width
- A thin gold ornamental rule as the bottom border of the masthead section

#### B. Search Bar
Centered below the masthead. ~600px wide input on desktop.
- Placeholder: "Search 30 years of NIC Informatics…"
- Uses Pagefind UI (already wired up)
- Fix the search icon overlap bug before launch

#### C. Orientation Blurb
One short paragraph (currently `.archive-about`) explaining what this archive is.
Keep the content, drop the bordered box styling — make it plain text, centered, max-width 700px, italic, 0.95rem Crimson Text.

#### D. Issues Grid
Full-width grid of issue cards. 4 columns on desktop (≥1200px), 2 columns on tablet, 1 column on mobile.

**Each issue card contains:**
- Cover page scan thumbnail (the first page JPG, sized consistently — ~220px tall)
- Issue date (e.g., "October 1992") in EB Garamond
- Article count (e.g., "12 articles")
- Hover: subtle gold border + lift shadow

Cards link to the issue's TOC page.

---

### 3.3 Issue TOC Page

**Current:** Same 820px box with masthead + page thumbnail strip + TOC list.

**New layout:**

#### A. Issue Masthead
Full-width, same nameplate style as homepage but smaller (3rem title). Shows the specific issue date prominently.

#### B. Page Thumbnail Strip
Keep the horizontal scrollable strip of all page thumbnails. Full-width, no box. Thumbnails click to open the full-page JPG.

#### C. TOC List
Full-width below the strip. Two-column layout on desktop (article entries side by side). Each entry: section badge + title + author + page number. Links to article page.

---

### 3.4 Article Page

**Current:** Dark scan sidebar (360px) + text panel (remaining width) inside a 1200px container.

**New layout:** True 50/50 split, full-viewport-width, no container box.

#### Left Panel — Original Scan (50% viewport width)
- Background: parchment (#f7f0d8) — NOT dark. Both panels share the same background so the page feels unified.
- Displays the **full-page JPG** of each page the article spans (not column crops)
- Image rendered at ~56% of its 1242px native width → sharp, no upscaling blur
- If article spans 2 pages: both full-page images stacked vertically with a thin gold divider between them
- Above the image: small label "Original scan · Page N" (0.75rem, gold, uppercase)
- Below the image: "Open full resolution ↗" link to the raw JPG
- **No highlight overlay** — the article's position on the page is not marked programmatically. The article title in the right panel is the user's reference point.

#### Right Panel — Article Text (50% viewport width)
- Same as current text panel content: section badge, article title (h1), byline, body text
- Drop cap on first paragraph
- `max-width: 680px` within the panel for readability (text doesn't stretch to 700px)
- Padding: 3rem on all sides

#### Mobile (≤768px)
- Left panel (scan) stacks above right panel (text) — full viewport width each
- Scan image scales to 100% width

#### Navigation
- Slim navbar (global) provides "INFORMATICS ARCHIVE" home link
- Below the article title: breadcrumb — `INFORMATICS › April 1995 › [Article Title]`
- At bottom of article: Previous article / Next article links within the same issue

---

## 4. Search Fix (Immediate Bug)

Two separate issues:

**Bug 1 — No results:** Pagefind index is stale. After every `python3 generate_site.py` run, must run:
```bash
npx pagefind --site docs/
```
This needs to be in the standard build workflow.

**Bug 2 — Search icon overlap:** CSS conflict in Pagefind UI widget. The search input text overlaps the magnifying glass icon. Fix by inspecting the rendered Pagefind widget and adding appropriate padding-left to the input.

**Search results display (current launch):** Text-only cards — title, section badge, issue date, 2-line excerpt. No thumbnails.

**Future upgrade:** Once all 120 issues are processed and crop quality verified, add column crop thumbnails to search result cards (requires `data-pagefind-meta="thumbnail"` on article pages + custom Pagefind UI JS).

---

## 5. What Is NOT in Scope

- Full issue page viewer / flipbook (separate future feature)
- Click-on-scan-to-select-article (coordinate accuracy not reliable enough)
- Search autocomplete dropdown (Pagefind's as-you-type results serve this purpose)
- React or any frontend framework
- Backend of any kind
- Dark mode
- Article thumbnails in search results (deferred to post-120-issue scale)

---

## 6. Implementation Phases

### Phase 1 — Bug fixes (do first, unblocks search testing)
1. Run `npx pagefind --site docs/` — fix no-results
2. Fix search icon overlap in CSS

### Phase 2 — Global layout (affects all pages)
3. Remove the 820px `.page` box — switch to full-width layout
4. Build slim fixed navbar
5. Add `padding-top: 48px` to all page bodies

### Phase 3 — Homepage
6. Redesign masthead as newspaper nameplate (full-width)
7. Restyle orientation blurb (plain text, no bordered box)
8. Build full-width issue card grid (replace thumbnail strip + TOC)

### Phase 4 — Article pages
9. Replace dark sidebar + text panel with 50/50 full-page split
10. Add breadcrumb navigation
11. Add previous/next article links

### Phase 5 — Issue TOC pages
12. Full-width redesign matching the new layout system
13. Two-column TOC list on desktop

### Phase 6 — Polish
14. Responsive behaviour (tablet 2-col grid, mobile stack)
15. Hover states, transitions, focus rings on new components

---

## 7. Open Questions (Resolved)
All 12 grilling questions resolved. No blockers to implementation.

---

## 8. Technical Notes for Implementation

- All changes live in `generate_site.py` — the CSS, HTML templates, and Python rendering logic
- Full-page scan images already exist in `docs/pages/{issue_slug}/page-N.jpg`
- Article frontmatter already contains `pages: [N, M]` — use this to know which full-page JPGs to show in the left panel
- The `_make_column_crop()` function stays in the codebase (used for future search thumbnails) but is no longer called for the article page left panel
- Pagefind wiring (`data-pagefind-body`, `data-pagefind-meta`, `data-pagefind-filter`) stays unchanged on article pages
- Max content width within full-width layout: article text panel uses `max-width: 680px` for readability; issue card grid uses CSS grid with `auto-fill` and `minmax(220px, 1fr)`
