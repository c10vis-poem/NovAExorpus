# AESOP Voice Engine — Quickstart

## What is AESOP?

AESOP is an **on-device voice engine** that runs Speech-to-Text (STT), Text-to-Speech (TTS), and Voice Activity Detection (VAD) entirely on an Android device — no cloud, no network calls for inference. It is built on [sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) and runs inside a Debian `proot` environment on top of Termux.

The engine is designed to be standalone: it can be used independently for terminal-based voice interaction or later wired into a companion Android app (Novus-Agenti) via HTTP.

## Repository Structure

```
voice-engine/
├── README.md                  Project overview, architecture diagram, quick-start
├── SETUP.md                   Step-by-step installation and model download
└── scripts/
    ├── stt_test.py            Standalone STT test (Moonshine)
    ├── tts_test.py            Standalone TTS test (Kokoro)
    ├── vad_test.py            Standalone VAD test (Silero)
    ├── voice_loop.py          VoiceEngine class + file-based self-test demo
    ├── live_voice_loop.py     Real-time mic → VAD → STT → TTS → speaker loop
    └── run_live.sh            Shell launcher: bridges PulseAudio into proot
```

The entire repository is five Python scripts, one shell launcher, and two Markdown docs. There is no package manager, no build system, and no test framework — verification is done by running the scripts and checking for `SUCCESS` output.

## Key Concepts

| Concept | Details |
|---|---|
| **Runtime** | Debian proot on Termux (Android). sherpa-onnx cannot install natively in Termux due to bionic libc + Python 3.14 incompatibility. |
| **Models** | Three ONNX models (~656 MB total) stored in `~/models/`, symlinked into the proot. See [Architecture → Models](architecture.md#models). |
| **Pipeline** | VAD detects speech segments → STT transcribes → (LLM callback) → TTS synthesizes reply. See [Architecture → Pipeline](architecture.md#pipeline). |
| **Audio I/O** | Two modes: file-based (default, no PulseAudio needed) and live (PulseAudio bridge). See [Operations → Audio I/O](operations.md#audio-io). |

## Quick Start

All commands are run from Termux and enter the Debian proot via `proot-distro login debian`.

```bash
# TTS — generate speech from text
proot-distro login debian -- python3 \
    /root/repos/aesop/voice-engine/scripts/tts_test.py "Hello world" --output /tmp/test.wav

# STT — transcribe a WAV file
proot-distro login debian -- python3 \
    /root/repos/aesop/voice-engine/scripts/stt_test.py \
    ~/models/moonshine-base-en-int8/test_wavs/0.wav

# VAD — detect speech segments
proot-distro login debian -- python3 \
    /root/repos/aesop/voice-engine/scripts/vad_test.py \
    ~/models/moonshine-base-en-int8/test_wavs/0.wav

# Full self-test (TTS → STT round-trip, no mic needed)
proot-distro login debian -- python3 \
    /root/repos/aesop/voice-engine/scripts/voice_loop.py --demo

# Live voice loop (requires PulseAudio bridge)
bash ~/repos/aesop/voice-engine/scripts/run_live.sh
```

## Where to Go Next

- **[Architecture](architecture.md)** — Runtime topology, model inventory, pipeline flow, script-by-script breakdown.
- **[Operations](operations.md)** — Setup, model download, PulseAudio bridging, environment variables, troubleshooting.

## Existing Documentation

The repository ships with two primary docs that serve as authoritative references:

- `voice-engine/README.md` — project overview, architecture diagram, model table, environment variables.
- `voice-engine/SETUP.md` — full installation walkthrough (sherpa-onnx, model download, symlink, PulseAudio, file-based fallback).

These OpenWiki pages synthesize and link to those docs rather than duplicating them.
