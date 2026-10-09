---
title: "README_DATA_VAULT.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/02_MY_ORIGINALS/README_DATA_VAULT.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

README — data_vault/
The Living Semantic Knowledge Base, High-Speed Cache &
Cognitive Tiers
W5+H Subsystem Identity
●​ WHO: Governed directly by the Files Executive Agent via the OpenWiki TUI.
●​ WHAT: Houses the 5+1 Cognitive Memory Tiers: immutable cold sources, conceptual
wiki markdown, machine recall caches, procedural tool libraries, and episodic telemetry.
●​ WHEN: Queried during every reasoning pass; updated dynamically upon new document
ingestion or task execution.
●​ WHERE: novae-xorpus/data_vault/ (Federated Subsystem Root).
●​ WHY: Enforces strict separation between human-readable markdown and
machine-readable vector/JSONL caches, preventing context pollution and database
degradation.
●​ HOW: Synchronizes nodes via bidirectional [[wikilinks]], computes SHA256
checksums, and maintains localized tier manifests.


Internal Directory Topology
data_vault/

├── README.md                                # This document (Cognitive memory tiers & access
rules)

├── manifest.jsonl                           # Master catalog of semantic notes and cache shards

│

├── 01_raw_sources/                          # TIER 1: Immutable Ground Truth (Cold Archive)

│   ├── manifest.jsonl                       # Local raw asset index

│   ├── pdf/                                 # Source whitepapers, specs, data sheets (*.pdf)

│   ├── media/                               # Audio memos, screen vision captures (*.wav, *.mp4)



│   └── text/                                # Raw unformatted scrapes & exports (*.txt, *.html)

│

├── 02_wiki_md/                              # TIER 2: Semantic Memory (The LLM Wiki)

│   ├── manifest.jsonl                       # Local conceptual node index

│   ├── concepts/                            # Atomic linked notes (Zettelkasten domain models)

│   ├── architectures/                       # Technical specs & cross-repo blueprints

│   ├── entities/                            # Device registers, schema contracts, hardware profiles

│   └── indexes/                             # Maps of Content (MOCs) & taxonomy hubs

│

├── 03_recall_cache/                         # TIER 3: Working Memory Accelerator (High-Speed
Cache)

│   ├── manifest.jsonl                       # Local cache shard index

│   ├── jsonl/                               # Pre-tokenized chunks for low-latency prompt injection

│   ├── vectors/                             # Dense embedding indices (FAISS / HNSW checkpoints)

│   └── kv_store/                            # Embedded SQLite key-value fast lookup tables

│

├── 04_skills_runtime/                       # TIER 4: Procedural Memory (Skills & Executables)

│   ├── manifest.jsonl                       # Local procedural catalog

│   ├── prompt_skills/                       # Modular SKILL.md prompt definitions (*.md, *.yaml)

│   ├── extracted_tools/                     # Mined deterministic code blocks (cli/*.sh, wrappers/*.py)

│   ├── runtimes/                            # Operational daemon scripts & socket listeners

│   └── policies/                            # Self-correction heuristics & validation schemas



│

└── 05_episodic_logs/                        # TIER 5: Episodic Memory (Telemetry & Telemetry Logs)

    ├── manifest.jsonl                       # Local session & audit registry

    ├── daily_driver_sync/                   # Ingested logs from mobile edge sessions

    ├── trajectories/                        # Tri-model run traces (Query, Executor, Frontier)

    ├── rlvr_verifiers/                      # Graded rewards (+1.0 / -1.0) & assertion outcomes

    └── hygiene_reports/                     # Schema integrity audits & failure logs


Beginner-Proof Implementation Rules
1.​ Sensory Immutability: Files placed in 01_raw_sources/ are write-once. Never
overwrite or reformat originals.
2.​ Clean Separation: Never place raw tabular JSONL or binary embeddings into
02_wiki_md/. Machine caches belong strictly in 03_recall_cache/.
