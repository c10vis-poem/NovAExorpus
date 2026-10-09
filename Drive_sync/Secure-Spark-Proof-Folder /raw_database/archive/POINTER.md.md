---
title: "POINTER.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/archive/POINTER.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

# POINTER.md — novus-aeyre Subsystem Specification
Repository: novus-aeyre (APK 3 — Native Media & Sensory Ingress Daemon)
Authority: 01_SOVEREIGN_NODE_AND_APK_TOPOLOGY.md &
05_FEDERATED_FILE_TREE_TOPOLOGY_MASTER.md

## Core Architectural Invariants
1. Voice AST Pipeline: Zero-latency voice activity detection running Silero VAD.
2. Speech-to-Text: Moonshine Small ONNX and whisper.cpp on-device transcription engine.
3. Text-to-Speech: Kokoro-82m and Sherpa-ONNX real-time local audio synthesis.
4. Screen Vision Capture: Frame buffer streaming via Android MediaProjection / Video Game
SDK for real-time OCR and screen understanding.
5. Ingestion & Normalization: Awaits Phase 1 extraction and pipeline integration.
