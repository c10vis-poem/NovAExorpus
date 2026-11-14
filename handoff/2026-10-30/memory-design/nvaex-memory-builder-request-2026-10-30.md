# NovÆxorpus Memory and SmartFolder: schema plan and builder request

*Prepared 2026-10-30 for a build session with Fable. This is a plan, not built code. Every file named here is a proposal until the owner signs off.*

---

## 0. How to use this document (for the builder)

**Naming:** the project owner is called **The Builder**. Documentation may also say the owner or the architect. Never use any other personal name. In this document, "the owner" means The Builder.

1. Read sections 1 to 3 first: the owner's rules and what already exists. They override anything else in this document.
2. Treat sections 4 to 8 as the target design. Where a detail is marked **[VERIFY]**, check it against the live source before relying on it.
3. Build in the phases in section 9. Each phase ends at a review gate: show the owner the exact files before writing them.
4. Section 10 lists open questions. Each has a recommended answer, but the owner can answer in their own words.

---

## 1. Owner's standing rules (non-negotiable)

- **Nothing gets written, built, installed or subscribed without the owner's explicit direction.** Show the exact content first.
- **No hook, script or skill may block the owner's direction or block reading a file.** Every hook is advisory and exits 0.
- **Every hook and script can be switched off mid-session** without a restart: a flag file such as `~/.nvaex-memory-off` is checked first.
- **No subagents until the owner has approved how they'll be deployed.**
- **No failure loops.** If a step fails twice, stop, research the fix, and report.
- **A half-answered question isn't answered.** Questions to the owner always allow a custom answer, never only yes/no or A/B/C.
- **Never guess file contents.** Read files end to end, and never invent rules.
- **Canonical memory lives in git as Markdown and JSONL.** SQLite, vectors and cloud stores are indexes and caches you can rebuild from git.
- **Nothing leaves the machine** (transcripts, memory) for an outside API without the owner's direction.

---

## 2. Goals in the owner's words, cleaned up

1. **Lazy loading at launch.** A session starts by reading only `MAP.md` and `manifest.jsonl`, never every plugin, skill and hook. Full content is read on demand.
2. **A flat asset folder.** Plugins and skills live in one shallow folder, one level down from the workspace root.
3. **SmartFolder everywhere it helps.** Use the create-smartfolder method (tiered routers, sidecars, syntheses, write-forward consolidation) for the asset folder, for memory compaction and consolidation, and for the corpus.
4. **The owner's own multi-tier memory plugin**, built from parts and from reverse-engineering mem0, OB1 (Open Brain) and OmniRoute. It includes:
   - a **SQLite database per project**;
   - a **separate SQLite database for episodic memory**;
   - **SHA-256 content addressing** for every node;
   - a **Next.js MCP server** that serves the nodes;
   - **code graphs** from tree-sitter and the AST (code-review-graph, graphify);
   - **graphify's Obsidian mapping**, so graphs appear in the vault;
   - **vectors**, as separate files or stores inside the home memory system;
   - **different setups per agent** (Claude, Fable, Gemini, Codex) and **per repository**.
5. **Uses the owner's existing cloud:** Supabase and Cloudflare.

---

## 3. What already exists (checked 2026-10-29 and 2026-10-30)

- **Repos:**
  - NovAExorpus is the corpus vault.
  - NovAExopia holds the 26-plugin marketplace and wiki-admin.
  - The other repos are NovusAExenti, Aesop-Xi, AEthX-AEsc, CloviX-AEyre, Hyperion-XI, raw-databank, NvAEx-agentk, Horizon-s-home-grid and NvAEx-Recaps (private, holding the live `memory/`).
- **Standard files:** seven repos already carry MEMORY, RESUME, AGENTS, PENDING, MAP and manifest.jsonl. None has a skills manifest.json or a settings .jsonl.
- **The vault's `manifest.jsonl`** is a **file index**: 585 lines of `file, source, type, sha256, chunks, bytes`. Keep it, and extend its shape (section 5.2).
- **The account skill memory-as-skill** is a frozen 2026-07-05 snapshot that never syncs back. It's being replaced by this plugin.
- **The earlier design brief**, "Memory-as-skill v-next: design brief" (https://claude.ai/artifact/MvawjrRUA5QGCFK7NBFnAc), has its own open questions. Section 10 carries them forward.
- **Per-plugin deep-read notes:** `memory-design/plugin-deep-read-notes.md`, covering 60+ memory, prompt, retention and compile plugins.
- **How hooks reach sessions** (verified):
  - Account-synced plugins run hooks in terminal, cloud and Cowork sessions.
  - Project threads load only the repo's `CLAUDE.md`, `.claude/CLAUDE.md` and `.claude/rules/`. They don't load repo `.claude/settings.json`, skills, agents or `.mcp.json`.
  - So the hooks have to ship in a plugin.
- **Real skills must sit at `<root>/.claude/skills/<name>/SKILL.md`** to register. Any other folder works only as files a pointer tells the agent to read.

---

## 4. Architecture overview

```
workspace root (one per device, or the NovAExorpus vault)
├── CLAUDE.md, AGENTS.md         Tier 1, byte-identical (SmartFolder dual profile), under 150 lines
├── MAP.md                       router: what's here, where to look next
├── manifest.jsonl               one line per asset or file (section 5.2): the only index loaded at start
├── assets/                      the flat asset folder, one level deep
│   ├── _README.md               Tier 2 router for the folder
│   ├── <skill-or-plugin-name>/  one folder per asset (SKILL.md, scripts, hooks)
│   └── ...
├── .claude/skills/<name>/       real registered skills (only the ones that must auto-register)
├── memory/                      canonical memory, in git
│   ├── _README.md
│   ├── layers.jsonl             memory-layer pointers (section 5.3)
│   ├── ledger/                  decisions, standing rules, rejected paths (MD + @meta)
│   ├── handoffs/                dated notes plus YAML records
│   ├── recaps/                  compiled session recaps (tiered: today → recent → archive)
│   └── wiki/                    the LLM wiki: raw/ → wiki/ → index
├── .nvaex/                      rebuildable caches, gitignored except schema files
│   ├── project.db               per-project SQLite: nodes, edges, facts, FTS, vectors
│   ├── episodic.db              per-project episodic SQLite: sessions, events
│   ├── code-graph.db            tree-sitter graph (code-review-graph format or a copy)
│   └── vectors/                 optional sqlite-vec or exported embeddings
└── graphify-out/ or vault/graphs/   graphify output, including the Obsidian vault export

home memory (per device: ~/.nvaex/)
├── home.db                      cross-project identity, preferences, agent profiles, repo registry
├── profiles/<agent>.json        per-agent read and write rights to each tier (section 7)
└── off                          the kill-switch flag file (if present, every hook exits 0 silently)

cloud mirrors (optional, owner-controlled)
├── Supabase                     Postgres + pgvector: "thoughts" or "nodes" mirror, OB1-style [VERIFY]
└── Cloudflare                   hosts the MCP server (Workers or Pages) and optionally R2, D1, Vectorize [VERIFY]
```

**Truth order.** Every surface states it:

1. The raw file beats anything derived.
2. Git Markdown and JSONL beat SQLite and vectors.
3. A newer as-of date beats an older one.
4. A live directory listing beats any map.

---

## 5. Schemas

### 5.1 `MAP.md` (Tier 1 router, loaded at launch)

```markdown
# MAP: <repo or workspace name>
As of YYMMDD · Provenance: generated from manifest.jsonl + folder _README.md files · Decays when: assets or folders added or moved
Protocol: read a folder's _README.md before working in it. Read an asset's full file only when its manifest summary matches the task.

| Area | Path | What's there | Read next |
|---|---|---|---|
| Assets | assets/ | Skills, plugins, hooks (one folder each) | assets/_README.md |
| Memory | memory/ | Ledger, handoffs, recaps, wiki | memory/_README.md |
...
To refresh: ask your AI assistant to update this.
```

### 5.2 `manifest.jsonl` (one JSON object per line, loaded at launch, filtered by scope)

This extends the vault's existing file index. The existing fields `file, source, type, sha256, chunks, bytes` stay.

```json
{"id":"sha256:<hex>","kind":"skill|plugin|hook|mcp|agent|script|doc|memory","name":"wiki-ingest","path":"assets/wiki-ingest/SKILL.md","summary":"Ingest a raw source into the LLM wiki with citations (≤120 chars)","triggers":["ingest","add to wiki"],"scope":["global"],"agents":["claude","fable","gemini"],"enabled":true,"load":"on-demand|session-start|never","tokens_est":1800,"sha256":"<hex of file bytes>","bytes":7210,"source":"forked:llm-wiki@3.2.0|own","as_of":"2026-10-30","deps":["sha256:<hex>"]}
```

- **Launch rule:** load only the rows where `load` is `session-start`, plus the `name`, `summary` and `triggers` of rows matching the current repo's scope. Everything else stays on disk.
- **Change rule:** when an asset's file changes, its `sha256` changes, and the SessionStart drift check reports the mismatch. It reports only, and never auto-fixes.
- **Scope values:** `global`, `repo:<name>`, `agent:<name>`. harness-scope profiles can use the same values to hide assets per repo.

### 5.3 `memory/layers.jsonl` (memory-layer pointers, for the router script)

```json
{"layer":"ledger","need":["past decision","standing rule","rejected path"],"store":"git:memory/ledger/","index":"project.db:nodes(kind='decision')","write":"ask"}
{"layer":"episodic","need":["what happened in session X","when did we"],"store":"episodic.db","index":"episodic.db:events_fts","write":"auto-local"}
{"layer":"recaps","need":["summary of last week"],"store":"git:NvAEx-Recaps/memory/","write":"ask"}
{"layer":"wiki","need":["how does X work","source for Y"],"store":"git:memory/wiki/","index":"project.db:nodes(kind='wiki')","write":"ask"}
{"layer":"code","need":["who calls X","impact of changing Y"],"store":"code-graph.db","write":"rebuild"}
{"layer":"files","need":["where is file X"],"store":"git:manifest.jsonl","write":"rebuild"}
{"layer":"pending","need":["what's next","open asks"],"store":"git:PENDING.md","write":"ask"}
```

The `write` field says what writing is allowed:
- `ask`: preview, then write only after the owner says yes.
- `auto-local`: append to a local cache only.
- `rebuild`: regenerated from sources.

### 5.4 Per-project SQLite: `.nvaex/project.db`

```sql
-- Every unit of memory is a node, addressed by the SHA-256 of its normalized content.
CREATE TABLE nodes (
  sha256        TEXT PRIMARY KEY,          -- hex of normalized body (NFC, trimmed, LF)
  kind          TEXT NOT NULL,             -- fact | decision | rule | rejected | wiki | doc_chunk | entity | asset
  title         TEXT,
  body          TEXT NOT NULL,
  source_path   TEXT,                      -- git path the node came from (truth lives there)
  source_sha256 TEXT,                      -- hash of the source file when ingested (staleness test)
  scope         TEXT NOT NULL DEFAULT 'repo',  -- global | repo:<name> | agent:<name>
  agent         TEXT,                      -- which agent created it
  confidence    REAL,                      -- 0..1
  evidence      TEXT,                      -- suspicion | static_check | test_passed | root_cause | verified (context-distill ladder)
  status        TEXT NOT NULL DEFAULT 'active', -- active | superseded | retracted
  valid_from    TEXT NOT NULL,             -- ISO time (bitemporal: when it became true)
  valid_to      TEXT,                      -- set when superseded; never deleted
  superseded_by TEXT REFERENCES nodes(sha256),
  created_at    TEXT NOT NULL
);

CREATE TABLE edges (
  src     TEXT NOT NULL REFERENCES nodes(sha256),
  dst     TEXT NOT NULL REFERENCES nodes(sha256),
  rel     TEXT NOT NULL,                   -- supports | contradicts | supersedes | mentions | derived_from | calls | imports
  weight  REAL DEFAULT 1.0,
  source  TEXT,                            -- graphify | code-review-graph | extractor | owner
  PRIMARY KEY (src, dst, rel)
);

-- mem0-style facts: add-only. A changed fact is a new row, and the old one gets valid_to and superseded_by.
CREATE TABLE facts (
  sha256     TEXT PRIMARY KEY REFERENCES nodes(sha256),
  subject    TEXT NOT NULL,
  predicate  TEXT NOT NULL,
  object     TEXT NOT NULL,
  episode_id TEXT                          -- which episode produced it (episodic.db)
);

CREATE VIRTUAL TABLE nodes_fts USING fts5(title, body, content='nodes', content_rowid='rowid');

-- Vectors: sqlite-vec locally (rebuildable). Mirror to Supabase pgvector only on direction. [VERIFY sqlite-vec on Termux/arm64]
CREATE VIRTUAL TABLE vec_nodes USING vec0(sha256 TEXT PRIMARY KEY, embedding float[384]);

CREATE TABLE meta (key TEXT PRIMARY KEY, value TEXT);   -- schema_version, embed_model, built_from_commit
```

### 5.5 Episodic SQLite: `.nvaex/episodic.db`

```sql
CREATE TABLE episodes (
  id             TEXT PRIMARY KEY,         -- session id
  agent          TEXT NOT NULL,            -- claude | fable | gemini | codex
  surface        TEXT,                     -- terminal | termux | cloud | cowork | chat
  repo           TEXT,
  started_at     TEXT NOT NULL,
  ended_at       TEXT,
  goal           TEXT,                     -- one sentence
  outcome        TEXT,                     -- done | partial | abandoned | failed
  summary        TEXT,                     -- ≤20 lines, written forward (state / next / context)
  transcript_sha TEXT,                     -- sha256 of the exported transcript file (chat-autoexporter)
  transcript_path TEXT
);

CREATE TABLE events (
  id          INTEGER PRIMARY KEY,
  episode_id  TEXT NOT NULL REFERENCES episodes(id),
  ts          TEXT NOT NULL,
  type        TEXT NOT NULL,               -- ask | decision | correction | failure | tool | file_change | commit | handoff
  content     TEXT,
  content_sha TEXT,
  tool        TEXT,
  path        TEXT
);

CREATE VIRTUAL TABLE events_fts USING fts5(content, content='events', content_rowid='id');
CREATE INDEX events_by_episode ON events(episode_id, ts);
```

**Episodic to semantic promotion (consolidation):**

1. A `correction` or `decision` event seen in **2 or more episodes** becomes a *candidate* node.
2. The owner approves the candidate.
3. It lands in `memory/ledger/` (git) and in `project.db`.

This combines memory-toolkit's "promote feedback seen 3+ times" with memory-agent's 3-fact gate. The threshold is the owner's call.

### 5.6 Home memory: `~/.nvaex/home.db`

```sql
CREATE TABLE repos (name TEXT PRIMARY KEY, path TEXT, remote TEXT, profile TEXT, project_db TEXT, last_seen TEXT);
CREATE TABLE preferences (sha256 TEXT PRIMARY KEY, body TEXT, scope TEXT, as_of TEXT, status TEXT);
CREATE TABLE agent_profiles (agent TEXT PRIMARY KEY, profile_json TEXT, as_of TEXT);
CREATE TABLE routes (need TEXT PRIMARY KEY, layer TEXT, notes TEXT);   -- cache of layers.jsonl + D.U.M.B.A.S.S. routing later
```

### 5.7 Graph layer

- **Code graph:** code-review-graph parses with tree-sitter into a local SQLite graph, updates incrementally by file hash or git diff, and exposes MCP tools. **[VERIFY** the current schema and its Kotlin support in tree-sitter-language-pack.**]** Either read its DB directly or copy its nodes and edges into `project.db.edges` with `source='code-review-graph'`.
- **Knowledge graph:** graphify turns a folder into a graph. It parses code locally with tree-sitter, and docs, PDFs and images go through an LLM. `--obsidian` writes an Obsidian vault with backlinks. **[VERIFY:** sources disagree on the language count (19 to 40), and the doc and image pass sends content to an LLM, which needs the owner's direction.**]**
- **Obsidian:** graph exports land in `vault/graphs/`. Run obsidian-notes' linter so links render on GitHub too.

### 5.8 Agent and repo profiles: `~/.nvaex/profiles/<agent>.json`

```json
{
  "agent": "fable",
  "reads": ["ledger","pending","wiki","recaps","code","files","episodic"],
  "writes": {"episodic":"auto-local","handoffs":"ask","ledger":"ask","wiki":"ask"},
  "session_start": ["MAP.md","manifest.jsonl:session-start","RESUME.md","PENDING.md"],
  "max_start_tokens": 6000,
  "repo_overrides": {"Aesop-Xi": {"reads+": ["code"]}, "raw-databank": {"writes": {"wiki":"ask"}}}
}
```

Gemini CLI and Codex get the same file. Their loaders read `AGENTS.md`, which points to these profiles.

---

## 6. The MCP server (Next.js)

- **Shape:** a Next.js app with a route handler exposing an MCP endpoint over streamable HTTP, using the official MCP TypeScript SDK. **[VERIFY** the current SDK and Next.js adapter.**]** It runs locally, on Termux, or hosted.
- **Hosting options:**
  1. Local on the phone or PC, reached by cloud sessions through an Anthropic MCP tunnel (the mcp-tunnels plugin).
  2. Cloudflare (Workers or Pages, with D1 or R2 holding read-only copies).
  3. Vercel.
  
  **[VERIFY** Next.js on Cloudflare: the adapter and its limits on SQLite and native modules.**]**
- **Tools (all read-only except the writes noted):**

| Tool | Does |
|---|---|
| `route.resolve(need)` | Returns which layer and file to read (from `layers.jsonl`) |
| `node.get(sha256)` | Returns one node, its edges and its provenance |
| `memory.search(query, scope, kinds, k)` | Hybrid search: FTS5, vectors and the graph neighborhood |
| `episode.list(repo, since)` / `episode.get(id)` | Episodic recall |
| `graph.neighbors(sha256, rel, depth)` | Graph walk |
| `code.impact(path_or_symbol)` | Proxies code-review-graph |
| `manifest.find(query, scope)` | Finds an asset without loading it |
| `memory.propose(kind, body, source)` | **Write.** Returns a preview and a pending id. Nothing is written yet |
| `memory.commit(pending_id)` | **Write.** Only after the owner says yes. Writes the git Markdown first, then indexes |

- **Auth:** a bearer token from a secret store, never committed. Supabase calls use row-level security and a scoped key.
- **Injection containment:** all text returned from memory is labeled as data. The server never returns instructions to obey (a pattern from whydone and oak-memory).

---

## 7. Reverse-engineering targets: what to take from each

| Target | What it is (secondhand, so **[VERIFY]** against the repo) | Take | Leave |
|---|---|---|---|
| **mem0** | Memory layer. Current open-source extraction is reported as single-pass and add-only: context lookup, then hash dedup, then embedding. The older version was a two-call ADD/UPDATE/DELETE/NOOP flow. Graph memory reportedly moved to their paid platform | Add-only facts with supersede (keeps history for "when did this change"), hash dedup, one extraction call per batch | Their hosted platform. Any background auto-capture |
| **OB1 (Open Brain)** | Nate B. Jones's open project: one Supabase Postgres "thoughts" table with vector search, reached through MCP. Forks add graph memory and a plain-HTTP (no-MCP) path | A Supabase mirror schema with pgvector, the MCP access pattern, and the no-MCP HTTP fallback for Termux | Anything that bypasses the git-truth rule |
| **OmniRoute** | A self-hosted AI gateway (diegosouzapw/OmniRoute, MIT, TypeScript with a Next.js dashboard): one OpenAI-compatible endpoint across many providers, routing strategies, failover, MCP support | Routing strategy ideas for model choice per job (a cheap model extracts atoms, a strong model merges, Gemini does bulk reading) and failover | Its "free tokens" marketing claims. Reviewers caution about production readiness |
| **code-review-graph** | tirth8205's tool: tree-sitter into a local SQLite graph, incremental, with MCP tools | The code layer as-is or a copy of its tables | Its unverified token-saving claims |
| **graphify** | safishamsi's tool: folder to knowledge graph, tree-sitter for code, LLM for docs, `--obsidian` export | The Obsidian export and the entity graph | Running the doc and image LLM pass without direction |

Sources: [OmniRoute](https://dev.co/ai/mcp/omniroute), [OmniRoute guide](https://agentpedia.codes/blog/omniroute-ai-gateway-routing-setup-guide), [OB1 on SourcePulse](https://www.sourcepulse.org/projects/26334376), [OpenBrain explainer](https://www.mindstudio.ai/blog/what-is-openbrain-personal-ai-memory-database), [graphify README](https://cdn.jsdelivr.net/gh/safishamsi/graphify@main/README.md), [code-review-graph](https://tomevault.io/tome/tirth8205/code-review-graph), [mem0 docs](https://docs.mem0.ai/core-concepts/memory-evaluation.md), [mem0 graph memory](https://docs.mem0.ai/components/graph_memory/overview).

---

## 8. SmartFolder applied: lazy loading and consolidation

Taken from create-smartfolder v6.6.0 (read in full):

- **Tiers:**
  - Tier 1 is the resident `CLAUDE.md` / `AGENTS.md`: byte-identical, under 150 lines, no `@` imports. It's the only thing that survives compaction.
  - Tier 2 is a `_README.md` router in each meaningful folder.
  - Tier 3 is derived surfaces: sidecars (`<stem>_Summary.md`), syntheses (`_Synthesis.md`), status boards and decision logs.
  - Raw files are opened last.
- **Applied to the asset folder:**
  - `assets/_README.md` routes by category.
  - Each asset's `manifest.jsonl` row is its one-line sidecar, so a session reads 365 summaries' worth of rows filtered down to the current scope, not 365 SKILL.md files.
- **Applied to compaction and consolidation:**
  - **Write forward, not backward.** A live surface (RESUME, status, handoff) leads with current state and next step. A refresh rewrites the front matter instead of appending.
  - At a chapter boundary, history is **demoted whole** into a labeled history section or a sealed, dated file. It's never deleted.
  - Before compaction (PreCompact, advisory), the brief written is goal, next step, files, decisions and state (better-compact's brief). The episodic DB keeps the full record.
- **Every derived surface carries:**
  - An `As of YYMMDD` line.
  - Provenance: what it was built from, and which commit.
  - A decay condition.
  - The line "To refresh: ask your AI assistant to update this."
- **Safety rules carried over:**
  - Back up before moving anything, and keep a move log.
  - Verify by content hash.
  - Never delete; archive with a sha256 manifest (cut-weight).
  - Never clobber an existing CLAUDE.md or AGENTS.md without the owner's OK.

---

## 9. Build phases (each ends at a review gate)

| Phase | Deliverable | Acceptance check |
|---|---|---|
| 0. Intent | Owner answers section 10 | Every question answered, custom answers welcome |
| 1. Inventory | Read-only report of the current MAP, manifest and memory files across the 11 repos plus NvAEx-Recaps/memory | Counts match a live listing, and nothing is written |
| 2. Schemas | Final `manifest.jsonl` fields, `layers.jsonl`, the three SQLite DDLs and profile JSON, shown in full | Owner sign-off |
| 3. Asset folder | `assets/` with `_README.md` plus a generated `manifest.jsonl` for one repo as a sample | A session start loads under `max_start_tokens`, and the owner judges the sample useful |
| 4. Indexer | Stdlib Python (or Node) script: git MD/JSONL into `project.db` and `episodic.db`, sha256 on every node, rebuildable from scratch | Delete the DBs, rebuild, and get identical row hashes |
| 5. Hooks (in a plugin) | SessionStart (read-only load plus drift report) and Stop (fixed nudge, never blocks). Both check `~/.nvaex/off` first | Creating the flag silences both mid-session. Neither ever exits non-zero |
| 6. Graphs | Wire in code-review-graph and graphify, with the Obsidian export into `vault/graphs/` | Graph queries answer on one repo, and links lint clean |
| 7. MCP server | Next.js MCP with the section 6 tools. Writes go through propose and commit | Writes refused without a commit. Reachable from a cloud session through the tunnel |
| 8. Cloud mirrors | Supabase pgvector mirror (OB1-style) and optional Cloudflare hosting | Mirror rebuilds from git, and nothing is mirrored without direction |
| 9. Agent parity | Profiles for Claude, Fable, Gemini and Codex, with AGENTS.md pointers | A parity probe: each agent quotes planted text exactly |
| 10. Routing | OmniRoute-style model routing for extraction and merge jobs, with the D.U.M.B.A.S.S. routing table slotted in | Each job's model choice is logged |

---

## 10. Open questions (my recommendation in brackets, but any answer works)

1. **Where does the workspace root live on each device?** [The NovAExorpus vault root on the phone (`/sdcard/Documents/NovÆxorpus/`) and in each cloud clone.]
2. **Does the flat asset folder hold the full plugin sources, or only pointers to NovAExopia?** [Full sources in NovAExopia, plus a generated `assets/` view of pointers and summaries.]
3. **Which embedding model and dimension?** [A small local one, e.g. bge-small at 384 dimensions, so nothing leaves the device. Check it runs on Termux.]
4. **Episodic capture:** exported transcripts only (chat-autoexporter), or live events from hooks? [Exported transcripts first. Live events later, local only.]
5. **Promotion threshold** from episodic to the ledger. [Seen in 2 or more episodes, then the owner approves.]
6. **MCP server hosting.** [Local on the phone first, through the MCP tunnel. Cloudflare after.]
7. **Supabase mirror scope.** [Ledger and wiki nodes only, never raw transcripts.]
8. **Is OmniRoute adopted as the gateway, or only studied for its routing ideas?** [Studied first. Gemini and Claude are called directly until it's verified.]
9. **Carried over from the earlier brief:**
   - `layers.jsonl` location [`memory/layers.jsonl` in NovAExorpus].
   - Upload to the account or install from the marketplace [upload, with the source in NovAExopia].
   - One plugin or several [one core plugin, with Recaps and retention as separate plugins].
   - What goes in settings .jsonl.
   - Handoff format [Markdown plus YAML].
   - Which of `handoff/` or `handoffs/` is canonical.
   - Recaps through memory-agent with a review gate.
   - Gemini parity now or later.

---

## 11. Parts library (plugins to fork from, all on the keep list)

- **Memory:**
  - anchor-memory: @meta anchors and the drift linter.
  - whydone: ask-mode journal and the nudge-only Stop hook.
  - memory-agent: compile with receipts and a conflict log.
  - remember: the now, today, recent, archive tiers.
  - agent-recall: bitemporal scope chains.
  - compounded: approve-before-learning.
  - claude-patterns, adaptive-agent, jevmem, pmm and memory-toolkit (PHILOSOPHY.md, docs-reflect).
- **SmartFolder and wiki:** create-smartfolder, llm-wiki, wiki-wonka, obsidian-notes, obsidian-sync, gdrive-to-markdown, rag-evaluation, headroom.
- **Code graph:** graph-indexer, code-map, claude-war-room, plus the external code-review-graph and graphify.
- **Handoff and compaction:** context-handoff, handoff (per branch), better-compact, chat-autoexporter, ccfind.
- **Control:** harness-scope (per-repo profiles), skill-gate, skill-provenance, cut-weight, spec-drift.
- **MCP:** mcp-server-dev, mcp-tunnels, mcp2cli, tool-schemas, mcp-debugging.
- **Cloud:** supabase-expert, cloudflare, firebase, gcp-devkit.
