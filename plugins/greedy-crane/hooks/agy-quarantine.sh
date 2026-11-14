#!/usr/bin/env sh
# AGY PostToolUse(read_file|view_file): queue a quarantine notice. Same scanner as Claude's quarantine.sh.
# AGY runs hooks in the plugin folder. Never blocks, fails open. Off: see killswitch.sh.
R="$(cd "$(dirname "$0")/.." && pwd)"
sh "$R/scripts/killswitch.sh" greedy-crane quarantine && { echo '{}'; exit 0; }
python3 "$R/scripts/wa_quarantine.py" --hook 2>/dev/null || echo '{}'
