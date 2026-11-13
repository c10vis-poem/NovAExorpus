---
status: staged
source: wiki-admin session 3c1dfa47, contract B task S
date: 2026-11-11
---
# Inventory: the vault, shared storage and the phone's model folders (2026-11-11)

Method: `du -sh` (size), `du --inodes` (entries = files + folders), `du -d 1/2`, `find -printf` for model files and
the planning folders. Hidden entries (`.git`, `.obsidian`) are not in the top-level counts. Nothing was opened except
READMEs/AGENTS files named below. `_personal/` was sized only, never listed (private).

## 1. Vault NovAExorpus (`/storage/emulated/0/Documents/NovAExorpus`), about 10.7 GB visible
| Folder | Size | Entries | What it is |
|---|---|---|---|
| `QAIRT-QNN/` | 7.1 G | 2,258 | flat dump of Qualcomm QAIRT/QNN SDK files (many numbered copies, e.g. `Android (1..19).mk`, raw test tensors, model JSONs `qwen2.5-7b.json`, `gemma-2b.json`) |
| `Drive_sync/` | 1.8 G | 2,363 | Drive mirror: `Secure-Spark-Proof-Folder/` 1.2 G (`novae-xorpus/` 1.1 G + per-repo folders), `__RESUME.md/Housekeeping` 599 M, `Original_Corpora/` 74 M |
| `Vendor-Registries/` | 650 M | 73 | vendor docs; detail in vendors-and-models.md |
| `qairt_/` | 86 M | 3 | QAIRT archives |
| `global-documentation-vault/` | 74 M | 168 | google-dev-docs 26 M, qairt-docs 26 M, unsloth-docs 16 M, qwen-models 5.5 M, research 1.2 M, llama-docs, reverse-engneering |
| `__RESUME.md/` (a folder) | 52 M | 867 | `__Builder-Guide_Directory-` 30 M, `_whatisit` 6.3 M, `_inbox` 1.7 M, `llm-wiki_`, `_PENDING.md` |
| `raw_database/` | 30 M | 889 | `raw/` 21 M, `Dump/` 6.9 M, `clean_md/` 1.3 M, `02_MY_ORIGINALS`, `spark_recommendations` |
| `chunk.jsonl` | 7.1 M | 1 | RAG chunk index |
| `clean_md/` | 6.5 M | 556 | converted Markdown |
| `Codebase-Graphs/` | 6.3 M | 4 | code graphs |
| `02_wiki_md/` | 6.2 M | 550 | wiki pages |
| `benchmarks/` | 6.0 M | 36 | |
| `audit/` | 4.0 M | 5 | |
| `reverse-engineering/` | 3.9 M | 30 | |
| `handoff/` | 1.7 M | 94 | dated handoffs |
| `plugins/` | 1.6 M | 198 | greedy-crane and others |
| `project-exports/` | 921 K | 43 | |
| `skill-observations/` | 624 K | 210 | task-observer log |
| `_recaps/` | 440 K | 34 | |
| `Skills/` | 374 K | 28 | |
| `OpenWiki_sync/` | 334 K | 11 | OpenWiki is dropped (AGENTS.md:92) |
| `recovered/` | 243 K | 34 | |
| `tools/` | 179 K | 14 | |
| `grill/` | 168 K | 5 | |
| `GitHub/` | 140 K | 36 | |
| `manifest.jsonl` | 120 K | 1 | lists 585 converted files (AGENTS.md:39) |
| small (under 100 K) | | | `01-inbox`, `01-sources` (15), `01_raw_sources` (11), `03_recall_cache`, `04_skills_runtime`, `05_episodic_logs`, `Assets-Index` (5 POINTER.md), `HTP` (5), `Markor`, `docs` (12), `device-stt-tts`, `google_agentic_ai`, `handoffs`, `llm-wiki`, `termux`, `skill-updates`, `Scripts`, `agents`, `archive`, `hooks`, `pending`, `plug-ins`, `raw`, `wiki_md`, `_res` |
| loose root files | | ~30 | specs `00_`..`05_` (wrong per AGENTS.md:23-30) + `00_...md.bak`; `Argon reports*.md` (3); `Frontier Agent Engineering & Skill Consolidation Architecture*.html` (2 copies, 52 K each); `RESUME.conflict-android-20261031T173452Z.md`; `Untitled*.base` (2); `nee.md`; `2026-11-03T0904_111.md`; canon files (AGENTS, MAP, MEMORY, RESUME, PENDING, NAMING-CANON, CONTEXT, BOARD-INTAKE, GRILL-MANIFEST, LOCKED-DECISIONS, SOURCE-RETRIEVAL-MAP, TOOLS-SCRIPTS-HOOKS-INVENTORY) |

MAP.md is 5 lines (title and authority only): it routes nothing yet.

## 2. Shared Documents (`/storage/emulated/0/Documents`)
| Folder | Size | What it is |
|---|---|---|
| `_File-Driven-Agent-Operating-Environment/` | **84 G** | the owner's planning + model store; see 2a |
| `_Merovingians_Keep/` | 20 G | archive: `Zip/` 14 G (a full older vault copy incl. `QAIRT-QNN/` 7.1 G, `Drive_sync/` 2.4 G, `.git` 317 M, `_quarantine/` 3.0 G), `NovAExorpus-nested-mirror/` 3.1 G, `_salvage_yard/` 1.8 G, `Reverse.Eng_Research/` 854 M, `homegrid/` 373 M, `Obsid ian-Archives/` 219 M, `GitHub_vault/` 99 M, `vault-pdfs/` 39 M, `PDF"s/` 13 M, `NovA-Corpus/` 4.3 M |
| `_personal/` | 11 G | private: sized only |
| `_Termux-sync/` | 1.6 G | dot-folder backup (`.claude` 1.1 G, `.cache`, `.android`, `.bun`, `.cargo`) |
| `NovAExorpus-6d2f7df…/` | 332 M | older vault snapshot (commit-named) |
| `NovAExorpus-v2/` | 22 M | vault variant |
| `Drive-sync/` | 5.6 M | |
| `WebView/` 1.3 M, `zArchive/` 1.2 M, `_sessions-manifest/` 701 K, `_local-environment/` 147 K, `markor/` 63 K, `Security-Breach_Triage /` 7.5 K | | |
| loose | | `SKILL.md`, `_agents.md`, `tablet-setup.tar.gz`, **`tablet-age-key.txt` (secret-looking: name only, not opened; an age key in shared storage)** |

### 2a. `_File-Driven-Agent-Operating-Environment/`
| Folder | Size / files | What it is |
|---|---|---|
| `Inventory/_models/` | **79 G** | `gguf/` 47 G, `qairt/` 17 G, `installed/` 11 G, `speech/` 3.4 G, `stt/` 1.3 G, `runtimes/` 144 M; listed in vendors-and-models.md |
| `Inventory/_assets/` | 5.2 G | `_node_tar.gz+_` 196 M, `geniex-chat` 98 M, `_GitHub-forks` 50 K, ~4.9 G in loose files not yet listed |
| `Inventory/_plugins/` | 67 M | incl. `llm-wiki`, `MCP Kotlin SDK` |
| `Greedy-crane/` | 1.9 M, 24 files | **the wiki-admin compilation**: `Wiki Admin Hybrid Bridge Skill.md` (2 copies, 17 K), `Wiki Admin Runtime Architecture.md` (2 copies), `wiki_admin_harness_guide.md` (2), `extract_artifacts.py`, `greedy-crane-only.zip` 266 K, `wiki-admin-harness.zip` 263 K, `User-guides/Wiki-Agent-User-Guide.md` 26 K (+zip), 7 skills (`save-images`, `end-session`, `continue-subject`, `summarize-subject`, `What sign-in does`, `save-knowledge`, `connect-create-state`), `Wiki.Admin/Untitled.html` 1.2 M, `#to-do-2026-11-06/Wiki-Agent-To-Do.md` |
| `_Jev/` | 1.8 M, 178 entries | TypeSafe Jev docs: Build with Jev (Cookbooks 43, Demos), Documentation (Concepts, Get started, Patterns), Reference (API, Client SDKs 92) |
| `_README.txt/` (a folder) | 369 K, 31 | `Cialdini's-influence_JEVs-affluence_&_...` (Closing, "Jev up in this bitch.", "Subagent Persuasion."), `APK_3=HyperionXi`, `Repo-File-Structure`, memory-as-skill design brief |
| `Jev Observation Database & Predictive Trajectory Enforcement System...` | 374 K | design doc |
| `plan-docs/` | 203 K, 16 | `FABLE_MASTER_BRIEF_v3.5_...txt`, `cloudflare_memory_stack_deployment_guide.md`, `Architecture planning (1)/`, `Rev.Eng.ify (1)/` |
| `Assets/` | 2.7 M, 10 | |
| `embeddinggemma-2-/` | 72 K | `EMBEDDING_GEMMA_INT8_USER_GUIDE.md` (copy also in home) |
| `More-Argon-Builds/` | 52 K, 4 | `corpus-ingest.js`, `jev_observation_db.py`, `nvaex_drive_consolidator_and_archiver.py`, `nvaex_jev_and_stage0_bundle.zip` |
| `_Target-planning_objectives/` | 44 K, 4 | `Agent Engineering & Skill Consolidation.md`, `Archive & Automated JEV Stage-0 Corpus Ingest Workflow.txt`, `Local-first-multi-agent-state-MACHINE.md`, `agent_architecture_report.md` |
| `Plan-Order-1,2&3/` | 36 K, 3 | `BUILD-ORDER-1/2/3.md` (10 Nov 2026) |
| `Cloudflare/` | 20 K | |

## 3. Download (`/storage/emulated/0/Download`), 1.5 G
Mixed: music folders (artist names), planning docs (`frontier_agent_architecture_blueprint (2).md`,
`agent_plugin_consolidation_spa.html`, `enterprise_jev_memory_agent_architecture_spa.html`,
`agent_os_cloudflare_architectural_research_master_blueprint.html`, `Consolidating AI Agent Plugin Architectures - Google
Gemini.mht` (2 copies), `19_Phase1-Dynamic-Workflows_...md.txt`), folders `Frankenstein/`, `Fable-2026-11-03/`, `OR/`,
`Copy of Agent os/`, `litedoc_workspace (1)` x5 copies, 15 `gemini-code-*.txt` snippets, session exports
(`session-2026-11-10-d6cff583-*.jsonl/.md`, `session-e40bf516-2026-11-10.txt`), `takeout-20261103T173929Z-1-001.zip`,
`gitleaks-results.sarif.zip`, `master-hook.tar.gz` (2), `Openship-arm64.AppImage`, `anthropic-incident-report-2026-11-10.txt`.

## 4. Home model folders (`~`)
| Folder | Size | Notes |
|---|---|---|
| `~/downloads/` | 8.5 G | `llama.cpp/` 1.3 G, `WhisperInput/` 146 M, Gemma 4 12B UD-Q4_K_XL gguf, EmbeddingGemma 2 UD-Q4_K_XL gguf, EmbeddingGemma 300M int8 tflite, `.nexa` bundles |
| `~/models-npu/` | 2.9 G | EmbeddingGemma 2 LiteRT x3 (SM8750) + generic + Q8_0 gguf; Qwen 3.5 0.8B Q4_0 (GenieX cache); qwen3_vl (not used) |
| `~/gemma-e2b/` | 2.5 G | Gemma 4 E2B UD-Q4_K_XL |
| `~/npu-work/` | 2.1 G | EG2 NPU server, HTP work (1A, 1BC, 1D), vendor-corpus |
| `~/tools/` | 1.8 G | geniex-bench v0.7.1 / v0.9.3 / v0.10.0, geniex-cli v0.10.0, geniex-serve |
| `~/gemma-12b/` | 168 M | Gemma 4 12B mmproj |

## Duplicates (by name and size; nothing deleted)
- **Whole-vault copies:** `_Merovingians_Keep/Zip/` (14 G, own `.git`), `_Merovingians_Keep/NovAExorpus-nested-mirror/`
  (3.1 G), `Documents/NovAExorpus-6d2f7df…/` (332 M), `Documents/NovAExorpus-v2/` (22 M).
- **QAIRT-QNN 7.1 G twice:** vault `QAIRT-QNN/` and `_Merovingians_Keep/Zip/QAIRT-QNN/`; inside, numbered copies (`Android (N).mk`).
- **Models twice:** `Qwen3.5-0.8B-Q4_0.gguf` 507,154,688 B in Inventory `gguf/` and in `~/models-npu/geniex-cache`;
  Qwen 3.5 9B Q4_0 twice (`Qwen3.5-9B-Q4_0.gguf` 5.38 G, `Qwen_Qwen3.5-9B-Q4_0.gguf` 5.74 G: different builds);
  Gemma 4 E4B three quants (IQ4_NL, q4_0, q4_k_m); InternVL 3.5 2B/4B as zips and unpacked `installed/` copies; zipformer,
  melotts for two chips each.
- **Docs:** `Greedy-crane/` holds pairs (`Wiki Admin Hybrid Bridge Skill.md` = `wiki_admin_hybridge_skill.md`, 17,240 B
  each; runtime architecture and harness guide twice); `Frontier Agent Engineering ... .html` x2 in the vault root;
  `litedoc_workspace (1)` x5 in Download; `00_...md` + `.bak`.
- **Vendor-Registries** also copied into `_Merovingians_Keep/Zip/Vendor-Registries/` (536 M).

## Flags
- `tablet-age-key.txt` in shared Documents: looks like a private key in shared storage (not opened).
- `Vendor-Registries/README (6).md` (Prime Agent README): quarantine hook FLAGGED it (`run-command`); describe only.
- `_personal/` 11 G: private, out of scope.
