# claude-mem as the memory server: first breakdown (2026-11-13 05:0x, session 8e3a65ec)

Owner, 04:57: claude-mem becomes the new memory server, run from our own MCP, replaces ~90% of the current memory
plugin, stripped of what we don't need; stop hooks force every memory layer, tool and skill 100% of the time.
Frozen as claim 846bdf4e. Clone: ~/repos/NvAEx-claude-mem, commit 0c488b54e (2026-11-12 20:57), version 15.18.3.
Read so far: README.md, AGENTS.md, folder listings, MCP tool names (src/servers/mcp-server.ts), skills, services.
Not read yet: docs/architecture/*, the code of each part.

## Where it runs (owner, 05:00-05:03: Cloudflare over Termux; backups to local, GitHub, Supabase, Docker, phone)
Proposed layers (owner to confirm):
1. Primary: Cloudflare Worker = the memory server + MCP endpoint; D1 = SQLite store; Vectorize = vector search;
   observer model = Workers AI or the owner's Claude/Gemini key. Unverified: D1 FTS5, free-tier limits, hook latency.
2. Live mirror: Supabase Postgres + pgvector (the old server's "supabase_mirror" was never built; global AGENTS.md
   gives each harness its own Supabase).
3. Phone: local SQLite copy, read when offline; writes queue there and flush when back online.
4. GitHub: scheduled export (redacted JSONL + markdown) to the private NvAEx-Recaps memory/ folder.
5. Docker: same Worker code run as a container (local or VM) when Cloudflare is down.
Secrets stripped before any copy leaves the phone (<private> tags + redaction).

## How it works (README "How it fits together")
Hooks on every Claude Code event -> local worker (HTTP, run by Bun) -> an observer model turns tool activity into
observations and a session summary -> SQLite ~/.claude-mem/claude-mem.db (FTS5) + Chroma vectors -> a compact
index injected at SessionStart; details fetched on demand through MCP tools.

## Blockers on this phone (checked)
- Bun: NOT installed (`command -v bun` empty). The worker runs on Bun. Bun on Android/bionic: unproven; fallback is
  the Debian proot (Aesop-Xi AGENTS.md "Termux/Android platform gap").
- Node v26.13.0 (needs >=20.19): ok. uv: installed.
- Observer model: needs one provider: Claude plan, OpenRouter, Gemini key, Codex, or OpenAI-compatible (local Qwen?).

## MCP tools (27): keep candidates
search, timeline, get_observations, get_tool_uses, save_memory, session_start_context, observation_add,
observation_record_event, observation_search, observation_context, observation_generation_status,
work_state_write, work_state_read, smart_search, smart_outline, smart_unfold, dumb_search, important_workflow.
Corpus tools (build/list/prime/query/rebuild/reprime_corpus): owner decides (overlap with the wiki admin).
team_brief, team_search: strip candidates (TeamBrain, hosted).

## Strip candidates (owner approves by name; nothing deleted before that)
- Account and payment: sign-in, magic link, 30-day trial checkout, cmem.ai observer, CMEM token text.
- Telemetry: src/services/telemetry/ (12 files), on by default upstream.
- Cloud sync: src/services/sync/CloudSync.ts, SyncClient.ts and the sync-hub/sync-api services (keep Chroma sync).
- Auto-update: src/services/auto-update/.
- Other-agent packaging we don't use: .cursor-plugin, .grok-plugin, .qoder-plugin, claude-mem-cursor,
  claude-mem-grok-bot, cowork, omp, pi, windsurf/kimi/devin adapters, docker, docs/i18n (31 languages).
  KEEP for our agents: claude-code, codex, gemini, antigravity-cli (AGY), hermes/, dsh/.
- Skills (29): keep mem-search, smart-explore, learn-codebase, handoff, timeline-report, how-it-works; strip
  candidates: release, build-and-release, version-bump, wowerpoint, childhood, oh-my-issues, ccs-align, screenpipe,
  agent-cost-report, cloud-sync, design-is, owner-goals, babysit, standup, weekly-digests, what-the, do,
  make-plan, pathfinder, mode-creator, knowledge-agent, request-progress, backup-setup, build. Each read first.

## What the old memory plugin (nvaex-memory) keeps, the other ~10% (f66841fd: every feature listed, ported or struck)
To list in full next: frozen claims + snapshot, task state, anchor lint, MAP.md smartfolder, recap/weekly roll-up
to NvAEx-Recaps, ccfind, whydone, handoff notes, CAS sha256 ledger, code-review-graph and graphify query.

## Enforcement (the stop hooks), to design after the strip
Every memory layer, tool and skill used in the opening, negotiation and mid-contract: REQUIRE lines the rules
plugin adds itself (e.g. session_start_context + search before work; save_memory / observation_add at each task).
