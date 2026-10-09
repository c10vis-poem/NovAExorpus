---
title: "MAP.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/03_ALTERNATIVES_PROPOSAL_V1/novaexopia/MAP.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

MAP.md — novaecopia (The Tool Harness Runtime
& 3-APK Native Repo)
Subsystem Identity & Navigation Ontology
-​
WHO: Invoked by Horizons UI concierge, OpenWiki TUI, and local CLI agents (Æsc
shell, Prime Agent, ECC).
-​
WHAT: The execution bridge and native runtime environment hosting the decoupled
3-APK Android architecture, on-device daemons, Model Context Protocol (MCP)
connectors, and TUI profiles.
-​
WHEN: Active continuously on Node Alpha (Motorola Razr Ultra) during all interactive
terminal, voice ingress, screen capture, and tool execution sessions.
-​
WHERE: novaexopia/ (Subsystem Root inside
__NovÆxorpus_LIVING_MASTER_CANON).
-​
WHY: Decouples heavy AI execution, background terminals, and media streaming from
the Android UI process, eliminating Android LMK crashes and permission boundaries
without rooting.
-​
HOW: Inter-process communication across localhost TCP loopbacks, UNIX domain
sockets, and WebSocket channels.


Directory Topology
novaexopia/

├── MAP.md                      # This document (Internal layout and daemon topology)

├── manifest.jsonl              # Machine-readable catalog of all assets and endpoints

├── AGENTS.md                   # Operational guardrails, model roles, and execution rules

├── RESUME.md                   # Active runtime state, daemon PIDs, and checkpoint markers

├── UNRESOLVED.md               # Open engineering tickets, APK enhancements, latency
optimizations

│

├── aesc/                       # TIER 2 APK: System Terminal & Shell Daemon



│   ├── WirelessAdbBridgeService.kt # Kotlin local ADB loopback service (127.0.0.1:5555)

│   ├── npu_manager.py          # UNIX socket model swapper (/dev/socket/npu_manager.sock)

│   ├── system_housekeeper.sh   # Background maintenance & zero-trust hygiene daemon

│   └── agent_panel.sh          # Terminal UI controller and workspace monitor

│

├── aeyre/                      # TIER 3 APK: Media & Sensory Ingress Daemon

│   ├── voice_stream_daemon.py  # Audio ingress daemon (Silero VAD + Moonshine +
Kokoro)

│   └── screen_vision_bounds.json # Display coordinates, resolution, and VLM crop configs

│

├── horizons-ui/                # TIER 1 APK: Master Visual Concierge Frontend

│   └── webview_bridge_contract.json # JSON-RPC 2.0 WebSocket schema for UI-to-daemon
comms

│

├── openwiki-tui-harness/       # Unified Terminal User Interface Shell Profiles

│   ├── file_administrator.yaml # Configuration for File Administrator profile

│   └── oracle_helpdesk.yaml    # Configuration for Œræcle Help Desk profile

│

└── mcp_connectors/             # Model Context Protocol Tool Bridges

    ├── filesystem_mcp.json     # Node.js local filesystem MCP server configuration

    ├── sqlite_mcp.py           # Lightweight Python SQLite MCP server (stdio JSON-RPC)

    └── postgres_mcp.json       # PostgreSQL MCP connector over Tailscale mesh




Native Daemon Topology & Network Routing
┌───────────────────────────────────────────────────────────
─────────────┐

│                        HORIZONS UI (APK 1)                            │

│                     Master Visual Presentation                        │

│          - Chromium WebView (HTML5 / React user interface)             │

│          - JSON-RPC 2.0 WebSocket client to background daemons         │

└───────────────────┬────────────────────────────────┬──────
─────────────┘

                    │                                │

       WebSocket ws://127.0.0.1:8080/shell  WebSocket ws://127.0.0.1:8765/media

                    │                                │

                    ▼                                ▼

┌──────────────────────────────────────┐
┌───────────────────────────────┐

│              ÆSC (APK 2)             │ │             ÆYRE (APK 3)      │

│      Terminal & Shell Daemon         │ │    Media & Sensory Daemon     │

│ - ADB Loopback: 127.0.0.1:5555       │ │ - Silero VAD (Speech gating)  │

│ - Socket: /dev/socket/aesc_shell.sock│ │ - Moonshine Small ONNX (STT)  │

│ - NPU Mgr: /dev/socket/npu_manager...│ │ - Kokoro-82M ONNX (TTS)       │

│ - Background CLI agent executor      │ │ - Screen capture coordinate   │

│ - START_STICKY (LMK shielded)        │ │   bounding & VLM preprocessing│



└──────────────────────────────────────┘
└───────────────────────────────┘
