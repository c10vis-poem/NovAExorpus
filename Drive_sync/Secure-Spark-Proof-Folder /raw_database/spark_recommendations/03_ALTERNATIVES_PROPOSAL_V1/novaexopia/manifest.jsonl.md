---
title: "manifest.jsonl"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/03_ALTERNATIVES_PROPOSAL_V1/novaexopia/manifest.jsonl.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

{"name": "MAP.md", "path": "MAP.md", "type": "reference", "subsystem": "root", "description":
"Internal directory layout and native daemon topology for novaecopia."}
{"name": "manifest.jsonl", "path": "manifest.jsonl", "type": "data", "subsystem": "root",
"description": "Machine-readable streaming catalog of all assets and tools in novaecopia."}
{"name": "AGENTS.md", "path": "AGENTS.md", "type": "policy", "subsystem": "root",
"description": "Operational guardrails, memory boundaries, and execution rules for agents."}
{"name": "RESUME.md", "path": "RESUME.md", "type": "memory", "subsystem": "root",
"description": "Active runtime state, socket paths, daemon PIDs, and checkpoint markers."}
{"name": "UNRESOLVED.md", "path": "UNRESOLVED.md", "type": "reference", "subsystem":
"root", "description": "Engineering backlog, APK enhancements, latency optimizations, and open
tickets."}
{"name": "WirelessAdbBridgeService.kt", "path": "aesc/WirelessAdbBridgeService.kt", "type":
"tool", "subsystem": "aesc", "description": "Kotlin START_STICKY service for local ADB
loopback on 127.0.0.1:5555 without root."}
{"name": "npu_manager.py", "path": "aesc/npu_manager.py", "type": "tool", "subsystem": "aesc",
"description": "UNIX domain socket model swapping daemon on
/dev/socket/npu_manager.sock."}
{"name": "system_housekeeper.sh", "path": "aesc/system_housekeeper.sh", "type": "tool",
"subsystem": "aesc", "description": "Zero-trust hygiene daemon, process supervisor, and
manifest validator."}
{"name": "agent_panel.sh", "path": "aesc/agent_panel.sh", "type": "tool", "subsystem": "aesc",
"description": "Terminal UI control panel for workspace monitoring, sync, and process status."}
{"name": "voice_stream_daemon.py", "path": "aeyre/voice_stream_daemon.py", "type": "tool",
"subsystem": "aeyre", "description": "Low-latency audio ingress daemon combining Silero VAD,
Moonshine STT, and Kokoro TTS."}
{"name": "screen_vision_bounds.json", "path": "aeyre/screen_vision_bounds.json", "type":
"schema", "subsystem": "aeyre", "description": "Display coordinate bounds, resolution scaling,
and VLM crop configs."}
{"name": "webview_bridge_contract.json", "path": "horizons-ui/webview_bridge_contract.json",
"type": "schema", "subsystem": "horizons-ui", "description": "JSON-RPC 2.0 WebSocket schema
between Chromium WebView and backend daemons."}
{"name": "file_administrator.yaml", "path": "openwiki-tui-harness/file_administrator.yaml", "type":
"skill", "subsystem": "openwiki-tui-harness", "description": "OpenWiki TUI File Administrator
profile configuration for codebase hygiene."}
{"name": "oracle_helpdesk.yaml", "path": "openwiki-tui-harness/oracle_helpdesk.yaml", "type":
"skill", "subsystem": "openwiki-tui-harness", "description": "OpenWiki TUI Œræcle Help Desk
profile configuration for on-device troubleshooting."}
{"name": "filesystem_mcp.json", "path": "mcp_connectors/filesystem_mcp.json", "type":
"schema", "subsystem": "mcp_connectors", "description": "Configuration for Node.js filesystem
MCP server with path sandboxing."}
{"name": "sqlite_mcp.py", "path": "mcp_connectors/sqlite_mcp.py", "type": "tool", "subsystem":
"mcp_connectors", "description": "Lightweight Python MCP server providing safe read/write
SQLite operations via stdio."}


{"name": "postgres_mcp.json", "path": "mcp_connectors/postgres_mcp.json", "type": "schema",
"subsystem": "mcp_connectors", "description": "PostgreSQL MCP connector configuration over
encrypted Tailscale mesh."}
