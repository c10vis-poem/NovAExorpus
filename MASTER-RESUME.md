# MASTER-RESUME (auto-generated, do not hand-edit)

Every base repo's `RESUME.md` from its `main` branch, rebuilt by
`.github/workflows/master-files.yml` whenever one of them changes.
Edit the repo's own `RESUME.md`, never this file.

---

## NovAExorpus  (`RESUME.md` @ 7ee160f)

Session files: [[AGENTS]] · [[PENDING]] · [[MAP]] · [[GRILL-MANIFEST]] · [[NAMING-CANON]]

### RESUME.md — Session Ledger (rewritten every session)

Repository: NovÆxorpus (`c10vis-poem/NovAExorpus`, PUBLIC), the master wiki and vault.
**Last session: 2026-10-02** (phone, Claude Code, Opus 5.5, personal account). It covered the NPU server's vision path, the device cleanup, H1–H7 on aesop-xi, the wiki-admin toolkit and the OpenWiki retirement. Full ledger: `~/.claude/session-work/2026-10-02/SESSION-LOG.md`.

#### NEXT SESSION — START HERE
The Stop gate requires a status for each numbered item: `resume-item <n> done|blocked "<evidence / what's needed>"`.

0. **FIRST: fix GitSync (stuck in a "remote changing" loop 2026-10-02; nothing since 04:38 reached GitHub) and push today's vault work.**
1. **Planning session in the wiki-admin agent.** Start it with `wiki-admin`. Activate the wiki toolkit (obsidian-wiki `/wiki-setup` once: decide where `OBSIDIAN_VAULT_PATH` points) and the LLM Wiki agent (`/llmwiki-*`). The operator runs the Pocock chain by typed slash command: `/setup-matt-pocock-skills` → `/grill-with-docs` → `/to-spec` → `/to-tickets` → `/implement`. Guide: `docs/WIKI-ADMIN-GUIDE.md`.
2. **Close the wiki-admin open decisions** (guide §10): memory link for `~/wiki-admin`; the Obsidian skills loading twice; OmniGlyph attach point (user-wide proxy vs OmniRoute engine); Render MCP build (Go + API key); delete `~/.openwiki/` (1.1 GB).
3. **Restart the NPU work one model at a time WITH the operator**, per `docs/NPU-FINDINGS-2026-10-02.md` §4. Reboot first and check the CPU clock caps. First add InternVL 2B: the X Elite bundle ran 27.5 tok/s here.
4. **Housekeeping (due since end of week):** roll up `_recaps/`, repo audit (unmerged branches), observation-log review (open: 0001, 0002, 0004–0009, 0012, 0015, 0016, 0019–0021; 0018 is an empty file), cloud billing, disk bloat (~22 GB: uv/npm caches, Gemma 12B and E2B copies; PENDING "afternoon").

#### STATE (verified 2026-10-02)
- **Enforcement:** H1–H7 live user-wide on the phone *and* attached to aesop-xi (`.claude/settings.json` → `deploy/phone/hooks/run-hook.sh`; stands down where the global copy exists). Operator override = `#skip-enforce`, typed by the user only.
- **What loads where** (Claude Code docs, skills page): an attached folder (`--add-dir`, e.g. this vault) loads its `.claude/skills/`, `commands/` and `agents/` only, never its settings, plugins, hooks or MCP. Corpus-wide skills therefore go in `NovAExorpus/.claude/skills/` (as copies; shared storage can't hold links). NotebookLM is there now.
- **wiki-admin** (`~/bin/wiki-admin` → `~/wiki-admin` + vault attached):
  - Project-scope plugins: obsidian-wiki (fork AEsops-obsidian-wiki), OpenWiki for Claude Code (fork NvAEx-openwiki-for-claude-code), wiki-compiler (fork llm-wiki-compiler-NvAEx).
  - `/llmwiki-*` = the nocode commands with a prefix, so they don't clash with obsidian-wiki's `/wiki-*`.
  - anydoc (`~/bin/anydoc`, runs in the Debian proot); NotebookLM.
  - Global: graphify 0.9.73 (fork), Obsidian skills (fork), Pocock (25/35 skills load; the planning chain is typed-slash only).
  - Plugin scripts needed `termux-fix-shebang` on Termux. Redo it after plugin updates.
- **OpenWiki retired:** MCP removed, CLI uninstalled, vault `AGENTS.md` block removed. `~/AGENTS.md` and `~/CLAUDE.md` deleted by the operator (backup in `$TMPDIR/ow`).
- **NPU server** `npu-serve <name>` → `127.0.0.1:18181/v1`, GenieX v0.7.1. All 6 models accept images (OpenAI `image_url`). Decode on the clock-capped phone: smolvlm2 23 · internvl3.5-4b QAIRT ~16 (AI Hub 16.0–16.4) · gemma-4-e4b 9.7 · internvl3.5-8b 5.9 · qwen3.5 0.8B/2B ~3 (CPU-placed Q5_K weights). Guide: `docs/NPU-SERVE-USER-GUIDE.md`.
- **Installed for later, not on:** OmniGlyph proxy (`~/bin/omniglyph`, v1.4.0 from the fork; it's a proxy, not MCP; Fable 5 only by default); Render MCP fork cloned (render.com service management; needs Go).
- **Cleanup:** about 9 GB freed (byte-identical copies, `~/kokoro` JS package, Gemma E2B + MTP). Kokoro v1.1 deleted by mistake; v1.0 kept (the v1.1-zh card says it isn't a strict upgrade).

#### DECISIONS 2026-10-02
- Wiki toolkit lives in a separate launch folder so normal sessions stay lean. Skills meant for every session go in the vault.
- Same-named skills: obsidian-wiki owns `/wiki-*`; nocode becomes `/llmwiki-*` with its own wiki tree in `~/wiki-admin`; wiki-compiler is used by its full plugin names.
- Cleanup rules: dedup by model identity (name/chip/version + inner weights + byte-diff count), not by whole-file hash; never cut the newer version; ambiguous assent ≠ approval of separate questions.
- Fix small defects in-session; "later" needs a named reason.
- Commands for the operator: `!` works only at the Claude Code prompt, one per line. For a plain terminal, give them without `!`.

#### OPEN ITEMS, IN ORDER
1. The START HERE items above.
2. Ship (this wrap-up): aesop-xi `feat/npu-serve-model-switching` (7 commits, incl. 1627b3f hooks and 751fb79 docs) and the older `feat/stop-gate-resume-enforce` worktree branch.
3. Operator: `notebooklm login`.
4. npu-serve: tool calls, multi-image; Kokoro TTS script fix.
5. The grill-session agenda (unchanged): H5/H6 per-tool blocks, H7 auto-classifier, post-task flagging, keyword false triggers, Hermes/dsh/terrestrial-brain, OmniRoute config, PR #18, wiki agent home (now partly answered by wiki-admin).
6. Everything else in `PENDING.md`.

#### HANDOFF SOURCES
Read this session (post-compaction):
- Code and config: `~/tools/geniex-serve/{shim.c,server.py,models.json}`, `geniex-v0.7.1.h` (VLM sections), GenieX `cli/cmd/geniex/infer.go` (inferVLM), `docs/en/models/supported.mdx` (local bundle), `~/bin/npu-serve`.
- Repos and toolkit: aesop-xi hook files and settings, every SKILL.md of the OpenWiki plugin, obsidian-wiki ingest/query/lint (first ~45 lines each), `.env.example`, `SETUP.md`, the llm-wiki-nocode BOOTSTRAP / CLAUDE / commands, anydoc and NotebookLM SKILL.md, the wiki-compiler hooks, OmniGlyph README sections + package.json + build script, Claude Code docs (skills page, add-dir section).
- State files: vault RESUME.md, PENDING.md, `docs/NPU-FINDINGS-2026-10-02.md`, `LOCAL-AI-GUIDE.md` (to line 160), `ENFORCEMENTS.md`, hooks README, `WRAP-UP.md`, memory files edited, the GitSync state.

Not read: the full obsidian-wiki skills (40) and docs, the Render MCP README, OmniGlyph docs beyond the README, wiki-compiler commands, the rest of aesop-xi `CLAUDE.md`, vault docs 00–05.

---

## aesop-xi  (`RESUME.md` @ 72fda7f)

### RESUME.md — Session Ledger

Repository: `aesop-xi` (orchestration repo)
Last session: 2026-10-02 (phone, Claude Code). Full ledger: `~/.claude/session-work/2026-10-02/SESSION-LOG.md`. Master handoff: vault `RESUME.md`.

#### WHAT LANDED (branch `feat/npu-serve-model-switching`, ships at /wrapup)
- `4a0b3a7`, `567d941`: npu-serve model switching (`deploy/phone/geniex-serve/models.json` registry; the request's `model` picks it).
- `34fb58a`: VLM path. Image input for GGUF + mmproj and for QAIRT VLM bundles. All 6 registry models answered an image correctly. InternVL3.5-4B QAIRT decodes at 15.4–17.1 tok/s (AI Hub S25: 16.0–16.4).
- `106a296`: npu-serve start script no longer hangs when piped; waits 240 s for big models.
- `995a7ba`: default model path → `Models/gguf/Qwen3.5-2B-Q4_0.gguf` (the `~/downloads` copy was a byte-identical duplicate, removed).
- `1627b3f`: H1–H7 attached to this repo (`.claude/settings.json` → `deploy/phone/hooks/run-hook.sh`). Tested: stands down where the global copy exists; otherwise the repo copy runs (secret-guard blocked a hook-skip commit).
- Wrap-up docs: CLAUDE.md (hook section), MEMORY.md, PENDING.md, this file.

#### STATE
- Server: `npu-serve <name>` → `http://127.0.0.1:18181/v1`. Guide: vault `docs/NPU-SERVE-USER-GUIDE.md`.
- Speeds measured on a clock-capped phone; not trustworthy until the caps are explained (vault `docs/NPU-FINDINGS-2026-10-02.md`).

#### NEXT
1. Add InternVL 2B to models.json (the X Elite bundle ran 27.5 tok/s, prefill 1,528 on this v79 phone; compare with the 8 Elite bundle).
2. Tool calls in npu-serve; multiple images per message.
3. NPU restart one model at a time with the operator (vault RESUME START HERE).

#### Sources read this session (for this repo)
`deploy/phone/geniex-serve/{shim.c,server.py,models.json}`, `deploy/phone/bin/{npu-serve,npu-ask,ai-web}`, `deploy/phone/hooks/{settings.hooks.json,README.md,stop-gate.sh (head)}`, `.claude/settings.json`, CLAUDE.md (section list + hook grep), MEMORY.md, PENDING.md, the old RESUME.md (first 30 lines). Not read: the rest of CLAUDE.md, `docs/`, `skills/`, `tools/`.

---

## novus-aexenti  (`RESUME.md` @ 81a9088)

### RESUME.md

Repository: `novus-aexenti`

Authority: NovÆxorpus Master Canon Specifications

---

## NovAExopia  (`RESUME.md` @ f0e993d)

### RESUME.md

Repository: `NovAExopia`

Authority: NovÆxorpus Master Canon Specifications

---

## Hyperion-XI  (`RESUME.md` @ 7dab022)

### RESUME.md — horizons-ui

**2026-09-15:** Repo wiped and recreated empty. Old history (38 PRs,
"Novus Agenti / Omni Claw") archived in `raw-databank/horizons-ui-full-history.bundle`.
Nothing built yet — this is session zero.

---

## novus-aesc  (`RESUME.md` @ 6cc2734)

### RESUME.md — novus-aesc (Æsc)

**Status:** Scaffold. Nothing runs yet. Build order item #2 (see `docs/BUILD-ORDER.md`), blocked on #1 (DroidDesk install) per operator sequencing — do not re-sequence.

#### Current state

- Repo layout, docs (`CLAUDE.md`, `README.md`, `STACK-MAP.md`, `docs/BUILD-ORDER.md`, `protocol/README.md`, `salvage/README.md`) already written and operator-declared — not touched here.
- `salvage/` — 5 extraction targets defined (NPU loader, ADB loopback, Chromium integration, terminal render, model router), none pulled from `horizons-ui` yet (all unchecked in `salvage/README.md`).
- `manifest.jsonl` — empty (`entries: []`).
- Known blocker: the Watchdog daemon doesn't survive Android process management (MIUI/One UI/Android 13+ kill it). Fix is a `ForegroundService`, not yet built.

#### Prior art not yet reviewed (per `docs/BUILD-ORDER.md`)

`NovAExorpus/unresolved.md` item 10: a bridge daemon (`deploy/phone/bridge/aesopd.py`), a supervised `llamad` daemon with real NPU/Hexagon offload (`deploy/phone/daemons/`), `protocol/bridge-protocol.md`, and a `termux-helper` skill already exist in `aesop-xi` — merged from `origin/claude/wiki-quinn-npu-local-m1crql`, never reviewed. May already cover most of this repo's task. Read before writing new daemon code.

#### Document 05 vs. this repo's actual plan — flagged, not reconciled

`05_FEDERATED_FILE_TREE_TOPOLOGY_MASTER.md` sketches this repo's contents generically:
`src/main/java/com/horizons/ui/adb/`, `npu_watchdog/`, `scripts/`, `process-isolation/`,
`lmk-mitigation/`, `wireless-adb/`. This repo's actual operator-declared plan is more
specific and different in shape: `laptop-trick-tunnel/` (ADB loopback), `npu-watchdog/`
(underscore vs. hyphen naming also differs), `protocol/`, `salvage/` with 5 named targets.
Did not force this repo's layout to match Document 05's sketch — the existing plan is more
detailed and explicitly operator-declared ("Do not re-sequence"). Needs the user's call on
whether Document 05's sketch should be updated to match reality, or whether this repo should
be reshaped to match Document 05.

#### Second master Drive folder — not found

Per Document 05, this repo's content source is `___Lex-Novi-Æxentis-Copiæ/--•💻_TERMUX_[>_]_main.` and `.../Reverse-Engineering` (both subfolders of a second master Drive folder). That folder has not been shared with this session as of this pass — checked `sharedWithMe = true and mimeType = 'application/vnd.google-apps.folder'`, only `__NovÆxorpus_LIVING_MASTER_CANON`, `22-Hooks`, `Termux ECC`, and `__NovÆxorpus(NÆX)` are shared. Nothing to pull from it yet.

#### Next

1. Read the `aesop-xi` prior art above before writing any daemon code.
2. DroidDesk install (build order #1) is the actual blocker, not this repo.
3. `ForegroundService` rewrite for the Watchdog whenever salvage starts.

---

## novus-aeyre  (`RESUME.md` @ 578a0f4)

### RESUME.md — novus-aeyre

**Last updated:** 2026-09-07
**Branch:** `restructure/drive-file-tree`

#### Current state

Voice: working scaffold, confirmed end-to-end via `--demo` (TTS → speaker →
STT round-trip, text matched). Currently lives in `aesop-xi/voice-engine/`
under Termux + Debian proot — temporary, moves here and gets wiped from
`aesop-xi`. Live mic loop not yet verified — only `--demo` has run.

Vision: not started. No code, no design beyond the stub directories.

Two real bugs already found and fixed, documented in `README.md` — don't
rediscover them: Moonshine STT's ~10s silent-failure ceiling, and the
two-part PulseAudio/proot audio bridge fix (ALSA-over-Pulse routing +
client-side SHM disabled).

#### What was done this session

Checked this repo's Drive source material (`Æsc&Æyre` subfolder of
`___Lex-Novi-Æxentis-Copiæ`, per `05_FEDERATED_FILE_TREE_TOPOLOGY_MASTER.md`'s
14-subfolder mapping table, entry `Reverse-Engineering`). Confirmed via
`AUDIT_LEX_NOVI_AESOP_XI.md` that this material was already fully synthesized
into `NovAExopia/README_NOVAEXOPIA.md` and
`NovAExopia/01_SOVEREIGN_NODE_AND_APK_TOPOLOGY.md` — out of scope for this
repo. The raw subfolder itself is not shared with this Claude Code session
(only the audit summary is), so nothing further was retrievable to place
here. Added the missing section-kit files (`agent.md`, this file,
`unresolved.md`) per the corrected per-repo layout in
`NovAExorpus/project_novae_xorpus_repo_layout_correction.md` (see project
memory, not committed to this repo).

#### Next

- Extract the voice engine from `aesop-xi/voice-engine/` into `app/audio/`,
  `app/vad/`, `app/stt/`, `app/tts/` per the planned layout in `README.md`.
- Verify the live mic loop before building further on it.
- Start the vision path — no design exists yet; check `aesop-xi` and
  `NovAExopia` first for anything already decided.
