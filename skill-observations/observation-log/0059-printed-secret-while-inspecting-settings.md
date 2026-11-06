---
id: 59
title: "Printed a settings file's env block and exposed a real API key in the transcript"
status: open
type: open-source
skill: []
proposes_skill: []
target_file: ["c10vis-poem/Aesop-Xi/hooks/secret-guard.sh"]
siblings_checked: "none: target is a hook; principle 14 (inspection must not leak secrets) already covers it"
area: "reading config files"
date: 2026-11-05
session_context: "Changing the model setting; the agent printed the first lines of settings.json."
parked_until:
resolved:
resolution:
reference:
commands_verified: "run: sed of settings.json lines 1-8 showed the value; hooks were stubs, so no guard fired"
---

**Issue:** The agent ran a plain sed over settings.json to find the env block, which printed an API key value into the transcript. The secret guard was a stub at the time.

**Suggested improvement:** Read config files through a masking filter, and install the secret guard so a print of a known secret-bearing file is blocked.

**Principle:** Inspect structure, not values: list key names when a file can hold secrets.
