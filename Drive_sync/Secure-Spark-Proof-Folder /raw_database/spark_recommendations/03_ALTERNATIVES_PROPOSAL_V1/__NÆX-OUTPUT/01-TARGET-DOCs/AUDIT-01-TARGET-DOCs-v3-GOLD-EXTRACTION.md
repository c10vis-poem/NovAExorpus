# AUDIT — Folder 01 · TARGET DOCs · v3 (GOLD-EXTRACTION LENS)

**Framing correction (per operator, 2026-09-04):** v2 focused on what to kill/merge and re-surfaced established canon as if new. v3 flips the lens: **what does each document uniquely add that appears NOWHERE ELSE in this folder?** The kill-list is a side effect of that analysis, not the point.

**Gold-standard anchor (operator-declared):**
> **S6 `Definitive Master Specification.txt` + F6 `Response.` (the 5+1 tier reconciliation) = absolute gold standard of this folder.**
>
> Every other document is measured against these two: does it add a distinct increment those don't already carry?

---

## Anchor: S6 + F6 baseline

**S6 (Definitive Master Specification v3.0)** already covers:
- 5+1 Tier cognitive memory topology (Sensory / Semantic / Working / Procedural / Episodic + Metacognitive root)
- Directory schema with per-tier access-control matrix
- Hierarchical `manifest.jsonl` protocol + full schema
- OpenWiki TUI Files Executive Agent lifecycle
- Universal Skill & Tool dual-extraction engine
- End-of-Day P2P Sync + Cross-Auditor + Sandboxed Red Auditor workflow
- Tri-Model Trace Alignment (Query / Executor / Frontier)
- Complete bash scaffolding script

**F6 (Response.)** already covers:
- Reconciliation matrix between 4-tier (System A) and 5-tier (System B)
- Cognitive-to-engineering memory type mapping (Episodic / Semantic / Procedural / Working)
- Unified 5+1 directory layout
- KAG Recurse & RLVR feedback cycle (attempt→verifier→backprop diagram)
- Implementation resolution checklist

**Everything below is what a specific file adds ON TOP of that baseline.**

---

## 1B-GLM-3-PRELIMINARY_OVERVIEW — unique increments

### 1B.1 `1- OpenRouter Chat Sun Aug 30 2026.md` (314KB)

Unique increments (not present in S6/F6):
- **Full working source** of `setup-aesop.sh` (~400-line Termux bash one-shot installer with color-coded steps, env-var block, embedded Python scripts, interactive OpenWiki `personal --init` walkthrough)
- **Full source** of `convert-raw-to-md.py` (pymupdf/python-docx/markdownify pipeline with frontmatter injection + idempotent mtime check)
- **Full source** of `generate-jsonl-markers.py` (SHA256 hashing, source_type=RAW_SOURCE / WIKI_SYNTHESIS, retrieval_tokens harvested from H2/H3 headers)
- **GCP Cross-Account IAM Handshake bootstrap script** (`gcp_cross_account_handshake.sh` with the specific service-account principal `service-<PROJECT_NUMBER>@gcp-sa-discoveryengine.iam.gserviceaccount.com` + `roles/storage.objectViewer` + `gs://business-secure-vault-bucket`)
- **ECC internal routing table**: `honey-crush`, `nexus-mapper`, `ecc-planner`, `px-reader` (four internal ECC skills discovered from a user-flagged orchestrator SKILL.md — S6/F6 don't touch ECC internals at all)
- **SKILL.md format specifics**: YAML frontmatter mandatory, description-as-trigger, `$ARGUMENTS`, `!command` for live shell context, two-pattern (inline vs `references/`)
- **QAIRT env-var block** with the exact path `hexagon-v73/unsigned` for ADSP_LIBRARY_PATH + the `genie-t2t-run` invocation
- **`haozixu/llama.cpp-npu` reference + `libhtp_ops.so`** — parallel NPU project as an implementation reference
- **Benchmark numbers**: ~90 tok/s prefill / ~27 tok/s decode on 1.7B Q8_0 (concrete throughput data)
- **User's stated fallback model roster** for the help-desk agent (Phi instructor, Granite mini, Gemma 4B, Gemma 12B, Qwen, Twin 9B)
- **Watchdog daemon post-mortem** — user's own account of why the prior APK crashed ("Watchdog daemon was wired wrong, I vibe-coded it") — motivation for the "no room to wiggle" discipline
- **Two hallucinations to annotate before use**: fabricated URL `https://0x0.st/Xk7p.md`, fabricated npm package `openwiki-obsidian`

### 1B.2 `2- fusion-response 2026-08-30.md` (20KB)

Unique increments over S6/F6/A6:
- The **exact QAIRT env-var pattern** as a copy-pasteable block (`QAIRT_HOME`, `PATH`, `LD_LIBRARY_PATH`, `ADSP_LIBRARY_PATH`) — cleaner than 1B.1's ad-hoc form
- **Explicit RAM math** for 9B Q4_0: `5.45 GB weights + 0.5–1 GB KV cache = 6–6.5 GB total`; `9–12 GB available stripped down; 2.5–6 GB headroom for system + APKs`
- **Fallback hierarchy** as a numbered decision path (`9B npu → 9B hybrid → 4B npu`) rather than prose

### 1B.3 `3- fusion-response 2026-08-30 [8-extended].md` (3KB)

Unique increment: only the **completed Part 8 (Grill Session Manifest tail)** that 1B.2 truncated mid-sentence.

---

## S-tier — unique increments (S6 is the anchor)

### S1 `1A vault_root/.txt` + S2 `1B- vault_root/.txt`

Unique increments over S6:
- **Emoji-coded tier labels** (`[TIER 1: COLD ARCHIVE]` etc, `[METACOGNITIVE]` for the root)
- **Colored bullet convention** in S2 that S6 lacks — visual scannability layer
- Otherwise a strict simplification of S6's directory schema

### S3 `Branding ligature` (Gdoc)

Unique increments over everything else in this folder:
- **The full Xçineribus motto** in canonical typography with the em dash break — this is the ONLY place the motto is presented in its complete authored form
- The **"Æsc 🌳 et 🦁 Æyre"** pairing glyphs (the tree/lion pairing) — visual identity that never appears again
- The **"transmuting to the UI (The ASCII Trick)"** section — explicit `Æ` / `æ` Android string-resource guidance with font-picker note
- The **"Ever-evolving ecosystems, For ever-expanding Horizons"** Horizons UI tagline

Nothing else in the folder carries the brand identity at this fidelity.

### S4 `Clarifying -Clean Text- to skills and tools...` (Gdoc)

Unique increments (the user's OWN annotations layered on a stale earlier doc):
- **"Pretty sure this is just fluff about a tool it was ultimately never able to utilize"** — the bookmarklet is dead
- **"This is outdated in far off from the actual scope of work"** on the entire Priority Sequence
- **"Unslaught might be helpful but there are many others that hold priority"** — the moment `Unsloth` gets demoted and the harnesses (ECC, Honey for Devs, Pocock, Prime Agent, Claude Video, Reverse Skills, GSD, mem0, node.js, code review graph, LocalAI OmniRoute, OB1) get named as competing priorities
- **"THIS IS THE FIRST MAIN GOAL OF THE GRILL WITH DOCKS SESSION"** (all-caps user emphasis) — the moment the grill session becomes the anchor deliverable, not just a tool
- **"priority four and five pretty much have to run parallel"** — the moment 4 & 5 get de-serialized
- **"way before the 3 APK architecture and additional tools are added so this is way out of date but still correct thinking process"** — user distinguishes "outdated content" from "outdated thinking"
- **"perfecting the horizons and the red auditor but also the on-device inference AKA to model query/executor setup and also the home node housekeeping / cross agent auditor and logs compiler script editor agent as well as my help desk agent web search agent, open Wiki files management and on device npu / inference manager"** — the full expanded agent roster (~8 agents) in one sentence
- **"my comment on file 5 code being ass probably rings true for this document as well"** — user's live quality judgment on generated code
- **"NO. this is absolutely going to be executed by the agent that performs the grill session"** — the moment the human explicitly transfers execution authority to the grill agent

These annotations are the **highest signal in the entire folder**: they're the user reasoning out loud about what's stale, what's still-correct-in-spirit, and where authority transfers. **These are gold; the wrapper document they annotate is dross.**

### S5 `Copy of The 3-APK Native Topology & The Concierge Dataflow.`

Unique increments over S6/GLM-PT.1/A10:
- **Concrete WebSocket/Webview bridge architecture** — the ONLY doc naming this as the persistent bidirectional IPC layer between the 3 APKs
- **The exact "Concierge Execution Loop" enumeration** (5 steps: mic trigger → 9B meta-prompt → UI approval → inference → TTS + VAD standby) — precise handshake sequence not in S6
- **APK 2 explicit description as Termux replacement** with OS Accessibility Registration granting elevated permissions — most explicit statement of the Termux-replacement thesis in the folder
- **APK 3 explicit hooks**: Video Game SDK permissions + OS accessibility APIs for screen capture — specific permission pathway
- **"Every AI session that has tried to help with voice on Android has failed"** — the singular declaration that voice is greenfield with no prior art

### S6 `Definitive Master Specification.txt` ★ GOLD STANDARD

(Baseline — see anchor section above)

### S7 + S8 `ARCHITECTURE BLUEPRINT-(Pt.1) & (Pt.2)`

Unique increments over everything else in the folder (concentrated in the two YAML profiles):
- **`file_administrator.yaml`** — complete production-grade config for the housekeeping profile (GLM-5.2, native-libc-cpu, cpu_priority=low_background_ionice, 8K ctx, allow_hexagon_access=false, max_temp=42C, throttle=pause_execution, allow_write_mutation=true to novae-xorpus/, plugin allocations for local_fs_crawler + sha256_hasher, concurrency=YIELD_TO_NPU_INFERENCE)
- **`oeracle_helpdesk.yaml`** — complete production-grade config for **Œræcle** (qwen-3.5-9b-gguf-q4_0, qairt-htp-hexagon-npu, kotlin_bridge_lib=librc_kotlin_kernel, 32K ctx, allocation_floor_gb=5.2, max_temp=45C under Video Game SDK flags, throttle=fallback_to_openrouter, mem0+ob1_static_protocol, read-only to source docs, concurrency=ACQUIRE_NPU_LOCK)
- **Concurrency arbitration policy** between the two profiles: `DISALLOW_NPU_OVERLAP` + explicit memory allocation floors (system_reserve=2.5GB, qwen_9b=5.2GB, scratchpad=1.0GB) + IO priority steering — the ONLY doc that spells out the actual hardware-sharing contract between the two profiles
- **The concrete boot sequence**: `openwiki-tui --profile config/profiles/file_administrator.yaml` vs `--profile config/profiles/oeracle_helpdesk.yaml` — how the same TUI engine multiplexes into two personas
- **NopeDataBank** (Zero-Memory Layer, isolated volatile scratchpad hooked to `novus-aexenti/nope_databank/`) — introduced with a directory position, not just named
- **`reasoning_bank/post_regression/`** subtree with `baseline_tests/` and `regression_audit_report.jsonl` — regression guardrail against RLVR-induced degradation (this specific subtree is not in S6)

### S9 `Continual harness online adaptation...` (91KB arXiv paper)

Unique increment: **It is the paper.** External research anchor for the Continual Harness pattern that Prime Agent implements. Do not summarize; verbatim preserve per hard rule 3.

---

## A-tier — unique increments

### A1 `The Manifest Taxonomy (The 5 Document Types)`

Unique increments over S6/F6:
- **The 5 Document Types themselves** (Tool / Skill / Reference / Memory / Data) — S6 has the extraction engine but never crystallizes the classification vocabulary this cleanly
- **The full Æsop-Xi/NovÆxorpus repo tree with named subsystems** (arbitration_engine.py, policy_engine, hardware_throttler.py, dual_agent_router/query_analyzer.py + executor_bridge.py, mem0_episodic/ob1_static_protocols/OmniRoute data retrieval bridge, reasoning_bank/failure_logs/reward_variables/frontier_traces/post_regression, nope_databank, openwiki-tui-harness/config_profiles, mcp_connectors/anthropic_official + custom_node.js_mcp + filesystem_mcp, skills-and-capabilities/notebook-lmpy + obsidian-skills + graphify-visual + claude-video + code-review-graph + early-trend-scraper) — the ONLY doc that shows the entire novaexopia tree at that granularity
- **The `early-trend-scraper` subsystem** — `daily_scraper.py`, `stack_analyzer.py`, `trending_databank.jsonl` — the "know about trending repos months before they trend" scraper that appears nowhere else at file-tree granularity
- **The dual repo tree** at the bottom (`__NovÆ-Core/COGNITIVE_PLANE/APPLICATION_PLANE/SWARM_CLUSTERS/CAPABILITIES_VAULT/DATA_VAULT_SANDBOX`) — an alternative organizational lens (by function, not by naming-canon entity)
- **`data_vault_sandbox/` with the explicit "NO RCLONE AUTO-SYNC"** rule — hard boundary that only appears here
- **Named model roles**: `jeanie_x_qwen_0.8b` (0.8B alias) + `openwiki_cli_glm` + `helpdesk_installer_agent` — named service identities for the 4 on-device agents

### A2 `Convert Google Docs to Markdown - Google Search` (34KB)

Unique increment: **the bookmarklet reference that S4 declares dead.** If salvageable at all, extract just the bookmarklet URL/script and trash the rest — otherwise low-value search dump.

### A3 `Official Google Developer Documentation for System Architecture, Multi-Processing, and Shared Memory Constraints`

Unique increments (nothing else in the folder touches this level of NDK detail):
- **`AndroidManifest.xml` snippet** with `android:process=":orchestrator_daemon"` / `:qairt_engine` / `:llamacpp_engine` colon-prefix pattern — the exact isolation syntax
- **`ASharedMemory` NDK invocation** with `mmap` + `PROT_READ` drop for security via `ASharedMemory_setProt`
- **UNIX Abstract Namespace socket binding** (`addr.sun_path[0] = '\0'`) — no disk I/O, kernel-namespace-only IPC
- **`SCM_RIGHTS` ancillary payload** for file-descriptor passing via `sendmsg` + `cmsghdr` — the POSIX pattern for passing shared-memory FDs between the isolated daemons
- **Kotlin `MainOrchestratorService.startForeground()`** with `START_STICKY` return + notification channel — the LMK bypass pattern
- **The `isolatedProcess=true` trade-off** (pure sandbox but manual FD handling over IPC bounds) — the trade-off calibration that's operationally load-bearing

This is real Android reference material and directly implementable — it's the concrete IPC contract for Æsc↔Æyre↔Horizons.

### A4 `The Consolidated Master README`

Unique increment: **the explicit "1M token context window" call-out for GLM-5.2** + the specific `z-ai/glm-5.2` OpenRouter model id and `~$1.40 per million input tokens` price point — practical routing economics not covered in S6/F6.

### A5 `GLM-PT.2-fusion-response.md`

Unique increment: paired with A6 — likely a follow-up correction cycle. Small delta unless a specific correction shows up on close read (need to compare line-by-line against A6 if it's kept; otherwise archive).

### A6 `GLM-PT.1-MASTER.DOCUMENT.md` ★ (secondary anchor)

Unique increments over S6/F6:
- **The 15-gap list** — the numbered enumeration of what the older architecture docs get wrong (3-APK vs 1 APK; two NPU pathways; memory pipeline order; RLVR framing; naming canon; GCP handshake missing; home node agents missing; ECC routing table missing; Prime Agent role missing; SKILL.md format missing; JSONL record format; data tiering; MCP filesystem missing; companion document registry; Node Delta missing)
- **The Priority table** (6 rows × 4 cols: Priority / Name / What Happens / When [NOW/LATER])
- **The Tier 2 install list** (ECC, Pocock, OpenWiki, file converters) with exact commands
- **The `LocalAI vs OmniRoute` capability comparison table** — the moment LocalAI gets demoted to redundant-on-phone
- **The Grill Session Structure** with concrete input file table (each novae-xorpus path + role) and the 5 grill session phases (Interrogation / Repo Partitioning / Skill-to-Agent / Data Tiering / Roadmap)
- **The 7 output documents** the grill produces (MASTER_PLAN, REPO_STRUCTURE, SKILL_MATRIX, DATA_TIERING, CONTEXT, NAMING_CANON, GCP_HANDSHAKE) — the concrete deliverable spec

### A7 `Integrating Graphify, Obsidian, and NotebookLM.docx`

Unique increments:
- The specific `uv tool run graphify . --obsidian --output wiki/ast/` invocation with the `--obsidian` flag and per-tier output routing (wiki/code, wiki/ast, raw/research)
- The **`llm-wiki` compiler framework** (Pratiyush/llm-wiki) as a compiler that turns the OpenWiki output into a browsable static site at `http://127.0.0.1:8765`
- The "GLM-5.2 = 744-billion parameter, ~$1.40/M input tokens, 1M ctx" positioning with lambda/z.ai citations
- **The nested-tools submodule pattern**: `git submodule add https://github.com/... tools/llm-wiki`

### A8 `SQLite.txt`

Unique increment (small but load-bearing):
- **The `better-sqlite3` file-lock isolation guarantee** — SQLite at `~/.omniroute/*.db` never conflicts with ECC hooks or Prime Agent because it's file-locked not port-bound; the ONLY collision surface is other MCP servers on `localhost:20128` next to code-review-graph. This is the concrete "no, there is no clash" answer for the memory pipeline concurrency question.

### A9 `Architectural realignment.docx`

Unique increment:
- The complete **`AESOP_XI_Skill_Onboarding_Template`** JSON schema (skill_identity + hardware_execution_routing + runtime_permissions_bounds) — first-class artifact ready to lift out as a real .json file

### A10 `The Complete Systems Architecture Blueprint. Accurate launch`

Unique increments over GLM-PT.1:
- The full **v2.2-Production-Ready 4-node infrastructure table** (Alpha=Moto Razr Ultra + Snapdragon 8 Elite + Hexagon NPU v79; Beta=Jetson Orin Nano Super 8GB + 60-70 TOPs CUDA; Gamma=Rubik Pi 3 Dragonwing + 14+ TOPs; Delta=GCP Vertex + $1,000 credit tier + Cloud TPUs/A100/H100) — the concrete hardware manifest with per-node roles
- The **5-agent home node topology** on Node Beta (Home Assistant / Red Agent Auditor / IT Help Desk / Web Ingestion Monitor / NPU Inference Manager) with distinct responsibilities per agent
- The **GCP Cross-Account IAM Handshake detail**: business tier holds `gs://business-secure-vault-bucket/` and grants `roles/storage.objectViewer` to `service-PERSONAL_PROJECT_NUMBER@gcp-sa-discoveryengine.iam.gserviceaccount.com`, so Vertex AI Discovery Engine points at the business bucket WITHOUT copying data — the personal $1K credits absorb 100% of RAG query cost
- The **v2.2 dataflow diagram** — the only diagram in the folder that stitches Media Daemon → Moonshine STT → OmniRoute/LocalAI → Executor/Query Core → Horizons UI (verification) → Frontier → Reasoning Bank → Home Assistant (cross-agent audit + log compilation) → Red Agent Auditor Sandbox → (Match Nope → Drop) / (Pass → Local Obsidian + GCS) → GCP Training Flywheel (Vertex + Unsloth/Axolotl GRPO) → new weights back to edge
- The **explicit `roles/storage.objectViewer`** IAM role name — the specific role, not just "read access"
- **`RECORD_ID` example**: `SKILL_POCOCK_GRILL_001` with `target_runtime: PRIME_AGENT_RLM` — concrete manifest.jsonl instance

---

## Findings — unique increments (F6 is the anchor)

### F1 `Example 1`

Unique increment: **crisp 5-layer conceptual flow** (raw_pdf → wiki_md → recall_jsonl → repos/scripts → INDEX.jsonl) with a "why this pipeline works" 3-point justification (speed / context preservation / traceability). Compact enough to embed in a quick reference card.

### F2 `Example 2` (Gdoc)

Unique increment: the **explicit human-cognitive→AI-engineering mapping** of 3 memory types (Episodic=chat history / Semantic=facts / Procedural=tool-execution-schemas) with the physical layout (`memory_pipeline/{storage/saver.py, injection/context_loader.py, recall/search_engine.py, types/{episodic.py, semantic.py, procedural.py}}`).

### F3 `Example 3`

Unique increments:
- **The direct A-vs-B side-by-side of the two schema systems** (4-tier vs 5-tier) — F3 is the doc that SETS UP F6's reconciliation
- **The 4-type cognitive→engineering→RLVR-role table** (Episodic / Procedural / Semantic / Working) with per-type function in the KAG-recurse/RLVR loop — F3 has the mapping table that F6 later formalizes
- **The 4-step Flow of Training loop** (Working Memory → Episodic Log → RLVR verifier → backprop into Procedural/Semantic weights) — cleaner statement than F6's later diagram

### F4 `Example 4`

Unique increments:
- Concrete file names inside each tier (`HORIZONS_state_and_corrections_MASTER.md`, `ARCHITECTURE_REVIEW_v3_amendment.md`, `N0_V4_ARCHITECTURE_v3.md`, `BUILD-ACTION-PLAN.md`, `FAILURE_LOG_SESSION_20260527.md`, `weekly_audit_prompt.md`, `NeuroOmni_agy_build_pack.md`, `GENIEX-DAEMON-PLAN.md`, `llm-wiki-termux-setup-full-notes.md`)
- The **legacy references** (`Stanford AI Index`, `MEMO_ A Modular Framework for Training a Dedicated Memory Model`, `Together AI OSCAR`, `NVIDIA Polar`, `Meet GitAgent`, `OpenAI Symphony`, `CopilotKit`, `GitHub Spec-Kit`, `OmniVoice Studio`, `Hexo Labs SIA`, `Liquid AI LFM2.5-8B-A1B`) — the specific external research/repo references the user has flagged as reference material
- The **`FUTO Keyboard` reference** — voice input models pointer that appears nowhere else

### F5 `Question` (Gdoc)

Unique increment: **the user's actual verbatim question that prompted F6's reconciliation matrix.** Speaker attribution per hard rule 4. This is the human question that "we've said a million times" got a rigorous answer to — preserve for the human-in-the-loop record.

### F6 `Response.` ★ GOLD STANDARD (anchor with S6)

(Baseline — see anchor section above)

---

## CLOSE_2_TARGET — unique increments

### C1 `ACFrOgDK...md` (30KB, PDF conversion)

Unique increment vs S4 (which C1 duplicates): **it is the raw PDF-conversion version.** Same source text as S4 but as flat text instead of a Gdoc. **If a specific formatting artifact matters** (line breaks preserved, code blocks fenced differently), C1 might be preferred for programmatic re-parsing; otherwise S4 (the Gdoc) is easier to edit. Not both.

### C2 `AESOP XI: Autonomous Edge-Computing Architecture Blueprint..txt`

Unique increments over GLM-PT.1 (A6) — this is a distinct v2.2 declaration:
- **"v2.2-Production-Ready"** version tag — the ONLY doc claiming production readiness
- The **6-phase priority sequence in prose form** (as opposed to A6's tabular form) with `\rightarrow` LaTeX-style arrows for the Concierge Flow — reads as an operating manual, not a spec
- The 5-agent Home Node topology with the same names as A10 but with **micro-defined responsibilities** ("Home Assistant = manages real-time cross-agent auditing during live inference sessions, aggregates daily execution logs, compiles draft automation scripts, and packages raw telemetry pairs for downstream training")
- **`service-PERSONAL_PROJECT_NUMBER@gcp-sa-discoveryengine.iam.gserviceaccount.com`** — same specific principal as A10 (cross-corroborates)
- The **10-repo `master_workspace/` tree** (not 12 like GLM-PT.1) — leaner variant worth reconciling
- The **universal JSONL marker schema** with `record_id`, `document_path`, `category`, `target_runtime`, `metadata.title/description/primary_tools/required_context_keys`, `retrieval_tokens`, `entry_points.repl_command/jsonrpc_method` — most complete JSONL marker schema in the folder

---

## Contribution graph — where each unique increment lands

If we were to build a repo tomorrow, here is which folder-1 document supplies which artifact:

| Artifact | Sourced from |
|---|---|
| 5+1 Tier vault_root schema | **S6** (baseline) + **F6** (reconciliation) — anchor pair |
| Manifest.jsonl schema per tier | S6 (protocol) + C2 (universal marker instance) + A10 (record example) |
| 5 doc-type taxonomy (Tool/Skill/Reference/Memory/Data) | **A1** (canonical statement) |
| Full novaexopia sub-tree | **A1** (only place at that granularity) |
| `file_administrator.yaml` + `oeracle_helpdesk.yaml` | **S7/S8** (only source) |
| NopeDataBank position in tree | S7/S8 + A1 |
| Œræcle profile + persona | S7/S8 + A1 |
| Concurrency policy (DISALLOW_NPU_OVERLAP + memory floors) | **S7/S8** (only source) |
| 3-APK Concierge Loop (5-step) | **S5** (only source at that step-granularity) |
| Web-socket / Webview bridge architecture | S5 |
| AndroidManifest daemon isolation pattern | **A3** (only source) |
| ASharedMemory + SCM_RIGHTS FD passing | **A3** (only source) |
| ForegroundService LMK-bypass Kotlin | **A3** (only source) |
| GCP Cross-Account Handshake bootstrap script | **1B.1** (only source) |
| Setup-aesop.sh + convert-raw-to-md.py + generate-jsonl-markers.py | **1B.1** (only source) |
| ECC internal routing (honey-crush / nexus-mapper / ecc-planner / px-reader) | **1B.1** (only source) |
| SKILL.md format spec | **1B.1** (only source) |
| 15-gap list | **A6** + **1B.1** (corroborate) |
| 6-priority phase table with NOW/LATER | **A6** (only source) |
| LocalAI vs OmniRoute comparison | **A6** (only source) |
| 5-agent Home Node topology (Beta) | **A10** + **C2** (corroborate) |
| 4-node hardware manifest (Alpha/Beta/Gamma/Delta) | **A10** + **C2** (corroborate) |
| Universal JSONL marker schema instance | **C2** (most complete) + A10 |
| RAM math (9B Q4_0 = 5.45GB + 0.5-1GB KV) | **1B.2** (only concrete) |
| QAIRT env-var block | **1B.1** + **1B.2** (corroborate) |
| Xçineribus motto + Æsc/Æyre glyphs + ASCII trick | **S3** (only source) |
| USER-CORRECTIONS on stale architecture | **S4** (only source of live annotations) |
| Cognitive→engineering memory-type mapping | **F2** + **F3** + **F6** (corroborate; F3 has the crispest table, F6 has the formal reconciliation) |
| Named legacy reference materials (Stanford AI Index, MEMO, OSCAR, Polar, etc.) | **F4** (only source) |
| SQLite file-lock isolation guarantee | **A8** (only source) |
| Continual Harness paper (external reference) | **S9** (verbatim) |
| Brand narrative (Ever-evolving ecosystems...) | **S3** |
| GLM-5.2 pricing + 1M ctx call-out | **A4** (only source) |
| llm-wiki compiler + static site pattern (127.0.0.1:8765) | **A7** (only source) |
| AESOP_XI_Skill_Onboarding_Template JSON schema | **A9** (only source) |
| Early-trend-scraper (daily_scraper.py + stack_analyzer.py + trending_databank.jsonl) | **A1** (only source at file-tree granularity) |

**Every file except A2, A5, C1 delivers at least one unique artifact.**

---

## Kill-list (revised — narrow)

Only truly redundant items:
1. **A2** `Convert Google Docs to Markdown - Google Search` — a search-results dump; extract bookmarklet URL if present, otherwise trash.
2. **C1** `ACFrOgDK...md` — PDF re-conversion of S4's Gdoc; pick one representation (Gdoc = edit-friendly; PDF text = re-parse-friendly), trash the other.
3. **1B.2 + 1B.3** may be archived AFTER their unique increments (RAM math, QAIRT env block, Fallback hierarchy tabular form) are extracted — the increments themselves are keepers.

Everything else in this folder contributes at least one unique artifact.

---

## Feed-forward to folder 2

Folder 2 (PRPSD FILE TREE, 15 files) will be audited against **S6 + F6** as the schema anchor pair. For each tree in folder 2, I will surface:
- Which specific tier/directory choices it makes that S6/F6 don't
- What it OMITS that S6/F6 include
- Whether it superseded or predates S6/F6

Same lens applied to every subsequent folder: **what does THIS doc uniquely add?**

---

*Folder 01 v3 audit complete. v2's kill-list is preserved as the operational digest; v3 is the value-mining lens. v1 remains as the initial in-progress skeleton for provenance.*
