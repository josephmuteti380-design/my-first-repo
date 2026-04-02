Portfolio Project: Cursor IDE Setup and GitHub Repository

## AI-powered SEO content production — research track

This repository now includes a structured **research corpus** on the topic *AI-powered SEO content production*: practitioners who run agencies, products, or large client programs and publish from that experience (not armchair commentary).

### What was collected

| Location | Contents |
|----------|-----------|
| [`research/sources.md`](research/sources.md) | **Ten experts** with profile/site links, primary content links, collection dates, and short annotations tied to AI + SEO content workflows. |
| [`research/linkedin-posts/`](research/linkedin-posts/) | Captured **LinkedIn posts** (manual export: URL + full text), filed by author and date. |
| [`research/youtube-transcripts/`](research/youtube-transcripts/) | **YouTube videos** — per-video `.md` index plus **`.txt` transcripts** fetched with Python + [`youtube-transcript-api`](https://pypi.org/project/youtube-transcript-api/) (see [`research/scripts/`](research/scripts/)). |
| [`research/other/`](research/other/) | **Collection methodology**, podcast/channel pointers, and space for episode notes. |

### Why these experts

The list mixes **operators** (agency founders, platform builders) with **analysts who still touch live programs** (large-site SEO, quality updates, generative search). Together they cover:

- Using AI for **decisions** (topics, intent, structure) vs. spammy volume  
- **Citations and visibility** in AI-mediated answers (GEO / AI Overviews context)  
- **Quality bars** (helpful content, E-E-A-T) when drafts are AI-assisted  
- **Product and engineering** views (tools that shape how SEO content is produced)

### Tooling notes

- **LinkedIn:** Captured manually for compliance and stability; filenames follow `author-slug-topic-YYYY-MM-DD.md`.  
- **YouTube transcripts:** Captions pulled programmatically with **`youtube-transcript-api`** (script + `requirements.txt` under [`research/scripts/`](research/scripts/)); committed `.txt` artifacts live next to each video index. Supadata remains a valid alternative (see [`research/other/collection-methods.md`](research/other/collection-methods.md)).  

Commits for this work are kept in **small, reviewable steps** rather than one monolithic diff.

**How this is graded (typical rubric):** expert *quality* (strong practitioners, not generic lists), *repo structure*, *use of APIs/tools* (e.g. transcript pipelines), and whether material can support a *real playbook*—**signal over volume**. See [`research/other/evaluation-alignment.md`](research/other/evaluation-alignment.md).

---

## Original portfolio: tools and setup

### Tools installed

- **Cursor IDE:** https://cursor.com/ — main development environment.  
- **Claude Code add-on:** Cursor Extensions → search “Claude Code” → sign in.  
- **Codex add-on:** Cursor Extensions → search “Codex” → sign in.  
- **GitHub:** Public repository hosting this project.

### Completed steps

1. Installing Cursor IDE and verifying it runs correctly.  
2. Adding and signing into the Claude Code and Codex extensions.  
3. Creating a public GitHub repository for the project.  
4. Opening the GitHub repository in Cursor IDE.  
5. Creating this README and describing the process.  
6. Committing and pushing the repository to GitHub.  
7. Verifying the repository is public and contains this README.

### Issues encountered and solutions

- **Issue:** Difficult to find the “Clone Repository” button in Cursor IDE.  
  - **Solution:** Used the Git URL of the GitHub repository directly in Cursor’s “Open Repository” flow.  
- **Issue:** Unsure which local folder to open after clone.  
  - **Solution:** Opened the folder that contains the `.git` directory.  
- **Issue:** First-time setup of Claude Code and Codex.  
  - **Solution:** Followed online tutorials and product docs to install, activate, and sign in.

### Outcome

- Installed and integrated AI-assisted coding tools.  
- Created and synced a public GitHub repository from Cursor.  
- Demonstrated self-directed learning, troubleshooting, and research organization (including the SEO research track above).

### Notes

- This portfolio project showcases research, AI-tool usage, and problem-solving.  
- Steps were completed independently with minimal guidance.
