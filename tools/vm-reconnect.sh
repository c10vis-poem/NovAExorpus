#!/data/data/com.termux/files/usr/bin/bash
# vm-reconnect.sh — Reconnect and fix all VM services from phone
# Run: bash ~/repos/NovAExorpus/tools/vm-reconnect.sh
set -euo pipefail

GCLOUD="$HOME/google-cloud-sdk/bin/gcloud"
VM="omniroute-brain"
ZONE="us-central1-a"
IP="34.31.112.77"

log() { printf '\n=== %s ===\n' "$1"; }

ssh_cmd() { "$GCLOUD" compute ssh "$VM" --zone="$ZONE" --command="$1" 2>&1; }

# ── 0. Check gcloud auth ──
log "Auth check"
"$GCLOUD" auth list 2>&1 | grep -q ACTIVE && echo "gcloud: authed" || { echo "ERROR: run gcloud auth login"; exit 1; }

# ── 1. Start VM if stopped ──
log "VM status"
STATE=$("$GCLOUD" compute instances describe "$VM" --zone="$ZONE" --format="get(status)" 2>&1)
echo "VM state: $STATE"
if [ "$STATE" != "RUNNING" ]; then
  echo "Starting VM..."
  "$GCLOUD" compute instances start "$VM" --zone="$ZONE" --quiet
  echo "Waiting 30s for boot..."
  sleep 30
fi

# ── 2. Set OpenRouter key ──
log "OpenRouter key"
if [ -f "$HOME/.openwiki/.env" ]; then
  KEY=$(grep -o 'sk-or-v1-[a-zA-Z0-9_-]*' "$HOME/.openwiki/.env")
  ssh_cmd "grep -q OPENROUTER_API_KEY ~/.bashrc 2>/dev/null && echo 'key already set' || { echo 'export OPENROUTER_API_KEY=\"$KEY\"' >> ~/.bashrc && echo 'key added'; }"
else
  echo "WARN: ~/.openwiki/.env not found, skipping key"
fi

# ── 3. Fix passwordless sudo ──
log "Sudo fix"
ssh_cmd "[ -f /etc/sudoers.d/d_drew_legrand ] && echo 'sudo already fixed' || { echo 'd_drew_legrand ALL=(ALL) NOPASSWD:ALL' | sudo tee /etc/sudoers.d/d_drew_legrand >/dev/null && sudo chmod 440 /etc/sudoers.d/d_drew_legrand && echo 'sudo fixed'; }"

# ── 4. Restart all services ──
log "Services"
ssh_cmd "
sudo systemctl restart ttyd 2>/dev/null; sudo systemctl is-active ttyd && echo 'ttyd: UP' || echo 'ttyd: DOWN'
sudo systemctl restart dsh 2>/dev/null; sudo systemctl is-active dsh && echo 'dsh: UP' || echo 'dsh: DOWN'
sudo systemctl restart dsh-proxy 2>/dev/null; sudo systemctl is-active dsh-proxy && echo 'dsh-proxy: UP' || echo 'dsh-proxy: DOWN'
sudo systemctl is-active code-server@d_drew_legrand && echo 'code-server: UP' || echo 'code-server: DOWN'
sudo systemctl is-active omniroute && echo 'omniroute: UP' || echo 'omniroute: DOWN (check manually)'
echo '---'
# Get dsh token
sudo journalctl -u dsh --no-pager -n 5 2>/dev/null | grep -o 'token=[^ ]*' | tail -1
"

# ── 5. Health checks ──
log "Health checks"
for svc in "code-server:8080" "ttyd:7681" "dsh:8001" "omniroute:20128" "tb:8000"; do
  name="${svc%%:*}"
  port="${svc##*:}"
  if curl -sf --connect-timeout 3 "http://$IP:$port" >/dev/null 2>&1; then
    echo "  $name :$port  UP"
  else
    echo "  $name :$port  DOWN"
  fi
done

# ── 6. Print access URLs ──
log "Access URLs"
TOKEN=$(ssh_cmd "sudo journalctl -u dsh --no-pager -n 10 2>/dev/null | grep -o 'token=[^ ]*' | tail -1" 2>/dev/null | tr -d '\n')
echo "  VS Code:    http://$IP:8080  (password: changeme)"
echo "  Terminal:   http://$IP:7681"
echo "  dsh:        http://$IP:8001/?$TOKEN"
echo "  OmniRoute:  http://$IP:20128"
echo "  TB:         http://$IP:8000"
echo ""
echo "Repos on VM: ~/repos/{NovAExorpus,aesop-xi,NovA-terrestrial-brain,NoVa-honey-for-devs,novus-deepseek-harness}"
