#!/usr/bin/env bash
# vm-install.sh — Bootstrap the GCP VM with dev services
#
# Run ON THE VM (via SSH), not on the phone.
#   ssh user@34.31.112.77 'bash -s' < tools/vm-install.sh
#
# Installs:
#   1. code-server   — VS Code in browser (:8080)
#   2. ttyd          — terminal in browser (:7681)
#   3. dsh           — DeepSeek harness web UI (:8001)
#   4. idle-shutdown — auto-stop VM after 60min idle
#
# NOT installed here:
#   - ollama / Qwen Coder — runs on phone via Qualcomm NPU (QAIR/T + HTP SDK)
#   - OmniRoute (:20128) and TB (:8000) — already running via systemd
#
# Architecture:
#   Phone (Snapdragon NPU) → local inference (Qwen Coder via QAIR/T)
#   VM (GCP)               → code-server, dsh (DeepSeek via OpenRouter), OmniRoute, TB

set -euo pipefail

OPENROUTER_KEY="${OPENROUTER_API_KEY:-}"
DSH_PORT=8001
CODESERVER_PORT=8080
TTYD_PORT=7681

log() { printf '\n=== %s ===\n' "$1"; }

# ── 1. System deps ──────────────────────────────────────────────────────
log "System packages"
sudo apt-get update -qq
sudo apt-get install -y -qq curl git tmux jq nginx-light

# ── 2. Node.js 22 (for dsh) ────────────────────────────────────────────
log "Node.js"
if ! node --version 2>/dev/null | grep -qE '^v2[2-9]|^v[3-9]'; then
  curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
  sudo apt-get install -y -qq nodejs
fi
npm install -g pnpm@latest 2>/dev/null || true
echo "Node $(node --version), pnpm $(pnpm --version)"

# ── 3. code-server (VS Code in browser) ────────────────────────────────
log "code-server"
if ! command -v code-server >/dev/null 2>&1; then
  curl -fsSL https://code-server.dev/install.sh | sh
fi
mkdir -p ~/.config/code-server
cat > ~/.config/code-server/config.yaml <<EOF
bind-addr: 0.0.0.0:$CODESERVER_PORT
auth: password
password: \${CODE_SERVER_PASSWORD:-changeme}
cert: false
EOF
sudo systemctl enable --now code-server@$USER
echo "code-server on :$CODESERVER_PORT"

# ── 4. ttyd (terminal in browser) ──────────────────────────────────────
log "ttyd"
if ! command -v ttyd >/dev/null 2>&1; then
  sudo apt-get install -y -qq ttyd 2>/dev/null || {
    # Build from release if not in apt
    TTYD_VER=$(curl -sf https://api.github.com/repos/tsl0922/ttyd/releases/latest | jq -r .tag_name)
    curl -fsSL "https://github.com/tsl0922/ttyd/releases/download/$TTYD_VER/ttyd.$(uname -m)" -o /tmp/ttyd
    sudo install /tmp/ttyd /usr/local/bin/ttyd
  }
fi
sudo tee /etc/systemd/system/ttyd.service >/dev/null <<UNIT
[Unit]
Description=ttyd - terminal in browser
After=network.target
[Service]
ExecStart=/usr/local/bin/ttyd -p $TTYD_PORT -W bash
Restart=on-failure
[Install]
WantedBy=multi-user.target
UNIT
sudo systemctl daemon-reload
sudo systemctl enable --now ttyd
echo "ttyd on :$TTYD_PORT"

# ── 5. DeepSeek harness (dsh) ──────────────────────────────────────────
log "DeepSeek harness"
DSH_DIR="$HOME/repos/novus-deepseek-harness"
if [ ! -d "$DSH_DIR" ]; then
  mkdir -p "$HOME/repos"
  git clone https://github.com/c10vis-poem/novus-deepseek-harness.git "$DSH_DIR"
fi
cd "$DSH_DIR"
git pull --ff-only origin main 2>/dev/null || true
pnpm install --frozen-lockfile 2>/dev/null || pnpm install
pnpm run build 2>/dev/null || echo "dsh build skipped (may need manual config)"

# dsh systemd service
sudo tee /etc/systemd/system/dsh.service >/dev/null <<UNIT
[Unit]
Description=DeepSeek Harness web UI
After=network.target
[Service]
WorkingDirectory=$DSH_DIR
ExecStart=$(which node) --max-old-space-size=4096 apps/web/dist/index.js --port $DSH_PORT --host 0.0.0.0
Environment="OPENROUTER_API_KEY=$OPENROUTER_KEY"
Environment="NODE_ENV=production"
Restart=on-failure
User=$USER
[Install]
WantedBy=multi-user.target
UNIT
sudo systemctl daemon-reload
sudo systemctl enable --now dsh
echo "dsh on :$DSH_PORT"

# ── 6. Idle auto-shutdown (60 min) ──────────────────────────────────────
log "Idle auto-shutdown"
sudo tee /usr/local/bin/idle-shutdown.sh >/dev/null <<'SCRIPT'
#!/bin/bash
# Shut down VM if no SSH sessions and no HTTP requests in 60 minutes.
# Runs every 10 minutes via cron.
IDLE_LIMIT=3600  # seconds

last_ssh=$(stat -c %Y /var/log/auth.log 2>/dev/null || echo 0)
last_http=$(stat -c %Y /var/log/nginx/access.log 2>/dev/null || echo 0)
last_api=$(stat -c %Y /tmp/.omniroute-last-request 2>/dev/null || echo 0)

now=$(date +%s)
latest=$(printf '%s\n' "$last_ssh" "$last_http" "$last_api" | sort -n | tail -1)
idle=$((now - latest))

if [ "$idle" -gt "$IDLE_LIMIT" ]; then
  logger "idle-shutdown: ${idle}s idle, shutting down"
  /sbin/shutdown -h now
fi
SCRIPT
sudo chmod +x /usr/local/bin/idle-shutdown.sh
(sudo crontab -l 2>/dev/null | grep -v idle-shutdown; echo "*/10 * * * * /usr/local/bin/idle-shutdown.sh") | sudo crontab -
echo "Auto-shutdown after 60min idle"

# ── 7. Firewall reminder ───────────────────────────────────────────────
log "Firewall"
cat <<MSG
Open these ports in GCP if not already:
  gcloud compute firewall-rules create allow-dev-services \\
    --allow tcp:$CODESERVER_PORT,tcp:$TTYD_PORT,tcp:$DSH_PORT \\
    --target-tags=omniroute-brain \\
    --description="Dev services for NovAExorpus"
MSG

# ── 8. Summary ──────────────────────────────────────────────────────────
log "Done"
cat <<SUMMARY
Services installed and enabled:

  OmniRoute          :20128  (was already running)
  Terrestrial Brain  :8000   (was already running)
  code-server        :$CODESERVER_PORT  NEW — VS Code in browser
  ttyd               :$TTYD_PORT  NEW — terminal in browser
  dsh                :$DSH_PORT  NEW — DeepSeek harness (OpenRouter)

Local inference (Qwen Coder) runs on phone via Qualcomm NPU.
DeepSeek runs via OpenRouter key through dsh on this VM.
VM auto-shuts down after 60 minutes idle.

Access from phone browser:
  VS Code:    http://34.31.112.77:$CODESERVER_PORT
  Terminal:   http://34.31.112.77:$TTYD_PORT
  dsh:        http://34.31.112.77:$DSH_PORT

Lifecycle:
  Start VM:  bash tools/vm-connect.sh up
  Stop VM:   bash tools/vm-connect.sh down
  Status:    bash tools/vm-connect.sh status
SUMMARY
