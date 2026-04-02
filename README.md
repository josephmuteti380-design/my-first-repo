## AI-powered SEO content production - research corpus

This repo is a structured **research corpus** on *AI-powered SEO content production*: practitioners who run agencies, products, or large client programs and publish from that experience (not armchair commentary).

### What was collected

| Location | Contents |
|----------|-----------|
| [`research/sources.md`](research/sources.md) | **Ten experts** with links, collection dates, and short annotations. |
| [`research/linkedin-posts/`](research/linkedin-posts/) | Captured **LinkedIn posts** (manual export: URL + full text), by author/date. |
| [`research/youtube-transcripts/`](research/youtube-transcripts/) | **YouTube videos** - per-video `.md` index + **`.txt` transcripts** (Python + [`youtube-transcript-api`](https://pypi.org/project/youtube-transcript-api/)). |
| [`research/other/`](research/other/) | **Collection methodology** and rubric notes. |

### Why these experts

The list mixes **operators** (agency founders, platform builders) with **analysts who still touch live programs** (large-site SEO, quality updates, generative search). Together they cover:

- Using AI for **decisions** (topics, intent, structure) vs. spammy volume  
- **Citations and visibility** in AI-mediated answers (GEO / AI Overviews context)  
- **Quality bars** (helpful content, E-E-A-T) when drafts are AI-assisted  
- **Product and engineering** views (tools that shape how SEO content is produced)

### Tooling notes

- **LinkedIn:** Captured manually for compliance and stability; filenames follow `author-slug-topic-YYYY-MM-DD.md`.  
- **YouTube transcripts:** Captions pulled programmatically with **`youtube-transcript-api`** (script + `requirements.txt` under [`research/scripts/`](research/scripts/)); committed `.txt` artifacts live next to each video index.

## Rubric alignment (signal over volume)

This corpus is curated for **high-signal practitioners** and **playbook potential**.
See [`research/other/evaluation-alignment.md`](research/other/evaluation-alignment.md).

## YouTube transcript API pipeline

- Dependency pin: [`research/scripts/requirements.txt`](research/scripts/requirements.txt)
- Fetch script: [`research/scripts/fetch_youtube_transcript.py`](research/scripts/fetch_youtube_transcript.py)
- Transcript artifacts (examples):
  - [`research/youtube-transcripts/nathan-gotch-9wuHUDm4-WE-transcript.txt`](research/youtube-transcripts/nathan-gotch-9wuHUDm4-WE-transcript.txt)
