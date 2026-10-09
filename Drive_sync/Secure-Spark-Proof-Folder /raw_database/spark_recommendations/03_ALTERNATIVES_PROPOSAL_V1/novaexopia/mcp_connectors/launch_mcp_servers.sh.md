---
title: "launch_mcp_servers.sh"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/03_ALTERNATIVES_PROPOSAL_V1/novaexopia/mcp_connectors/launch_mcp_servers.sh.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

#!/usr/bin/env bash
#
========================================================================
======
# launch_mcp_servers.sh — Production Startup for MCP Suite (Æsc Terminal Daemon)
# Directory: novaexopia/mcp_connectors/
# Target User: UID 2000 (shell) / Android App Sandbox
#
========================================================================
======

set -euo pipefail

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_DIR="${BASE_DIR}/logs"
PID_DIR="${BASE_DIR}/pids"
WORKSPACE_DIR="${HOME}/novae-xorpus"
DB_PATH="${BASE_DIR}/../../_dumbass_universal_memory/sqlite/aesc_cache.db"

mkdir -p "${LOG_DIR}" "${PID_DIR}" "${WORKSPACE_DIR}"

echo "[*] Initializing Model Context Protocol (MCP) Server Suite..."

# Graceful cleanup on SIGINT / SIGTERM
cleanup() {
    echo ""
    echo "[!] Trapped termination signal. Stopping all active MCP servers..."
    for pidfile in "${PID_DIR}"/*.pid; do
        if [ -f "$pidfile" ]; then
            pid=$(cat "$pidfile")
            server_name=$(basename "$pidfile" .pid)
            if kill -0 "$pid" 2>/dev/null; then
                echo "    [-] Stopping ${server_name} (PID: ${pid})..."
                kill -TERM "$pid" 2>/dev/null || kill -KILL "$pid" 2>/dev/null
            fi
            rm -f "$pidfile"
        fi
    done
    echo "[✓] All MCP servers halted cleanly."
    exit 0
}
trap cleanup SIGINT SIGTERM EXIT



# 1. Start Node.js Filesystem MCP Server
echo "[+] Starting Node.js Filesystem MCP Server..."
if command -v node >/dev/null 2>&1; then
    NODE_ENV=production node
"${BASE_DIR}/node_modules/@modelcontextprotocol/server-filesystem/dist/index.js" \
        "${WORKSPACE_DIR}" \
        > "${LOG_DIR}/filesystem_mcp.log" 2>&1 &
    FS_PID=$!
    echo $FS_PID > "${PID_DIR}/filesystem_mcp.pid"
    echo "    [✓] Filesystem MCP running on PID ${FS_PID} (Target: ${WORKSPACE_DIR})"
else
    echo "    [!] WARN: Node.js binary not found. Skipping filesystem MCP launch."
fi

# 2. Start Python SQLite MCP Bridge
echo "[+] Starting Python SQLite MCP Server..."
if command -v python3 >/dev/null 2>&1; then
    python3 "${BASE_DIR}/sqlite_mcp.py" \
        --db "${DB_PATH}" \
        > "${LOG_DIR}/sqlite_mcp.log" 2>&1 &
    SQLITE_PID=$!
    echo $SQLITE_PID > "${PID_DIR}/sqlite_mcp.pid"
    echo "    [✓] SQLite MCP running on PID ${SQLITE_PID} (Target DB: ${DB_PATH})"
else
    echo "    [!] WARN: Python3 binary not found. Skipping SQLite MCP launch."
fi

# 3. Verify ADB Loopback Socket
echo "[+] Checking Local ADB Loopback Socket (127.0.0.1:5555)..."
if nc -z 127.0.0.1 5555 2>/dev/null || (exec 3<>/dev/tcp/127.0.0.1/5555) 2>/dev/null; then
    echo "    [✓] Local ADB daemon responsive on port 5555."
else
    echo "    [!] NOTE: Local ADB port 5555 not active yet. Wireless Debugging pairing required."
fi

echo "[*] All background MCP connectors dispatched. Monitoring process health..."
while true; do
    sleep 10
done
