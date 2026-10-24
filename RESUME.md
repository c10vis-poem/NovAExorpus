Session files: [[AGENTS]] · [[PENDING]] · [[MEMORY]] · [[MAP]] · [[NAMING-CANON]] · [[BOARD-INTAKE]]

# RESUME.md — Session Ledger (rewritten every session)

Repository: NovÆxorpus (`c10vis-poem/NovAExorpus`, PUBLIC). Readable from any device, agent or account once GitSync has synced: everything this file points to is inside this vault unless marked **(phone only)**.
**Last session: 2026-10-24** (cloud, Claude Code, Fable 5.1, stopped early by the operator to save credits). Aesop-Xi hooks rebuilt for cloud sessions (draft PR Aesop-Xi #81, not merged); five reading extracts and the remaining-deliverables plan in `handoff/2026-10-24/README.md`. Previous: 2026-10-23 (phone, Opus 5.5) pre-grill housekeeping, long-term work in [[BOARD-INTAKE]].

## NEXT SESSION — START HERE
0. **Read `handoff/2026-10-24/README.md`**: the credits/Fable answer, the five extracts (latest config, wiki-admin, on-disk docs, asset inventory, plugin audit) and the six deliverables still to build (Fable orchestrator agent, wiki-admin package, appraisal, plugin cross-comparison, 3-APK stack, cognitive pipeline + enterprise config). Review and merge Aesop-Xi #81, then install the hook copies on the phone with a `!` command.
1. **Read** [[AGENTS]] ("Start here" + "Current stack"), then [[PENDING]] "Open". The shared agent rules are `agents/AGENTS.global.md`.
2. **NPU proof result.** A proof run (`~/tools/npu-proof.sh`, GenieX v0.9.3, Qwen3.5 2B and 4B) was still running at wrap-up. Its log is **(phone only)** `~/.claude/session-work/2026-10-23/npu-proof-*.log`; the summary at its end says whether each model ran on the HTP (Hexagon v79), which HTP sessions opened, layers offloaded, memory per device, and npu/hybrid/cpu speeds. Then continue `handoff/2026-10-23/npu-install-plan.md` §6 from step 8, one model at a time with the operator. The permission checker blocks the agent from running freshly downloaded binaries: give the operator `!` commands.
3. **Operator items** (exact commands in [[PENDING]] Open): secrets into the store (new OpenRouter key needed), a few deletes, decisions on starter principles / hook 3 / small calls, answers owed, infrastructure.
4. **Agent items:** Jev skills fork review (`c10vis-poem/NvAEx-Jev.skills`) before install; observations 0038-0041 each propose a rule or check to build in Aesop-Xi.

## STATE (verified 2026-10-23)
- **PRs:** all merged except `Horizon-s-home-grid #1` (operator: leave it).
- **Hooks (phone, live, equal to Aesop-Xi main):** H1-H9 plus the auditor (`type: agent` Stop hook, 8-line transcript pages), absence-gate, state-guard, settings-guard (agents cannot change Claude Code settings: verified blocking), build-doc-gate, agent-type-gate, delegation-tripwire. Sources and README: `c10vis-poem/Aesop-Xi/hooks/`.
- **Instructions:** Claude-only rules in `~/.claude/CLAUDE.md` **(phone only)**, which imports `~/.agents/AGENTS.md`; that shared file is copied to `agents/AGENTS.global.md` here.
- **Models on the phone:** `Documents/_models/` (gguf: Qwen3.5 0.8B/2B/4B/9B + mmproj, Gemma 4 12B QAT/E4B/E2B, InternVL3.5 8B, SmolVLM2, Granite micro; qairt: InternVL3.5 2B/4B bundles for 8 Elite, X Elite, X2 Elite; stt: Distil-Whisper QNN/TFLite/ONNX). Inventory: `handoff/2026-10-23/models-report.md` (Drive IDs redacted).
- **GenieX:** v0.9.3 at `~/tools/geniex-bench-android-arm64-v0.9.3` (sha OK, skel link done); v0.3.14 and v0.7.1 kept until v0.9.3 is proven. Route: AI Hub bundles → `qairt`; any GGUF → `llama_cpp` (GGML Hexagon backend); same GenieX endpoint.
- **Dropped:** OmniRoute, mem0, Terrestrial Brain, OpenWiki, Qwen3-VL.
- **Forks:** GenieX, ai-hub-models (`ai-hub-merovingian-models-`), generative-ai synced today; 23 bot branches archived as `archive/*` tags; no workflow is disabled in any fork (11 wrongly disabled today were turned back on).
- **Observer:** 19 active entries; open 0038-0041; parked 0012 (hook 3 undecided). 16 cross-cutting principles in `skill-observations/cross-cutting-principles.md`.

## DECISIONS 2026-10-23
[[BOARD-INTAKE]] "Decisions recorded 2026-10-23", plus today: nothing is turned off in any repo or config without the operator naming it; Claude Code settings are operator-owned (changes go to the operator as `!` commands); apps are separate APKs; own LLM server instead of llama-server; Qwen family = Qwen 3.5 only.

## SOURCES
Reports behind this file: `handoff/2026-10-23/` (NPU install plan and audit, branch review, models, voice research, voice APK brief, remote access, skills inventory, Anthropic research, principles table).
Read this session: PENDING.md, BOARD-INTAKE.md, the observation log (frontmatter scan + 0034, 0038 bodies), `~/.claude/hooks/README.md`, NPU-ON-DEVICE.md, the GenieX docs cited above, every subagent report named here, the Qualcomm Qwen3.5-2B model card and release_assets.json.
Not read: the PRIORITY ONE plan docs (00-13); most of `Drive_sync/`; `~/.hermes/.env` (secret-guard); `~/.claude.json` (never read).
