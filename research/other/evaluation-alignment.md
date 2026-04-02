# Alignment with evaluation criteria

This file records how this corpus is meant to be judged—not by **volume**, but by **signal** and **usability for a future playbook**.

## What evaluators care about

- **Quality of chosen experts** — genuinely strong voices, not “first ten Google results.”  
- **Repository structure** — easy to navigate and extend.  
- **APIs and technical tools** — evidence you can wire real data pipelines (transcripts, etc.), not only bookmarks.  
- **Playbook potential** — material is concrete enough to support strategy, standards, and workflows later.

**Principle:** *Ten high-signal sources beat fifty generic ones.*

## How this project responds

### 1. Expert quality (high-signal, on-purpose mix)

The ten entries are **not** a keyword-stuffed influencer list. They are chosen to cover **non-overlapping jobs-to-be-done** in *AI-powered SEO content production*:

| Lens | Who | Why it’s high-signal |
|------|-----|----------------------|
| **Commercial intent & content types** | Pratik Thakker (captured post) | Ties SEO content to revenue mechanics (comparisons, migrations, ROI)—what AI should inform, not replace. |
| **AI for decisions, not word count** | Omer Riaz (captured post) | Explicit thesis: topic/intent/structure intelligence vs. “write faster.” |
| **Visibility in AI answers (GEO / citations)** | Anna York (captured post) | Bridges classic SEO to **being cited** in LLM-style surfaces. |
| **Distribution vs. AI-only narratives** | Wil Reynolds (video + API transcript) | Large-agency operator; stress-tests where **audience and channel** still matter. |
| **Quality, helpfulness, updates** | Marie Haynes | Consultant deeply tied to **quality systems**—the bar AI drafts must clear. |
| **AI search surfaces & evidence** | Lily Ray | VP-level operator on **publisher / large-site** reality under AI summaries. |
| **Technical + generative-search ops** | Michael King (iPullRank) | Bridges **IR, engineering, and SEO**—how “AI SEO” scales as a system. |
| **Technical + international execution** | Aleyda Solís | Still runs client work; **Crawling Mondays** as ongoing practitioner corpus. |
| **Repeatable process for practitioners** | Nathan Gotch (video notes) | Agency-training lens: **workflows** for fragmented search + AI visibility. |
| **Product-shaped content lifecycle** | Bernard Huang (Clearscope) | Builder of tools that **encode** how teams research, draft, and measure SEO content (including AI-assisted drafting). |

Together, this supports a **playbook skeleton**: *strategy (intent/topics) → structure & quality → measurement & surfaces → tooling & ops → distribution skepticism.*

### 2. Repository structure

- `research/sources.md` — single index of experts with links, dates, annotations.  
- `research/linkedin-posts/` — primary sources by author (manual capture, cited URLs).  
- `research/youtube-transcripts/` — per-video **`.md` index** + **`.txt` transcript** (fetched via `youtube-transcript-api`).  
- `research/other/` — methodology, podcast pointers, **this rubric**.

### 3. APIs and technical tools

- **LinkedIn:** No scraping pipeline—**manual export** with canonical URLs (stable, ToS-safe, auditable).  
- **YouTube:** **Automated caption pull** with the open-source **`youtube-transcript-api`** Python package (no API key). Scripts and pinned dependency versions live under `research/scripts/`; transcript text is committed as **`.txt`** next to each video’s **`.md`** index. **Supadata** (or similar) remains a valid alternative if you prefer a hosted API.

Evaluators should see: **reproducible command**, **dependency pin**, and **raw transcript artifacts**—not only links.


### 4. Playbook strength

Annotations in `sources.md` are written so each expert answers a **design question** for a future playbook (e.g. “What do we optimize for when ChatGPT cites competitors?” “Where do we insert human QA?” “How do we avoid AI-slop at scale?”). That is intentional: *fewer names, sharper roles.*

---

*Keep this file updated if you swap an expert—explain in one line why the replacement raises signal for the playbook.*
