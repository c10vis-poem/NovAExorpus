---
title: "MAP.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /novus-aesc/MAP.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

# MAP.md — novus-aesc Repository Navigation & Component Ledger

**Subsystem Identity:** `novus-aesc` (Æsc / APK 2 System Daemon)
**Location:** `/novus-aesc/`
**Primary Authority:** [[01_SOVEREIGN_NODE_AND_APK_TOPOLOGY.md]] |
[[05_FEDERATED_FILE_TREE_TOPOLOGY_MASTER.md]] |
[[PROPOSAL-V2-CORRECTED-WIKI-TERMINOLOGY-AND-s-tier-ALTERNATIVE.md]]

---

## 1. Subsystem Scope & Architectural Responsibilities
- **Role:** Native Android system terminal and background daemon service.
- **Process Management:** Runs as a ForegroundService with `START_STICKY` and
`FOREGROUND_APP_ADJ` to bypass Android Low Memory Killer (LMK).
- **Elevated Execution:** Operates ADB loopback connection on `127.0.0.1:5555` executing as
UID 2000 (`shell`).
- **Hardware Interfacing:** Houses `npu_manager.py` over UNIX domain sockets for dynamic
model switching and execution control.

---

## 2. Directory Hierarchy & Navigation
- [[raw/]] — Intake landing zone for untransformed incoming scripts and logs.
- [[clean_md/]] — Condensed technical documentation adhering to Non-1:1 Condensation Law.
- [[wiki_md/]] — Compounding living wiki notes with bidirectional `[[wikilinks]]`.
- [[skills/]] — Locally co-located procedural skills for terminal management and shell automation.
- [[tools/]] — Local CLI utilities, socket monitors, and packaging tools.
- [[scripts/]] — Executable shell and Python scripts for daemon execution, ADB loopback, and
NPU control.
- [[hooks/]] — Subsystem-specific lifecycle, sync, and audit hooks.
- [[pending/]] — Staged tasks, backlogs, and unverified work.
- [[audit/]] — Test outputs, failure traces, and hygiene logs.
- [[archive/]] — Superseded snapshots and historical records.

### Domain-Specific Subfolders:
- [[laptop_trick_tunnel/]] — Laptop trick reverse tunnel protocols and connection scripts.
- [[npu_watchdog/]] — Watchdog service monitoring Hexagon NPU execution state and socket
health.
- [[adb_loopback/]] — ADB loopback connection manager (`127.0.0.1:5555`) with UID 2000
shell wrappers.

---



## 3. Upstream Spec References
- **Apex Architecture:** `00_DEFINITIVE_MASTER_SPECIFICATION_V3_COMPLETE.md`
- **Node & APK Topology:** `01_SOVEREIGN_NODE_AND_APK_TOPOLOGY.md`
- **Memory Subsystem:** `02_DUMBASS_UNIVERSAL_MEMORY_SPEC.md`
- **Federated Topology:** `05_FEDERATED_FILE_TREE_TOPOLOGY_MASTER.md`
- **Terminology & Philosophy:**
`PROPOSAL-V2-CORRECTED-WIKI-TERMINOLOGY-AND-s-tier-ALTERNATIVE.md`
