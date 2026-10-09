---
title: "MAP.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/03_ALTERNATIVES_PROPOSAL_V1/novus-aexenti/MAP.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

MAP.md — novus-aexenti
Cognitive Architecture & Navigation Map
novus-aexenti/

├── MAP.md                       # This directory map and cognitive pipeline topology

├── manifest.jsonl               # Machine-readable registry of files, SHA256 hashes, and types

├── AGENTS.md                    # Operational constraints, triage vs executor model roles

├── RESUME.md                    # Active model weights, execution state, and session
checkpoints

├── UNRESOLVED.md                # Open optimization tickets, benchmark gaps, and backlog
tasks

│

├── dual_agent_router/           # Dynamic query analysis, model routing & prompt bridging

│   ├── query_analyzer.py        # Evaluates token complexity and intent (0.8B vs 9B)

│   ├── executor_bridge.py       # Formats clean, compressed meta-prompts for execution
models

│   └── model_profile_registry.json # Model specs, context window sizes, quantization types

│

├── mem0_episodic/               # In-session episodic facts, habit retention & preferences

│   ├── vector_recall_engine.py  # Local semantic lookup script for conversational facts

│   └── rolling_habits.json      # Concrete syntax rules, naming invariants & user habits

│

└── reasoning_bank/              # Execution flywheel, crash recovery & test batteries



    ├── active_execution_paths.json # Persistent ledger of fractional task steps

    └── baseline_tests.json      # Standardized regression capability test battery
Subsystem Pipeline Flow
1.​ Ingress: Incoming user prompt arrives at
dual_agent_router/query_analyzer.py.
2.​ Triage: Short, deterministic requests route to local on-device 0.8B triage. Complex tasks
route to 9B executor.
3.​ Context Enrichment: mem0_episodic/vector_recall_engine.py injects relevant
episodic facts and user habits from rolling_habits.json.
4.​ Formatting: dual_agent_router/executor_bridge.py strips conversational fluff
and builds structured meta-prompts.
5.​ Execution & Checkpointing: Tasks are checkpointed in
reasoning_bank/active_execution_paths.json to enable zero-loss crash
recovery.
