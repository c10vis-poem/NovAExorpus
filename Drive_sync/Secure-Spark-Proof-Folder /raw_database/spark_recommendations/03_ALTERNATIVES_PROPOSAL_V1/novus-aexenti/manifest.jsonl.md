---
title: "manifest.jsonl"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/03_ALTERNATIVES_PROPOSAL_V1/novus-aexenti/manifest.jsonl.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

{"path": "MAP.md", "type": "navigation", "description": "Internal directory layout and cognitive
pipeline map"}
{"path": "manifest.jsonl", "type": "manifest", "description": "Machine-readable catalog of all files
in this repo"}
{"path": "AGENTS.md", "type": "policy", "description": "Operational boundaries, role definitions
(triage vs executor), and context limits"}
{"path": "RESUME.md", "type": "state", "description": "Current model configuration, active
weights, and session checkpoints"}
{"path": "UNRESOLVED.md", "type": "backlog", "description": "Pending model optimizations,
benchmark discrepancies, and backlog tasks"}
{"path": "dual_agent_router/query_analyzer.py", "type": "tool", "description": "Directs incoming
prompt strings to 0.8B triage or 9B executor based on token complexity and intent"}
{"path": "dual_agent_router/executor_bridge.py", "type": "tool", "description": "Formats clean,
compressed meta-prompts for the execution models"}
{"path": "dual_agent_router/model_profile_registry.json", "type": "data", "description": "Registry
of context window limits, quantization types, and system prompt paths"}
{"path": "mem0_episodic/vector_recall_engine.py", "type": "tool", "description": "Semantic lookup
script for in-session conversational facts and habit keys"}
{"path": "mem0_episodic/rolling_habits.json", "type": "data", "description": "Concrete user syntax
preferences, style invariants, and active operational habits"}
{"path": "reasoning_bank/active_execution_paths.json", "type": "state", "description": "Persistent
ledger tracking fractional task steps for crash recovery"}
{"path": "reasoning_bank/baseline_tests.json", "type": "verification", "description": "Standardized
regression capability test battery across model swaps"}
