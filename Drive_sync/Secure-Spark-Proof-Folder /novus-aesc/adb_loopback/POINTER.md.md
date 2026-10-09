---
title: "POINTER.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /novus-aesc/adb_loopback/POINTER.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

# POINTER.md — novus-aesc Subsystem Specification
Repository: novus-aesc (APK 2 — Native System Terminal & Shell Daemon)
Authority: 01_SOVEREIGN_NODE_AND_APK_TOPOLOGY.md &
05_FEDERATED_FILE_TREE_TOPOLOGY_MASTER.md

## Core Architectural Invariants
1. ForegroundService Execution: Runs with START_STICKY and FOREGROUND_APP_ADJ to
ensure 100% resilience against Android Low Memory Killer (LMK).
2. ADB Loopback (127.0.0.1:5555): Maintains persistent loopback connection to execute shell
commands with UID 2000 permissions without requiring root.
3. NPU Watchdog: Operates npu_manager.py over UNIX domain sockets
(/dev/socket/npu_manager.sock) for hot-swapping open-weights on Qualcomm Hexagon NPU.
4. Laptop Trick Tunnel: Routes reverse-proxy shell connections and debugging telemetry across
local network interfaces.
5. Ingestion & Normalization: Awaits Phase 1 extraction and script migration from Termux
environment.
