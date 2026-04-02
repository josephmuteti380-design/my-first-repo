# How this research was collected

## LinkedIn

- **Approach:** Manual capture of specific posts (URL + full text) into `research/linkedin-posts/`, one file per post.  
- **Why not scrape at scale:** Automated scraping often violates LinkedIn’s terms and breaks easily; for coursework/portfolio work, **manual collection with citations** is safer and auditable.  
- **Tip:** When you save a post, include **author, date, canonical post URL, and “Post Content:”** so future-you can trace the source.

## YouTube transcripts

- **Target:** Videos from people who **operate agencies, products, or large programs** (aligned with “practice what they teach”).  
- **Implemented in this repo (2026-04-02):**  
  - Install: `pip install -r research/scripts/requirements.txt` (Python 3.12+).  
  - Fetch plain text: `python research/scripts/fetch_youtube_transcript.py VIDEO_ID > research/youtube-transcripts/<slug>-transcript.txt`  
  - Each video has a **`.md`** index (metadata + how it was fetched) and a **`.txt`** transcript file next to it.  
- **Alternatives:** Supadata or other paid APIs; **`youtube-transcript-api`** is a free path Alex’s brief allows; always respect YouTube ToS / rate limits.  
- **YouTube UI:** Transcript panel → copy (fallback if captions are disabled).

## Podcasts & long audio

- Store show notes links, episode URLs, and your own bullet summary under `research/other/` (or split by host in subfolders if the corpus grows).

## Git hygiene

- Commit after **each batch** (e.g. “Add 3 LinkedIn captures”, “Add Wil Reynolds YouTube notes”) instead of one enormous commit at the end.
