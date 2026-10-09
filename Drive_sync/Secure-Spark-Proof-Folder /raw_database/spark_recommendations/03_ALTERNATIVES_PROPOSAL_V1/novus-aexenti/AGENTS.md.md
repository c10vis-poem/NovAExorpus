---
title: "AGENTS.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/03_ALTERNATIVES_PROPOSAL_V1/novus-aexenti/AGENTS.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

AGENTS.md — novus-aexenti
Operational Guidelines & Model Invariants
1. Role Definitions
A. 0.8B Triage Model (Qwen3.5-0.8B-Instruct)
●​ Target Hardware: Snapdragon 8 Elite (Hexagon v79 HTP / NPU).
●​ Execution Format: GenieX / GGUF Q4_0.
●​ Scope:
○​ Classifying incoming voice/text input from Horizons UI and Æyre.
○​ Fast routing decisions (evaluating token counts and complexity thresholds).
○​ Direct execution of atomic queries (< 120 tokens, no code generation).
●​ Context Budget: Max 4,096 tokens (output capped at 512 tokens).
B. 9B Executor Model (Qwen3.5-9B-Instruct)
●​ Target Hardware: Jetson Orin Nano Super (CUDA) or local NPU.
●​ Execution Format: llama.cpp / GGUF Q4_0.
●​ Scope:
○​ Complex multi-step reasoning, tool execution, and code synthesis.
○​ File-by-file refactoring and structural audits.
○​ Receiving compressed meta-prompts formatted via executor_bridge.py.
●​ Context Budget: Max 16,384 tokens (output capped at 4,096 tokens).


2. Operational Invariants
1.​ Non-Destructive Execution: Under no circumstances should an agent overwrite or
delete original source documents in cold storage (01_raw_sources/).
2.​ Deterministic Fallbacks: All tools and scripts invoked by agents must yield
deterministic exit codes (0 for success, non-zero for error traces).
3.​ Session Checkpointing: Agents performing multi-step actions must update
active_execution_paths.json after every step to ensure recovery on power loss
or task interruption.
4.​ No Hallucinated Tool Names: Strict adherence to canonical repository names:
horizons-ui, novus-aexenti, novaecopia, aesop-xi, novae-xorpus, and
#d.u.m.b.a.s.s..
