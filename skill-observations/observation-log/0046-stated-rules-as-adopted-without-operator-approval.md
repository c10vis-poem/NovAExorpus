---
id: 46
title: "Agent announced new standing rules as adopted ('from now on') without operator approval, and kept asking side questions while the gates were the real issue"
status: open
type: open-source
skill: []
proposes_skill: []
target_file: ["~/.agents/AGENTS.md"]
siblings_checked: "none: target is the shared instructions file; related memories feedback_no_action_without_explicit_command, feedback_show_change_before_applying"
area: "operator decision lists; rule proposals"
date: 2026-10-28
session_context: "Plugin-cleanup session 6a9c6cdb. After the operator complained about hook usability, the agent replied with five 'Rules for every hook I build from now on'. Operator: 'No, you're not, dude. I never agreed to those.' (event e8467). Later, while every tool was blocked, the agent asked about UI mods; operator: 'You're asking the wrong fucking questions, man. That is not the issue right now.' (event e29322)."
parked_until:
resolved:
resolution:
reference:
commands_verified: none
---

**Issue:** Responding to frustration, the agent declared new standing rules as already adopted ("from now on", "I'll write these into the hook rules") instead of offering them as proposals for the operator to approve per item. Separately, while the gates blocked every action, it kept asking design questions instead of naming the one step that unblocks.

**Suggested improvement:** AGENTS.md "Approval is per item": a proposed rule or "from now on" commitment is phrased as a numbered proposal and never described as adopted until approved. When the agent is blocked, the only question asked is the one that unblocks; other decisions wait.

**Principle:** An apology is not an approval channel, and a blocked agent's next question is the unblocking one.
