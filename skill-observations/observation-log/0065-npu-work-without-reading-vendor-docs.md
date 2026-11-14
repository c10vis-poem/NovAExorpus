---
id: 65
title: "Runtime work reasoned from memory instead of the vendor docs the operator keeps on hand"
status: open
type: open-source
skill: [termux-helper]
proposes_skill: []
target_file: ["~/.agents/AGENTS.md"]
siblings_checked: "no family registry; aesop-voice-pipeline and android-termux-operator touch the same runtimes but neither was read for a vendor-doc rule, so assumed; principle 3 and 10 are related"
area: "on-device runtimes; reading vendor documentation"
date: 2026-11-06
session_context: "Planning an embedding runtime on the phone. The operator said earlier NPU attempts failed because agents would not read the vendor documentation library. In this session the agent proposed a runtime on the strength of it being installed, before checking the operator's runtime notes."
parked_until:
resolved:
resolution:
reference:
commands_verified: none
---

**Issue:** Agents working on fast-moving runtimes answer from memory or from what happens to be installed, while a vendor documentation library sits on the device. The operator reports this as the cause of repeated failures.

**Suggested improvement:** Add to the shared instructions: before any claim, plan or code about a vendor runtime, read the vendor doc and cite file and line. A written rule has not held, so consider a structural check.

**Principle:** For tools newer than training data, the vendor's documentation is the only valid source. If the docs are on hand, not reading them is the failure.
