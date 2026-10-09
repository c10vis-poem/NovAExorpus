---
title: "AGENTS.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/03_ALTERNATIVES_PROPOSAL_V1/novaexopia/AGENTS.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

AGENTS.md — novaecopia Operational Boundaries
& Execution Rules
Target Scope & Agent Roles
This document specifies the operational rules, model tiering, and hardware boundaries for all
autonomous agents executing within novaexopia/.


1. Multi-Model Tiering & Responsibilities
Agent Tier
Primary Model
Hardware Allocation Assigned Role in
novaecopia
Triage / Gatekeeper
Qwen 2.5 / 3.5 0.8B
CPU Little Cores
Parses incoming
voice/text payloads;
determines whether
an action requires
tool execution, shell
invocation, or direct
conversational
response.
Local Executor
Qwen 3.5 9B Q4_0 /
Gemma 4 12B QAT
Hexagon v79 NPU
(Node Alpha)
Executes complex
reasoning, code
inspection, AST
queries, and MCP
tool calls. Must obey
NPU swapping
protocols.
Frontier Scripter
Claude 3.7 Sonnet /
Opus (ECC /
OpenRouter)
Cloud API Fallback
Handles massive
refactoring, deep
multi-file compilation,
and training batch
synthesis.




2. Hardware & Memory Invariants (Anti-LMK Rules)
1.​ Strict Single-Model NPU Invariant:
-​
Android's Low Memory Killer (LMK) enforces strict memory pressure ceilings.
Never attempt to load two local LLMs concurrently.
-​
Any model transition must issue a SWAP command to
/dev/socket/npu_manager.sock and await confirmation before loading the
next backend.
2.​ Thermal Throttling Ceilings:
-​
Battery/SoC temperature ceiling is set to 42°C for background tasks and 45°C for
interactive inference. If exceeded, agents must switch to cloud fallback or pause.
3.​ Elevated Shell Loopback Protocol:
-​
Never attempt raw unprivileged shell execution. Route commands through
WirelessAdbBridgeService on 127.0.0.1:5555 or the Ktor WebSocket
bridge on ws://127.0.0.1:8080/shell to retain UID 2000 (shell)
capabilities without rooting.


3. Tool & Skill Execution Guidelines
-​
MCP Isolation: All filesystem, SQLite, and PostgreSQL database queries must pass
through the registered MCP servers in mcp_connectors/.
-​
Sensory Deferral: Audio capture (voice_stream_daemon.py) and screen capture
(screen_vision_bounds.json) operate under aeyre/ with priority yielding during
heavy model inference.
-​
Naming Rule: The canonical name of this repository and subsystem is novaecopia
(NovaeCopia™). Never use deprecated or hallucinated names (e.g., "Omni Claw" is
strictly prohibited).
-​
Manifest Mutation Mandate: Every new script, tool, or profile created in novaexopia
must be registered in manifest.jsonl immediately upon creation.
