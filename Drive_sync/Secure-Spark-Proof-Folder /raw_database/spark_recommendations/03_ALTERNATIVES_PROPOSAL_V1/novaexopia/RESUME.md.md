---
title: "RESUME.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/03_ALTERNATIVES_PROPOSAL_V1/novaexopia/RESUME.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

RESUME.md — novaecopia Runtime State &
Recovery Checkpoint
Session Context & Active Architecture State
-​
Current Operational Node: Node Alpha (Motorola Razr Ultra 2025 / Snapdragon 8
Elite)
-​
Subsystem Target: novaexopia/ (Tool Harnesses, 3-APK Decoupled Topology, MCP
Bridges)
-​
Last Sync Timestamp: 2026-09-06T19:07:00-07:00


1. Active Daemon & Socket Ledger
Daemon / Service
Target Endpoint /
Socket
Active Status
Process Role
WirelessAdbBridg
eService
127.0.0.1:5555
(TCP)
PAIRED / RUNNING
Elevated Android
shell execution with
UID 2000
Ktor WebSocket
Bridge
ws://127.0.0.1:8
080/shell
LISTENING
Terminal streaming to
Horizons UI
Chromium viewport
npu_manager.py
/dev/socket/npu_
manager.sock
ACTIVE (GenieX
Backend)
Model swapping
between Qwen 3.5
9B and Gemma 4
QAT
voice_stream_dae
mon.py
/dev/socket/aeyr
e_media.sock
INITIALIZED (Silero
VAD)
Ambient voice
ingress and
Kokoro-82M TTS
synthesis
OpenWiki TUI File
Admin
stdio / TUI
STAGED
Low-overhead
codebase sanitization
& manifest
compilation




2. MCP Server Connectivity
-​
Filesystem MCP: Configured in mcp_connectors/filesystem_mcp.json.
Sandboxed to ~/novae-xorpus.
-​
SQLite MCP: Deployed in mcp_connectors/sqlite_mcp.py. Ready for local
#d.u.m.b.a.s.s. tables and audit_ledger.db.
-​
PostgreSQL MCP: Configured in mcp_connectors/postgres_mcp.json. Direct
route to Node Beta (Jetson Orin Nano Super) via Tailscale IP 100.64.0.2:5432.


3. Fast Recovery & Bootstrap Commands
If the device reboots or process state drops:

# 1. Verify ADB Loopback connection

adb connect 127.0.0.1:5555

# 2. Spawn NPU manager socket daemon in background

python3 novaexopia/aesc/npu_manager.py &

# 3. Launch Æyre voice stream daemon

python3 novaexopia/aeyre/voice_stream_daemon.py &

# 4. Open Æsc Agent Panel

bash novaexopia/aesc/agent_panel.sh
