---
title: "chunk.jsonl"
source: "Drive_sync/Secure-Spark-Proof-Folder /novus-aesc/chunk.jsonl.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

{"chunk_id":"novus_aesc_c001","source":"README.md","heading":"Overview","tokens":75,"text
":"novus-aesc (Æsc) is the native Android system terminal daemon and shell executor for the
NovÆxorpus ecosystem. It supersedes Termux sandbox limitations by running as a native
Android ForegroundService, maintaining persistent background execution and interfacing
directly with the device hardware."}
{"chunk_id":"novus_aesc_c002","source":"README.md","heading":"Core Architectural
Invariants","tokens":110,"text":"Configured with START_STICKY and
FOREGROUND_APP_ADJ to ensure continuous background operation without process
termination by Android OS. Maintains an elevated ADB loopback connection on 127.0.0.1:5555,
executing shell operations with UID 2000 privileges."}
{"chunk_id":"novus_aesc_c003","source":"README.md","heading":"NPU Hardware
Interfacing","tokens":65,"text":"Runs npu_manager.py over UNIX domain sockets to handle
zero-copy model switching and runtime execution across the Snapdragon Hexagon NPU."}
