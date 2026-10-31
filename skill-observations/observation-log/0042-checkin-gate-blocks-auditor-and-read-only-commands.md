---
id: 42
title: "checkin-gate blocks the Stop-hook auditor's StructuredOutput and read-only transcript queries as state changes"
status: open
type: internal
skill: []
proposes_skill: []
target_file: ["c10vis-poem/Aesop-Xi/hooks/checkin-gate.sh"]
siblings_checked: "none: target is a hook script, not a skill family member; related gates (stop-gate, enforce-gate) noted in body"
area: "hook gating before operator check-in"
date: 2026-10-23
session_context: "/wrapup of session 7cb1c8c0, run from session ac090dde before the operator had checked in"
parked_until:
resolved:
resolution:
reference: "~/.claude/state friction events 2026-10-23 14:04-14:22 (observe-dismiss list): about 35 StructuredOutput blocks and 4 Bash blocks by checkin-gate"
commands_verified: "run: observe-dismiss list showed the StructuredOutput and Bash blocks by checkin-gate"
---

**Issue:** Before the operator checked in, checkin-gate.sh blocked calls that change nothing. (1) The `type: agent` Stop-hook auditor's StructuredOutput calls, several per turn from 14:04 on, so the auditor could never return its verdict. (2) Read-only Bash (jq and grep over session transcripts), apparently matched on words such as `rm -`, `mv`, `delete` or `tar` inside grep patterns and jq strings. Each block becomes a friction event that stop-gate then requires the agent to clear, so every turn ended with a new batch. That also pushed the agent toward dismissing events itself, which the operator called bypassing and told it to stop.

**Suggested improvement:** In checkin-gate.sh: always allow StructuredOutput and any call from inside a hook agent; judge Bash by the commands that run, not by substrings in quoted arguments, or allow the read-only binaries (jq, grep, cat, ls, stat, find without -delete/-exec) when there is no `>` redirection. Do not raise a friction event for an auditor tool call. Add a test per case. Also: `/ok 1-4` recorded only item 1; either parse ranges or say so in the CHECK-IN line.

**Principle:** A gate that stops writes has to judge the action, not the text. Quoted search patterns and a hook's own reporting tool are not state changes; blocking them blinds the agent and the auditor and protects nothing, and a gate that raises events nobody can clear invites the agent to clear them itself.

**Recurrence 2026-10-28 (session 6a9c6cdb):** the phone ran the old checkin-gate (live copies in ~/.claude/hooks were plain copies; merges never reached them). It blocked about 60 StructuredOutput calls from the Stop auditor, an AskUserQuestion card, a Drive search and observe-dismiss calls whose text held `!` or `#`. Each block made a friction event the stop gate required clearing, so every turn end restarted the loop; only a literal `#ok` typed by the operator broke it (spoken "okay, skip, enforce" did not). Fix shipped: Aesop-Xi PR #81 merged (c933648); ~/.claude/hooks/*.sh and lib/ are now symlinks into ~/repos/Aesop-Xi/hooks, so a pull updates them. Still open: stop gate counting gate-block events, git-gate needing the exact "push now", ship-session not picking up PRs from earlier sessions.
