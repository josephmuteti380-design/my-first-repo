# How this research was collected

## LinkedIn

- **Approach:** Manual capture of specific posts (URL + full text) into `research/linkedin-posts/`, one file per post.  
- **Why not scrape at scale:** Automated scraping often violates LinkedIn’s terms and breaks easily; for coursework/portfolio work, **manual collection with citations** is safer and auditable.  
- **Tip:** When you save a post, include **author, date, canonical post URL, and “Post Content:”** so future-you can trace the source.

## YouTube transcripts

- **Target:** Videos from people who **operate agencies, products, or large programs** (aligned with “practice what they teach”).  
- **API / tooling paths:**  
  - **Supadata** or similar transcript APIs (paste URL → JSON/text).  
  - **youtube-transcript-api** (Python, unofficial; use responsibly).  
  - **YouTube UI:** Transcript panel → copy.  
- **This repo:** Some videos include **metadata + sourced summaries** until a full transcript is pasted into the same markdown file.

## Podcasts & long audio

- Store show notes links, episode URLs, and your own bullet summary under `research/other/` (or split by host in subfolders if the corpus grows).

## Git hygiene

- Commit after **each batch** (e.g. “Add 3 LinkedIn captures”, “Add Wil Reynolds YouTube notes”) instead of one enormous commit at the end.
