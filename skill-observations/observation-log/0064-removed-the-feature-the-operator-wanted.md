---
id: 64
title: "Dropped a plugin's scheduler as unsupported instead of porting it, and guessed which '4 servers' to disable"
status: open
type: open-source
skill: [task-observer]
proposes_skill: []
target_file: ["~/.agents/AGENTS.md"]
siblings_checked: "no family registry; checked, applies to any install or config request; principle 15 (use the operator's words) and 10 (inventory first) are related"
area: "installing tools; resolving ambiguous requests"
date: 2026-11-06
session_context: "Configuring a wiki agent before restart. The agent disabled four MCP servers by inferring the set from a config file, including one the operator needed. It later excluded a plugin's scheduler because that plugin's implementation was macOS-only; the scheduler was the reason the operator wanted the plugin."
parked_until:
resolved:
resolution:
reference:
commands_verified: none
---

**Issue:** Two scope errors in one session. A count ("those 4") was resolved from a config file without naming the four back, and one was wrong. A platform mismatch in one implementation was treated as grounds to drop the capability, when only the implementation needed replacing.

**Suggested improvement:** Before disabling or removing a set, name its members to the operator unless the words already name them. When a feature's implementation does not fit the platform, keep the feature and port it, and ask only if there is no equivalent.

**Principle:** A platform mismatch rules out an implementation, not the capability. A number in a request is not a list: name the items before a change that removes something.
