---
title: "aesc-terminal-orchestrator.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/03_ALTERNATIVES_PROPOSAL_V1/skills-and-capabilities/prompt_skills/aesc-terminal-orchestrator.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

name: aesc-terminal-orchestrator description: Operational guide
and prompt skill for LLMs to interface with the Æsc Terminal
Daemon APK, routing NPU models via UNIX domain sockets,
executing shell commands through local ADB WebSockets, and
retrieving files via MCP.
Æsc Terminal Orchestrator Protocol
Overview & Identity
The Æsc Terminal Daemon (aesc APK) is the native Android system execution layer that
completely replaces Termux. It runs as a START_STICKY foreground Android service, holds the
local ADB loopback connection on 127.0.0.1:5555 with elevated UID 2000 (shell)
privileges, hosts a Ktor WebSocket server on port 8080, and interfaces directly with the
Qualcomm Hexagon HTP v79 NPU over UNIX domain sockets.

When operating as an agent inside or connected to the Æsc terminal environment, you must
adhere to the three operational execution channels detailed below.


Execution Channel 1: Snapdragon Hexagon NPU Routing
All local model swaps and context priority allocations are routed through the local UNIX domain
socket:

●​ Socket Path: /dev/socket/npu_manager.sock
●​ Transport: POSIX AF_UNIX Stream Socket
1. Model Roles & Hardware Priorities
●​ 0.8B_triage (qwen3.5-0.8b-q4_0): Run under QNN_PRIORITY_LOW. Used for
intent routing, token classification, and entity extraction. Interruptible with minimal
thermal impact.
●​ 9B_executor (qwen3.5-9b-q4_0): Run under QNN_PRIORITY_HIGH. Used for code
generation, multi-step planning, and complex AST analysis.


2. Hardware Prefill Chunking Guardrail
●​ Maximum Prefill Chunk: 512 tokens.
●​ Never send unchunked prompts larger than 512 tokens directly to the HTP in a single
pass. Hexagon DSP hardware watchdog timers will abort execution if prefill bursts
exceed hardware timeout thresholds.
3. Socket JSON-RPC Schema
To dispatch an inference pass or check status, format your socket payload as:

{

  "action": "infer",

  "model_role": "0.8B_triage",

  "tokens": [101, 2054, 2003, ...],

  "max_tokens": 1024

}

To request a model swap:

{

  "action": "swap_model",

  "target_role": "9B_executor"

}


Execution Channel 2: Local ADB Loopback Shell
Terminal shell commands must be executed through the elevated ADB loopback bridge rather
than standard Android app sandboxes.
1. Connection Architecture
●​ Loopback URL: ws://127.0.0.1:8080/shell


●​ Underlying ADB Bridge: 127.0.0.1:5555 (Paired via Wireless Debugging)
●​ Privilege Level: UID 2000 (shell) — grants access to background daemon
spawning, /data/local/tmp, and cross-process signals without requiring root.
2. Execution Protocol
1.​ Open a WebSocket frame to ws://127.0.0.1:8080/shell.
2.​ Transmit the command string as a plain text frame.
3.​ Stream the output frames until the process exit code is returned.
4.​ Safety Rule: Always use absolute paths or paths rooted at ${HOME}/novae-xorpus.
Never issue recursive deletion commands (rm -rf) on root or sensory archives
(01_raw_sources/).


Execution Channel 3: Model Context Protocol (MCP) Suite
When retrieving files, inspecting schemas, or updating memory records, use the configured
MCP connectors rather than raw terminal calls whenever possible.
Available MCP Servers
1.​ filesystem:
●​ Scoped to ${HOME}/novae-xorpus.
●​ Tools: read_file, write_file, list_directory, get_file_info.
●​ Invariant: Modification of files in 01_raw_sources/ is strictly denied.
2.​ sqlite_memory:
●​ Connected to
${HOME}/novae-xorpus/_dumbass_universal_memory/sqlite/aesc_c
ache.db.
●​ Tools: query, execute, get_task_state.
●​ Used for low-latency active session state persistence and entity lookups.
3.​ npu_manager:
●​ UNIX socket bridge for real-time model telemetry and thermal status checks.


Summary of Invariants for Agents
1.​ Thermal Headroom Check: Before launching heavy 9B executor passes, query
/dev/socket/npu_manager.sock for thermal state. If status is WARM (≥42°C), defer
non-critical batch processing.


2.​ Zero App GC Interference: Keep model execution completely inside native background
processes (:qairt_engine, qnn_htp_scheduler.py) to prevent Android UI
micro-stutters.
3.​ Session Checkpointing: Log all multi-step tool invocations to sqlite_memory so that
any unexpected daemon termination resumes from the latest verified step.
