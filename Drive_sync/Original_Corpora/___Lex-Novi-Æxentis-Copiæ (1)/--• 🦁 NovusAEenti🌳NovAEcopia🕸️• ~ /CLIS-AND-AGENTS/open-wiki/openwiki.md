# OpenWiki — Repository Reference

Source: `/home/user/openwiki` (fork of `langchain-ai/openwiki`, this checkout's `origin` → `c10vis-poem/openwiki`). Category: **runtime / CLI tool** (doc-generation agent), not a memory system.

## 1. What it actually is

OpenWiki is a **TypeScript CLI that writes and maintains documentation for a codebase, built to be read by other coding agents.** It's a LangChain-ecosystem tool (`deepagents` + `langchain`/`@langchain/*`) that runs an LLM-driven documentation agent against a target repo and produces/maintains a tree of Markdown docs under `openwiki/` in that repo.

Three modes:
- `--init` — generate docs from scratch
- `--update` — refresh docs based on the git diff since the last run
- `chat` — interactive mode
- `-p/--print` — one-shot mode

It self-installs a pointer block into the host repo's `AGENTS.md`/`CLAUDE.md` so other agents know to read `openwiki/quickstart.md` first.

**Important**: this particular checkout is a downstream fork, not vanilla upstream. Its own git history shows "docs: add openwiki's own SKILL.md — dogfood the feature as a focal persistence layer" and "feat: project-scoped openwiki/SKILL.md for per-repo customization." `openwiki/SKILL.md` in this fork explicitly frames that addition as "memory as a skill" and calls it the fork's focal architecture.

## 2. Repo structure

| Path | Purpose |
|---|---|
| `CLAUDE.md`, `AGENTS.md` | Identical pointer files: "docs live in `/openwiki`, start at `openwiki/quickstart.md`" |
| `README.md` | Install/usage/customization, incl. the SKILL.md convention |
| `DEVELOPMENT.md` | Local dev/link instructions (pnpm) |
| `openwiki/` | The generated wiki itself — `quickstart.md`, `architecture/overview.md`, `agent/workflow.md`, `cli/usage.md`, `operations/credentials-and-updates.md`, `SKILL.md`, `.last-update.json` |
| `src/cli.tsx` | Ink UI, run lifecycle, auto-exit |
| `src/commands.ts` | argv parsing/help |
| `src/credentials.tsx` | onboarding |
| `src/env.ts` | `~/.openwiki/.env` persistence/diagnostics |
| `src/constants.ts` | provider configs, path constants, validation |
| `src/agent/index.ts` | agent runtime/model creation |
| `src/agent/prompt.ts` | system/user prompt assembly (the actual maintenance rulebook lives here) |
| `src/agent/utils.ts` | git evidence + content-hash snapshot + metadata writes |
| `src/agent/types.ts` | shared types |
| `.github/workflows/checks.yml` | lint/format CI |
| `.github/workflows/openwiki-update.yml`, `examples/openwiki-update.yml` | copyable scheduled-update GitHub Action |

## 3. The schema/config layer for wiki maintenance

Two mechanisms, layered:

1. **`CLAUDE.md`/`AGENTS.md`** — generic, auto-inserted pointer block any agent reads first (templated in `src/agent/prompt.ts` ~lines 92-105).
2. **`openwiki/SKILL.md`** — per-repo, optional, project-scoped override, read on *every* run (chat, `--init`, `--update`). Layers project conventions/terminology/scope on top of built-in behavior without forking OpenWiki's own code. Cannot override security rules or the "only write inside `openwiki/`" restriction. Called "memory as a skill" in-repo.

The actual maintenance rulebook is `createSystemPrompt()`/`createModeInstructions()` in `src/agent/prompt.ts` — governs structure (quickstart-first, ≤8 pages on init, no thin stub pages), git-evidence discipline, subagent fan-out rules, and a "surgical update" policy (only touch pages tied to real diffs).

## 4. Memory / retrieval / RAG / MCP surface

**None.** Confirmed via repo-wide grep for `websocket|embedding|RAG|retriev|MCP|vector|memory` — only hits are the SKILL.md "memory as a skill" prose. What it does have as persistence primitives:

- **SQLite checkpointer** (`~/.openwiki/openwiki.sqlite`, `@langchain/langgraph-checkpoint-sqlite`) — persists LangGraph conversation threads for chat continuity, not a knowledge base.
- **`openwiki/.last-update.json`** — run metadata (`updatedAt`, `command`, `gitHead`, `model`) scoping incremental updates.
- **Content-hash snapshot** (`createOpenWikiContentSnapshot()`) — SHA-256 over `openwiki/` to detect no-op updates.
- **DeepAgents `LocalShellBackend`** (`virtualMode: true`) — the agent execution substrate. No MCP, no external tool integration beyond LangChain model providers (Anthropic/OpenAI/OpenRouter/Baseten/Fireworks).
- Optional LangSmith tracing for observability, not memory.

## 5. Testing/tooling

No test suite at all. Quality gates are static only: `.github/workflows/checks.yml` runs `pnpm run format:check` (Prettier) + `pnpm run lint:check` (ESLint). Build via `tsc`; dev loop via `tsx src/cli.tsx` or `OPENWIKI_DEV=1 openwiki --dry-run`.

## 6. Extensibility as a base layer

Two seams make OpenWiki plausible as a fork-base for a larger system:

1. **`openwiki/SKILL.md`** — already the natural injection point for behavioral rules from other systems (e.g. OB1, reasoning-bank) without touching `src/`.
2. **`src/constants.ts` provider abstraction** (`PROVIDER_CONFIGS`, `OpenWikiProvider`, `createModel()`) — clean pattern for adding new backends, mirrorable for adding new memory backends or transport channels.

But OpenWiki's core loop is narrowly a **doc-generation CLI** — git-evidence-driven, file-snapshot-gated, LangGraph/DeepAgents-specific, no runtime API/server. There's no WebSocket, HTTP server, or plugin/hook system here today. Forking on it gets you the prompt-discipline/doc-structure conventions, the SKILL.md layering convention, and the metadata/snapshot pattern — the websocket/frontend interface layer itself would be new code.

## Key file paths
- `/home/user/openwiki/CLAUDE.md`, `/home/user/openwiki/AGENTS.md`
- `/home/user/openwiki/README.md`, `/home/user/openwiki/DEVELOPMENT.md`
- `/home/user/openwiki/openwiki/quickstart.md`
- `/home/user/openwiki/openwiki/SKILL.md`
- `/home/user/openwiki/openwiki/architecture/overview.md`
- `/home/user/openwiki/openwiki/agent/workflow.md`
- `/home/user/openwiki/openwiki/cli/usage.md`
- `/home/user/openwiki/openwiki/operations/credentials-and-updates.md`
- `/home/user/openwiki/src/agent/prompt.ts`
- `/home/user/openwiki/src/constants.ts`
- `/home/user/openwiki/.github/workflows/checks.yml`, `/home/user/openwiki/examples/openwiki-update.yml`
