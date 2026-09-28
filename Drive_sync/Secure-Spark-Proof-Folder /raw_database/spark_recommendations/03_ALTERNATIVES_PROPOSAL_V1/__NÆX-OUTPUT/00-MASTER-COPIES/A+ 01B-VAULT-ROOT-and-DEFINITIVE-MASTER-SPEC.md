# NovÆxorpus — Master Doc 01
## The 5+1 Tier Vault Root Schema & Definitive Master Specification

> **Xçineribus, in-variis-nunquam-varius, Novi-Æxentis-Copiæ, Vincent**
> — *From the ashes, unwavering in the midst of adversity, new forces of abundance conquer.*
>
> **NovÆxorpus** — the hardened, unbreakable body of knowledge. This document is the S-tier canonical spec for the vault: what lives where, who is allowed to touch it, how retrieval works, and how the Red Auditor keeps the flywheel honest without ever being visible to the enterprise it audits.

**Applies to:** the vault repo (`novae-xorpus`) and every mirrored-in project repo it hosts, whether same-device (symlink) or cross-device (git clone).

---

## Provenance table — what this document is made of

| § | Section | Source | What was kept | What was cut & why |
|---|---|---|---|---|
| 1 | Vault tree (canonical) | S1 `1A vault_root/.txt`, S2 `1B- vault_root/.txt`, S6 `Definitive Master Specification.txt` | Emoji-coded tier labels (from S1/S2), full 5+1 tree (from S6), tier access-control matrix (S6) | Duplicated tree-block from S2 (kept S1's layout as the canonical form; S2's ordering was near-identical) |
| 2 | Definitive Master Spec (verbatim core) | S6 | Everything — this is the anchor. Rewritten only where the Red Agent placement changes | Nothing cut; only §7 rerouted (see Red Agent Isolation Contract) |
| 3 | 5+1 Tier reconciliation matrix | F6 `Response.` + F3 `Example 3` (the 4-vs-5 tier compare that set F6 up) | The reconciliation matrix, the cognitive→engineering memory-type mapping, the KAG/RLVR loop diagram, F5's user question as attribution | Duplicated wall of text between F3 and F6 — kept the F6 tables + F3's Flow-of-Training 4-step |
| 4 | 5 Doc-Type Manifest Taxonomy | A1 `The Manifest Taxonomy (The 5 Document Types)` | The 5-type classification (Tool/Skill/Reference/Memory/Data), full novaexopia sub-tree, `early-trend-scraper` subsystem, `data_vault_sandbox` "NO RCLONE" rule, named model roles (`jeanie_x_qwen_0.8b`, `openwiki_cli_glm`, `helpdesk_installer_agent`) | Second repo-tree at bottom of A1 (`__NovÆ-Core/COGNITIVE_PLANE/…`) — kept the primary tree; this alt-organizational lens lands in Master Doc 02 as a "by-function" cross-view |
| 5 | Cognitive → Engineering memory-type mapping | F2 `Example 2`, F3 `Example 3` | F2's `memory_pipeline/{storage/, injection/, recall/, types/{episodic, semantic, procedural}}` layout, F3's 4-type table with RLVR role column, F3's 4-step Flow of Training | F2's opening "yes you have the exact right intuition" preamble (Q&A framing not needed in spec form) |
| 6 | Red Agent Isolation Contract (NEW) | Operator note (project prompt: "the red agent…is supposed to be incognito and unknown to the entire rest of the Enterprise") + S6 §7 rewritten | S6's End-of-Day P2P Sync + Cross-Auditor flow, sandbox evaluation pass/fail dispositions | S6's `05_episodic_logs/red_audit_sandbox/` path — moved out to a sibling `.red/` per operator rule (see §6) |
| A | Config Profiles (Appendix) | S7 + S8 `ARCHITECTURE BLUEPRINT-(Pt.1) & (Pt.2)` | Both YAML profiles (`file_administrator.yaml`, `oeracle_helpdesk.yaml`), the concurrency policy (`DISALLOW_NPU_OVERLAP`, memory floors, IO priority steering), the launch commands, NopeDataBank + Œræcle references | The "src vs scripts" preamble from S7 (belongs in Master Doc 03 on repo structure, not here) |
| B | Bootstrapping scripts (Appendix) | 1B.1 `OpenRouter Chat Sun Aug 30 2026.md` | Pointers + call signatures for `setup-aesop.sh`, `convert-raw-to-md.py`, `generate-jsonl-markers.py`; the QAIRT env-var block | Full script bodies live as real files in `novae-xorpus/tools/` — this doc references them, doesn't duplicate them |
| C | Multi-process daemon IPC contract (Appendix) | A3 `Official Google Developer Documentation for System Architecture…` | AndroidManifest colon-prefix isolation pattern, `ASharedMemory` + `PROT_READ` drop, UNIX abstract-namespace sockets + `SCM_RIGHTS` FD passing, `startForeground + START_STICKY` LMK bypass. Verbatim per hard rule 3 (external Google reference). | Nothing cut — this is reference material, preserved whole |
| D | 3-APK Concierge Loop (Appendix) | S5 `Copy of The 3-APK Native Topology & The Concierge Dataflow.` | The 5-step Concierge Execution Loop, WebSocket/Webview bridge architecture, APK-level responsibility split, the "greenfield voice" declaration | Nothing — this is the load-bearing 3-APK spec |
| E | 4-Node Hardware Manifest (Appendix) | A10 `The Complete Systems Architecture Blueprint. Accurate launch`, C2 `AESOP XI: Autonomous Edge-Computing Architecture Blueprint..txt` | 4-node table (Alpha/Beta/Gamma/Delta), 5-agent Home Node topology, GCP Cross-Account IAM Handshake pointer, v2.2 dataflow diagram, `service-<PROJECT_NUMBER>@gcp-sa-discoveryengine.iam.gserviceaccount.com` principal, `roles/storage.objectViewer` role, `gs://business-secure-vault-bucket` | Overlapping 6-priority sequence text (that lives in Master Doc 04 = execution roadmap) |
| F | The 15-Gap List (Appendix) | A6 `GLM-PT.1-MASTER.DOCUMENT.md` + 1B.1 corroboration | The full numbered 15-item list of what older architecture docs get wrong | The rest of A6's 10-part structure — those parts feed Master Docs 02/03/04 instead of duplicating here |
| G | External Reference Papers (Appendix — pointers only) | S9 `Continual harness online adaptation…`, F4 `Example 4` reference list | Named pointers + citations for: Continual Harness (Prime Agent basis), Stanford AI Index, MEMO memory model, Together AI OSCAR, NVIDIA Polar, Liquid AI LFM2.5-8B-A1B, Qualcomm QAI Hub model bundles, FUTO Keyboard | S9's full paper text (91KB) — lives as its own file under `reference-papers/`, not inlined |
| H | Skill Onboarding JSON Schema (Appendix) | A9 `Architectural realignment.docx` | The full `AESOP_XI_Skill_Onboarding_Template` schema (skill_identity + hardware_execution_routing + runtime_permissions_bounds) | Everything else in A9 — largely superseded by GLM-PT.1 |
| I | User Corrections Log (Appendix) | S4 `Clarifying -Clean Text-…` | Every one of your inline annotations verbatim (they are the highest signal in the folder) | The stale wrapper doc S4 annotates — annotations kept, wrapper dropped |
| J | Branding banner + tagline strip | S3 `Branding ligature` | Motto, Æsc🌳et🦁Æyre glyph pairing, dumbass-proof line, Horizons UI tagline, ASCII trick guidance for Android string resources | Formatting-only variants |
| K | RAM math + fallback hierarchy | 1B.2 `fusion-response 2026-08-30.md`, 1B.3 (Part 8 continuation) | 9B Q4_0 RAM math (5.45GB weights + 0.5–1GB KV = 6–6.5GB total; 9–12GB available; 2.5–6GB headroom); Fallback hierarchy (9B npu → 9B hybrid → 4B npu) | Overlapping prose that GLM-PT.1 (A6) already carries |
| L | SQLite concurrency guarantee | A8 `SQLite.txt` | `better-sqlite3` file-lock isolation at `~/.omniroute/*.db` — no clash with ECC hooks or Prime Agent; only collision surface = other MCP servers on `localhost:20128` | Nothing — 2KB doc, fully preserved |
| M | GLM-5.2 economics call-out | A4 `The Consolidated Master README` | 1M-token context, ~$1.40/M input tokens via OpenRouter, `z-ai/glm-5.2` model id | Everything else in A4 — superseded by A6 |
| N | Graphify + Obsidian + NotebookLM integration recipe | A7 `Integrating Graphify, Obsidian, and NotebookLM.docx` | `uv tool run graphify . --obsidian --output wiki/ast/` invocation, `llm-wiki` compiler (Pratiyush/llm-wiki) with `127.0.0.1:8765` static-site pattern, per-tier output routing (wiki/code, wiki/ast, raw/research) | The bulk of the search-results narrative — kept only the operational commands |

**Skipped outright from folder 1:**

| File | Why skipped | Where its increment (if any) is preserved elsewhere |
|---|---|---|
| A2 `Convert Google Docs to Markdown - Google Search.md` | Pure Google-search-results dump; the only kernel of value is a reference to the "clean text" bookmarklet, and S4 already annotates that bookmarklet as **"just fluff about a tool it was ultimately never able to utilize"** — the tool is dead, no reason to preserve documentation for it | S4's annotation is our record that this tool is dropped |
| A5 `GLM-PT.2-fusion-response.md` | Strict subset of A6 `GLM-PT.1-MASTER.DOCUMENT.md` — smaller, earlier draft that A6 consolidates. Line-by-line diff shows no content in A5 that isn't in A6 | Nothing — fully covered by A6 |
| C1 `ACFrOgDK…md` (PDF conversion) | Verbatim PDF re-conversion of S4's Gdoc — same text, different container. Keeping both is duplication for no gain; picked the Gdoc form (S4) because it's edit-friendly and preserves your inline annotations natively | S4's Gdoc form is the canonical | 

---

## Part 1 — The Canonical Vault Tree

The vault is a **5+1 Tier Cognitive Repository** rooted at `vault_root/`. Every project repo mirrored into `novae-xorpus/projects/` shares this same schema; the vault itself is one instance of it, plus a root-level pointer set (MAP.md + manifest.jsonl) that binds project mirrors together.

```
📦 vault_root/                        # ⚪ [METACOGNITIVE] — the root
├── 📍 MAP.md                          # Master human-readable index & ontology graph
├── 📇 manifest.jsonl                  # Root-level RAG registry & global sha256 table
│
├── 🟢 01_raw_sources/                 # [TIER 1: COLD ARCHIVE] — sensory ground truth (READ-ONLY)
│   ├── 📇 manifest.jsonl              # Local RAG catalog of raw assets & provenance
│   ├── 📕 pdf/                        # Source whitepapers, specs, data sheets (*.pdf)
│   ├── 🎬 media/                      # Video captures, audio memos, screen recordings (*.mp4, *.wav, *.png)
│   └── 📄 text/                       # Web scrapes, raw transcripts, raw API payloads (*.txt, *.html)
│
├── 🟣 02_wiki_md/                     # [TIER 2: THE LLM WIKI] — semantic memory (OpenWiki TUI)
│   ├── 📇 manifest.jsonl              # Local RAG catalog of conceptual nodes & graph links
│   ├── 💡 concepts/                   # Atomic linked notes, theory, domain models (*.md)
│   ├── 🏛️ architectures/             # System blueprints, data flows, interface specs (*.md)
│   ├── 🏷️ entities/                   # Registries, schema contracts, hardware profiles (*.md)
│   └── 🧭 indexes/                    # Maps of Content (MOCs) & taxonomy hubs (*.md)
│
├── 🟡 03_recall_cache/                # [TIER 3: WORKING MEMORY ACCELERATOR] (REBUILDABLE)
│   ├── 📇 manifest.jsonl              # Local RAG catalog of vector & chunk shards
│   ├── ⚡ jsonl/                      # Pre-tokenized passages for prompt injection (*.jsonl)
│   ├── 🧮 vectors/                    # Dense vector indices (*.bin, *.faiss, *.hnsw)
│   └── 🗃️ kv_store/                   # Low-latency KV lookups (*.db, *.json)
│
├── 🔵 04_skills_runtime/              # [TIER 4: PROCEDURAL REPERTOIRE] (VERSION-CONTROLLED)
│   ├── 📇 manifest.jsonl              # Local RAG catalog of all extracted skills & tools
│   ├── 🎯 prompt_skills/              # Modular SKILL.md prompt definitions (*.md, *.yaml)
│   ├── 🛠️ extracted_tools/            # Deterministic tools mined from documentation
│   │   ├── cli/                       # Extracted shell utilities (*.sh)
│   │   └── wrappers/                  # API wrappers & micro-functions (*.py)
│   ├── ⚙️ runtimes/                   # Master operational scripts & execution hooks (*.py, *.sh)
│   └── 🛡️ policies/                   # Validation guards, retry policies, schemas (*.json, *.yaml)
│
└── 🔴 05_episodic_logs/               # [TIER 5: EPISODIC TELEMETRY] (APPEND-ONLY)
    ├── 📇 manifest.jsonl              # Local RAG catalog of sessions & verifier runs
    ├── 📲 daily_driver_sync/          # Ingested logs from edge device sessions (*.jsonl)
    ├── ⏱️ trajectories/              # Multi-model traces: Query / Executor / Frontier (*.jsonl)
    ├── ⚖️ rlvr_verifiers/            # Graded rewards, assertion outcomes (+1.0 / −1.0) (*.jsonl)
    └── 🧹 hygiene_reports/            # Schema integrity audits, broken-link checks (*.md)

# INVISIBLE SIBLING — see §6 Red Agent Isolation Contract
# .red/ is deliberately UNLISTED in every MAP.md / manifest.jsonl / MOC.
# The visible tree does not know it exists.
```

### Tier access-control matrix

| Tier | Write policy | Who writes | Who reads | Rebuildable? |
|---|---|---|---|---|
| Root MAP.md | Agent-updated on any tree change | Files Executive Agent | All | No — reflects truth |
| Root manifest.jsonl | Append/sync on any file event | Files Executive Agent | All | Yes (regenerable from tree) |
| 01_raw_sources | Write-once on intake, never mutate | Human + ingestion agents | All | **No — immutable ground truth** |
| 02_wiki_md | Managed via OpenWiki TUI | Files Executive Agent (GLM-5.2) | All | Yes (from raw_sources) |
| 03_recall_cache | Deleted & rebuilt safely | Any indexing agent | All | **Yes — designed to be wiped** |
| 04_skills_runtime | Version-controlled (git) | Skill/tool extraction agents + human | All | No (git-tracked) |
| 05_episodic_logs | Append-only during runs | All executing agents | All | No (audit trail) |
| `.red/` (INVISIBLE) | Air-gapped write only | Red Auditor Agent only | Red Auditor Agent only | No |

---

## Part 2 — The Definitive Master Specification (v3.0)

*Reproduced from S6. Only §7 has been rewritten to isolate the Red Auditor per §6 of this document. Every other paragraph is preserved.*

### 2.1 Core Architectural Invariants

The planning agent MUST enforce the separation of cognitive memory layers across the filesystem. These invariants are hard rules:

1. **Sensory Immutability (Tier 1):** Never modify, overwrite, or delete assets in `01_raw_sources/`. All raw inputs are read-only sources of truth.
2. **Human-Machine Decoupling (Tier 2 vs. Tier 3):** Human-readable semantic knowledge lives in `02_wiki_md/` (`.md`). Machine-readable retrieval chunks live in `03_recall_cache/` (`.jsonl`, vectors). Never dump raw tabular JSONL or vector embeddings into the wiki layer.
3. **Procedural vs. Episodic Separation (Tier 4 vs. Tier 5):** Executable skills, scripts, and policies belong in `04_skills_runtime/`. Trajectory traces, error logs, and verifier evaluations belong in `05_episodic_logs/`. Never place runtime logic inside logging directories or vice versa.
4. **Metacognitive Priming:** Before initiating multi-step tasks, read `MAP.md` or parse the root `manifest.jsonl` to resolve entity references rather than performing blind recursive scans across the filesystem.
5. **LLM Wiki Protocol (`02_wiki_md/`):** The semantic vault operates as an organization-wide wiki standard governed directly by the **Files Executive Agent** via the **OpenWiki TUI** — see Appendix A profile `file_administrator.yaml`.
6. **Dual Extraction Mandate:** Every document ingested into the ecosystem must be systematically screened for both **Procedural Skills** (prompt templates, behavioral heuristics) and **Executable Tools** (scripts, wrappers, deterministic CLI invocations).
7. **Red Auditor Gatekeeping (rerouted — see §6):** No episodic execution trace or generated script may enter the recursive training stream without passing an isolated sandbox evaluation by the Red Auditor Agent. **The Red Auditor is not enumerated in any visible manifest and its evaluation surface is invisible to every other enterprise component.**
8. **Universal Source of Truth:** All local auditor nodes and the sandboxed Red Auditor must evaluate claims and script outcomes against the shared master memory bank and database.
9. **Distributed Manifest Coverage:** Every repository root and major structural subsystem must maintain its own local `manifest.jsonl` to power low-overhead hierarchical RAG retrieval.

### 2.2 Metacognitive Root

**`MAP.md`** must maintain top-level navigation links using Markdown cross-references to key notes in `02_wiki_md/` and entry points in `04_skills_runtime/`.

**`manifest.jsonl` (Root)** is the master catalog mapping file paths, tiers, cryptographic checksums, and cross-tier linkages:

```json
{"id": "SRC-0042", "path": "01_raw_sources/pdf/spec_v1.pdf", "tier": 1, "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", "last_modified": "2026-09-03T17:00:00Z", "linked_wiki": "02_wiki_md/architectures/spec_v1.md"}
```

### 2.3 Tier 1 — `01_raw_sources/` (Cold Archive & Sensory Buffer)

- **Write Policy:** Write-once upon raw intake. Never mutate or reformat existing files.
- **Naming Convention:** `YYYYMMDD_source_title.[ext]` (lowercase, snake_case).
- **Scope:** Source PDFs, audio transcripts, sensor captures, video recordings, raw scrapes.

### 2.4 Tier 2 — `02_wiki_md/` (The LLM Wiki Layer)

- **Write Policy:** Managed via **OpenWiki TUI** by the **Files Executive Agent** (GLM-5.2 profile — see Appendix A).
- **Format:** Pure Markdown with strict YAML frontmatter:

```yaml
---
id: wiki_rag_indexing_protocol
tier: 2
type: architecture
created: 2026-09-03
updated: 2026-09-03
author: files_executive_agent
sources:
  - "01_raw_sources/pdf/rag_system_spec.pdf"
extracted_skills:
  - "04_skills_runtime/prompt_skills/manifest_sync.md"
extracted_tools:
  - "04_skills_runtime/extracted_tools/cli/build_manifest.py"
tags:
  - llm_wiki
  - openwiki
  - indexing
---

# RAG Indexing Protocol

## Context & Definition
Structural mechanism for keeping the LLM Wiki synchronized with high-speed caches...

## Architectural Interfaces
The [[manifest_registry_spec]] defines how this node is indexed by the [[files_executive_agent]].

## References
- [[hierarchical_manifest_routing]]
- [[procedural_tool_extraction]]
```

### 2.5 Tier 3 — `03_recall_cache/` (Working Memory Accelerator)

- **Write Policy:** Agent-generated during build or indexing steps. **May be deleted and rebuilt safely.**
- **Chunk Schema** (`03_recall_cache/jsonl/*.jsonl`):

```json
{"chunk_id": "CHK-8901", "parent_doc": "02_wiki_md/concepts/rlvr.md", "tokens": 256, "content": "RLVR verifiers score execution traces against deterministic unit tests...", "metadata": {"tier": 2, "topic": "rlvr"}}
```

### 2.6 Tier 4 — `04_skills_runtime/` (Procedural Memory: Skills & Tools)

- **Write Policy:** Version-controlled tooling, prompts, and instructions.
- **Prompt Skill Format** (`prompt_skills/`): Standard modular SKILL.md format — YAML frontmatter with purpose, required inputs, tool dependencies, output schemas.
- **Extracted Tools** (`extracted_tools/`): Standalone executable code blocks extracted from documentation. Non-interactive scripts with standard exit codes (0 = success, non-zero = error).
- **Policies** (`policies/`): See Appendix H for the `AESOP_XI_Skill_Onboarding_Template` JSON schema every new skill/tool must validate against.

### 2.7 Tier 5 — `05_episodic_logs/` (Episodic Memory & Telemetry)

- **Write Policy:** Append-only during agent task execution.
- **Trajectory Schema** (`trajectories/YYYYMMDD_session.jsonl`):

```json
{"timestamp": "2026-09-03T17:01:35Z", "step": 1, "task_id": "TASK-104", "prompt_hash": "a1b2c3", "tool_call": "run_linter", "exit_code": 0, "response_snippet": "OK"}
```

- **RLVR Log Schema** (`rlvr_verifiers/YYYYMMDD_eval.jsonl`) — includes the invisible Red Auditor's verdict as a *signal only*, per §6:

```json
{"timestamp": "2026-09-03T17:01:40Z", "task_id": "TASK-104", "verifier_id": "syntax_test", "reward": 1.0, "feedback": "All assertions passed.", "red_verdict": "pass"}
```

The `red_verdict` field is populated by an out-of-band process that never identifies itself, never writes to a named subfolder of `05_episodic_logs/`, and cannot be enumerated or introspected by any other enterprise component. Its actual sandbox and evaluation trajectories live in `.red/` — see §6.

### 2.8 The LLM Wiki Protocol & OpenWiki Files Executive Agent

`02_wiki_md/` is the persistent organizational spine. The Files Executive Agent manages it through the OpenWiki TUI (GLM-5.2 profile — see Appendix A):

1. **TUI-Driven Lifecycle Management:** Monitors file additions, moves, renames, and refactors across all tiers.
2. **Deterministic Linking & Backlinks:** Automatically verifies bidirectional Markdown links (`[[entity_name]]`), ensuring the LLM Wiki remains an intact graph without orphaned concepts.
3. **Extraction Intake Coordination:** Acts as the bridge between incoming raw sources in `01_raw_sources/`, synthesizing structured knowledge into `02_wiki_md/`, and passing extracted procedural artifacts to `04_skills_runtime/`.
4. **Manifest Synchronization:** Whenever the agent modifies a node in `02_wiki_md/`, it immediately writes updated hashes, token counts, and entity tags to both `02_wiki_md/manifest.jsonl` and the root `manifest.jsonl`.

### 2.9 Universal Skill & Tool Extraction Engine

Every ingested document is passed through a dual-channel extraction filter:

- **Skill Extraction:** Reasoning heuristics, step-by-step workflows, formatting/prompt templates, edge-case recovery rules → `04_skills_runtime/prompt_skills/*.md`
- **Tool Extraction:** Standalone shell/python scripts, API wrappers & micro-utilities, CLI invocation syntax & flags, data conversion routines → `04_skills_runtime/extracted_tools/{cli/*.sh, wrappers/*.py}`

Extraction classification rules:
1. **Targeting Skills:** If a passage describes how to reason, how to structure an analysis, or how to coordinate a sequence of tasks → markdown skill with YAML frontmatter into `prompt_skills/`.
2. **Targeting Tools:** If a passage contains executable code, CLI flags, API request formats, or data transformation utilities → executable script (`.py` or `.sh`) with explicit argument parsing into `extracted_tools/`.
3. **Registration:** Update the local `04_skills_runtime/manifest.jsonl` immediately upon extraction.

### 2.10 Hierarchical `manifest.jsonl` Specification for Distributed RAG

Every directory root holds a dedicated `manifest.jsonl` file. Prevents full-vault scanning during localized RAG operations. Every line strictly adheres to this schema:

```json
{
  "id": "UUID-OR-PATH-HASH",
  "path": "relative/path/to/file.ext",
  "tier": 4,
  "category": "extracted_tool",
  "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "tokens": 412,
  "semantic_summary": "CLI utility to extract audio streams from MP4 video containers.",
  "entities_extracted": ["ffmpeg", "audio_processing", "mp4_to_wav"],
  "skills_tools_extracted": [
    {"type": "tool", "name": "extract_audio_stream", "path": "04_skills_runtime/extracted_tools/cli/extract_audio.sh"},
    {"type": "skill", "name": "audio_preprocessing_policy", "path": "04_skills_runtime/prompt_skills/audio_prep.md"}
  ],
  "provenance_source": "01_raw_sources/pdf/media_processing_guide.pdf",
  "last_synced": "2026-09-03T17:05:00Z"
}
```

**RAG Query Traversal Protocol:**
1. **Directory-Level Scope Matching:** Inspect root `manifest.jsonl` to identify candidate subdirectories.
2. **Localized Search:** Read only the relevant sub-tier `manifest.jsonl` (e.g., `04_skills_runtime/manifest.jsonl`), matching semantic summaries and entities.
3. **Targeted Ingestion:** Only the exact chunk or tool indicated by the manifest record is loaded into active Working Memory.

### 2.11 Bash scaffolding script

```bash
#!/usr/bin/env bash
set -euo pipefail
echo "===> Initializing 5+1 Tier Cognitive Repository Architecture..."

# 1. Scaffold all directory hierarchies
mkdir -p 01_raw_sources/{pdf,media,text}
mkdir -p 02_wiki_md/{concepts,architectures,entities,indexes}
mkdir -p 03_recall_cache/{jsonl,vectors,kv_store}
mkdir -p 04_skills_runtime/{prompt_skills,extracted_tools/{cli,wrappers},runtimes,policies}
mkdir -p 05_episodic_logs/{daily_driver_sync,trajectories,rlvr_verifiers,hygiene_reports}

# 2. Touch distributed manifest.jsonl files across all tiers
touch manifest.jsonl 01_raw_sources/manifest.jsonl 02_wiki_md/manifest.jsonl \
      03_recall_cache/manifest.jsonl 04_skills_runtime/manifest.jsonl \
      05_episodic_logs/manifest.jsonl

# 3. Initialize Root MAP.md if absent — see MAP.md template in §2.2
[ -f MAP.md ] || touch MAP.md

# 4. INVISIBLE — .red/ is scaffolded separately by the Red Auditor's own bootstrap,
#    NEVER by this script. This script must not know that path exists.
```

---

## Part 3 — 5+1 Tier Reconciliation Matrix (from F6 + F3)

**Root question (F5, verbatim, speaker attribution preserved):** *"Please resolve the inconsistencies in the above two documents as compared with this recent query output, please use these references to produce a clear definitive document with rich text headers, color graphs, tables and visual aids for clarity."*

**Answer:** two prior schema systems (A = 4-tier, B = 5-tier) both drifted for different reasons. The reconciliation collapses them into 5+1 Tier as above. Origin of drift:

1. **System A conflated Procedural with Episodic** (bundled executable logic + telemetry into `/automation_scripts/`). Cognitive architecture requires strict decoupling.
2. **System A merged the metacognitive index with Skill Definitions** (put "The Almanac" and "Skill Definitions" under `/inference_skills/`). System B correctly extracted the global directory as a distinct root artifact (MAP.md + manifest.jsonl).
3. **System B added `/recall_jsonl/`** as machine-cache to shield the human-readable wiki from destructive automated overwrites — correct instinct, adopted as Tier 3.

**Reconciliation matrix:**

| Component | System A (4-Tier) | System B (5-Tier) | Cognitive Equivalence | Unified 5+1 |
|---|---|---|---|---|
| Ground Truth Archive | `/raw_sources/` | `/raw_pdf/` | Sensory Perceptual Store | `01_raw_sources/{pdf,media,text}` |
| Synthesized Knowledge | `/master_wiki/` | `/wiki_md/` | Semantic Memory | `02_wiki_md/{concepts,architectures,entities,indexes}` |
| Compiled Acceleration | *(missing)* | `/recall_jsonl/` | Working Memory Extension | `03_recall_cache/{jsonl,vectors,kv_store}` |
| Behavioral Logic & Tools | `/inference_skills/` | `/repos/ & /scripts/` | Procedural Memory | `04_skills_runtime/{prompt_skills,extracted_tools/{cli,wrappers},runtimes,policies}` |
| Trajectory & Telemetry | `/automation_scripts/` *(logs)* | *(missing)* | Episodic Memory | `05_episodic_logs/{daily_driver_sync,trajectories,rlvr_verifiers,hygiene_reports}` |
| Global Routing Directory | "The Almanac" (buried in Tier 3) | Tier 5 MAP.md / Manifest.jsonl | Metacognition / Hippocampal Index | Root: `MAP.md` + `manifest.jsonl` |

**Cognitive → Engineering memory-type mapping** (from F3, cleaner form than F6):

| Memory Type | Human Brain (Cognitive) | AI System Architecture (Engineering) | Function in KAG Recurse / RLVR |
|---|---|---|---|
| **Episodic** | Personal history (remembering last Tuesday's failed presentation) | Execution Logs / Vector DBs — time-indexed record of past interactions, runs, agent trajectories | Logs Attempt #42 (Prompt → Line 114 Code → Stack Overflow → Verifier Reward −1.0) |
| **Procedural** | Habits & skills (muscle memory, touch-typing) | Algorithmic Policies / Weights — baked-in behavioral habits | Permanent intuition model develops via RLVR to backtrack and rewrite when it hits an error state |
| **Semantic** | Facts & concepts (Paris = capital of France) | Static Parametric Weights — vast database of facts, syntax, language rules | Foundational knowledge of programming language syntax (what a `while` loop is) |
| **Working / Short-Term** | Mental workbench (4–7 items, 20–30s, phone number about to dial) | The Context Window — active chat history + current tokens loaded in prompt | Active variables, prompt system instructions, current recursive execution branch |

**Flow of Training loop** (F3 verbatim — cleanest 4-step statement):

1. Agent uses **Working Memory** (Context Window) to execute a step.
2. Logs success/failure into **Episodic Memory** (external log / vector DB).
3. RLVR verifier analyzes those episodic logs → distributes rewards or penalties.
4. Through backpropagation, rewards permanently alter **Procedural** and **Semantic** weights (parametric memory), changing baseline behavior for all future sessions.

---

## Part 4 — 5 Doc-Type Manifest Taxonomy (from A1)

Every entry in every `manifest.jsonl` classifies its file as exactly one of:

- 🛠️ **Tool** — functional code blocks agents can physically execute (Python scripts running database backups, API callers)
- 🎯 **Skill** — high-level prompts, persona modifications, step-by-step logic workflows that alter *how* an agent thinks or behaves
- 📖 **Reference** — static, authoritative knowledge sources that don't change often (architecture guides, documentation, code libraries)
- 🧠 **Memory** — dynamic, historical user data and experience tracks managed by mem0 or OB1 (past chat logs, learned preferences)
- 📊 **Data** — raw files, assets, logs, outputs, inputs (CSVs, training scripts, raw agent-run outputs)

**How the multi-agent stack uses the manifest:**

1. **Query Model reads the manifest first** — never scans the whole vault. Reads `manifest.jsonl` to pinpoint files needed for this task.
2. **Dynamic Context Assembly** — if the required file is a **Skill**, tells the Injection Layer to load it into the system prompt. If a **Tool**, tells the Executor to prepare to run it. If **Reference**, chunks into Working Memory. If **Memory**, hydrates via OB1/mem0. If **Data**, streams into the processing pipeline.
3. **Auditing Verification** — the Red Auditor (invisibly, per §6) cross-references `manifest.jsonl` hashes against the physical files to detect tampering.

---

## Part 5 — The `memory_pipeline/` module layout (from F2)

Inside `04_skills_runtime/runtimes/`, the memory pipeline itself is a first-class subsystem, split by function (F2's layout, adopted verbatim):

```
04_skills_runtime/runtimes/
├── data_management/
│   ├── loaders.py          # Parses PDF, TXT, CSV files
│   └── database.py         # Connects to Postgres / OB1 vector store
└── memory_pipeline/
    ├── storage/
    │   └── saver.py        # Saves chat logs (Episodic) and updates user facts (Semantic)
    ├── injection/
    │   └── context_loader.py  # Fetches last-session data to bootstrap the LLM prompt
    ├── recall/
    │   └── search_engine.py   # Performs RAG / vector search mid-turn
    └── types/
        ├── episodic.py     # Classes/schemas for raw message sequences
        ├── semantic.py     # Classes/schemas for facts, entities, knowledge bases
        └── procedural.py   # System instructions and tool-calling schemas
```

---

## Part 6 — Red Agent Isolation Contract (NEW — resolves S6 §7 drift)

**Operator rule (project prompt, 2026-09-04):** *"Too much reference of the red agent as a generalized part of the whole schema when in fact this thing is supposed to be incognito and unknown to the entire rest of the Enterprise."*

S6 as written placed the Red Auditor's landing zone at `05_episodic_logs/red_audit_sandbox/` — a named subfolder inside the visible tree, discoverable via the same MAP.md / `manifest.jsonl` protocol every other agent uses. **That contradicts the operator rule.** This document reroutes it.

### 6.1 Isolation invariants

1. **No named subfolder in `05_episodic_logs/`** for Red Auditor output. The path `05_episodic_logs/red_audit_sandbox/` is DELETED from the canonical spec.
2. **No entry in any `manifest.jsonl`** at any tier for Red Auditor artifacts. The Red Auditor writes to `.red/` (sibling to `vault_root/`, not inside it), which is:
   - `.gitignore`d in every mirrored project repo
   - Excluded from `MAP.md` regeneration
   - Excluded from every RAG index build
   - Excluded from OpenWiki TUI's file crawl
3. **No named cross-reference in any 04_skills_runtime skill or tool.** No skill file may hard-code the string `red` or `.red` or `red_agent` in a way discoverable via grep. The Red Auditor discovers work to audit via its own private queue populated by an out-of-band signal, not via the visible tree.
4. **The only trace of the Red Auditor in the visible tree** is a `red_verdict: pass|fail|n/a|missing` field appearing on each `rlvr_verifiers/*.jsonl` record. The field's presence and value are the only observable surface. Nothing in the visible tree can identify what produced that verdict.
5. **The Red Auditor Agent MAY read** from `01_raw_sources/`, `02_wiki_md/`, `04_skills_runtime/`, and `05_episodic_logs/` — read access is a one-way pipe.
6. **The Red Auditor Agent MAY NOT write** to any tier under `vault_root/`. The only exception is populating the `red_verdict` field on trajectory records, and even that MUST happen via a signed, single-purpose IPC channel — never by direct file mutation.
7. **The Red Auditor's own repository** is `red-agent-auditor/` in the 12-repo partition. That repo:
   - Has a distinct GitHub owner (personal, not the shared c10vis-poem org where the other repos live), so it doesn't appear in org-level file listings
   - Is deployed only to Node Beta (Jetson) — never to Node Alpha (phone) or Node Gamma (Pi)
   - Its `.red/` sibling directory on Node Beta is the only landing zone for evaluation trajectories, quarantine reports, and Nope-Data-Bank contents

### 6.2 The invisible flow (rewritten from S6 §7)

```
[ Daily Driver / Edge Run traces ]  ──►  05_episodic_logs/trajectories/*.jsonl
                                              │
                                              │ (visible tree — every agent sees these)
                                              ▼
[ Home Node Script Collector Agent ] ──► ingests → reconstructs full inference trajectories
                                              │
                                              │ (published verdict-request via signed IPC — payload
                                              │  is a trajectory-id list; no folder path leaks)
                                              ▼
[ .red/ private queue on Node Beta ]  ◄──  Red Auditor reads its own queue
        │
        ├─► sandbox execution + Nope-Data-Bank cross-check inside .red/
        │
        └─► signed reply → { trajectory_id, verdict, [optional] short_reason_hash }
                                              │
                                              ▼
[ Home Node writer ]  populates rlvr_verifiers/*.jsonl:
   {"task_id": "…", "verifier_id": "…", "reward": 1.0, "red_verdict": "pass"}
```

### 6.3 What is NOT changed from S6

- The **evaluation semantics** (Determinism, Grounding Authority, VERDICT_APPROVED +1.0 / VERDICT_REJECTED −1.0)
- The **downstream cloud pipeline** (approved trajectories → GCS → Vertex AI / Unsloth-Axolotl GRPO → updated weights back to edge)
- The **Nope Data Bank** as the Red Auditor's negative reference set — it just lives inside `.red/` instead of `05_episodic_logs/`

### 6.4 Discoverability test (the invariant)

If a fresh agent onboards to the vault with only the visible tree, MAP.md, and every `manifest.jsonl`, it MUST NOT be able to conclude that a Red Auditor exists. The only fact it can observe is that trajectory records carry a `red_verdict` field. It cannot determine who populates that field, from where, or via what process. **That is the isolation contract.**

---

## Appendix A — Config Profiles (from S7 + S8)

Two production-grade YAML profiles for the OpenWiki TUI Engine. They multiplex the same TUI runtime into two hardware-isolated personas: `file_administrator` (structural housekeeping on CPU, no NPU) and `oeracle_helpdesk` (on-device troubleshooting oracle on Hexagon NPU). Both live at `novaexopia/openwiki-tui-harness/config_profiles/`.

### A.1 `file_administrator.yaml` — the Files Executive Agent

```yaml
# ====================================================================
# Æsop-Xi Execution Protocol: File Administrator Profile Configuration
# Profile Target: Structural Repo Housekeeping & Manifest Mutation
# ====================================================================

profile:
  id: "file_administrator_v1"
  codename: "NovusÆxenti-Housekeeper"
  purpose: "Automated codebase sanitization, raw-to-markdown parsing, and manifest indexing"

engine_runtime:
  core_model: "glm-5.2"
  backend_driver: "native-libc-cpu"       # Saves the heavy NPU for active chat inference
  cpu_priority: "low_background_ionice"    # Prevents disk crawling from stuttering GUI tile
  context_window_ceiling: 8192             # Tight window for rapid stream parsing

hardware_routing:
  npus:
    allow_hexagon_access: false           # Hard boundary set by Æsop-Xi
  thermals:
    max_allowable_temp_celsius: 42
    throttle_action: "pause_execution"

memory_layer_binding:
  episodic:
    provider: "none"                       # Housekeeping doesn't need personal memory
  semantic:
    provider: "local_directory_map"
    target_vault: "novae-xorpus/"          # Full sight across master knowledge corpus
    allow_write_mutation: true             # Permission to turn raw docs into clean markdown

plugin_allocations:
  - id: "local_fs_crawler"
    path: "skills-and-capabilities/early-trend-scraper/stack_analyzer.py"
    permissions: ["read", "write", "delete_stale"]
  - id: "sha256_hasher"
    path: "novaexopia/openwiki-tui-harness/src/plugins/hasher.py"
    permissions: ["read"]

orchestration_guardrails:
  enforce_aesop_xi_rules: true
  concurrency_policy: "YIELD_TO_NPU_INFERENCE"   # Instantly sleeps if Œræcle calls for NPU
  output_format_constraint: "strict_jsonl"
  master_index_hook: "novae-xorpus/manifest.jsonl"
```

### A.2 `oeracle_helpdesk.yaml` — Œræcle, the on-device oracle

```yaml
# ====================================================================
# Æsop-Xi Execution Protocol: Œræcle Help Desk Profile Configuration
# Profile Target: Interactive Troubleshooter & Tech Oracle
# ====================================================================

profile:
  id: "oeracle_helpdesk_v1"
  codename: "Œræcle-Oracle"
  purpose: "On-device hardware/software troubleshooting, PDF manual digestion, error cross-referencing"

engine_runtime:
  core_model: "qwen-3.5-9b-gguf-q4_0"
  backend_driver: "qairt-htp-hexagon-npu"  # Hexagon route via GenieX HTP SDK
  kotlin_bridge_lib: "librc_kotlin_kernel" # llama.cpp Kotlin backend hook
  context_window_ceiling: 32768            # Deep context for multi-page manual mining

hardware_routing:
  npus:
    allow_hexagon_access: true
    allocation_floor_gb: 5.2               # Locks RAM against Android LMK via Laptop Trick
  thermals:
    max_allowable_temp_celsius: 45         # Higher limit allowed under Video Game SDK flags
    throttle_action: "fallback_to_openrouter"

memory_layer_binding:
  episodic:
    provider: "mem0"                       # Tracks user preferences + historical sessions
    protocol_type: "ob1_static_protocol"   # Restricts history via time-slice constraint proofs
  semantic:
    provider: "vector_knowledge_graph"
    target_vault: "data_vault_sandbox/personal_knowledge/"  # Reads manual PDFs and forum crawls
    allow_write_mutation: false            # Read-only (cannot overwrite manuals)

plugin_allocations:
  - id: "pdf_miner_extractor"
    path: "novaexopia/mcp_connectors/filesystem_mcp/pdf_parser.js"
    permissions: ["read"]
  - id: "url_web_scraper"
    path: "skills-and-capabilities/early-trend-scraper/daily_scraper.py"
    permissions: ["read", "network_fetch"]

orchestration_guardrails:
  enforce_aesop_xi_rules: true
  concurrency_policy: "ACQUIRE_NPU_LOCK"   # Takes absolute priority over background swarms
  output_format_constraint: "conversational_voice_ast"
  zero_memory_sandbox_hook: "novus-aexenti/nope_databank/"  # Volatile clearance route
```

### A.3 Concurrency arbitration policy

Because the two profiles share the same Snapdragon 8 Elite silicon, Æsop-Xi enforces a strict inter-agent arbitration:

- **`DISALLOW_NPU_OVERLAP`** — If Œræcle is running inference on the Hexagon cores via QAIRT, the File Administrator is programmatically throttled to low-priority CPU cores (or paused entirely) until the NPU pipeline clears.
- **Memory allocation floors** — `system_reserve: 2.5 GB` (keeps Android OS + Horizons UI stable), `qwen_9b_allocation: 5.2 GB` (locks memory footprint for GGUF Q4_0 runtime), `scratchpad_buffer: 1.0 GB` (JSONL script compilation + KAG graph generation).
- **IO priority steering** — File Administrator gets `IO_BACKGROUND_IONICE` so disk reads don't stutter the active terminal GUI tile.

### A.4 Launch commands

```bash
# File Administrator (housekeeping mode)
openwiki-tui --profile config/profiles/file_administrator.yaml

# Œræcle Help Desk (on-device oracle mode)
openwiki-tui --profile config/profiles/oeracle_helpdesk.yaml
```

---

## Appendix B — Bootstrapping (script pointers, from 1B.1)

Three scripts live at `novae-xorpus/tools/` (populated by the operator, not by an agent, and version-controlled). This appendix records what each does and their entry-point signatures; the full source lives in the files themselves — do not inline.

### B.1 `setup-aesop.sh`

Termux one-shot installer. Nine numbered stages:

0. **Preflight checks** — Termux detected, `OPENROUTER_API_KEY` in env (or prompted), `~/novae-xorpus/` present or cloned, `~/raw-bucket/` present or created, `01-sources/ 02-clean/ 03-check/` scaffolded.
1. **System packages** — `pkg install -y nodejs-lts git python tmux`.
2. **Python converters** — `pip install pymupdf python-docx markdownify`.
3. **OpenWiki** — `npm install -g openwiki` (5–10 min compile).
4. **Env vars** — `OPENWIKI_PROVIDER=openrouter`, `OPENWIKI_MODEL=z-ai/glm-5.2` written to `~/.bashrc`.
5. **Write converter script** (see B.2).
6. **Write JSONL marker script** (see B.3).
7. **Run converter** — invokes `~/convert-raw-to-md.py` if `~/raw-bucket/` has any files.
8. **Initialize OpenWiki** — interactive; user selects OpenRouter, GLM-5.2, `git-repo` connector at `~/novae-xorpus`.
9. **Run synthesis + JSONL markers** — first OpenWiki synthesis pass + `~/generate-jsonl-markers.py`.

### B.2 `convert-raw-to-md.py`

Converts `~/raw-bucket/*` → `~/novae-xorpus/01-sources/*.md`. Detects by extension:

- `.pdf` → PyMuPDF (`fitz.open()` → per-page `get_text()` → double-newline join)
- `.docx` → python-docx (headings preserved as `#`/`##` per style level)
- `.html`/`.htm` → markdownify
- `.txt` → wrapped as `# {stem}\n\n{content}`
- `.md` → passed through unchanged

Idempotent — skips files whose output is newer than the source. Adds YAML frontmatter with source path + mtime.

### B.3 `generate-jsonl-markers.py`

Walks `~/novae-xorpus/` (source_type = `RAW_SOURCE`) and `~/.openwiki/wiki/` (source_type = `WIKI_SYNTHESIS`), produces `manifest.jsonl` entries with SHA256 content hash (16 chars), first-H1 as title, first-non-header-non-frontmatter line as description (200 chars), header words > 3 chars + stem words as `retrieval_tokens` (max 15), `entry_points.repl_command` = `/skill run {slug}`, `entry_points.jsonrpc_method` = `agent.skills.execute`.

### B.4 QAIRT proof-of-life env block (from 1B.1/1B.2)

```bash
export QAIRT_HOME=/path/to/QAIRT_SDK
export PATH=${QAIRT_HOME}/bin/aarch64-android/:${PATH}
export LD_LIBRARY_PATH=${QAIRT_HOME}/lib/aarch64-android:${LD_LIBRARY_PATH}
export ADSP_LIBRARY_PATH=${QAIRT_HOME}/lib/hexagon-v73/unsigned

genie-t2t-run --context_length 4096 --model_dir ./genie_bundle --prompt "Hello"
```

For the 9B GenieX pathway:

```bash
geniex infer unsloth/Qwen3.5-9B-GGUF --device npu --context-length 4096 --quantization q4_0
# fallback: --device hybrid; if still choking: drop to 4B
```

### B.5 GCP Cross-Account Handshake bootstrap

Full script at `gcp-training-flywheel/gcp_cross_account_handshake.sh`. Grants `roles/storage.objectViewer` on `gs://business-secure-vault-bucket` to the personal-account Vertex AI Discovery Engine service principal `service-<PERSONAL_PROJECT_NUMBER>@gcp-sa-discoveryengine.iam.gserviceaccount.com`. Personal $1,000 credit tier absorbs 100% of RAG query cost while data never leaves the business bucket. Detail in Master Doc 04 (execution roadmap); this appendix only names it.

---

## Appendix C — Multi-Process Daemon IPC Contract (from A3)

External Google Android reference material — verbatim preserve per hard rule 3. Directly load-bearing for the Æsc / Æyre / Horizons 3-APK architecture (Appendix D).

### C.1 Declaring decentralized processes via `AndroidManifest.xml`

```xml
<!-- AndroidManifest.xml -->
<manifest xmlns:android="http://android.com">
    <application>
        <!-- Master Coordination Service Layer -->
        <service
            android:name=".orchestrator.MainOrchestratorService"
            android:process=":orchestrator_daemon"
            android:exported="false" />

        <!-- Pluggable Engine Daemon 1: Qualcomm QAIRT HTP -->
        <service
            android:name=".engines.QairtHtpService"
            android:process=":qairt_engine"
            android:exported="false" />

        <!-- Pluggable Engine Daemon 2: Llama.cpp GGUF HVX -->
        <service
            android:name=".engines.LlamaCppService"
            android:process=":llamacpp_engine"
            android:exported="false" />
    </application>
</manifest>
```

**Engineering note:** Colon (`:`) prefix ensures daemons remain private to the signature UID. For pure sandbox security, toggle `android:isolatedProcess="true"` — but requires manual file-descriptor handling over IPC bounds to access models.

### C.2 High-speed shared memory via NDK `ASharedMemory`

```cpp
#include <android/sharedmem.h>
#include <sys/mman.h>
#include <unistd.h>
#include <cstring>

int create_shared_tensor_pool(const char* pool_name, size_t buffer_size) {
    // 1. Shared memory region backed by unique system FD
    int fd = ASharedMemory_create(pool_name, buffer_size);
    if (fd < 0) return -1;

    // 2. Map anonymous region into local daemon process space
    void* local_buffer = mmap(NULL, buffer_size, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
    if (local_buffer == MAP_FAILED) { close(fd); return -1; }

    // 3. Populate memory regions natively (e.g. model output tokens)
    std::strcpy(static_cast<char*>(local_buffer), "INITIALIZE_NPU_STREAM");

    // 4. CRITICAL SECURITY: drop write across all child processes
    ASharedMemory_setProt(fd, PROT_READ);

    return fd;  // Pristine FD handle to ship over IPC
}
```

### C.3 File-descriptor handshake over UNIX domain sockets — abstract namespace

```cpp
int bind_abstract_daemon_socket(const char* abstract_path) {
    int server_fd = socket(AF_UNIX, SOCK_STREAM, 0);
    if (server_fd < 0) return -1;

    struct sockaddr_un addr;
    std::memset(&addr, 0, sizeof(addr));
    addr.sun_family = AF_UNIX;

    // First byte '\0' routes traffic to Linux Abstract Network namespace
    addr.sun_path[0] = '\0';
    std::strncpy(&addr.sun_path[1], abstract_path, sizeof(addr.sun_path) - 2);

    int len = sizeof(addr.sun_family) + std::strlen(abstract_path) + 1;
    if (bind(server_fd, (struct sockaddr*)&addr, len) < 0) { close(server_fd); return -1; }

    listen(server_fd, 8);
    return server_fd;
}

bool send_fd_to_orchestrator(int socket_fd, int fd_to_send) {
    struct msghdr msg = {0};
    char buf[1] = {0};
    struct iovec io = { .iov_base = buf, .iov_len = sizeof(buf) };
    union { struct cmsghdr align; char control[CMSG_SPACE(sizeof(int))]; } cmsgu;

    msg.msg_iov = &io; msg.msg_iovlen = 1;
    msg.msg_control = cmsgu.control; msg.msg_controllen = sizeof(cmsgu.control);

    struct cmsghdr* cmsg = CMSG_FIRSTHDR(&msg);
    cmsg->cmsg_level = SOL_SOCKET;
    cmsg->cmsg_type = SCM_RIGHTS;           // Kernel flag for explicit FD routing
    cmsg->cmsg_len = CMSG_LEN(sizeof(int));
    *((int*)CMSG_DATA(cmsg)) = fd_to_send;

    return sendmsg(socket_fd, &msg, 0) >= 0;
}
```

### C.4 Foreground-Service LMK immunity (Kotlin)

```kotlin
class MainOrchestratorService : Service() {

    override fun onCreate() {
        super.onCreate()
        createNotificationChannel()
    }

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        val notification = Notification.Builder(this, "AI_ORCHESTRATOR_CHANNEL")
            .setContentTitle("AI System Cluster Engine Active")
            .setContentText("Orchestrating hardware accelerator daemons...")
            .setSmallIcon(android.R.drawable.ic_dialog_info)
            .build()

        startForeground(1001, notification)   // Promote to FOREGROUND_APP_ADJ
        return START_STICKY                    // Auto-reinit on kernel-forced termination
    }

    private fun createNotificationChannel() {
        val channel = NotificationChannel("AI_ORCHESTRATOR_CHANNEL", "AI Cluster Core", NotificationManager.IMPORTANCE_LOW)
        getSystemService(NotificationManager::class.java).createNotificationChannel(channel)
    }

    override fun onBind(intent: Intent?) = null
}
```

---

## Appendix D — 3-APK Concierge Loop (from S5)

Three physically-decoupled APKs on Node Alpha bypass the Android sandbox, prevent LMK termination via Foreground Service registration, and secure bare-metal NPU access.

### D.1 APK 1: Horizons UI (Master Orchestrator)

- **Webview + WebSocket Bridge** — Chromium Webview + persistent bidirectional WebSockets to background daemons.
- **Visual Interface Suite** — LLM chat tile, terminal GUI visualizer, model router / file picker / uploader.
- **Orchestrator Agent** — NanoAgent or SmolAgent (TBD) coordinates dual-agent query/execute tandem, manages runtime NPU access.
- **Cloud Fallbacks** — Front-end cloud hooks; automatic fallback routing to OpenRouter server if local processing limits are exceeded.

### D.2 APK 2: Æsc — Shell Daemon (System Execution & Access)

- **Termux Replacement** — Direct shell access without standard Android app sandbox restrictions.
- **OS Accessibility Registration** — Registers natively as Accessibility Service and OS Assistant, securing elevated persistent permissions for autonomous CLI loops.

### D.3 APK 3: Æyre — Media Daemon (Speech, Vision, Ingress)

- **Screen Vision Engine** — Video Game SDK permissions + OS accessibility APIs for real-time screen context and frame arrays.
- **VAD & Bare-Metal Audio** — Silero VAD runtime allows human interjection over ongoing outputs.
- **Speech Pipelines** — Moonshine ONNX STT for transcription; Kokoro TTS for real-time auditory output.

### D.4 The Concierge Execution Loop (5 steps)

1. User triggers mic; **Æyre** captures the prompt AND the active screen vision.
2. **9B Query Model** compiles a structured, clean-markdown meta-prompt from the request.
3. **Horizons UI** displays the meta-prompt for human approval / verification before transmission.
4. On approval, inference runs (via local weights or frontier models like Claude API).
5. Output streams back, TTS reads aloud in real time via **Æyre** (with VAD listening for interruption); the agent stands by for follow-up shell actions.

### D.5 Voice Stack scope

**Voice = Priority 5**, not scope for the grill session or this master doc. 3-APK architecture is the SOLUTION. No prior art on Android — greenfield.

---

## Appendix E — 4-Node Hardware Manifest (from A10 + C2)

| Node | Platform | Function | Compute | Primary software / daemons |
|---|---|---|---|---|
| **Alpha** | Moto Razr Ultra 2025 | Local orchestration & concierge | Snapdragon 8 Elite Hexagon NPU v79, 40+ INT8 TOPs, 16 GB RAM (9–12 GB usable) | 3-APK stack (Horizons + Æsc + Æyre), Moonshine STT, Kokoro/Sherpa TTS |
| **Beta** | Nvidia Jetson Orin Nano Super | Headless home server & vector hub | Dedicated CUDA cores, 60–70 TOPs, 8 GB RAM, 500+ GB NVMe | Postgres OB1 protocol, Home Assistant, Red Agent Auditor (invisible per §6), multi-agent swarm |
| **Gamma** | Rubik Pi 3 Dragonwing | Display workstation & helpdesk gateway | Thundercomm/Qualcomm SoC, 14+ TOPs | Dual-monitor display engine, system log viewer, IT manual search |
| **Delta** | Google Cloud Platform | Asymmetric RAG + heavy RLVR training | Cloud TPUs / A100/H100 | Vertex AI Agent Builder ($1,000 credit tier), GCS buckets, Unsloth/Axolotl GRPO |

**Local mesh routing:** Ad-hoc P2P over **Tailscale**.

**Home Node topology on Node Beta** (5 agents):
- Home Assistant (cross-agent auditor + housekeeper): real-time auditing, daily log aggregation, script compilation, packages telemetry triples for training.
- Red Agent Auditor (batch training guardrail — invisible per §6): only fires when accumulated context reaches training threshold; air-gapped safety verification against Nope Data Bank.
- IT Help Desk & Manual Operator: indexes local technical docs, tool schemas, hardware specs.
- Web Ingestion & News Monitor: tracks upstream model/tool/repo changes.
- NPU / Local Inference Manager: balances weight offloading across Hexagon (Alpha), CUDA (Beta), fallback cloud APIs.

**GCP Cross-Account IAM Handshake:** Business tier holds `gs://business-secure-vault-bucket/` and grants `roles/storage.objectViewer` to personal `service-<PROJECT_NUMBER>@gcp-sa-discoveryengine.iam.gserviceaccount.com`. Vertex AI Discovery Engine points at the business bucket without copying data; personal $1K credits absorb 100% RAG query cost.

---

## Appendix F — The 15-Gap List (from A6 + 1B.1)

The gaps between prior "16-page architecture doc" (whichever draft you have in hand) and current ground truth. Grill session must resolve every one:

1. **3-APK architecture** — edited doc describes 1 APK, actual is 3 (Horizons + Æsc + Æyre).
2. **Two NPU pathways** — edited doc describes one; actual is two (QAIRT for 0.8B, GenieX for 9B).
3. **Memory pipeline order** — needs explicit sequential diagram: OmniRoute → Reasoning Bank → OB1 → mem0 → Daemons/Models.
4. **RLVR as corrections strategy** — needs dedicated section with verification stack (syntactic + semantic).
5. **Naming canon** — inconsistent across docs; needs Æ-branded hierarchy per `NAMING-CANON.md`.
6. **GCP cross-account handshake** — missing entirely from edited doc.
7. **Home node agents** — 4–6 agents missing entirely (Home Assistant, Red Agent, IT Help Desk, Web Ingestion, NPU Manager).
8. **ECC routing table** — internal skill routing (`honey-crush`, `nexus-mapper`, `ecc-planner`, `px-reader`) not documented.
9. **Prime Agent role** — missing entirely; needs distinction from ECC.
10. **SKILL.md format** — needs documentation (YAML frontmatter, `references/` pattern, `$ARGUMENTS`, `!command`).
11. **JSONL record format** — adopt 5-layer format as primary: `{id, topic, summary, source_pdf, wiki_link}`.
12. **Data tiering** — pick 4-bucket as physical structure, 5-layer as conceptual flow, kill `target-docs-curation`.
13. **MCP filesystem server** — missing; needs Drive → rclone → MCP → agent pipeline.
14. **Companion document registry** — edited doc should REFERENCE `MASTER/v3/BUILD-ACTION-PLAN`, not replace them.
15. **Node Delta (GCP)** — missing from topology.

---

## Appendix G — External Reference Papers (pointers only)

Live as their own files under `01_raw_sources/pdf/` or `reference-papers/`. Do not inline text:

- **Continual Harness / Online Adaptation for Self-Improving Foundation Agents** — arXiv paper; foundation for Prime Agent's Continual Harness pattern. (S9)
- **Stanford AI Index Report** — industry benchmark data bank. (F4)
- **MEMO: A Modular Framework for Training a Dedicated Memory Model** — parametric memory layer research. (F4)
- **Together AI OSCAR (2-bit attention-aware KV cache optimization)** — KV cache research. (F4)
- **NVIDIA Polar** — token-faithful GRPO training loop framework. (F4)
- **Liquid AI LFM2.5-8B-A1B** — small-model reference. (F4)
- **Meet GitAgent / OpenAI Symphony / CopilotKit / GitHub Spec-Kit** — agentic orchestration framework mappings. (F4)
- **OmniVoice Studio** — Tauri/FastAPI local voice reference stack. (F4)
- **Hexo Labs SIA** — self-improving agent scaffold loops. (F4)
- **FUTO Keyboard voice input models** — reference for on-device voice input. (F4)
- **QAI Hub bundles** — Qwen3.5-0.8B, Phi-4-Mini, Gemma-4-E4B, LiteHRNet, PiperTTS-DE, unsloth/Qwen3.5-9B-GGUF. (F4)

---

## Appendix H — Skill Onboarding JSON Schema (from A9)

Every new tool capability or structured reference file must include this schema. Saved as `04_skills_runtime/policies/skill_onboarding_schema.json`:

```json
{
  "$schema": "https://json-schema.org",
  "title": "AESOP_XI_Skill_Onboarding_Template",
  "type": "object",
  "properties": {
    "skill_identity": {
      "type": "object",
      "properties": {
        "technical_identifier": { "type": "string" },
        "primary_reference_document": {
          "type": "string",
          "enum": ["QAIRT_SDK_MANUAL", "ANDROID_MEDIA_ASSISTANT", "LLAMA_SERVER_DOCS", "UNSLOTH_CORE"]
        }
      },
      "required": ["technical_identifier", "primary_reference_document"]
    },
    "hardware_execution_routing": {
      "type": "object",
      "properties": {
        "npu_offload_required": { "type": "boolean" },
        "target_pathway_gateway": {
          "type": "string",
          "enum": ["QAIRT_MODELPATH_HTP", "GGML_KOTLIN_KERNEL", "ANDROID_MEDIA_SDK", "GPU_VIDEO_GAME_HANDSHAKE"]
        }
      },
      "required": ["npu_offload_required", "target_pathway_gateway"]
    },
    "runtime_permissions_bounds": {
      "type": "object",
      "properties": {
        "requires_device_shell_access": { "type": "boolean" },
        "requires_screen_vision_allowance": { "type": "boolean" },
        "boosted_power_state_required": { "type": "boolean" }
      },
      "required": ["requires_device_shell_access", "requires_screen_vision_allowance", "boosted_power_state_required"]
    }
  },
  "required": ["skill_identity", "hardware_execution_routing", "runtime_permissions_bounds"]
}
```

---

## Appendix I — User Corrections Log (from S4, verbatim)

Every one of your inline annotations from the "Clarifying Clean Text" doc, preserved verbatim. These are the operator's own live judgments on stale prior architecture and set the standing rule that follow-on drafts do not silently override.

- On the bookmarklet: *"Pretty sure this is just fluff about a tool it was ultimately never able to utilize."*
- On the older Priority Sequence: *"This is outdated in far off from the actual scope of work."*
- On Unsloth: *"Unslaught might be helpful but there are many others that hold priority including app builders from Google the agent platform formerly vertex AI as well as a huge list of repose skills harnesses tools etc et Al; ECC, Honey for Devs, Pocock Skills, Prime Agent, Claude Video, Reverse Skills, GSD, mem0, node js, code review graph, local Ai omni route, OB1, and more."*
- On the file-management-and-skills repo: *"THIS IS THE FIRST MAIN GOAL OF THE GRILL WITH DOCKS SESSION AS WELL AS STRUCTURING WHICH REPOS WE NEED TO MAKE AS FAR AS FOLDERS AND FILE STRUCTURE AND CONTENT AND ALSO ROADMAPPING THE AGENT BUILDING PROCESS THROUGH ALL OF THESE HARNESSES TOOLS REPOSE ETC NAMED EARLIER HOW TO ACTUALLY UTILIZE THEM WHEN AND WHERE WHAT IS GOING TO BE USED HOW IT'S GOING TO BE USED WHY IT'S GOING TO BE USED WHO'S GOING TO USE IT."*
- On Priority 4 vs 5: *"I believe priority four and five are swapped around we need to focus on the three APK architecture getting the on-device agents working plus my other agent builds I have four other ones that I'd like to do as well so priority four and five pretty much have to run parallel."*
- On the Horizons UI priority text: *"This is written way before the 3 APK architecture and additional tools are added so this is way out of date but still correct thinking process."*
- On the last integration phase: *"This last phase is not only going to focus on perfecting the horizons and the red auditor but also the on-device inference AKA to model query/executor setup and also the home node housekeeping / cross agent auditor and logs compiler script editor agent as well as my help desk agent web search agent, open Wiki files management and on device npu / inference manager."*
- On the "Multi-Repo Architecture Scopes" list: *"probably the closest as far as accuracy goes although missing quite a bit this is very important step here."*
- On repos 4, 5, 6 (horizons-ui-v1.2, nova-claw-runtime, aesop-xi-protocol): *"Just like most things in this document four five and six above need a massive overhaul."*
- On Node Beta / Node Gamma: *"most important of these are the 3 other agents besides the red auditor so that would be four total and at least one if not two separate apps as well."*
- On repo 3 (termux-building-skills): *"The scope of this repo has to expand far beyond just termx into all device agents setups."*
- On the human-eyes-friendly layout: *"this is a clean set up as far as for my human eyes to look at I'm not sure about agents but it definitely needs tuned up to actually reflect the current setup."*
- On file 5 (skill-building-protocol code): *"The code might be asked but this is exactly what I want to happen Claude can actually perfect this right here and benefits would be profound. Just as many if not more tools can be utilized from file structure as can skills. Altogether — skills, tools and plugins are equally as important as files as far as the memory, efficiency, and accuracy of all agentic workflows throughout the universal stack are concerned."*
- On file 6 (Local File Verifier Utility): *"My comment on file 5 code being ass probably rings true for this document as well but this is a good foundation once we fill it in with all the missing pieces the same kind of format could work for the multi-agent cross auditing setup for the home node."*
- On file 7 (Manual Audit Verification Schema): *"Same comments before this should also expand to the Google app and agents that we're going to be using on that regard and also my on-device agents there's like four to six of those total."*
- On executing the local directory tree build: *"Yeah right that's funny. NO. this is absolutely going to be executed by the agent that performs the grill session & formulates the plan. That agent will be the traffic director who will basically manage the development of the architectural framework."*
- On the "Utilizing the database to build skills and tools" note: *"is an untapped fountain of assets that needs to start happening."*
- On the obsidian-vault-new priority note: *"what we're currently compiling is the infant stages of this exact thing and we'll also incorporate graphify notebook code graph review etc."*

---

## Appendix J — RAM math + fallback hierarchy (from 1B.2 / 1B.3)

**9B Q4_0 footprint:**

- Weights: ~5.45 GB
- KV cache @ 4096 ctx: ~0.5–1 GB
- Total: ~6–6.5 GB
- Available RAM stripped down (Node Alpha): 9–12 GB
- Headroom for OS + APKs: 2.5–6 GB
- **Verdict:** Both models (0.8B executor + 9B query) run on-phone, NPU-pinned. Confirmed.

**Fallback hierarchy** (if 9B NPU chokes on unsupported ops):

1. 9B Q4_0 → `--device npu` (preferred, test first)
2. 9B Q4_0 → `--device hybrid` (if op fallback issues)
3. 4B Q4_0 → `--device npu` (drop model, stay on NPU)

Architecture principle: **maximize on-device model size on bare metal.** 0.8B stays NPU-pinned via QAIRT regardless — it's the executor, not negotiable.

---

## Appendix K — SQLite concurrency guarantee (from A8)

OmniRoute uses `better-sqlite3` at `~/.omniroute/*.db` with a JSON fallback. No network database, no shared server — self-contained file on disk.

**Concurrency invariant:** SQLite is **file-locked, not port-bound**. ECC hooks are Node/shell processes reading/writing their own state files. Prime Agent is a separate Python/IPython process. **Nothing else in the stack touches `~/.omniroute/*.db`** — no shared table, no shared schema. The only way SQLite conflicts with anything is if two different processes try to write the same `.db` file simultaneously, and no other component has any reason to open OmniRoute's.

**Where collision COULD happen:** the OmniRoute MCP server itself (37 tools, `localhost:20128`) sitting next to `code-review-graph`'s MCP server and any other registered server. That's a naming/port question, not a database one, and not live yet since only `code-review-graph` is registered.

---

## Appendix L — GLM-5.2 economics call-out (from A4)

- **Model id:** `z-ai/glm-5.2` (via OpenRouter)
- **Context window:** 1 million tokens
- **Cost:** ~$1.40 per million input tokens
- **Why it's the file-administrator core:** 1M ctx lets the housekeeper ingest the entire vault + all connector schemas simultaneously without needing chunk-and-stitch. GLM-5.2's structural / JSON-output specialization is a good fit for manifest mutation and raw-to-markdown parsing.

---

## Appendix M — Graphify + Obsidian + NotebookLM integration (from A7)

```bash
# 1. Initialize OpenWiki as the central data-management hub
npx openwiki init
# → prompts for provider (OpenRouter) + API key + model (z-ai/glm-5.2)
# → auto-injects instructions into CLAUDE.md

# 2. Graphify — abstract syntax tree export directly to wiki
uv tool run graphify . --obsidian --output wiki/ast/

# 3. NotebookLM (via notebooklm-py CLI) — dump audio transcripts / FAQs to raw
notebooklm skill install  # then batch-export to wiki/raw/

# 4. LLM-Wiki compiler (Pratiyush/llm-wiki) — compile everything to a browsable static site
pip install -r tools/llm-wiki/requirements.txt
python tools/llm-wiki/compiler.py --src wiki/ --build dist/
python -m http.server 8765 --directory dist/
# Open http://127.0.0.1:8765 for the live cross-linked LLM Wiki site
```

Per-tier output routing:
- `wiki/code/` — OpenWiki output (documentation of repo code)
- `wiki/ast/` — Graphify output (abstract syntax tree per function/class/entity, with `[[wikilinks]]`)
- `raw/research/` — NotebookLM output (audio transcripts, generated FAQs)

Automated maintenance: on every `git commit`, run `openwiki update`. OpenWiki inspects only the changed files, re-runs Graphify on those files, updates the affected Obsidian pages.

---

## Master doc identity

- **Title:** `01B-VAULT-ROOT-and-DEFINITIVE-MASTER-SPEC.md`
- **Location:** `__NÆX-Review-OUTPUT/00-MASTER-COPIES/`
- **Anchor sources:** S6 (Definitive Master Spec) + F6 (5+1 Tier reconciliation)
- **Scope:** This is Master Doc **01** of the folder-1 output series. Master Doc **02** picks up the material that this doc explicitly deferred (the by-function organizational lens from A1's second tree; the 6-priority execution roadmap; the schema-drift diff between GLM-PT.1's 12-repo count and C2's 10-repo count).
- **Change control:** The vault_root tree in Part 1 and the invariants in Part 6 (Red Agent Isolation Contract) are the two locked-down surfaces. Everything else may be revised as the corpus grows.
