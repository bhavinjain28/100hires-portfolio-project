#!/usr/bin/env python3
"""Fetch YouTube transcripts and save as markdown under research/youtube-transcripts/."""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    NoTranscriptFound,
    TranscriptsDisabled,
    VideoUnavailable,
)

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "research" / "youtube-transcripts"
MANIFEST = ROOT / "research" / "video-manifest.json"


def slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def load_manifest() -> list[dict]:
    with MANIFEST.open(encoding="utf-8") as f:
        return json.load(f)


def fetch_transcript(video_id: str) -> str:
    api = YouTubeTranscriptApi()
    fetched = api.fetch(video_id, languages=["en", "en-US", "en-GB"])
    return " ".join(snippet.text for snippet in fetched.snippets)


def save_transcript(entry: dict, body: str) -> Path:
    author_slug = slugify(entry["author"])
    out_dir = OUTPUT_DIR / author_slug
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{entry['video_id']}.md"
    header = f"""# {entry['title']}

- **Author:** {entry['author']}
- **Video ID:** {entry['video_id']}
- **URL:** https://www.youtube.com/watch?v={entry['video_id']}
- **Published:** {entry.get('published', 'unknown')}
- **Collected:** {datetime.now(timezone.utc).strftime('%Y-%m-%d')}

## Summary

{entry.get('summary', 'No summary provided.')}

## Transcript

"""
    out_path.write_text(header + body, encoding="utf-8")
    return out_path


def main() -> int:
    if not MANIFEST.exists():
        print(f"Manifest not found: {MANIFEST}", file=sys.stderr)
        return 1

    entries = load_manifest()
    if len(sys.argv) > 1:
        authors = {a.lower() for a in sys.argv[1:]}
        entries = [e for e in entries if slugify(e["author"]) in authors or e["author"].lower() in authors]

    ok, failed = 0, 0
    for entry in entries:
        video_id = entry["video_id"]
        try:
            body = fetch_transcript(video_id)
            path = save_transcript(entry, body)
            print(f"OK  {video_id} -> {path.relative_to(ROOT)}")
            ok += 1
        except (TranscriptsDisabled, NoTranscriptFound, VideoUnavailable) as exc:
            print(f"SKIP {video_id} ({entry['author']}): {exc}", file=sys.stderr)
            failed += 1
        except Exception as exc:  # noqa: BLE001
            print(f"ERR  {video_id} ({entry['author']}): {exc}", file=sys.stderr)
            failed += 1

    print(f"\nDone: {ok} saved, {failed} failed")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
