# PENDING.md — NovAExorpus

Durable cross-session backlog. Not rewritten each session — items persist until resolved or explicitly dropped.

## Routines
last-housekeeping: 2026-10-01
- Roll _recaps/ older than 30 days into a monthly summary, delete the originals
- Audit repos: uncommitted / unpushed / stray branches → merge or discard with the builder
- Review the task-observer observation log
- Check cloud billing (VM disks)
- Builder reminders: (add here)

## Added 2026-10-05
- **Grill session (all of these are drafts/inputs, not decisions):**
  - Vault restructure into the 00–10 layout (`_#Repository-layout.txt`, PRIORITY ONE with `Master_dumbass_plan-session/`). `__RESUME.md/` gets dissolved into it. Draft: `~/.claude/session-work/2026-10-05/VAULT-RESTRUCTURE-PLAN.md`.
  - Where each wiki tool writes in 00–10; `OBSIDIAN_VAULT_PATH`; one manifest schema (6 conflicting ones found); where `Drive_sync/LlmWiki` lands.
  - Wiki-admin agent DRAFT in `~/wiki-admin/AGENTS.md`. The real roles of the files-admin and Oracle agents (`file_administrator.yaml` / `oracle_helpdesk.yaml` are wrong, per the operator).
  - Wiki corpus inventory to build from: `~/.claude/session-work/2026-10-05/WIKI-SYNTHESIS.md` (+ `agent-wiki-{A..K}.md`, incl. each batch's "Chat — mine later" list for extracting scripts/skills from chats).
  - Stop-hook enforcement of the subagent protocol; packaging H1–H7 as installable; the `CLAUDE.md`-trigger design (now AGENTS.md).
- **Vault cleanups awaiting the operator's yes:** delete the 12 `MASTER-*.conflict-android-*` files (Zip has copies); remove `WebView/` (Android browser cache) from the vault and gitignore it; delete the 2 empty files (`Untitled.md`, `.md`); move `_quarantine/` (3 GB) and `qairt_/` (87 MB) out of the vault; a hook that blocks agent writes in Documents outside `01-inbox/` and the pinned root files.
- **Missing tools named in the docs** (not on disk): `compile_manifest.py`, `doc_to_skill_and_tool.py`, `system_housekeeper.sh`, `boot.sh`, `htp_partition_calc.py`, `smart-grep-hook.sh`. The `.migrate` BM25 index uses pickle: replace it.
- **NvAEx-agentk:** the operator creates the GitHub org `NvAEx-agentk`; then transfer `c10vis-poem/NvAEx-agentk` in as `NvAEx-agentk/skills`, add the org front page, update the links. Branch protection after the first CI run.
- **GCP VM:** the operator is leaning toward retiring it. Copy anything needed off first, then delete it (stops the billing; the plaintext OpenRouter key goes with it).
- **Master-files token:** `VAULT_DISPATCH_TOKEN` can push but cannot open PRs. Re-make it with Contents + Pull requests write and re-set it in all 7 repos (RESUME item 0). Repo-history erase is operator-run (RESUME item 0b).
- **APK session** to resume: `cd ~/agent-stack && claude --resume 125f2d23-df2c-4a1b-823c-45acfa0cf8af` (its own handoff: `~/agent-stack/RESUME.md`).
- **Hardware brainstorm** (private): parked in `~/.claude/session-work/2026-10-04/SESSION-LOG.md` (prior-art search to do). Never into a repo.
- **Observation review:** 0022–0025 new this session (open), on top of the older open ones.
- **Carried from the 2026-10-04 START HERE** (deferred 2026-10-05):
  - Planning session in the wiki-admin agent (now the grill session, RESUME item 1).
  - Close the wiki-admin open decisions (guide §10): 2b–2e still open.
  - Restart the NPU work one model at a time with the operator (InternVL 2B first).
  - Housekeeping (due since end of week): roll up `_recaps/`, branch audit, observation review, billing, disk.

## Added 2026-10-02 (afternoon)
- ~~**[TOP] GitSync stuck in a "remote changing" loop**~~ resolved 2026-10-05: `main`, `vault-sync` and GitSync's `lastSyncedCommit` aligned on the same commit; the local index was reset to it.
- **wiki-admin open decisions** (guide `docs/WIKI-ADMIN-GUIDE.md` §10): where obsidian-wiki writes (`OBSIDIAN_VAULT_PATH`: vault root vs a subfolder); ~~link `~/wiki-admin` memory to the main memory dir~~ (done 2026-10-04, symlink); Obsidian skills load twice (links in `~/.claude/skills/` + `obsidian@obsidian-skills` plugin) — remove the links?
- **OpenWiki leftovers:** ~/AGENTS.md + ~/CLAUDE.md deleted by operator 2026-10-02 (backup in $TMPDIR/ow). Decide: delete `~/.openwiki/` (1.1 GB old DB) and the duplicate clone `~/openwiki`.
- **OmniGlyph** built (`~/bin/omniglyph`, fork NvAEx-OmniGlyph v1.4.0), not switched on. Decide: user-wide `ANTHROPIC_BASE_URL` + background service, or OmniRoute's `omniglyph` engine. Fable 5 only by default; Remote Control may hide behind any proxy. Full round trip (reply text) not yet captured.
- **Render MCP** (fork NvAEx-render-mcp-server, render.com) cloned only: needs `pkg install golang`, build, `RENDER_API_KEY`, `claude mcp add`.
- **NotebookLM:** operator runs `notebooklm login` once (CLI 0.8.4 from fork; skill in vault `.claude/skills/notebooklm`).
- **Disk bloat (~22 GB, read-only survey 2026-10-02):** `~/.cache/uv` 8.2 GB and `~/.npm` 5.7 GB (rebuildable caches); `~/gemma-12b/gemma-4-12b-it-qat-q4_0.gguf` same size as the `Models/gguf` copy (hash-check, then cut one); `~/gemma-e2b/` + `~/downloads/gemma-4-E2B-it-qat-UD-Q4_K_XL.gguf` (two copies of an E2B build); `~/downloads` x86/Windows installers. Dedup rule: model identity, not whole-file hash (memory feedback_same_model_bytes_differ); keep the newest version.
- **Kokoro TTS** `tts_speak.py` fails on the multi-lang v1.0 model (needs lexicon/lang). Kokoro v1.1 was deleted by mistake (restorable: k2-fsa sherpa-onnx tts-models `kokoro-multi-lang-v1_1.tar.bz2`).
- **Observation file `0018-resume-gate-and-enforce-gate-deadlock.md` is 0 bytes** (created 08:36 by another process) — fill or remove.
- **npu-serve:** add InternVL 2B (X Elite bundle ran 27.5 tok/s, prefill 1,528 here); tool calls; multi-image.

## Added 2026-10-02
- **H7 classifier: automatic skill matching (grill, with H5/H6).** `classify.sh` asks `$CLASSIFY_URL` first and falls back to the ENFORCEMENTS keyword rows if there's no answer in 2 s (it falls back, it doesn't fail). Plan: point it at a model that reads the prompt plus every skill's description, so new skills are covered without hand-written rows. Raise the 2 s timeout to whatever the model needs (candidate: local `npu-serve` :18181, if the tier-1 benchmark shows it is fast enough).
- **Post-task flagging (after the task-observer + Reasoning Bank pipeline works).** After task completion, a hook reviews which skills or rows *should* have fired and didn't. It feeds that back to the classifier and proposes new ENFORCEMENTS rows, so the list grows from real misses instead of by hand.
- **Keyword false triggers (grill):** rows fire on mentions as well as commands ("brand new" → naming; "wrap up" mentioned in passing → wrap-up mode). Needs command-vs-mention handling.
- **Resume the parked skill-observation review** (started 2026-10-01, 4 decision groups, never finished; `last-review-date.txt` = never).
- **Vault code-review-graph build crashes** on a long filename under `Drive_sync/` (stat before ignore). Fix in the fork or rename the file.
- **NPU benchmark (3 tiers + role map) in progress:** `~/tools/npu-bench/bench.py`, results in `docs/NPU-BENCHMARKS.md`. QAIRT route + vision input DONE 2026-10-02 (all 6 models). Next: TFLite/LiteRT setup, pure-Q4_0 requant of the Qwen 3.5 files.

## Added 2026-10-01
- NPU speed gap: v0.3.14 16–23 tok/s vs ~45–50 target; v0.7.1 DSP-queue failure from Termux. ADB test steps in RESUME.md.
- GenieX HTTP wrapper (NPU in the browser / for tools) — not built.
- aesop-xi PR #18 (orchestration contract) — held for the grill.
- Wiki agent home + forks decision (see RESUME grill agenda); custom skills' final home; vault-only corpus scripts' home.
- Voice: Tab-to-talk (Android STT) stops at the first pause; offline Moonshine has a 10 s cap; VAD never wired; nothing speaks the output (speak exists). `talk` built, untested with the mic.
- Small dead-path fixes listed in ~/.claude/INVENTORY.md (awaiting the operator's OK).
- ECC review: stale ecc-dashboard / nanoclaw launchers; ECC CI fix ships on PR #7's branch.
- Qwen 3.5 9B on the NPU — untested.
- Recaps: `_recaps/` older than 30 days get rolled into a monthly summary during housekeeping.

## Backlog

- **RESUME.md's "PHASES 1-4 COMPLETE" is wrong.** 585 files cleaned is nowhere near real scope — the two original source folders in `Drive_sync` total 5,000+ files. Needs correction and a real re-ingestion pass, not just a status-line fix.
- **Other 6 repos still POINTER.md stubs.** `novus-aexenti`, `NovAExopia`, `aesop-xi`, `horizons-ui`, `novus-aesc`, `novus-aeyre` haven't had their own ingestion pass — only `NovAExorpus` itself has real `clean_md`/`wiki_md` content.
- **`NovAExopia/horizons-ui/` was built from Document 05** (the nested-repo model), which is superseded now that RFMC (flat 8-repo model, `Drive_sync/LlmWiki/Repo-Files-Map-core/`) is the actual direction. Needs reconciling once the new standalone Horizons UI repo exists.
- **Terrestrial-brain backend location** — currently phone-local Postgres (works today via env vars in `.mcp.json`), migrating to self-hosted on the Jetson Orin Nano Super once the terminal-APK/Android-Local-Desktop work (next session) makes that device reachable and manageable.
- **QNN-QAIRT SDK (3035 files) and canvas-ui-main (416 files)** — sitting in `__RESUME.md/whatisit-/` on device, not yet ingested.

## Added 2026-09-28

- **Session-end discipline isn't enforced.** RESUME.md must be rewritten top to bottom every session and unresolved items moved here — no hook checks it. Needs a structural check (grill topic 11 / launch script).
  - *2026-10-02: partly enforced — `stop-gate.sh` blocks wrap-up until RESUME.md is rewritten. Moving unresolved items here is still unchecked.*
- **Operator's own MEMORY.md** — enterprise-wide, separate from Claude's memory; RESUME / AGENTS / MEMORY / PENDING from the other six base repos to sync into this corpus repo (grill topic 3).
- **Hooks not registered yet** — `sync-forks` / `ship-session` need the operator's paste (classifier blocks the agent).
- **Old Claude memory + ECC rules** — archive line not run yet.
- ~~**Other six repos: CLAUDE.md → AGENTS.md**~~ (done 2026-10-05; Horizons/Hyperion-OXiLm renamed to `Hyperion-XI`). Still open: GitHub renames to `NovusAExenti`, `AEsop-Xi`, `AEsc`, `AEyre` — after the grill.
- ~~**OpenWiki replacement**~~ DONE 2026-10-02: plugin from fork NvAEx-openwiki-for-claude-code (in ~/wiki-admin), MCP removed, CLI uninstalled, vault AGENTS block removed. Leftovers in 'Added 2026-10-02 (afternoon)'.
- **OB1 Obsidian plugin + OmniRoute Obsidian plugin** — none exist; build (grill topics 5/7).
- **MemVault** — operator setting up; decide if its folder is public.
- ~~**Nested `/NovAExorpus/` repo mirror in the vault (3.1 GB)**~~ moved out to `Documents/NovAExorpus-nested-mirror/` (2026-10-05).
- **Stale VM IP `34.31.112.77`** in `tools/launch.sh`, `router-guard.sh`, `.mcp.json` defaults.
- **OmniRoute on the VM runs the npm build, not the c10vis-poem fork.**
- **Terrestrial Brain VM unit file has the OpenRouter key in plaintext, world-readable** — rotate the key.
- **Recovered plugin drafts** (`recovered/2026-09-26-ob1/omni-feat/`) never pushed; orchestration contract = Æsop-Xi draft PR #18.
- **3 diverged forks** — pm-claude-skills, trusted-firmware-a, ai-hub-apps get upstream PRs on next `sync-forks`.
- **ECC-aesop has 18 unpushed local commits on main** — skipped by ship-session (ECC off-limits); operator to decide.

## Carried from RESUME.md 2026-09-18 (not re-verified this session)

- Qwen3.5-2B on phone NPU (geniex-bench, HTP v79) not wired; OmniRoute backend for it.
- `feat/vm-lifecycle-2026-09-18` branch never pushed.
- sherpa-onnx: 8 inherited upstream cron workflows still active.
- dsh workspace selection; OpenRouter key on VM; passwordless sudo on VM.
- mem0 + TB actually writing during sessions; mem0 vault export; mem0 self-hosting on VM.
- Honey-for-devs setup wizard; Graphify integration; NotebookLM integration.
- OmniRoute MCP round-trip test; web UI dashboards on VM; `bootstrap.sh` still points at localhost.
- Source docs in `~/storage/shared/Documents/9-18-26/` unread.
- `vault-ci.yml` workflow; shell alias `cc`; global `~/.claude/CLAUDE.md` rewrite.
- "Rename repo to NovAEcorpus" — conflicts with NAMING-CANON (NovÆxorpus / `NovAExorpus`); confirm or drop.
- "Obsidian Git plugin" — superseded by GitSync Portal; drop unless wanted.
- **MemVault server** (carried from the 2026-09-28 session) — waits for the Jetson; fork `dreamor/MemVault` → c10vis-poem and build the image from the fork (not `ghcr.io/dreamor/memvault`). Decide in grill topic 7 whether it earns a place next to Mem0 and OB1.

## Added 2026-09-29

- **Continual Harness read unfinished.** See `grill/continual-harness-read-ledger.md` "Not yet read".
- **aesop-xi CLAUDE.md:** false ReasoningBank/Continual Harness lines fixed in aesop-xi PR #20 (2026-09-30); Honey rule restored in PR #21. Its other agent-written hard rules still need the operator's review.
- **`_dumbass_unified-config/` unread.**
- **Task-observer review outstanding.**
- **aesop-xi local clone:** branch `feat/memory-stack-canonical-2026-09-15` is 1 commit ahead with uncommitted `tools/bootstrap.sh` and an untracked `tools/aesop-tmux.sh`. Not this session's work; needs the operator's call.
- **OmniRoute local clone:** uncommitted `.source/dynamic.ts`, and the clone is dated 2026-08-15. Sync the fork before relying on it.

## Done 2026-09-30

- PR #21 merged after adding `.gitleaksignore` (8 reviewed findings); the scan on `main` passed.
- PR #7 closed and its branch deleted (built from Document 05; would have re-deleted `01-sources/` and `tools/check.py`).
- GitHub branches cut to `main` only. `master` preserved as tag `archive/master-2026-09-06` (its 2026-09-05 decisions are not carried into `main`, per the operator).
- GitSync Portal now syncs straight to `main` (`syncBranch`); push protection plus the gitleaks job on `main` still apply. First sync hit a DNS error on the phone; retry pending.
- AGENTS.md (vault + aesop-xi): false ReasoningBank crash-recovery and Continual Harness auto-rollback claims corrected; stale VM IP removed. Honey stays (operator: leave Honey and OmniRoute alone). OmniRoute turns ReasoningBank, Continual Harness and the memory layers on and off; while running each is its own MCP server (operator, 2026-09-30).
