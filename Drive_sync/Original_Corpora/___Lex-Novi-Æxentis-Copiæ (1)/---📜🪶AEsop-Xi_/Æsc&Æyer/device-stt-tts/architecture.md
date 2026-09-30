# Architecture

## Runtime Topology

AESOP runs on Android via a two-layer stack:

```
┌─────────────────────────────────────────────────┐
│  Termux (Android host)                           │
│  bionic libc, Python 3.14                        │
│  ~/repos/aesop/voice-engine/   (this repo)       │
│  ~/models/  ──symlink──→ proot rootfs/models     │
│                                                  │
│  proot-distro login debian ─────────────────┐    │
│  ┌─────────────────────────────────────────┐ │    │
│  │  Debian proot                           │ │    │
│  │  glibc, Python 3.13                     │ │    │
│  │                                         │ │    │
│  │  sherpa-onnx 1.13.4                    │ │    │
│  │  numpy, huggingface_hub, sounddevice   │ │    │
│  │                                         │ │    │
│  │  /root/models/                          │ │    │
│  │    kokoro-multi-lang-v1.0/   (TTS)       │ │    │
│  │    moonshine-base-en-int8/  (STT)       │ │    │
│  │    silero-vad/              (VAD)        │ │    │
│  └─────────────────────────────────────────┘ │    │
└─────────────────────────────────────────────────┘
```

**Why proot?** sherpa-onnx has no prebuilt wheels for Termux's bionic libc + Python 3.14. The Debian proot provides glibc + Python 3.13 where sherpa-onnx installs cleanly via pip. Model files are ABI-agnostic ONNX data — one copy is shared via symlink/bind-mount between the Termux home and the proot rootfs.

Source: `voice-engine/README.md` lines 43–65.

## Models

All three models are ONNX files downloaded from HuggingFace and stored under `~/models/` (symlinked to `/root/models/` inside the proot).

| Component | Model | Size | HuggingFace Source | Key Files |
|---|---|---|---|---|
| **TTS** | Kokoro multi-lang v1.0 | ~382 MB | `csukuangfj/kokoro-multi-lang-v1_0` | `model.onnx`, `voices.bin`, `tokens.txt`, `espeak-ng-data/`, `lexicon-us-en.txt` |
| **STT** | Moonshine base-en int8 | ~273 MB | `csukuangfj/sherpa-onnx-moonshine-base-en-int8` | `preprocess.onnx`, `encode.int8.onnx`, `uncached_decode.int8.onnx`, `cached_decode.int8.onnx`, `tokens.txt` |
| **VAD** | Silero VAD v5 | ~629 KB | `R4kSo1997/sherpa-onnx-silero-vad-v5` | `silero_vad.onnx` |

Model paths are resolved at runtime via the `AESOP_MODELS_DIR` environment variable (default `~/models`). Each script constructs subdirectory paths by joining the models directory with a fixed directory name (e.g., `kokoro-multi-lang-v1.0`).

Source: `voice-engine/README.md` lines 6–15; all scripts read `MODELS_DIR = os.environ.get("AESOP_MODELS_DIR", ...)`.

## Pipeline

The voice pipeline chains three stages. The core flow is **VAD → STT → (callback) → TTS → playback**.

### 1. Voice Activity Detection (VAD)

- **Model:** Silero VAD v5
- **Config:** threshold 0.5, min_silence_duration 500 ms, max_speech_duration 30 s, sample_rate 16000 Hz
- **Window:** 512 samples per window (Silero requirement)
- **API:** `sherpa_onnx.VoiceActivityDetector` — feed audio via `accept_waveform()`, segments come out via `vad.front` / `vad.pop()`
- **Segment data:** each segment has `.start` (sample offset) and `.samples` (list of float audio samples)

Source: `voice-engine/scripts/vad_test.py` lines 22–74; `live_voice_loop.py` lines 47–55.

### 2. Speech-to-Text (STT)

- **Model:** Moonshine base-en int8 (offline recognition)
- **Config:** greedy_search decoding, configurable thread count (default 2)
- **API:** `sherpa_onnx.OfflineRecognizer.from_moonshine()` — create a stream, `accept_waveform()`, then `decode_stream()`
- **Input:** float32 samples at native sample rate (resampling to 16 kHz happens in VAD, not STT)

Source: `voice-engine/scripts/stt_test.py` lines 27–53; `live_voice_loop.py` lines 58–68.

### 3. Text-to-Speech (TTS)

- **Model:** Kokoro multi-lang v1.0 (offline synthesis)
- **Config:** `length_scale` controls speed (1.0 = normal), `sid` selects voice
- **API:** `sherpa_onnx.OfflineTts` — `tts.generate(text=..., sid=..., speed=...)`
- **Output:** float32 samples at Kokoro's native sample rate; scripts convert to int16 WAV

Source: `voice-engine/scripts/tts_test.py` lines 27–58; `live_voice_loop.py` lines 71–85.

### Pipeline Variants

| Script | Pipeline | Audio I/O |
|---|---|---|
| `tts_test.py` | TTS only | Text input → WAV file output |
| `stt_test.py` | STT only | WAV file input → text output |
| `vad_test.py` | VAD only | WAV file input → segment list |
| `voice_loop.py` | TTS → STT (self-test) | File-based, no mic/speaker |
| `live_voice_loop.py` | Mic → VAD → STT → TTS → Speaker | Real-time via sounddevice + PulseAudio |

## Script Breakdown

### `voice_loop.py` — VoiceEngine class

`VoiceEngine` (`voice_loop.py` line 38) is the standalone pipeline class that loads all three models and exposes:
- `transcribe_audio(samples, sample_rate)` — STT on raw float32 samples
- `speak(text, output_path)` — TTS to WAV file or raw samples
- `transcribe_wav(wav_path)` — helper: read WAV → transcribe

The `demo()` function (line 124) runs a TTS→STT round-trip self-test: generates speech from a fixed sentence, writes to a temp WAV, transcribes it back, and prints both texts. This is the simplest end-to-end verification.

### `live_voice_loop.py` — LiveVoiceLoop class

`LiveVoiceLoop` (`live_voice_loop.py` line 113) is the real-time interactive loop:
- Opens a `sounddevice.InputStream` at 16 kHz mono with 512-sample blocks
- Mic callback (`_mic_callback`, line 134) pushes samples into a thread-safe `deque` queue
- Main loop (`_process_loop`, line 175) drains 512-sample windows, feeds VAD, and when VAD emits a segment:
  1. Skips if duration < 0.2 s (noise filter)
  2. Runs STT → gets transcription text
  3. Builds response (currently `f"You said: {text}"` — placeholder for LLM integration)
  4. Runs TTS → gets reply audio
  5. Plays via `sd.play()` / `sd.wait()`

The `run_demo()` function (line 227) tests TTS → speaker → STT without a mic.

### `run_live.sh` — Launcher

This shell script is the primary entry point for live voice interaction. It:
1. Searches `/data/data/com.termux/files/usr/tmp/pulse-*` for the PulseAudio socket
2. Validates the socket exists
3. Launches `proot-distro login debian` with a bind-mount of the PulseAudio socket directory
4. Sets `PULSE_SERVER` and `AESOP_MODELS_DIR` environment variables inside the proot
5. Execs `live_voice_loop.py` with any passed arguments

Source: `voice-engine/scripts/run_live.sh`.

## Relationship to Novus-Agenti

Per `voice-engine/README.md` lines 67–76:

- Novus-Agenti is a separate Android app with its own `VoiceLoopController.kt` — it is not part of this repository.
- This voice engine runs in Termux + proot, not in the Android app process.
- Model files are shared data and do not conflict.
- The engine can later be wired into Novus-Agenti via HTTP (similar to an `ort_engine` pattern) or used standalone for terminal-based voice interaction.

This is an architectural boundary, not a code dependency. There is no import, API call, or shared code between AESOP and Novus-Agenti in this repository.

## Extension Points

- **LLM callback:** `live_voice_loop.py` line 211 hardcodes `response = f"You said: {text}"`. Replacing this with an LLM call (local or remote) is the intended integration point for conversational voice interaction.
- **Voice selection:** Kokoro TTS supports multiple voices via `--sid` / `--voice`. The `--voice` flag in `live_voice_loop.py` is accepted but the `sid=0` in `text_to_speech()` (line 92) is currently hardcoded — wiring voice name to sid is a future enhancement.
- **HTTP server:** The README mentions wiring the engine into Novus-Agenti via HTTP. No HTTP server exists yet; adding one (e.g., Flask/FastAPI wrapping `VoiceEngine`) would enable remote invocation.
