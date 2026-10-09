---
title: "Getting the local LLM + voice pipeline working_  (every time after a reboot)_"
source: "Drive_sync/Original_Corpora/___Lex-Novi-Æxentis-Copiæ (1)/--•🖥️_TERMUX_[__ ]_main./Getting the local LLM + voice pipeline working_  (every time after a reboot)_.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

Getting the local LLM + voice pipeline working
  (every time after a reboot)

  1. Open Termux.
  2. Run: bash ~/aesop/deploy/phone/boot.sh
  This starts your local Qwen 3.5-9B model in the
  background (in a tmux session called llm). Wait
  for it to print "AESOP Edge Online" — takes ~20
  seconds.
  3. Run: ow
  This launches OpenWiki, already pointed at your
  local model. Press Ctrl+R to record a voice
  message, Ctrl+S to stop and transcribe — that's
  local STT/TTS (Kokoro + moonshine), no cloud.
  4. If you ever want to switch to GLM/OpenRouter
  instead of local: type /provider inside ow,
  arrow to the one you want, hit Enter.

  That whole pipeline is independent of Claude
  Code — it's your own app.

  Testing Claude Code's own built-in mic (this
  session, right here)

  1. Fully close Termux (swipe it out of recent
  apps — don't just background it), then reopen
  it. This is required for the new
  ESC/TAB/CTRL/ALT button row to actually show up
  above your keyboard.
  2. Relaunch claude in Termux.
  3. Look for that new row of small buttons right
  above your regular keyboard.
  4. Tap ALT, then tap K (that sends "meta+k",
  which is what triggers push-to-talk now —
  holding physical spacebar will never work since
  Android's keyboard eats that gesture first).
