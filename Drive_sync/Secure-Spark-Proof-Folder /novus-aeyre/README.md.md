---
title: "README.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /novus-aeyre/README.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

# novus-aeyre (APK 3 — Media & Sensory Ingress Daemon)

## Overview
novus-aeyre is the native Android foreground media and sensory daemon within the sovereign
multi-node architecture. It executes sensory acquisition, local voice pipelines, and screen
capture outside the heavy terminal sandbox to ensure persistence and real-time response.

### Architecture References
- **01_SOVEREIGN_NODE_AND_APK_TOPOLOGY.md**:
https://docs.google.com/document/d/10K8oIQojpKYjQ21cbRPPSIJewnUXi11Ahvj4rvdv80k/edit
- **PROPOSAL-V2-CORRECTED-WIKI-TERMINOLOGY-AND-s-tier-ALTERNATIVE.md**:
https://drive.google.com/file/d/1S2cQzDPTknjzX9fR3q6lqsRLZxkcQAcA/view
- **Universal file configuration**:
https://docs.google.com/document/d/1oWzHeX_MIIjyVb0RUBZphdPCoc4Nw0z8ccK4cXgJhlE/e
dit

## Subsystem Capabilities
1. **Voice Activity Detection (VAD)**: Silero VAD running continuously in native runtime.
2. **Speech-to-Text (STT)**: Moonshine ONNX / local WhisperKit transcription on device.
3. **Text-to-Speech (TTS)**: Kokoro-82m ONNX high-efficiency audio synthesis.
4. **Screen Vision Ingress**: Framebuffer capture and OCR streaming for visual context.

## Subsystem Structure
- `screen_vision/` — Video buffer capture and OCR processing
- `voice_ast_stack/` — Audio AST and VAD state machine
- `stt_models/` — ONNX speech recognition model weights and configs
- `tts_models/` — Kokoro audio synthesis model weights
- `raw/`, `clean_md/`, `wiki_md/`, `skills/`, `tools/`, `scripts/`, `hooks/`, `pending/`, `audit/`,
`archive/`
