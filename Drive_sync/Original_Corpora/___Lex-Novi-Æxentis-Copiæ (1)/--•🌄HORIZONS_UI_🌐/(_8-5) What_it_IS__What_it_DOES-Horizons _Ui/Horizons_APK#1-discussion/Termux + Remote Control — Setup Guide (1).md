---
title: "Termux + Remote Control — Setup Guide (1)"
source: "Drive_sync/Original_Corpora/___Lex-Novi-Æxentis-Copiæ (1)/--•🌄HORIZONS_UI_🌐/(_8-5) What_it_IS__What_it_DOES-Horizons _Ui/Horizons_APK#1-discussion/Termux + Remote Control — Setup Guide (1).pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

PERSONAL REFERENCE · SAVE THIS FILE
Termux + Claude Code Remote Control
How to run Claude Code in Termux and drive it from your phone's
browser or the Claude app — plus the one setting that silently
breaks it, and the open bug to watch for if you wrap it in tmux.
01 WHAT THIS ACTUALLY IS
Remote Control is an official Anthropic feature (research preview, all plans).
It connects claude.ai/code or the Claude mobile app to a claude session
running on your phone in Termux. Execution and filesystem access never
leave the device — the web/mobile view is just a window into the same
session.
It is not the same thing as --cloud, which runs Claude Code on Anthropic's
own servers instead of your machine. Remote Control keeps everything local;
--cloud moves everything off-device. Don't confuse the two — the
requirements and flags are different.
02 START IT
# in a real project directory — the trust dialog never saves for $HOME,
# so starting from your home folder means re-confirming every time
cd ~/my-project
# server mode — stays running, prints a session URL,
# press spacebar for a QR code, supports several sessions at once
claude remote-control
# OR: one interactive session, works from your terminal AND remotely
claude --remote-control
# OR: turn it on inside a session that's already running


# OR: turn it on inside a session that s already running
/remote-control
To connect from your phone or another computer: open the printed URL, scan
the QR code straight into the Claude app, or find the session by name at
claude.ai/code — it shows a green dot when the Termux side is online.
03 BEFORE YOU START — FOUR THINGS THAT SILENTLY DISABLE IT
!
You must be logged in with a real claude.ai account, not an API key. Run claude
then /login if you haven't. This is the one that matters most — see the warning below.
!
Start it inside a project folder, not your home directory — the workspace-trust
prompt won't remember a home-directory session.
!
Check your shell profile for DISABLE_TELEMETRY, DO_NOT_TRACK,
CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC, or DISABLE_GROWTHBOOK. Any one
of these silently turns Remote Control off. Unset all four if present.
!
If you've set ANTHROPIC_BASE_URL to point at a proxy or gateway instead of Anthropic
directly, Remote Control won't work — unset it, or use a different terminal for this.
04 THE CONFLICT THAT WILL BITE YOU
READ THIS BEFORE TROUBLESHOOTING ANYTHING ELSE
If you've ever fixed Termux asking you to log in over and over by switching to
export ANTHROPIC_API_KEY=… — that workaround makes Remote Control
impossible. Remote Control checks for a real OAuth login and refuses outright if it
finds an API key instead, with no override.
There's no way to have both "stopped re-auth loop via API key" and "Remote Control
working" at the same time. You need OAuth to actually hold on this device, not
routed around.
05 KEEPING IT ALIVE WHEN YOU BACKGROUND TERMUX


The claude process has to keep running — close Termux (not just switch apps)
and the session ends. To make it survive backgrounding, run it inside tmux:
tmux new -s remote
claude remote-control
# Ctrl-B, then D — detaches. Session + Remote Control connection both survive
# later, to check on it or reattach locally:
tmux attach -t remote
BUT CHECK THIS FIRST
There's an open, unresolved upstream bug reporting repeated re-auth prompts
specifically inside tmux, even with valid stored credentials (anthropics/claude-
code #9903). Test plain claude remote-control outside tmux first. If that stays
logged in cleanly, the bug is tmux-specific on your setup and wrapping it will
reintroduce the loop you're trying to avoid.
06 TROUBLESHOOTING FLOW
If you're stuck in a re-auth loop, work through this in order rather than
guessing at fixes:
1 · Check what's actually stored
ls -la ~/.claude/ right after logging in. Note whether it's there.
↓
2 · Close Termux the way you normally do, reopen, check again
ls -la ~/.claude/ a second time.
↓ file gone?
Yes, it's gone
Something is deleting it on close — check
for a Termux:Boot script, a stray rm in
.bashrc/.profile, or a proot/container
setup that doesn't persist $HOME.
No, still there
The file persists but you're still asked to
log in — the bug is elsewhere (wrong
$HOME being read, a different user
context, or the token itself expiring


Also filed in Horizons-UI: skills/termux-mobile-dev/SKILL.md
