---
title: "README.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /novus-aesc/README.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

# novus-aesc — Native System Terminal & Shell Daemon (APK 2)

## Overview
`novus-aesc` (Æsc) is the native Android system terminal daemon and shell executor for the
NovÆxorpus ecosystem. It supersedes Termux sandbox limitations by running as a native
Android ForegroundService, maintaining persistent background execution and interfacing
directly with the device hardware.

## Core Architectural Invariants
1. **Low Memory Killer (LMK) Resilience:** Configured with `START_STICKY` and
`FOREGROUND_APP_ADJ` to ensure continuous background operation without process
termination by Android OS.
2. **Elevated Shell Access:** Maintains an elevated ADB loopback connection on
`127.0.0.1:5555`, executing shell operations with UID 2000 privileges.
3. **NPU Hardware Interfacing:** Runs `npu_manager.py` over UNIX domain sockets to handle
zero-copy model switching and runtime execution across the Snapdragon Hexagon NPU.
4. **Locality of Reference:** Subsystem-specific scripts, tools, and hooks live locally inside this
repository.

## Subdirectories
- `raw/` — Ingestion landing zone for raw logs, shell traces, and input dumps.
- `clean_md/` — Clean, condensed technical markdown documentation.
- `wiki_md/` — Living wiki documentation nodes linked via `[[wikilinks]]`.
- `skills/` — Terminal operation and daemon control procedural skills.
- `tools/` — Local CLI tools, socket testers, and execution wrappers.
- `scripts/` — Subsystem shell and Python scripts (daemon startup, ADB connect, NPU
controls).
- `hooks/` — Lifecycle management, Git, and automated audit hooks.
- `pending/` — Backlog tasks and staging tickets.
- `audit/` — System logs, failure traces, and regression test results.
- `archive/` — Historical logs and superseded scripts.
- `laptop_trick_tunnel/` — Reverse tunnel routing scripts and protocols.
- `npu_watchdog/` — Health checking and watchdog services for NPU domain sockets.
- `adb_loopback/` — Loopback initialization, key management, and execution harnesses.

## Master References
- `01_SOVEREIGN_NODE_AND_APK_TOPOLOGY.md`
- `00_DEFINITIVE_MASTER_SPECIFICATION_V3_COMPLETE.md`
- `PROPOSAL-V2-CORRECTED-WIKI-TERMINOLOGY-AND-s-tier-ALTERNATIVE.md`
