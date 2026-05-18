"""Shared utilities for the NIC Archives pipeline."""

from __future__ import annotations

import json
import re
import threading
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
ARCHIVES_DIR = BASE_DIR / "Archives"
RAW_TEXT_DIR = BASE_DIR / "raw_text"
ARTICLES_DIR = BASE_DIR / "articles"
CLASSIFIED_PATH = BASE_DIR / "classified.json"
ERRORS_PATH = BASE_DIR / "pipeline" / "errors.json"


# ── Slug helpers ──────────────────────────────────────────────────────────────

def filename_to_slug(filename: str) -> str:
    """Convert a PDF filename to a URL-safe slug.

    "Apr-1995.pdf" → "apr-1995"
    "April-2003.pdf" → "april-2003"
    """
    stem = Path(filename).stem
    slug = stem.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    return slug.strip("-")


def slug_to_raw_text_path(slug: str) -> Path:
    return RAW_TEXT_DIR / f"{slug}.json"


# ── classified.json ───────────────────────────────────────────────────────────

def load_classified() -> list[dict]:
    if not CLASSIFIED_PATH.exists():
        return []
    with open(CLASSIFIED_PATH, encoding="utf-8") as f:
        return json.load(f)


def save_classified(entries: list[dict]) -> None:
    with open(CLASSIFIED_PATH, "w", encoding="utf-8") as f:
        json.dump(entries, f, indent=2)


# ── Error logging ─────────────────────────────────────────────────────────────

_error_log_lock = threading.Lock()

def log_error(filename: str, step: str, message: str) -> None:
    """Append error to pipeline/errors.json without aborting the run. Thread-safe."""
    with _error_log_lock:
        errors: list[dict] = []
        if ERRORS_PATH.exists():
            with open(ERRORS_PATH, encoding="utf-8") as f:
                errors = json.load(f)
        errors.append({"filename": filename, "step": step, "error": message})
        with open(ERRORS_PATH, "w", encoding="utf-8") as f:
            json.dump(errors, f, indent=2)
    print(f"  [ERROR] {filename} ({step}): {message}")


# ── Article frontmatter ───────────────────────────────────────────────────────

def make_frontmatter(
    title: str,
    issue_date: str,
    pages: list[int],
    author: str | None = None,
    section: str | None = None,
) -> str:
    pages_yaml = "[" + ", ".join(str(p) for p in pages) + "]"
    author_yaml = f'"{author}"' if author else "null"
    section_yaml = f'"{section}"' if section else "null"
    return (
        "---\n"
        f'title: "{title}"\n'
        'publication: "Informatics"\n'
        f'issue_date: "{issue_date}"\n'
        f"pages: {pages_yaml}\n"
        f"author: {author_yaml}\n"
        f"section: {section_yaml}\n"
        "---\n\n"
    )


def make_article_slug(title: str, issue_date: str) -> str:
    """Generate a unique slug for an article file.

    "NIC's Election Experience" + "April 1995" → "nics-election-experience-april-1995"
    Truncated to 180 chars to stay within macOS 255-char filename limit (leaving room for .md).
    """
    combined = f"{title} {issue_date}"
    slug = combined.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = slug.strip("-")
    return slug[:180]
