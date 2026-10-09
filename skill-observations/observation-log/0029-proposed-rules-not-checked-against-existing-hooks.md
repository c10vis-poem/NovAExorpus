---
id: 29
title: "Subagent/review output relayed without checking the operator's existing setup (hooks, forks, rules)"
status: open
type: open-source
skill: [task-observer]
proposes_skill: []
target_file: ["~/repos/aesop-xi/hooks/README.md"]
siblings_checked: "none: task-observer belongs to no registered family (no skill-families.md)"
area: "Weekly review staging; relaying subagent results"
date: 2026-10-08
session_context: "Observation review dispatched to a subagent; its staged CLAUDE.md additions were presented to the operator"
parked_until:
resolved:
resolution:
reference: "skill-updates/2026-10-08/claude-md/CLAUDE.md.additions.md; aesop-xi hooks/README.md"
commands_verified: none
---

**Issue:** The weekly review (run by a subagent) staged five "new rules" for CLAUDE.md. The agent relayed them to the operator as new, including a GitHub-workflow rule, without first checking them against the operator's enforcement hooks (H1-H7: branch-current-gate, sync-on-use, gitleaks, git-gate, ship-session PR + auto-merge + branch delete), which it had been blocked by all session. The operator had to point out the hooks already existed. Only one real gap remained (no CI / required-checks check), which became H8.

**More instances, same session:** (2) the review called task-observer and honey "foreign-maintained"; both are the operator's forks. (3) a reader report's `convert_raw_to_markdown.py` / `generate_jsonl_markers.py` were relayed as "duplicates of clean.py / build_rag_chunks.py", against the operator's own rule that no tool's output is checked by the same tool (the second set is the cross-check). (4) a PENDING line ("move qairt_ out") was handed to a subagent without checking qairt_ is referenced by NPU-ON-DEVICE.md. Each was caught by the operator, not the agent.

**Suggested improvement:** In the weekly review procedure (Step: proposing fixes), require a mapping of every proposed rule to the existing enforcement layer (hooks README, settings.json hooks) with a verdict per rule: already enforced (cite the hook), partly (name the gap), or new. Text additions are only proposed for rules no hook can check. The relaying agent re-checks that mapping before presenting.

**Principle:** Before proposing a rule, check the enforcement layer that already exists; a proposal that duplicates a working mechanism costs the operator's trust and attention, and the real gap hides inside the duplicate.
