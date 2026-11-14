---
id: 63
title: "Standing order to spawn agents plus 'read in full' prompts burned over a million tokens in an hour with no cost check"
status: open
type: open-source
skill: [task-observer]
proposes_skill: []
target_file: ["~/.claude/CLAUDE.md", "~/repos/Aesop-Xi/hooks/agent-type-gate.sh"]
siblings_checked: "no family registry; checked, applies to any agent launch; principle 16 (validate cheaply before spending heavily) is related"
area: "subagent spawning; token budget"
date: 2026-11-06
session_context: "Asked to get agents to find out what was going on; the agent launched three full-read jobs over documents already summarized the session before, one an audit nobody asked for."
parked_until:
resolved:
resolution:
reference:
commands_verified: none
---

**Issue:** The agent never checked whether existing write-ups already answered the question, set no scope or token limit, and gave no cost before launching. Six agents used about 1.16M tokens. A standing instruction to spawn unasked made this the default path. Earlier text rules on reading and on approval did not prevent it.

**Suggested improvement:** Barrier in the hook rewrite: a PreToolUse gate on Agent that refuses a prompt with no explicit file list or containing full-read wording unless the operator's current prompt asks for agents. Set a low maxTurns on read-only agent definitions. Narrow the standing order to work the operator asked to delegate.

**Principle:** Delegation multiplies cost invisibly; a launch needs a bounded scope and a stated cost before it runs.
