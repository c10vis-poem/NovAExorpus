# Operations

## Prerequisites

- **Termux** (latest from F-Droid, not Play Store)
- **proot-distro** with Debian installed
- ~1 GB free disk space for model downloads
- Internet connection for initial setup

## Initial Setup

The full setup walkthrough is in `voice-engine/SETUP.md`. Summary:

### 1. Install sherpa-onnx in the Debian proot

```bash
proot-distro login debian -- /usr/bin/python3 -m pip install --break-system-packages \
    sherpa-onnx numpy huggingface_hub
```

For the live voice loop, also install `sounddevice`:

```bash
proot-distro login debian -- /usr/bin/python3 -m pip install --break-system-packages sounddevice
```

### 2. Download models

Models are downloaded from HuggingFace into the proot's `/root/models/` directory:

```bash
# Kokoro TTS (~382 MB)
proot-distro login debian -- /usr/bin/python3 -c "
from huggingface_hub import snapshot_download
snapshot_download('csukuangfj/kokoro-multi-lang-v1_0', local_dir='/root/models/kokoro-multi-lang-v1.0')
"

# Moonshine STT (~273 MB)
proot-distro login debian -- /usr/bin/python3 -c "
from huggingface_hub import snapshot_download
snapshot_download('csukuangfj/sherpa-onnx-moonshine-base-en-int8', local_dir='/root/models/moonshine-base-en-int8')
"

# Silero VAD (~629 KB)
proot-distro login debian -- /usr/bin/python3 -c "
from huggingface_hub import snapshot_download
snapshot_download('R4kSo1997/sherpa-onnx-silero-vad-v5', local_dir='/root/models/silero-vad')
"
```

### 3. Symlink models to Termux home

```bash
ln -sfn /data/data/com.termux/files/usr/var/lib/proot-distro/containers/debian/rootfs/root/models \
    /data/data/com.termux/files/home/models
```

This makes models accessible from both Termux (`~/models`) and the proot (`/root/models`).

### 4. Clone the repo into the proot

```bash
proot-distro login debian -- git clone https://github.com/c10vis-poem/aesop.git /root/repos/aesop
```

Alternatively, if already cloned in Termux, bind-mount the repos directory:

```bash
proot-distro login debian --bind /data/data/com.termux/files/home/repos:/root/repos -- \
    python3 /root/repos/aesop/voice-engine/scripts/voice_loop.py --demo
```

Source: `voice-engine/SETUP.md` lines 1–62.

## Environment Variables

| Variable | Default | Purpose |
|---|---|---|
| `AESOP_MODELS_DIR` | `~/models` | Root directory containing the three model subdirectories |

`run_live.sh` sets `AESOP_MODELS_DIR=/root/models` inside the proot regardless of the Termux-side value.

Source: `voice-engine/README.md` lines 86–90; `scripts/run_live.sh` line 38.

## Running Tests

### Individual component tests

```bash
# TTS — text to speech
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
```

Each script prints `SUCCESS` on completion. The STT and TTS scripts accept additional flags:

| Script | Flags | Description |
|---|---|---|
| `tts_test.py` | `--output`, `--sid`, `--speed` | Output path, voice ID, speed multiplier |
| `stt_test.py` | `--threads` | CPU threads for Moonshine decoder |
| `vad_test.py` | `--threshold` | VAD confidence threshold (default 0.5) |

### Full self-test (no mic needed)

```bash
proot-distro login debian -- python3 \
    /root/repos/aesop/voice-engine/scripts/voice_loop.py --demo
```

This runs a TTS→STT round-trip: generates speech from a fixed sentence, writes to a temp WAV, transcribes it back, and prints both texts. Verifies all three models load and the audio conversion pipeline works end-to-end.

Source: `voice-engine/scripts/voice_loop.py` lines 124–146.

## Audio I/O

### File-based mode (no PulseAudio)

Works without any audio bridge. Use Termux's built-in tools for recording and playback:

```bash
# Record 5 seconds
termux-microphone-record -d 5 -f ~/input.wav

# Transcribe
proot-distro login debian -- python3 \
    /root/repos/aesop/voice-engine/scripts/stt_test.py /root/input.wav

# Generate speech
proot-distro login debian -- python3 \
    /root/repos/aesop/voice-engine/scripts/tts_test.py "Response text" --output /root/output.wav

# Play
termux-media-player play ~/output.wav
```

### Live mode (PulseAudio bridge)

Real-time mic input and speaker output require bridging PulseAudio from Android into the proot.

**Start PulseAudio in Termux:**

```bash
pkg install pulseaudio
pulseaudio --start -nF ~/pulse-noauth.pa --exit-idle-time=-1 --disable-shm
```

**Run the live voice loop:**

```bash
bash ~/repos/aesop/voice-engine/scripts/run_live.sh
```

`run_live.sh` handles socket discovery and proot bind-mounting automatically. It:
1. Finds the PulseAudio socket in `/data/data/com.termux/files/usr/tmp/pulse-*`
2. Bind-mounts that directory into the proot at `/tmp/pulse-termux`
3. Sets `PULSE_SERVER=unix:/tmp/pulse-termux/native` inside the proot
4. Execs `live_voice_loop.py` with any passed arguments

**Live loop options:**

```bash
bash ~/repos/aesop/voice-engine/scripts/run_live.sh --demo          # TTS→speaker→STT, no mic
bash ~/repos/aesop/voice-engine/scripts/run_live.sh --speed 1.1      # Faster TTS
bash ~/repos/aesop/voice-engine/scripts/run_live.sh --voice af_heart # Kokoro voice name
```

Source: `voice-engine/SETUP.md` lines 79–108; `scripts/run_live.sh`; `scripts/live_voice_loop.py` lines 251–264.

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| `ERROR: File not found` in STT/VAD test | WAV path wrong or file missing | Use absolute paths inside the proot (e.g., `/root/models/...`) |
| `ERROR: Models not found` in live loop | `AESOP_MODELS_DIR` not set or models not downloaded | Verify `~/models/kokoro-multi-lang-v1.0/model.onnx` exists |
| `ERROR: PulseAudio socket not found` | PulseAudio not started in Termux | Run `pulseaudio --start -nF ~/pulse-noauth.pa --exit-idle-time=-1 --disable-shm` |
| sherpa-onnx import fails | Running in Termux directly instead of proot | Prefix all commands with `proot-distro login debian --` |
| `sounddevice` import fails in live loop | Not installed in the proot | `proot-distro login debian -- pip install --break-system-packages sounddevice` |
| VAD finds no segments | Audio not 16 kHz mono, or threshold too high | VAD internally resamples via simple decimation; check `--threshold` (lower = more sensitive) |

## Verification Checklist

After setup, verify each layer works:

1. **TTS:** `tts_test.py` prints `SUCCESS` and creates a WAV file with non-zero size
2. **STT:** `stt_test.py` prints a transcription and `SUCCESS`
3. **VAD:** `vad_test.py` prints detected segments and `SUCCESS`
4. **Pipeline:** `voice_loop.py --demo` prints both the original and transcribed text and `SUCCESS`
5. **Live:** `run_live.sh --demo` plays audio through the speaker and prints `SUCCESS`
