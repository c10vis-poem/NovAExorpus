# NeuroOmni / N0.V4 — Active

## What it is
Multi-agent orchestration project. Repo: `NeuroOmni.Vag-Agenti` under org `M0DU14R-SYSx-inc`.
Key files: `AGENT_GO.md`, `UNIVERSAL_PREFIX.md`, `EXECUTION_BOARD.md`, `builder.system.md`.

## State
- M1.1 STT = DONE
- M1.2 Kokoro TTS = stalled (was on Gemini Code Assist, should move to Qwen Code)
- M2.3 in progress via Claude Code
- Dev environment: Google Cloud Shell Editor, Antigravity IDE + CLI, ARM64 Linux builds. GCP project: `main-catwalk-492516-s7`.
- `N0_V4_ARCHITECTURE.md` and `HORIZONS_UI_ARCHITECTURE.md` exist as sidebar artifacts.
- **Known open contradiction:** Stack B references Supabase; Section 5 rejects it in favor of self-hosted Postgres + pgvector. Needs resolution before further build-out.

## Related, adjacent work
- Termux voice pipeline (llama-server + Gemma 4 E2B QAT + VoxSherpa/Kokoro TTS + talk.sh): built and working. `talk.sh` uses curl → jq → termux-tts-speak. Aider configured but reinstall pending.
- Horizons UI: visual language locked (industrial neo-steampunk, obsidian/violet/copper/cyan), hub-and-spoke hex layout, Orbitron font. Saved as artifact `horizons_ui_v3`.

## Next step
- Resolve Supabase vs self-hosted Postgres+pgvector contradiction.
- Restart aider integration.
- Move M1.2 TTS work from Gemini Code Assist to Qwen Code.
