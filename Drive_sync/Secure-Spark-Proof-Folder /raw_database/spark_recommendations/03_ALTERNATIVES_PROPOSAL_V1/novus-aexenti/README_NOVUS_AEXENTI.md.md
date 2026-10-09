---
title: "README_NOVUS_AEXENTI.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/03_ALTERNATIVES_PROPOSAL_V1/novus-aexenti/README_NOVUS_AEXENTI.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

README — novus-aexenti/
Cognitive Reasoning Engine & Asymmetric Dual-Brain MoE
W5+H Subsystem Identity
●​ WHO: Houses the 0.8B Triage / Intent Model and the 4B/9B Core Executor Model.
●​ WHAT: Dual-agent routing logic, in-session mem0 episodic state, and the Reasoning
Bank RLVR recovery ledger.
●​ WHEN: Fired on every incoming user prompt, voice transcription, or background task
dispatch.
●​ WHERE: novae-xorpus/novus-aexenti/ (Federated Subsystem Root).
●​ WHY: Solves the context bloat and RAM saturation problem by separating fast intent
parsing from heavy code generation, keeping mobile RAM usage under 5.0 GB.
●​ HOW: Dispatches small prompts to the 0.8B triage model, pulls habits from mem0,
compiles clean meta-prompts, and logs step progress to
active_execution_paths.json.


Internal Directory Topology
novus-aexenti/

├── README.md                                # This document (Cognitive architecture & dataflow)

├── manifest.jsonl                           # Local cryptographic catalog of router & memory modules

│

├── dual_agent_router/                       # Triage vs. Executor handshake engine

│   ├── query_analyzer.py                    # Evaluates user intent and checks token complexity

│   ├── executor_bridge.py                   # Formats clean, compressed meta-prompts for the 9B
model

│   └── model_profile_registry.json          # Context window limits and quantization configs

│



├── mem0_episodic/                           # In-session memory and dynamic preference caching

│   ├── vector_recall_engine.py              # Semantic lookup for active conversational facts

│   ├── rolling_habits.json                  # User syntax preferences and operational habits

│   └── ob1_static_protocols/                # Ground-truth static query bridges over MCP

│

└── reasoning_bank/                          # The Self-Healing System Flywheel

    ├── active_execution_paths.json          # Persistent JSON ledger tracking fractional task
steps

    ├── failure_logs/                        # Structured error reports for weekly pattern detection

    └── post_regression/                     # Rollback checkpoints to prevent capability decay

        ├── baseline_tests/                  # Standardized test suites for on-device swarms

        └── regression_audit_report.jsonl     # Historical accuracy metrics across model swaps


Beginner-Proof Implementation Rules
1.​ State Continuity: If a model process panics or the phone restarts, the recovery engine
reads active_execution_paths.json to resume the task at the exact step where
execution halted.
2.​ Zero Raw Chat Flooding: mem0 returns only condensed fact tokens—never dump raw
multi-turn chat logs into the 9B model's prompt.
