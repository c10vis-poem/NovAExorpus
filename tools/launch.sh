#!/data/data/com.termux/files/usr/bin/bash
# NovAExorpus pipeline launch — sources secrets, starts Claude Code
# with router-guard output style in the corpus root.

set -euo pipefail

# Load secrets (TB_MCP_URL, TB_MCP_KEY, etc.)
[ -f "$PREFIX/etc/secrets.env" ] && source "$PREFIX/etc/secrets.env"

# Export for .mcp.json env-var references
export TB_MCP_URL="${TB_MCP_URL:-http://34.31.112.77:8000}"
export TB_MCP_KEY="${TB_MCP_KEY:-}"
export MEM0_MCP_URL="${MEM0_MCP_URL:-https://mcp.mem0.ai/mcp}"
export MEM0_MCP_TOKEN="${MEM0_MCP_TOKEN:-}"
export OMNIROUTE_MCP_URL="${OMNIROUTE_MCP_URL:-http://34.31.112.77:20128}"
export OMNIROUTE_API_KEY="${OMNIROUTE_API_KEY:-}"

cd ~/repos/NovAExorpus

exec claude --output-style router-guard "$@"
