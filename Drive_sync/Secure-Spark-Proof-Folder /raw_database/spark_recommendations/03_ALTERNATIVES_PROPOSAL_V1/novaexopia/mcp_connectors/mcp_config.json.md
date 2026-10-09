---
title: "mcp_config.json"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/03_ALTERNATIVES_PROPOSAL_V1/novaexopia/mcp_connectors/mcp_config.json.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

{
  "mcpServers": {
    "filesystem": {
      "command": "node",
      "args": [

"${HOME}/novae-xorpus/novaexopia/mcp_connectors/node_modules/@modelcontextprotocol/s
erver-filesystem/dist/index.js",
        "${HOME}/novae-xorpus"
      ],
      "env": {
        "NODE_ENV": "production"
      },
      "description": "Local filesystem access restricted to ~/novae-xorpus repository root."
    },
    "sqlite_memory": {
      "command": "python3",
      "args": [
        "${HOME}/novae-xorpus/novaexopia/mcp_connectors/sqlite_mcp.py",
        "--db",
        "${HOME}/novae-xorpus/_dumbass_universal_memory/sqlite/aesc_cache.db"
      ],
      "env": {
        "PYTHONUNBUFFERED": "1"
      },
      "description": "Embedded zero-latency key-value and task state database for
#d.u.m.b.a.s.s."
    },
    "adb_loopback": {
      "transport": "websocket",
      "url": "ws://127.0.0.1:8080/shell",
      "headers": {
        "X-Security-Clearance": "aesc_terminal_daemon"
      },
      "description": "Local ADB WebSocket bridge executing terminal shell commands with UID
2000 privileges."
    },
    "npu_manager": {
      "transport": "unix_socket",
      "socket_path": "/dev/socket/npu_manager.sock",
      "description": "Hexagon HTP v79 model scheduler and context priority router."
    }
  }


}
