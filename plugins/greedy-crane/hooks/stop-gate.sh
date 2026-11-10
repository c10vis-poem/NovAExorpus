#!/usr/bin/env sh
# SubagentStop for corpus-ingest workers. The write-to-task checks (progress file, skipped steps, stale file,
# tools or skills that failed to load) come from aesops-enforcements' subagent-stop-gate, loaded at the root.
# This adds the worker's own check: every file in its assigned paths list was opened (worker_stop_check.py).
# Fails open. Off: touch ~/.claude/state/off/greedy-crane.stop-gate.
R="${CLAUDE_PLUGIN_ROOT:-$(cd "$(dirname "$0")/.." && pwd)}"
sh "$R/scripts/killswitch.sh" greedy-crane stop-gate && exit 0
in=$(cat)
printf '%s' "$in" | python3 "$R/scripts/worker_stop_check.py"; rc=$?
[ "$rc" = 2 ] && exit 2
exit 0
