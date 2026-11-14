#!/usr/bin/env sh
# PostToolUse(Read): flag injection-looking files as DATA. Never blocks, fails open.
R="${CLAUDE_PLUGIN_ROOT:-$(cd "$(dirname "$0")/.." && pwd)}"
# Wired in ~/.claude/settings.json via ~/.claude/hooks/greedy-crane-gate.sh (operator 2026-11-08): the plugin copy steps aside.
[ -z "${GREEDY_FROM_SETTINGS:-}" ] && grep -q greedy-crane-gate.sh "$HOME/.claude/settings.json" 2>/dev/null && exit 0
sh "$R/scripts/killswitch.sh" greedy-crane quarantine && exit 0
exec python3 "$R/scripts/wa_quarantine.py" --hook 2>/dev/null || exit 0
