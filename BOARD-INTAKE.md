---
title: Board and project-thread intake
date: 2026-10-23
tags: [intake, board, projects]
---

# Board and project-thread intake

Work that belongs to the board of directors, the cloud orchestrator and the per-thread grill sessions (operator, 2026-10-23). Moved here from `PENDING.md` so PENDING only holds what the current session owes. Each thread takes items from here; nothing here is "pending" for a phone session.

## Decisions recorded 2026-10-23 (operator)
- **Repo layout:** NovusAExenti = modular agent packages; NovAExopia = capabilities; Aesop-Xi = orchestration (scripts, hooks, rules, enforcement). The skill stack becomes a customized plugin/mod. No NvAEx-agentk org; the agentk repo folds into this layout.
- **Strip-and-judge strategy:** OmniRoute, mem0, Terrestrial Brain, OB1, ECC and every other third-party stack get broken down by REA/JEV and Fable into extractable assets, then judged: plug in as its own asset/server/marketplace, or fold into our own runtimes, agent packages and modular harnesses (in-session harness customization). No 2.5 GB plugins run whole. ECC is used only as a marketplace for individual skills; no fork maintenance.
- **Grill:** runs as per-thread grill sessions in Claude Projects threads (Fable), monitored by a cloud orchestrator, after the board of directors exists.
- **Dashboard:** Obsidian + graphify combined is the user's dashboard in the agentic OS.
- **Success tracking** belongs to the success-verification grade classifications (cross-agent auditor + orchestration CEO, overseen by the board), not CLAUDE.md.
- **Architecture (operator, repeated ~10 times; logged verbatim 2026-10-23):** files as infrastructure; agents as packages; plugins as configurations; repos as marketplaces; memory, workflows and data extraction designed as skills, scripts and hooks. Agent harnesses and agent packages are modular customizable setups, using Anthropic's own strategies from its customizable mod setup and its dynamic workflow logic, modifiable in session alongside Anthropic's workflows/harnesses. Names for the split beyond "skills/capabilities" still open. Pointers: text in AGENTS.md, enforced/injected by hooks.
- **Apps:** the three APKs are separate apps. Hyperion-XI hosts tiles with plugin connectors that run each app's dashboard, plus webview tiles for any URL. On-device edge-model + voice-stack API (MCP server + HTTP endpoints) is its own runtime/repo that the apps plug into (decide: standalone repo vs inside Hyperion-XI or the terminal APK).
- **Dashboard:** custom (operator has a template), opened in the same browser in a separate window from Obsidian + graphify; both get Android MTP and Chrome DevTools plugins for agent access.
- **llama-server:** not used; build our own server (GenieX C API shim `~/tools/geniex-serve` is the start).
- **Wiki-admin agent package** is where the memory packages, Obsidian skills etc. get their first runs (test and review all: openwiki-for-claude-code, llm-wiki-nocode, headroom, context7, MemVault, claude-mem, agentmemory, oak-memory, pmm, mem0; custom mods/agent packages where needed).
- **Orchestration audit:** every task audited by a subagent auditor (Claude Code Stop `type: "agent"` hook or a reviewer subagent/workflow), plus one full Fable review and an adversarial cross-agent run. Research: `~/.claude/session-work/2026-10-23/anthropic-research-report.md`.
- **Corpus uses pointers**, so syncing other repos' RESUME/AGENTS/MEMORY/PENDING copies into it is moot. `~/.claude/INVENTORY.md` (capability table) moves into the corpus skills/capabilities area as the canonical copy; the phone file becomes a pointer.

## Thread: NPU
- Audit 2026-10-23: `~/.claude/session-work/2026-10-23/npu-audit-report.md` (phone CPU capped during every run; v0.7.1 2.7 tok/s figure invalid; vendor recipes run as adb shell from /data/local/tmp; GenieX v0.9.3 current vs installed v0.3.14/v0.7.1; qairt route half done; models folder `Documents/Models` gone).
- Restart one model at a time with the operator; Qwen 3.5 9B/2B wiring, GenieX HTTP wrapper, npu-serve InternVL/tool calls/multi-image, TFLite/LiteRT + Q4_0 requant, 3-tier bench (`docs/NPU-BENCHMARKS.md`).
- NPU job queue: `NvAEx-Recaps/npu/` + `npu-run` + `npu-queued`, then unattended Qwen 3.5 queue.

## Thread: wiki-admin agent package
- Finish the wiki-admin build as an agent package and install it in NovusAExenti (replaces "corpus re-ingestion"; the RESUME "PHASES 1-4 COMPLETE" claim is stale; 6 repos are pointer stubs; reconcile `NovAExopia/horizons-ui/` with RFMC; QNN-QAIRT SDK and canvas-ui ingestion; `_dumbass_unified-config/`, `9-18-26/`, Continual Harness ledger).
- Inputs: `~/wiki-admin/GRILL-INPUTS.md`, PRIORITY ONE docs, vault 00-10 restructure (dissolve `__RESUME.md/`), one manifest schema, roles 2b-2e, `file_administrator.yaml` / `oracle_helpdesk.yaml`, wiki agent home, Aesop-Xi #6/#8 architecture decisions, Aesop-Xi #18 orchestration contract (merged 2026-10-22; review in its thread).

## Thread: apps (Jetpack Compose, Material 3)
- Voice engine as an in-app API: brief `~/.claude/session-work/2026-10-23/voice-apk-brief.md` (CloviX-AEyre media APK, `:voice-core` + Compose UI, 127.0.0.1 HTTP/WS with token, GitHub Actions build).
- Terminal APK (Android Local Desktop), Horizons 3-APK plan.
- Obsidian plugins: OB1 and OmniRoute plugins under strip-and-judge; push recovered drafts `recovered/2026-09-26-ob1/omni-feat/` and `feat/vm-lifecycle-2026-09-18` only if judged worth keeping.

## Thread: skills and plugins
- Inventory and plan: `~/.claude/session-work/2026-10-23/skills-inventory-report.md` (obsidian-skills, AEsops-obsidian-wiki, openwiki packs, llm-wiki-compiler/nocode, graphify, notebooklm-py, honey, mem0, MemVault, claude-mem, agentmemory, pmm; pick ONE auto-capture memory).
- H7 classifier: tell a mention from a command (obs 0033); point `classify.sh` at a model.
- Missing tools: `htp_partition_calc.py` (never existed), `system_housekeeper.sh.txt`, `compile_manifest.py.md`, `doc_to_skill_and_tool.py.md`: restore or drop references.
- OmniGlyph switch-on decision.
- Unbuilt hook specs (from `skill-updates/2026-10-08/proposals/hooks-spec.md`; mapped against `~/repos/Aesop-Xi/hooks/` 2026-10-23). Parked observations 0005, 0012, 0017 wait on this item.
  - Item 1 (obs 0017): refuse agent rm/mv/redirect on `~/.claude/state/*` enforcement files; clearing only by an operator-typed override. Not built (secret-guard.sh has no state rule).
  - Item 2 (obs 0005): block `pip install|npm install|make|cargo build` in a checkout until its platform/install doc was read. Half built: H2 `sync-on-use.sh` does the fork sync; the doc-read half is missing.
  - Item 3 (obs 0012): SessionStart lists the newest sessions across all `~/.claude/projects/*` dirs. Not built (`context-diff.sh` diffs CLAUDE.md/MEMORY.md only).
  - Item 4 (obs 0023): refuse Explore/Plan spawns whose prompt names a progress file. Partly covered: `subagent-stop-gate.sh` blocks the subagent at stop; no PreToolUse Agent check.
  - Item 5 (obs 0028): delegation trip-wire (~6 Bash calls over more than 3 repos in a turn). Not built.
  - Item 6 (obs 0007, 0016, 0024): Stop-hook flag on absence claims with no read in the turn. Not built (CLAUDE.md rule only).
  - Item 7 (obs 0006): stop-gate checks task-observer protocol steps beyond the scan. Partly covered (skill loaded + scan line, again after compaction).
  - Item 8 (obs 0030) is built: H9 `carryover.sh`, live copy equals the repo.

## Thread: infrastructure
- Jetson / Rubik Pi (not procured): T3 infra, MemVault, OB1 Jetson backend, TB Postgres move, Acode + dsh, desktop.
- Spark backlog (from `raw_database/spark_recommendations/` 00-11): FastRPC thermal hook, `audit_ledger.db` sync to Jetson, 24 h HMAC rotation; NX-01/02/03/05; novus `rolling_habits.json` to SQLite, Car Wash harness; SKILLS-01..04.
- Secrets: move plaintext `.env` keys (OpenRouter, mem0, OmniRoute) into `NvAEx-Recaps/secrets` and read them via `nvaex-secret`.
- Hardware brainstorm (private notes stay in `session-work/2026-10-04/`).
