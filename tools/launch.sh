#!/data/data/com.termux/files/usr/bin/bash
# NovAExorpus pipeline launch — sources secrets, boots Claude Code
# with router-guard output style in the corpus root.
#
# Usage:
#   bash tools/launch.sh          — full pipeline with router-guard
#   bash tools/launch.sh --agent corpus-architect  — with specific agent
#   alias cc="bash ~/repos/NovAExorpus/tools/launch.sh"

set -euo pipefail

# Load secrets (TB_MCP_KEY, MEM0_MCP_TOKEN, OMNIROUTE_API_KEY, etc.)
[ -f "$PREFIX/etc/secrets.env" ] && source "$PREFIX/etc/secrets.env"

# Export for .mcp.json env-var references
export TB_MCP_URL="${TB_MCP_URL:-http://34.31.112.77:8000}"
export TB_MCP_KEY="${TB_MCP_KEY:-}"
export MEM0_MCP_URL="${MEM0_MCP_URL:-https://mcp.mem0.ai/mcp}"
export MEM0_MCP_TOKEN="${MEM0_MCP_TOKEN:-}"
export OMNIROUTE_MCP_URL="${OMNIROUTE_MCP_URL:-http://34.31.112.77:20128}"
export OMNIROUTE_API_KEY="${OMNIROUTE_API_KEY:-}"

cd ~/repos/NovAExorpus

# Pre-flight: check layer health (non-blocking)
echo "[launch] Checking layers..."
curl -sf "http://34.31.112.77:20128/api/monitoring/health" >/dev/null 2>&1 \
  && echo "[launch] OmniRoute: UP" \
  || echo "[launch] OmniRoute: DOWN (fallback mode)"
curl -sf "http://34.31.112.77:8000/" >/dev/null 2>&1 \
  && echo "[launch] Terrestrial Brain: UP" \
  || echo "[launch] Terrestrial Brain: DOWN"
[ -x "$HOME/repos/NovA-code-review-graph/.venv-debian/bin/code-review-graph" ] \
  && echo "[launch] CRG: OK" \
  || echo "[launch] CRG: binary not found"
echo "[launch] mem0: cloud (always available)"
echo "[launch] Starting Claude Code with router-guard..."

exec claude --output-style router-guard "$@"
