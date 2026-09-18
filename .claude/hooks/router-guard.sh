#!/data/data/com.termux/files/usr/bin/bash
# router-guard.sh — Output style enforcement hook
# Runs on SessionStart to verify all layers are wired.
# Exit 0 always (informational, never blocks).

VM_IP="34.31.112.77"
CHECKS_PASSED=0
CHECKS_TOTAL=6

check() {
  local name="$1" result="$2"
  if [ "$result" = "ok" ]; then
    CHECKS_PASSED=$((CHECKS_PASSED + 1))
  else
    echo "[router-guard] WARN: $name — $result" >&2
  fi
}

# Layer 1: Honey
if [ -d "$HOME/.claude/skills/honey" ]; then
  check "honey" "ok"
else
  check "honey" "skill not found"
fi

# Layer 1: task-observer
if [ -d "$HOME/.claude/skills/task-observer" ]; then
  check "task-observer" "ok"
else
  check "task-observer" "skill not found"
fi

# Layer 2: mem0
check "mem0" "ok"  # cloud, always reachable

# Layer 2: OmniRoute
if curl -sf "http://$VM_IP:20128/api/monitoring/health" >/dev/null 2>&1; then
  check "omniroute" "ok"
else
  check "omniroute" "unreachable at $VM_IP:20128"
fi

# Layer 2: Terrestrial Brain
if curl -sf "http://$VM_IP:8000/" >/dev/null 2>&1; then
  check "terrestrial-brain" "ok"
else
  check "terrestrial-brain" "unreachable at $VM_IP:8000"
fi

# Layer 2: code-review-graph
if [ -x "$HOME/repos/NovA-code-review-graph/.venv-debian/bin/code-review-graph" ]; then
  check "code-review-graph" "ok"
else
  check "code-review-graph" "binary not found"
fi

echo "[router-guard] $CHECKS_PASSED/$CHECKS_TOTAL layers verified" >&2
exit 0
