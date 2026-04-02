#!/usr/bin/env python3
"""Fetch YouTube captions as plain text using youtube-transcript-api (no API key).

Usage:
  python fetch_youtube_transcript.py VIDEO_ID > ../youtube-transcripts/slug.txt

Requires: pip install youtube-transcript-api
"""

from __future__ import annotations

import argparse
import sys

from youtube_transcript_api import YouTubeTranscriptApi


def main() -> None:
    parser = argparse.ArgumentParser(description="Print YouTube transcript lines (English first).")
    parser.add_argument("video_id", help="11-character YouTube video ID")
    parser.add_argument(
        "--languages",
        default="en",
        help="Comma-separated language codes, priority order (default: en)",
    )
    args = parser.parse_args()
    langs = tuple(x.strip() for x in args.languages.split(",") if x.strip())
    fetched = YouTubeTranscriptApi().fetch(args.video_id, languages=langs)
    for snippet in fetched:
        sys.stdout.write(snippet.text.replace("\n", " ").strip() + "\n")


if __name__ == "__main__":
    main()
