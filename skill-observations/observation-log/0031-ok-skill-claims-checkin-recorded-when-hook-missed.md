---
id: 31
title: "/ok skill says 'the hook has recorded it' when the hook matched nothing; mid-prompt /ok and typos silently ignored"
status: open
type: internal
skill: [ok]
proposes_skill: []
target_file: ["~/.claude/hooks/enforce-prompt.sh", "~/repos/Aesop-Xi/hooks/enforce-prompt.sh"]
siblings_checked: "check-off family: ok, defer, reject share the same static 'recorded' text and the same parser; all three affected"
area: "operator check-in parsing and confirmation text"
date: 2026-10-18
session_context: "Session start check-in. Operator wrote '/ok -0' mid-sentence, then '/o 0'; neither created state/checkin-<sid>. The /ok skill's injected text still said the hook recorded it. Agent tried to spawn subagents and was blocked; operator was frustrated by the wait."
parked_until:
resolved:
resolution:
reference:
commands_verified: "run: ls ~/.claude/state/checkin-7cb1c8c0* -> no matches after both prompts"
---

**Issue:** `enforce-prompt.sh:18` only rewrites `/ok` at the start of the prompt; `#ok` anywhere. A mid-sentence `/ok -0` or a typo `/o 0` creates no check-in file, yet the `/ok` skill text claims "The hook has recorded it". The agent cannot tell from context whether check-in happened, and the operator gets no feedback that it failed.

**Suggested improvement:** (1) enforce-prompt.sh: accept `/ok` anywhere as a word, and print a one-line stdout result ("check-in recorded: items 0" or "no check-in mark found") so the context carries the real outcome. (2) ok/defer/reject skill text: drop the unconditional "recorded" claim; say "check state/checkin-<sid>".

**Principle:** A confirmation message must be produced by the component that did the work, from its actual result; static "done" text in a layer that did nothing is a false positive the agent will trust.
