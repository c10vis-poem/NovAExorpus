---
title: "DECOUPLED_3APK_NATIVE_SPECIFICATION.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/03_ALTERNATIVES_PROPOSAL_V1/data_vault/02_wiki_md/DECOUPLED_3APK_NATIVE_SPECIFICATION.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

Decoupled 3-APK Native Specification & Android
System Architecture
Native Android Service Decoupling, ADB Loopback & Sensory
Streaming
Derived from: What and Why.txt, Where and When.txt, and
4-ARCHITECTURE-cont.-(6-files).​
Status: Canonical System Architecture Spec | Clean Markdown Layer​
Target Repository: data_vault/02_wiki_md/


1. The Core Engineering Challenge & Solution
The Failure Mode of Monolithic Android Apps:
Running an LLM inference engine, speech pipeline, and reactive UI inside a single Android
application process guarantees failure:

1.​ Garbage Collection Freezes: Model tokenization and inference introduce Java/Kotlin
GC pauses that freeze UI rendering.
2.​ Low Memory Killer (LMK) Panics: Android aggressively terminates background
processes that exceed memory thresholds (FOREGROUND_APP_ADJ boundaries).
3.​ Sandbox Restrictions: Standard Android applications cannot spawn persistent
daemons, access hardware sockets directly, or maintain headless execution.
The Decoupled 3-APK Suite Architecture:
The system bypasses Termux and standard application sandboxes by partitioning on-device
operations into three native APKs communicating over local abstract UNIX sockets (\0) and
WebSockets (127.0.0.1:8080, 127.0.0.1:8765):

┌───────────────────────────────────────────────────────────
─────────────┐

│ APK 1: HORIZONS UI (Master Presentation Shell & Concierge)             │

│ - Technology: Chromium WebView (HTML5 / React user interface)          │



│ - Permissions: Standard Android user app permissions                   │

│ - Components:                                                          │

│   ├─ Chat tile interface, terminal visualizer, model router/picker     │

│   ├─ Cloud fallback client (OpenRouter / OmniRoute HTTP API)           │

│   └─ Persistent Netty/Ktor WebSocket client to background daemons      │

└───────────────────┬────────────────────────────────┬──────
─────────────┘

                    │                                │

    UNIX Abstract Socket / WebSocket    UNIX Abstract Socket / WebSocket

    /dev/socket/aesc_shell.sock         /dev/socket/aeyre_media.sock

                    ▼                                ▼

┌──────────────────────────────────────┐
┌───────────────────────────────┐

│ APK 2: ÆSC (Terminal & Shell Daemon) │ │ APK 3: ÆYRE (Sensory Daemon)  │

│ - Technology: Native C++/Kotlin      │ │ - Technology: Native C++/ONNX │

│ - Permissions: Accessibility Service │ │ - Permissions: Video Game SDK │

│   and Android OS Assistant Role      │ │   and Media Projection API    │

│ - Components:                        │ │ - Components:                 │

│   ├─ Local ADB Loopback (127.0.0.1)  │ │   ├─ Silero VAD audio stream  │

│   ├─ Runs outside sandbox (UID 2000) │ │   ├─ Moonshine ONNX STT       │

│   ├─ NPU Unix socket hot-swapper     │ │   ├─ Kokoro-82M ONNX TTS      │

│   └─ Spawns persistent background CLI│ │   └─ Screen-vision frame scan │



└──────────────────────────────────────┘
└───────────────────────────────┘


2. The Local ADB Loopback Mechanism (Zero-Root Privilege Escalation)
●​ UID Separation: Standard apps run with isolated UIDs (e.g. u0_a245). The Android
adbd daemon runs with UID 2000 (shell).
●​ Wireless Debugging Bridge: By enabling Wireless Debugging, Android exposes adbd
over a local TCP loopback interface on 127.0.0.1.
●​ Execution Flow:
1.​ Pairing: Æsc generates an RSA key pair (~/.android/adbkey) and connects
once via adb pair 127.0.0.1:<pairing_port>.
2.​ Connection: On every system boot (boot.sh), Æsc automatically issues adb
connect 127.0.0.1:<port>.
3.​ Privilege Escalation: Commands launched through this local loopback execute
as UID 2000 (shell), enabling persistent background processes, socket
creation, and file manipulation across app boundaries without rooting the device.


3. The Concierge Processing Sequence
[User Speaks / Screen Event]

             │

             ▼

[Æyre Media Daemon] ──► Silero VAD detects voice ➔ Moonshine STT transcribes speech

             │          Screen Vision captures active frame context

             ▼

[Horizons UI Concierge] ──► Passes stream to 0.8B Qwen model to strip run-on typos

             │              Compiles clean, structured Markdown meta-prompt

             ▼

[User One-Tap Verification] (Optional prompt review on screen tile)



             │

             ▼

[OmniRoute Dispatcher] (Port 20128) ──► Local NPU (9B) OR Cloud Frontier (Claude/Vertex)

             │

             ▼

[Model Completion] ──► Kokoro TTS synthesizes voice response to earbud

                        Active execution steps logged to Reasoning Bank
