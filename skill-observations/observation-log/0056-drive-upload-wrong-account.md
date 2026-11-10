---
id: 56
title: "Drive upload went to a saved remote on another account; drive-find's account map goes stale when the login changes"
status: open
type: open-source
skill: [drive-find]
proposes_skill: []
target_file: []
siblings_checked: "no family registry; checked — instance-specific to drive-find, no propagation"
area: "account routing for Drive writes"
date: 2026-11-05
session_context: "Operator asked whether a document could be found in their Drive; the agent uploaded it through a saved rclone remote without checking which account that remote belongs to."
parked_until:
resolved:
resolution:
reference:
commands_verified: "run: Drive connector list_recent_files showed the signed-in account as owner, while drive-find names a different account for that connector"
---

**Issue:** The operator meant the Drive of the account they were signed in to. The agent used a saved rclone remote because it was the easiest way to send the bytes, and that remote belongs to their other account. drive-find also maps the Drive connector to a fixed account, but the connector follows the current login.

**Suggested improvement:** In drive-find, replace the fixed mapping: the connector follows the signed-in account, so confirm its account from a file owner before use, and treat rclone remotes as separate logins. Before any Drive write, name the target account and check it matches the one the operator means.

**Principle:** A saved credential that works says nothing about whether it is the account the user meant. Check the target account before writing.
