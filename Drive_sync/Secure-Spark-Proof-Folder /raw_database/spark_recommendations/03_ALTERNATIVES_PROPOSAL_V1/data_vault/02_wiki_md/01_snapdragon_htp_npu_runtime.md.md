---
title: "01_snapdragon_htp_npu_runtime.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/03_ALTERNATIVES_PROPOSAL_V1/data_vault/02_wiki_md/01_snapdragon_htp_npu_runtime.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

# Snapdragon 8 Elite Hexagon v79 HTP & GenieX Runtime

## 1. Unified GenieX Execution Pipeline
Snapdragon 8 Elite utilizes Qualcomm's GenieX runtime (`qualcomm/GenieX`) with native
GGML Hexagon backend integration.
- **Direct GGUF Execution**: Any HuggingFace GGUF (e.g. Qwen 3.5 0.8B / 9B Q4_0)
executes directly on the NPU without offline host compilation.
- **Execution Modes**:
  - `--device hybrid`: Per-tensor scheduling offloading supported ops to HTP while falling back
gracefully (~90 tok/s prefill, ~27 tok/s decode).
  - `--device npu`: Pinned deterministic execution on HTP0.

## 2. Low Memory Killer (LMK) Isolation
By running model inference inside isolated native daemons (`:qairt_engine`,
`:llamacpp_engine`) communicating via UNIX domain sockets, the system avoids Android UI
GC pauses and insulates background tasks from game/UI stutters.
