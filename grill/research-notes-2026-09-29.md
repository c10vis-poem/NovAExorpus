# Research notes — grill session 2026-09-28 → 29

These are facts established this session outside the two read ledgers, each with its source, so nobody has to re-read the sources.
The OB1 facts are in `grill/ob1-read-ledger.md`, the Continual Harness code facts are in `grill/continual-harness-read-ledger.md`, and the decisions are in `grill/DECISIONS.md`.

## OmniRoute

Source: the local clone `~/repos/OmniRoute` @ `2a6de705f` (2026-08-15, v3.8.49; it was not synced with upstream this session): its `AGENTS.md`, `docs/routing/AUTO-COMBO.md` (first ~420 lines), and searches of `src/`, `open-sse/` and `bin/`. The live instance on the VM was not checked, because the `omniroute` MCP config has an invalid URL.

- **Routing is decided by OmniRoute's own configuration**, stored in its SQLite database (`DATA_DIR`, default `~/.omniroute/`).
  - "Combos" are ordered provider/model lists kept in the `combos` table.
  - There are 17–19 strategies (the docs disagree): priority, weighted, fill-first, round-robin, P2C, random, least-used, reset-aware, reset-window, cost-optimized, strict-random, auto, lkgp, context-optimized, context-relay, headroom, fusion.
  - `model: "auto"` and `auto/<category>:<tier>` build a combo for each request and store nothing.
  - Auto scoring weighs health, cost, latency, quota, task fit and so on. The docs say 9, 12 or 13 factors in different places.
- **What worked and what failed:** OmniRoute only knows this at the provider-call level.
  - A circuit breaker per provider (CLOSED/HALF_OPEN/OPEN; OPEN is excluded).
  - LKGP (last-known-good path), cached in `readCache.ts`.
  - Usage, quota and cost tables.
  - An `mcp_audit` table logging every MCP tool call (tool, args, success, API key, time).
  - Nothing judges whether an agent's task succeeded or whether it followed rules.
- **"Continual Harness" and "Reasoning Bank" do not exist in OmniRoute.** A search found 0 hits in src/open-sse/bin. The closest thing is "Reasoning Replay", which only caches `reasoning_content` between turns for DeepSeek, Kimi, Qwen, GLM and MiMo. The planned `observation_log` tool doesn't exist either.
- **OmniRoute has a real plugin system:** `src/lib/plugins/` (hooks.ts, loader.ts, manager.ts, sdk.ts, marketplace.ts). Hooks include `onRequest`, `onResponse` and `onStreamEnd` (hooks.ts:36-45; loader.ts:294). This is what makes "ReasoningBank as an OmniRoute plugin" possible without changing OmniRoute's own code.
- **Protocols:**
  - an MCP server with 104 tools and scoped keys (30–31 scopes), over stdio, SSE and streamable HTTP;
  - A2A v0.3 (JSON-RPC, 6 skills: smartRouting, quotaManagement, providerDiscovery, costAnalysis, healthReport, listCapabilities; Agent Card at `/.well-known/agent.json`);
  - an ACP registry;
  - webhooks (HMAC-signed, auto-disabled after 10 failures);
  - its own memory system (SQLite `memories` table plus a `memory_fts` full-text index, with optional Qdrant; MCP tools memory_search, memory_add and memory_clear);
  - skills, guardrails (PII masking is off by default), and compression (caveman and RTK engines, stackable).
- OmniRoute has no built-in link to mem0, OB1, Graphify or code-review-graph. We wire those.

## ReasoningBank

Source: the fork `~/repos/reasoning-bank` @ `ef1ec9f`: README, `WebArena/autoeval/prompts.py`, `WebArena/prompts/memory_instruction.py`, `WebArena/memory_management.py` (function list), and `third_party/src/minisweagent/memory/{induce_memory.py, instruction.py}`.

- **What it is:** a general method, shown on two benchmarks: WebArena (web browsing) and SWE-Bench (coding).
  - Before a task: retrieve similar past tasks by embedding and inject their lessons.
  - After a task: judge it success or fail, then distil it into at most 3 lessons.
  - Storage: JSONL plus embeddings. The embedding model is `gemini-embedding-001` or Qwen.
  - The README says "for demonstration purposes only".
- **Where the verdict comes from** (`induce_memory.py:175-186`): `criteria="gt"` uses the environment's ground-truth reward, and `criteria="autoeval"` uses the model judge's opinion. The result is binary: success or fail.
- **The web judge** sees the user's intent, the action history, the final state and the agent's reply. It returns success, fail or "task-impossible", with its reasoning. Its rubric covers web tasks only (information seeking, navigation, content modification).
- **Lesson rules** (`memory_instruction.py`):
  - reflect on why the run succeeded or failed first;
  - at most 3 lessons, with no overlap;
  - concrete, actionable steps over abstract principles;
  - keep task-specific names and strings out;
  - each lesson has a title, a "when to use and when NOT to use" line, and 1–3 sentences.
- The model setting (`model_name` "path to the model checkpoint", `model_url`) says which model or file to load. The operator's decision is to keep it and point it at OmniRoute or a local model.
- **No crash recovery:** a search for crash/recover/resume/ledger finds nothing relevant.

## Continual Harness (the paper)

Source: arXiv 2605.09998, HTML version, read through a web-fetch summary (so this is secondhand); the code is being read directly (see its ledger).

- The authors are from Google DeepMind and Princeton, May 2026. The official code is `sethkarten/continual-harness`, MIT licence, forked as `c10vis-poem/AEsops-continual-harness`.
- **The harness has four parts:** system prompt, sub-agents, skills and memory. The meta-tools are define_agent, run_code and process_memory.
- **The loop:** every F steps after a warm-up of W steps, a Refiner (the same model as the agent) reads the recent trajectory window for failure signs: navigation loops, tool-call failures, stalled objectives and missed exploration. It then makes four passes (prompt, sub-agents, skills, memory) of create/update/delete edits. The changes apply immediately, with no reset.
- **The paper describes no rollback;** changes accumulate.
- **Progress is measured against game ground truth:** milestones, and button presses compared with the BFS optimum. There is also a process-reward-model variant.
- **Only tested on Pokémon Red and Emerald.** There is a capability floor: Flash-Lite does worse with it than without it.
- **Relevance:** the Refiner rewrites the agent's own prompt, skills and memory, which is close to the operator's objection to agents writing their own rules. In the code, only the "strategy" prompt is rewritten, never the system prompt (see its ledger).

## Æsop-Xi docs vs today's decisions

Source: `~/repos/aesop-xi/{AGENTS.md, CLAUDE.md, RESUME.md}` (2026-09-15).

1. CLAUDE.md calls ReasoningBank "a multi-model execution ledger, crash recovery (resume from step N+1)". This is wrong and invented; decided today (see DECISIONS).
2. CLAUDE.md calls the Continual Harness "a reset-free self-improvement loop with rollback". That half-matches the paper ("reset-free" is right); "rollback" does not. Still open.
3. AGENTS.md says "never call mem0 or terrestrial-brain directly; all memory access goes through OmniRoute's single MCP endpoint". Today's decision is that each memory layer is its own MCP server. The two can coexist if the servers sit behind OmniRoute, but this has not been decided. Still open.
4. CLAUDE.md lays out folders `skills/omniroute/`, `tools/reasoning_bank/` and `tools/continual_harness/`. The operator wants ReasoningBank in its own folder with subfolders inside Æsop-Xi, holding its judge checklist.
5. The operator said agent-written hard rules like these should never have been written; the memory note `feedback_no_hard_rules_no_canonical` records this.
- The last session's plugin drafts are in `recovered/2026-09-26-ob1/omni-feat/dumbass-plugins/` (reasoning-bank, continual-harness, retrieval-planner), with the orchestration contract (§3.4–3.5). The continual-harness draft is only per-session checkpoints: the last 5 asked/answered pairs, 10 kept, rollback through a header. It does not match the paper.

## Housekeeping facts found this session

- **33 vendor files** in `02_wiki_md/vendors/github/` had been moved into the gitignored nested `NovAExorpus/` folder (byte-identical copies there), so git saw them as deleted. They were restored.
- **PR #23** merged `main` into `happy-ending-unresolved-updates` (the direction was reversed; 1,614 files). **#24**, that branch into `main`, was empty and has been merged. Nothing was lost.
- **ECC was loading every session** from `~/.claude/rules/ecc/` and the ECC block in `~/.claude/CLAUDE.md`, although no ECC plugin or agents were installed. It is now parked at `~/.claude/ecc-parked/`.
- **The local vault `.git` is a leftover.** GitSync syncs through the GitHub API to `vault-sync`.
