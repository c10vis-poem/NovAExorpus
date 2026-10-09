---
title: "MAP.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /novus-aeyre/MAP.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

# MAP.md — novus-aeyre Navigation Map & Component Ontology

## Subsystem Overview
**novus-aeyre** (APK 3): Sovereign Media & Sensory Ingress Daemon.
Responsible for native on-device audio/speech processing, voice AST pipelines, and real-time
screen vision capture.

### Authoritative Architecture Pointers
- **01_SOVEREIGN_NODE_AND_APK_TOPOLOGY.md**:
https://docs.google.com/document/d/10K8oIQojpKYjQ21cbRPPSIJewnUXi11Ahvj4rvdv80k/edit
- **PROPOSAL-V2-CORRECTED-WIKI-TERMINOLOGY-AND-s-tier-ALTERNATIVE.md**:
https://drive.google.com/file/d/1S2cQzDPTknjzX9fR3q6lqsRLZxkcQAcA/view
- **3- 05_FEDERATED_FILE_TREE_TOPOLOGY_MASTER.md.txt**:
https://drive.google.com/file/d/19K44g7ygYMZ-OCU83VmYqcjUntZ8JGCm/view

---

## Directory Layout

### Universal Baseline Subfolders
- `raw/` — Ingestion landing zone for raw sensory inputs, test audio captures, and unprocessed
data.
- `clean_md/` — Condensed markdown documentation complying with the Non-1:1
Condensation Law.
- `wiki_md/` — Compounding living wiki entries with bidirectional wikilinks.
- `skills/` — Local procedural skills for sensory capture, voice trigger processing, and VAD
tuning.
- `tools/` — Local executable CLI utilities and testing tools.
- `scripts/` — Executable shell/Python scripts for daemon lifecycle and model testing.
- `hooks/` — Subsystem-specific Git, compilation, and validation hooks.
- `pending/` — Staged tasks, unverified outputs, and audio/vision pipeline tickets.
- `audit/` — Verification reports, latency benchmarks, and failure traces.
- `archive/` — Superseded snapshots and historical records.

### Domain-Specific Subfolders
- `screen_vision/` — Frame capture buffers, OCR pipelines, and visual stream decoders.
- `voice_ast_stack/` — Silero VAD, voice activity state machine, and audio AST routing.
- `stt_models/` — Moonshine ONNX / WhisperKit local speech-to-text models and runtimes.
- `tts_models/` — Kokoro-82m / Piper ONNX local text-to-speech synthesis models.
