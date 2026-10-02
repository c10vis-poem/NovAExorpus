---
id: 16
title: "Stated 'the vendor page has no file' after one summarized web fetch and two guessed repo names"
status: open
type: open-source
skill: []
proposes_skill: []
target_file: ["~/.claude/CLAUDE.md"]
siblings_checked: "none — target is an instructions file, not a skill"
area: "Read Before Claim; absence claims"
date: 2026-10-01
session_context: "NPU server work: checking whether the vendor's model hub served a different GGUF than the operator's file"
parked_until:
resolved:
resolution:
reference:
---

**Issue:** Asked whether the vendor hub served a different model file, the agent ran one WebFetch of a JavaScript-rendered page (read through a summarizer) and guessed two Hugging Face repo names. It then reported "neither page has the file". The operator supplied the model README, which named the vendor's own CLI (`fetch --runtime ... --precision ...`) as the distribution path. That CLI answered the question in one command: same file, plus the vendor's own benchmark table. Restates the pattern in 0007 (absence claims need a full search).

**Suggested improvement:** Read Before Claim (CLAUDE.md): an absence claim about an external source must name the exact probes and say "not found by these", never "does not exist". Before any absence claim about a vendor model, run the vendor's documented tool or API first.

**Principle:** A shallow probe that finds nothing is evidence about the probe. Report what was checked, and use the source's own documented access path before concluding something is absent.
