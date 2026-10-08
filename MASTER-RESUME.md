# MASTER-RESUME (auto-generated, do not hand-edit)

Every base repo's `RESUME.md` from its `main` branch, rebuilt by
`.github/workflows/master-files.yml` whenever one of them changes.
Edit the repo's own `RESUME.md`, never this file.

---

## NovAExorpus  (`RESUME.md` @ a440343)

Session files: [[AGENTS]] · [[PENDING]] · [[MEMORY]] · [[MAP]] · [[NAMING-CANON]]

### RESUME.md — Session Ledger (rewritten every session)

Repository: NovÆxorpus (`c10vis-poem/NovAExorpus`, PUBLIC). Private files removed 2026-10-05; history not yet erased (item 0b).
**Last session: 2026-10-04/05** (phone, Claude Code, Opus 5.5, session `edd68643`, started in `~`).
It covered the vault privacy cleanup, the master-files workflow, AGENTS.md only, Hyperion-XI, the wiki corpus search and the wiki-admin agent draft.
Reports you can open: `Documents/Session-reports/2026-10-05/` (01 = wiki search results).

#### NEXT SESSION — START HERE
The Stop gate requires a status for each numbered item: `resume-item <n> done|blocked "<evidence / what's needed>"`.

0. **Fix the master-files token, then prove it works.** The pings and builds work, but `VAULT_DISPATCH_TOKEN` can't open PRs ("Resource not accessible by personal access token"). The operator makes a token that has **Contents + Pull requests: read and write** on NovAExorpus (or a classic token with `repo`) and re-sets it in all 7 repos (zsh: `read -rs "T?token: "`, then the `gh secret set` loop, then `unset T`). Then run the Master files workflow once and check that `MASTER-AGENTS.md` / `MASTER-RESUME.md` have real content.
0b. **Repo history (operator runs; Claude Code's safety check blocked it as irreversible):** old commits still hold the removed private files. To erase them: `gh repo rename NovAExorpus-old -R c10vis-poem/NovAExorpus`, create a fresh public `NovAExorpus`, push today's `main` as a single commit, re-set the secret, re-point GitSync, then `gh repo delete c10vis-poem/NovAExorpus-old`. Ask Claude to prepare the exact commands.
1. **Grill session** (`wiki-admin`, Pocock chain typed by the operator: `/setup-matt-pocock-skills` → `/grill-with-docs` → `/to-spec` → `/to-tickets` → `/implement`). Inputs: the PRIORITY ONE docs (`_#Repository-layout.txt` + `Master_dumbass_plan-session/`), `Documents/Session-reports/2026-10-05/`, the wiki-admin agent draft (`~/wiki-admin/AGENTS.md`), PENDING "Added 2026-10-05".
2. **Vault cleanups awaiting the operator's yes** (PENDING "Added 2026-10-05"): the conflict copies, `WebView/`, the empty files, `_quarantine/` + `qairt_/` out, the Documents write-guard hook.
3. **NPU work, one model at a time WITH the operator** (`docs/NPU-FINDINGS-2026-10-02.md` §4): reboot, check the clock caps, InternVL 2B first. Carried over, not started.
4. **Housekeeping** (overdue): recaps rollup, 7-repo branch audit, observation review (0022–0025 new), cloud billing / VM retirement, ~22 GB disk.

#### STATE (verified 2026-10-05)
- **Privacy:** personal memory files, every copy of the unfiled-designs "Device Stack" doc, a subscriptions list and a billing CSV were removed from GitHub (PR #34). Old commits still hold them (item 0b). One saved Google page with embedded keys is gitignored (device only). Originals: `Documents/private-memory/` (outside the vault).
- **Master files:** `.github/workflows/master-files.yml` + `tools/build_masters.sh` build MASTER-AGENTS/RESUME from every base repo's main. They're triggered by each base repo's `notify-vault.yml`; no timer. `MASTER-CLAUDE.md` is retired; the phone post-commit hook is removed.
- **AGENTS.md only** in all 6 base repos + `~/wiki-admin` (Claude Code reads it natively). The Stop gate checks it at wrap-up, along with MEMORY.md per touched repo and the PENDING update.
- **Hyperion-OXiLm → Hyperion-XI** (repo + clone).
- **Wiki toolkit (chosen 2026-10-02):** OpenWiki for Claude Code, obsidian-wiki, wiki-compiler (+ nocode, anydoc, NotebookLM, graphify, Obsidian skills). The wiki lives in this vault. The wiki-admin agent is a DRAFT.
- **Launchers:** `wiki-admin`, `nvaex`, `nvaex-all` (all 7 repos read/write).
- **Device:** `Documents/Zip/` = exact vault backup (15 GB); nested mirror moved to `Documents/NovAExorpus-nested-mirror/`.
- **Public toolkit repo** `c10vis-poem/NvAEx-agentk` (MIT, plugin `nvaex`, skill `subagent-protocol`).

#### DECISIONS 2026-10-05
- PRIORITY ONE: `_#Repository-layout.txt` + `Master_dumbass_plan-session/`. The restructure is grill work; `__RESUME.md/` dissolves into the 00–10 layout. The device vault ends up an exact mirror of this repo.
- Documents outside the vault stays outside; never pull it into the vault.
- No CLAUDE.md in repos; the only one is the user-level `~/.claude/CLAUDE.md`.
- RESUME.md is the handoff: no separate handoff docs.
- The master files rebuild only on change, never on a timer.
- `file_administrator.yaml` / `oracle_helpdesk.yaml` are wrong; real roles come from the grill.
- Replies to the operator stay short.

#### OPEN ITEMS, IN ORDER
1. The START HERE items above.
2. The APK session: `cd ~/agent-stack && claude --resume 125f2d23-df2c-4a1b-823c-45acfa0cf8af` (package IDs `com.aethx.aesc` / `com.clovix.aeyre` awaiting confirmation).
3. NvAEx-agentk: the operator creates the GitHub org; then transfer the repo in as `NvAEx-agentk/skills`.
4. wiki-admin decisions 2b–2e (Obsidian skills loading twice, OmniGlyph, Render MCP, delete `~/.openwiki/`).
5. Everything else in `PENDING.md`.

#### RESUMING ON THE OTHER ACCOUNT (same phone)
Sessions are stored on the phone: `claude auth logout`, then `claude auth login`, then `cd <start folder> && claude --resume <id>`.
This session: `cd ~ && claude --resume edd68643-a1df-46c4-a17b-3ef5a61d291f`.

#### HANDOFF SOURCES
Read this session: this RESUME (old) + PENDING, `_#Repository-layout.txt`, all of `Master_dumbass_plan-session/` (00–13), `docs/WIKI-ADMIN-GUIDE.md`, `WRAP-UP.md`, `stop-gate.sh`, `git-gate.sh`, `regenerate_masters.sh`, the base repos' CLAUDE/AGENTS/MEMORY files, the Claude Code memory docs (AGENTS.md section), the 11 reader reports, the GitSync plugin settings.
Not read directly: most of `__RESUME.md/` and `Drive_sync/` (the readers covered the usable artifacts; chats only listed), `planner.md` (reader A), docs 00–05.

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
