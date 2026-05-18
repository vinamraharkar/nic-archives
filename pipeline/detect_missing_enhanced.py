#!/usr/bin/env python3
"""
Enhanced targeted detection for articles that previously returned NOT FOUND.

Two-stage approach per article:
  Stage 1: Direct title-anchor search (same as main script)
  Stage 2: Ask Gemini to list ALL headlines on the page, then match by title/body

Saves results directly into the existing coords.json for each issue.

Usage:
    python pipeline/detect_missing_enhanced.py
    python pipeline/detect_missing_enhanced.py --dry-run   # just print what would run
"""

from __future__ import annotations

import json
import os
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

BASE_DIR = Path(__file__).parent.parent
DOCS_PAGES_DIR = BASE_DIR / "docs" / "pages"
ARTICLES_DIR = BASE_DIR / "articles"

MAX_RETRIES = 5

# The 19 articles that permanently failed detection
MISSING = [
    ("october-2020",  "aims-agricultural-information-management-system-october-2020",                                                                          [38]),
    ("april-2005",    "awards-to-nic-officers-on-the-occasion-of-56th-republic-day-celebrations-april-2005",                                                   [24]),
    ("october-2005",  "bcwd-computerization-in-bankura-wb-october-2005",                                                                                       [20]),
    ("july-1997",     "computerized-results-july-1997",                                                                                                        [13]),
    ("october-2019",  "dg-nic-participates-in-ciso-leadership-summit-2019-in-new-delhi-october-2019",                                                          [43]),
    ("october-2020",  "dg-nic-shared-her-insights-on-the-role-of-women-leading-tech-in-the-post-pandemic-world-at-a-virtual-discussion-organised-by-newsx-assocham-october-2020", [42]),
    ("january-2003",  "e-governance-projects-inaugurated-at-distt-fatehgarh-sahib-punjab-january-2003",                                                        [47, 48]),
    ("july-2021",     "esajag-mobile-app-launched-by-district-collector-jaisalmer-rajasthan-july-2021",                                                        [45]),
    ("july-2021",     "hon-ble-chief-minister-assam-reviews-kritagyata-online-pension-sanction-and-payment-tracking-july-2021",                                [41]),
    ("october-2021",  "hon-ble-chief-minister-of-assam-launches-mvahan-learner-license-from-home-applications-october-2021",                                   [46]),
    ("october-2021",  "hon-ble-prime-minister-interacted-with-covid-vaccine-beneficiaries-and-officials-of-hp-through-nic-video-conferencing-services-october-2021", [42]),
    ("july-2021",     "launch-of-cghs-convergence-with-pmjay-scheme-and-rashtriya-arogya-nidhi-and-health-minister-s-discretionary-grants-hmdg-through-national-health-authority-nha-s-it-platforms-july-2021", [41]),
    ("july-2002",     "message-from-director-general-july-2002",                                                                                               [48]),
    ("january-2020",  "nic-honored-with-govinsider-innovation-award-2019-gets-international-recognition-from-unescap-january-2020",                            [48]),
    ("january-2003",  "nic-s-support-during-president-s-thiruvananthapuram-visit-january-2003",                                                                [52, 53]),
    ("january-2006",  "nilamagal-land-records-computerization-inaugurated-at-pondicherry-january-2006",                                                        [24]),
    ("april-2005",    "panch-lekha-web-based-accounting-information-system-for-pris-april-2005",                                                               [20]),
    ("january-2003",  "technology-seminar-on-e-governance-at-orissa-january-2003",                                                                             [49, 50]),
    ("october-2020",  "usa-tops-ai-readiness-index-october-2020",                                                                                              [40]),
]


def parse_article(slug: str) -> dict | None:
    md = ARTICLES_DIR / f"{slug}.md"
    if not md.exists():
        return None
    text = md.read_text(encoding="utf-8")
    m_title = re.search(r'^title:\s*"([^"]+)"', text, re.MULTILINE)
    parts = text.split("---")
    body = parts[2].strip() if len(parts) >= 3 else ""
    body_lines = [l for l in body.splitlines() if l.strip() and not l.startswith("#")][:5]
    body_snippet = " ".join(body_lines)[:250]
    return {
        "slug": slug,
        "title": m_title.group(1) if m_title else slug,
        "body_snippet": body_snippet,
    }


def stage1_direct(client, page_n: int, page_path: Path, article: dict, img_w: int, img_h: int) -> dict | None:
    """Direct headline search — more forceful than the main script."""
    from google.genai import types as gai_types

    title = article["title"]
    snippet = article["body_snippet"]

    prompt = f"""You are analyzing page {page_n} of a scanned NIC Informatics newsletter.
Image dimensions: {img_w} x {img_h} pixels.

Find the article with headline: "{title}"
It may appear in ALL CAPS, mixed case, or with slight OCR variations.
This article may be very small — just a few lines — or a brief news item.
Opening text of the article: "{snippet[:200]}"

IMPORTANT: Even if the article is only 2-3 lines tall, return its bounding box.
Include any photo or caption that belongs to this article.

Return ONLY the tightest bounding box in PIXEL coordinates ({img_w}x{img_h}):
{{"y_start": <int>, "y_end": <int>, "x_start": <int>, "x_end": <int>}}

If this exact article is NOT visible on this page, return:
{{"not_found": true}}

Return ONLY valid JSON, nothing else."""

    img_bytes = page_path.read_bytes()
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash-lite",
                contents=[
                    gai_types.Part.from_bytes(data=img_bytes, mime_type="image/jpeg"),
                    prompt,
                ],
            )
            return _parse_bbox(response.text.strip(), img_w, img_h)
        except Exception as e:
            wait = 60 if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e) else 2 ** attempt
            if attempt < MAX_RETRIES:
                print(f"      [s1 retry {attempt}] {e} — wait {wait}s")
                time.sleep(wait)
            else:
                print(f"      [s1 failed] {e}")
    return None


def stage2_scan_all(client, page_n: int, page_path: Path, article: dict, img_w: int, img_h: int) -> dict | None:
    """
    Ask Gemini to list ALL article headlines on the page with bounding boxes,
    then pick the best match by title similarity.
    """
    from google.genai import types as gai_types

    title = article["title"].lower()
    snippet = article["body_snippet"]

    prompt = f"""You are analyzing page {page_n} of a scanned NIC Informatics newsletter.
Image dimensions: {img_w} x {img_h} pixels.

List EVERY article headline visible on this page, with its bounding box in pixel coordinates.
Include even very small news items, brief notices, and 1-paragraph articles.

Return a JSON array — one entry per article:
[
  {{"headline": "...", "y_start": <int>, "y_end": <int>, "x_start": <int>, "x_end": <int>}},
  ...
]

Be exhaustive — include ALL text blocks that look like article headers or news items.
Return ONLY valid JSON, nothing else."""

    img_bytes = page_path.read_bytes()
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash-lite",
                contents=[
                    gai_types.Part.from_bytes(data=img_bytes, mime_type="image/jpeg"),
                    prompt,
                ],
            )
            raw = response.text.strip()
            raw = re.sub(r"^```(?:json)?\s*", "", raw)
            raw = re.sub(r"\s*```$", "", raw)
            items = json.loads(raw)
            if not isinstance(items, list):
                raise ValueError("Expected a JSON array")

            # Find best match by title keyword overlap
            best = None
            best_score = 0
            title_words = set(re.findall(r'\w+', title.lower()))
            snippet_words = set(re.findall(r'\w+', snippet.lower()))

            for item in items:
                h = item.get("headline", "").lower()
                h_words = set(re.findall(r'\w+', h))
                # Score: intersection of title words + snippet words
                score = len(h_words & title_words) + 0.3 * len(h_words & snippet_words)
                if score > best_score:
                    best_score = score
                    best = item

            if best and best_score >= 2:  # At least 2 title words match
                print(f"      [s2 matched] '{best['headline'][:60]}' score={best_score:.1f}")
                return _parse_bbox_from_item(best, img_w, img_h)
            else:
                print(f"      [s2] No confident match (best score={best_score:.1f})")
                return None

        except Exception as e:
            wait = 60 if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e) else 2 ** attempt
            if attempt < MAX_RETRIES:
                print(f"      [s2 retry {attempt}] {e} — wait {wait}s")
                time.sleep(wait)
            else:
                print(f"      [s2 failed] {e}")
    return None


def stage3_body_anchor(client, page_n: int, page_path: Path, article: dict, img_w: int, img_h: int) -> dict | None:
    """
    Last resort: ask Gemini to find the article using ONLY its body text as anchor,
    ignoring the headline.
    """
    from google.genai import types as gai_types

    snippet = article["body_snippet"][:300]
    title = article["title"]

    prompt = f"""You are analyzing page {page_n} of a scanned NIC Informatics newsletter.
Image dimensions: {img_w} x {img_h} pixels.

Find the text block on this page that contains or begins with this text:
"{snippet}"

The section may have a headline like "{title}" above it, or may begin mid-paragraph.
This could be a very small news item or brief notice — just 1-4 lines of text.

Return the bounding box of the ENTIRE article/news item in pixel coordinates ({img_w}x{img_h}):
{{"y_start": <int>, "y_end": <int>, "x_start": <int>, "x_end": <int>}}

If this text is NOT visible on this page, return:
{{"not_found": true}}

Return ONLY valid JSON, nothing else."""

    img_bytes = page_path.read_bytes()
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash-lite",
                contents=[
                    gai_types.Part.from_bytes(data=img_bytes, mime_type="image/jpeg"),
                    prompt,
                ],
            )
            return _parse_bbox(response.text.strip(), img_w, img_h)
        except Exception as e:
            wait = 60 if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e) else 2 ** attempt
            if attempt < MAX_RETRIES:
                print(f"      [s3 retry {attempt}] {e} — wait {wait}s")
                time.sleep(wait)
            else:
                print(f"      [s3 failed] {e}")
    return None


def _parse_bbox(raw: str, img_w: int, img_h: int) -> dict | None:
    raw = re.sub(r"^```(?:json)?\s*", "", raw)
    raw = re.sub(r"\s*```$", "", raw)
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError:
        return None
    if parsed.get("not_found"):
        return None
    return _parse_bbox_from_item(parsed, img_w, img_h)


def _parse_bbox_from_item(item: dict, img_w: int, img_h: int) -> dict | None:
    try:
        x0 = max(0, int(item["x_start"]))
        y0 = max(0, int(item["y_start"]))
        x1 = min(img_w, int(item["x_end"]))
        y1 = min(img_h, int(item["y_end"]))
    except (KeyError, ValueError, TypeError):
        return None
    if y1 <= y0 or x1 <= x0:
        return None
    return {"y_start": y0, "y_end": y1, "x_start": x0, "x_end": x1,
            "img_width": img_w, "img_height": img_h}


def detect_article_on_page(
    client, issue_slug: str, slug: str, page_n: int, article: dict
) -> dict | None:
    from PIL import Image as PILImage

    page_path = DOCS_PAGES_DIR / issue_slug / f"page-{page_n}.jpg"
    if not page_path.exists():
        print(f"    page-{page_n}.jpg not found, skipping")
        return None

    img = PILImage.open(page_path)
    img_w, img_h = img.size

    print(f"    Page {page_n} ({img_w}x{img_h}):")

    # Stage 1: Direct title search
    print(f"      Stage 1: direct title match...")
    bbox = stage1_direct(client, page_n, page_path, article, img_w, img_h)
    if bbox:
        print(f"        ✅ Found: y={bbox['y_start']}→{bbox['y_end']} x={bbox['x_start']}→{bbox['x_end']}")
        return bbox
    print(f"        ✗ Not found")
    time.sleep(1)

    # Stage 2: Scan all headlines
    print(f"      Stage 2: scan all headlines...")
    bbox = stage2_scan_all(client, page_n, page_path, article, img_w, img_h)
    if bbox:
        print(f"        ✅ Found: y={bbox['y_start']}→{bbox['y_end']} x={bbox['x_start']}→{bbox['x_end']}")
        return bbox
    print(f"        ✗ Not found")
    time.sleep(1)

    # Stage 3: Body text anchor
    if article.get("body_snippet"):
        print(f"      Stage 3: body text anchor...")
        bbox = stage3_body_anchor(client, page_n, page_path, article, img_w, img_h)
        if bbox:
            print(f"        ✅ Found: y={bbox['y_start']}→{bbox['y_end']} x={bbox['x_start']}→{bbox['x_end']}")
            return bbox
        print(f"        ✗ Not found")

    return None


def run(dry_run: bool = False) -> None:
    from dotenv import load_dotenv
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("ERROR: GEMINI_API_KEY not set")
        sys.exit(1)

    from google import genai as gai
    client = gai.Client(api_key=api_key)

    total_found = 0
    total_tried = 0

    for issue_slug, slug, pages in MISSING:
        article = parse_article(slug)
        if not article:
            print(f"⚠️  Article file not found: {slug}")
            continue

        coords_path = DOCS_PAGES_DIR / issue_slug / "coords.json"
        if coords_path.exists():
            coords = json.loads(coords_path.read_text())
        else:
            coords = {}

        print(f"\n{'='*70}")
        print(f"Article: {article['title'][:70]}")
        print(f"  Issue: {issue_slug}  |  Pages: {pages}")

        if dry_run:
            continue

        found_any = False
        for page_n in pages:
            total_tried += 1
            bbox = detect_article_on_page(client, issue_slug, slug, page_n, article)
            if bbox:
                coords.setdefault(slug, {})[str(page_n)] = bbox
                coords_path.write_text(json.dumps(coords, indent=2))
                print(f"      💾 Saved to coords.json")
                total_found += 1
                found_any = True
            time.sleep(0.5)

        if not found_any:
            print(f"  ❌ STILL NOT FOUND on any page")

    print(f"\n{'='*70}")
    print(f"Results: {total_found}/{total_tried} page-entries found")
    if not dry_run:
        print("Next: python3 generate_site.py && npx pagefind --site docs/")


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true", help="Print articles without calling API")
    args = p.parse_args()
    run(dry_run=args.dry_run)
