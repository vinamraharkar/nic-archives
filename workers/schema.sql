-- New schema: metadata only. Vectors live in Cloudflare Vectorize.
-- Run: wrangler d1 execute nic-archives --remote --file=schema.sql

CREATE TABLE IF NOT EXISTS articles (
  slug        TEXT PRIMARY KEY,
  title       TEXT NOT NULL,
  issue_date  TEXT NOT NULL,
  issue_slug  TEXT NOT NULL,
  url         TEXT NOT NULL
);
