# Custom skills, scripts, tools and hooks: full inventory

Built 2026-10-20 from every session and chat in the "Skills and Abilities" project, then checked against the live repo `c10vis-poem/novaexorpus` (main at the 2026-10-19 merge of PR #51).

**Legend**
- **LIVE**: present in `c10vis-poem/novaexorpus` main right now. Path is relative to the repo root.
- **PHONE**: created or found on the phone (`/sdcard/...` or `~/...`) in a September session. Not in the repo, so it may have since changed or been deleted.
- **ACCOUNT**: a claude.ai account skill or account memory.
- **SPEC**: exists only as code or a description inside a doc or PDF. There is no runnable file.
- **DRAFT**: drafted in a session and never saved.

Assets are extracted from source files and chats. One source can yield several assets, and several assets can merge into one unified asset (see the last section).

## Sources read
| Source | Date | Asset work in it |
|---|---|---|
| Chat: Building a custom skill together | 2026-07-05 | memory-as-skill v1 and the openwiki fork plan |
| Chat: Syncing Markdown and JSON to Obsidian | 2026-07-08 | None (sync setup steps only) |
| Chat: Work release note documents | 2026-10-07 | None (ESD and job search) |
| Cowork: Inbox and Drive cleanup | 2026-09-16 | None in the latest page (Gmail trashing only) |
| Code session: Code review graph tools (NovÆxorpus build) | 2026-09-09 | Most of the PHONE assets; read in full |
| Cowork: Building a reusable skill | 2026-09-18 | Session Bootstrap Check skill (DRAFT); read in full |
| Cowork: Memory-as-skill editing | 2026-09-22 | memory-as-skill v3.0 proposal |
| Cowork: Scheduled task automation | 2026-09-22 | Morning-briefing sample; nothing was scheduled |
| Cowork: Memory-as-skill MCP builder | 2026-09-22/23 | Extraction-layer build guide artifact and a vault `.gitignore`; no MCP server code |
| Cowork: Chapter seven filing amount | 2026-09-23 | None in the latest page (personal) |
| Cowork: Training benefits application | 2026-10-04 | None in the latest page (personal) |
| Repo `TOOLS-SCRIPTS-HOOKS-INVENTORY.md` | 2026-09-10 | Verified device inventory |

## Skills
| Asset | Status | Where |
|---|---|---|
| task-observer, plus scripts `migrate-log.py`, `validate-skill-bundle.py` and `new-observation.sh` | LIVE | `.claude/skills/task-observer/` |
| drive-to-obsidian-migration | LIVE | `.claude/skills/` |
| notebooklm | LIVE | `.claude/skills/` |
| debug-issue, explore-codebase, refactor-safely, review-changes | LIVE (duplicated) | `.claude/skills/` and `.gemini/skills/` |
| memory-as-skill | LIVE (3 copies) | `Skills/SKILL.md`, `Skills/memory-as-skill/`, `__RESUME.md/_PENDING.md/SKILL.md` |
| memory-as-skill v1: SKILL.md plus `memory/general.md`, `active/novus-agenti.md`, `archive/neuroomni.md`, with STOP and SCOPE blocks | ACCOUNT | Built in the chat of 2026-07-05 |
| memory-as-skill v3.0: storage moved to account memory `/mas/*`, loads unconditionally | ACCOUNT (proposed) | Cowork session of 2026-09-22 |
| create-cowork-plugin, cowork-plugin-customizer | LIVE | `Skills/Plugin Management-0.2.2-v39/` and `__RESUME.md/_inbox/SKILL (2).md` |
| llm-wiki-compiler-NvAEx | LIVE (doc) | `Skills/llm-wiki-compiler-NvAEx.md` |
| android-termux-operator update (3 safety rules) | LIVE (staged, not installed) | `skill-updates/2026-10-08/` |
| Skill reference docs: aesop-wiki, horizons-wiki, horizons-repo-skill, android-reverse-engineering, memory-as-skill, claude-skills | LIVE (docs filed under hooks/) | `.claude/hooks/skills-corpus/` |
| corpus-batch-processing, corpus-verify | PHONE | `~/.claude/skills/`, raw_database/skills/ |
| code-review, tdd | PHONE | `raw_database/skills/` |
| snapdragon-npu-partitioner | PHONE | `aesop-xi/skills/` |
| parallel-session-orchestration (never exercised) | PHONE | `novaexopia/skills/` |
| corpus_verify_skill_skill.md (output of a smoke test) | PHONE | `novae-xorpus/04_skills_runtime/prompt_skills/` |
| openspec-apply-change, openspec-archive-change, openspec-explore, openspec-propose | PHONE | `~/repos/NovA-terrestrial-brain/.claude/skills/` |
| project-memory, horizons-wiki, termux-mobile-dev | PHONE | Novus-Agenti `skills/` and the QNN-QAIRT Obsidian wiki |
| technical-builder-style, mobile-grep-skill | PHONE | `__RESUME.md/_Unresolved/` and the archive |
| Session Bootstrap Check: reads CLAUDE.md, RESUME.md and PENDING.md, then wires up honey, Terrestrial Brain, mem0 and code-review-graph | DRAFT | Cowork session of 2026-09-18 |
| openwiki/SKILL.md for the Termux fork | DRAFT | Chat of 2026-07-05 |
| session_close_skill, qa_session, audio_prep, manifest_sync | SPEC | Lex-Novi audits, `04_skills_runtime/prompt_skills/` |
| Installed vendor skills and plugins: honey plus 13 satellites, mem0, code-review-graph (30 MCP tools), happy-ending, mattpocock-skills, obsidian, watch, grilling, termux-helper, aesop-voice-pipeline, clean-my-ai-harness, graphify | PHONE (installed) | `~/.claude/skills`, plugins |

## Tools and scripts
| Asset | Status | Where |
|---|---|---|
| `clean.py`, `check.py`, `chunk.py` (pipeline phases 1 to 3) | LIVE | `tools/` |
| `bootstrap.sh`, `launch.sh`, `vm-connect.sh`, `vm-install.sh`, `vm-reconnect.sh` | LIVE | `tools/` |
| `process_folder.py`, `dedup.py`, `build_rag_chunks.py`, `build_rag_index.py`, `query_rag.py`, `verify_corpus.py`, `audit.py`, `generate_jsonl_markers.py` | LIVE | `.migrate/` |
| `dsh-termux-shim.sh`, `install-dsh-alpine.sh`, `install-openwiki-alpine.sh` | LIVE | `Scripts/` |
| `run_audit.sh`, `divergence_detector.py`, `cross_auditor_orchestrator.py`, `tool_call_interceptor.py`, `htp_partition_calc.py` | PHONE | `aesop-xi/tools/` |
| `nanoclaw_router.py` (its skill registry is stale) | PHONE | `novaexopia/tools/` |
| `agent_panel.sh` | PHONE | `NovAExopia/aesc/scripts/` |
| `doc_to_skill_and_tool.py` | PHONE | `novae-xorpus/tools/` |
| `voice_bot.py`, `live_voice_loop.py`, `kokoro_tts.py`, `stt_test.sh`, `nanobot_from_scratch.py`, `validate_repo_integrity.py`, `crawl_agent_vault.py`, `setup-aesop.sh`, `gcp_cross_account_handshake.sh`, `scaffold_cognitive_repository_architecture.sh`, `failures.sh`, `gemini-code-1777423316551.sh`, `gemini-code-1788194504002.sh` | PHONE | `raw_database/tools/` |
| `regenerate_masters.sh`, `bootstrap-stack.sh`, `session-start.sh`, `geniex-bench`, `whisper-parakeet` | PHONE | `~/NovAExorpus/tools`, `~/tools`, repo `scripts/` |
| `convert_raw_to_markdown.py` | SPEC | Code inside `04_ON_DEVICE_INGESTION_AND_W5H_FRAMEWORK.md` |
| `compile_manifest.py`, `daily_scraper.py`, `log_builder.py`, `npu_manager.py`, `export_drive_docs.js`, `build_manifest.py`, `extract_audio.sh` | SPEC | PDFs and spec references only |
| `system_housekeeper.sh` (only a patch fragment was ever found) | SPEC | Named in `05_FEDERATED_FILE_TREE_TOPOLOGY_MASTER.md` |
| Pipeline phases 4 to 6: wiki_synthesize, extract_skills, memory_writeback | SPEC (gap) | Extraction-layer build guide |

## Hooks and session wiring
| Asset | Status | Where |
|---|---|---|
| SessionStart runs `router-guard.sh`, which checks the 6-layer pipeline | LIVE | `.claude/settings.json`, `.claude/hooks/router-guard.sh` |
| Gemini SessionStart runs `crg-session-start.sh`; AfterTool runs `crg-update.sh` | LIVE | `.gemini/settings.json`, `.gemini/hooks/` |
| router-guard output style | LIVE | `.claude/output-styles/router-guard.md` |
| builder and corpus-architect agents | LIVE | `.claude/agents/` |
| `hooks/` folder | LIVE (empty stub) | `hooks/POINTER.md` |
| aesop-xi post-commit hook that runs `regenerate_masters.sh` | PHONE | `~/repos/aesop-xi/.git/hooks/post-commit` |
| Plugin hooks: honey, mem0, watch | PHONE | Installed plugins |
| Permission allow list in `~/.claude/settings.json` (blanket allow, with Drive trash and update denied) | PHONE | Set 2026-09-09 |
| SessionStart hook that loads the failure report | DRAFT | Offered 2026-09-09, never built |
| openwiki session-end hook, Termux webhook receiver, MCP server, PWA connector | DRAFT | Planned 2026-07-05 |

## Candidates to combine into unified assets
1. **memory-as-skill.** There are 5 or more copies: 3 in the repo, 1 in `hooks/skills-corpus`, and account v1 and v3.0. Merge them into one skill that uses v3.0's storage model.
2. **Session lifecycle.** Combine `router-guard.sh`, `session-start.sh`/`bootstrap-stack.sh`, the Session Bootstrap Check draft, task-observer's first-call trigger and happy-ending's close into one start-and-close asset.
3. **Verification.** `check.py`, `verify_corpus.py` and the corpus-verify skill do the same RLVR check.
4. **Ingest and extraction.** `clean.py`, `process_folder.py`, corpus-batch-processing, drive-to-obsidian-migration and `doc_to_skill_and_tool.py` all cover the raw-to-clean-to-extract path.
5. **Chunking and indexing.** `chunk.py`, `build_rag_chunks.py`, `build_rag_index.py` and `generate_jsonl_markers.py`.
6. **Code review.** The code-review skill (phone), review-changes and the crg hooks.
7. **VM access.** `vm-connect.sh`, `vm-reconnect.sh`, `vm-install.sh` and `bootstrap.sh`.
8. **Duplicates.** Four skills are copied between `.claude/skills` and `.gemini/skills`.
