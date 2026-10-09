# Audio pipeline on this device

Verified working 2026-08-18 on motorola razr ultra 2025, native Termux.
Load this only when working on recording, transcription, or speech output.

**Update 2026-08-29:** a real-time (mic -> VAD -> STT -> TTS -> speaker) voice engine
now also works on this device, in addition to everything below — see the
`aesop-voice-pipeline` skill. Everything in this file is still accurate for the
`vv`/`ccv` manual-capture flow described here; the new skill is a separate,
continuous alternative, not a replacement. It also documents a real Moonshine STT bug
(silent failure past ~10s of audio) that affects the `local` engine described below.

## Recording

Two non-obvious failures, both of which look like "the microphone is broken":

1. **The recorder does not release the mic.** Without `-q` first, every capture
   after the first returns near-silence (amplitude ~0.001 instead of ~0.3). VAD
   then correctly reports NO SPEECH, which reads as a broken VAD.
2. **The file is MP4/AAC no matter what you name it.** `-f out.wav` still produces
   `ftypmp42` ISO Media. `sox` and whisper.cpp reject it: "RIFF header not found".

Working sequence:

```bash
termux-microphone-record -q >/dev/null 2>&1        # mandatory release
termux-microphone-record -f rec.m4a -l 8 -r 16000 -c 1 -b 64
ffmpeg -y -i rec.m4a -ar 16000 -ac 1 -acodec pcm_s16le rec.wav
```

`-r 16000` works fine *after* a release — it was only silent when the mic was
still locked. Native 16 kHz beats capturing at the 8 kHz default and upsampling.

Verify a capture actually contains speech before blaming anything downstream:

```bash
sox rec.wav -n stat 2>&1 | grep "Maximum amplitude"
```

Real speech reads roughly 0.2–0.6. Anything under 0.01 is silence.

## Cueing the operator

stdout does not appear until the command completes, so a printed "TALK NOW" is
never seen in time. Use:

```bash
termux-toast -b red -c white -g middle "TALK NOW - 3 SEC"
termux-vibrate -d 800
```

Do **not** background these with `&`. A backgrounded job inherits stdout and holds
the pipe open, which hangs the calling tool until it times out.

## Transcription

`~/record_transcribe.sh` runs the full chain: record → convert → Silero VAD →
Moonshine, inside `proot-distro login debian`. Silero at 16 kHz requires exactly
512-sample frames; pad the final short chunk or it misbehaves.

## Speech output

`~/bin/speak` — strips markdown, chunks by sentence, interruptible.

```bash
speak "some **markdown** text"
cat notes.md | speak
speak --stop                    # cut off immediately
```

**Use Kokoro. Android TTS on this phone is a dead end.** Verified 2026-08-18,
operator confirmed hearing it: `~/models/kokoro-multi-lang-v1.0/` is a complete
sherpa-onnx voice (model.onnx, voices.bin, tokens.txt, espeak-ng-data, dict,
lexicons). Synthesize to a wav in `$TMPDIR` and play it with `play`. No Android
dependency at all.

`soundfile` is NOT installed in the Debian venv — write wavs with the stdlib
`wave` module.

Every Android engine here fails, and none of it is fixable from this side:
`com.google.android.tts` and `com.qualcomm.qti.voiceai.speech` both **hang**
(exit 124, no audio); VoxSherpa exits 0 instantly and is silent. Audio output
itself is fine — the operator hears `play`. Do not spend more time on
`termux-tts-speak`. Note `~/bin/speak` still expects
`-e com.CodeBySonu.VoxSherpa` to be present.

Markdown must be stripped before speaking or headings and paths are pronounced
as "hashtag hashtag" and "slash". `~/bin/speakclean.py` does this and drops code
blocks entirely.

## Known broken, do not build on

- `kokoro_tts.py` — loads `kokoro-v1.0.onnx`, which does not exist on this device.
  Its phoneme map also iterates single characters, so multi-character phonemes
  (`aɪ`, `dʒ`, `oʊ`) never match and are silently dropped.
  **This entry is about that one script and that one missing file. It is NOT a
  verdict on Kokoro.** The working voice is the separate
  `~/models/kokoro-multi-lang-v1.0/` directory — see Speech output above. A
  previous session read this bullet as "Kokoro is broken" and lost hours. That is
  the third time a "known broken" note here pointed at the wrong artifact; check
  what is actually on disk before trusting any of them.
- `say.py` — imports `ttstokenizer`, not installed. `model.onnx` (178 MB) and
  `voices.json` (54 MB) are present, so only the tokenizer is missing.
(`listen.sh` was listed here until 2026-08-18. That was wrong — see below.)

## Voice input — read this before building anything

**The offline chain is the default. `termux-speech-to-text` is the fallback.**
This flipped twice in one day — read both halves before changing it again.

`termux-speech-to-text` works (verified 2026-08-18) and is genuinely nicer to
use: one press, Android's own recognizer, words appear as you speak, no proot.
But it **truncates every capture after roughly 8–12 words**. Android owns that
endpointing decision and the wrapper exposes no timeout to tune it, so it cannot
be fixed from here. It also has no press-to-stop: it is a single blocking call,
which is why a second press appears to do nothing.

The offline path has no endpointing at all — recording runs until the key is
pressed again. Slower and complete beats instant and truncated. `~/bin/vv`
therefore defaults to `ENGINE=local`; `VV_ENGINE=system` restores the recognizer
for short utterances.

Do not "fix" the truncation by calling the recognizer again and stitching. Tried
2026-08-18: it needs 1–2 s just to initialise — longer than the pause between
sentences — so it reliably misses the continuation it was added to catch. 7 s for
a ten-word utterance, still truncated. Strictly worse than a single call.

`RecognitionListener#onError(7)` in logcat is `ERROR_NO_MATCH` — the recognizer
ran and heard nothing. It does **not** mean anything is broken. Empty output with
exit 0 almost always means the operator was not told when to talk.

The offline Moonshine chain (record → Silero VAD → Moonshine in proot, ~3 s) is
the fallback, not the default. Its real cost is architectural: the mic only works
from Termux, the models only run in proot, so every utterance round-trips
Termux → proot → Termux. That round-trip is the confusing part, and the system
recognizer removes it entirely.

`~/repos/aesop-xi/deploy/phone/stt_process.py` already does file-in → text-out and
takes the recorder's `.m4a` directly (it runs its own ffmpeg). Do not write a new
transcriber.

### The keyboard mic button does not work in Termux, and cannot be made to

Termux reports `inputType = TYPE_NULL` ("not a text field, send raw keys"), so
Gboard disables voice typing. `enforce-char-based-input = true` switches it to
`TYPE_TEXT_VARIATION_VISIBLE_PASSWORD | TYPE_TEXT_FLAG_NO_SUGGESTIONS` — **tested
2026-08-18, does not help**: keyboards suppress voice input on password-type
fields, so the mic stays dead and suggestions are lost. Left off. Do not retry.

Whisper+ has never been installed on this device despite notes assuming it.
Only `com.qualcomm.qti.voiceai.speech` and `com.CodeBySonu.VoxSherpa` are present.

### Getting speech into a TUI prompt

There is no supported way to inject text into Claude Code's prompt except tmux
`send-keys -l` (literal, no Enter, so it arrives editable). This means Claude
must be **started** inside tmux — a running process's terminal cannot be moved in
afterwards. `~/bin/ccv` is that launcher; `~/bin/vv` is the mic; `~/.tmux.conf`
binds F1/F2/F3, surfaced as 🎤/🔊 extra-keys in `~/.termux/termux.properties`.

No clipboard step anywhere: the operator has explicitly rejected copy-and-paste.

**The MIC key is F1, and nvim maps `<F1>` to `:help`.** In any Claude Code
session *not* wrapped in tmux, nothing intercepts the key, so pressing MIC while
the prompt is open in the external editor opens `help.txt` over the buffer — and
Claude then blocks forever waiting for the editor to exit. Two sessions hung this
way on 2026-08-18 and it reads exactly like "the mic button is broken."
`~/.config/nvim/init.lua` now maps F1/F2/F3 to `<Nop>` unconditionally. Inside
tmux this never bites, because tmux consumes the key first.

Because of that, launch **every** session with `ccv`, never a bare `claude` in a
fresh Termux tab. `ccv` now opens a new window in the current directory instead
of dumping you back into the first one, so there is no longer any reason to.

tmux is not a substitute for `termux-wake-lock`. tmux keeps the session alive when
the terminal goes away; wake-lock keeps the CPU running with the screen off.

### Speaking replies back

`~/bin/speakd` follows the session transcript JSONL rather than the terminal, so
scrolling cannot stop it and `tool_use` entries cannot kill it. Speech is
block-granular — Claude Code has no per-token hook. Scraping the TUI with
`pipe-pane` re-reads redrawn frames and stutters; rejected.

**Termux has no `/usr/bin/env`.** A `#!/usr/bin/env python3` shebang fails
silently when the file is executed directly while working fine under
`python3 file`. Use `#!/data/data/com.termux/files/usr/bin/env python3`.
