---
id: 21
title: "Duplicate detection treated whole-file SHA as the only test of 'same model'"
status: open
type: open-source
skill: []
proposes_skill: []
target_file: ["~/.claude/projects/-data-data-com-termux-files-home/memory/feedback_same_model_bytes_differ.md"]
siblings_checked: "feedback_keep_cross_chip_variants"
area: "model/file dedup methodology"
date: 2026-10-02
session_context: "Byte-identical scan of Models/, ~/downloads, ~/models and proot roots"
parked_until:
resolved:
resolution:
reference:
---

**Issue:** The agent said a byte-identical match "settles it" and near-same-size files are not duplicates. Operator: re-downloading the exact same model back to back often gives files a few KB apart. Counter-cases found in the same session: Kokoro v1.0 vs v1.1 model.onnx are 1 KB apart in size but 268M of 325M bytes differ (different models); the two Kokoro "v1.0" voice packs differ in nearly every byte but are the same voices in two packagings.

**Suggested improvement:** Dedup = model identity: full name (chip target, quant, version), inner weight hashes (zip CRC/SHA per weight, GGUF tensor data vs header), and a differing-byte count (`cmp -l | wc -l`). Whole-file SHA is one positive signal, not the definition.

**Principle:** Bytes are a packaging fact; "same model" is an identity question.
