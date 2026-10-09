---
title: "RESUME.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/03_ALTERNATIVES_PROPOSAL_V1/novus-aexenti/RESUME.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

RESUME.md — novus-aexenti
Current Execution State & Checkpoint
Last Updated: 2026-09-07T02:00:00Z​
Status: Canonical Subsystem Populated​
Active Phase: Phase 1 (Repository Structural Hardening)


Active Model Configurations & Weights
1.​ Triage Tier:

●​ Model: Qwen3.5-0.8B-Instruct
●​ Weights File: Qwen3.5-0.8B-Instruct-Q4_0.gguf (local path:
models/qwen_0.8b/)
●​ Engine: GenieX on Snapdragon Hexagon v79 NPU (Node Alpha)
●​ Status: Verified operational.

2.​ Executor Tier:

●​ Model: Qwen3.5-9B-Instruct
●​ Weights File: Qwen3.5-9B-Instruct-Q4_0.gguf (local path:
models/qwen_9b/)
●​ Engine: llama.cpp / CUDA on Jetson Orin Nano Super (Node Beta)
●​ Status: Active primary executor.

3.​ Specialist Analytical Tier:

●​ Model: Gemma-4-12B-IT-QAT
●​ Weights File: Gemma-4-12B-IT-QAT-Q4_0.gguf
●​ Engine: llama.cpp with -fa -ctk q8_0 -ctv q8_0 memory flags
●​ Status: Staged for deep cross-document audit sweeps.


Session Checkpoints
​Created dual_agent_router/ with query_analyzer.py, executor_bridge.py,
and model_profile_registry.json.


​Created mem0_episodic/ with vector_recall_engine.py and
rolling_habits.json.
​Created reasoning_bank/ with active_execution_paths.json and
baseline_tests.json.
​Created root repository control files (MAP.md, manifest.jsonl, AGENTS.md,
RESUME.md, UNRESOLVED.md).
