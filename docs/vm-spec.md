# GCP VM Spec — 34.31.112.77

## What this is

A GCP Compute Engine instance that hosts infrastructure services for the
NovAExorpus pipeline. Any agent working in any repo needs to know this
VM exists and what it runs.

## Running services

| Service | Port | Protocol | Status |
|---------|------|----------|--------|
| OmniRoute (AI gateway) | 20128 | HTTP | Production — execution/routing/memory-retrieval layer |
| Terrestrial Brain (MCP) | 8000 | HTTP | Production — structural memory, Postgres+pgvector |
| Postgres (pgvector) | 5432 | TCP | Internal only — TB backend, not exposed |

Health check: `curl -sf http://34.31.112.77:20128/api/monitoring/health`

## Planned services (install via `tools/vm-install.sh`)

| Port | Service | Purpose |
|------|---------|---------|
| 8080 | code-server | VS Code in browser — full IDE from phone |
| 7681 | ttyd | Terminal in browser — shell access from any device |
| 8001 | dsh | DeepSeek harness — cloud inference via OpenRouter |

## Architecture split

- **Phone (Snapdragon NPU)** — local model inference via QAIR/T + HTP
  SDK + GenieX. Qwen Coder and other models run on-device weights.
- **VM (GCP)** — cloud dev environment (code-server, dsh), infrastructure
  services (OmniRoute, TB), and DeepSeek via OpenRouter.
- **OmniRoute** — bridges both. Phone agents hit OmniRoute for routing,
  memory retrieval, and cloud model calls.

## VM lifecycle

Auto-shutdown after 60 minutes idle (cron on VM). Start/stop from phone:
```bash
bash tools/vm-connect.sh up     # start VM, wait for health
bash tools/vm-connect.sh down   # stop VM (no compute charges)
bash tools/vm-connect.sh status # check all services
```
Requires gcloud CLI on the phone (`pip install google-cloud-sdk`).

## Access patterns

### From this phone (Termux)
```bash
# SSH (requires gcloud auth or SSH key)
gcloud compute ssh omniroute-brain --zone=us-central1-a

# Or direct SSH if key is configured
ssh user@34.31.112.77
```

### From any browser
Once a service is running on an open port:
```
http://34.31.112.77:<port>
```

### From Claude Code / agents
Via MCP entries in `.mcp.json` (env vars for URL + auth key).

## Deployment capabilities

### 1. Terminal in browser (ttyd)
WebSocket-based terminal. Gives a full Linux shell from any browser.
```bash
# On VM:
apt install ttyd
ttyd -p 7681 -W bash
```
Access: `http://34.31.112.77:7681`

### 2. VS Code in browser (code-server)
Full VS Code IDE accessible from any browser including the phone.
```bash
# On VM:
curl -fsSL https://code-server.dev/install.sh | sh
code-server --bind-addr 0.0.0.0:8080 --auth password
```
Access: `http://34.31.112.77:8080`

### 3. Desktop in browser (noVNC)
Full Linux desktop over WebSocket, viewable in any browser.
```bash
# On VM:
apt install xvfb x11vnc novnc
Xvfb :1 -screen 0 1920x1080x24 &
x11vnc -display :1 -nopw -listen 0.0.0.0 -forever &
websockify --web /usr/share/novnc 3000 localhost:5900
```
Access: `http://34.31.112.77:3000/vnc.html`

### 4. Large model hosting (ollama)
Run large models (70B+) that won't fit on the phone.
```bash
# On VM:
curl -fsSL https://ollama.com/install.sh | sh
OLLAMA_HOST=0.0.0.0:11434 ollama serve
ollama pull deepseek-coder-v2:236b
```
Access: `http://34.31.112.77:11434` (OpenAI-compatible API)
OmniRoute can proxy this as a model backend.

### 5. DeepSeek harness (dsh)
Web-based harness for DeepSeek models.
```bash
# On VM:
cd ~/repos/novus-deepseek-harness
npm start -- --port 8001 --host 0.0.0.0
```
Access: `http://34.31.112.77:8001`

### 6. Debian proot (hosted Linux environment)
Full Debian environment with no containerization overhead.
```bash
# On VM (if needed for compatibility):
apt install proot debootstrap
debootstrap stable ~/debian
proot -S ~/debian
```
For most use cases the VM is already a full Linux host — proot is only
needed if you want an isolated Debian inside it.

## Security

- All exposed ports MUST be behind GCP firewall rules.
- Services with auth (code-server password, OmniRoute Bearer token, TB
  x-brain-key) are required — never expose unauthenticated.
- Secrets live in `$PREFIX/etc/secrets.env` on the phone and in systemd
  unit environment files on the VM. Never in git.
- SSH keys or gcloud IAM for shell access — no password auth.

## Firewall rules (GCP)

Current open:
```
tcp:20128  — OmniRoute
tcp:8000   — Terrestrial Brain
```

To open a new port:
```bash
gcloud compute firewall-rules create allow-<service> \
  --allow tcp:<port> \
  --target-tags=omniroute-brain \
  --source-ranges=0.0.0.0/0 \
  --description="<service> for NovAExorpus"
```

Replace `0.0.0.0/0` with your IP range for restricted access.

## VM specs

- **Project**: Project Alchemist
- **Zone**: us-central1-a (verify with `gcloud compute instances list`)
- **OS**: Debian or Ubuntu (verify with `cat /etc/os-release` on VM)
- **Managed by**: systemd units for OmniRoute and TB

## For agents reading this

1. OmniRoute at `:20128` is always your first contact point — it routes
   completions, retrieves memory, and orchestrates via Continual Harness
   and Reasoning Bank.
2. TB at `:8000` is structural memory — long-term facts, preferences,
   constraints. Auth via `x-brain-key` header.
3. Don't open new ports or install services without operator approval.
4. If a service is down, report the exact error — don't silently fall back.
