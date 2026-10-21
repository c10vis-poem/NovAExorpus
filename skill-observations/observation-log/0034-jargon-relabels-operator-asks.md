---
id: 34
title: "Agent replaced the operator's terms with its own (stop gate, same-path, heredoc; Jev guessed as GEPA)"
status: open
type: open-source
skill: [task-observer]
proposes_skill: []
target_file: ["~/.claude/CLAUDE.md"]
siblings_checked: "none: target is the global instructions file; task-observer listed only as the logger, no family"
area: "operator-facing explanations and questions"
date: 2026-10-21
session_context: "Pre-grill housekeeping: Drive dedup report and hook fixes, operator dictating by voice"
parked_until:
resolved:
resolution:
reference:
commands_verified: none
---

**Issue:** The operator asked that subagents get the same stop hooks as the main agent. The agent turned this into its own term ("SubagentStop gate") and then asked "build the subagent stop gate?" as if it were a new proposal. The operator replied: "I didn't say anything about Stop gate." Over the same stretch the agent used "365 same-path files" and "heredoc" without defining either. Both came back as questions in the following turn ("Still haven't told me what the same file path is", "What the hell is a heredoc").

**Suggested improvement:** Add a rule to the CLAUDE.md behavioral constraints. When restating an operator ask, quote their words first. Define any internal or technical term in one plain sentence the first time it reaches the operator. A question about the operator's own request should confirm it ("you asked X; I'll do it by Y"), not re-propose it under a new name.

**Principle:** Labels coined during the work are the agent's private shorthand. When they appear in a question to the user, the user can't tell their own request from a new proposal, so they have to spend another round just decoding the terms.

**Second instance (2026-10-21, event e16292):** The operator named "JEV" as the compiler for the metaprompt layer. The agent didn't know the name and swapped in its own guess (GEPA/DSPy), explaining that instead. The operator: "No I literally mean Jeff", then "Jev". Jev (TypeSafe's System One model) was in the operator's own notes (`tr1v3r/dsh-jev`, 2026-10-01 repo inventory). A search of local notes before answering would have found it. Same shape as above: an unknown operator term was replaced by the agent's own term.
