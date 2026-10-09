---
title: "universal_memory_chunks.jsonl"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/03_ALTERNATIVES_PROPOSAL_V1/data_vault/03_recall_cache/universal_memory_chunks.jsonl.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

{"record_id": "MEM_HTP_NPU_001", "subsystem": "novaexopia/aesc", "title": "GenieX
Snapdragon NPU Execution", "content": "Snapdragon 8 Elite Hexagon v79 HTP runs GGUF
Q4_0 directly via GenieX. Hybrid mode provides ~90 tok/s prefill by offloading supported ops to
HTP while falling back to CPU.", "tokens": ["geniex", "npu", "htp", "gguf", "snapdragon"]}
{"record_id": "MEM_IPC_SHM_002", "subsystem": "novaexopia/aesc", "title": "ASharedMemory
Zero-Copy IPC", "content": "ASharedMemory_create and abstract UNIX domain sockets
(sun_path[0]='\\0') bypass Android 1MB Binder limits, allowing zero-copy tensor passing to
Qualcomm NPU.", "tokens": ["asharedmemory", "mmap", "scm_rights", "binder"]}
{"record_id": "MEM_MOE_MEM0_003", "subsystem": "novus-aexenti", "title": "3-Tier MoE
Memory Architecture", "content": "Mem0 decouples fast 0.8B intent triage from 4B/9B execution
within 6GB mobile RAM by extracting concise semantic facts without multi-turn chat history
bloat.", "tokens": ["mem0", "moe", "triage", "ram_ceiling"]}
{"record_id": "MEM_PIPE_DATA_004", "subsystem": "data_vault", "title": "Ingestion Pipeline
Order", "content": "Data moves strictly from raw sources to clean markdown, dual skill/tool
extraction, pre-tokenized JSONL chunks, and living wiki concepts.", "tokens": ["raw",
"clean_md", "skills", "tools", "chunks"]}
