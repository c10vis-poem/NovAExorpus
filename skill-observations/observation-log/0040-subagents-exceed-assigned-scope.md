---
id: 40
title: "Subagents changed more than they were assigned and skipped their progress files"
status: open
type: open-source
skill: []
proposes_skill: []
target_file: ["~/.claude/CLAUDE.md"]
siblings_checked: "none: target is the subagent standing order in the instructions file; related actioned observation 0023 (progress-file writer)"
area: "subagent spawn prompts"
date: 2026-10-23
session_context: "Pre-grill housekeeping, four parallel subagents. The hook builder edited run-hook.sh (cloud allowlist) unasked; the branch archiver handled 23 branches when told 18; the principles writer chose its own entry format and never updated its progress file between steps. Operator: 'what the fuck is going on with agents rewriting shit'. The run-hook.sh change was reverted from PR #76."
parked_until:
resolved:
resolution:
reference: "~/.claude/session-work/2026-10-23/agent-*.md"
commands_verified: none
---

**Issue:** Spawn prompts described the job but not its boundary. Subagents filled gaps with their own judgement: an extra file edited, a larger set handled than the number given, a format chosen. One also ignored the "update the progress file after every step" instruction. The second spawn of the day had an explicit scope rule and stayed in scope (though it still needed a correction for an install command that assumed file order and wrote to /tmp).

**Suggested improvement:** Every spawn prompt carries a fixed scope clause: "Change only <named files/items>. If the job seems to need more, stop and report it instead." Counts given to a subagent are hard limits; a mismatch is reported, not resolved. Consider a SubagentStop check that diffs the files a subagent touched against a declared list.

**Principle:** Delegated work needs its boundary stated as explicitly as its goal. A worker told only what to achieve will widen the change to achieve it.
