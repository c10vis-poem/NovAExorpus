---
id: 37
title: "Check-in parser fix (obs 0031) read numbered-reply list labels as item approvals; its report line showed stale marks"
status: actioned
type: internal
skill: [ok]
proposes_skill: []
target_file: ["~/repos/Aesop-Xi/hooks/enforce-prompt.sh", "~/.claude/hooks/enforce-prompt.sh"]
siblings_checked: "check-off family: ok, defer, reject share the one parser; all three covered by the same fix"
area: "operator check-in parsing"
date: 2026-10-23
session_context: "Operator answered a 34-item numbered list with lines like '16. /ok 17. Is there...'; the hook recorded RESUME items 17 and 26 and printed 'CHECK-IN recorded: 3=accepted 4=accepted 5=accepted 17=accepted 26=accepted'"
parked_until:
resolved: 2026-10-23
resolution: "Aesop-Xi PR #67 (fix/checkin-list-labels): numbers followed by '.' are skipped as list labels, numbers not in START HERE are refused with a message, and the CHECK-IN line shows only this prompt's marks. checkin.test.sh 11/11. Live install by operator copy."
reference:
commands_verified: "run: bash hooks/tests/checkin.test.sh -> 11 passed, 0 failed"
---

**Issue:** The obs 0031 fix made `/ok` count anywhere in a prompt. Its tests covered single marks only. A numbered operator reply ("16. /ok 17. Is there a reason...") put the next line's list label right after `/ok`, so the hook recorded item 17 (and 26). The CHECK-IN line printed `tail -5` of the whole session log, so earlier marks (3, 4, 5) looked like new ones, which confused the operator.

**Suggested improvement:** Done in PR #67. Tests for parsers of operator input should include the operator's real reply shapes (numbered lists, voice-dictated run-ons), not just the canonical form.

**Principle:** When loosening a parser to accept marks anywhere, test it against the user's actual message shapes, and make any confirmation line report only what this input changed.
