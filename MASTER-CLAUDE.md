# Master CLAUDE.md overview (auto-generated — do not hand-edit)

Regenerated: 2026-09-15T22:08:32Z
Source: NovAExorpus/tools/regenerate_masters.sh

One overview across every attached project. Edit each project's own
CLAUDE.md, not this file — it's rebuilt from those every time.

---

## NovAExopia

# NovÆxopia — tools, harness, and engine layer

Canon name: **NovÆxopia**. Repo name: `NovAExopia`. See `NovAExorpus/NAMING-CANON.md`.

## What this is

The action surface of the Æsop-Xi stack — what the agent (NovÆxenti) can
actually do. Contains inference engine configs, model weight management,
runtime definitions, and tool-skill wiring. Supersedes the earlier "Omni Claw"
/ "NovA-Claw" / "NovÆcopia" naming.

## Stack position

```
Æsop-Xi          infrastructure (MCPs, hooks, memory, routing, protocols)
  └─ NovÆxenti   agent logic — executor + query cores
       └─ NovÆxopia   tools, harness, engine (this repo)
            ├─ Æsc         terminal daemon
            └─ Æyre        voice / vision daemon
```

## Conventions

- `daemons/` — shell daemon and media daemon lifecycle configs, IPC contracts.
- `runtimes/` — how a model is loaded and served (llama.cpp, QAIRT, ONNX, etc.).
- `tool-skills/` — tool/skill wiring per inference backend (was `engines/`).
- Weight manifests in `weights/` — model metadata, quantization specs, device
  compatibility. Actual weight files are NOT stored in git.
- `config/` holds cross-cutting settings (temperature defaults, token limits,
  routing rules).
- `manifest.jsonl` is the machine-readable index.

## Operator Rule 1 — no action without an explicit prompt

A skipped or unanswered question is NOT consent. No action — reading,
searching, or anything else — without an explicit prompt or permitted
request. State-changing or not, it doesn't matter.

## Operator Rule 2 — read this file and RESUME.md first

Before doing anything else in this repo, read this CLAUDE.md and RESUME.md.
Standing convention across the operator's repos for months — step one,
every session, no exceptions.

## Git workflow

PR required. No direct pushes to main. CI runs gitleaks + structure check.
Before every push, scan the diff for secrets/keys and refuse to push if any
are found. On green CI, auto-merge into `main` immediately — do not wait for
a manual merge step. Leave the branch in place after merge; do not delete it.

The point of this workflow is that everything reaches `main` — a branch
that never gets a PR opened, or a PR that never gets merged, is a failure
of this rule, not a valid alternative to it. Don't let work sit stranded.

## Memory — runtime infrastructure (references aesop-xi)

The whole stack's runtime memory infrastructure (mem0, terrestrial-brain,
OmniRoute, reasoning-bank, continual-harness) lives canonically in
**aesop-xi** — see `~/repos/aesop-xi/CLAUDE.md` §Runtime memory stack.
Not duplicated here.

Every agent in this repo — regardless of harness (Claude Code, Codex, dsh,
Prime Agent, Hermes) — reaches memory via one MCP endpoint:
`http://localhost:20128/mcp` (OmniRoute). Never call mem0 or
terrestrial-brain directly; that bypasses OmniRoute's async memory tap
and the observation layer.

**Bootstrap this repo**: `bash tools/bootstrap.sh` — thin wrapper that
calls aesop-xi's canonical bootstrap first.

---

## NovAExorpus

# CLAUDE.md — NovAExorpus (Claude Code only)

Repository: `NovAExorpus` — NovÆxorpus Federated Master Corpus Root.

Tool-agnostic rules (apply to every engine, not just Claude Code) live in
`AGENTS.md` — read that first, every session.

## Meta-skill activation

Invoke the `task-observer` skill (`.claude/skills/task-observer/`) before
the first tool call of any session and before writing or proposing a plan.
Description matching alone under-triggers it — this line is the enforceable
trigger.

## MCP servers

Defined in `.mcp.json` at repo root: `mem0` (memory) and `terrestrial-brain`
(corpus knowledge base). Both take their endpoint/credentials from env vars
— see `.mcp.json` for the exact variable names. Set them locally; never
commit values.

## Memory — runtime infrastructure (references aesop-xi)

The whole stack's runtime memory infrastructure (mem0, terrestrial-brain,
OmniRoute, reasoning-bank, continual-harness) lives canonically in
**aesop-xi** — see `~/repos/aesop-xi/CLAUDE.md` §Runtime memory stack.
Not duplicated here.

Every agent in this repo — regardless of harness (Claude Code, Codex, dsh,
Prime Agent, Hermes) — reaches memory via one MCP endpoint:
`http://localhost:20128/mcp` (OmniRoute). Never call mem0 or
terrestrial-brain directly; that bypasses OmniRoute's async memory tap
and the observation layer.

**Bootstrap this repo**: `bash tools/bootstrap.sh` — thin wrapper that
calls aesop-xi's canonical bootstrap first.

---

## aesop-xi

# Æsop-Xi — repo conventions for Claude Code

[IF THIS HAS CHANGED SINCE 9-01-2026 THIS DOCUMENT NEEDS TO BE UPDATED TO REFLECT THAT] 

Applies to any Claude Code session working in this repo, regardless of which
session or model. Created 2026-08-31
— previously nonexistent despite RESUME.md
implying a handoff process was already in place.

## Operator Rule 1 — no action without an explicit prompt

A skipped or unanswered question is NOT consent. No action — reading,
searching, or anything else — without an explicit prompt or permitted
request. State-changing or not, it doesn't matter.

## Operator Rule 2 — read this file and RESUME.md first

Before doing anything else in this repo, read this CLAUDE.md and RESUME.md.
Standing convention across the operator's repos for months — step one,
every session, no exceptions. (Complements the session-handoff workflow below.)

## Session handoff workflow

- **`RESUME.md` is fully rewritten at the end of every session** — never appended
  to. It is a snapshot of current state, not a running log. (The pre-2026-08-31
  version had grown to 300 lines across many sessions and contained literal
  unresolved git conflict markers from a stash that was never cleanly finished —
  that's what happens when this rule isn't followed.)
- **Repo-specific unaddressed items go into `PENDING.md`** at repo root, not
  into RESUME.md. `PENDING.md` is a durable, cross-session backlog — items
  persist until resolved or explicitly dropped, and it is NOT rewritten each
  session the way RESUME.md is. Cross-repo backlog lives at
  `~/repos/NovAExorpus/unresolved.md` (the per-repo `unresolved.md` is a stub
  pointer only).
- **Review open `PENDING.md` items with the user early in a session** that
  touches this repo, rather than silently carrying them forward or silently
  dropping them.
- `RESUME.md` may point to specific `PENDING.md` items when they're relevant to
  the immediate next session; `PENDING.md` remains the permanent home for
  everything else.

## Memory — three separate systems, don't conflate them

- **Dev-process continuity building Æsop-Xi**: this file + `RESUME.md` +
  `PENDING.md`. Operational, about the build process.
- **The finished Æsop-Xi agent's own runtime memory model**: `ARCHITECTURE.md`
  §4 (Declarative / Recall / Strategic / Working-Ephemeral) and
  `protocol/memory.md`. Product architecture spec.
- **The whole stack's runtime memory infrastructure** (the actual mem0 /
  terrestrial-brain / OmniRoute / reasoning-bank services that every agent
  across the 7 base repos consumes): see `## Runtime memory stack` below.
  aesop-xi is the canonical home per the naming canon ("memory layer, context
  formatting, tool and context orchestration, protocols"). The other 6 base
  repos reference this section, they don't duplicate it.

## Runtime memory stack (data plane, canonical here)

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
- **Reasoning Bank** — multi-model execution ledger, crash recovery
  (resume from step N+1 if killed at N); JSON KV under `tools/reasoning_bank/`
- **Continual Harness** — reset-free self-improvement loop with rollback

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
Runs on session start via CLAUDE.md instruction, git post-checkout hook,
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

## Termux/Android platform gap — the general fix (2026-09-06)

`bootstrap-stack.sh` (retired 2026-09-15, replaced by `tools/bootstrap.sh`)'s Android
failures (code-review-graph, notebooklm-py/Playwright,
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

## Discovered assets (2026-08-30/31) — previously unused, now catalogued

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
  novae-xorpus.

## Git workflow — PR required, no direct pushes to main

Push changes to a branch, open a PR, let the `CI` GitHub Action run, merge
once it's green (`allow_auto_merge` is on, so this can auto-merge with no
manual click). Do not `git push origin main` directly for code changes.
Before every push, scan the diff for secrets/keys and refuse to push if any
are found. Leave the branch in place after merge; do not delete it.

The point of this workflow is that everything reaches `main` — a branch
that never gets a PR opened, or a PR that never gets merged, is a failure
of this rule, not a valid alternative to it. Don't let work sit stranded.

## Scoping note

This file only loads automatically when a session's working directory is inside
this repo. A session started elsewhere (e.g. `~/downloads`) will not see it or
`RESUME.md`/`unresolved.md` unless it's explicitly pointed here.

---

## horizons-ui

# Horizons UI — master visual presentation shell

Canon name: **Horizons UI**. Rebuilt from scratch 2026-09-15 — the prior
38-PR history (broken NPU-runtime architecture, half-finished GenieX
migration) is archived, not carried forward. Full history + last snapshot:
`raw-databank/horizons-ui-full-history.bundle` and `raw-databank/horizons-ui-full/`.
Salvage rationale and post-mortem: `raw-databank/README-SALVAGE.md`.

## What this is

Part of the 3-APK architecture alongside Æsc (terminal) and Æyre (voice/vision).
See `NovAExorpus/NAMING-CANON.md`.

## Operator Rule 1 — no action without an explicit prompt

A skipped or unanswered question is NOT consent. No action — reading,
searching, or anything else — without an explicit prompt or permitted
request. State-changing or not, it doesn't matter.

## Operator Rule 2 — read this file and RESUME.md first

Before doing anything else in this repo, read this CLAUDE.md and RESUME.md.
Standing convention across the operator's repos for months — step one,
every session, no exceptions.

## Git workflow

PR required. No direct pushes to main. Before every push, scan the diff for
secrets/keys and refuse to push if any are found. On green CI, auto-merge
into `main` immediately. Leave the branch in place after merge; do not delete it.

The point of this workflow is that everything reaches `main` — a branch
that never gets a PR opened, or a PR that never gets merged, is a failure
of this rule, not a valid alternative to it. Don't let work sit stranded.

## Memory — runtime infrastructure (references aesop-xi)

The whole stack's runtime memory infrastructure (mem0, terrestrial-brain,
OmniRoute, reasoning-bank, continual-harness) lives canonically in
**aesop-xi** — see `~/repos/aesop-xi/CLAUDE.md` §Runtime memory stack.
Not duplicated here.

Every agent in this repo — regardless of harness (Claude Code, Codex, dsh,
Prime Agent, Hermes) — reaches memory via one MCP endpoint:
`http://localhost:20128/mcp` (OmniRoute). Never call mem0 or
terrestrial-brain directly; that bypasses OmniRoute's async memory tap
and the observation layer.

**Bootstrap this repo**: `bash tools/bootstrap.sh` — thin wrapper that
calls aesop-xi's canonical bootstrap first.

---

## novus-aesc

# Æsc — terminal daemon

Canon name: **Æsc**. Repo name: `novus-aesc`. See `NovAExorpus/NAMING-CANON.md`.

## What this is

The terminal daemon layer of the Æsop-Xi stack. Provides OS-level shell
access, accessibility services, and Termux-free command execution on Android.
Part of the 3-APK architecture alongside Horizons-Ui and Æyre.

## Stack position

```
Æsop-Xi → NovÆxenti → NovÆxopia → Æsc (this repo)
                                 → Æyre (voice/vision)
```

Æsc runs independently. Horizons-Ui does NOT require Æsc to function — any
document claiming otherwise is superseded by the naming canon.

## Conventions

- `laptop-trick-tunnel/` — ADB-to-WebSocket local Unix host bridge logic.
- `npu-watchdog/` — real-time Genie SDK thermal and OOM monitoring loop.
- Protocol specs in `protocol/` — daemon lifecycle, IPC contract, permissions.
- Reference docs in `docs/` — Android accessibility API notes, shell execution
  patterns.
- Salvaged material in `salvage/` — content from earlier "Æsh" / "daemon.aexenti"
  designs, preserved for reference.

## Operator Rule 1 — no action without an explicit prompt

A skipped or unanswered question is NOT consent. No action — reading,
searching, or anything else — without an explicit prompt or permitted
request. State-changing or not, it doesn't matter.

## Operator Rule 2 — read this file and RESUME.md first

Before doing anything else in this repo, read this CLAUDE.md and RESUME.md.
Standing convention across the operator's repos for months — step one,
every session, no exceptions.

## Git workflow

PR required. No direct pushes to main. CI runs gitleaks + structure check.
Before every push, scan the diff for secrets/keys and refuse to push if any
are found. On green CI, auto-merge into `main` immediately — do not wait for
a manual merge step. Leave the branch in place after merge; do not delete it.

The point of this workflow is that everything reaches `main` — a branch
that never gets a PR opened, or a PR that never gets merged, is a failure
of this rule, not a valid alternative to it. Don't let work sit stranded.

## Memory — runtime infrastructure (references aesop-xi)

The whole stack's runtime memory infrastructure (mem0, terrestrial-brain,
OmniRoute, reasoning-bank, continual-harness) lives canonically in
**aesop-xi** — see `~/repos/aesop-xi/CLAUDE.md` §Runtime memory stack.
Not duplicated here.

Every agent in this repo — regardless of harness (Claude Code, Codex, dsh,
Prime Agent, Hermes) — reaches memory via one MCP endpoint:
`http://localhost:20128/mcp` (OmniRoute). Never call mem0 or
terrestrial-brain directly; that bypasses OmniRoute's async memory tap
and the observation layer.

**Bootstrap this repo**: `bash tools/bootstrap.sh` — thin wrapper that
calls aesop-xi's canonical bootstrap first.

---

## novus-aexenti

# NovÆxenti — agent logic layer

Canon name: **NovÆxenti**. Repo name: `novus-aexenti`. See `NovAExorpus/NAMING-CANON.md`.

## What this is

The agent intelligence layer of the Æsop-Xi stack. Houses executor-core (task
execution agents, mode definitions) and query-core (meta-prompt compilation,
intent classification). This is the "brain" — Æsop-Xi is the infrastructure it
runs on, NovÆxopia is the action surface it drives.

## Stack position

```
Æsop-Xi          infrastructure (MCPs, hooks, memory, routing, protocols)
  └─ NovÆxenti   agent logic (this repo) — executor + query cores
       └─ NovÆxopia   tools, harness, engine — what the agent can do
            ├─ Æsc         terminal daemon
            └─ Æyre        voice / vision daemon
```

NovÆxorpus (NovAExorpus) is the data bank — orthogonal to this stack, feeds
all layers.

## Conventions

- `executor-core/` — small-model task execution agents (0.8B executor,
  file-administrator, NPU inference manager, frontier callers).
- `query-core/` — large-model query/reasoning agents (9B query, oeracle,
  IT helpdesk).
- `node-beta-swarm/` — Node Beta home-node agents (cross-auditor,
  home-assistant, red-auditor, trend-scraper, web-ingestion).
- Harness configs in `harnesses/` define how an agent runtime is invoked.
- Mode definitions in `modes/` describe behavioral presets.
- `manifest.jsonl` is the machine-readable index — regenerate, don't hand-edit.

## Operator Rule 1 — no action without an explicit prompt

A skipped or unanswered question is NOT consent. No action — reading,
searching, or anything else — without an explicit prompt or permitted
request. State-changing or not, it doesn't matter.

## Operator Rule 2 — read this file and RESUME.md first

Before doing anything else in this repo, read this CLAUDE.md and RESUME.md.
Standing convention across the operator's repos for months — step one,
every session, no exceptions.

## Git workflow

PR required. No direct pushes to main. CI runs gitleaks + structure check.
Before every push, scan the diff for secrets/keys and refuse to push if any
are found. On green CI, auto-merge into `main` immediately — do not wait for
a manual merge step. Leave the branch in place after merge; do not delete it.

The point of this workflow is that everything reaches `main` — a branch
that never gets a PR opened, or a PR that never gets merged, is a failure
of this rule, not a valid alternative to it. Don't let work sit stranded.

## Memory — runtime infrastructure (references aesop-xi)

The whole stack's runtime memory infrastructure (mem0, terrestrial-brain,
OmniRoute, reasoning-bank, continual-harness) lives canonically in
**aesop-xi** — see `~/repos/aesop-xi/CLAUDE.md` §Runtime memory stack.
Not duplicated here.

Every agent in this repo — regardless of harness (Claude Code, Codex, dsh,
Prime Agent, Hermes) — reaches memory via one MCP endpoint:
`http://localhost:20128/mcp` (OmniRoute). Never call mem0 or
terrestrial-brain directly; that bypasses OmniRoute's async memory tap
and the observation layer.

**Bootstrap this repo**: `bash tools/bootstrap.sh` — thin wrapper that
calls aesop-xi's canonical bootstrap first.

---

## novus-aeyre

# Æyre — voice and vision daemon

Canon name: **Æyre**. Repo name: `novus-aeyre`. See `NovAExorpus/NAMING-CANON.md`.

## What this is

The voice and vision daemon layer of the Æsop-Xi stack. Handles STT
(Moonshine/Whisper), TTS (Kokoro/termux-tts-speak), VAD (Silero), and
screen-vision context capture. Part of the 3-APK architecture alongside
Horizons-Ui and Æsc.

## Stack position

```
Æsop-Xi → NovÆxenti → NovÆxopia → Æsc (terminal)
                                 → Æyre (this repo)
```

Æyre runs independently. Horizons-Ui does NOT require Æyre to function.

## Conventions

- `screen-vision/` — real-time pixel canvas parsing and vision capture.
- `voice-ast-stack/` — native low-latency VAD, TTS, and STT pipelines.
- Protocol specs in `protocol/` — media daemon lifecycle, audio pipeline
  contract, VAD thresholds, TTS streaming.
- Reference docs in `docs/` — Moonshine/Kokoro setup, Silero VAD integration,
  screen-vision API, device profiles (Razr Ultra NPU vs Tab S9 vs base).

## Operator Rule 1 — no action without an explicit prompt

A skipped or unanswered question is NOT consent. No action — reading,
searching, or anything else — without an explicit prompt or permitted
request. State-changing or not, it doesn't matter.

## Operator Rule 2 — read this file and RESUME.md first

Before doing anything else in this repo, read this CLAUDE.md and RESUME.md.
Standing convention across the operator's repos for months — step one,
every session, no exceptions.

## Git workflow

PR required. No direct pushes to main. CI runs gitleaks + structure check.
Before every push, scan the diff for secrets/keys and refuse to push if any
are found. On green CI, auto-merge into `main` immediately — do not wait for
a manual merge step. Leave the branch in place after merge; do not delete it.

The point of this workflow is that everything reaches `main` — a branch
that never gets a PR opened, or a PR that never gets merged, is a failure
of this rule, not a valid alternative to it. Don't let work sit stranded.

## Memory — runtime infrastructure (references aesop-xi)

The whole stack's runtime memory infrastructure (mem0, terrestrial-brain,
OmniRoute, reasoning-bank, continual-harness) lives canonically in
**aesop-xi** — see `~/repos/aesop-xi/CLAUDE.md` §Runtime memory stack.
Not duplicated here.

Every agent in this repo — regardless of harness (Claude Code, Codex, dsh,
Prime Agent, Hermes) — reaches memory via one MCP endpoint:
`http://localhost:20128/mcp` (OmniRoute). Never call mem0 or
terrestrial-brain directly; that bypasses OmniRoute's async memory tap
and the observation layer.

**Bootstrap this repo**: `bash tools/bootstrap.sh` — thin wrapper that
calls aesop-xi's canonical bootstrap first.

