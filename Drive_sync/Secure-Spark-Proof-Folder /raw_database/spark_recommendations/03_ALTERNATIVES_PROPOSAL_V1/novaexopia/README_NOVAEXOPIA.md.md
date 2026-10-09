---
title: "README_NOVAEXOPIA.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/03_ALTERNATIVES_PROPOSAL_V1/novaexopia/README_NOVAEXOPIA.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

README — novaexopia/
The "Claw" Harness Runtimes, 3-APK Topology & Terminal Shells
W5+H Subsystem Identity
●​ WHO: Houses Horizons UI (APK 1), Æsc (APK 2: Terminal daemon), Æyre (APK 3:
Media daemon), and OpenWiki TUI.
●​ WHAT: Native Android services, Ktor WebSocket bridges, ADB loopback clients, Prime
Agent RLM loops, and MCP connectors.
●​ WHEN: Active continuously from Android boot (START_STICKY); listens for UI
interactions, shell commands, and audio streams.
●​ WHERE: novae-xorpus/novaexopia/ (Federated Subsystem Root).
●​ WHY: Eliminates Android sandbox restrictions and Low Memory Killer (LMK) process
termination, bypassing Termux entirely.
●​ HOW: Decouples UI rendering from native execution daemons, streaming data across
local UNIX sockets (AF_UNIX) and Netty WebSockets.


Internal Directory Topology
novaexopia/

├── README.md                                # This document (APK architecture & harnesses)

├── manifest.jsonl                           # Local cryptographic catalog of runtimes & tools

│

├── horizons-ui/                             # APK 1: Master Visual Presentation Shell

│   ├── app/src/main/assets/web/             # Chromium WebView HTML5 / React bundle

│   ├── ui_tiles/                            # Chat interface tile, Terminal visualizer, Model picker

│   └── bridge/                              # Persistent WebSocket clients to Æsc and Æyre

│

├── aesc/                                    # APK 2: System Terminal Daemon (Termux Replacement)



│   ├── src/main/java/com/horizons/ui/adb/   # WirelessAdbBridgeService.kt (Loopback on
127.0.0.1:5555)

│   ├── npu_watchdog/                        # npu_manager.py (UNIX socket hot-swap daemon)

│   └── scripts/                             # system_housekeeper.sh, agent_panel.sh

│

├── aeyre/                                   # APK 3: Media & Sensory Ingress Daemon

│   ├── voice_stack/                         # Silero VAD, Moonshine ONNX STT, Kokoro-82m TTS

│   └── screen_vision/                       # Android Media & Video Game SDK frame capture

│

├── openwiki-tui-harness/                    # Interactive Terminal Workspace Shell

│   ├── config_profiles/

│   │   ├── file_administrator.yaml          # Profile A: Master database housekeeper

│   │   └── oracle_helpdesk.yaml             # Profile B: On-device interactive help desk

│   └── src/                                 # OpenWiki CLI terminal bindings

│

├── modular_harnesses/                       # Agent Execution Frameworks

│   ├── prime-agent/                         # Prime Intellect RLM loop inside persistent Python REPL

│   └── ecc-claude-code/                     # Everything Claude Code specialized prompt skills

│

└── mcp_connectors/                          # Model Context Protocol Server Suite

    ├── filesystem_mcp/                      # Node.js @modelcontextprotocol/server-filesystem

    ├── sqlite_mcp/                          # Python on-device embedded key-value server



    └── postgres_mcp/                        # Remote OB1 connection over Tailscale


Beginner-Proof Implementation Rules
1.​ Fault Isolation: If the model process dies inside aesc/, horizons-ui/ remains
completely stable and reconnects automatically via WebSockets.
2.​ No Root Required: All shell privileges are obtained through the onboard loopback
connection to 127.0.0.1:5555 via Wireless Debugging.
