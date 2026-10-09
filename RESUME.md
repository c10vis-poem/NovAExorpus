Session files: [[AGENTS]] · [[PENDING]] · [[MEMORY]] · [[MAP]] · [[NAMING-CANON]]

# RESUME.md — Session Ledger (rewritten every session)

Repository: NovÆxorpus (`c10vis-poem/NovAExorpus`, PUBLIC).
**Last session: 2026-10-08** (phone, Claude Code, Opus 5.5, session `34c3e229`, started in `~`).
It covered: eson + honey hook fix, PDF move to the keep (1,046 → 12 in the vault), NovA-Corpus condensed swap, vault tools fixed, hooks H2 blocking / H8 CI / change-log review, NvAEx-Recaps (recaps + secrets), LiteDoc, grill inputs, PR triage.
Everything from that session, with every report: `~/.claude/session-work/2026-10-08/` (start with `WRAPUP-QUEUE.md`).

## How to run this session: subagents in tandem
Every START HERE item below is a **workstream** written so one orchestrator can hand it to a subagent unchanged. Standing order (`~/.claude/CLAUDE.md`): independent workstreams run in parallel; each subagent writes its progress file FIRST (`~/.claude/session-work/<date>/agent-<topic>.md`: Plan / Last action / Findings / Blocked) and updates it after every step. The orchestrator answers "where is X" from those files. Nothing ships mid-session: every change is recorded by `change-log.sh`; at `/wrapup` the operator reviews it and types `/ok push`.
Parallel-safe groups: **A** = items 2, 3, 4 (GitHub + repos) · **B** = items 5, 6 (vault files; never two vault-moving agents at once) · **C** = item 1 (operator-led) · item 0 first, alone.

## NEXT SESSION — START HERE
**Operator, 2026-10-09: items 0, 3, 4 and 5 have been carried over for more than a week. The next session finishes them FIRST, completely, as parallel subagents, before any other work (grill and NPU included). "Partly done" is not a status: each item ends done with evidence, or blocked on something only the operator can do, named exactly.**
The Stop gate requires a status for each numbered item: `resume-item <n> done|blocked "<evidence / what's needed>"`.

0. **Carry-over check (first, alone; haiku).** Open `~/.claude/session-work/2026-10-08/WRAPUP-QUEUE.md`. Every `[ ]` line not shipped at the 2026-10-08 wrap-up becomes part of items 2–6 below; mark `[x]` what the `## Shipped` section of `_recaps/2026-10-08-34c3e229.md` proves shipped. Done = each open line assigned to an item.
1. **Grill session (operator-led; wiki-admin).** The operator types `/ask-matt` → `/setup-matt-pocock-skills` → `/grill-with-docs` → `/to-spec` → `/to-tickets` → `/implement`. Single input list: `~/wiki-admin/GRILL-INPUTS.md` (PRIORITY ONE docs, 2026-10-05 reports, 2026-10-08 additions: repos/ mirrors, 2x2 converter/checker design, OmniRoute compression + vision plugin, observation-review staged skills, aesop-xi PR #18 contract, hooks H1–H8 review). Agents assist; they do not decide.
2. **NPU job queue, then NPU runs (opus orchestrator; cloud subagents + Fable advisor).** Restart the plan in `~/.claude/session-work/2026-10-08/agent-npu-queue.md` (stopped at step 0 by a usage limit): jobs/results in `NvAEx-Recaps/npu/`, `npu-run` + `npu-queued` daemon on the phone, `npu/ORCHESTRATOR.md`, one real test (Qwen3.5-0.8B, npu + CPU baseline). Rules: `~/.claude/NPU-ON-DEVICE.md` (read fully; no "needs a computer"), `docs/NPU-FINDINGS-2026-10-02.md` §4. Qwen 3.5 only. Then the orchestrator runs the model queue (InternVL 2B first) with no operator present. Done = test job result with NPU-proof lines + CPU baseline.
3. **PRs and CI (sonnet).** Source: `~/.claude/session-work/2026-10-08/pr-triage-report.md` + the operator's answers in `WRAPUP-QUEUE.md`. Merge: NovA-terrestrial-brain#3, termux-app#2, termux-packages#6, termux-gui-bash#1 (adopt; add CI first). Fix then merge: honey #1/#2 + NovA-skills#1 (required check `check` matches no job), obsidian-skills#1. Close: aesop-xi#33, openwiki#2/#3, OB1#1, ai-hub-merovingian-models-#1. Leave open: aesop-xi#18 (grill), Horizon-s-home-grid#1 + Hyperion-XI#4 (3-APK build). ECC: not touched. Then improve H8 `ci-ready.sh` to check required names against real job names. Done = triage table all closed/merged/left-by-decision.
4. **Repos (sonnet).** (a) `repos/` folder in this vault = live mirrors of the 6 base repos, built by `master-files.yml` on each `notify-vault`; retire MASTER-AGENTS/MASTER-RESUME + `tools/build_masters.sh`; delete the stale `AEsc/ AEsop-Xi/ AEyre/ NovAExopia/ NovusAExenti/ projects/` folders after a unique-content check (unique → keep). Needs `VAULT_DISPATCH_TOKEN` set in all 7 repos (operator). (b) `ship-session.sh` copies each recap into `NvAEx-Recaps/recaps/<repo>/` for every repo touched; CI + branch protection on NvAEx-Recaps. (c) Renames (last): 19 `NovA-`/`NoVa-` repos → `NvAEx-<rest>`, `aesop-xi` → `Aesop-Xi`, local folders + every hook/launcher/`nvaex-repos.sh` path; delete `c10vis-poem/NovA-Corpus` + `~/repos/NovA-Corpus` (unique content already saved); delete the 44 old branches. (d) Fix two `ship-session.sh` gaps found at the 2026-10-08 wrap-up: a worktree that never appears under "Repos touched" in the recap is skipped (AEthX-AEsc `pending-fold` in `.wt-AEthX-AEsc-pending` was missed); `~/wiki-admin` is skipped as "origin not a c10vis-poem fork" (check its origin and the ORIGIN_RE match). Done = mirrors present + recaps flowing + renames verified by a hook test run + both gaps covered by a ship test.
5. **Vault cleanup (sonnet; group B).** Fold the vault's 12 `*unresolved*` files into `PENDING.md`, then delete them. The 12 PDFs still in the vault (fail: fused tokens): re-run through the 2x2 design once the grill builds `check2.py`. Report (do not delete) the 82 exact duplicates in `clean_md/`. Also: GitSync Portal stalled since 2026-10-02 (operator suspects a zip); the 2026-10-08 sync was done by hand (PR #44), so reset its `local-sync-state.json` base to `03e65f3` (or reset the plugin) and find what it chokes on. Done = 0 unresolved files; PENDING has their items.
6. **Observations (sonnet; group B).** 29 logged, 13 open (0001, 0005–0007, 0012, 0015–0017, 0023, 0024, 0028, 0029, + 0018 empty). Staged: `skill-updates/2026-10-08/`. Fix 0001/0006/0015 in the operator's forks (task-observer = `aesop-task-observer`, honey = `NoVa-honey-for-devs`). Proposed rules become hooks in `aesop-xi/hooks/` only after checking H1–H8 (obs 0029). Done = each open observation actioned, parked with a condition, or handed to the grill.

## STATE (verified 2026-10-08)
- **Hooks (live in `~/.claude/hooks/`, sources `aesop-xi/hooks/`, moved from `deploy/phone/hooks/`):** H2 `sync-on-use.sh` now BLOCKS until the fork is synced (17 tests); `change-log.sh` records every change, `review-changes.sh` + `/ok push` gate every push (20 tests); H8 `ci-ready.sh` blocks wrap-up / auto-merge without CI + required checks; `documents-guard` merged into change-log (nothing blocked). `test-ship-v2.sh` fails 14/18 on origin/main too (pre-existing).
- **NvAEx-Recaps (private):** `recaps/<7 repos>/`, `recaps/ROLLUP.md`, sops+age secrets `secrets/secrets.enc.yaml`, CLI `nvaex-secret` (get/set/list/push/edit). Only the phone's age key can decrypt: add a second key. No CI yet.
- **Vault tools:** `tools/clean.py` + `tools/check.py` fixed (vault-root layout, mutool, `type: condensed`, sources in the keep, canary); `.migrate/` complete (pickle → JSON BM25; `dedup.py` runs `git rm`: operator approval); `generate_jsonl_markers.py` = independent chunk cross-check. LiteDoc (fork, v3.3.0 CLI) installed: `litedoc`. `mutool`, `sops`, `age`, `eson` installed.
- **Keep (`Documents/Merovingian's_keep/`):** `vault-pdfs/` (970 PDFs), `_salvage/NovA-Corpus/` (+ `originals/`, HomeGrid.kt), `vault-moved/_quarantine/` (3.0 GB).
- **Disk:** 136 GB free (17.7 GB caches/duplicates + 8.3 GB Qwen3-VL bundles deleted).
- **Cloud:** project-alchemist-490416 kept; billing off, $0.

## DECISIONS 2026-10-08
- PDFs live only in the keep unless no text version exists.
- `unresolved.md` retired: open items go to each repo's PENDING.md. "canon", POINTER.md and the `NovA-` prefix are removed whenever touched.
- The vault gets live repo mirrors (`repos/`); no MASTER-* files.
- Two converters + two checkers on four PDF engines (MuPDF, pdf.js, pypdf, Poppler); no tool checks its own output.
- Qwen models: Qwen 3.5 only. Render MCP dropped (forks kept). Context-as-image through OmniRoute.
- Nothing is pushed until the operator reviews the session's change list (`/ok push`).

## OPEN ITEMS, IN ORDER
1. START HERE above.
2. APK session: `cd ~/agent-stack && claude --resume 125f2d23-df2c-4a1b-823c-45acfa0cf8af`.
3. NvAEx-agentk org transfer (operator creates the org).
4. Everything else in `PENDING.md`.

## HANDOFF SOURCES
Read this session: old RESUME.md + PENDING "Added 2026-10-05", `~/.claude/hooks/README.md`, `stop-gate.sh`, `ship-session.sh`, `session-ledger.sh`, `enforce-prompt.sh`, `sync-on-use.sh`, `NPU-ON-DEVICE.md`, `NPU-FINDINGS-2026-10-02.md` §4, `01-WIKI-SEARCH-RESULTS.md` §3, `WIKI-ADMIN-GUIDE.md` §6/§10, OmniGlyph + OmniRoute READMEs, every subagent report in `session-work/2026-10-08/`.
Not read: the PRIORITY ONE plan docs (00–13) beyond file names; `Master_dumbass_plan-session` content; most of `Drive_sync/`.
