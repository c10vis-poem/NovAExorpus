# Asset inventory ledger (collected 2026-10-24)

Collector: inventory worker (read-only). Sources: local clones `/home/user/novaexorpus` (HEAD 16a5a5b3, 2026-10-24, "Merge pull request #56 from c10vis-poem/vault-sync") and `/home/user/aesop-xi` (HEAD 094dda5b, 2026-10-23, "docs: drop the checkin-gate and wrap-up defect items (#80)"), plus read-only `gh api`.

## Reading rules and status vocabulary

- `verified-on-disk`: I opened the file or counted the files in the clone this session. This proves the doc, script or directory exists in the clone. It does NOT prove the phone state the doc describes.
- `stated-in-doc`: a doc says so; I did not check the phone, the GitHub org or the device. Phone paths (`~/tools`, `~/.claude/...`, `Documents/_models`) are not mounted here, so everything about them is stated-in-doc.
- `gh-api`: returned by `gh api repos/c10vis-poem/<name>` this session.
- Per AGENTS.md Rule 3 of the vault, docs `00_`..`05_` at the vault root are known wrong. I cite them only as "stated in 0X, unverified". Where a source cited them I say so. Other docs (RESUME, PENDING, handoff reports) are the operator's current docs, but they are still doc claims.
- Vault RESUME.md says "Not read: ... most of Drive_sync/". Nothing in this ledger reflects Drive_sync content beyond file counts.

## Collection gaps (read this first)

1. `gh repo list c10vis-poem` returned HTTP 403 ("GitHub GraphQL is not available from Claude Code sessions"). `gh api users/c10vis-poem/repos` returned HTTP 403 ("sessions are bound to their configured repositories"). So there is NO authoritative list of all c10vis-poem repos. Table 1 is built from names in the docs and is therefore incomplete. The branch-review report says a 161-repo audit was done on 2026-10-23 ("branch audit (161 repos)", vault PENDING.md "Closed 2026-10-23"). That count is stated-in-doc only.
2. `gh api repos/c10vis-poem/<name>` worked for only 2 of the 17 named repos (Aesop-Xi, NovAExorpus). The other 15 returned "GitHub access to this repository is not enabled for this session. Use add_repo to request access." I did not call `add_repo`: it changes the session's attached sources and mints credentials, which is outside my read-only scope clause. Default branch, issue count and archived flag are therefore NOT collected for those 15. Caller can run `add_repo` for them and re-run, or supply the list.
3. Handoff dir `handoff/2026-10-23/` has no `secrets-report.md` (RESUME/PENDING mention one in `session-work`, phone only). Ten reports exist (listed in Table 3 sources). Not found by `ls handoff/2026-10-23/` and `find /home/user/novaexorpus -name '*secrets-report*'` (the find was not run; only the `ls` was). Treat as "not found by ls of that directory".
4. The names "Alpha / Beta / Gamma / Delta" for nodes do not appear in any doc I was told to read (grep of AGENTS, RESUME, PENDING, BOARD-INTAKE, MEMORY, CONTEXT, NAMING-CANON, handoff/, aesop-xi AGENTS/RESUME/PENDING/MEMORY/ARCHITECTURE, profiles/, deploy/ READMEs, docs/). Table 6 uses the docs' own names (phone, tablet, Jetson, Rubik Pi, GCP VM, computer/laptop). Mapping to Alpha..Delta is the caller's.
5. Vault RESUME.md says the observer has "19 active entries". On disk `skill-observations/observation-log/` holds 8 observation files plus an `archive/` dir (51 files inside). Count mismatch recorded in Table 9.

---

## 1. Repositories

Name casing is as the docs write it. Base-repo mapping is from: vault `NAMING-CANON.md` (2026-08-24, operator-stated), vault `BOARD-INTAKE.md` "Decisions recorded 2026-10-23", aesop-xi `AGENTS.md` ("the 7 base repos"), `TOOLS-SCRIPTS-HOOKS-INVENTORY.md` §3 ("all 8 federated repos"), vault `PENDING.md` "Closed 2026-10-22" (repo renames). Which exact 7 or 8 are "the base repos" is NOT listed in one place; the grouping below is my reading and is marked.

### 1a. Repos with gh-api data

| Name | Fork? | Private? | Last push | Language | Size (KB, gh) | Default branch | Open issues | Archived | What it is per docs | Base repo? | Source / status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Aesop-Xi | no | no | 2026-10-23T21:51:53Z | Shell | 526 | main | 0 | false | Orchestration repo: scripts, hooks, rules, enforcement; "data plane" of the three-plane split; deploy files for phone / Jetson / Rubik Pi / GCP VM; skills (4) | YES (canon "Æsop-Xi") | gh-api; role stated-in-doc (BOARD-INTAKE "Aesop-Xi = orchestration"; CONTEXT.md) |
| NovAExorpus | no | no (PUBLIC; vault AGENTS says repo is PUBLIC) | 2026-10-24T12:46:25Z | HTML | 334094 | main | 0 | false | The vault / universal data bank / Obsidian vault; source of truth; synced by GitSync via `vault-sync` branch | YES (canon "NovÆxorpus") | gh-api; role stated-in-doc |

Note: the clones' git remotes are `https://github.com/c10vis-poem/novaexorpus` and `.../aesop-xi` (lowercase) (verified-on-disk, `git remote -v`). The gh-api names are `NovAExorpus` and `Aesop-Xi`. NAMING-CANON table says the canonical repo form of Æsop-Xi is `AEsop-Xi`; the actual repo is `Aesop-Xi` (PENDING "Repo renames (Aesop-Xi, NovusAExenti, AEsc, AEyre): done").

### 1b. The other 15 repos you named (gh-api denied; role from docs)

| Name | gh-api | What it is per docs | Base repo? (my reading) | Source |
|---|---|---|---|---|
| NovAExopia | DENIED (add_repo) | "capabilities"; agent tools, harness, engine, "claw" aspect; spelled with no ligature in the URL (locked decision 7, 2026-09-05). Per voice brief it holds `AGENTS.md` and a `daemons/` contract-doc target; per TOOLS inventory it had `aesc/scripts/agent_panel.sh` placed 2026-09-10 | YES | stated-in-doc (BOARD-INTAKE; NAMING-CANON; voice-apk-brief) |
| NovusAExenti | DENIED | "modular agent packages"; agent logic | YES | stated-in-doc (BOARD-INTAKE; NAMING-CANON) |
| Hyperion-XI | DENIED | Hosts tiles with plugin connectors that run each app's dashboard, plus webview tiles for any URL (BOARD-INTAKE). Open PR #4 merged 2026-10-22 (PENDING). Whether Hyperion-XI = Horizons-Ui is NOT stated in the docs I read (NAMING-CANON lists "Horizons-Ui" as the UI) | probably YES (UI shell) - unverified | stated-in-doc |
| AEthX-AEsc | DENIED | Æsc terminal daemon repo. Holds `docs/npu-proof/2026-10-23.md` (GenieX v0.9.3 proof run) per aesop-xi RESUME. Name "AEthX-AEsc" vs canon "AEsc": spelling difference, not resolved in docs | YES (terminal APK) | stated-in-doc (aesop-xi RESUME "recorded in the Æsc repo (AEthX-AEsc/docs/npu-proof/2026-10-23.md)") |
| CloviX-AEyre | DENIED | Æyre: voice and vision daemon layer, the "Media APK"; repo name `novus-aeyre` per voice brief; stub dirs `voice-ast-stack/`, `stt_models/`, `tts_models/`, `screen-vision/`; `docs/VOICE-EXTRACTION-PLAN.md`; no Kotlin code yet; recommended home of the voice APK | YES | stated-in-doc (voice-apk-brief §1, §10) |
| NvAEx-Recaps | DENIED | PRIVATE repo; sops+age secret store (`nvaex-secret`); session recaps (`recaps/<repo>/`), NPU job queue (`npu/`), `secrets` | support repo (not a base repo) | stated-in-doc (vault AGENTS "Current stack"; aesop-xi hooks README; BOARD-INTAKE) |
| raw-databank | DENIED | Holds `horizons-ui-full/` (prior Compose APK, package `com.horizons`, last commit 94c3abf 2026-09-15). Relation to vault `raw_database/` not stated | maybe the "raw_database" 8th federated repo - unverified | stated-in-doc (voice-apk-brief §1) |
| AEsopXi-mobile-harness | DENIED | Not described in any doc I read (grep not run beyond the files listed in the task) | unknown | name only (from task); not found in the read docs |
| ECC-aesop | DENIED | Fork of ECC (affaan-m/ECC); a Claude Code plugin ready but never installed; ECC "intentionally uninstalled 2026-09-09"; "ECC deferred"; now "used only as a marketplace for individual skills; no fork maintenance"; "ECC-aesop 18 unpushed commits: stale (now 1 ahead, 415 behind)"; ECC #7 PR merged 2026-10-23 | no | stated-in-doc (TOOLS inventory §1; BOARD-INTAKE; PENDING) |
| NvAEx-skills | DENIED | Not described. vault PENDING 2026-10-22 mentions "honey/NovA-skills mismatch" required-check names in branch-review §4. Content unknown | unknown | stated-in-doc (name hint only) |
| NvAEx-code-review-graph | DENIED | Fork of the code-review-graph MCP (structural memory layer). As of the 2026-10-23 branch review: Actions disabled, only `main`, PR #2 "skip ignored paths before stat" BLOCKED (8 required checks cannot report). PENDING says "crg #2 merged" and "code-review-graph fork #2 auto-merging" later the same day; RESUME says "all [PRs] merged except Horizon-s-home-grid #1" | no | stated-in-doc (branch-review §4; PENDING; RESUME). The report and the later PENDING differ because they are from different times that day |
| claude-code-android | DENIED | Fork of ferrumclaudepilgrim (Claude Code on Android). Branch `claude/android-architecture-review-Is4hk` = only copy of the NeuroOmni / Horizons scaffold (KEEP until 3-APK build decides); branch `claude/generator-noise-analysis-IOzhr` unrelated | no | stated-in-doc (branch-review row 26-27) |
| termux-app | DENIED | Fork of termux/termux-app, "terminal-APK base"; fork master 2 ahead of upstream; 8 upstream-owned branches archived as tags | no (terminal-APK base) | stated-in-doc (branch-review rows 11-18) |
| GenieX | DENIED | Fork of qualcomm/GenieX (NPU inference runtime). Fork synced to `692086f0` on 2026-10-23; fork has NO releases (prebuilt binaries only from `qualcomm/GenieX` releases) | no | stated-in-doc (npu-install-plan §0.8, §6 step 1) |
| ai-hub-apps | DENIED | Fork of Qualcomm ai-hub-apps; PR #4 (v0.39.1 + GenieX Chat workflow `build-geniex-chat.yml`) merged 2026-10-23; HEAD `7fbeb9b` when read | no | stated-in-doc (PENDING; npu-install-plan) |

### 1c. Other repos named in the docs (not in your list; no gh-api call made)

All status `stated-in-doc`. "Fork of" is as the docs say.

| Name | What it is per docs | Source |
|---|---|---|
| NovA-Corpus | Old vault name; deleted ("Delete NovA-Corpus: done (not in repo list)", PENDING 2026-10-22) | PENDING |
| NvAEx-OmniRoute | Fork; PR #1 merged 2026-10-22; OmniRoute DROPPED 2026-10-23 | PENDING |
| NovA-terrestrial-brain / NvAEx-terrestrial-brain | Fork of TerrestrialOrigin/terrestrial-brain, 0 behind / 7 ahead; DROPPED; TB #7 merged | skills-inventory-report; PENDING |
| aesop-task-observer | Operator fork of rebelytics/one-skill-to-rule-them-all (task-observer); fork PR #1 (09a4101) holds the 0015 fix | AGENTS Rule (task observer); skill-updates/PENDING.md |
| OB1 | Fork of NateBJones-Projects/OB1 "Open Brain"; open PR #2 (bot) to be closed, not merged; under strip-and-judge | branch-review |
| clovis-mem0-vingiaN | Fork of mem0ai/mem0 (marketplace "mem0-plugins"); mem0 DROPPED | skills-inventory-report |
| NvAEx-honey-for-devs | Fork of Green-PT/honey-for-devs (0 behind / 5 ahead); marketplace "greenpt" | skills-inventory-report |
| honey | fork; honey #3, #6 merged 2026-10-22; Actions enabled | PENDING |
| obsidian-skills | Fork of kepano/obsidian-skills (0 / 4 ahead) | skills-inventory-report |
| AEsops-obsidian-wiki | Fork of Ar9av/obsidian-wiki (25 behind) | skills-inventory-report |
| NvAEx-openwiki-for-claude-code | Fork of jatinmayekar/openwiki-for-claude-code | skills-inventory-report |
| NvAEx-openwiki-skills | Fork of kinensake/openwiki-skills (not cloned) | skills-inventory-report |
| openwiki | Fork of langchain-ai/openwiki; OpenWiki DROPPED/retired 2026-10-02 | skills-inventory-report; PENDING |
| NvAEx-llm-wiki-nocode | Fork of rosidotidev/llm-wiki-nocode | skills-inventory-report |
| llm-wiki-compiler-NvAEx | Fork of ussumant/llm-wiki-compiler | skills-inventory-report |
| AEsopXi-obsidian-tars | Fork of TarsLab/obsidian-tars (Obsidian app plugin, not a Claude skill) | skills-inventory-report |
| graphify | Fork of Graphify-Labs/graphify (330 behind; default branch v8) | skills-inventory-report |
| notebooklm-py | Fork of teng-lin/notebooklm-py (HEAD 00b2bd50 2026-10-22) | skills-inventory-report; remote-access-report |
| memsearch-aesop | Fork of zilliztech/memsearch | skills-inventory-report |
| pm-claude-skills | Fork of mohitagw15856/pm-claude-skills (own weekly-digest commits; bot branches) | skills-inventory-report; branch-review |
| MemVault, claude-mem, agentmemory, oak-memory-plugin, pmm-plugin | Forks created 2026-10-23 (items 9, 24); memory candidates, "pick ONE auto-capture memory" is an open item | PENDING |
| notebooklm-py, headroom, context7 (x2) | Forks synced 2026-10-23 | PENDING |
| NvAEx-Jev.skills | Fork to be reviewed before any install ("what it sends to TypeSafe, which key") | PENDING |
| NvAEx-rea | REA fork, review before install | PENDING; anthropic-research-report |
| dsh-jev | Repo hit for "JEV" (JEV/REA are not defined in local notes) | anthropic-research-report |
| NvAEx-DroidDesk | DroidDesk README read for tablet desktop (Termux:X11) | remote-access-report |
| Horizon-s-home-grid | Operator's own repo; main = README only; draft PR #1 "Add definitive HomeGrid.kt" (leave open, operator 2026-10-23) | branch-review §3 |
| Novus-WhisperKitAndroid | named only | voice-apk-brief (not read there) |
| c10vis-LocalAI | Fork of mudler/LocalAI | branch-review |
| clovis-hermes-agent | Fork of NousResearch/hermes-agent | branch-review |
| modern-web-guidance-src | Fork of GoogleChrome guidance source | branch-review |
| poem-langflow | Fork of Langflow | branch-review |
| NvAEx-worldmonitor | Fork of koala73/worldmonitor | branch-review |
| ai-hub-merovingian-models- | Fork of Qualcomm AI Hub models (759 behind); also called `ai-hub-models` in RESUME | branch-review; RESUME |
| glibc-packages | Fork of termux-pacman/glibc-packages | branch-review |
| claude-skills | Fork of alirezarezvani/claude-skills | branch-review |
| claude-android-skill | Fork of dpconde skill | branch-review |
| adk-docs | Fork of google/adk-docs; 184 branches, 33 behind; `gh repo sync` fast-forwards cleanly | branch-review §2 |
| generative-ai | Fork synced 2026-10-23 | PENDING |
| sherpa-onnx | Fork; "149 fork Actions disabled" (PENDING 2026-10-22) then "11 wrongly disabled re-enabled" | PENDING |
| happy-ending, NoVa-reverse-skill, trusted-firmware-a | forks/clones mentioned; trusted-firmware-a "moot" | PENDING; TOOLS inventory |

---

## 2. Hooks (aesop-xi/hooks)

Source: `/home/user/aesop-xi/hooks/README.md` (verified-on-disk), `ENFORCEMENTS.md`, `WRAP-UP.md`, `settings.hooks.json`, file headers read with `sed -n`, and `grep -l` of file names inside `hooks/tests/*.sh` (verified-on-disk). Test-suite column = a test file in `hooks/tests/` references the script by name; I did not run anything. aesop-xi RESUME states "All 22 hook test suites pass at #77" (stated-in-doc; aesop-xi MEMORY 2026-10-23 says the earlier "test-ship-v2 fails 14/18" note is stale). Test files on disk: 26 `*.sh` incl. `lib.sh`, `test-ledger.sh`, `test-ship.sh`, `test-ship-v2.sh`.

Live copies are on the phone at `~/.claude/hooks/` (stated-in-doc; RESUME says "equal to Aesop-Xi main"). `.claude/settings.json` in aesop-xi registers them via `hooks/run-hook.sh`.

| Hook file | Event / matcher | Purpose | Test suite present? | Status |
|---|---|---|---|---|
| `resume-gate.sh` | PreToolUse `*` | No tool runs until RESUME.md (repo's, else vault's) has been read | cloud-standdown.test.sh (indirect) | verified-on-disk; live: stated-in-doc |
| `checkin-gate.sh` | PreToolUse `*` | After RESUME is read: no changes until operator checks in with `#ok`/`#defer`/`#reject` | checkin.test.sh references enforce-prompt, but NO test names `checkin-gate.sh` itself (grep: NONE) | verified-on-disk. Note: last aesop-xi commit #80 is "drop the checkin-gate and wrap-up defect items" |
| `secret-guard.sh` | PreToolUse `Bash\|Read` | Refuses printing secret files unless redacted; refuses git hook skipping / hooksPath changes | cloud-standdown.test.sh (indirect) | verified-on-disk |
| `enforce-gate.sh` | PreToolUse `*` | No tool runs until this prompt's ENFORCEMENTS requirements are met | enforce.test.sh | verified-on-disk |
| `enforce-prompt.sh` + `classify.sh` | UserPromptSubmit | Works out required skill/read/script per prompt from ENFORCEMENTS.md rows (keyword/`repo:`), or `CLASSIFY_URL` backend; H7 tells a mention from a command (#71) | enforce.test.sh, h7-mention.test.sh, carryover/change-log/checkin/gitgate tests | verified-on-disk |
| `branch-current-gate.sh` | PreToolUse `Bash\|Edit\|Write` | No edits or `git commit` in a c10vis-poem repo whose branch lacks the latest `origin/<default>`; vault exempt | branch-current.test.sh | verified-on-disk |
| `sync-on-use.sh` (H2) | PreToolUse `Bash\|Edit\|Write\|Read` | BLOCKING fork sync (`gh repo sync` + fetch + ff) on first touch of a `~/repos/<fork>` | sync-on-use.test.sh | verified-on-disk |
| `plugin-fork-sync.sh` | SessionStart (detached, exit 0) | `gh repo sync` for every plugin marketplace backed by a c10vis-poem fork, then refresh marketplace and enabled plugins. NOT in README table | NONE | verified-on-disk (file header) |
| `git-gate.sh` | PreToolUse `Bash` | No push/PR/merge mid-session; unlocked by wrap-up mode or "push now" (lasts session; "hold push" revokes); quoted text ignored. NOT in README table | gitgate.test.sh, cloud-standdown.test.sh | verified-on-disk |
| `change-log.sh` | PreToolUse `Write\|Edit\|NotebookEdit\|Bash` | Records every write/move/copy/delete/script run to `state/changes-<sid>.log` for wrap-up review; blocks nothing. NOT in README table | change-log.test.sh | verified-on-disk |
| `review-changes.sh` | wrap-up helper | Summarises change log into recap "## Change review"; operator approves with `#ok push` | change-log.test.sh | verified-on-disk |
| `ci-ready.sh` (H8) | helper for stop-gate and ship-session | Exit 0 only if repo has >=1 Actions workflow AND branch requires status checks; exit 3 for private free-plan repos | ci-ready.test.sh, test-ship-v2.sh | verified-on-disk |
| `session-ledger.sh` (H3) | PostToolUse `Edit\|Write\|Bash` | Logs repos touched/files written/git actions to vault `_recaps/<date>-<sid>.md` (git-ignored) | test-ledger.sh | verified-on-disk |
| `context-diff.sh` | SessionStart | Shows CLAUDE.md/MEMORY.md lines changed since last session | NONE | verified-on-disk |
| `housekeeping-check.sh` | SessionStart | "HOUSEKEEPING DUE" when PENDING.md `last-housekeeping` is 7+ days old | housekeeping.test.sh | verified-on-disk |
| `staged-updates.sh` | SessionStart (Termux only) | Lists staged skill updates still pending in vault `skill-updates/PENDING.md` plus a one-line inventory of Termux skills/plugins; Stop gate asks until installed or `#staged-defer` (#69) | staged-updates.test.sh | verified-on-disk |
| `ship-session.sh` (H4, v2) | SessionEnd | Ships only repos touched this session: branch, commit (gitleaks), PR, auto-merge; writes `## Shipped`; copies recap to `NvAEx-Recaps/recaps/<repo>/`; never ships the vault | change-log, ship-gaps, test-ship-v2, test-ship | verified-on-disk |
| `vault-ship.sh` (+ `~/bin/vault-ship`) | wrap-up (from ship-session) or by hand | Uploads the vault: merge GitHub's, commit, push `vault-sync`, PR to `main` with auto-merge; `--dry-run` | NONE | verified-on-disk |
| `archive-scratchpad.sh` | SessionEnd / PreCompact | Copies session scratchpad to `~/.claude/scratchpad-archive/` | NONE | verified-on-disk |
| `stop-gate.sh` (H1) | Stop | Turn can't end until RESUME read, START HERE items have status, task-observer loaded + scan, friction events logged, no ENFORCEMENTS pending; wrap-up checks | carryover, cloud-standdown, observe, staged-updates, subagent-stop-gate tests | verified-on-disk |
| `carryover.sh` (H9) | Stop, `/wrapup` | A START HERE item left unfinished earlier can't be deferred again without `/defer N why: <reason>` (#53) | carryover.test.sh | verified-on-disk |
| `absence-gate.sh` | Stop | Final answer saying "not found / doesn't exist / no such X" needs a search in the same turn or named probes; blocks once; fails open (#76; obs 0034; decision 56). Live install is manual | absence-gate.test.sh | verified-on-disk |
| `subagent-stop-gate.sh` | SubagentStop | Subagent whose spawn prompt names `~/.claude/session-work/<date>/agent-<topic>.md` can't finish while that file is missing or a `- [ ]` Plan step isn't under `## Blocked` (#59). This is the gate that applies to this worker | subagent-stop-gate.test.sh | verified-on-disk |
| `observe-event.sh` (+ `observe-corrections.txt`, `~/bin/observe-dismiss`) | SessionStart `compact`, PostToolUseFailure, PermissionDenied, UserPromptSubmit | Queues friction events; compaction clears `satisfied-<sid>.tsv` (#56) | observe.test.sh | verified-on-disk |
| `state-guard.sh` | PreToolUse `Bash\|Write\|Edit` | obs 0017: refuses agent changes to `~/.claude/state/` enforcement files (#77) | state-guard.test.sh | verified-on-disk |
| `settings-guard.sh` | PreToolUse `Bash\|Write\|Edit` | Agent can't change `~/.claude/settings.json`, `settings.local.json`, `~/.claude.json`; operator uses `!` commands (#77) | settings-guard.test.sh | verified-on-disk |
| `build-doc-gate.sh` | PreToolUse `Bash` + PostToolUse `Read` | obs 0005: install/build commands in a `~/repos/<repo>` blocked until its README/INSTALL/BUILD doc was read (#77) | build-doc-gate.test.sh | verified-on-disk |
| `agent-type-gate.sh` | PreToolUse `Agent` | obs 0023: refuses Explore/Plan spawn whose prompt names a progress file (#77) | agent-type-gate.test.sh | verified-on-disk |
| `delegation-tripwire.sh` | UserPromptSubmit, PostToolUse/PreToolUse `Bash` | obs 0028: non-blocking reminder after >6 Bash calls over >3 repos in a turn (#77) | delegation-tripwire.test.sh | verified-on-disk |
| `auditor/` (`install-auditor.sh`, `settings-snippet.json`) | Stop `type: "agent"` | Opus subagent audits each working turn; `ok:false` on unverified done/fixed/merged claims; reads transcript 8 lines at a time (#72, #74, #75). README says optional/experimental/not installed by default; RESUME says installed live | auditor.test.sh | verified-on-disk; live: stated-in-doc |
| `run-hook.sh` | launcher | Registers all hooks in aesop-xi `.claude/settings.json`; stands down if `~/.claude/hooks/<name>` exists; in cloud sessions runs only secret-guard, branch-current-gate, context-diff (#54). Cloud allowlist leaves out #76/#77 hooks on purpose (open decision) | cloud-standdown.test.sh | verified-on-disk |
| `git-hooks/` (`dispatch`, `pre-commit`, `pre-push`, `post-commit`, `post-checkout`, `post-merge`) | git, every repo (global hooksPath `~/.config/git/hooks`) | gitleaks on pre-commit/pre-push, then repo's own hook; exceptions only via `.gitleaksignore` | NONE by name | verified-on-disk |
| `ENFORCEMENTS.md` / `WRAP-UP.md` | data/protocol | ENFORCEMENTS rows (termux, naming, observer, hooks, npu, wrapup, inventory, vault, graphify, voice, bench...); wrap-up steps 1-8 | n/a | verified-on-disk |

Unbuilt hook specs (vault BOARD-INTAKE "Thread: skills and plugins", from `skill-updates/2026-10-08/proposals/hooks-spec.md`): Item 1 (obs 0017) now built as state-guard (#77); Item 2 (obs 0005) half built, then built as build-doc-gate (#77); Item 3 (obs 0012, list newest sessions) NOT built, operator undecided; Item 4 (obs 0023) built as agent-type-gate; Item 5 (obs 0028) built as delegation-tripwire; Item 6 (obs 0007/0016/0024) built as absence-gate; Item 7 (obs 0006) partly covered; Item 8 (obs 0030) built as H9. BOARD-INTAKE text still lists 1,3,5,6 as "Not built" (dated before #76/#77); aesop-xi RESUME and PENDING say they were installed. Doc conflict, newest (aesop-xi RESUME 2026-10-23, hooks README) wins.

aesop-xi `.claude/settings.json` also contains an ECC plugin hook line (`ecc/2.2.0/scripts/hooks/session-activity-tracker.js ... || true`) (verified-on-disk, grep). TOOLS inventory says ECC's cached hooks are stale/inert since ECC was uninstalled. Flagged because aesop-xi MEMORY/PENDING say ECC not installed.

---

## 3. Skills

Sources: vault `TOOLS-SCRIPTS-HOOKS-INVENTORY.md` §1 (dated 2026-09-10, "by direct inspection"), `handoff/2026-10-23/skills-inventory-report.md`, `.claude/skills/*/SKILL.md`, `skill-updates/PENDING.md`, aesop-xi `skills/*`, aesop-xi `hooks/staged-updates.sh` text.

### 3a. Project skills on disk in the clones

| Skill | Location | What it is | Status |
|---|---|---|---|
| debug-issue | `novaexorpus/.claude/skills/debug-issue/SKILL.md` | code-review-graph MCP debugging procedure | verified-on-disk |
| explore-codebase | `novaexorpus/.claude/skills/explore-codebase/SKILL.md` | graph architecture/community exploration | verified-on-disk |
| refactor-safely | `novaexorpus/.claude/skills/refactor-safely/SKILL.md` | graph-based refactor planning | verified-on-disk |
| review-changes | `novaexorpus/.claude/skills/review-changes/SKILL.md` | graph risk-scored code review | verified-on-disk |
| drive-to-obsidian-migration | `novaexorpus/.claude/skills/drive-to-obsidian-migration/SKILL.md` | Drive -> Termux rclone -> vault pipeline (uses a Google OAuth client_id) | verified-on-disk |
| notebooklm | `novaexorpus/.claude/skills/notebooklm/SKILL.md` | notebooklm-py CLI/API operation (also the "Gemini Notebook" skill) | verified-on-disk |
| task-observer | `novaexorpus/.claude/skills/task-observer/` (SKILL.md plus README, USER-GUIDE, references/, scripts/, LICENSE CC BY 4.0, by Eoghan Henn / rebelytics) | session-start observation skill; operator fork `c10vis-poem/aesop-task-observer` | verified-on-disk |
| aesop-voice-pipeline | `aesop-xi/skills/aesop-voice-pipeline/` (SKILL.md, `scripts/{run_voice_loop,setup_geniex_bench,setup_whisper_parakeet}.sh`, `references/htp-backend-mismatch.md`) | mic->VAD->STT->TTS loop and NPU/STT bench setup; skill refers to a `VoiceEngine` class that was never written (voice brief) | verified-on-disk |
| corpus-batch-processing | `aesop-xi/skills/corpus-batch-processing/SKILL.md` | orchestrator+subagent raw/ -> clean_md/ | verified-on-disk |
| corpus-verify | `aesop-xi/skills/corpus-verify/SKILL.md` | independent RLVR check of cleaning | verified-on-disk |
| termux-helper | `aesop-xi/skills/termux-helper/SKILL.md` | Termux on-device AI stack (llamad port 8081, aesopd port 8765, NPU Part 2) | verified-on-disk |
| memory-as-skill | `novaexorpus/Skills/memory-as-skill/SKILL.md` | vault copy; also a "local addition" in the obsidian-skills clone on the phone | verified-on-disk |
| Skills/ plugin-management 0.2.2 | `novaexorpus/Skills/Plugin Management-0.2.2-v39/` (10 files) | vendored plugin management skills | verified-on-disk (contents not read) |
| Skills/ others | `ECC_skills_strategic-compact_SKILL.md at main - affaan-m_ECC.md`, `Happy Ending - AI skill - skills-for-ai.mht`, `llm-wiki-compiler-NvAEx.md`, `SKILL.md`, `POINTER.md` | captured pages | verified-on-disk (16 files total in `Skills/`) |

Inventory section "Project-specific skills (7, confirmed real)" (TOOLS inventory §1, 2026-09-10): corpus-batch-processing and corpus-verify at `~/.claude/skills/` (global); drive-to-obsidian-migration at `~/repos/NovA-Corpus/.claude/skills/`; openspec-apply-change / -archive-change / -explore / -propose at `~/repos/NovA-terrestrial-brain/.claude/skills/` (TB dropped). stated-in-doc, 2026-09-10, predates the drops.

### 3b. Vendor / third-party skills and packs (phone state, stated-in-doc)

From `skills-inventory-report.md` (2026-10-23, read-only, config-inferred):

| Pack | Local path (phone) | Fork | Skills | Installed? | Behind/ahead | Status |
|---|---|---|---|---|---|---|
| obsidian-skills (kepano) | `~/repos/obsidian-skills` | obsidian-skills | 6 upstream (defuddle json-canvas knap bases cli markdown) + local adds aesop-wiki, horizons-repo-skill, memory-as-skill, termux-helper | yes, `obsidian@obsidian-skills` 1.0.1 enabled | 0 / 4 | stated-in-doc |
| obsidian-wiki (Ar9av) | `~/repos/AEsops-obsidian-wiki` | AEsops-obsidian-wiki | 40 in `.skills` | project scope (wiki-admin) only; not in enabledPlugins | 25 behind | stated-in-doc |
| openwiki-for-claude-code | `~/repos/NvAEx-openwiki-for-claude-code` | yes | 4 (ask generate schedule update) | installed user + wiki-admin v0.1.0, `enabledPlugins=false`; OpenWiki DROPPED | 0/0 | stated-in-doc |
| openwiki-skills (kinensake) | not cloned | NvAEx-openwiki-skills | unknown | no | 0/0 | stated-in-doc |
| openwiki (langchain) | `~/repos/openwiki` | openwiki | 4 SKILL.md; bare `~/.claude/skills/openwiki` | skill dir only | n/c | stated-in-doc |
| llm-wiki-nocode (rosidotidev) | `~/repos/NvAEx-llm-wiki-nocode` | yes | 0 SKILL.md, 3 commands | no | 0/0 | stated-in-doc |
| llm-wiki-compiler (ussumant) | `~/repos/llm-wiki-compiler-NvAEx` | yes | 1 | project scope v2.1.0, not enabled | 0/0 | stated-in-doc |
| Obsidian Tars | not cloned | AEsopXi-obsidian-tars | 0 (Obsidian app plugin) | no | 0/0 | stated-in-doc |
| graphify | `~/repos/graphify` | graphify | bare skill `~/.claude/skills/graphify` (listing denied) | skill yes, not a plugin | 330 behind | stated-in-doc |
| notebooklm-py | `~/repos/notebooklm-py` | notebooklm-py | 1 root SKILL.md + bare `~/.claude/skills/notebooklm` | skill yes, not a plugin | 18 behind | stated-in-doc |
| honey-for-devs | `~/repos/NoVa-honey-for-devs` | NvAEx-honey-for-devs | ~14 | yes `honey@greenpt` 1.4.0 enabled; bare `~/.claude/skills/honey*` symlinks point at stale 1.3.1 | 0 / 5 | stated-in-doc |
| mem0 plugin | `~/repos/clovis-mem0-vingiaN` | yes | plugin mem0 0.3.3 | enabled at report time; DROPPED 2026-10-23 | 3 behind / 9 ahead | stated-in-doc |
| MemVault | not cloned | fork created later 2026-10-23 | n/a | no | | stated-in-doc |
| claude-mem | not cloned | fork created later | n/a | no | | stated-in-doc |
| agentmemory (rohitg00) | not cloned | fork created later | n/a | no | | stated-in-doc |
| pmm | account-synced plugin (anthropic-plugin-directory) | none | 12 `pmm:*` skills | yes (synced from claude.ai account) | | stated-in-doc |
| memsearch | `~/repos/memsearch-aesop` | yes | 17 SKILL.md | no | 17 behind | stated-in-doc |
| terrestrial-brain | `~/repos/NovA-terrestrial-brain` | NvAEx-terrestrial-brain | not checked | MCP server (timed out), DROPPED | 0 / 7 | stated-in-doc |
| OB1 | `~/repos/OB1` | OB1 | 26 SKILL.md | no | n/c | stated-in-doc |
| pm-claude-skills | `~/repos/pm-claude-skills` | yes | not counted | no | n/c | stated-in-doc |
| honey + 13 satellites | `~/.claude/skills/honey*` (honey-ccr, -chat, -compress, -debt, -design, -eco, -gain, -hive, -loop, -memory, -px, -review, -superpowers) | | | "Active, plugin installed" as of 2026-09-10 | | stated-in-doc (TOOLS inventory §1) |
| code-review-graph (MCP, 30 tools) | MCP connector | | | Connected 2026-09-10; registered repos then: aesop-xi, NovA-terrestrial-brain; "not NovAExorpus" | | stated-in-doc |
| reverse-skill / NoVa-reverse-skill | `~/repos/NoVa-reverse-skill` | | routing repo read via its AGENTS.md/RULES.md | not a skill/MCP | | stated-in-doc |
| technical-builder-style | `/storage/emulated/0/archive/technical-builder-style.SKILL.md` | | | "false lead", unrelated writing-style skill | | stated-in-doc |
| skills-and-capabilities/{code-review-graph,notebook-lmpy,obsidian-skills} | `~/repos/NovAExorpus/skills-and-capabilities/` | | | empty placeholder dirs (2026-09-10) | | stated-in-doc |

Overlap flags in the report: skill-creator, memory-as-skill, termux-helper name collisions; 5 memory paths (mem0, claude-mem, MemVault, agentmemory, pmm) - "do not enable all together"; honey symlinks stale 1.3.1 vs plugin 1.4.0; obsidian-wiki / llm-wiki-compiler / llm-wiki-nocode all Karpathy LLM-wiki pattern. Install plan order: 1 sync obsidian-skills/honey/mem0, 2 sync+refresh obsidian-wiki, 3 openwiki enable decision, 4 manifests for graphify/notebooklm-py/llm-wiki-nocode, 5 new forks for memory packs. The mem0 and OpenWiki items are superseded by the 2026-10-23 drops.

### 3c. Staged updates (vault `skill-updates/`)

Source: `skill-updates/PENDING.md` (verified-on-disk; reconciled 2026-10-23). Files on disk: 6 under `skill-updates/`.

| Staged item | Path | State | Status |
|---|---|---|---|
| android-termux-operator (obs 0004, 0025, 0009: Safety rules) | `skill-updates/2026-10-08/android-termux-operator/{SKILL.md,references/audio-pipeline.md}` | `[installed 2026-10-23]` into live `~/.claude/skills/android-termux-operator/SKILL.md` (no repo source); redaction sed replaced with tested one | verified-on-disk (files), installed: stated-in-doc |
| CLAUDE.md additions A-E (absence claims, subagent progress-file/delegation, auto-merge preflight, long-CI preflight, durable-not-scratchpad) | `skill-updates/2026-10-08/claude-md/CLAUDE.md.additions.md` | `[installed 2026-10-23]` via agents-md-v2 split (A, B in CLAUDE.md; C, D in `~/.agents/AGENTS.md`; E in CLAUDE.md) | verified-on-disk, installed: stated-in-doc |
| Hook specs | `skill-updates/2026-10-08/proposals/hooks-spec.md` | design only; items mapped (see Table 2 note) | verified-on-disk |
| task-observer upstream draft (0015) | `skill-updates/2026-10-08/proposals/task-observer-upstream.md` | NOT sent; operator to send to rebelytics or drop; fix is in fork PR #1 (09a4101) | verified-on-disk |

### 3d. Agents in `.claude/agents/` (vault)

| Agent | Model | Tools | Notes | Status |
|---|---|---|---|---|
| builder | sonnet | Read, Grep, Glob, Bash, Edit, Write, Monitor, SendMessage, Skill, mem0 search/add | Scope names OmniRoute / Terrestrial Brain / VM management and mem0 tools; all DROPPED 2026-10-23, so this file is stale vs the dropped list | verified-on-disk |
| corpus-architect | opus | Read, Grep, Glob, Bash, Edit, Write, WebFetch, WebSearch, Monitor, SendMessage, Skill, 6 mem0 tools | Refs `Drive_sync/LlmWiki/` supersession rule and mem0; mem0 DROPPED | verified-on-disk |

Other skill-like items noted in the docs: the weekly-review `skill-observations/` (see Table 9); `Vendor-Registries/skills-references/mattpocock-ask-matt-SKILL.md` (verified-on-disk); `reverse-engineering/skill_manifest.json` (verified-on-disk); `.skill_manifest_jsonl/` (1 file at vault root).

---

## 4. Plugins and MCP servers

Authoritative drop list: vault `AGENTS.md` "Current stack (2026-10-23)", `RESUME.md` "Dropped", `PENDING.md` "Closed 2026-10-23", aesop-xi `AGENTS.md`/`RESUME.md`: "Dropped, do not set up, test or route through: OmniRoute, mem0, Terrestrial Brain, OpenWiki, Qwen3-VL." (verified-on-disk text). "Strip-and-judge may still mine their ideas" (BOARD-INTAKE). ECC: "used only as a marketplace for individual skills; no fork maintenance"; PENDING 2026-10-23 "Dropped: ... ECC unified-memory and ECC fork upkeep (31)". TOOLS inventory: ECC "intentionally uninstalled by the operator 2026-09-09", but aesop-xi AGENTS.md (older text) says never installed/deferred. vault MEMORY.md and docs disagree on ECC history; either way it is not installed.

| Item | Kind | State per docs | Source | Status |
|---|---|---|---|---|
| OmniRoute (gateway/router; "memory extraction layer" decision 2026-09-05) | gateway / MCP stack, GCP VM :20128 | DROPPED 2026-10-23. Fork NvAEx-OmniRoute (PR #1 merged 2026-10-22). Port 20128 plan and "OmniRoute deploy to GCP VM [P0]" in aesop-xi PENDING are moot | AGENTS "Current stack"; PENDING | stated-in-doc |
| mem0 (MCP + plugin) | memory MCP/plugin | DROPPED. Had live entities `novaexorpus-corpus`, `novaexorpus-test` (2026-09-09) | TOOLS inventory; RESUME | stated-in-doc |
| Terrestrial Brain | MCP server (Postgres :8000/mcp, 23 migrations, Deno) | DROPPED. TB PR #7 merged | aesop-xi PENDING; RESUME | stated-in-doc |
| OpenWiki | wiki generator | DROPPED / retired 2026-10-02 (PENDING 2026-10-22) then dropped "for good" 2026-10-23; `~/openwiki` deleted | PENDING | stated-in-doc |
| Qwen3-VL | model, not a plugin | DROPPED ("we're not using qwen 3vl"); #73 removed from docs; 458 MB partial and Drive zip to delete | PENDING; models-report | stated-in-doc |
| Reasoning Bank wiring | service | DROPPED (aesop-xi AGENTS "Runtime memory stack: DROPPED") | aesop-xi AGENTS | stated-in-doc |
| OB1 (Open Brain) | memory backend | Under strip-and-judge; OB1 plugin drafts recovered at `recovered/2026-09-26-ob1/` (push only if judged worth keeping). Not in the formal "Dropped" list | BOARD-INTAKE | stated-in-doc |
| ECC (affaan-m/ECC fork ECC-aesop) | Claude Code plugin | "ECC deferred"; not installed; marketplace-only for single skills | BOARD-INTAKE; aesop-xi PENDING | stated-in-doc |
| code-review-graph | MCP (30 tools) + skills debug-issue, explore-codebase, refactor-safely, review-changes | ACTIVE in "Current stack: Code intel / graphs: code-review-graph (MCP), graphify". Vault has `.code-review-graph/` (2 files) and `Codebase-Graphs/` (graph.json, graph.html, GRAPH_REPORT.md) | AGENTS; vault dirs | stated-in-doc; dirs verified-on-disk |
| graphify | skill / graph | ACTIVE (code intel; Obsidian+graphify = dashboard). ENFORCEMENTS row requires skill: graphify on keywords | AGENTS; BOARD-INTAKE | stated-in-doc |
| Obsidian + GitSync | vault app + plugin | ACTIVE. GitSync "Portal plugin" syncs on Obsidian startup only; replaced by `vault-ship.sh` upload per hooks README; `.obsidian/` (20 files) on disk | AGENTS; MEMORY | stated-in-doc; `.obsidian` verified-on-disk |
| honey (honey-for-devs, marketplace greenpt) | plugin | ACTIVE 1.4.0 (report); "Honey applies universally" in AGENTS | skills-inventory-report; AGENTS | stated-in-doc |
| obsidian@obsidian-skills 1.0.1 | plugin | enabled | skills-inventory-report | stated-in-doc |
| openwiki@openwiki-for-claude-code v0.1.0 | plugin | installed, disabled; OpenWiki dropped | skills-inventory-report | stated-in-doc |
| llm-wiki-compiler v2.1.0, obsidian-wiki | plugins (project scope: wiki-admin) | installed, not enabled | skills-inventory-report | stated-in-doc |
| claude-video/watch | plugin | "installed" (2026-09-10) | TOOLS inventory §3 | stated-in-doc |
| happy-ending | plugin | hand-registered, enabled (2026-10-22); `.bak-preSymlink` dir to delete | PENDING | stated-in-doc |
| pmm (account-synced) | plugin | active; pmm:* skills | skills-inventory-report | stated-in-doc |
| MemVault, claude-mem, agentmemory, oak-memory-plugin, pmm-plugin | memory plugin candidates | forks created 2026-10-23; "pick ONE auto-capture memory" open | PENDING | stated-in-doc |
| Chrome DevTools MCP (ChromeDevTools/chrome-devtools-mcp) | proposed MCP | proposed for ADB/Chrome Dev; "Android MTP plugin" referent not found | remote-access-report | stated-in-doc |
| Claude Code `playwright` / `browser-use` plugins | MCP plugins | "failed to connect this session" (cause not diagnosed) | remote-access-report | stated-in-doc |
| Render MCP | MCP | Dropped (PENDING item 21) | PENDING | stated-in-doc |
| notebooklm-py / Gemini Notebook CLI | CLI + skill | active as skill; login on tablet pending | remote-access-report | stated-in-doc |
| OmniGlyph | tool | "switch on or drop" open | PENDING | stated-in-doc |
| Jev skills (NvAEx-Jev.skills), REA (NvAEx-rea) | skill forks | review before any install | PENDING | stated-in-doc |
| memsearch, headroom, context7, claude-mem | candidates | forks synced / created | PENDING | stated-in-doc |
| llamad (llama-server :8081), aesopd (WebSocket bridge :8765), npu-serve (GenieX HTTP :18181), MemVault :8092, media :8091, NPU app :8080 | local daemons/ports | port plan 2026-10-01; "own LLM server instead of llama-server"; `~/tools/geniex-serve` shim is the start | aesop-xi MEMORY; RESUME vault | stated-in-doc |
| cross_auditor_orchestrator, tool_call_interceptor (:8088), nanoclaw_router, divergence_detector, run_audit.sh | auditor scripts | "never wired"; superseded by the Stop-hook auditor | TOOLS inventory; aesop-xi INVENTORY | stated-in-doc |

MCP/plugin connectors visible in THIS worker session (not from the docs; context only, not part of operator's stack): not recorded.

---

## 5. Models and weights (phone / nodes)

Sources: `handoff/2026-10-23/models-report.md` (probed 2026-10-23, `find -size +50M`, Drive IDs redacted), `npu-install-plan.md` §4.4, vault `RESUME.md`, vault `LOCKED-DECISIONS-2026-09-05.md`, `profiles/nav.yaml`. All stated-in-doc (phone not mounted here). Base path `Documents/_models/` = `/storage/emulated/0/Documents/_models` = `~/storage/shared/Documents/_models`; not inside an Obsidian vault.

### 5a. `_models/gguf` (all Q4_0 unless noted)

| Model | Quant | Bytes | Path | Target hardware / route | Status |
|---|---|---|---|---|---|
| Qwen3.5-9B-Q4_0.gguf | Q4_0 | 5,379,417,312 | `_models/gguf/` | llama_cpp, NPU HTP0 (dynamic map, then 2 sessions); Drive copy too | local+Drive |
| Qwen_Qwen3.5-9B-Q4_0.gguf | Q4_0 | 5,741,391,904 | `_models/gguf/` | same; different build, not a dup | local+Drive; identity check not done |
| Qwen3.5-4B-Q4_0.gguf (+ mmproj-Qwen3.5-4B-F16.gguf 672,423,616) | Q4_0 | 2,583,221,408 | `_models/gguf/` | operator's multimodal pick (unsloth/Qwen3.5-4B-GGUF), added 2026-10-23, sha256 verified vs HF LFS | local only |
| Qwen3.5-2B-Q4_0.gguf (+ mmproj F16 668,227,264) | Q4_0 | 1,214,873,856 | `_models/gguf/` | AI Hub asset; benchmark model; prior best decode 20.5 tok/s hybrid (v0.3.14) | local+Drive |
| Qwen3.5-0.8B-Q4_0.gguf (+ mmproj F16 204,987,232) | Q4_0 | 507,154,688 | `_models/gguf/` | QDC model | LOCAL ONLY |
| gemma-4-12b-it-qat-q4_0.gguf | Q4_0 | 6,975,877,728 | `_models/gguf/` | 2 HTP sessions (6.98 GB ~ 2 x 3.5 GB) | local+Drive |
| gemma-4-e4b-it-q4_k_m.gguf | Q4_K_M | 5,335,273,760 | `_models/gguf/` | K-quant HTP repack on v0.9.3 | local+Drive |
| gemma-4-E4B_q4_0-it.gguf (+ mmproj-gemma-4-E4B 991,552,256) | Q4_0 | 5,154,941,280 | `_models/gguf/` | Qualcomm AI Hub page: prefill 427, decode 12.4 tok/s | local+Drive |
| gemma-4-E4B-it-IQ4_NL.gguf | IQ4_NL | 4,835,837,088 | `_models/gguf/` | | local+Drive |
| granite-4.0-h-micro-Q4_0.gguf | Q4_0 | 1,860,759,584 | `_models/gguf/` | | local+Drive |
| OpenGVLab_InternVL3_5-8B-Q4_0.gguf (+ mmproj f16 678,065,568) | Q4_0 | 4,787,329,216 | `_models/gguf/` | VLM, mmproj on HTP1 | local only |
| SmolVLM2-2.2B-Instruct-Q8_0.gguf (+ mmproj 592,523,200) | Q8_0 | 1,927,933,984 | `_models/gguf/` | QDC benches it on npu | local only |

### 5b. Other local model files

| Model / bundle | Size | Path | Target / note | Status |
|---|---|---|---|---|
| qairt InternVL3.5-VL 4B zips (8-elite-galaxy, x-elite) | 3.7 GB each | `_models/qairt/{8-elite-galaxy,x-elite}/` | qairt route; "galaxy" = SM8750-AC alias, same v79 | stated-in-doc |
| qairt InternVL3.5-VL 2B zips (all 3 chips: 8-elite-galaxy, x-elite, x2-elite) | 2.4 GB | `_models/qairt/*/` | qairt | stated-in-doc |
| qairt qwen3_1_7b (x-elite) | 1.5 GB | `_models/qairt/x-elite/` | other HTP arch (v73), test-load only | stated-in-doc |
| qairt smollm2_1_7b (x2-elite, 8-elite) | ~1 GB | `_models/qairt/` | | stated-in-doc |
| installed/: intern3_5_vl_4b-8elite (5 parts + vision + embedding), intern3_5_vl_2b-8elite, intern3_5_vl_2b-xelite, whisper-large-v3-turbo-8elite | n/a | `_models/installed/` | unpacked bundles; InternVL 4B on qairt measured decode 15.4-17.1 tok/s (2026-10-02); X Elite 2B 27.5 tok/s with err 5005 | stated-in-doc |
| speech/: whisper_medium, whisper_large_v3_turbo, distil_whisper (onnx / qnn_dlc / tflite), deepspeech2, zipformer x3, melotts x2, pipertts | n/a | `_models/speech/` (RESUME: `stt/` Distil-Whisper QNN/TFLite/ONNX) | STT comparison planned (npu plan step 8-16) | stated-in-doc |
| runtimes/local-ai-v4.10.0-linux-arm64 | 150 MB binary | `_models/runtimes/` | | stated-in-doc |
| gemma-4-12B-it-qat-UD-Q4_K_XL.gguf (+ mmproj-gemma-4-12b-it-qat-q4_0 175,115,264) | 4,267,937,792 local; Drive copy is 6,716,356,800 (DIFFERENT file, same name) | `~/downloads/`, `~/gemma-12b/` | locked decision 6 (2026-09-05) | stated-in-doc |
| gemma-4-E2B-it-qat-UD-Q4_K_XL.gguf | 2,620,368,960 | `~/gemma-e2b/` | local only; Drive has a different E2B_q4_0-it | stated-in-doc |
| qwen3_vl_4b_instruct-geniex_qairt-w4a16-8_elite part3_of_4.bin | 457,768,960 (partial) | `~/models-npu/` | NOT USED; operator to delete | stated-in-doc |
| weights-1-8.nexa (and "(2)") | 770,293,308 / 767,131,196 | `~/downloads/` | .nexa identity unread | stated-in-doc |
| model.onnx (unidentified) | 177,870,108 | `~` | unidentified | stated-in-doc |
| ggml-tiny.en.bin | 77,704,715 | `~/downloads/WhisperInput/...` | | stated-in-doc |
| Vendor-Registries/google-gemma-litert/model.safetensors | 560,571,228 | vault (dup in `_Merovingians_Keep/Zip/Vendor-Registries/`) | | stated-in-doc; folder verified-on-disk |
| hybrid_llama_qnn.pte | 930,694,676 | vault `Drive_sync/Secure-Spark-Proof-Folder .../01_raw_sources (1)/Agent models and assets/` (dup in keep) | | stated-in-doc |
| Proot Debian `/root/models`: kokoro-multi-lang-v1.0/model.onnx 325,630,829; parakeet ggml-parakeet-tdt-0.6b-v3-q8_0.bin 668,757,119; sherpa-onnx-moonshine-base-en-int8 (2 onnx ~100/122 MB); sherpa-onnx streaming-zipformer-en-2023-06-26 encoder int8 71,083,163 | | `containers/debian/rootfs/root/models` | voice stack (Silero VAD, Moonshine, Kokoro) | stated-in-doc |
| GenieX runtime bundles | v0.9.3 at `~/tools/geniex-bench-android-arm64-v0.9.3` (sha OK, skel link done); v0.3.14 (`~/tools/geniex-bench`) and v0.7.1 kept until v0.9.3 proven; shim `~/tools/geniex-serve` | | | stated-in-doc |

### 5c. Drive-only (folder `_models`, id redacted; parent "_agents.md")

gemma-4-E2B_q4_0-it.gguf 3,349,516,256; mtp-gemma-4-E2B-it-BF16.gguf 170,211,200; complete qwen3_vl_4b qairt zip "(2).zip" 3,035,113,774 (NOT USED); duplicate "(1)" copies of Qwen3.5-9B/2B. stated-in-doc.

### 5d. Model roster / profile statements

- profiles/nav.yaml (verified-on-disk): phone local "Qwen3.5-9B-VLM" Q4_0-GGUF via QAIRT/HTP; Jetson local executive "gemma-4-E2B (ONNX)"; cloud auditor "openrouter:z-ai/glm-5.2"; Rubik Pi TTS "kokoro / sherpa-onnx".
- Locked decisions 2026-09-05: POCKET-35B dropped; Gemma 4 12B multimodal on roster (`gemma-4-12B-it-qat-UD-Q4_K_XL.gguf`).
- Operator 2026-10-23: "Qwen family = Qwen 3.5 only"; multimodal 4B = Qwen/Qwen3.5-4B; Gemma 4 E4B LiteRT (`litert-community/gemma-4-E4B-it-litert-lm`) download undecided.
- Voice models: Silero VAD (~2 MB, shipped in assets), Moonshine base-en-int8 (10 s ceiling), Kokoro multi-lang v1.0; candidates from voice research: Supertonic-3 int8, Pocket TTS / Phonon-31m, Parakeet unified-en-0.6b-int8-streaming-560ms, Moonshine tiny-en-quantized-2026-02-27, whistle (Cactus). Research only, nothing fetched.

NPU docs (aesop-xi `docs/NPU-ON-DEVICE.md`, verified-on-disk) facts: SM8750, Hexagon v79; GenieX `llama_cpp` + `qairt` runtimes; bench Qwen3.5-2B Q4_0 v0.3.14 npu 151/16.8, hybrid 177/20.5, v0.7.1 npu 98/2.7 (the 2.7 figure was shown invalid: 7-token EOS run, npu-audit-report). The aesop-xi copy still carries the pre-correction text (line 8 "hybrid ... don't present it as the fast path" is not in this copy; the copy already says hybrid is Qualcomm's fast path). Vault PENDING says NPU-ON-DEVICE.md line 8 was replaced 2026-10-23 and six smaller corrections still need operator OK. Known corrections owed: `GGML_HEX_VERBOSE` should be `GGML_HEXAGON_VERBOSE`; `Documents/Models/` is now `Documents/_models/gguf/`; `Vendor-Registries/GOOGLE _DEV/` does not exist; `llm-wiki/` contents moved. Proof-run result (npu-proof) is on the phone only; the vault RESUME says the log was still running at wrap-up and aesop-xi RESUME says the result is recorded in `AEthX-AEsc/docs/npu-proof/2026-10-23.md` (not readable here).

---

## 6. Hardware nodes

Greek-letter labels not found in docs (see gap 4). Sources: aesop-xi `profiles/nav.yaml`, `deploy/README.md`, `deploy/gcp-vm/README.md`, `deploy/jetson/FLASHING.md`, `deploy/rubik-pi/SETUP.md` (all verified-on-disk), vault PENDING/BOARD-INTAKE/RESUME, remote-access-report, npu docs.

| Node (docs' name) | Hardware | Status | What runs / is planned | Source | Status tag |
|---|---|---|---|---|---|
| Phone ("Alpha"?) | Motorola razr ultra 2025, Snapdragon 8 Elite SM8750, Hexagon v79, Termux (cpuset 0-5 only), Debian + Ubuntu proot, Tailscale Android app | LIVE | Claude Code on the phone with hooks H1-H9 + auditor; GenieX v0.3.14/0.7.1/0.9.3; `npu-serve` (GenieX C-API shim, :18181); llamad :8081; aesopd :8765; voice stack (sherpa-onnx, Moonshine, Kokoro, Silero VAD); models in `Documents/_models`; vault clone (GitSync) at `Documents/NovAExorpus`; adb, tmux, sshd, termux-x11, tigervnc, x11vnc installed; Tailscale CLI/ttyd/code-server NOT installed (2026-10-23) | remote-access-report; npu-install-plan; RESUME | stated-in-doc |
| Tablet ("tablet") | not specified (model unnamed) | operator-stated, unverified | Tailscale app + browser; DroidDesk Debian desktop (Termux:X11 on the same device); NotebookLM login target (Playwright); needs age public key; "Tailscale installed on phone and tablet" (PENDING Dropped item 8); not visible to the worker | remote-access-report; PENDING | stated-in-doc |
| Jetson Orin Nano Super 8GB ("Beta"?) | NVIDIA, JetPack 6.x, 128 GB+ microSD | NOT PROCURED ("hardware not yet procured"; "T3 infra on hold") | Planned T3 hub: Postgres+pgvector (OB1), Redis, OmniRoute, vault bare git `~/vault.git`, small executive gemma-4-E2B ONNX; deploy files exist (`docker-compose.yml`, `first-boot-setup.sh`, `vault-sync-setup.sh`) but target dropped components (OmniRoute, OB1); BOARD-INTAKE infrastructure thread lists it | deploy/jetson; LOCKED-DECISIONS; BOARD-INTAKE | stated-in-doc; files verified-on-disk |
| Rubik Pi (Qualcomm Dragonwing) ("Gamma"?) | Thundercomm | NOT PROCURED | Planned T3 audio/desktop node: sherpa-onnx + Kokoro TTS endpoint :8080 (systemd), shared `~/models/` | deploy/rubik-pi/SETUP.md | stated-in-doc; file verified-on-disk |
| GCP VM ("Delta"?) `omniroute-x86` | project `project-alchemist-490416`, us-central1-a, e2-standard-4 (4 vCPU/16 GB), Ubuntu 24.04, 50 GB pd-balanced, ~$0.134/hr + ~$5/mo disk | EXISTS; operator task "retire the VM" (PENDING "Infrastructure: retire the VM"); "Check cloud billing (VM disks)" routine | OmniRoute control plane, Terrestrial Brain, mem0 stack scripts, Chrome Remote Desktop XFCE, idle-shutdown (30 min) + nightly-stop-4am; all hosted services now DROPPED | deploy/gcp-vm/README.md; PENDING | stated-in-doc; README verified-on-disk |
| "computer" / laptop | not specified | tier T2 | in nav.yaml `computer: tiers: [personal]`; "LAPTOP-TRICK.md" at vault root covers loopback adb; "NvAExinandroid" purpose is an open question | nav.yaml; PENDING | stated-in-doc |
| Cloud (T4) | OpenRouter `z-ai/glm-5.2` auditor; GCP enterprise "walled training"; object-store vault backup | planned | auditor decision (isolation vs cloud GLM-5.2) listed unresolved; the realised auditor is now a Claude Stop-hook subagent | nav.yaml; ARCHITECTURE §9; LOCKED-DECISIONS | stated-in-doc |

Architecture note: ARCHITECTURE.md (aesop-xi, verified-on-disk) is device-agnostic tiers T1 edge, T2 personal, T3 home, T4 cloud; its memory design (OpenWiki, OB1, ReasoningBank, OmniRoute) is largely superseded by the 2026-10-23 drops (aesop-xi AGENTS.md now points to the vault). The Docker compose, nav.yaml and deploy READMEs have NOT been updated to the drops.

---

## 7. Accounts, credits, subscriptions, keys (names only; no values read or printed)

I read no `.env`, `~/.claude.json` or secret file; names below come from prose in docs.

| Name | Where named | What for | Status |
|---|---|---|---|
| GitHub account `c10vis-poem` (operator <operator-email>; org/user hosting all forks) | vault AGENTS; LOCKED-DECISIONS "Owner: c10vis-poem" | all repos; gh authenticated on phone as c10vis-poem (voice brief) | stated-in-doc |
| `OPENROUTER_API_KEY` | PENDING Open (secrets) | OpenRouter; old key "lost with ~/.openwiki"; operator must make a new one at openrouter.ai/settings/keys | stated-in-doc |
| `HF_TOKEN` | PENDING | Hugging Face | stated-in-doc |
| `QAI_HUB_API_TOKEN` | PENDING | Qualcomm AI Hub | stated-in-doc |
| `TYPESAFE_API_KEY` | PENDING | TypeSafe (Jev skills sends data to TypeSafe; "which key" under review) | stated-in-doc |
| sops+age secret store in private repo `NvAEx-Recaps` (`nvaex-secret`); a second age key; tablet age public key | vault AGENTS; PENDING | secret storage | stated-in-doc |
| `VAULT_DISPATCH_TOKEN` (repo secret in aesop-xi) | aesop-xi MEMORY 2026-10-05 | `notify-vault.yml` dispatch (now no receiver) | stated-in-doc |
| `PYPI_API_TOKEN` + `environment: pypi` | branch-review §4 | upstream code-review-graph publish workflow (only on release) | stated-in-doc |
| mem0 API key (`~/.claude/plugins/data/mem0-mem0-plugins/api-key`) | aesop-xi PENDING | mem0 plugin; dropped | stated-in-doc |
| `TB_MCP_URL` / `TB_MCP_KEY`, `OMNIROUTE_URL`, OmniRoute keys (`omni-keys.sh`), mem0 env | aesop-xi PENDING; deploy/gcp-vm/stack scripts | dropped stack; "move plaintext .env keys (OpenRouter, mem0, OmniRoute) into NvAEx-Recaps/secrets" | stated-in-doc |
| `~/.hermes/.env` keys | PENDING "import or not" | Hermes agent; not read by anyone (secret-guard) | stated-in-doc |
| `~/.credential-quarantine-2026-08-17/` | PENDING | delete or keep question | stated-in-doc |
| Claude subscription (claude.ai Pro/Max/Team/Enterprise login) | remote-access-report | needed for Claude Remote Control; "API keys unsupported"; Claude Code also runs on the phone (Opus 5.5 per RESUME) | stated-in-doc |
| Anthropic API / Fable access ("Fable consent") | anthropic-research-report; BOARD-INTAKE | advisor/auditor model options (Fable $10/$50, Opus 5.5 $4/$20 per MTok per research report) | stated-in-doc |
| Google account(s): Drive (many folders), Google Cloud project `project-alchemist-490416`, Google Cloud OAuth client for rclone, Google AI Studio ("operator's API"), Gemini, NotebookLM session cookies (`storage_state.json`, `master_token.json`) | drive-to-obsidian skill; gcp-vm README; voice brief; remote-access-report | "Google visibility ... accounts/credits/services" vendor README pattern (locked decision 8, 10) | stated-in-doc |
| Tailscale account/tailnet | remote-access-report | private network; ttyd auth password (`-c operator:...` placeholder in doc) | stated-in-doc |
| Cloud billing for VM disks (GCP) | PENDING routines | recurring check; `*BILLING*.csv` gitignored; billing material kept in `Documents/private-memory/` | stated-in-doc |
| GitHub Actions secrets (release signing key later), gitleaks CI, GitHub secret scanning / push protection | voice brief; AGENTS GH workflow | | stated-in-doc |
| "Credits": no credit balances are stated anywhere in the files I read | grep for credit | `google` vendor README should list "credits/expirations" per locked decision 8; the README files themselves were not found in the read set | not found by grep of the listed docs |
| Other vendor accounts named in locked decision 11 as top-level folders: google/, qualcomm/, nvidia/, github/, anthropic/, primeintellect/, deepseek/ | LOCKED-DECISIONS | hybrid-structure plan 2026-09-05, "post-tonight"; not built | stated-in-doc |

---

## 8. Tools and scripts

### 8a. Per TOOLS-SCRIPTS-HOOKS-INVENTORY.md (compiled 2026-09-10, SD-card mirror and phone, "25 total")

| Item | Where (per doc) | Purpose | Status |
|---|---|---|---|
| `run_audit.sh` | `aesop-xi/tools/`, `NovAExopia/tools/` (SD-card mirror, uncommitted then) | "Incognito Red Auditor" daemon: watch incoming JSONL, validate, move approved/quarantined | doc says exists; aesop-xi `tools/run_audit.sh` present now: verified-on-disk |
| `divergence_detector.py` | same | flags tool-bypass/protected-path violations; "never wired" | verified-on-disk in aesop-xi/tools |
| `cross_auditor_orchestrator.py` | same | ClearanceTokens, SQLite audit ledger | verified-on-disk in aesop-xi/tools |
| `tool_call_interceptor.py` | same | telemetry :8088 | not in aesop-xi/tools listing (not found by `ls aesop-xi/tools`) |
| `nanoclaw_router.py` | same | keyword router with stale placeholder registries | not in aesop-xi/tools listing |
| `htp_partition_calc.py` | same | Hexagon NPU domain split (`D=HTP0,HTP1`) | PENDING/BOARD-INTAKE: "never existed"; reference to restore or drop |
| raw_database tools (13 listed) | `raw_database/tools/` | `voice_bot.py`, `live_voice_loop.py`, `kokoro_tts.py`, `stt_test.sh`, `nanobot_from_scratch.py`, `validate_repo_integrity.py`, `crawl_agent_vault.py`, `setup-aesop.sh`, `gcp_cross_account_handshake.sh`, `scaffold_cognitive_repository_architecture.sh`, `failures.sh`, two `gemini-code-*.sh` | verified-on-disk (`ls raw_database/tools`: 14 files incl. POINTER.md) |
| `.migrate/` pipeline (7) | `Drive_sync/.../.migrate/` and vault `.migrate/` (8 files) | `process_folder.py`, `dedup.py`, `build_rag_chunks.py`, `build_rag_index.py`, `query_rag.py`, `verify_corpus.py`, `audit.py` | `.migrate/` 8 files verified-on-disk; names stated-in-doc |
| `agent_panel.sh` | `NovAExopia/aesc/scripts/` | mobile workspace panel, placed 2026-09-10 | stated-in-doc |
| `system_housekeeper.sh` | would be in `NovAExopia/aesc/scripts/` | "Known real gap"; later list: `system_housekeeper.sh.txt`, `compile_manifest.py.md`, `doc_to_skill_and_tool.py.md`, `htp_partition_calc.py` = "4 missing tool references" (PENDING Open "Small calls") | stated-in-doc |
| `regenerate_masters.sh` / `build_masters.sh` / `master-files.yml` / MASTER-* | | RETIRED 2026-10-20; post-commit hook removed 2026-10-05 | stated-in-doc (MEMORY) |
| `~/bin/sync-forks`, `~/bin/ship-session` | phone | AGENTS GH workflow enforcement (older); replaced by hooks `sync-on-use.sh` and `ship-session.sh` | stated-in-doc |
| `~/bin/{resume-item, observe-dismiss, vault-ship, npu-ask, npu-serve, models, ai-web, ai-stop, talk, vv, speak, nx, ax}` | phone / `aesop-xi/deploy/phone/bin/` | shortcuts; `nx`, `ax` listed broken/stale in aesop-xi INVENTORY | `deploy/phone/bin/` 8 files verified-on-disk |
| `~/tools/{geniex-bench*, geniex-serve, llama-hexagon, llama-mixed, whisper-parakeet, npu-proof.sh, dl-geniex}` | phone | NPU/benchmark tools | stated-in-doc |
| `~/bin/npu-run`, `npu-queued`, `NvAEx-Recaps/npu/` | phone / private repo | NPU job queue | stated-in-doc |

### 8b. On disk in the clones

| Path | Files | Contents | Status |
|---|---|---|---|
| `novaexorpus/tools/` | 9 | POINTER.md, `bootstrap.sh`, `check.py`, `chunk.py`, `clean.py`, `launch.sh`, `vm-connect.sh`, `vm-install.sh`, `vm-reconnect.sh` | verified-on-disk (names; not run or read in full) |
| `novaexorpus/Scripts/` | 4 | POINTER.md, `dsh-termux-shim.sh`, `install-dsh-alpine.sh`, `install-openwiki-alpine.sh` | verified-on-disk |
| `novaexorpus/benchmarks/results/` | 2 | `2026-<drive-id>.log`, `2026-10-02-t1-Qwen3.5-0.8B-Q4_0.gguf.json` | verified-on-disk |
| `novaexorpus/.migrate/` | 8 | migration pipeline | verified-on-disk |
| `aesop-xi/tools/` | 9 entries | `aesop-tmux.sh`, `bootstrap.sh`, `cross_auditor_orchestrator.py`, `divergence_detector.py`, `gcloud-setup.sh`, `omniroute/{start,stop}.sh`, `run_audit.sh`, `setup-graph-pipeline.sh`, `vm-startup-script.sh` | verified-on-disk |
| `aesop-xi/scripts/` | `bootstrap-stack.sh`, POINTER.md | stack bootstrap (Termux failure triage 2026-09-06) | verified-on-disk |
| `aesop-xi/voice-engine/scripts/` | live_voice_loop.py, run_live.sh (per voice brief) | Python voice loop (temporary; to be removed once Æyre native round-trips) | `voice-engine/` verified-on-disk |
| `aesop-xi/deploy/phone/` | 27 files: `boot.sh`, `setup-voice.sh`, `stt_process.py`, `tts_speak.py` (fails on Kokoro v1.0 multi-lang, operator: leave), `vad_monitor.py`, `bin/` (8), `bridge/` (1), `commands/` (defer, ok, reject, wrapup .md), `daemons/` (`install-daemons.sh`, `llamad-run`), `geniex-serve/` (`geniex.h`, `geniex-v0.7.1.h`, `models.json`, `server.py`, `shim.c`), `archive/` | verified-on-disk |
| `aesop-xi/deploy/gcp-vm/` | 25 files: `01-base.sh`, idle-shutdown + .service + .timer, `phone/` (close-firewall, fix-tb-check, merge-mem0, openwiki-update, vm), `stack/` (15: code-review-graph.sh, compose.yaml, initdb, install-plugins.sh, make-env.sh, make-mem0-env.sh, mcpcall.sh, mcptest.sh, mem0-bootstrap.sh, omni-keys.sh, omniroute, schemas.sh, tb-schema.sh, terrestrial-brain.sh, vault-sync.sh) | verified-on-disk; most target dropped stack |
| `aesop-xi/deploy/jetson/` | 5 | `.env.example`, `FLASHING.md`, `docker-compose.yml`, `first-boot-setup.sh`, `vault-sync-setup.sh` | verified-on-disk |
| `aesop-xi/deploy/rubik-pi/` | 1 | `SETUP.md` | verified-on-disk |
| `aesop-xi/deploy/init/` | 1 | `ob1-schema.sql` | verified-on-disk |
| `aesop-xi/deploy/` depth 2 totals | gcp-vm 25, init 1, jetson 5, phone 27, rubik-pi 1 (+ README.md) | | verified-on-disk |
| aesop-xi `protocol/` | 5 docs: bridge-protocol, classify, memory, orchestration-contract, tiers | | verified-on-disk |
| aesop-xi `profiles/` | `nav.yaml`, `_example.yaml` | | verified-on-disk |
| aesop-xi `docs/` | INVENTORY.md, NPU-ON-DEVICE.md (both read), LOCAL-AI-GUIDE.md, NPU-SERVE-BUILD-LOG.md (not read) | | verified-on-disk |
| aesop-xi `policies/`, `arbitration/`, `HTP/`, `pending/`, `archive/`, `audit/`, `raw/`, `clean_md/`, `wiki_md/` | stubs / data | `policies` holds `02_DUMBASS_UNIVERSAL_MEMORY_SPEC.md.txt` (stated in 02, unverified) | verified-on-disk |
| Known-broken per aesop-xi `docs/INVENTORY.md` (2026-10-01) | dead path `~/novae-xorpus`, dead `~/aesop`, deleted clone refs, ECC cache refs, `~/bin/ax` missing manifest, CRLF `run_audit.sh`, `smart-grep-hook.sh` not in settings | corpus-verify frontmatter; duplicate skills | stated-in-doc |

---

## 9. Corpus stats (vault `/home/user/novaexorpus`, verified-on-disk, counts via `find -type f`, `.git` excluded)

- Total files in clone (excluding `.git`): 4,479. Markdown files (`*.md`): 2,943. Top-level loose files: 31. Vault AGENTS says "~4,500 files" in your brief; AGENTS Rule 4 says "~4,000 markdown files" (operator estimate 2026-09-28; disk shows 2,943 `.md`).
- `manifest.jsonl`: 585 lines (matches AGENTS Rule 4 "585 converted files"). `chunk.jsonl`: 3,135 lines. `raw_database/manifest.jsonl` 5 lines; `raw_database/chunk.jsonl` 5 lines; aesop-xi `manifest.jsonl` 5 / `chunk.jsonl` 5 lines.
- `GRILL-MANIFEST.md` exists at root (AGENTS Rule 4 says it is empty; not checked).
- Observation log: `skill-observations/observation-log/` = 8 observation files (0012, 0038, 0039, 0040, 0041, 0042, 0043, 0044) plus `archive/` with 51 files. `skill-observations/` total 73 files. Vault RESUME says "19 active entries; open 0038-0041; parked 0012" and vault AGENTS/PENDING mention observations 0038-0041; on disk additional 0042, 0043, 0044 exist (newer than RESUME). The "19 active" figure is NOT reproduced on disk.

### Counts by top-level directory (files, recursive)

| Dir | Files | Dir | Files |
|---|---|---|---|
| Drive_sync | 1,463 | .obsidian | 20 |
| raw_database | 846 | reverse-engineering | 17 |
| clean_md | 555 | Skills | 16 |
| 02_wiki_md | 538 | recovered | 15 |
| __RESUME.md | 515 | 01-sources | 13 |
| global-documentation-vault | 138 | handoff | 10 |
| skill-observations | 73 | docs | 10 |
| Vendor-Registries | 57 | tools | 9 |
| .claude | 50 | .migrate | 8 |
| .gemini | 8 | OpenWiki_sync | 7 |
| 01_raw_sources | 6 | skill-updates | 6 |
| handoffs | 5 | Markor | 5 |
| .clawness | 5 | grill | 4 |
| audit | 4 | Scripts | 4 |
| HTP | 4 | 03_recall_cache | 4 |
| 04_skills_runtime | 4 | 05_episodic_logs | 4 |
| raw | 3 | Codebase-Graphs | 3 |
| llm-wiki | 2 | google_agentic_ai | 2 |
| benchmarks | 2 | .github | 2 |
| .code-review-graph | 2 | wiki_md | 1 |
| termux | 1 | pending | 1 |
| hooks | 1 | archive | 1 |
| agents | 1 | _res | 1 |
| .skill_manifest_jsonl | 1 | .NovAExorpus | 1 |

(Dirs not in this table are empty or absent. Also on disk at the top level: `HTP`, `LAPTOP-TRICK.md`, `GRILL-MANIFEST.md`, `session-failures-2026-09-07.md`, `CLAUDE.md.original.md`, `00_...V3_COMPLETE.md(.bak)`, `01_`..`05_` doc files, `README.md`, `__RESUME.md/`, `Drive_sync/`.)

### Requested individual dirs

| Dir | Files | `.md` | Immediate subdirs / notes |
|---|---|---|---|
| `01_raw_sources/` | 6 | 5 | `Agent models and assets`, `media`, `pdf`, `text`, POINTER.md. NOT the same as `01-sources/` |
| `02_wiki_md/` | 538 | 538 | `INDEX.md`, architectures, concepts, entities, references, vendors (129 files under vendors/qualcomm per npu plan) |
| `03_recall_cache/` | 4 | 4 | POINTER.md, jsonl, kv_store, vectors |
| `04_skills_runtime/` | 4 | 4 | POINTER.md, policies, prompt_skills, runtimes |
| `05_episodic_logs/` | 4 | 4 | POINTER.md, hygiene_reports, rlvr_verifiers, trajectories |
| `01-sources/` | 13 | 3 | single subdir `DRIVE_FILES_MGMT16` (corpus pipeline `01-sources -> 02-clean -> 03-check` per TOOLS inventory) |
| `clean_md/` | 555 | 541 | no subdirs (flat) |
| `raw/` | 3 | 2 | `MASTER_SCRIPTS_REGISTRY.md.txt`, `POINTER.md`, `Standardized UNIX socket protocol,.md` |
| `wiki_md/` | 1 | 1 | POINTER.md only |
| `Drive_sync/` | 1,463 | 772 | `Original_Corpora` 772, `Secure-Spark-Proof-Folder ` 464, `__RESUME.md` 221, `README` 5, `-InBox` 0 (empty); most not read per RESUME |
| `raw_database/` | 846 | 631 | `Dump` 588, `raw` 96, `clean_md` 93, `tools` 14, `02_MY_ORIGINALS` 13, `skills` 4, `Drive` 2, `scripts` 1, `hooks` 1; 15 subdirs; matches TOOLS inventory "106->97 files" loosely (raw 96, clean_md 93 now) |

### Listing of requested vault directories (depth 2, file counts; from the Skills.../recovered pass)

- `Skills/` 16: Plugin Management-0.2.2-v39 (10; `.claude-plugin/`, LICENSE, `skills/` 8), `memory-as-skill/SKILL.md`, ECC strategic-compact page, Happy Ending mht, llm-wiki-compiler page, SKILL.md, POINTER.md.
- `skill-updates/` 6: see Table 3c.
- `Vendor-Registries/` 57: `agents-gateways` 2 (OmniRoute wiki, agent gateway overview), `google-gemma-litert` 16 (Gemma 4 pages, LiteRT, LiteRT-LM mht, model.safetensors), `guides` 2 (LOCAL-AI-GUIDE.md, operator_guide.md), `huggingface-smolvlm` 2, `internvl` 1 (paper 2508.18265v2), `opencode` 1, `piper` 1, `qualcomm-ai-hub` 20 (GenieX-Android-docs 3, GenieX-Chat-App 1, speech 8, model cards: Granite-4.0-Micro, Intern3.5-VL-4B, Llama-3.2-3B-Instruct-SSD, Qwen3-1.7B, Qwen3.5-2B, SmolLM2-1.7B x2, VoiceAI_ASR release note), `qwen` 9, `skills-references` 1, plus README (6).md, README (8).md.
- `Codebase-Graphs/` 3: GRAPH_REPORT.md, graph.html, graph.json.
- `google_agentic_ai/` 2: Gemini Enterprise Agent Platform page; Deploying GEMMA4&GeminiFLASH page (both the same vertex rag-engine notebook capture).
- `llm-wiki/` 2: a "Metacognitive Indexing vs. Procedural Skills" note and the llm-wiki-compiler-NvAEx page. (Hexagon_SDK_Linux.zip no longer here; at `_Merovingians_Keep/NovAExorpus-nested-mirror/llm-wiki/`, phone.)
- `reverse-engineering/` 17: CLAUDE.md, README.md, llm_wiki.md, skill_manifest.json, `duplicates-review/` 2, `research/` 11 (AI-Agents-Projects-Tutorials, CLAUDE.CODE-ANDROID_REV.ENG_, CQRS pattern, Edge overlay AI & Off-Grid AI 2, How to Build a Custom Agent Harness x2, Kotlin SDK, MLC LLM, VIA_BROWSER, Web guidance skill repo).
- `termux/` 1: `main/TMUX_ASSISTANT-RESURRECT/` (1 file).
- `tools/` 9, `Scripts/` 4, `benchmarks/` 2, `recovered/` 15 (see Table 8b; `recovered/2026-09-26-ob1/` 11 files incl. READING-NOTES.md, README.md, aesop-xi-contract, aesop-xi-vm, omni-feat (7); `recovered/2026-10-23/` 4: README.md + ai-hub-merovingian-models- docs (horizons-sotu.md, architecture-verify report) + claude-skills/horizons/index.html, secret scan clean).

---

## 10. Open items and decisions pending (verbatim titles / bullets)

### 10a. `PENDING.md` (vault, verified-on-disk), "Open" (moved 2026-10-23)

Routines (last-housekeeping: 2026-10-23):
- "Roll _recaps/ older than 30 days into a monthly summary, delete the originals"
- "Audit repos: uncommitted / unpushed / stray branches → merge or discard with the builder"
- "Review the task-observer observation log"
- "Check cloud billing (VM disks)"
- "Builder reminders: (add here)"

**Operator to run / decide** (verbatim lead phrases):
- "Secrets (plain Termux tab, one at a time): `nvaex-secret set OPENROUTER_API_KEY` ... `HF_TOKEN`, `QAI_HUB_API_TOKEN`, `TYPESAFE_API_KEY`; then commit + push `NvAEx-Recaps` (branch, PR, auto-merge)."
- "Deletes (operator): `~/storage/shared/Documents/_models/models-npu/qwen3_vl_4b_…_8_elite` (458 MB partial), `~/downloads` DeepChat / SocketSweep / llama-macos tarballs (keep or delete `Claude Setup.exe`: undecided), `~/repos/happy-ending/.agents/skills/happy-ending.bak-preSymlink` ... Drive: Qwen3-VL zip."
- "Starter principles: pick numbers to import from `handoff/2026-10-23/principles-match.md` (2 full matches, 6 partial, 21 none)."
- "Hook 3 (list newest sessions across all `~/.claude/projects/*` at start; obs 0012): build or drop."
- "Small calls: task-observer upstream draft (send or drop); 4 missing tool references (`htp_partition_calc.py` etc.); OmniGlyph (switch on or drop); pick one auto-capture memory (MemVault / claude-mem / agentmemory / pmm); Gemma 4 E4B LiteRT (`litert-community/gemma-4-E4B-it-litert-lm`, no QAT/NPU file listed): download or not."
- "Answers owed: "babbly" STT name; graphify NotebookLM plugin link; tablet age public key; `~/.credential-quarantine-2026-08-17/` delete or keep; import `~/.hermes/.env` keys or not; what `NvAExinandroid` is for."
- "Infrastructure: retire the VM, second age key, NotebookLM login on the tablet (steps in BOARD-INTAKE infrastructure thread)."
- "Leave alone: `Horizon-s-home-grid` PR #1 (operator 2026-10-23)."

**Agent work (next session)**:
- "NPU: read the proof-run summary in `~/.claude/session-work/2026-10-23/npu-proof-*.log` ... then the plan's steps 8-16: Qwen3.5 2B/4B A/B, InternVL bundles vs Qwen3.5-4B vision bench, Distil-Whisper QNN vs TFLite vs ONNX ... K-quant placement on v0.9.3. The six smaller NPU-ON-DEVICE.md corrections need the operator's OK each (`handoff/2026-10-23/npu-install-plan.md` §5)."
- "Jev: review fork `c10vis-poem/NvAEx-Jev.skills` ... before any install; REA fork `NvAEx-rea` likewise."
- "Observations open: 0038 (value review before delete offers), 0039 (never bundle a turn-off), 0040 (subagent scope clause), 0041 (encode delete ordering in the command). Each proposes a rule or check; build in Aesop-Xi."

Closed sections present: "Closed 2026-10-23", "Closed 2026-10-22" (long done/stale/moot lists, not reproduced).

### 10b. `BOARD-INTAKE.md` (vault, verified-on-disk, dated 2026-10-23)

Section titles (verbatim): "Decisions recorded 2026-10-23 (operator)"; "Thread: NPU"; "Thread: wiki-admin agent package"; "Thread: apps (Jetpack Compose, Material 3)"; "Thread: skills and plugins"; "Thread: infrastructure".

Decision bullets (bold lead-ins, verbatim): "Repo layout:" (NovusAExenti = modular agent packages; NovAExopia = capabilities; Aesop-Xi = orchestration; skill stack becomes a customized plugin/mod; no NvAEx-agentk org); "Strip-and-judge strategy:"; "Grill:" (per-thread grill sessions in Claude Projects threads (Fable), cloud orchestrator, after the board of directors exists); "Dashboard:" (Obsidian + graphify combined; custom dashboard from operator's template; both get Android MTP and Chrome DevTools plugins); "Success tracking"; "Architecture (operator, repeated ~10 times; logged verbatim 2026-10-23):" ("files as infrastructure; agents as packages; plugins as configurations; repos as marketplaces; ..."); "Apps:" (three separate APKs; Hyperion-XI hosts tiles; voice-stack API own runtime/repo, decide standalone vs inside Hyperion-XI or terminal APK); "llama-server:" (not used; build own, `~/tools/geniex-serve`); "Wiki-admin agent package"; "Orchestration audit:"; "Corpus uses pointers".

Thread items: NPU (audit report; "Restart one model at a time with the operator; Qwen 3.5 9B/2B wiring, GenieX HTTP wrapper, npu-serve InternVL/tool calls/multi-image, TFLite/LiteRT + Q4_0 requant, 3-tier bench"; "NPU job queue: NvAEx-Recaps/npu/ + npu-run + npu-queued"); wiki-admin ("Finish the wiki-admin build as an agent package and install it in NovusAExenti"; "the RESUME 'PHASES 1-4 COMPLETE' claim is stale; 6 repos are pointer stubs"); apps (voice engine in-app API brief, "Terminal APK (Android Local Desktop), Horizons 3-APK plan", "Obsidian plugins: OB1 and OmniRoute plugins under strip-and-judge; push recovered drafts"); skills and plugins ("H7 classifier ... point classify.sh at a model"; "Missing tools: htp_partition_calc.py (never existed), system_housekeeper.sh.txt, compile_manifest.py.md, doc_to_skill_and_tool.py.md"; "OmniGlyph switch-on decision"; "Unbuilt hook specs" items 1-8, see Table 2 note); infrastructure ("Jetson / Rubik Pi (not procured): T3 infra, MemVault, OB1 Jetson backend, TB Postgres move, Acode + dsh, desktop"; "Spark backlog (from raw_database/spark_recommendations/ 00-11): FastRPC thermal hook, audit_ledger.db sync to Jetson, 24 h HMAC rotation; NX-01/02/03/05; novus rolling_habits.json to SQLite, Car Wash harness; SKILLS-01..04"; "Secrets: move plaintext .env keys ... into NvAEx-Recaps/secrets and read them via nvaex-secret"; "Hardware brainstorm").

### 10c. Other pending lists

- aesop-xi `PENDING.md` (verified-on-disk) headings: "Added 2026-10-02" (npu-serve tool calls / first image only / InternVL 2B in models.json / `tts_speak.py` fails on Kokoro v1.0 / "Hooks for other agents: Hermes / dsh don't get H1-H7"), "Blocking / decisions needed" ("[P0] OmniRoute deploy to Google Cloud VM" - moot), "Wiring work", "Deferred to post-grill" (Novus-Agenti nested checkout; "Any repo-shape decisions"), "Other" (ECC plugin never installed; "novus-aeyre PR 6 ... verify it landed"; "mem0 CLI plugin API key"), "2026-10-23" (hook 3; checks from obs 0038-0041; "`run-hook.sh` cloud allowlist does not include the #76/#77 hooks").
- aesop-xi `RESUME.md` NEXT: "1. Checks proposed by vault observations 0038-0041"; "2. Decide whether cloud sessions need the #76/#77 hooks"; "3. npu-serve: tool calls, multiple images per message, InternVL 2B in models.json".
- vault `RESUME.md` "NEXT SESSION - START HERE": 1 read AGENTS/PENDING; 2 "NPU proof result"; 3 "Operator items"; 4 "Agent items: Jev skills fork review ... observations 0038-0041".
- `skill-updates/PENDING.md` open: hook specs (operator decides), task-observer upstream draft (send/drop).
- Long-term vs old locked decisions (2026-09-05, vault `LOCKED-DECISIONS-2026-09-05.md`, verified-on-disk; the file title inside is "NovÆxorpus - Session Resume / Handoff"): 11 operator decisions; "Immediate next targets": DroidDesk install, Æsc terminal daemon setup, fold Termux-era work into Æsc; "Post-tonight targets (deferred)": grill session with docs, new repo build-out (Hybrid 12 top-level), Œræcle on-device oracle, model weights into NovAExopia, DeepSeek harness spec, vendor-workspace skill implementation; "Unresolved items" list (Tailscale install status, T3 infra on hold, obsidian-skills clone, ...). Many are superseded by 2026-10-23 decisions (e.g. OmniRoute "memory extraction layer" decision 1 is overridden by the drop).
- Branch-review recommendations awaiting the operator (report, 2026-10-23): MERGE NovAExorpus `docs/delete-branch-after-merge`; close OB1 PR #2; SALVAGE-then-tag two branches (done: `recovered/2026-10-23/`); KEEP claude-code-android architecture-review branch and Horizon-s-home-grid PR #1; adk-docs `gh repo sync` + delete 177 branches; NvAEx-code-review-graph Actions decision. PENDING says 23 bot branches archived as `archive/*` tags and deleted.
- Voice APK brief open questions: "1. Media APK as its own app now (this brief), or voice-core inside the Terminal APK first? ... 2. Material 3 Expressive beta now, or stable 1.4.0 and upgrade later? 3. API reachable only on the phone (127.0.0.1), or also from the tablet over Tailscale with the token?"
- Governance conflicts to flag for the caller: (a) vault AGENTS.md rule 5 says "Leave the branch in place after merge"; aesop-xi AGENTS and the global rules say delete after merge; branch `docs/delete-branch-after-merge` (MERGE recommended) is unmerged; newest-wins rule per aesop-xi MEMORY. (b) Vault `builder.md`/`corpus-architect.md` agents still reference mem0/OmniRoute/TB (dropped). (c) Deploy/profile files in aesop-xi still describe dropped components. (d) vault AGENTS says no CLAUDE.md in repos but `.claude/` dir and `CLAUDE.md.original.md` exist at vault root. (e) RESUME vs disk observation counts (gap 5).

---

*End of ledger.*
