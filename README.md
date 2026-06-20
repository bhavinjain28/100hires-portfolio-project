# Cursor IDE Setup

## Tools Installed
- Cursor IDE
- Claude Code extension (Anthropic)
- Codex extension (OpenAI)

## Steps Completed
1. Installed Cursor IDE on Windows
2. Installed the Claude Code extension
3. Installed the Codex extension
4. Created this public GitHub repository
5. Cloned the repository, and opened it in Cursor
6. Wrote this README
7. Committed and pushed to GitHub

## Issues Encountered
Got a warning about cloning an empty repository. This was expected, since the GitHub repo wasn't initialized with a README at creation time.

---

# 100Hires Portfolio Project — Cold Outreach Research

Research repository for building a **Cold Outreach Pipeline for B2B SaaS** playbook.

## Topic choice

**Cold outreach pipeline for B2B SaaS** was selected because:

- Practitioners publish tactical, step-by-step content on YouTube (ideal for transcript API collection)
- The expert pool is deep and differentiated—operators, copy specialists, deliverability engineers, and signal-based GTM builders
- The topic maps cleanly to a structured playbook: ICP → list building → copy → sequences → deliverability → metrics
- Material is stable (unlike fast-moving AI SEO topics) but still current for 2025–2026

## What was collected

| Asset | Count | Location |
|-------|-------|----------|
| Experts | 10 | [research/sources.md](research/sources.md) |
| YouTube transcripts | 13 videos | [research/youtube-transcripts/](research/youtube-transcripts/) |
| LinkedIn posts | 10 authors | [research/linkedin-posts/](research/linkedin-posts/) |
| Other materials | 1 summary | [research/other/](research/other/) |

Transcripts were fetched programmatically via `youtube-transcript-api` using [scripts/fetch_transcripts.py](scripts/fetch_transcripts.py) and [research/video-manifest.json](research/video-manifest.json).

## Why these experts

We prioritized **practitioners who run outbound systems**, not generic sales motivation accounts. The 10 experts cover the full pipeline:

| Expert | Angle |
|--------|-------|
| Eric Nowoslawski | Agency operator; 1M+ emails/month; Clay + AI list building |
| Jordan Crawford | Signal-based GTM; PQS/PVP frameworks |
| Will Allred | Copy psychology; Lavender email coaching product |
| Jason Bay | Messaging Matrix; trained Shopify, Gong, Rippling |
| Josh Braun | 4T framework; skeptical-prospect copy |
| Nils Schneider | Deliverability infrastructure; Instantly.ai CEO |
| Armand Farrokh | 3x3 rule; scaled Pave to $13M ARR |
| Morgan J Ingram | Multi-channel; LinkedIn video outbound |
| Kyle Coleman | Enterprise omni-channel; 12yr cold email practitioner |
| Nick Cegelski | Enterprise AE; cold email teardowns |

Armand Farrokh and Nick Cegelski both co-host 30 Minutes to President's Club but cover distinct angles: Armand brings the operator/VP Sales perspective (built pipeline from $0 to $13M ARR at Pave), while Nick brings enterprise AE deal context and email teardowns. Including both is deliberate — they represent the two dominant lenses on cold email from the same practitioner community.

See [research/sources.md](research/sources.md) for links, collection dates, and annotations.

## Repository structure

```text
research/
├── sources.md                 # Expert list with links and rationale
├── video-manifest.json      # YouTube videos for transcript script
├── youtube-transcripts/       # Transcripts by author slug
├── linkedin-posts/          # Posts organized by author
└── other/                   # Supplementary materials
scripts/
└── fetch_transcripts.py     # Fetch and save YouTube transcripts
```

## Tools used

- Cursor IDE with Claude Code and Codex extensions
- Python + [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api) for transcript collection
- Manual curation of LinkedIn posts (public posts, collected 2026-06-20)

## Setup & usage

To re-run or extend transcript collection:

```bash
pip install -r requirements.txt

# Fetch transcripts for all authors in the manifest
python scripts/fetch_transcripts.py

# Fetch for a single author only
python scripts/fetch_transcripts.py "Eric Nowoslawski"
python scripts/fetch_transcripts.py "Jordan Crawford"
```

Transcripts are written to `research/youtube-transcripts/<author-slug>/<video-id>.md`. The manifest at `research/video-manifest.json` controls which videos are fetched.

