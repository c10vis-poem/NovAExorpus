# Remote access to the phone's agent sessions and dashboards (2026-10-23)

Read-only research. Nothing installed, no config changed. One side effect: running `adb devices` started the local adb daemon (tcp:5037); it lists no devices.

## What is actually on the phone (checked with dpkg/command -v today)
- Installed: adb (android-tools 37.0.0p1-3), tmux 3.8, openssh 10.6p1 (sshd + ssh), termux-x11-nightly 1.03.01-6, tigervnc 1.16.2, x11vnc 0.9.17, node, python3, proot-distro with `debian` and `ubuntu`.
- NOT installed: tailscale/tailscaled CLI (the Tailscale on the phone is the Android app only, per operator), ttyd, code-server, websocat.
- Running now: no tmux server (`tmux ls`: no server), sshd not seen in `ps`. `adb devices` empty (Wireless debugging not paired).
- Available to install (apt-cache policy): ttyd 1.7.7-5, code-server 4.141.0, gotty 1.10.0-1. No Termux `tailscale` package (only `tailcat`).
- ~/.ssh already has id_ed25519, authorized_keys (contents not read).
- Tablet: I cannot see it. Skill table (~/.claude/skills/android-termux-operator/SKILL.md:22) says "Tablet, DroidDesk Debian = desktop: VS Code, browser, GUI tools". Vault planner.md (NovAExorpus/__RESUME.md/__Builder-Guide_Directory-/Master_Dumbass_config/planner.md:1372-1376, 1896-1912) is a planning chat about installing DroidDesk; it is not proof the tablet has it installed. Treat "tablet has DroidDesk Debian + Tailscale" as operator-stated, unverified here. DroidDesk README (~/repos/NvAEx-DroidDesk/README.md:46-50,118-121) says desktop runs on `DISPLAY=:0` in Termux:X11 on the same device.

## 4. Plain-words map (read this first)
- Tailscale = the private network. It gives every device a 100.x.y.z address and a name; devices see each other as if on one Wi-Fi, from anywhere. Needs to be ON (VPN key icon) on BOTH phone and tablet.
- tmux = keeps a terminal alive on the phone even if you close the window, and lets a second screen attach to the same one. Claude Code must be STARTED inside tmux to be shared this way; a Claude already running in a bare terminal cannot be moved into tmux.
- ttyd = turns one terminal command (here: `tmux attach`) into a web page. Runs on the phone. You open it from any browser.
- sshd (Termux) = the phone accepting SSH logins. Alternative to ttyd, needs an SSH client (the tablet's Debian has `ssh`).
- Claude Remote Control = Anthropic's own bridge: claude.ai/code in any browser shows your running local session. No Tailscale needed (outbound only).
- X11 / Termux:X11 = a graphical desktop drawn on the SAME device that runs it. It is NOT how you reach the phone. DroidDesk Debian = the tablet's own Linux with a desktop and browser. It is not a mirror of the phone: the phone's Debian proot and the tablet's Debian are two separate installs. Debian does not "automatically appear"; the tablet's DroidDesk shows only what is installed on the tablet.
- What runs where: PHONE = Claude Code, tmux, ttyd (or sshd), dashboards, Tailscale app. TABLET = Tailscale app + any browser (Android Chrome or the DroidDesk Debian browser) + optionally Debian terminal for ssh/notebooklm login.
- Each time on the tablet: turn Tailscale on -> open a browser -> go to `http://<phone-tailscale-name-or-100.x-ip>:7681` -> enter ttyd user/password -> you are in the tmux session with Claude. (Phone side must have started tmux + ttyd, see Q3.)
- Note: DroidDesk's processes use Android's VPN like any app, so the Debian browser should reach 100.x addresses once the Tailscale app is connected. Not verified on this tablet; test with the Android browser first.

## 3. Tablet gets into a phone session from a browser
Option A (recommended): tmux + ttyd over the tailnet. Needs one install (approval card first): `pkg install ttyd`.
```
# PHONE, Termux (not proot). 1) hold the phone awake
termux-wake-lock
# 2) start Claude inside tmux (a=attach-or-create, session named claude)
tmux new -A -s claude
claude                       # run inside; detach with Ctrl-b then d
# 3) in a SECOND Termux session: serve that tmux session as a web page
ttyd -W -p 7681 -c operator:CHANGE-ME-LONG-PASSWORD tmux new -A -s claude
# 4) find the phone's tailnet address: Tailscale app -> this device -> 100.x.y.z (or MagicDNS name)
```
```
# TABLET: Tailscale ON, browser:
http://100.x.y.z:7681        # log in with operator / the password
```
- ttyd flags (from https://github.com/tsl0922/ttyd): `-p` port (default 7681), `-W` allow typing (read-only by default), `-c user:pass` basic auth, `-i` bind interface, `-b` base path, `-O` check origin. Verify with `ttyd --help` after install; I could not confirm a Termux install note on that page.
- Several browsers attached to `-A -s claude` all see the same screen (phone terminal and tablet at once).
- Security: Tailscale encrypts device-to-device (WireGuard), so plain http over the tailnet is acceptable. But ttyd binds all interfaces by default, so it is also reachable on the phone's Wi-Fi LAN. The password in `-c` is the only gate there. Use a long password; stop ttyd when not needed (Ctrl-c). Do not port-forward it on a router.
- Tradeoff: touch typing on a web terminal is fiddly (Ctrl/Esc keys); battery use; ttyd dies when Termux is killed (keep wake-lock, set Termux + Tailscale to "Unrestricted" battery).

Option B: SSH. Termux sshd listens on 8022 (not 22).
```
# PHONE, Termux: (key login; authorized_keys exists already)
sshd                      # starts on port 8022
whoami                    # your Termux username, e.g. u0_a538
# TABLET Debian terminal:
ssh -p 8022 u0_a538@100.x.y.z
tmux new -A -s claude     # attach to the same session
```
Tradeoff: strongest auth (keys), but needs a terminal app on the tablet and the tablet's pubkey appended to the phone's `~/.ssh/authorized_keys`.

Option C: Claude Remote Control (no tunnel). Docs: https://code.claude.com/docs/en/remote-control
```
# PHONE, inside the running Claude Code session:
/remote-control          # alias /rc ; or start fresh:  claude remote-control   |  claude --remote-control
# TABLET: open https://claude.ai/code  -> pick the session in the list (or scan the QR)
```
- Needs a claude.ai subscription login (Pro/Max/Team/Enterprise; API keys unsupported; not with ANTHROPIC_BASE_URL pointing at another host, e.g. OmniRoute). That last point may block it here: check env before relying on it.
- Gives chat UI, not a shell, and not dashboards. Works from any browser with no Tailscale.

## 2. "Agentic OS website" URL openable from any browser
Simplest, works with what is installed: any web dashboard (a node/python server on the phone) listening on 0.0.0.0:PORT is reachable from every tailnet device at `http://<phone-100.x-ip>:PORT`. Put ttyd on one port, the dashboard on another, and a small index page linking both.
```
# PHONE, Termux: example static index + dashboards (python3 is installed)
cd ~/some-dashboard-dir && python3 -m http.server 8080 --bind 0.0.0.0
# TABLET/any tailnet device: http://100.x.y.z:8080
```
- `tailscale serve` (HTTPS, a *.ts.net name, tailnet-only): syntax `tailscale serve --https=443 http://localhost:8080` per https://tailscale.com/kb/1242/tailscale-serve ; `tailscale funnel` publishes to the PUBLIC internet instead (needs a `funnel` attribute in the tailnet policy; avoid for an agent terminal). The Serve page does not mention Android, and https://tailscale.com/docs/install/android mentions no CLI/serve/funnel. Not found by those two pages = Android app serve support unconfirmed. Termux has no tailscale package (apt-cache). The official userspace route is `tailscaled --tun=userspace-networking` (https://tailscale.com/kb/1112/userspace-networking/) but you would need a tailscaled binary from a source I did not verify, and a second tailnet node name; do not start there.
- "Any browser" over the open internet (not on your tailnet) requires Funnel or a Cloudflare tunnel; Remote Control (Q3-C) already gives any-browser access to the session safely. Recommendation: tailnet URL for dashboards, claude.ai/code for any-browser chat.
- Auth: tailnet-only is the default security; add a token/basic auth to every dashboard anyway (Python http.server has none).

## 1. ADB/Chrome DevTools into Chrome Dev on this phone
What it gives: a script/agent on the phone drives and reads Chrome Dev tabs (dashboards you have open there) via Chrome DevTools Protocol. Docs: https://developer.chrome.com/docs/devtools/remote-debugging (manual forward: `adb forward tcp:9222 localabstract:chrome_devtools_remote`, check `http://localhost:9222/json`).
```
# PHONE: Settings > Developer options > Wireless debugging ON (Wi-Fi must be connected). Tap "Pair device with pairing code": note PORT_P, CODE.
# Termux (native):
adb pair localhost:PORT_P          # enter the 6-digit CODE
adb connect localhost:PORT_C       # PORT_C = the port on the main Wireless debugging screen (differs from PORT_P)
adb devices -l                     # must show the phone as "device"
# Find Chrome Dev's socket name (Chrome stable is chrome_devtools_remote; Dev's name is NOT in the docs):
adb shell cat /proc/net/unix | grep -i devtools
# Forward (use the exact name printed, e.g. chrome_devtools_remote or chrome_devtools_remote_<pid>)
adb forward tcp:9222 localabstract:chrome_devtools_remote
curl -s http://127.0.0.1:9222/json/version      # round-trip test: must print JSON
```
- Chrome Dev must be open. If the socket has a `_<pid>` suffix (seen when several Chrome-family browsers run), forward that exact name. Wireless-debug port changes on every toggle/reboot; pairing is a one-time step.
- Clients: Chrome DevTools MCP (Google): https://github.com/ChromeDevTools/chrome-devtools-mcp ; its Android doc (https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/debugging-android.md, marked experimental) uses `npx chrome-devtools-mcp@latest --wsEndpoint=ws://127.0.0.1:9222/devtools/browser/`. The ws URL needs the id from `/json/version` ("webSocketDebuggerUrl"); the doc's trailing-slash form is as written, check against your curl output. Playwright `chromium.connectOverCDP("http://127.0.0.1:9222")` also works in principle (Playwright treats Chrome-for-Android CDP as best effort).
- Claude Code's playwright / browser-use plugins: they failed to connect this session (cause not diagnosed). Even when healthy they launch their own browser; pointing them at 127.0.0.1:9222 means editing the plugin MCP args (a config change, approval first). Cleaner: add chrome-devtools-mcp as its own MCP server.
- "Android MTP plugin": not found by my probes (I did not search the installed plugin list thoroughly; MTP is the USB file-transfer protocol and does nothing for browsers). The operator likely means Chrome DevTools MCP or an ADB MCP; ask which.
- Tablet reaches dashboards without CDP: just open the dashboard's tailnet URL (Q2). CDP is for the AGENT on the phone to see the phone's browser, not for you to see it from the tablet. (Chrome's own `chrome://inspect` on the tablet could also remote-inspect the phone, but only over USB/adb, not Tailscale, unless you adb connect over the tailnet: unverified.)

## 5. NotebookLM login (fork: ~/repos/notebooklm-py, HEAD 00b2bd50 "fix(auth)... (#2504)" 2026-10-22; I did not run `gh repo sync`, do that before any install per your fork rule)
Why not the phone: interactive `notebooklm login` needs Playwright + a downloaded Chromium (~170 MB) (docs/installation.md:34, 96, 109-113). Headless/no-display sandboxes are told to log in on a workstation and copy the file (docs/installation.md:125). Playwright Chromium on Termux/proot Android: no evidence found; unverified.
```
# TABLET, DroidDesk Debian desktop terminal (needs a display for the Google sign-in window; Python 3 + venv)
python3 -m venv ~/nlm && . ~/nlm/bin/activate
pip install "notebooklm-py[browser]"     # (docs/installation.md:231-233) prefer your synced fork checkout: pip install "~/path/to/notebooklm-py[browser]"
playwright install chromium
notebooklm login                          # Chromium opens; sign into Google; wait for it to close (installation.md:113, 663-670)
notebooklm auth check --test --json       # need "status":"ok" and token_fetch true (installation.md:116)
ls -l ~/.notebooklm/profiles/default/storage_state.json   # <- the file lands here (installation.md:116, 669)
```
```
# Copy to the phone over the tailnet (phone: run `sshd`; this is installation.md:237-239 pattern but port 8022)
ssh -p 8022 u0_a538@100.x.y.z 'mkdir -p ~/.notebooklm/profiles/default'
scp -P 8022 ~/.notebooklm/profiles/default/storage_state.json u0_a538@100.x.y.z:.notebooklm/profiles/default/storage_state.json
# PHONE, Termux: lock it and test (no browser needed for normal use, installation.md:210, 397)
chmod 600 ~/.notebooklm/profiles/default/storage_state.json
notebooklm auth check --test --json
# alternative one-off: notebooklm --storage /path/storage_state.json list   (installation.md:139)
```
- The file is a bearer credential for your Google account (installation.md:145): 0600, never commit, and note this vault repo is PUBLIC, so keep it out of the vault and out of Drive sync.
- Cookie snapshots go stale: another active client supersedes them within ~10 minutes (installation.md:242-247). For a phone that runs unattended, use the master-token path instead: `pip install "notebooklm-py[browser,headless]"` then `notebooklm login --master-token --account you@gmail.com`, ship `master_token.json`, then `notebooklm login --master-token-refresh` on the phone (installation.md:250-264, 300-315, 400).
- `--browser-cookies chrome` (read cookies from an installed browser) needs the `[cookies]` extra (installation.md:122, 399); no evidence it can read Chrome Dev on Android, so skip it.
- On the phone itself (fallback): phone already has termux-x11-nightly, tigervnc, x11vnc and a Debian proot, so a Playwright login inside the proot desktop is conceivable, but not verified, and Google may flag it. Try the tablet first.

## Gaps
Not read: tablet state, Tailscale app settings (MagicDNS/HTTPS enabled?), phone's authorized_keys contents, Chrome Dev's actual socket name (adb not paired), whether playwright/browser-use plugin failures have a fixable cause, an "Android MTP plugin" referent. Tailscale Android CLI/serve support: neither Tailscale page I fetched mentions it.

## Sources
- https://developer.chrome.com/docs/devtools/remote-debugging
- https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/debugging-android.md
- https://tailscale.com/kb/1242/tailscale-serve
- https://tailscale.com/docs/install/android
- https://tailscale.com/kb/1112/userspace-networking/
- https://github.com/tsl0922/ttyd
- https://code.claude.com/docs/en/remote-control
- https://github.com/teng-lin/notebooklm-py (local fork docs/installation.md)
