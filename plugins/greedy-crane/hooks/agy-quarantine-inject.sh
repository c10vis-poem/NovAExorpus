#!/usr/bin/env sh
# AGY PreInvocation: inject queued quarantine notices once (AGY PostToolUse cannot return context).
R="$(cd "$(dirname "$0")/.." && pwd)"
sh "$R/scripts/killswitch.sh" greedy-crane quarantine && { echo '{}'; exit 0; }
python3 "$R/scripts/wa_quarantine.py" --agy-inject 2>/dev/null || echo '{}'
