---
id: 67
title: "Session documents again presented a generic GPU/CPU runtime as an NPU route, despite a written memory rule against it"
status: open
type: open-source
skill: [termux-helper]
proposes_skill: []
target_file: ["~/.agents/AGENTS.md"]
siblings_checked: "no family registry; aesop-voice-pipeline and android-termux-operator touch the same runtimes, assumed applicable, not added: termux-helper Part 2 is the NPU section"
area: "on-device NPU runtime selection"
date: 2026-11-08
session_context: "Resume session. Operator: 'dont ever mention llama cpp as a primary npu access ever again'. A prior directions file listed a llama.cpp embedding server as route 2 for an NPU embedding model, while a memory note already restricted llama.cpp to models without a vendor-compiled bundle."
parked_until:
resolved:
resolution:
reference: "NvAEx-Recaps handoff/2026-11-06/WIKI-ADMIN-DIRECTIONS.md line 76; NOTES.md section 'Session 2026-11-08'"
commands_verified: none
---

**Issue:** A memory rule (vendor-compiled bundles go through the vendor NPU runtime; the generic runtime only for models without one) was written down and loaded, yet a later directions document still offered the generic runtime as an NPU route. That is the second miss of one rule, so per the second-violation rule the fix has to be a barrier, not a rewording.

**Suggested improvement:** A structural check, such as a pre-write lint on handoff and directions files, that flags any NPU route naming the generic runtime unless it is marked as a CPU or GPU fallback. termux-helper Part 2 should list the vendor routes first (LiteRT-LM chip bundles, QAIRT/QNN/AI Hub bundles, hybrid vendor GGUF to HTP), and the agent should read the pointed vendor directories in full before making any runtime claim.

**Principle:** When a rule about choosing a route keeps failing in prose, add a check that runs at write time on the documents that carry the routes forward.
