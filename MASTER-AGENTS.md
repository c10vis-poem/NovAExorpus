# MASTER-AGENTS (auto-generated, do not hand-edit)

Every base repo's `AGENTS.md` from its `main` branch, rebuilt by
`.github/workflows/master-files.yml` whenever one of them changes.
Edit the repo's own `AGENTS.md`, never this file.

---

## NovAExorpus  (`AGENTS.md` @ 7ee160f)

### AGENTS.md

Repository: `NovAExorpus`

Authority: NovÆxorpus Master Canon Specifications

#### RULE 1 — NO ACTION WITHOUT AN EXPLICIT PROMPT

A skipped or unanswered question is NOT consent. No action — reading,
searching, or anything else — without an explicit prompt or permitted
request. State-changing or not, it doesn't matter.

#### RULE 2 — READ THE REPO'S OWN AGENTS.MD AND RESUME.MD FIRST

Before doing anything else in any of the operator's repos — before
investigating, before answering a question about that project's state —
check for and read that repo's own AGENTS.md and RESUME.md. Step one,
every session, every repo, no exceptions.

`AGENTS.md` is the single instruction file for every engine. A repo's
`CLAUDE.md` is only `@AGENTS.md` plus things only Claude Code can use.

#### RULE 3 — DOCUMENTS 00–05 ARE WRONG

`00_DEFINITIVE_MASTER_SPECIFICATION_V3_COMPLETE.md`,
`01_SOVEREIGN_NODE_AND_APK_TOPOLOGY.md`, `02_DUMBASS_UNIVERSAL_MEMORY_SPEC.md`,
`03_DUAL_OPERATIONAL_HARNESS_AND_MCP_SPEC.md`,
`04_ON_DEVICE_INGESTION_AND_W5H_FRAMEWORK.md` and
`05_FEDERATED_FILE_TREE_TOPOLOGY_MASTER.md` all contain inconsistencies
and incorrect statements (operator, 2026-09-28). Never cite them as truth.
The grill-with-docs session replaces them. (The `01_raw_sources/`…
`05_episodic_logs/` folders are unrelated.)

#### RULE 4 — MOST OF THE CORPUS HAS NOT BEEN READ

Fewer than ~150 files have honestly been read and implemented into the
plan; 1,000+ remain (operator estimate, 2026-09-28; the vault holds ~4,000
markdown files). No record exists of which files were read —
`manifest.jsonl` only lists 585 converted files, and `GRILL-MANIFEST.md` is
empty. Never claim the plan reflects "the corpus". Say which files you
actually read.

#### GH workflow (every repo)

1. Use the operator's `c10vis-poem` fork of every tool. At session start,
   sync every fork with upstream so everything is current. A fork with its
   own commits gets an upstream PR — never a force-sync.
2. Work on a branch, never directly on `main`/`master`.
3. At the END of the session — once, not after every change — push.
   GitHub's secret scanning and push protection are the secret scan (plus
   the gitleaks CI job); an agent grepping is not a substitute.
4. CI runs, PR opens, auto-merge into `main` on green.
5. Leave the branch in place after merge — do not delete it.
6. Nothing sits unmerged: every pending change, unpushed commit and open
   PR is merged or flagged as needing a fix.
7. Never change these rules or invent exceptions when something breaks —
   report the problem and ask the operator.

Enforced by `~/bin/sync-forks` (session start) and `~/bin/ship-session`
(session end) on the operator's phone. The vault syncs through the
GitSync Portal plugin on the `vault-sync` branch, which goes through the
same PR → CI → auto-merge gate.

Source: operator-confirmed 2026-09-13, restated and extended 2026-09-28.

#### Task observer (every engine)

Run the task-observer skill (`c10vis-poem/aesop-task-observer`) before the
first tool call of any session and before proposing a plan. Every harness
carries the skill; observations go to one shared log in this vault
(`skill-observations/`). Planned: an OmniRoute tool `observation_log` so
all harnesses write through one endpoint (orchestration contract §3.2,
aesop-xi PR #18) — not built yet, so each harness runs the skill itself.

#### Launch

`bash tools/launch.sh` loads secrets, checks OmniRoute, Terrestrial Brain,
mem0 and code-review-graph, then starts the engine. Claude Code also loads
the `router-guard` output style and the `.claude/hooks` SessionStart check —
those two are the only Claude-Code-only pieces.

#### MCP servers

Defined in `.mcp.json` at repo root: `omniroute` (gateway), `mem0`
(episodic memory), and `terrestrial-brain` (structural memory). All take
endpoint/credentials from env vars — see `.mcp.json` for the exact
variable names. Set them locally; never commit values.

#### Mandatory runtime pipeline (all engines)

Every agent — Claude Code, Codex, dsh, Prime Agent, Hermes — must satisfy
these layers in order before writing files or running commands.

##### Layer sequence

| # | Layer | Name | Interface | Endpoint |
|---|-------|------|-----------|----------|
| 0 | Execution + routing | OmniRoute | HTTP gateway daemon | VM `:20128` |
| — | Judgment | Continual Harness | OmniRoute internal | via OmniRoute |
| — | Execution ledger | Reasoning Bank | OmniRoute internal | via OmniRoute |
| 1 | Token saver | honey-for-devs | MCP tool / skill / text-strip | per-engine |
| 2 | Orchestration | task-observer | CLI / file-gen (Claude Code only) | per-engine |
| 3 | Code intel | code-review-graph | MCP Server (stdio) | local binary |
| 4 | Episodic memory | mem0 | MCP Server (HTTP) | `mcp.mem0.ai` |
| 5 | Structural memory | terrestrial-brain | MCP Server (HTTP) | VM `:8000` |

The VM's external IP changes on every start; `~/bin/vm on` prints it.

**OmniRoute** is the execution layer, memory retrieval layer, and routing
layer. It distributes requests, retrieves memory context, and makes
routing decisions. Continual Harness provides the judgment — it watches
agents and their refinements mid-run and optimizes routing. Reasoning Bank judges each finished
task and distils lessons for similar tasks later. Neither does crash
recovery or automatic rollback (verified in source 2026-09-30). OmniRoute
decides when they and the memory layers turn on and off; while running,
each is its own MCP server (operator, 2026-09-30).

**OmniRoute fallback:** if OmniRoute is unreachable, fall back to direct
execution and log a warning. All other memory layers remain active via
their individual MCP connections.

**mem0 safety:** before `update_memory` or `delete_memory`, always
`get_memory` or `search_memories` first. Never `delete_all_memories`.

##### Multi-write protocol

Every execution cycle follows three phases:

1. **READ** — query mem0 (session context), terrestrial-brain (static
   guards/preferences), code-review-graph (code dependencies). Do not
   guess file imports.
2. **WRITE-BACK** — commit ephemeral state to mem0, long-term invariants
   to terrestrial-brain.
3. **OBSIDIAN LOG** — on every terrestrial-brain write, create/append a
   markdown file in `~/storage/shared/Documents/NovAExorpus/memories/`
   with YAML frontmatter (`source_db`, `uuid`, `timestamp`, `category`).

##### Secondary tools (on-demand, not per-prompt)

| Tool | Interface | When |
|------|-----------|------|
| graphify | CLI via proot (`~/bin/graphify`) | Codebase mapping, knowledge graph, `--obsidian` export |
| obsidian | obsidian-skills plugin or CLI | Vault interaction, note linking |
| notebook-lm | Python CLI (`notebooklm-py`) | Document ingestion, audio overview, research export |

##### Harness anchors

The multi-write protocol, layer roles table, and pre-flight gate are
immutable — no automated refinement or optimization pass may alter them.

##### Enforcement

- Do not write code before pre-flight layers have run.
- Do not bypass OmniRoute unless it is unreachable.
- Do not silently skip a memory layer — log the failure if one is down.
- Do not skip the Obsidian vault log on any terrestrial-brain write.

#### Cross-engine compatibility (this file only — tool-agnostic)

This file is read by any agent, not just Claude Code. Two rules that follow
directly from testing across engines:

- **Honey for Devs applies universally** — natively in Claude Code, as a
  text-strip layer in Codex, as a Cordis plugin in DeepSeek Harness (dsh).
  Apply its rules regardless of which engine is running.
- **task-observer / GSD-style skill scaffolding is Claude-Code-only.** Codex
  cannot parse markdown skill wrappers or the dual-layer activation protocol;
  dsh's sandboxed plugin layer blocks task-observer's observation-log writes
  entirely. Do not expect either to work, or try to force them, under Codex
  or dsh — that's the `.claude/` directory's job, not this file's.
- Claude Code and any local engine (Prime Agent, Codex, dsh) are never active
  in the same repo directory at the same time — running two simultaneously
  causes git-lock and file-write races.

#### Agent skills

##### Issue tracker

GitHub Issues on `c10vis-poem/NovAExorpus`, via `gh -R c10vis-poem/NovAExorpus`. See `docs/agents/issue-tracker.md`.

##### Triage labels

Default five: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. See `docs/agents/triage-labels.md`.

##### Domain docs

Single-context: root `CONTEXT.md` + `docs/adr/`, created lazily by `/domain-modeling`. See `docs/agents/domain.md`.

---

## aesop-xi  (`AGENTS.md` @ da888a4)

### Æsop-Xi — repo conventions (every agent: Claude Code, Codex, dsh, Hermes, Prime Agent)

[IF THIS HAS CHANGED SINCE 9-01-2026 THIS DOCUMENT NEEDS TO BE UPDATED TO REFLECT THAT] 

Applies to any agent session working in this repo, regardless of which
session or model. Created 2026-08-31
— previously nonexistent despite RESUME.md
implying a handoff process was already in place.

#### Operator Rule 1 — no action without an explicit prompt

A skipped or unanswered question is NOT consent. No action — reading,
searching, or anything else — without an explicit prompt or permitted
request. State-changing or not, it doesn't matter.

#### Operator Rule 2 — read this file and RESUME.md first

Before doing anything else in this repo, read this AGENTS.md and RESUME.md.
Standing convention across the operator's repos for months — step one,
every session, no exceptions. (Complements the session-handoff workflow below.)

#### Session handoff workflow

- **`RESUME.md` is fully rewritten at the end of every session** — never appended
  to. It is a snapshot of current state, not a running log. (The pre-2026-08-31
  version had grown to 300 lines across many sessions and contained literal
  unresolved git conflict markers from a stash that was never cleanly finished —
  that's what happens when this rule isn't followed.)
- **Anything flagged during a session but not addressed goes into `unresolved.md`**
  at repo root, not into RESUME.md. `unresolved.md` is a durable, cross-session
  backlog — items persist until resolved or explicitly dropped, and it is NOT
  rewritten each session the way RESUME.md is.
- **Review open `unresolved.md` items with the user early in a session** that
  touches this repo, rather than silently carrying them forward or silently
  dropping them.
- `RESUME.md` may point to specific `unresolved.md` items when they're relevant to
  the immediate next session; `unresolved.md` remains the permanent home for
  everything else.

#### Memory — three separate systems, don't conflate them

- **Dev-process continuity building Æsop-Xi**: this file + `RESUME.md` +
  `unresolved.md`. Operational, about the build process.
- **The finished Æsop-Xi agent's own runtime memory model**: `ARCHITECTURE.md`
  §4 (Declarative / Recall / Strategic / Working-Ephemeral) and
  `protocol/memory.md`. Product architecture spec.
- **The whole stack's runtime memory infrastructure** (the actual mem0 /
  terrestrial-brain / OmniRoute / reasoning-bank services that every agent
  across the 7 base repos consumes): see `## Runtime memory stack` below.
  aesop-xi is the canonical home per the naming canon ("memory layer, context
  formatting, tool and context orchestration, protocols"). The other 6 base
  repos reference this section, they don't duplicate it.

#### Runtime memory stack (data plane, canonical here)

**Architecture — one-way routing through OmniRoute:**

```
[any agent, any harness]
      │
      ▼
OmniRoute @ localhost:20128/mcp     ← single MCP endpoint
      │
   ┌──┴────────┬────────────────┐
   ▼           ▼                ▼
 mem0     terrestrial-brain   local SQLite FTS5
 (hosted) (Postgres+pgvector) (offline fallback)
      │
      ▼  async tap on every completion
 mem0 habits + Reasoning Bank failure traces
                │
                ▼
   NovAExorpus/05_episodic_logs/
```

**Layer roles:**
- **mem0** — in-session episodic state, user habits, "what was said 2 min ago"
- **terrestrial-brain (= OB1)** — structural governed retrieval via MCP
  (`knowledge.retrieve`, `knowledge.record`); universal, node-independent
- **OmniRoute** — the gateway; dynamic-dispatch + local fallback + async
  memory tap; agents never manually pick backends
- **ReasoningBank** — judges each finished task (success/fail) and distils
  up to 3 lessons, recalled for similar tasks later. Planned as an OmniRoute
  plugin; not built. No crash recovery.
- **Continual Harness** — reset-free self-improvement loop (rewrites its own
  strategy prompt, skills and memory mid-run). No automatic rollback; backups
  are restored by hand. Scope for us still open; not built.

**Homes on disk (all under aesop-xi):**
- `skills/omniroute/` — routing config, decay policies, memory-tap rules
- `skills/mem0/` — mem0 client config, per-project user_id defaults
- `skills/terrestrial_brain/` — obsidian sync config, ingestion routes
- `tools/omniroute/` — start/stop scripts, port 20128 bind
- `tools/reasoning_bank/` — ledger reader/writer; trajectories flush to
  `NovAExorpus/05_episodic_logs/`
- `tools/continual_harness/` — supervisor loop

Upstream fork trackers stay for sync only (`clovis-mem0-vingiaN`,
`NovA-terrestrial-brain`, `OmniRoute`, `reasoning-bank`) — operational
code lives here.

**Runtime state (not repo):**
- Postgres data: `~/pgdata/` on device; migrates to Jetson later
- Keys: `~/.mem0/.env` (chmod 600), `~/.openwiki/.env`,
  `~/repos/NovA-terrestrial-brain/local-mcp/.env.local`
- mem0 hosted MCP: `https://mcp.mem0.ai/mcp`; key starts with `m0-`
- OmniRoute upstream provider: OpenRouter (single, 160+ models via
  `OPENROUTER_API_KEY`)

**Bootstrap** — `tools/bootstrap.sh` is canonical. Every other repo's
`tools/bootstrap.sh` is a thin wrapper that calls this first, then does
repo-specific post-boot. Idempotent, fast on hot start, loud on failure.
Runs on session start via AGENTS.md instruction, git post-checkout hook,
or manual invocation.

**Decisions:**
- Chose hosted mem0 MCP over self-hosted docker server (Termux can't run
  Docker; hosted covers cross-device automatically).
- mem0 pip SDK doesn't install on Termux (grpcio wheel build fails on
  bionic); use MCP + plugin only. SDK path via proot-Debian if ever needed.
- Terrestrial-brain runs phone-local NOW (Termux Postgres 18.2 + pgvector
  v0.8.6 built from source with `MKDIR_P/INSTALL/SHLIB_LINK` overrides);
  migrates to Jetson later via env var URL swap, no rebuild.
- OmniRoute → OpenRouter as single upstream, not direct provider APIs.
- Repo-shape decisions (Novus-Agenti demolish, restructure) deferred to
  post-grill session.

#### Termux/Android platform gap — the general fix (2026-09-06)

`bootstrap-stack.sh`'s Android failures (code-review-graph, notebooklm-py/Playwright,
OmniRoute/libsql) share one root cause: those packages target **glibc Linux**;
Termux is **Android/bionic**. `proot-distro login debian` (already installed on
this phone) is genuine glibc aarch64 — route glibc-only pieces through it instead
of patching each package individually. Use Termux's own native builds first where
they already exist and are better (e.g. Postgres: Termux ships PG18 natively,
faster and no proot needed — pgvector just needs building from source with
`MKDIR_P`/`INSTALL`/`SHLIB_LINK` overridden, since Termux's own `pg_config` bakes
in nonexistent `/usr/bin/*` paths and doesn't link `libm`). `proot-distro login`
runs with `--kill-on-exit` — a persistent background process needs the *outer*
`proot-distro login ...` command itself backgrounded, not just an inner
`nohup`/`disown`, or it dies the instant the invoking shell returns. Full account:
the "Bootstrap Triage" artifact from the 2026-09-06 session.

#### Discovered assets (2026-08-30/31) — previously unused, now catalogued

Found sitting unused in `~/downloads` or built during this session. Don't
re-discover these from scratch:

- **`~/tools/geniex-bench`** — GenieX's NPU benchmark tool (native Android/bionic,
  no proot needed). Confirmed working: `--plugin {llama_cpp|qairt} --device
  {cpu|gpu|npu|hybrid|auto} -m <path-or-model-id>`. This is the tool to point at a
  Gemma GGUF for a real NPU benchmark. Needs `LD_LIBRARY_PATH` set to
  `lib:lib/llama_cpp:lib/qairt:lib/qairt/htp-files` (all four, not just one — this
  bit initially non-obvious). Set up via `aesop-voice-pipeline` skill's
  `setup_geniex_bench.sh`.
- **`~/tools/whisper-parakeet`** — whisper.cpp + NVIDIA Parakeet toolkit (glibc,
  needs the Debian proot). Includes `whisper-server`, `whisper-quantize`, Parakeet
  CLI/test binaries. Set up via the same skill's `setup_whisper_parakeet.sh`.
- **`~/downloads/processor_config.json`** — a real `Gemma4AudioFeatureExtractor`
  config (mel spectrogram params) for the multimodal Gemma 4 models also in
  `~/downloads` (`gemma-4-12B-it-qat-UD-Q4_K_XL.gguf` etc.). Needed if their audio
  branch ever gets run.
- **`~/downloads/htp_backend_ext_config.json`** — NOT directly reusable: targets
  `dsp_arch: v73` / a ViT vision graph, not this phone's actual v79 chip or an LLM
  graph. See `aesop-voice-pipeline/references/htp-backend-mismatch.md` for detail.
  Regenerate fresh via Qualcomm's own AI Hub/QAIRT tooling when actually needed,
  don't hand-patch this one.
- **`~/downloads/mcp.json`** — a working MCP server config for an `agentmemory`
  server via `npx`, usable as-is.
- **`~/downloads/quickstart.md` / `usage.md`** — real docs for OpenWiki (your
  `c10vis-poem/openwiki` fork), not generic filler.
- **`~/downloads/INSTRUCTIONS.md`** — doc-writing instructions for the
  `Novus-Agenti` wiki project specifically.
- **ECC** (`~/repos/ECC-aesop`) — a real, ready-to-go Claude Code plugin
  (`.claude-plugin/plugin.json`) never actually installed via the plugin system.
  Confirmed against `~/.claude/plugins/installed_plugins.json` (only 3 unrelated
  plugins listed). Deferred to a future flash session — see `unresolved.md` in
  NovAExorpus.

#### Enforcement hooks H1–H7 travel with this repo (2026-10-02)

`.claude/settings.json` registers every phone hook (RESUME/check-in/Stop gates, sync-on-use, ledger, ship-session, secret-guard, ENFORCEMENTS gate, prompt classifier, branch/git gates, context-diff, housekeeping, archive) through `deploy/phone/hooks/run-hook.sh`. A session started in this repo gets them on any device; where `~/.claude/hooks/<name>` already exists (this phone) the launcher exits 0 so nothing fires twice. Sources stay in `deploy/phone/hooks/` — edit there, copy to `~/.claude/hooks/`.

#### Subagents — standing order (operator, 2026-10-01; updated 2026-10-04)
This is the explicit ask the Agent tool requires; don't wait to be told.
- A request with independent parts → spawn subagents for them in parallel; do the
  remaining parts myself meanwhile; never sit idle waiting.
- Size the model per task: haiku = mundane lookup/grep/listing; sonnet = normal
  research, audits, routine code; opus/fable = hard reasoning, architecture, debugging.
- Single, simple, sequential tasks stay inline — no spawn.
- **Every subagent keeps a live progress file**, and the spawn prompt must say so:
  `~/.claude/session-work/<date>/agent-<topic>.md`, written FIRST (before any work)
  and updated after every step, with:
  - `## Plan` — every step as a checkbox, `[x]` done / `[ ]` pending
  - `## Last action` — timestamp + what it just did / is doing now
  - `## Findings` — results so far (so nothing is lost if it's stopped)
  - `## Blocked` — anything it's stuck on
- When the operator asks where a subagent is, read its progress file and answer —
  never wait for it to finish. A stale `Last action` timestamp = likely hung: say so
  and offer to stop it; its findings survive in the file.

#### Every agent must know

Two things every agent MUST know:
- **Never call mem0 or terrestrial-brain directly.** All memory access
  goes through OmniRoute at `localhost:20128/mcp`. OmniRoute dispatches
  intelligently and taps every response for async writes to mem0 habits +
  Reasoning Bank traces. Direct calls bypass the observation layer.
- **Every session starts with `bash tools/bootstrap.sh`** in any repo.
  Idempotent; hydrates runtime deps (Postgres, OmniRoute, keys, skills)
  and syncs the repo with origin/main.

#### Cross-engine compatibility

Testing-derived rules:

- **Honey applies universally** — natively in Claude Code, as a text-strip
  layer in Codex, as a Cordis plugin in DeepSeek Harness (dsh). Apply its
  rules regardless of engine.
- **task-observer / GSD-style skill scaffolding is Claude-Code-only.**
  Codex cannot parse markdown skill wrappers or the dual-layer activation
  protocol; dsh's sandboxed plugin layer blocks the observation-log writes
  entirely. Do not expect either to work, or force them, under Codex/dsh —
  that's the `.claude/` directory's job.
- **Claude Code and any local engine (Prime Agent, Codex, dsh) are never
  active in the same repo directory at the same time** — running two
  simultaneously causes git-lock and file-write races.

#### Hook conventions per engine

- **Claude Code**: hooks live in `~/.claude/hooks/` (device-local); sourced
  from `aesop-xi/skills/omniroute/hooks/claude-code/`. `PreToolUse` queries
  OmniRoute for relevant memories; `PostToolUse` writes trajectories.
- **Codex**: hooks live in `~/.codex/hooks/`; sourced from
  `aesop-xi/skills/omniroute/hooks/codex/`. Same signal points, different
  hook API.
- **dsh (DeepSeek Harness)**: Cordis plugin under
  `aesop-xi/skills/omniroute/hooks/dsh/`; installed via `cordis add`.
- **Prime Agent / Hermes / other**: shape TBD; capture per-harness plugin
  layer as we identify them.

Source: operator-confirmed 2026-09-15; cross-linked in
`~/.claude/CLAUDE.md` on the operator's device and in the
`gh-workflow-convention` memory entry.

#### Git workflow — PR required, no direct pushes to main

Push changes to a branch, open a PR, let the `CI` GitHub Action run, merge
once it's green (`allow_auto_merge` is on, so this can auto-merge with no
manual click). Do not `git push origin main` directly for code changes.
Before every push, scan the diff for secrets/keys and refuse to push if any
are found. Delete the branch after merge (`--delete-branch`; repo auto-delete
is on) unless the operator says otherwise for a specific case.

The point of this workflow is that everything reaches `main` — a branch
that never gets a PR opened, or a PR that never gets merged, is a failure
of this rule, not a valid alternative to it. Don't let work sit stranded.

#### Scoping note

This file only loads automatically when a session's working directory is inside
this repo. A session started elsewhere (e.g. `~/downloads`) will not see it or
`RESUME.md`/`unresolved.md` unless it's explicitly pointed here.

---

## novus-aexenti  (`AGENTS.md` @ 7e4e8f7)

### NovÆxenti — agent logic layer

Canon name: **NovÆxenti**. Repo name: `novus-aexenti`. See `NovAExorpus/NAMING-CANON.md`.

#### What this is

The agent intelligence layer of the Æsop-Xi stack. Houses executor-core (task
execution agents, mode definitions) and query-core (meta-prompt compilation,
intent classification). This is the "brain" — Æsop-Xi is the infrastructure it
runs on, NovÆxopia is the action surface it drives.

#### Stack position

```
Æsop-Xi          infrastructure (MCPs, hooks, memory, routing, protocols)
  └─ NovÆxenti   agent logic (this repo) — executor + query cores
       └─ NovÆxopia   tools, harness, engine — what the agent can do
            ├─ Æsc         terminal daemon
            └─ Æyre        voice / vision daemon
```

NovÆxorpus (NovAExorpus) is the data bank — orthogonal to this stack, feeds
all layers.

#### Conventions

- `executor-core/` — small-model task execution agents (0.8B executor,
  file-administrator, NPU inference manager, frontier callers).
- `query-core/` — large-model query/reasoning agents (9B query, oeracle,
  IT helpdesk).
- `node-beta-swarm/` — Node Beta home-node agents (cross-auditor,
  home-assistant, red-auditor, trend-scraper, web-ingestion).
- Harness configs in `harnesses/` define how an agent runtime is invoked.
- Mode definitions in `modes/` describe behavioral presets.
- `manifest.jsonl` is the machine-readable index — regenerate, don't hand-edit.

#### Operator Rule 1 — no action without an explicit prompt

A skipped or unanswered question is NOT consent. No action — reading,
searching, or anything else — without an explicit prompt or permitted
request. State-changing or not, it doesn't matter.

#### Operator Rule 2 — read this file and RESUME.md first

Before doing anything else in this repo, read this AGENTS.md and RESUME.md.
Standing convention across the operator's repos for months — step one,
every session, no exceptions.

#### Git workflow

PR required. No direct pushes to main. CI runs gitleaks + structure check.
Before every push, scan the diff for secrets/keys and refuse to push if any
are found. On green CI, auto-merge into `main` immediately — do not wait for
a manual merge step. Leave the branch in place after merge; do not delete it.

The point of this workflow is that everything reaches `main` — a branch
that never gets a PR opened, or a PR that never gets merged, is a failure
of this rule, not a valid alternative to it. Don't let work sit stranded.

#### Memory — runtime infrastructure (references aesop-xi)

The whole stack's runtime memory infrastructure (mem0, terrestrial-brain,
OmniRoute, reasoning-bank, continual-harness) lives canonically in
**aesop-xi** — see `~/repos/aesop-xi/AGENTS.md` §Runtime memory stack.
Not duplicated here.

Every agent in this repo — regardless of harness (Claude Code, Codex, dsh,
Prime Agent, Hermes) — reaches memory via one MCP endpoint:
`http://localhost:20128/mcp` (OmniRoute). Never call mem0 or
terrestrial-brain directly; that bypasses OmniRoute's async memory tap
and the observation layer.

**Bootstrap this repo**: `bash tools/bootstrap.sh` — thin wrapper that
calls aesop-xi's canonical bootstrap first.

---

## NovAExopia  (`AGENTS.md` @ e75ac92)

### NovÆxopia — tools, harness, and engine layer

Canon name: **NovÆxopia**. Repo name: `NovAExopia`. See `NovAExorpus/NAMING-CANON.md`.

#### What this is

The action surface of the Æsop-Xi stack — what the agent (NovÆxenti) can
actually do. Contains inference engine configs, model weight management,
runtime definitions, and tool-skill wiring. Supersedes the earlier "Omni Claw"
/ "NovA-Claw" / "NovÆcopia" naming.

#### Stack position

```
Æsop-Xi          infrastructure (MCPs, hooks, memory, routing, protocols)
  └─ NovÆxenti   agent logic — executor + query cores
       └─ NovÆxopia   tools, harness, engine (this repo)
            ├─ Æsc         terminal daemon
            └─ Æyre        voice / vision daemon
```

#### Conventions

- `daemons/` — shell daemon and media daemon lifecycle configs, IPC contracts.
- `runtimes/` — how a model is loaded and served (llama.cpp, QAIRT, ONNX, etc.).
- `tool-skills/` — tool/skill wiring per inference backend (was `engines/`).
- Weight manifests in `weights/` — model metadata, quantization specs, device
  compatibility. Actual weight files are NOT stored in git.
- `config/` holds cross-cutting settings (temperature defaults, token limits,
  routing rules).
- `manifest.jsonl` is the machine-readable index.

#### Operator Rule 1 — no action without an explicit prompt

A skipped or unanswered question is NOT consent. No action — reading,
searching, or anything else — without an explicit prompt or permitted
request. State-changing or not, it doesn't matter.

#### Operator Rule 2 — read this file and RESUME.md first

Before doing anything else in this repo, read this AGENTS.md and RESUME.md.
Standing convention across the operator's repos for months — step one,
every session, no exceptions.

#### Git workflow

PR required. No direct pushes to main. CI runs gitleaks + structure check.
Before every push, scan the diff for secrets/keys and refuse to push if any
are found. On green CI, auto-merge into `main` immediately — do not wait for
a manual merge step. Leave the branch in place after merge; do not delete it.

The point of this workflow is that everything reaches `main` — a branch
that never gets a PR opened, or a PR that never gets merged, is a failure
of this rule, not a valid alternative to it. Don't let work sit stranded.

#### Memory — runtime infrastructure (references aesop-xi)

The whole stack's runtime memory infrastructure (mem0, terrestrial-brain,
OmniRoute, reasoning-bank, continual-harness) lives canonically in
**aesop-xi** — see `~/repos/aesop-xi/AGENTS.md` §Runtime memory stack.
Not duplicated here.

Every agent in this repo — regardless of harness (Claude Code, Codex, dsh,
Prime Agent, Hermes) — reaches memory via one MCP endpoint:
`http://localhost:20128/mcp` (OmniRoute). Never call mem0 or
terrestrial-brain directly; that bypasses OmniRoute's async memory tap
and the observation layer.

**Bootstrap this repo**: `bash tools/bootstrap.sh` — thin wrapper that
calls aesop-xi's canonical bootstrap first.

---

## Hyperion-XI  (`AGENTS.md` @ 309f494)

### Horizons UI — master visual presentation shell

Canon name: **Horizons UI**. Rebuilt from scratch 2026-09-15 — the prior
38-PR history (broken NPU-runtime architecture, half-finished GenieX
migration) is archived, not carried forward. Full history + last snapshot:
`raw-databank/horizons-ui-full-history.bundle` and `raw-databank/horizons-ui-full/`.
Salvage rationale and post-mortem: `raw-databank/README-SALVAGE.md`.

#### What this is

Part of the 3-APK architecture alongside Æsc (terminal) and Æyre (voice/vision).
See `NovAExorpus/NAMING-CANON.md`.

#### Operator Rule 1 — no action without an explicit prompt

A skipped or unanswered question is NOT consent. No action — reading,
searching, or anything else — without an explicit prompt or permitted
request. State-changing or not, it doesn't matter.

#### Operator Rule 2 — read this file and RESUME.md first

Before doing anything else in this repo, read this AGENTS.md and RESUME.md.
Standing convention across the operator's repos for months — step one,
every session, no exceptions.

#### Git workflow

PR required. No direct pushes to main. Before every push, scan the diff for
secrets/keys and refuse to push if any are found. On green CI, auto-merge
into `main` immediately. Leave the branch in place after merge; do not delete it.

The point of this workflow is that everything reaches `main` — a branch
that never gets a PR opened, or a PR that never gets merged, is a failure
of this rule, not a valid alternative to it. Don't let work sit stranded.

#### Memory — runtime infrastructure (references aesop-xi)

The whole stack's runtime memory infrastructure (mem0, terrestrial-brain,
OmniRoute, reasoning-bank, continual-harness) lives canonically in
**aesop-xi** — see `~/repos/aesop-xi/AGENTS.md` §Runtime memory stack.
Not duplicated here.

Every agent in this repo — regardless of harness (Claude Code, Codex, dsh,
Prime Agent, Hermes) — reaches memory via one MCP endpoint:
`http://localhost:20128/mcp` (OmniRoute). Never call mem0 or
terrestrial-brain directly; that bypasses OmniRoute's async memory tap
and the observation layer.

**Bootstrap this repo**: `bash tools/bootstrap.sh` — thin wrapper that
calls aesop-xi's canonical bootstrap first.

---

## novus-aesc  (`AGENTS.md` @ 0d121c6)

### Æsc — terminal daemon

Canon name: **Æsc**. Repo name: `novus-aesc`. See `NovAExorpus/NAMING-CANON.md`.

#### What this is

The terminal daemon layer of the Æsop-Xi stack. Provides OS-level shell
access, accessibility services, and Termux-free command execution on Android.
Part of the 3-APK architecture alongside Horizons-Ui and Æyre.

#### Stack position

```
Æsop-Xi → NovÆxenti → NovÆxopia → Æsc (this repo)
                                 → Æyre (voice/vision)
```

Æsc runs independently. Horizons-Ui does NOT require Æsc to function — any
document claiming otherwise is superseded by the naming canon.

#### Conventions

- `laptop-trick-tunnel/` — ADB-to-WebSocket local Unix host bridge logic.
- `npu-watchdog/` — real-time Genie SDK thermal and OOM monitoring loop.
- Protocol specs in `protocol/` — daemon lifecycle, IPC contract, permissions.
- Reference docs in `docs/` — Android accessibility API notes, shell execution
  patterns.
- Salvaged material in `salvage/` — content from earlier "Æsh" / "daemon.aexenti"
  designs, preserved for reference.

#### Operator Rule 1 — no action without an explicit prompt

A skipped or unanswered question is NOT consent. No action — reading,
searching, or anything else — without an explicit prompt or permitted
request. State-changing or not, it doesn't matter.

#### Operator Rule 2 — read this file and RESUME.md first

Before doing anything else in this repo, read this AGENTS.md and RESUME.md.
Standing convention across the operator's repos for months — step one,
every session, no exceptions.

#### Git workflow

PR required. No direct pushes to main. CI runs gitleaks + structure check.
Before every push, scan the diff for secrets/keys and refuse to push if any
are found. On green CI, auto-merge into `main` immediately — do not wait for
a manual merge step. Leave the branch in place after merge; do not delete it.

The point of this workflow is that everything reaches `main` — a branch
that never gets a PR opened, or a PR that never gets merged, is a failure
of this rule, not a valid alternative to it. Don't let work sit stranded.

#### Memory — runtime infrastructure (references aesop-xi)

The whole stack's runtime memory infrastructure (mem0, terrestrial-brain,
OmniRoute, reasoning-bank, continual-harness) lives canonically in
**aesop-xi** — see `~/repos/aesop-xi/AGENTS.md` §Runtime memory stack.
Not duplicated here.

Every agent in this repo — regardless of harness (Claude Code, Codex, dsh,
Prime Agent, Hermes) — reaches memory via one MCP endpoint:
`http://localhost:20128/mcp` (OmniRoute). Never call mem0 or
terrestrial-brain directly; that bypasses OmniRoute's async memory tap
and the observation layer.

**Bootstrap this repo**: `bash tools/bootstrap.sh` — thin wrapper that
calls aesop-xi's canonical bootstrap first.

---

## novus-aeyre  (`AGENTS.md` @ 70677f1)

### Æyre — voice and vision daemon

Canon name: **Æyre**. Repo name: `novus-aeyre`. See `NovAExorpus/NAMING-CANON.md`.

#### What this is

The voice and vision daemon layer of the Æsop-Xi stack. Handles STT
(Moonshine/Whisper), TTS (Kokoro/termux-tts-speak), VAD (Silero), and
screen-vision context capture. Part of the 3-APK architecture alongside
Horizons-Ui and Æsc.

#### Stack position

```
Æsop-Xi → NovÆxenti → NovÆxopia → Æsc (terminal)
                                 → Æyre (this repo)
```

Æyre runs independently. Horizons-Ui does NOT require Æyre to function.

#### Conventions

- `screen-vision/` — real-time pixel canvas parsing and vision capture.
- `voice-ast-stack/` — native low-latency VAD, TTS, and STT pipelines.
- Protocol specs in `protocol/` — media daemon lifecycle, audio pipeline
  contract, VAD thresholds, TTS streaming.
- Reference docs in `docs/` — Moonshine/Kokoro setup, Silero VAD integration,
  screen-vision API, device profiles (Razr Ultra NPU vs Tab S9 vs base).

#### Operator Rule 1 — no action without an explicit prompt

A skipped or unanswered question is NOT consent. No action — reading,
searching, or anything else — without an explicit prompt or permitted
request. State-changing or not, it doesn't matter.

#### Operator Rule 2 — read this file and RESUME.md first

Before doing anything else in this repo, read this AGENTS.md and RESUME.md.
Standing convention across the operator's repos for months — step one,
every session, no exceptions.

#### Git workflow

PR required. No direct pushes to main. CI runs gitleaks + structure check.
Before every push, scan the diff for secrets/keys and refuse to push if any
are found. On green CI, auto-merge into `main` immediately — do not wait for
a manual merge step. Leave the branch in place after merge; do not delete it.

The point of this workflow is that everything reaches `main` — a branch
that never gets a PR opened, or a PR that never gets merged, is a failure
of this rule, not a valid alternative to it. Don't let work sit stranded.

#### Memory — runtime infrastructure (references aesop-xi)

The whole stack's runtime memory infrastructure (mem0, terrestrial-brain,
OmniRoute, reasoning-bank, continual-harness) lives canonically in
**aesop-xi** — see `~/repos/aesop-xi/AGENTS.md` §Runtime memory stack.
Not duplicated here.

Every agent in this repo — regardless of harness (Claude Code, Codex, dsh,
Prime Agent, Hermes) — reaches memory via one MCP endpoint:
`http://localhost:20128/mcp` (OmniRoute). Never call mem0 or
terrestrial-brain directly; that bypasses OmniRoute's async memory tap
and the observation layer.

**Bootstrap this repo**: `bash tools/bootstrap.sh` — thin wrapper that
calls aesop-xi's canonical bootstrap first.
