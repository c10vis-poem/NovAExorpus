# Handoff 2026-10-24 (cloud session, Fable 5.1)

Stopped early at the operator's request to conserve cloud credits. This folder holds everything the session produced that was not already shipped, so the board threads and grill sessions can pick it up without re-reading.

## What shipped
- **Aesop-Xi hooks rebuilt** for cloud sessions: draft PR https://github.com/c10vis-poem/Aesop-Xi/pull/81 (branch `hooks/cloud-write-checklists`). Hooks never disable in the cloud; a watchdog (`run-hook.sh`, 8 s per hook, fail-open with a logged NOTE) keeps a crash or hang from killing the session. New `/write N <text>` and `/write <new item>` check-in verbs beside `/ok`, `/defer`, `/reject`. RESUME.md date is checked (must be today at wrap-up, not older than 14 days at start). Opening sequence O1-O6 and wrap-up W1-W8 are each verified by `stop-gate.sh`. SubagentStop gets a scope check. Interpreter runs count as writes. 28 of 30 test suites pass in the container; the two ship suites need the `gitleaks` binary (CI job added). Operator still has to install the live copies on the phone with a `!` command.

## What is in this folder
- `extracts/latest-config-extract.md`: the Drive "latest-config" folder (NAEX Proposal v2, the 2026-10-13 OpenRouter session, the Jev Router / GPT-6.1 fan-out) with operator decisions separated from LLM proposals (Part V is the merged view).
- `extracts/wiki-admin-extract.md`: every wiki-admin document in Drive (`_wiki-admn-docs`, Solid-plan, prior dumbass planning): roles, File Administrator profile, W5H skill, converter and marker scripts in full, frontmatter and JSONL schemas, promotion rules, 19 open questions.
- `extracts/ondisk-extract.md`: the four big on-disk docs (master config session, Graphify + code-review-graph article, joy-08, joy-14): six cognitive layer factors, six dynamic workflows, pre-construction order.
- `extracts/asset-inventory.md`: repos, hooks, skills, plugins, models, nodes, accounts (names only), tools, corpus counts, open items. 15 repos could not be read by `gh` (session not attached); the list is incomplete and says so.
- `extracts/plugin-skill-audit.md`: 109 synced plugin dirs, ~695 skills, 163 agents, 28 SessionStart hooks, the hook-collision map, ten overlap clusters, marketplace gaps, context-cost estimate and a recommendation table.
Drive file IDs and the operator email were replaced with placeholders because this repo is public.

## Credits and Fable (answer to "why can't I use the $100 credit for Fable")
Grounded in the Anthropic docs fetched this session; verify the dates on the billing page.
- The promotional cloud credit ($100 Pro, $250 Max) is spendable only in cloud sessions (claude.ai/code and the app), not in the terminal on the phone, and it expires on Nov 4.
- Fable bills to usage credits, never to the subscription allowance, and the first use in a session shows a consent prompt. Decline it or close it and the session silently stays on Opus.
- Fable needs Claude Code 2.1.257 or newer and is excluded for zero-data-retention orgs.
- This very session reports rate-limit type `ccr_promotional` on `claude-fable-5-1`, so the credit is in fact being used here. Where it looked unusable: the per-session consent prompt, an `availableModels` managed setting that hides Fable, or starting from the phone terminal instead of a cloud session.
- To use it on purpose: open a cloud session, run `/model fable` (or start with `claude --model fable`), accept the consent prompt once, and watch the credit on the billing page.

## Remaining deliverables (not built this session; each is a thread or grill session)
1. **Fable orchestrator agent** for the project threads: a `.claude/agents/fable-orchestrator.md` (model `claude-fable-5-1`) in this vault and in Aesop-Xi, with tools limited to Read/Grep/Glob/Agent/SendMessage, that plans, spawns builder subagents at Sonnet/Opus, and runs the Stop-hook auditor. Source: BOARD-INTAKE "Grill" and "Orchestration audit".
2. **Wiki-admin agent package** (BOARD-INTAKE thread): build in `agents/wiki-admin/` here, install into NovusAExenti. Inputs are all in `extracts/wiki-admin-extract.md` sections B1-B11: File Administrator profile, W5H extraction, wiki-reference-router, convert-raw-to-md and marker scripts (with the listed weaknesses fixed: deterministic retrieval tokens, full sha256, per-tier manifests), corpus-verify as the independent check, capture -> stage -> verify -> promote, cross-auditor six checks. Open questions E1-E19 need the operator before the schema is frozen (one chunk schema, one frontmatter schema, who approves promotion).
3. **Assets and capabilities appraisal**: `extracts/asset-inventory.md` is the ledger; the appraisal verdicts (keep / strip-and-judge / drop) are not yet written. Add the 15 unread repos by attaching them with `add_repo` first.
4. **Plugin and skill cross-comparison**: `extracts/plugin-skill-audit.md` section F is the recommendation table. Decisions it waits on: one memory auto-capture plugin, one orchestration framework, drop the ECC-dependent PostToolUse entries in Aesop-Xi settings, consolidate the three task-observer and three termux-helper copies. Marketplace candidates: kotlin-lsp, Mobile Release Check, GCP DevKit, huggingface-skills, session-report, MCP Workflow Audit, Setup Audit. Jev + REA strip the forked repos into asset marketplaces per BOARD-INTAKE "Strip-and-judge"; review `NvAEx-Jev.skills` and `NvAEx-rea` first (PENDING).
5. **3-APK Jetpack Compose Xi stack**: Hyperion-XI (tiles + webview, Compose, Material 3), AEthX-AEsc (foreground-service terminal daemon, PTY, UNIX socket + WebSocket bridge, NPU loader), CloviX-AEyre (`:voice-core` VAD/STT/TTS + screen vision, 127.0.0.1 HTTP/WS with token). Design inputs: `extracts/ondisk-extract.md` F3/F4 sections B, `handoff/2026-10-23/voice-apk-brief.md`, NAMING-CANON. Those three repos must be attached to the session before a skeleton can be pushed.
6. **Recursive cognitive pipeline and enterprise config**: six-factor `.agent/` layout (recursive_learning, orchestration, dev_ast, curation, enforcement, observation), 5+1 tiers, the six dynamic workflows hybridised as extraction and enforcement layers, protocols 01-07 contract docs, GCP lane (Gen AI App Builder on the $1,000 Vertex credit) with the Success Verification Grade Log as the only training gate. Inputs: `extracts/ondisk-extract.md` Part II and `extracts/latest-config-extract.md` Part V.

## Operator decisions needed before the next session
- Install the new hook copies on the phone (`!` command; agents cannot touch `~/.claude/settings.json`).
- Keep or drop the two ECC PostToolUse entries in `Aesop-Xi/.claude/settings.json` (left untouched; nothing is turned off without the operator naming it).
- Add `gitleaks` to the cloud environment setup script so the ship test suites run there.
- Attach the 15 unread repos and the three APK repos to the next cloud session.
- Open questions E1-E19 in `extracts/wiki-admin-extract.md` and F1-F12 in `extracts/ondisk-extract.md`.

## Sources read for this folder
This session: Aesop-Xi hooks, tests, AGENTS/MEMORY/PENDING/RESUME; vault AGENTS, BOARD-INTAKE, RESUME, PENDING, NAMING-CANON, `.claude/agents/`, `handoff/2026-10-23/` listing; the five extracts above (written by reader subagents from Drive and the vault). Not read: `Drive_sync/`, `raw_database/`, the `Master_Dumbass_config` subtree, the `_dumbass-bin-files` binaries (need `download_file_content`).
