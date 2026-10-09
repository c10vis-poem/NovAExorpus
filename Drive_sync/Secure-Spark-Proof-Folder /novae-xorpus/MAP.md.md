---
title: "MAP.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /novae-xorpus/MAP.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

MAP.md — The Master Navigation Map &
Component Ledger (novae-xorpus)
Repository: novae-xorpus (The Master Core & Living Wiki Vault)​
Parent Workspace: Secure-Spark-Proof-Folder
(12OJenWnx-wbBN-vHwkPcQ6ymTBp6k0gn)​
Authority References:

●​ 1 main dumbass map
●​ PROPOSAL-V2-CORRECTED-WIKI-TERMINOLOGY-AND-s-tier-ALTERNATIVE.md
●​ 02_DUMBASS_UNIVERSAL_MEMORY_SPEC.md


1. The Agent's First-Move Directive
1.​ Read root MAP.md (orient: structural overview, bounded size).
2.​ Read tier-local MAP.md if working within a specific subsystem.
3.​ Stream & query manifest.jsonl (locate targeted entities/hashes; never load full
JSONL).
4.​ Load only the targeted file paths.


2. Master Repository Layout
novae-xorpus/

├── MAP.md                               # Master visual navigation & component ledger

├── manifest.jsonl                       # Machine RAG index, SHA-256 hashes, tokens

├── README.md                            # Repository identity & operational runbook

├── AGENTS.md                            # Operational boundaries, agent contracts & hard rules

├── RESUME.md                            # Session checkpoints & verified state of progress

├── chunk.jsonl                          # Pre-tokenized machine retrieval passage layer



│

├── raw/                                 # Ingestion landing zone

├── clean_md/                            # Normalized, non-1:1 condensed markdown

├── wiki_md/                             # Living LLM wiki nodes

├── skills/                              # Procedural skills co-located locally

├── tools/                               # Executable tools (compile_manifest.py, check.py)

├── scripts/                             # Master scripts registry & cross-repo orchestrators

├── hooks/                               # Master hooks registry & lifecycle sync hooks

├── pending/                             # Staged backlogs & unverified items

├── audit/                               # Divergence logs, test traces, RLVR reports

├── archive/                             # Superseded historical snapshots

│

├── _dumbass_universal_memory/           # The Integrated 7-Component Memory Engine

│   ├── sqlite/                          # Local zero-latency tables (<5ms)

│   ├── postgres/                        # Authoritative relational & vector store (Node Beta)

│   ├── mem0/                            # Rolling user habits & episodic state (Mobile RAM)

│   ├── ob1_protocol/                    # Ground-truth static retrieval via MCP

│   ├── omniroute/                       # Port 20128 asynchronous memory extraction tap

│   ├── reasoning_bank/                  # Active execution ledger & crash recovery

│   └── continual_harness/               # Online adaptation loop & snapshot rollback

│

└── 5+1 Cognitive Tiers:



    ├── 01_raw_sources/                  # Tier 1: Sensory / cold archive (immutable)

    ├── 02_wiki_md/                      # Tier 2: The 18-Branch Living LLM Wiki

    │   └── vendors/                     # Canonical vendor workspaces:

    │       ├── google/                  # GCP, NDK, Gemma 4, Gemini API/Nano, Compose

    │       ├── qualcomm/                # QAIRT, Genie bundles, Hexagon HTP v79, FastRPC

    │       ├── nvidia/                  # Jetson Orin Nano, CUDA, TensorRT

    │       ├── github/                  # c10vis-poem repos, forks, actions

    │       ├── anthropic/               # Claude Code CLI, ECC harness, APIs

    │       ├── primeintellect/          # Compute clusters & decentralized training

    │       └── deepseek/                # Open weights & deep reasoning harnesses

    ├── 03_recall_cache/                 # Tier 3: High-speed retrieval (jsonl chunks, vectors)

    ├── 04_skills_runtime/               # Tier 4: Procedural repertoire & execution policies

    └── 05_episodic_logs/                # Tier 5: Execution traces, telemetry & RLVR scores
