#!/data/data/com.termux/files/usr/bin/bash
# tools/bootstrap.sh — NovÆxorpus full-stack startup
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VM_IP="34.31.112.77"
GCLOUD="$HOME/google-cloud-sdk/bin/gcloud"

log() { echo "[bootstrap] $*"; }

# --- Layer 1: Output discipline (local, always available) ---
log "Layer 1: Honey + task-observer (loaded by Claude Code via skills)"

# --- Layer 2: Memory & knowledge MCPs ---
log "Layer 2: Checking MCP servers..."

# OmniRoute on VM
if curl -sf "http://$VM_IP:20128/api/monitoring/health" >/dev/null 2>&1; then
  log "  OmniRoute: healthy"
else
  log "  OmniRoute: DOWN — starting on VM..."
  if [ -x "$GCLOUD" ]; then
    "$GCLOUD" compute ssh omniroute-brain --zone=us-central1-a \
      --command='omniroute serve --daemon --no-open --no-tray' 2>/dev/null || true
    sleep 3
    curl -sf "http://$VM_IP:20128/api/monitoring/health" >/dev/null 2>&1 \
      && log "  OmniRoute: started" \
      || log "  OmniRoute: FAILED to start"
  else
    log "  WARN: gcloud not installed, cannot start OmniRoute remotely"
  fi
fi

# Terrestrial Brain on VM
if curl -sf "http://$VM_IP:8000/" >/dev/null 2>&1; then
  log "  Terrestrial Brain: running"
else
  log "  Terrestrial Brain: DOWN — needs manual start on VM"
fi

# mem0 (cloud, always available)
log "  mem0: cloud (mcp.mem0.ai)"

# code-review-graph (local stdio, started by Claude Code on demand)
log "  code-review-graph: local stdio (proot debian)"

# --- Layer 3: Behavioral constraints (loaded via CLAUDE.md) ---
log "Layer 3: Behavioral constraints (via CLAUDE.md)"

# --- Layer 4: Success tracking ---
log "Layer 4: Success Rate Verification Grade (via CLAUDE.md rubric)"

# --- Layer 5: Obsidian vault link check ---
VAULT="$HOME/storage/shared/Documents/NovAExorpus"
if [ -d "$VAULT/.obsidian" ]; then
  log "Layer 5: Obsidian vault found at $VAULT"
else
  log "Layer 5: WARN — Obsidian vault not found at $VAULT"
fi

log "Bootstrap complete."
