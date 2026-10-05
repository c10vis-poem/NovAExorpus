---
tags: []
created: '2026-09-10'
title: '2026-09-10_Dir-sys-specification'
---



----
SYSTEM SPECIFICATION: COGNITIVE REPOSITORY ARCHITECTURE
Document Target: Autonomous Planning, Auditing, and Execution Agents Role: Injected Structural, Operational & Synchronization Protocol Repository Model: 5+1 Tier Cognitive Memory, OpenWiki TUI File Management, Multi-Model Cross-Auditing, Sandboxed Red Gatekeeping, and Distributed RAG Manifests Version: 3.0 (Definitive Master Specification)
1. Core Architectural Invariants
As the planning agent, you must enforce the separation of cognitive memory layers across the filesystem. Adhere strictly to the following invariants:
1. Sensory Immutability (Tier 1): Never modify, overwrite, or delete assets in 01_raw_sources/. All raw inputs are read-only sources of truth.
2. Human-Machine Decoupling (Tier 2 vs. Tier 3): Human-readable semantic knowledge lives in 02_wiki_md/ (.md). Machine-readable retrieval chunks live in 03_recall_cache/ (.jsonl, vectors). Never dump raw tabular JSONL or vector embeddings into the wiki layer.
3. Procedural vs. Episodic Separation (Tier 4 vs. Tier 5): Executable skills, scripts, and policies belong in 04_skills_runtime/. Trajectory traces, error logs, and verifier evaluations belong in 05_episodic_logs/. Never place runtime logic inside logging directories or vice versa.
4. Metacognitive Priming: Before initiating multi-step tasks, read MAP.md or parse the root manifest.jsonl to resolve entity references rather than performing blind recursive scans across the filesystem.
5. LLM Wiki Protocol (wiki_md/): The semantic vault operates as an organization-wide wiki standard governed directly by the Files Executive Agent via the OpenWiki TUI.
6. Dual Extraction Mandate: Every document ingested into the ecosystem must be systematically screened for both Procedural Skills (prompt templates, behavioral heuristics) and Executable Tools (scripts, wrappers, deterministic CLI invocations).
7. Red Auditor Gatekeeping: No episodic execution trace or generated script may enter the recursive training stream without passing an isolated sandbox evaluation by the Red Auditor Agent.
8. Universal Source of Truth: All local auditor nodes and the sandboxed Red Auditor must evaluate claims and script outcomes against the shared master memory bank and database.
9. Distributed Manifest Coverage: Every repository root and major structural subsystem must maintain its own local manifest.jsonl to power low-overhead hierarchical RAG retrieval.
2. Directory Schema & Access Control Matrix
📦 vault_root/
├── 📜 MAP.md                                # Master human-readable index & ontology graph (Read-Heavy / Agent Update)
├── 📊 manifest.jsonl                        # Root-level RAG registry & global hash table (Append / Sync)
│
├── 📁 01_raw_sources/                       # TIER 1: COLD SENSORY ARCHIVE (Access: READ-ONLY)
│   ├── 📊 manifest.jsonl                    # Local RAG catalog of all immutable raw sources
│   ├── 📑 pdf/                              # Source whitepapers, specs, data sheets (*.pdf)
│   ├── 🎬 media/                            # Video captures, audio memos, transcripts (*.mp4, *.wav, *.png)
│   └── 📝 text/                             # Raw text scrapes, dumps, API payload exports (*.txt, *.html)
│
├── 📁 02_wiki_md/                           # TIER 2: THE LLM WIKI LAYER (Access: READ / WRITE - OpenWiki TUI)
│   ├── 📊 manifest.jsonl                    # Local RAG catalog of conceptual nodes & graph links
│   ├── 💡 concepts/                         # Atomic linked notes, theory, and domain models (*.md)
│   ├── 🏛️ architectures/                    # System blueprints, data flows, interface specs (*.md)
│   ├── 🏷️ entities/                         # Registries, schema contracts, hardware profiles (*.md)
│   └── 🧭 indexes/                          # Maps of Content (MOCs) and taxonomy clusters (*.md)
│
├── 📁 03_recall_cache/                      # TIER 3: WORKING MEMORY ACCELERATOR (Access: REBUILD / OVERWRITE)
│   ├── 📊 manifest.jsonl                    # Local RAG catalog of vector & chunk shards
│   ├── ⚡ jsonl/                            # Pre-tokenized passages for high-speed prompt injection (*.jsonl)
│   ├── 📐 vectors/                          # Dense vector indices (*.bin, *.faiss, *.hnsw checkpoints)
│   └── 🗝️ kv_store/                         # Low-latency key-value entity lookups (*.db, *.json)
│
├── 📁 04_skills_runtime/                    # TIER 4: PROCEDURAL REPERTOIRE & TOOLS (Access: VERSION-CONTROLLED)
│   ├── 📊 manifest.jsonl                    # Local RAG catalog of all extracted skills & tools
│   ├── 🎯 prompt_skills/                    # Modular SKILL.md prompt definitions (*.md, *.yaml)
│   ├── 🛠️ extracted_tools/                  # Deterministic tools mined from ingested documentation
│   │   ├── cli/                             # Extracted command-line utilities (*.sh)
│   │   └── wrappers/                        # Extracted API interfaces & micro-functions (*.py)
│   ├── ⚙️ runtimes/                          # Master operational scripts and execution hooks (*.py, *.sh)
│   └── 🛡️ policies/                         # Validation guards, retry policies, schemas (*.json, *.yaml)
│
└── 📁 05_episodic_logs/                     # TIER 5: TELEMETRY & EPISODIC RUNS (Access: APPEND-ONLY)
    ├── 📊 manifest.jsonl                    # Local RAG catalog of sessions, audits, and verifiers
    ├── 📲 daily_driver_sync/                # Ingested logs from edge device sessions (*.jsonl)
    ├── ⏱️ trajectories/                     # Multi-model traces: Query, Executor, Frontier (*.jsonl)
    ├── 🛑 red_audit_sandbox/                # Red Auditor evaluation reports & pass/fail quarantine (*.jsonl)
    ├── ⚖️ rlvr_verifiers/                   # Graded rewards, assertion outcomes (+1.0 / -1.0) (*.jsonl)
    └── 🧹 hygiene_reports/                  # Schema integrity audits, broken link checks (*.md)