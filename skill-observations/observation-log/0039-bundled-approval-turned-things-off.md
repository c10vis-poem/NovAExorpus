---
id: 39
title: "A bundled 'all recommended' approval included turning off workflows the operator never meant to switch off"
status: open
type: open-source
skill: []
proposes_skill: []
target_file: ["~/.agents/AGENTS.md"]
siblings_checked: "none: target is the shared instructions file; related feedback memory never-turn-off-without-command"
area: "operator decision lists; approval scope"
date: 2026-10-23
session_context: "Pre-grill housekeeping. Decision 48 ('turn off the upstream automations in your forks') sat in a table with a 'yes' recommendation; operator answered 'All recommended'; a subagent disabled 11 workflows in 7 forks. Operator: 'nothing should be turned off in any of the repositories unless I fucking give the command.' Re-enabled the same day (reenable-workflows.sh, verified 0 disabled)."
parked_until:
resolved:
resolution:
reference: "~/.claude/session-work/2026-10-23/reenable-workflows.sh"
commands_verified: "run: gh api …/actions/workflows state check after re-enable → 0 disabled_manually"
---

**Issue:** A list of numbered decisions mixed harmless items with one that disabled things (workflows in forks). The operator approved the whole list with "all recommended" and did not realise one item switched things off. Separately, the operator noted advisor mode had once been switched off with no record of who did it.

**Suggested improvement:** A rule in the shared instructions: turning anything off (workflows, Actions, settings, plugins, hooks, modes) is never part of a bundled or recommended set; it is asked as its own question naming every repo and item. Barrier already added for the settings half: settings-guard.sh blocks agent writes to Claude Code settings (Aesop-Xi #77). Still missing: a rule or hook for disabling GitHub workflows/Actions via `gh api`.

**Principle:** A blanket approval covers only reversible, additive actions. Anything that switches something off is asked separately, by name, because the person approving a bundle reads the headline, not each consequence.
