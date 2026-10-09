---
title: "UNRESOLVED.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/03_ALTERNATIVES_PROPOSAL_V1/novus-aexenti/UNRESOLVED.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

UNRESOLVED.md — novus-aexenti
Pending Issues, Optimizations & Backlog
Open Items & Tasks
1.​ NPU Thermal Throttling on Continuous Voice Streams:

●​ Description: When running Moonshine STT and Qwen 0.8B simultaneously
during long conversations, observe if Hexagon NPU thermal throttling drops
inference below 25 tok/sec.
●​ Target: Validate latency on Motorola Razr Ultra under load.

2.​ KV-Cache RAM Footprint on Jetson Orin Nano:

●​ Description: 9B Qwen model at 16k context window exceeds 6.2GB RAM without
TurboQuant.
●​ Target: Implement 4-bit KV-cache quantization (-ctk q4_0 -ctv q4_0) in
llama-server launch flags.

3.​ Mem0 Episodic Persistence vs SQLite Migration:

●​ Description: Evaluate whether in-session rolling_habits.json should
migrate to the local SQLite #d.u.m.b.a.s.s. database instance for
sub-millisecond retrieval.
●​ Target: Cross-link with #d.u.m.b.a.s.s. relational memory schema.

4.​ Car Wash Test Harness Validation:

●​ Description: Execute the synthetic end-to-end integration test across simulated
audio ingress and execution output to measure failure recovery response.
