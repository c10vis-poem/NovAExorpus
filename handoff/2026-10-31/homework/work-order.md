# Wiki-admin work order

2026-10-30 · v1. **This replaces** "Wiki-admin intake plan v2" and "Wiki-admin trim and compile plan", and the wiki-admin section of plugin-recommendations-2026-10-30.md.

This document is self-contained. Hand any homework packet (section 7) to an outside agent with no other context.

---

## 1. What wiki-admin is

Wiki-admin takes in **thousands of raw documents** from Google, the web, repos and media. It turns them into an **llm-wiki file structure** (Markdown pages, folder guides, a search index). Then it pulls **skills, tools and artifacts** out of what it has ingested.

It ships as **one compiled plugin** built from trimmed parts of about 44 existing plugins. The original plugins are never edited.

## 2. What is out of scope: the memory-store pipeline

These belong to a separate pipeline, not to wiki-admin:

- Self-hosted MCP servers
- Supabase
- Reverse-engineering OB1 and Mem0
- code-review-graph, graphify, notebooklm-py
- Own SHA-256 content addressing, own Next.js app
- Several SQLite databases (episodic and semantic memory, agent recall, repo status, codebase data)

Wiki-admin only produces the handoff described in section 3.

## 3. The output contract (the handoff to the memory-store pipeline)

Every ingested file gets a line in `manifest.jsonl`:

```json
{"sha256":"<hex of raw source bytes>","source":"gdrive|web|repo|gmail|media|local","source_ref":"<url or id>","raw_path":"raw/<sha256>.<ext>","md_path":"wiki/<section>/<slug>.md","converted_by":"<part name>","ingested_at":"<ISO8601>","bytes":0,"status":"ok|failed|quarantined","extracted":["skill:<name>","tool:<name>","artifact:<name>"]}
```

- Raw files are stored by their hash, so a file that shows up twice is stored once.
- A page is never deleted. It is marked ~~superseded~~ and moved to `wiki/_archive/`.
- Every wiki page has frontmatter with `sources:` listing the sha256 of each source file.

## 4. The pipeline

```
INTAKE ─► CONVERT ─► SIZE-GATE ─► FAN-OUT ─► WIKI + SEARCH ─► EXTRACT ─► CHECK ─► manifest.jsonl
```

| Stage | What it does | Main parts |
| --- | --- | --- |
| Intake | Pulls in Google files, web pages and media | Google connectors, gdrive-to-markdown, google-multi-account, firecrawl, apify, watch-video, local-whisper |
| Convert | Turns everything into Markdown | pdf, docx, xlsx and pptx account skills, desktop-commander, drunken-master |
| Size-gate | Reads huge files outline-first | headroom, mcp2cli, context-optimizer |
| Fan-out | Splits the work across many agents | agent-army, harness, Gemini lane, cc, backlog |
| Wiki and search | Builds the wiki and its search | llm-wiki (core), wiki-wonka, create-smartfolder, obsidian-notes |
| Extract | Pulls skills, tools and artifacts out | agent-ingest-audit-optimize, skill-creator, claude-patterns, compounded, skill-provenance |
| Check | Tests answers and blocks bad input | rag-evaluation, llm-secure-patterns, skill-gate |

## 5. What we know so far (measured on 2026-10-30)

- The 44 plugins take up **48 MB**, and **36 MB** of that is images, GIFs, video and lockfiles. All their skill text together is about 1.2 MB.
- The worst case is harness: 21 MB of demo media wrapped around 2 skills.
- They contain **16 hooks** in total, which get merged into one hook file you can switch off.
- These picks are based on plugin descriptions and file counts. Only agent-ingest-audit-optimize has been read in full. **The homework below is the full read.**

## 6. Rules every outside agent follows

1. **Think first:** state assumptions, and ask when unsure.
2. **Simplicity:** the minimum that solves the task.
3. **Surgical:** every line you keep traces back to wiki-admin's job.
4. **Goal-driven:** "done" only with evidence. Quote the file and line.
5. Never edit the original plugins. Every deliverable is a **new file**.
6. Use Sonnet or Haiku for reading. Never use Opus for read tasks.
7. Say for each claim whether it comes from a **full read** or only the **description**.
8. No hook may block reading a file or the owner's direction, and every hook must be able to be switched off mid-session.
9. Don't build, install, subscribe to anything or push. Research and drafts only.
10. Stop and report instead of retrying a failing step over and over.

### What every packet hands back

Each packet returns one new Markdown file, `P<n>-<name>.md`, with this for **each plugin** in the packet:

- **Source:** the repo, version and license.
- **Parts:** each skill, command, agent, script, hook and MCP server, with one line on what it does.
- **Verdict for each part:** keep, trim or cut, with a reason.
- **A trimmed draft:** the SKILL.md (or command) cut down to what wiki-admin needs.
- **The scripts it needs:** paths and dependencies.
- **Its hooks:** the event, what each one does, whether it can block, and the proposed merged version.
- **MCP servers:** whether we self-host it, and what the spec needs.
- **Conflicts:** overlaps with other parts, and the winner.
- **The bloat:** what to strip (media, tests, site files) and its size.

---

## 7. Homework packets

### P1 · Intake and convert

| Plugin | Source |
| --- | --- |
| gdrive-to-markdown | https://github.com/beaverbeard/gdrive-to-markdown |
| google-multi-account | https://github.com/stevegustafson32/google-multi-account |
| firecrawl | Repo not listed in its manifest. Locate the official Firecrawl Claude plugin. |
| apify | https://github.com/apify/apify-claude-code-plugin |
| watch-video | https://github.com/MarcinSufa/claude-watch-video |
| local-whisper | https://github.com/OrihuelaConde/local-whisper-mcp |
| desktop-commander | https://github.com/wonderwhy-er/DesktopCommanderMCP |
| drunken-master | https://github.com/beatlejute/drunken-master |
| claude-bridge | Repo not listed in its manifest. |

**Extra task:** map every source type (Docs, Sheets, Slides, PDF, DOCX, XLSX, PPTX, images with OCR, audio, video, HTML, email) to exactly one converter, and name a fallback for each.

### P2 · Size-gate and tool overhead

| Plugin | Source |
| --- | --- |
| headroom | https://github.com/petrovicistefan/claude-code-plugins |
| claude-context-optimizer | https://github.com/egorfedorov/claude-context-optimizer |
| cache-guard | https://github.com/Agulhas-Labs/claude-plugins |
| mcp2cli | https://github.com/myeolinmalchi/mcp2cli |

**Extra task:** set a size threshold above which every file goes through headroom first. From context-optimizer, name the 3 or fewer skills worth keeping, and confirm that `read-cache.js` is turned off.

### P3 · Agent fan-out

| Plugin | Source |
| --- | --- |
| agent-army | https://github.com/OneWave-AI/claude-skills |
| harness | https://github.com/revfactory/harness |
| agent-discussion | https://github.com/cyrusxyl/agent-discussion |
| crewmarshal | https://github.com/nguyengiatam/CrewMarshal |
| cc | https://github.com/anipotts/cc |
| noetic-control-room | https://github.com/NoeticEcho/control-room |
| backlog | https://github.com/backloghq/backlog |

**Extra task:** design how a batch of 1,000 documents runs end to end: batch size, checkpoints, how fake completion is caught, the Gemini CLI reading lane, the model for each role, and resuming after a crash.

### P4 · Wiki core and structure

| Plugin | Source |
| --- | --- |
| llm-wiki | https://github.com/praneybehl/llm-wiki-plugin |
| wiki-wonka | https://github.com/cooperacode/wiki-wonka |
| create-smartfolder | https://github.com/idea2go2go/smartfolder-skill |
| obsidian-notes | https://github.com/m4bwav/obsidian-notes |
| obsidian-sync | Repo not listed in its manifest. |
| cut-weight | https://github.com/enoevol81/enoevol-plugins |
| project-scaffolder | https://github.com/valsecchi75/project-scaffolder (take only the four Karpathy rules and `/wiki-gc`) |

**Extra task:** write the final wiki folder layout, the page frontmatter schema (including `sources:` sha256), and how llm-wiki's search index is rebuilt after each batch.

### P5 · Extract skills, tools and artifacts

| Plugin | Source |
| --- | --- |
| agent-ingest-audit-optimize | https://github.com/leoleonel-jf/agent-ingest-audit-optimize (already read in full) |
| skill-creator | Repo not listed in its manifest; it's Anthropic's official skill builder. |
| claude-patterns | https://github.com/adelaidasofia/claude-patterns |
| compounded | https://github.com/ankitkr3/compounded |
| adaptive-agent | https://github.com/truenorth-lj/adaptive-agent-skill |
| skill-provenance | https://github.com/snapsynapse/skill-provenance |
| skill-discovery | https://github.com/surenode-ai/skill-discovery |
| tool-schemas | https://github.com/grayskripko/marketing-skills |
| claude-war-room | https://github.com/RandMelville/claude-war-room |

**Extra task:** define the extraction loop: how a candidate is spotted, how it becomes a draft, how it's tested, how the owner approves it, and how it's published. Nothing becomes a skill or tool without the owner's approval. Record each candidate's source sha256.

### P6 · Checks and the merged hook file

| Plugin | Source |
| --- | --- |
| rag-evaluation | https://github.com/grayskripko/marketing-skills |
| llm-secure-patterns | https://github.com/wildblue-ai/llm-secure-patterns |
| skill-gate | Repo not listed in its manifest. |

**Extra task:** collect all 16 hooks from every packet into **one** `hooks.json` draft. List each hook's event, its job and how it is switched off. Add a quarantine step for documents that look like prompt injection.

### P7 · MCP self-host specs

These are the engines wiki-admin calls: memory-agent (https://github.com/noreff/memory-agent), agent-recall (repo not listed), backlog, cc, watch-video, desktop-commander, apify, google-multi-account, and cloudflare (repo not listed; Vectorize, D1 and R2 only).

**Extra task:** for each one, decide whether to self-host, keep the vendor version, or replace it with something else. For each self-hosted server, write a spec: its tools, how it is launched, where it is hosted, the secrets it needs, and its health check. Mark any that belong to the memory-store pipeline instead of wiki-admin.

### P8 · Assembly (run after P1 to P7)

Turn the packet outputs into a compile plan for one plugin:

```
wiki-admin/
  .claude-plugin/plugin.json
  skills/   scripts/   commands/   agents/
  hooks/hooks.json      (from P6)
  .mcp.json             (from P7)
  rules/                (the section 6 rules)
  SOURCES.md            (every part: origin repo, version, license, sha256 of the copied file)
```

**Acceptance:**

- The plugin is a few MB, down from 48 MB.
- About 12 plugins load at runtime instead of 44.
- Every kept line traces back to a packet finding.
- The license of every copied part is recorded.

---

## 8. Open questions for the owner

1. Where does the corpus live, and about how many documents are there?
2. Where does the wiki live: NovAExopia, the NovAExorpus vault, or somewhere else?
3. Should search start local (llm-wiki) or hosted (Supabase)?

Any answer works, including one that isn't listed here.
