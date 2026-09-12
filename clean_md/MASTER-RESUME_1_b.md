1. **Installation of OpenWiki.** Get it running with an OpenRouter key + GLM-5.2
   model hooked in. Note: `~/openwiki` is a real custom fork
   (`c10vis-poem/openwiki`, upstream `langchain-ai/openwiki`) on branch
   `claude/wiki-quinn-npu-local-m1crql` with genuine NPU/voice commits — not
   vanilla upstream. It had uncommitted changes (accidentally deleted
   `.gitignore`/`README.md`) restored 2026-08-29; separately there's both
   `package-lock.json` and `pnpm-lock.yaml` present, worth resolving which
   package manager is actually canonical before relying on either.
2. **Installation of DroidDesk** on both the phone and the tablet — not yet
   started on either device. Confirmed: DroidDesk itself renders via Termux:X11
   directly, not VNC (VNC is only an optional external-monitor bridge in its own
   docs). Decided: standalone real desktops on each device independently, not
   phone->tablet mirroring — scrcpy (already forked) was considered and
   explicitly ruled out for this purpose.
3. **Piping of the voice line.** Real-time engine confirmed working via
   `--demo` (see below) — this step is wiring it into actual use (the LLM
   callback stub, live mic verification), not building it from scratch.
4. **Installations of ECC, Pocock skills, and honey-for-devs.** Note: ECC is a
   ready-to-go plugin (`.claude-plugin/plugin.json` in `~/repos/ECC-aesop`)
   never actually installed via the plugin system — confirmed against
   `~/.claude/plugins/installed_plugins.json` (only 3 unrelated plugins listed).
   One-command install once reached.
5. **Grill session** (Pocock's grill-me skill).
6. **On-device help desk.**
7. **Salvaging the existing APK as a terminal daemon** — ties to the planned
   Æsc/Æyre daemon APKs (see "What this is" above).

Explicitly separate from this list, deferred without a fixed slot: the
HTTP/WebSocket server for remote voice-engine invocation (extension point noted
in the `aesop-voice-pipeline` skill, not built). See `unresolved.md` for the full
durable backlog (obsidian-skills into vault, notebooklm login path, OpenWiki
upstream PR, open architectural decisions, T3 hardware bring-up, Tailscale status,
the OmniRoute/OB1/ReasoningBank routing question).
