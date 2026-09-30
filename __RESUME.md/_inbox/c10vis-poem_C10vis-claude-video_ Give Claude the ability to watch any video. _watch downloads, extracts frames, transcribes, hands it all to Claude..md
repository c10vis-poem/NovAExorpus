<!-- Converted from c10vis-poem_C10vis-claude-video_ Give Claude the ability to watch any video. _watch downloads, extracts frames, transcribes, hands it all to Claude..pdf — 9 pages -->

## Page 1

C10vis-claude-video
Code Pull requests Agents Actions Projects Wiki Security and quality Insights Settings
Watch 0 Fork 0
# Give Claude the ability to watch any video. /watch downloads, extracts frames, transcribes, hands it all to Claude.
MIT License
0 stars 0 forks 0 watching 1 branch 0 tags Activity
Public repository · Forked from bradautomates/claude-video
m… 1 Branch 0 Tags Go to file T Go to file Add file Code
This branch is up to date with bradautomates/claude-video:main . Contribute Sync fork
| bradautomates and claude chore: release 0.3.2 |  |  | 03ceb42 · yesterday |
|---|---|---|---|
| .agents/plugins | Restructure as a self-contained Agent Skills … | 3 months ago |  |
| .claude-plugin | chore: release 0.3.2 | yesterday |  |
| .codex-plugin | chore: release 0.3.2 | yesterday |  |
| .github/workflows | feat: support only the latest yt-dlp and updat … | yesterday |  |
| docs/images/install | docs: clarify installation paths with desktop … | 2 weeks ago |  |
| hooks | fix: quote plugin root in SessionStart hook | last week |  |
| skills/watch | chore: release 0.3.2 | yesterday |  |
| tests | fix: keep SKILL.md frontmatter within the Ag … | yesterday |  |
| .gitattributes | Implement v0.3.0 reliability fixes and manag … | 2 weeks ago |  |
| .gitignore | chore: keep versioned planning docs out of t … | yesterday |  |
| .skillignore | Restructure as a self-contained Agent Skills … | 3 months ago |  |
| AGENTS.md | fix: keep SKILL.md frontmatter within the Ag … | yesterday |  |
| CHANGELOG.md | chore: release 0.3.2 | yesterday |  |
| CLAUDE.md | Restructure as a self-contained Agent Skills … | 3 months ago |  |
| LICENSE | Initial commit: /watch skill v0.1.0 | 5 months ago |  |
| README.md | docs: point Claude users to Claude Code an … | yesterday |  |
| dev-sync.sh | Restructure as a self-contained Agent Skills … | 3 months ago |  |
  
 
.claude-plugin chore: release 0.3.2 yesterday
.codex-plugin chore: release 0.3.2 yesterday
 
 
 
skills/watch chore: release 0.3.2 yesterday
 
 
 
 
 
CHANGELOG.md chore: release 0.3.2 yesterday
 
LICENSE Initial commit: /watch skill v0.1.0 5 months ago
 
 
README License
# /watch
# Give an agent video evidence: a URL or local file becomes timestamped frames and a transcript. Install it in Claude Code (the desktop app, VS
# Code, or a terminal), or use it with Codex and other Agent Skills hosts. Native captions come first; optional local WhisperX or Groq/OpenAI
# transcription handles videos without captions.

---

## Page 2

### Choose your app
Using Claude? Run Watch in Claude Code. Install it through Claude Desktop and use a Code session, or add it with the plugin commands in VS Code or a terminal. Watch does not work in Claude Chat or Cowork; see why.
Where you use your agent Start here
Claude Desktop — Code Install through Customize — no terminal needed
Codex — desktop app, CLI, or IDE extension Ask Codex to install it — no terminal needed
Claude Code in VS Code Use the extension's plugin window
Claude Code in a terminal Enter the plugin commands
Cursor, Copilot, or another local agent Use the Skills CLI
Claude Chat, Cowork, or a browser app Chat and Cowork don't work; browser apps have limits
Choose one installation method for your agent. If Watch is already installed, go straight to your first video.
### Claude Desktop — Code
1. Open Claude Desktop and click Customize in the sidebar.
2. Select Plugins, open Add, then choose Add marketplace.
3. Choose Add from a repository.
4. In URL, paste the address below. If a picker opens, paste into its search field and select Use for that URL. Click Sync.
https://github.com/bradautomates/claude-video

---

## Page 3

6. Start a Code session and ask it to use the watch skill. Watch does not work in Cowork tasks (why). Continue with your first video.
If you do not see these controls, update Claude Desktop. On a managed account, your administrator may control which plugins you can add. See the official plugin guide.
Screenshots show the installation controls only. Labels may vary slightly by app version.
### Codex
Paste this into Codex's message box in the desktop app, CLI, or IDE extension:
Use $skill-installer to install the watch skill from: https://github.com/bradautomates/claude-video/tree/main/skills/watch
Let Codex finish the installation, then start a new turn or session and ask it to use watch. If the skill does not appear, restart Codex. You do not need Node/npm for this route. See OpenAI's skill installation guide.
Alternative: native Codex plugin installation (desktop and CLI)
Continue with your first video.
### Claude Code in VS Code
1. Open the Claude Code panel in VS Code.
2. Type /plugins into the Claude Code message box to open Manage plugins.
3. Select Marketplaces and add bradautomates/claude-video .
4. Return to Plugins, find watch, and choose Install for you to use it across your projects.
5. Follow any activation or restart message. Then type and select the suggested skill — normally /watch /watch:watch — or ask Claude to use watch by name.
The extension has its own graphical installer; you do not need to switch to a terminal. Its plugin configuration is shared with the local Claude Code CLI. Official VS Code instructions
Continue with your first video.
### Claude Code in a terminal
Open a terminal and start Claude Code with claude . Enter these inside the Claude Code session, one at a time:
/plugin marketplace add bradautomates/claude-video /plugin install watch@claude-video
/watch Follow the activation message. If Watch is not available yet, start a new Claude Code session. Type and select /watch:watch from
autocomplete. Official installation guide
Already at an ordinary terminal prompt?
Continue with your first video.
### Other local agents
For other Agent Skills hosts, install Node.js if needed, then run this in your computer's terminal:
npx skills add bradautomates/claude-video -g --skill watch
Select your agent when prompted, follow the installer's reported destination, then restart the agent. Node/npm is needed for this installer, not for Watch's Python runtime.
You can target an agent explicitly, for example -a codex , but Codex users can use the simpler message-box installation. See the Skills CLI
documentation.

---

## Page 4

### Try your first video
~/.config/watch/.env open in your text editor so you can paste it after GEMINI_API_KEY= and save it yourself. Watch then hands the whole
video — picture and sound — to Google's agentic video model and relays its timestamped answer. YouTube links need nothing else installed. Local files are uploaded to Google and deleted after the answer.
local No key, or a private video? Choose . Watch extracts frames and a transcript on your machine ( ffmpeg + yt-dlp ), exactly as before. Force it any time with --engine local . The walkthrough below uses this no-key path.
1. Give your agent access to a folder containing a short video, such as example.mp4 . Open that folder as your agent's project. Replace the
filename below with your own.
2. Paste this into the agent's message box:
Use the watch skill on example.mp4 in the folder I shared. For setup, choose balanced detail and captions only (none). Summarize what is visible, with timestamps.
3. Let the agent check its tools. If it reports a missing program, follow Missing tools? below, then retry.
Success looks like a timestamped visual summary. This first run needs no transcription API key or local speech model. A local file with speech fallback disabled will not produce a speech transcript. The agent finds its bundled scripts itself; you do not need to locate a plugin-cache folder.
Next, try a public video URL and ask for transcript detail. Native captions can be read without downloading the video. URL access depends on the source and your session's network permissions.
You can add speech transcription afterward. Local WhisperX requires Watch v0.3.0 or later; if your installed copy is v0.2.0, update after the new release is available.
### Missing tools?
Watch uses Python 3.10+, FFmpeg/ffprobe, and current yt-dlp. YouTube also needs a supported JavaScript runtime/EJS setup. Installing the skill gives the agent instructions and scripts; it does not bundle these programs.
First, ask your agent:
Use the watch skill's bundled setup.py to check dependencies in this session. Tell me which tools are missing and help me install them here.
Cloud sessions (such as Claude Code on the web): let the agent check inside its execution environment. Installing FFmpeg with Homebrew on your Mac does not install it inside a cloud sandbox. Package and network permissions may require administrator help. A new cloud task may also need setup again.
Agents running directly on your computer: Watch can install missing media tools through Homebrew on macOS. On other systems it supplies commands. If manual installation is needed, run the appropriate commands in a terminal:
Operating Install commands system
macOS Install Homebrew, then brew install python ffmpeg yt-dlp . The current formula includes Deno/EJS/curl-cffi.
sudo apt install python3 ffmpeg pipx pipx install "yt-dlp[default,curl-cffi]"
, then and pipx
exact , and winget install --id DenoLand.Deno --exact .
Reopen the terminal and agent after installation so they can find the new tools. On Windows, verify Python with python --version or py -3 --version . Watch supports the latest yt-dlp release only, because sites routinely break older ones; it uses the executable available in the
active environment.

---

## Page 5

### Chat, Cowork, and browser apps
Watch works in Claude Code: a Code session in Claude Desktop, or Claude Code installed with the plugin commands in VS Code or a terminal. Codex and other local agents work too.
Surface What to know
Claude Chat Not supported, including uploading watch.skill as a custom skill.
web) block yt-dlp downloads from that environment.
Claude Code on the Uses a cloud environment with its own setup and network settings. The interactive /plugin installer is
web unavailable there. The terminal walkthrough above is for local Claude Code.
ChatGPT/Codex Attaching watch.skill to a chat is not a local Codex installation. Use the Codex installer above; a
browser surfaces public/workspace plugin listing is a separate distribution route.
See the official guides for Claude Code on the web and OpenAI plugin surfaces.
### Choose an engine
Setting Default and behavior
/ : Gemini when a resolves, otherwise . WATCH_ENGINE -- auto GEMINI_API_KEY local gemini without a key is an error before any network call.
engine local never contacts Google.
header; never logged.
WATCH_GEMINI_MODEL gemini-3.7-flash . Free-form, so newer model IDs work without an update.
WATCH_GEMINI_TIMEOUT 600 seconds for the question itself; upload and processing waits are bounded separately.
On a Gemini run, YouTube URLs go to Google directly; other URLs are downloaded with yt-dlp and, like local files, uploaded to Google's Files API, then deleted after the answer (an upload that cannot be deleted expires within 48 hours). / --start --end restrict Gemini to that range. Frame and transcription options ( , , --detail --fps --whisper , …) apply only to the local engine and are listed as ignored. Watch never switches engines on its own: a Gemini failure is reported with its category and you decide whether to rerun with --engine local . The rest of this README describes the local engine.
### Choose a transcription fallback
The first-run wizard asks for your detail preference and fallback backend. Start with none for a quick visual result; choose a speech backend
when you need it. Captions remain first under every choice. Settings persist in the execution environment, so temporary cloud sessions may need setup again.
Backend Requirements and behavior
environment and downloads its models.
| groq | Cloud whisper-large-v3 ; needs GROQ_API_KEY from Groq. |
|---|---|
| openai | Cloud whisper-1 ; needs OPENAI_API_KEY from OpenAI. |
| none | Captions only. Local files and captionless URLs can still provide visual evidence. |
none Captions only. Local files and captionless URLs can still provide visual evidence.
auto Existing 0.2.0 users retain : Groq key first, then OpenAI. No automatic migration to local inference. Explicit --whisper groq|openai|whisperx overrides this run's fallback, while --no-whisper disables all fallbacks and still permits native captions. Those two
flags conflict.

---

## Page 6

Settings live in ~/.config/watch/.env . Enter keys privately there or in the process environment; do not commit them or paste them into
public issues. Cloud-key lookup is provider preference first, then environment → user file → cwd .env for each provider. Explicit providers
never borrow another provider's key. Config files support UTF-8, UTF-8 BOM, and BOM-marked UTF-16; quotes, comments, and literal Windows
paths work without shell expansion. Last assignment wins.
### Managed WhisperX
WhisperX runs wherever the agent executes its scripts. In a local session, inference runs on your computer; in a cloud session it runs on the
cloud host. It avoids a separate transcription API, but cloud execution does not keep audio on your device.
Have the agent run the bundled setup.py --install-whisperx (or --backend whisperx --detail balanced ). It provisions uv if needed,
installs Python 3.12 and WhisperX 3.8.6, and transcribes two seconds of silence to warm the Whisper and Silero caches. No sudo is used by
the installer. The base watch process stays standard-library-only and can use newer Python independently.
| Requirement |  | Guidance |
|---|---|---|
| Free disk | At least 3 GB for the environment, small model, installer cache, and managed Python |  |
| RAM | At least 8 GB ; reference small-model peak process memory was about 2.4 GB |  |
Requirement Guidance
 
RAM At least 8 GB; reference small-model peak process memory was about 2.4 GB
Apple Silicon macOS is verified. Recipes target macOS 13+, Linux such as Ubuntu 22.04+, and Windows 10+ with
CPU/OS PowerShell, but Intel macOS/Linux/Windows installs remain untested. Wheel availability varies by architecture; this is not
a universal compatibility promise.
Network Needed for initial packages and model downloads. Warm caches allow offline inference.
The user chooses based on these requirements; the wizard does not inspect hardware, RAM, disk, or browser sessions.
small cpu int8 Defaults are , , , batch size 8 , with no alignment or diarization. Segment timestamps are retained. In the reference
measurements, small processed 69 seconds of English in 9.6 seconds on an Apple M5 Pro; slower CPUs and longer recordings take more
time.
WATCH_WHISPER_BACKEND=whisperx WATCH_WHISPERX_MODEL=small WATCH_WHISPERX_DEVICE=cpu WATCH_WHISPERX_COMPUTE_TYPE=int8 WATCH_WHISPERX_BATCH_SIZE=8 # WATCH_WHISPERX_LANGUAGE=es # WATCH_WHISPERX_TIMEOUT=1800
WATCH_WHISPERX_BIN ~/.cache/watch/whisperx-venv The installer writes the absolute path. The venv is , with a .deps-ok sentinel and
resolved package list in watch-install.json . Interrupted installs without the sentinel are rebuilt safely. Model caches normally live under
~/.cache/huggingface and ~/.cache/torch/hub ; uv also caches wheels and Python. These are outside the plugin, so updating the skill
does not remove them.
WATCH_WHISPERX_LANGUAGE=es For non-English audio, set the spoken-language hint ( , for example) or try WATCH_WHISPERX_MODEL=large-v3
and rerun the installer. Large-v3 downloads about 2.9 GB and used about 6 GB peak process RAM in the reference measurement. Small can
misidentify non-English speech without a hint. A caption translation request ( --sub-lang ) is never used as the spoken-language hint.
WhisperX 3.8.6's JSON language is unreliable with alignment disabled, so auto-detection is reported as unverified.
Local inference has no default timeout; WATCH_WHISPERX_TIMEOUT accepts positive seconds. Failure or cancellation never switches to cloud
transcription. CUDA is configurable but untested; MPS support is not promised. TorchCodec import warnings on newer FFmpeg are
suppressed for this CLI-decoding path; do not downgrade FFmpeg just for that warning.
### Detail and focus
| Detail |  | Selection | Default cap |
|---|---|---|---|
| transcript | Transcript only; cue frames can be requested explicitly |  | No regular frames |
| efficient | Fast keyframes; uniform fallback when sparse |  | 50 |
| balanced | Scene changes; uniform fallback on nearly static clips |  | 100 |
| token-burner | Scene changes without a count cap; warning above 250 |  | Uncapped |
Detail Selection Default cap

---

## Page 7

WATCH_DETAIL --detail Use for the saved preference or for one run. The /watch examples below are shorthand: in Claude Code plugins, select /watch:watch ; in other hosts, ask the watch skill to apply the same options. Best accuracy is usually with videos under 10 minutes or a
focused interval:
/watch video.mp4 --start 2:15 --end 2:45 /watch video.mp4 --detail efficient --max-frames 30 /watch video.mp4 --detail transcript --timestamps 1:05,2:30
Uniform sampling selects actual source frames across the range, reducing its rate to fit the remaining cap (at most 2 fps). Scene/keyframe selection detects candidates across the range, then samples to the cap. The last selected candidate need not be the last video frame; scene changes do not capture every event. Frame timestamps are source-relative, including focused and fractional seeks.
A 16×16 RGB thumbnail pass removes near-duplicates using mean channel difference. Use --no-dedup for subtle visual changes; tiny thumbnails cannot preserve every code edit. Default images are up to 512px wide and 1998px tall; --resolution 1024 helps with on-screen
text. Image cost depends on the host/model and frame dimensions.
After reading a transcript, the agent can pin “look here” moments with --timestamps . These consume the frame budget first. A caption-only
pass may not download a video; in that case the cue pass uses the URL again. An audio-only download cannot supply cue frames.
### Captions, authentication, and partial results
Auto caption selection uses original-language evidence when available, preferring same-language manual captions before original ASR. It requests at most one track. Unknown provenance is labeled unknown. / --sub-lang CODE WATCH_SUB_LANG chooses an explicit language, which may be a translation.
Authentication is opt-in:
/watch https://example.com/video --cookies /path/to/cookies.txt /watch https://example.com/video --cookies-from-browser firefox
Use one cookie mechanism at a time, or save WATCH_COOKIES_FILE / WATCH_COOKIES_FROM_BROWSER . A cookie file is a read/write jar; yt-dlp
may update it. Browser access can fail due to locked/encrypted stores, especially Chromium on Windows; Firefox is a possible alternative, not a guarantee. Watch never searches browser sessions automatically. Existing yt-dlp proxy, CA, runtime, and authentication configuration remains active when not explicitly overridden.
Fresh download directories prevent stale files from a failed source being reused. Media must complete successfully and report its final path; partial and merge-component files are rejected. Successful captions survive download, decoding, or probe failures. Reports distinguish unavailable evidence, no speech, and failed cloud chunks with missing time intervals. A silent requested interval never triggers fallback just because its captions are outside the range.
Cloud uploads use a 24,000,000-byte file budget with multipart and actual chunk checks. Local WhisperX takes the whole extracted audio file. No automatic provider/client/cookie cycling is performed.
### Updating and troubleshooting
Update Watch using the same method you installed it with, then start a new session:
Installation method Update path
Claude Desktop it. Check the installed Watch version afterward.
Claude Code CLI Enter /plugin update watch@claude-video inside Claude Code and follow the activation message.
Code
video .
Ask Codex to update the existing watch skill from this repository. The installer does not overwrite an existing skill Codex Skill Installer automatically.

---

## Page 8

Installation method Update path
Skills CLI In a terminal, run npx skills update watch -g .
Marketplace auto-update behavior depends on the host and your settings. Updating Watch is separate from updating its media tools.
Keep yt-dlp on its latest release. Update it with its owning installer, then verify the same executable with yt-dlp --version :
Homebrew: brew upgrade yt-dlp
pipx: pipx upgrade yt-dlp
Dedicated Python environment: python -m pip install -U "yt-dlp[default,curl-cffi]"
winget: winget upgrade --id yt-dlp.yt-dlp --exact
yt-dlp -U is not a universal package-manager update command. See upstream installation and EJS guidance.
Ask the agent to run bundled setup.py --json for resolved paths/versions, JS-runtime presence, impersonation targets, and local-backend
watch's Python. setup.py --check is fast, silent on success, and never imports Torch.
Symptom Next step
Check that Watch itself is installed, not just its marketplace. Start a new session and ask for the Watch does not appear watch skill by name.
commands inside local Claude Code.
Two watch skills appear Keep one installation method per host; check for both a plugin and a standalone copy.
Command missing / wrong Ask the agent to check dependencies in the active session, then reopen it after PATH changes. version
Python opens the Store Use an installed interpreter verified by python --version or py -3 --version .
FFmpeg option failure compatibility for older builds.
Missing JS runtime/EJS Update the owning yt-dlp package and follow upstream Deno/EJS setup.
Update yt-dlp to its latest release (see Updating and troubleshooting) and retry once; the agent does 403 / login challenge this automatically. If the 403 persists, read the original error and use explicit authentication only if you have access.
rejected upload service / / too long), a failed upload, a Google-side error, no route to generativelanguage.googleapis.com , or network response / / an unreadable reply. Nothing ran locally; fix the cause or rerun with --engine local .
429 Wait before retrying; the service is rate limiting requests.
Check the environment's network settings or use an accessible local source. Cloud ASR/cold model Explicit hosted egress denial setup still need network access.
Certificate failure Configure the trusted CA/proxy correctly; do not disable TLS verification.
Config parsing / encoding Save as UTF-8 or BOM-marked UTF-16; diagnostic locations never echo credential values.
Set the config to mode 0600. Windows ACLs are not audited. Prefer a Linux-home config in WSL; POSIX permissions warning Windows-mounted storage has different permission behavior.
Local install/inference failure requirements, and wheel compatibility.
### Development and packaging
python3 -m venv .venv .venv/bin/python -m pip install pytest

---

## Page 9

.venv/bin/pytest -q
For a manual install, create the host's skill directory and symlink or copy the whole
SKILL.md or use a directory junction. Do not split from its sibling scripts/
bash skills/watch/scripts/build-skill.sh builds dist/watch.skill
AGENTS.md for repository structure and release rules.
### Data and cleanup
Releases
No releases published Create a new release
Packages
No packages published Publish your first package
Contributors
No contributors
Languages
Python 94.9% Shell 5.1%
Suggested workflows
Based on your tech stack
Django Build and Test a Django Project By GitHub Actions
Pylint Lint a Python application with pylint. By GitHub Actions
Python application Create and test a Python application. By GitHub Actions
More workflows
folder. Windows users can copy the folder
Configure
Configure
Configure
Tests use isolated config homes and synthesized FFmpeg media; no provider keys or live service calls. The offline yt-dlp integration test
requires its CLI. CI runs on Linux, macOS, and Windows with real FFmpeg/ffprobe and gates the tag-triggered release job.
skills/watch/
or add a duplicate command wrapper.
from committed HEAD and refuses tracked dirty changes. Preview
uncommitted code from a temporary staging directory. The bundle includes no planning documents, environments, or model weights. See
WhisperX processes audio in the agent's execution environment: on your computer for local execution, or on the provider's infrastructure for