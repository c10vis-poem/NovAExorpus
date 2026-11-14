---
id: 68
title: "Parallel background subagents ran large models at once; Android killed the Termux app"
status: open
type: open-source
skill: [android-termux-operator, termux-helper]
proposes_skill: []
target_file: []
siblings_checked: "no family registry; aesop-voice-pipeline also loads models on-device, assumed applicable, not added: termux-helper owns runtime limits"
area: "on-device model runs from subagents; memory limits"
date: 2026-11-08
session_context: "A session spawned four background subagents (NPU embeddings, GenieX HTP, Adreno 9B/12B runs, docs ingest). The 12B runs pushed system RAM to ~15.1 GB of 15.2 GB; the Termux app was killed and restarted about a minute after the last tool call."
parked_until:
resolved:
resolution:
reference: "npu-work/1D/*.stats (peak_system_used_MB=15175)"
commands_verified: none
---

**Issue:** Several subagents loaded models at the same time with only a per-run kill watchdog at ~14.9 GB used. Nothing serialised model loads across agents (an HTP.lock existed for NPU only, not GPU/CPU runs). Android's low-memory killer took the whole Termux app, every subagent and the parent session with it.

**Suggested improvement:** One device-wide model-run lock for every model load (NPU, GPU, CPU), and a pre-run free-memory check that refuses to start when available RAM is below the model size plus a margin.

**Principle:** On a phone, the host app is the shared failure domain: parallel agents must serialise anything that can exhaust memory, because one overrun kills them all.
