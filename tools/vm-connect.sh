#!/data/data/com.termux/files/usr/bin/bash
# vm-connect.sh — connect to or manage services on the GCP VM
#
# Usage:
#   bash tools/vm-connect.sh status       — check all services
#   bash tools/vm-connect.sh ssh          — SSH into the VM
#   bash tools/vm-connect.sh open <svc>   — open a service in the browser
#   bash tools/vm-connect.sh start <svc>  — start a service on the VM (via SSH)

set -euo pipefail

VM_IP="34.31.112.77"

declare -A PORTS=(
  [omniroute]=20128
  [tb]=8000
  [code-server]=8080
  [ttyd]=7681
  [novnc]=3000
  [jupyter]=8888
  [ollama]=11434
  [dsh]=8001
)

declare -A HEALTH=(
  [omniroute]="/api/monitoring/health"
  [tb]="/"
)

cmd_status() {
  echo "=== VM Service Status ($VM_IP) ==="
  for svc in omniroute tb code-server ttyd novnc jupyter ollama dsh; do
    port="${PORTS[$svc]}"
    if curl -sf --connect-timeout 3 "http://$VM_IP:$port${HEALTH[$svc]:-/}" >/dev/null 2>&1; then
      echo "  $svc :$port  UP"
    else
      echo "  $svc :$port  DOWN"
    fi
  done
}

cmd_ssh() {
  if command -v gcloud >/dev/null 2>&1; then
    exec gcloud compute ssh novae-vm --zone=us-central1-a -- "$@"
  else
    exec ssh "user@$VM_IP" "$@"
  fi
}

cmd_open() {
  local svc="${1:?Usage: vm-connect.sh open <service>}"
  local port="${PORTS[$svc]:-}"
  [ -z "$port" ] && { echo "Unknown service: $svc"; echo "Known: ${!PORTS[*]}"; exit 1; }
  local url="http://$VM_IP:$port"
  [ "$svc" = "novnc" ] && url="$url/vnc.html"
  echo "Opening $svc at $url"
  termux-open-url "$url" 2>/dev/null || xdg-open "$url" 2>/dev/null || echo "Open manually: $url"
}

cmd_start() {
  local svc="${1:?Usage: vm-connect.sh start <service>}"
  case "$svc" in
    ttyd)
      cmd_ssh "nohup ttyd -p 7681 -W bash > /tmp/ttyd.log 2>&1 &"
      echo "ttyd started on :7681"
      ;;
    code-server)
      cmd_ssh "nohup code-server --bind-addr 0.0.0.0:8080 > /tmp/code-server.log 2>&1 &"
      echo "code-server started on :8080"
      ;;
    novnc)
      cmd_ssh "bash -c 'Xvfb :1 -screen 0 1920x1080x24 & x11vnc -display :1 -nopw -listen 0.0.0.0 -forever & websockify --web /usr/share/novnc 3000 localhost:5900 &'"
      echo "noVNC started on :3000"
      ;;
    ollama)
      cmd_ssh "nohup env OLLAMA_HOST=0.0.0.0:11434 ollama serve > /tmp/ollama.log 2>&1 &"
      echo "ollama started on :11434"
      ;;
    dsh)
      cmd_ssh "cd ~/repos/novus-deepseek-harness && nohup npm start -- --port 8001 --host 0.0.0.0 > /tmp/dsh.log 2>&1 &"
      echo "dsh started on :8001"
      ;;
    *)
      echo "Can't auto-start: $svc (use 'omniroute' and 'tb' are managed by systemd)"
      ;;
  esac
}

case "${1:-status}" in
  status) cmd_status ;;
  ssh)    shift; cmd_ssh "$@" ;;
  open)   shift; cmd_open "$@" ;;
  start)  shift; cmd_start "$@" ;;
  *)      echo "Usage: vm-connect.sh {status|ssh|open <svc>|start <svc>}"; exit 1 ;;
esac
