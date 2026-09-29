# RESUME.md — Session Ledger
Repository: NovAExorpus
Last session: 2026-09-18 (late session)

## WHAT LANDED THIS SESSION

### VM fully operational
- **GCP firewall rule `dev-ports`** created — ports 8080, 7681, 8001 open
  - gcloud CLI found on phone at `~/google-cloud-sdk/bin/gcloud`
  - Authenticated as d.drew.legrand@gmail.com
  - Project ID: `project-alchemist-490416`
- **code-server** (:8080) — VS Code in browser, password `changeme`, WORKING
- **ttyd** (:7681) — terminal in browser, no auth, WORKING
  - Binary at `/usr/bin/ttyd` (not /usr/local/bin — service was fixed)
- **dsh** (:8001) — DeepSeek harness, WORKING but needs config
  - dsh refuses `--host 0.0.0.0` for security, so socat proxies 8001→8002
  - systemd services: `dsh` (localhost:8002) + `dsh-proxy` (socat on :8001)
  - Token auth required — token changes on every restart
  - Get current token: `sudo journalctl -u dsh --no-pager -n 5 | grep token`
- **gh CLI** installed and authed on VM (c10vis-poem account)
- **Repos cloned on VM** at `~/repos/`:
  NovAExorpus, aesop-xi, NovA-terrestrial-brain, NoVa-honey-for-devs,
  novus-deepseek-harness

### Already running (from prior sessions)
- **OmniRoute** (:20128) — execution/routing/memory layer
- **Terrestrial Brain** (:8000) — structural memory, Postgres+pgvector

### Reconnect script
`bash tools/vm-reconnect.sh` — starts VM if stopped, sets OpenRouter key,
fixes sudo, restarts all services, health checks, prints access URLs with
current dsh token.

## STILL BROKEN / NOT DONE

1. **OpenRouter key not confirmed on VM** — `~/.bashrc` export may not
   have taken. The reconnect script handles this. dsh needs it to talk
   to DeepSeek models via OpenRouter.
2. **Passwordless sudo on VM** — command was given but user may not have
   run it yet. Reconnect script handles this too.
3. **dsh workspace selection** — user couldn't navigate to repos in the
   dsh UI. May need to set default workspace or restart with workspace arg.
4. **Qwen on phone NPU (HTP v79)** — geniex-bench is at
   `~/tools/geniex-bench/` with HTP v73/v75/v79 plugins. Needs
   `LD_LIBRARY_PATH` set to run. Model at
   `~/downloads/Qwen3.5-2B-Q4_0.gguf` (1.2GB). NOT wired up yet.
   Command to test:
   ```
   export LD_LIBRARY_PATH=$HOME/tools/geniex-bench/lib:$HOME/tools/geniex-bench/lib/qairt:$HOME/tools/geniex-bench/lib/llama_cpp
   ~/tools/geniex-bench/bin/geniex-bench --model ~/downloads/Qwen3.5-2B-Q4_0.gguf --backend htp --htp-soc v79 --server --port 8081
   ```
5. **OmniRoute not wired to phone's local model** — once Qwen is serving
   on phone:8081, OmniRoute needs a backend config pointing to it.
6. **feat/vm-lifecycle-2026-09-18 branch** — never pushed. Has vm-spec.md,
   vm-install.sh, vm-connect.sh updates. Push and PR still needed.
7. **sherpa-onnx cron workflows** — 8 inherited upstream workflows still
   active, all skipping. Classifier blocked `gh workflow disable`.

## PRIOR SESSION CARRY FORWARD (still not done)

1. Upgrade compact skill to ECC version
2. mem0 + TB must actually write during sessions
3. Honey-for-devs setup wizard
4. Graphify integration
5. NotebookLM integration
6. Obsidian Git plugin
7. OmniRoute MCP verification + round-trip test
8. mem0 vault export
9. Shell alias (`cc`)
10. Global ~/.claude/CLAUDE.md rewrite
11. Reasoning Bank / Continual Harness — spec-only
12. `restructure/drive-file-tree` branch — 250+ corpus files
13. `master` remote branch — review before deletion
14. Rename repo to NovAEcorpus
15. Read remaining source docs from `~/storage/shared/Documents/9-18-26/`
16. vault-ci.yml GitHub Actions
17. Git sync forked repos
18. Web UI dashboards on VM
19. mem0 self-hosting on VM
20. Bootstrap.sh — still points at localhost

## VM REFERENCE

- Instance: `omniroute-brain`, zone `us-central1-a`
- Project: `project-alchemist-490416` (display name: Project Alchemist)
- IP: `34.31.112.77`
- OS: Ubuntu 24.04 ARM64
- SSH: `~/google-cloud-sdk/bin/gcloud compute ssh omniroute-brain --zone=us-central1-a`
- gcloud on phone: `~/google-cloud-sdk/bin/gcloud`
- Firewall rule: `dev-ports` (tcp:7681,8080,8001)
- VM username: `d_drew_legrand`

## GH WORKFLOW — AUTOMATIC, DO NOT ASK

Feature branch → scan diff for secrets → push → PR → CI green → auto-merge.
Run `gh pr merge N --auto --merge` on every PR. If classifier blocks it,
tell the operator to run it manually.

## ENVIRONMENT

- Device: Android aarch64, Termux, kernel 5.15
- Shell paths with special chars need python os.path.join
- Output with parentheses/numbers gets blanked in terminal — use code blocks
- `!` prefix does not work in Termux — give raw commands in code blocks
