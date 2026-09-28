---
name: termux-mobile-dev
description: >-
  Set up and troubleshoot the on-device Termux environment — VNC/XFCE remote desktop
  (phone as TigerVNC host, tablet as AVNC client), the Matrix (zsh + tmux + cmatrix +
  Termux:Float) phone terminal, local LLM API + voice I/O (STT/TTS) setup, and native
  dependency build workarounds for packages with no prebuilt Android/Bionic wheels.
  Use for VNC connection failures, XFCE/dbus issues, local LLM/voice pipeline setup or
  breakage, or when a pip/npm install fails to compile natively on Termux. Every step
  is sourced or trial-verified; killed guesses are recorded so they aren't repeated.
---

# Termux Mobile Dev Environment

This file is the full reference — there is no separate `wiki/Termux-VNC-Matrix-Environment.md`;
an earlier version of this skill linked to one that was never actually created.

**2026-08-08: consolidated with the former `llm-wiki-termux-setup-SKILL.md` into this single
file** (per user instruction — duplicate/stale copies existed in `skills/skills-corpus/` and
3x inside `obsidian-wiki-clean/INBOX/`, none kept current). This is now the one canonical
Termux skill file.

## Topology
- **Host:** phone, Termux, no root → Xtigervnc + XFCE.
- **Client:** Samsung Tab S9 FE+, AVNC → geometry **1280×800** (half of 2560×1600).
- **Transport:** same WiFi LAN. Phone IP is **DHCP, it changes** — re-check `ifconfig`
  (`wlan0` inet) every session. `127.0.0.1` is loopback; the tablet cannot use it.
- Display `:1` = port **5901** (port = 5900 + display).

## First move on ANY connection failure: classify the error
- **Connection refused** → port closed / VNC bound to localhost.
- **Connection timed out** → packets reach nothing → still localhost-bound OR router
  **AP isolation**.

### Verification — `ss`/`netstat` DO NOT WORK on the phone
Unprivileged Termux denies netlink: `Cannot open netlink socket: Permission denied`
(and `/proc/net/tcp*` is permission-denied too). Verify via the **VNC log** instead:
```bash
cat ~/.vnc/*.log | grep -iE "listen|interface|port"
```
| Log line | Meaning | Fix |
|----------|---------|-----|
| `Listening for VNC connections on all interface(s)` | bound to LAN; phone is correct | still timing out → **AP isolation** → phone hotspot |
| `Listening ... localhost` / only `127.0.0.1` | localhost-bound | apply tigervnc.conf fix below |
| crash / no listen line | server died | read rest of log; usually dbus |

Secondary probe (also netlink-free):
```bash
pkg install netcat-openbsd
nc -vz 127.0.0.1 5901            # up?  (always works if server alive)
nc -vz <phone-wlan-ip> 5901      # bound to all interfaces? (refused = localhost-only)
```

## Make VNC listen on the LAN (persistent, documented method)
The CLI flag `-localhost no` was unreliable in trials. Use the config file:
```bash
echo '$localhost="no";' >> ~/.vnc/tigervnc.conf
echo '1;' >> ~/.vnc/tigervnc.conf
vncserver -kill :1
vncserver :1 -geometry 1280x800 -depth 24
```

## AP isolation (router blocks device-to-device WiFi)
If the log says "all interface(s)" / `nc` to the wlan IP succeeds but the tablet still
times out, the router is the blocker — not the phone. Enable the **phone hotspot**,
connect the tablet to it, point AVNC at the hotspot IP (often `192.168.43.1`). socat
fallback: `socat TCP-LISTEN:5902,bind=0.0.0.0,fork TCP:127.0.0.1:5901 &` → AVNC on 5902.

## XFCE/dbus won't start
Log shows `Failed to get a Console kit proxy` → no session dbus. xstartup must launch it:
```bash
cat > ~/.vnc/xstartup << 'EOF'
#!/data/data/com.termux/files/usr/bin/bash
export DISPLAY=:1
export XDG_RUNTIME_DIR=$TMPDIR
dbus-daemon --session --address=$DBUS_SESSION_BUS_ADDRESS --nofork --nopidfile --syslog-only &
sleep 1
xfce4-session &
EOF
chmod +x ~/.vnc/xstartup
```
Package is `dbus`, **not** `dbus-x11` (that name does not exist in Termux).

## Stale lock cleanup (Termux tmp is `$PREFIX/tmp`, NOT `/tmp`)
```bash
vncserver -kill :1 2>/dev/null
pkill -9 Xvnc; pkill -9 Xtigervnc
rm -f ~/.vnc/*.pid ~/.vnc/*.log
rm -f $PREFIX/tmp/.X1-lock $PREFIX/tmp/.X11-unix/X1
```

## Killed guesses (VNC/XFCE)
- ❌ "Android needs root to bind external ports." FALSE — Termux serves VNC to the LAN
  with no root (XDA `[NO-ROOT]` guide).
- ❌ Relying on CLI `-localhost no`. Use `tigervnc.conf` instead.
- ❌ Using `ss`/`netstat`/`/proc/net/tcp` to verify the bind. Netlink is denied on
  unprivileged Android. Use the VNC log or `nc`.
- ❌ Cleaning `/tmp`. Termux uses `$PREFIX/tmp`.

## Matrix phone terminal (the "native Android over a waterfall" look)
- Pieces: **zsh + Oh My Zsh** (the "zush"), **tmux** (split), **cmatrix** (waterfall),
  **Termux:Float** (overlay; F-Droid only, Play build won't work).
- Colors → `~/.termux/colors.properties`: bg `#0D0D0D`, fg/cursor `#00FF41`; then
  `termux-reload-settings`.
- Launcher `~/matrix-tmux.sh`: new detached session → `cmatrix -b -C green` top →
  `split-window -v -p 40` → attach. cmatrix top 60%, shell bottom 40%.
- tmux prefix on Android: `Vol-Down+B` barely registers — tap **CTR** on the keybar then
  **B**. Stop waterfall without switching panes:
  `tmux send-keys -t matrix:0.0 q ""`.
- Float attach needs `unset TMUX && tmux attach -t matrix` (else "sessions should be
  nested with care"). Float won't open → enable "Display over other apps". Resize →
  long-press, drag corners.

## Per-session checklist (VNC)
1. `ifconfig` → phone `wlan0` inet (not 127.0.0.1).
2. Clean locks if restarting.
3. `vncserver :1 -geometry 1280x800 -depth 24`.
4. Verify via the **log** (not `ss`): must say "all interface(s)".
5. AVNC → `<phone-ip>:5901` + vncpasswd.
6. Timeout despite "all interface(s)" → AP isolation → hotspot or socat.

---

## On-device coding agents: OpenClaude + DeepSeek V4 via OpenRouter

**Two-pronged attack** — Anthropic Claude Code in the cloud (heavy reasoning) plus
**OpenClaude** on Termux (model-swappable, cheap parallel grunt work) hitting the same
GitHub repo / branch. You arbitrate merges.

### Why OpenClaude, not OpenCode
OpenClaude is the closer behavioural clone of the Anthropic Claude Code CLI — same
agentic tool-use loop, MCP-style integrations, runs native on Termux without an
Anthropic key. Claude Code for Android (the community port) is similar but locked to
Anthropic's API. Both are **non-Anthropic-proprietary** and run on Android; OpenClaude
wins on flexibility because you can point it at any model.

### Install on Termux (phone or tablet)
```bash
pkg install nodejs git
npm i -g openclaude          # or: git clone … && npm i -g .
```

### Point it at DeepSeek V4 via OpenRouter
```bash
# one-time: paste just the key at the prompt
read -s OPENROUTER_KEY
export OPENROUTER_API_KEY="$OPENROUTER_KEY"

# persist for future shells
echo 'export OPENROUTER_API_KEY="<paste-in-editor>"' >> ~/.zshrc

# OpenClaude config — OpenAI-compat base URL, DeepSeek V4 model id
openclaude config set baseURL  https://openrouter.ai/api/v1
openclaude config set model    deepseek/deepseek-chat-v4
openclaude config set apiKey   "$OPENROUTER_API_KEY"
```

Then `openclaude` in the repo dir. Tool-call fidelity on DeepSeek is good but not
Anthropic-tier — give it the grunt work (refactors, doc gen, test scaffolding, lint
sweeps), keep architecture / multi-file reasoning on cloud Claude.

### Cost shape (June 2026, OpenRouter)
- DeepSeek V4: ~$0.27 / M in, ~$1.10 / M out.
- Cheap enough to run multiple parallel agents on the same branch all day.

### Killed guesses
- ❌ "DeepSeek can hit the official `claude` CLI directly." It can't — that CLI is
  hardcoded to Anthropic's `/v1/messages`. You'd need a proxy shim
  (`claude-code-router`, `anyclaude`). OpenClaude sidesteps the whole problem.
- ❌ "OpenCode = OpenClaude." Different projects. OpenClaude is the one to use here.

---

## Omnara (parked, not yet trialled)

YC S25 — mobile/web front-end for Claude Code. Same Anthropic Claude under the hood,
prettier UI, push notifications, multi-session management. Candidate for the next
multi-agent fan-out (cloud Claude Code + OpenClaude-on-Termux + Omnara mobile front).
Drop install + auth notes here after first run.

---

## Local LLM API + Open Wiki CLI

An "LLM Wiki" (Karpathy-style persistent AI memory system) has three layers: raw sources
(untouched originals), the wiki (AI-generated interlinked Markdown), and a schema file
(`CLAUDE.md`/`AGENTS.md`) telling the AI how to maintain it. This section covers running
that locally on Termux, with a local LLM serving an OpenAI-compatible API.

**Important**: this material originated from an AI-generated research conversation and the
code in it was NOT reliable as-is — several commands were broken or referenced non-existent
packages. The commands below are corrected. Don't hand a user raw AI-generated setup output
for this topic without this pass of scrutiny — see the 2026-08-08 section below for a fresh,
much more severe example of the same failure mode (a Gemini transcript inventing a specific
nonexistent Claude Code voice-mic bug).

### Critical path: get a local LLM API running in Termux
```bash
# 1. Base packages
pkg update && pkg upgrade -y
pkg install -y git cmake clang make

# 2. Build llama.cpp from source (there is NO prebuilt `llama-cpp` Termux package)
git clone https://github.com/ggml-org/llama.cpp
cd llama.cpp
cmake -B build
cmake --build build --config Release -j"$(nproc)"

# 3. Download a GGUF model to your device (e.g. via browser to /sdcard/Download/),
#    then start an OpenAI-compatible server
./build/bin/llama-server -m /sdcard/Download/your-model.Q4_K_M.gguf -c 4096 --host 0.0.0.0 --port 8080
```

**2026-08-08 addendum**: this repo's own `llama.cpp` checkout additionally needs
`-DGGML_HEXAGON=OFF` (the NPU/Hexagon backend needs a Hexagon SDK that isn't installed —
fails with `HEXAGON_SDK_ROOT` CMake error otherwise) and a workaround for the bundled web
UI's build step trying to download a nonexistent Hugging Face bucket asset — see "Native
dependency build workarounds" below, "llama-server web UI build" entry.

Simpler alternative if you don't want to compile anything — Ollama IS a real Termux package:
```bash
pkg install -y ollama
ollama serve &
ollama pull qwen2.5-coder:7b
```

### Verify it's alive
```bash
curl http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"local-model","messages":[{"role":"user","content":"ping"}],"max_tokens":5}'
```
A JSON response with an assistant message means it's working. "Connection refused" means the
server process isn't listening — check for a crash or a bad model path.

### Installing the Open Wiki CLI
```bash
pkg update && pkg upgrade -y
pkg install -y nodejs git
npm install -g openwiki
```
Then `openwiki --init` inside your wiki repo folder. Provider defaults to cloud (OpenRouter);
**`OPENWIKI_PROVIDER` and `OPENWIKI_MODEL_ID` must both be set** (env var or the persisted
`~/.openwiki/.env`) or it falls back to OpenRouter even if a local llama-server is running and
correctly configured — this bit the user directly on 2026-08-08 (see below).

### Corrections made vs. the original AI-generated notes
- `pkg install llama-cpp` doesn't exist → build from source with cmake.
- whisper.cpp: `pkg install ... wave-play ...` isn't real, clone URL was truncated → use
  `https://github.com/ggml-org/whisper.cpp.git`, build with `-DGGML_NO_OPENMP=ON` (avoids an
  Android thread-crash issue). Binary is `build/bin/whisper-cli`, not `./main`.
- `termux-microphone-record` output isn't a format whisper.cpp/sherpa-onnx accepts directly →
  needs `ffmpeg -ar 16000 -ac 1 -acodec pcm_s16le` conversion first.
- Voice→LLM→voice pipelines built with raw string interpolation + `grep`/`cut` parsing break on
  quotes/newlines in transcribed speech → use `jq -n` to build the request, `jq -r
  '.choices[0].message.content'` to parse the reply.
- Multi-step install commands (`openwiki`, `docling`) flattened into one broken line in AI-
  generated source material → split into separate commands (`pkg upgrade` swallows anything
  chained after it as arguments).

---

## 2026-08-08 session: voice/STT pipeline debugging, native dependency workarounds

Long session (~3 hours on the voice/STT thread alone). Documenting honestly, including what
**did not** get resolved — per user instruction, this is not a highlights reel.

### Claude Code's built-in `voice:pushToTalk` — ultimately unresolved in this session
Claude Code ships a native voice push-to-talk binding (default key `space`, `Chat` context).
Got the underlying audio capture working, but **never got a reliable keybinding for it on this
device — every approach tried failed for a different reason**:

- ❌ **Hold spacebar** (the default). Android's soft keyboard (Gboard) intercepts a long-press
  on the spacebar for its own "switch keyboard" gesture before it ever reaches the terminal.
  Not fixable from Termux/Claude Code's side.
- ❌ **`meta+k`** (tap ALT on Termux's extra-keys row, then tap `k`). *Appeared* to work for an
  unrelated zsh test (`Alt+B` = backward-word) — but that only worked because Termux's ALT
  button injects a raw ESC byte independent of the following keystroke, and zsh's readline
  reconstructs `ESC`+letter = Meta+letter from two separate bytes arriving close in time. Claude
  Code's Ink-based input parser does not reconstruct this the same way from a touchscreen tap
  with real timing gaps — the two bytes arrive as separate events, not a chord.
- ❌ **`ctrl+k`** (tap CTRL on the extra-keys row, then tap `k`). Confirmed dead at the raw byte
  level: piped through `cat -v`, tapping CTRL then `k` produced a literal `k`, not `^K`. Unlike
  ALT, Termux's CTRL extra-key button does not reliably apply as a true modifier to a keystroke
  typed via the separate soft keyboard.
- ❌ **`tab`** (plain, no modifier). Never got a clean test — collided with existing
  autocomplete/suggestion-accept behavior, and by the time it was retried the user had
  reasonably lost patience with the whole approach.

**If revisiting this**: the working theory is that any two-part chord requiring a tap on
Termux's extra-keys row *and* a separate tap on the main keyboard is fundamentally unreliable
here due to touch timing — a real hardware keyboard, or a single unmodified special key already
present as its own extra-keys button (no second tap needed), are the more promising directions.
Don't re-attempt `meta+k`/`ctrl+k` without a different input method.

### What actually got built instead: standalone voice→clipboard script
`~/bin/voice-transcribe.sh` — records via `termux-microphone-record`, blocks on Silero VAD
(`aesop/deploy/phone/vad_monitor.py`, tail mode) for real end-of-speech detection instead of a
fixed timer, transcribes via `aesop/deploy/phone/stt_process.py`, copies result to clipboard,
vibrates + toasts. Triggered via a `termux-notification` button (`--button1-action`, must use an
**absolute path**, not `~` — untested whether tilde expansion was the actual first-attempt
failure or something else, never fully isolated).

**Status: NOT confirmed working end-to-end with real speech by the user.** Verified only via:
(a) STT engine correctness against a bundled sample WAV with known transcript (exact match), and
(b) a self-test using `termux-tts-speak` for acoustic loopback through the phone's own
speaker/mic, which was inconclusive (VAD hit its 60s timeout, never detected the TTS audio as
speech — likely too quiet/wrong audio path, not a pipeline bug, but never proven either way).
**Next session: get a real confirmation from the user speaking into it before trusting this
path.**

### Real bugs found and fixed in `aesop/deploy/phone/`
These were breaking the *existing* voice pipeline (`openwiki`'s Ctrl+R/Ctrl+S voice mode uses
the same `stt_process.py`, so was equally broken until this session):
- `stt_process.py`: `stream.accept_waveform(seg.samples)` — sherpa-onnx's API requires
  `accept_waveform(sample_rate, waveform)`, not just the waveform. Two separate broken copies of
  this exact bug existed in different scripts.
- `stt_process.py`: requested `uncached_decode.onnx` / `cached_decode.onnx`, but the actual
  model files on disk are `uncached_decode.int8.onnx` / `cached_decode.int8.onnx` (int8-suffixed,
  matching the encoder). `File doesn't exist` at runtime.
- `stt_process.py`: called `sherpa_onnx.read_wave()`, which does not exist in this installed
  sherpa-onnx version (1.13.4) — only `write_wave`. Fixed by reading the WAV manually via the
  stdlib `wave` module + numpy, same approach used elsewhere in this codebase.
- `vad_monitor.py`: `onnxruntime` was not installed in the debian proot Python environment (only
  `sherpa_onnx` was) → `ModuleNotFoundError`. `pip install --break-system-packages onnxruntime`
  in the proot fixed it.
- `boot.sh`: `tee`'d the llama-server log to `/tmp/llama-server.log` — **Termux has no real
  `/tmp`**, only `$PREFIX/tmp` (`/data/data/com.termux/files/usr/tmp`). Silent permission-denied
  failure on every run. Fixed to use `${PREFIX}/tmp/llama-server.log`.

### Real mic input for Claude Code's voice mode: PulseAudio had no microphone source
Claude Code's voice mode shells out to `sox`, which wasn't installed, **and** even after
installing it, `pactl list short sources` showed only `OpenSL_ES_sink.monitor` (a loopback of
*output* audio) — no real microphone source existed. Fix:
```bash
pkg install sox
pactl load-module module-sles-source
pactl set-default-source OpenSL_ES_source
```
Verified with a real `sox` recording showing a non-flat waveform (not just digital silence).
**Persisted across restarts** via `$PREFIX/etc/pulse/default.pa.d/mic-source.pa` (this directory
is the documented, non-package-owned extension point — don't edit `default.pa` directly, it's
package-owned and `pkg upgrade` will overwrite it):
```
load-module module-sles-source
set-default-source OpenSL_ES_source
```
Confirmed by killing and restarting pulseaudio — the source loads automatically.

### Native dependency build workarounds (Android/Bionic has no prebuilt wheels for most ML/native packages)
Android/Termux (`aarch64-linux-android`) is not a `manylinux` platform — PyPI essentially never
ships prebuilt wheels for it, forcing from-source builds that frequently break in ways unrelated
to the actual package. Two techniques used this session, both real:

**1. Install inside `proot-distro login debian` instead of fighting the from-source build.** A
plain Debian aarch64 proot is a `manylinux`-compatible glibc target — the exact same PyPI
package that fails to compile on native Termux typically has a working prebuilt wheel there.
Used for `graphifyy` (24 hard-pinned tree-sitter language grammar dependencies, several with
real from-source bugs — wrong/missing internal headers, an upstream sdist packaging bug in
`tree-sitter-php` missing a shared file) and `code-review-graph` (`watchfiles`/`maturin`, a Rust
build failing with `Text file busy` under Termux's environment).
```bash
proot-distro login debian --bind "$HOME:$HOME" -- bash -c "
  python3 -m venv /root/venvs/<name>
  /root/venvs/<name>/bin/pip install <package>
"
```
Then wrap as a native command so it's invisible that it's running through proot:
```bash
#!/data/data/com.termux/files/usr/bin/bash
exec proot-distro login debian --bind "$HOME:$HOME" -- \
  /root/venvs/<name>/bin/<name> "$@"
```
❌ **Killed guess**: a first version of this wrapper omitted `cwd` handling. `proot-distro login`
always starts in the proot's own `/root`, **ignoring** whatever directory the wrapper was invoked
from — even with `--bind "$HOME:$HOME"`. Any tool that operates on "the current directory"
(`graphify .`, `code-review-graph install`) silently ran against an empty `/root` instead of the
real project, with no error. **Fix — pass the real cwd through explicitly**:
```bash
#!/data/data/com.termux/files/usr/bin/bash
exec proot-distro login debian --bind "$HOME:$HOME" -- env MYTOOL_CWD="$PWD" bash -c \
  'cd "$MYTOOL_CWD" && exec /root/venvs/<name>/bin/<name> "$@"' _ "$@"
```

**2. Vendor missing internal C headers when a from-source build is unavoidable.** Hit this
building `graphifyy`'s tree-sitter grammar deps natively before switching to the proot approach:
`tree-sitter-json`'s bundled `parser.c` needs `tree_sitter/parser.h`, which isn't shipped by
Termux's `tree-sitter` package (only `api.h`) and isn't installed by `pip install tree-sitter`
either (only present in the sdist, not the built wheel). Fix: `pip download --no-binary :all:`
the `tree-sitter` sdist, extract `tree_sitter/core/lib/src/*.h` (the whole directory, not just
`parser.h` — deeper deps like `TSFieldMapSlice` live in `language.h`), copy to
`~/.local/include/tree_sitter/`, build with `CFLAGS="-I$HOME/.local/include"` (note: `CPATH` did
**not** get inherited into `uv tool install`'s isolated build subprocess — `CFLAGS` did).
⚠️ **ABI-version-sensitive**: the tree-sitter core headers must match the ABI the specific
grammar package's pre-generated `parser.c` was built against. tree-sitter 0.26.0's headers were
missing `TSFieldMapSlice` entirely (renamed/removed upstream); tree-sitter 0.24.0's headers had
it. If a grammar fails with an "unknown type" error after vendoring headers, try an older
`tree-sitter` core version's headers, not a newer one.

**3. `llama-server` web UI build tries to download a Hugging Face bucket that doesn't exist.**
This repo's `llama.cpp` build downloads its bundled web UI from
`huggingface.co/buckets/${HF_BUCKET}/resolve/...`, but `HF_BUCKET` defaults to empty — guaranteed
404/401. `tools/ui/CMakeLists.txt`'s priority-1 path: if `tools/ui/dist/index.html` already
exists, it's used as-is, skipping both the npm build and the HF download. Fix: drop a minimal
placeholder `index.html` there before building — but `llama-ui-embed` (the tool that bundles the
UI into the binary) hard-validates a specific manifest of asset filenames and will fail if any
are missing (`loading.html`, `manifest.webmanifest`, `sw.js`, `build.json`, `version.json`, a
`bundle*.js`/`bundle*.css` pair, a `workbox*.js`) — create empty/placeholder files for all of
them, not just `index.html`. Also needs `-DGGML_HEXAGON=OFF` (no Hexagon SDK installed) and
`-DGGML_OPENMP=OFF`.

**4. npm-installed CLI tools with `#!/usr/bin/env node` shebangs fail on Termux** —
`/usr/bin/env` doesn't exist (Termux's real path is `/data/data/com.termux/files/usr/bin/env`).
Symptom: `bad interpreter: /usr/bin/env: no such file or directory`. Fix:
```bash
termux-fix-shebang /data/data/com.termux/files/usr/bin/<binary-name>
```
(Termux ships this exact tool for exactly this problem — don't hand-patch the shebang.)

**5. `npm install -g` silently skips native postinstall scripts** (npm's script-allowlisting
security gate) — packages with real native build steps (esbuild's platform binary fetch,
`@parcel/watcher`'s native build, `koffi`'s prebuilt-binary fetch) will install without error but
**hang or fail silently at runtime** with no indication the skipped scripts were the cause. If an
npm-installed server/tool hangs indefinitely on first run with no error, check for this before
assuming a code bug:
```bash
npm install -g --allow-scripts=<pkg1>,<pkg2>,... <package>
```
npm prints the exact package list to allow in its own warning output after a normal install —
use that list verbatim.

### Killed guesses (this session)
- ❌ Assuming `~` would expand correctly in a `termux-notification --button1-action` string.
  Switched to an absolute path defensively; never actually proved `~` was the failure.
- ❌ Assuming a Gemini-generated technical claim was accurate because it was specific and
  confident. A separate Gemini transcript claimed "the official claude-code core package relies
  on an automated microphone initialization routine that forces an instant system microphone
  check at boot" as the cause of voice-mode failure — fully fabricated; the real cause (missing
  `sox`, no PulseAudio mic source) was found by actually testing, not by pattern-matching a
  plausible-sounding Android/audio explanation.
- ❌ Trying `uv tool install <pkg>` with `CPATH` set to point at vendored headers. Not inherited
  by the isolated build subprocess. Use `CFLAGS` instead.
