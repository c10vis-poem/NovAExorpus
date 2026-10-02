---
id: 11
title: "termux-helper states 'Termux cannot reach the Hexagon DSP' as fact; operator's Qualcomm-sourced docs describe a GGML/libggml-htp path"
status: actioned
type: open-source
skill: [termux-helper]
proposes_skill: []
target_file: []
siblings_checked: "termux family: termux-helper, android-termux-operator, aesop-voice-pipeline — android-termux-operator excluded (no NPU claims, SKILL.md read in full 2026-10-01); aesop-voice-pipeline assumed, not opened"
area: "Part 2: What Termux Can and Cannot Reach; Part 3 'fastest model' framing"
date: 2026-10-01
session_context: "Operator asked about running Gemma locally. The agent repeated the skill's framing (12B Q4_0 'strongest/fastest'; NPU unreachable from Termux). The operator corrected: GenieX + HTP SDK + QAI-Hub compiled models are on the device; the GGML -> libggml-htp -> HTP split pipeline (HTP0/HTP1 weight split) comes straight from Qualcomm documentation stored on the device."
parked_until:
resolved: 2026-10-01
resolution: "Operator asked to fix directly. termux-helper Part 2/3, description and debug table rewritten in the live copy and in aesop-xi/skills/termux-helper/SKILL.md (PR). Untested claim and model ranking removed; GenieX GGUF->HTP path, split rule, test-before-claim added."
reference: "~/repos/aesop-xi/HTP/HTP-Memory-Architecture-and-runtime-splitting (1).txt; ~/repos/NovAExorpus/HTP/; ~/tools/geniex-bench/lib (libggml-hexagon.so, libggml-htp-v79.so)"
---

**Issue:** termux-helper Part 2 asserts "Termux CANNOT reach the Hexagon DSP … If a plan requires Termux to load QNN, GENIE, or QAIRT, the plan is wrong." The device has GenieX (libggml-hexagon, libggml-htp-v79, QNN HTP v79 libs), `libcdsprpc.so` readable from Termux, and vendor-derived docs describing llama.cpp's HTP backend with a two-domain weight split. The claim was never tested on this device (no run of `--device npu` recorded), yet the agent repeated it and ranked models without checking the operator's GenieX/QAI-Hub assets.

**Suggested improvement:** Replace the absolute claim with: "Unverified on this device; the operator's Qualcomm docs describe the GGML → libggml-htp → HTP path (see refs). Test with GenieX `--device npu` before asserting either way." Add a pointer to the on-device Qualcomm doc locations. Remove "strongest/fastest" model rankings, or make them conditional on a benchmark.

**Principle:** A skill must not state a platform capability limit as fact unless it was tested on the device; the operator's vendor documentation outranks a skill's untested claim.
