# MASTER-RESUME (auto-generated, do not hand-edit)

Every base repo's `RESUME.md` from its `main` branch, rebuilt by
`.github/workflows/master-files.yml` whenever one of them changes.
Edit the repo's own `RESUME.md`, never this file.

---

## NovAExorpus  (`RESUME.md` @ 0f29e0c)

Session files: [[AGENTS]] · [[PENDING]] · [[MEMORY]] · [[MAP]] · [[NAMING-CANON]]

### RESUME.md — Session Ledger (rewritten every session)

Repository: NovÆxorpus (`c10vis-poem/NovAExorpus`, PUBLIC).
**Last session: 2026-10-08** (phone, Claude Code, Opus 5.5, session `34c3e229`, started in `~`).
It covered: eson + honey hook fix, PDF move to the keep (1,046 → 12 in the vault), NovA-Corpus condensed swap, vault tools fixed, hooks H2 blocking / H8 CI / change-log review, NvAEx-Recaps (recaps + secrets), LiteDoc, grill inputs, PR triage.
Everything from that session, with every report: `~/.claude/session-work/2026-10-08/` (start with `WRAPUP-QUEUE.md`).

#### How to run this session: subagents in tandem
Every START HERE item below is a **workstream** written so one orchestrator can hand it to a subagent unchanged. Standing order (`~/.claude/CLAUDE.md`): independent workstreams run in parallel; each subagent writes its progress file FIRST (`~/.claude/session-work/<date>/agent-<topic>.md`: Plan / Last action / Findings / Blocked) and updates it after every step. The orchestrator answers "where is X" from those files. Nothing ships mid-session: every change is recorded by `change-log.sh`; at `/wrapup` the operator reviews it and types `/ok push`.
Parallel-safe groups: **A** = items 2, 3, 4 (GitHub + repos) · **B** = items 5, 6 (vault files; never two vault-moving agents at once) · **C** = item 1 (operator-led) · item 0 first, alone.

#### NEXT SESSION — START HERE
**Operator, 2026-10-09: items 0, 3, 4 and 5 have been carried over for more than a week. The next session finishes them FIRST, completely, as parallel subagents, before any other work (grill and NPU included). "Partly done" is not a status: each item ends done with evidence, or blocked on something only the operator can do, named exactly.**
The Stop gate requires a status for each numbered item: `resume-item <n> done|blocked "<evidence / what's needed>"`.

0. **Carry-over check (first, alone; haiku).** Open `~/.claude/session-work/2026-10-08/WRAPUP-QUEUE.md`. Every `[ ]` line not shipped at the 2026-10-08 wrap-up becomes part of items 2–6 below; mark `[x]` what the `## Shipped` section of `_recaps/2026-10-08-34c3e229.md` proves shipped. Done = each open line assigned to an item.
1. **Grill session (operator-led; wiki-admin).** The operator types `/ask-matt` → `/setup-matt-pocock-skills` → `/grill-with-docs` → `/to-spec` → `/to-tickets` → `/implement`. Single input list: `~/wiki-admin/GRILL-INPUTS.md` (PRIORITY ONE docs, 2026-10-05 reports, 2026-10-08 additions: repos/ mirrors, 2x2 converter/checker design, OmniRoute compression + vision plugin, observation-review staged skills, aesop-xi PR #18 contract, hooks H1–H8 review). Agents assist; they do not decide.
2. **NPU job queue, then NPU runs (opus orchestrator; cloud subagents + Fable advisor).** Restart the plan in `~/.claude/session-work/2026-10-08/agent-npu-queue.md` (stopped at step 0 by a usage limit): jobs/results in `NvAEx-Recaps/npu/`, `npu-run` + `npu-queued` daemon on the phone, `npu/ORCHESTRATOR.md`, one real test (Qwen3.5-0.8B, npu + CPU baseline). Rules: `~/.claude/NPU-ON-DEVICE.md` (read fully; no "needs a computer"), `docs/NPU-FINDINGS-2026-10-02.md` §4. Qwen 3.5 only. Then the orchestrator runs the model queue (InternVL 2B first) with no operator present. Done = test job result with NPU-proof lines + CPU baseline.
3. **PRs and CI (sonnet).** Source: `~/.claude/session-work/2026-10-08/pr-triage-report.md` + the operator's answers in `WRAPUP-QUEUE.md`. Merge: NovA-terrestrial-brain#3, termux-app#2, termux-packages#6, termux-gui-bash#1 (adopt; add CI first). Fix then merge: honey #1/#2 + NovA-skills#1 (required check `check` matches no job), obsidian-skills#1. Close: aesop-xi#33, openwiki#2/#3, OB1#1, ai-hub-merovingian-models-#1. Leave open: aesop-xi#18 (grill), Horizon-s-home-grid#1 + Hyperion-XI#4 (3-APK build). ECC: not touched. Then improve H8 `ci-ready.sh` to check required names against real job names. Done = triage table all closed/merged/left-by-decision.
4. **Repos (sonnet).** (a) `repos/` folder in this vault = live mirrors of the 6 base repos, built by `master-files.yml` on each `notify-vault`; retire MASTER-AGENTS/MASTER-RESUME + `tools/build_masters.sh`; delete the stale `AEsc/ AEsop-Xi/ AEyre/ NovAExopia/ NovusAExenti/ projects/` folders after a unique-content check (unique → keep). Needs `VAULT_DISPATCH_TOKEN` set in all 7 repos (operator). (b) `ship-session.sh` copies each recap into `NvAEx-Recaps/recaps/<repo>/` for every repo touched; CI + branch protection on NvAEx-Recaps. (c) Renames (last): 19 `NovA-`/`NoVa-` repos → `NvAEx-<rest>`, `aesop-xi` → `Aesop-Xi`, local folders + every hook/launcher/`nvaex-repos.sh` path; delete `c10vis-poem/NovA-Corpus` + `~/repos/NovA-Corpus` (unique content already saved); delete the 44 old branches. (d) Fix two `ship-session.sh` gaps found at the 2026-10-08 wrap-up: a worktree that never appears under "Repos touched" in the recap is skipped (AEthX-AEsc `pending-fold` in `.wt-AEthX-AEsc-pending` was missed); `~/wiki-admin` is skipped as "origin not a c10vis-poem fork" (check its origin and the ORIGIN_RE match). Done = mirrors present + recaps flowing + renames verified by a hook test run + both gaps covered by a ship test.
5. **Vault cleanup (sonnet; group B).** Fold the vault's 12 `*unresolved*` files into `PENDING.md`, then delete them. The 12 PDFs still in the vault (fail: fused tokens): re-run through the 2x2 design once the grill builds `check2.py`. Report (do not delete) the 82 exact duplicates in `clean_md/`. Also: GitSync Portal stalled since 2026-10-02 (operator suspects a zip); the 2026-10-08 sync was done by hand (PR #44), so reset its `local-sync-state.json` base to `03e65f3` (or reset the plugin) and find what it chokes on. Done = 0 unresolved files; PENDING has their items.
6. **Observations (sonnet; group B).** 29 logged, 13 open (0001, 0005–0007, 0012, 0015–0017, 0023, 0024, 0028, 0029, + 0018 empty). Staged: `skill-updates/2026-10-08/`. Fix 0001/0006/0015 in the operator's forks (task-observer = `aesop-task-observer`, honey = `NoVa-honey-for-devs`). Proposed rules become hooks in `aesop-xi/hooks/` only after checking H1–H8 (obs 0029). Done = each open observation actioned, parked with a condition, or handed to the grill.

#### STATE (verified 2026-10-08)
- **Hooks (live in `~/.claude/hooks/`, sources `aesop-xi/hooks/`, moved from `deploy/phone/hooks/`):** H2 `sync-on-use.sh` now BLOCKS until the fork is synced (17 tests); `change-log.sh` records every change, `review-changes.sh` + `/ok push` gate every push (20 tests); H8 `ci-ready.sh` blocks wrap-up / auto-merge without CI + required checks; `documents-guard` merged into change-log (nothing blocked). `test-ship-v2.sh` fails 14/18 on origin/main too (pre-existing).
- **NvAEx-Recaps (private):** `recaps/<7 repos>/`, `recaps/ROLLUP.md`, sops+age secrets `secrets/secrets.enc.yaml`, CLI `nvaex-secret` (get/set/list/push/edit). Only the phone's age key can decrypt: add a second key. No CI yet.
- **Vault tools:** `tools/clean.py` + `tools/check.py` fixed (vault-root layout, mutool, `type: condensed`, sources in the keep, canary); `.migrate/` complete (pickle → JSON BM25; `dedup.py` runs `git rm`: operator approval); `generate_jsonl_markers.py` = independent chunk cross-check. LiteDoc (fork, v3.3.0 CLI) installed: `litedoc`. `mutool`, `sops`, `age`, `eson` installed.
- **Keep (`Documents/Merovingian's_keep/`):** `vault-pdfs/` (970 PDFs), `_salvage/NovA-Corpus/` (+ `originals/`, HomeGrid.kt), `vault-moved/_quarantine/` (3.0 GB).
- **Disk:** 136 GB free (17.7 GB caches/duplicates + 8.3 GB Qwen3-VL bundles deleted).
- **Cloud:** project-alchemist-490416 kept; billing off, $0.

#### DECISIONS 2026-10-08
- PDFs live only in the keep unless no text version exists.
- `unresolved.md` retired: open items go to each repo's PENDING.md. "canon", POINTER.md and the `NovA-` prefix are removed whenever touched.
- The vault gets live repo mirrors (`repos/`); no MASTER-* files.
- Two converters + two checkers on four PDF engines (MuPDF, pdf.js, pypdf, Poppler); no tool checks its own output.
- Qwen models: Qwen 3.5 only. Render MCP dropped (forks kept). Context-as-image through OmniRoute.
- Nothing is pushed until the operator reviews the session's change list (`/ok push`).

#### OPEN ITEMS, IN ORDER
1. START HERE above.
2. APK session: `cd ~/agent-stack && claude --resume 125f2d23-df2c-4a1b-823c-45acfa0cf8af`.
3. NvAEx-agentk org transfer (operator creates the org).
4. Everything else in `PENDING.md`.

#### HANDOFF SOURCES
Read this session: old RESUME.md + PENDING "Added 2026-10-05", `~/.claude/hooks/README.md`, `stop-gate.sh`, `ship-session.sh`, `session-ledger.sh`, `enforce-prompt.sh`, `sync-on-use.sh`, `NPU-ON-DEVICE.md`, `NPU-FINDINGS-2026-10-02.md` §4, `01-WIKI-SEARCH-RESULTS.md` §3, `WIKI-ADMIN-GUIDE.md` §6/§10, OmniGlyph + OmniRoute READMEs, every subagent report in `session-work/2026-10-08/`.
Not read: the PRIORITY ONE plan docs (00–13) beyond file names; `Master_dumbass_plan-session` content; most of `Drive_sync/`.

---

## aesop-xi  (`RESUME.md` @ c0e503a)

### RESUME.md — Session Ledger

#### Next session (from 2026-10-08, session 34c3e229)
- Branches `hooks-to-top-level` (hooks moved to `hooks/`; H2 blocking sync, change-log + /ok push, H8 ci-ready, documents-guard merged) and `raw-condensed` ship at wrap-up (workstream 3/4).
- PR #18 (orchestration contract) stays open for the grill; #33 gets closed.
- Fix: `hooks/tests/test-ship-v2.sh` fails 14/18 on main too. H8: compare required check names with real job names.
- Last of workstream 4: rename the repo to `Aesop-Xi` and every hook path that points at `~/repos/Aesop-Xi`.
Full plan, run as parallel subagent workstreams: vault `NovAExorpus/RESUME.md` START HERE.

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

## NovAExopia  (`RESUME.md` @ 34de88d)

### RESUME.md

#### Next session (from 2026-10-08, session 34c3e229)
- Branch `raw-condensed`: `raw/novaecopia-vincet.md` (condensed, from NovA-Corpus before its deletion); ships at wrap-up.
- The local clone sits on an old branch (`feat/memory-stack-reference-2026-09-15`, merged): switch it back to main (workstream 4).
Full plan, run as parallel subagent workstreams: vault `NovAExorpus/RESUME.md` START HERE.

Repository: `NovAExopia`

Authority: NovÆxorpus Master Canon Specifications

---

## Hyperion-XI  (`RESUME.md` @ 7dab022)

### RESUME.md — horizons-ui

**2026-09-15:** Repo wiped and recreated empty. Old history (38 PRs,
"Novus Agenti / Omni Claw") archived in `raw-databank/horizons-ui-full-history.bundle`.
Nothing built yet — this is session zero.

---

## novus-aesc  (`RESUME.md` @ 6cea451)

### RESUME.md — novus-aesc (Æsc)

#### Next session (from 2026-10-08, session 34c3e229)
- Branch `pending-fold`: `unresolved.md` folded into PENDING.md; ships at wrap-up.
- 7 old local branches whose PRs merged get deleted (workstream 4).
Full plan, run as parallel subagent workstreams: vault `NovAExorpus/RESUME.md` START HERE.

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

## novus-aeyre  (`RESUME.md` @ e030b78)

### RESUME.md — novus-aeyre

#### Next session (from 2026-10-08, session 34c3e229)
- Branch `pending-fold`: `unresolved.md` folded into PENDING.md; ships at wrap-up.
- 4 old local branches whose PRs merged get deleted (workstream 4).
Full plan, run as parallel subagent workstreams: vault `NovAExorpus/RESUME.md` START HERE.

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
