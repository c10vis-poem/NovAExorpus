# P3 Agent fan-out

Pass 1: 2026-10-30, Sonnet-class worker on the phone. Pass 2: 2026-10-30/31, coordinator full read of harness, CrewMarshal and most of backlog; the findings were in `progress-P3.md`, not here. Pass 3 (this rewrite): 2026-11-03, cloud session `018DCykKdJ2PjJ15fAPaqeME`. Pass 3 folded in the pass-2 findings, finished backlog's engine, and re-ran every file:line citation.

**Sources.**
- Phone root `$S` = `/data/data/com.termux/files/home/.claude/plugins/synced/a5d13a90-190b-42eb-ad1b-69c924919b1b_b410cc73-6e72-411c-a9de-4edf62ec27d7/`.
- In pass 3, agent-army, agent-discussion and cc were read from the cloud synced copies (same versions).
- The rest came from upstream, pinned to the version read:

| Plugin | Version | Pass 3 source |
|---|---|---|
| agent-army | 1.0.0 | cloud synced copy |
| harness | 2.1.0 | github.com/revfactory/harness `92d9f1b` (HEAD = 2.1.0) |
| agent-discussion | 0.1.0 | cloud synced copy |
| CrewMarshal | 0.24.0 | github.com/nguyengiatam/CrewMarshal `37b6080` (the only 0.24.0 commit; 0.25.0 is `3d2fcf2`) |
| cc | 0.6.0 | cloud synced copy |
| noetic-control-room | 0.3.4 | github.com/NoeticEcho/control-room `13cb6d2`, `plugin/` |
| backlog | 2.4.3 | github.com/backloghq/backlog `b449d9f` (HEAD = 2.4.3) |

- The first-build scripts were read from their vault copies in `plugins/greedy-crane/scripts/`. These are the same files as `~/repos/.wt/novaexopia-wiki/tools/wiki-admin/` (pass-2 note).

## 0. Read status and gaps

| Plugin | Read depth |
|---|---|
| agent-army | FULL (`SKILL.md`, 271 lines) |
| harness | FULL text: `SKILL.md` (405), `evolve` (89), all 9 references, README, CHANGELOG, CONTRIBUTING, docs text, manifests. GIFs/images not opened |
| agent-discussion | `SKILL.md` all but 120-156; `watch_turn.sh` to line 50 |
| CrewMarshal | FULL: 12 skills with references, 4 hook scripts, hooks tests, README, docs, manifests, `watch_lane_run.py`. The design history specs (`docs/superpowers/specs`, plan) are partial |
| cc | `commands/batch.md` (77); `scripts/batch.py` 1-40, 124-175, 278-320; `hooks/hooks.json` (52); `hooks/cc.py` exit paths (453-481) |
| noetic-control-room | `brief-worker` (12-104), `land-ready` (5-60), `scripts/ready-check` exit paths. `run-desk`, `start-cloud-worker`, `gh-desk` not read |
| backlog | 7 skills, agent `task-planner`, README, CLAUDE.md (to ~200), `src/index.ts`, helpers, schemas, types, `task-schema.ts`, `engine/index.ts` FULL (704; tail finished in pass 3), 4 hook scripts. `src/tools/*`, tests, CI, CHANGELOG not read |

Notes on the gaps:
- **The worker spec has been found.** `plugins/greedy-crane/docs/corpus-ingest.md` (49 lines) and `docs/TOOLS.md` (18) were read in pass 2 and re-read in pass 3. Pass 1 couldn't find them, because they weren't committed until 2026-10-31. The worker contract in section 2 now cites them.
- **The worker can't spawn sub-agents.** `agents/corpus-ingest.md:13` gives it `Read, Grep, Glob, Bash, Write, Edit, Skill, WebFetch`, and no Agent tool. So one batch is one worker, and no second layer is possible. This confirms the agent-army cut below.
- `NvAEx-harness-skills` is Harness.io CI/CD, not revfactory/harness. Ignore it.
- Gemini CLI was not installed on the phone. The CLI lane in section 4 is a contract, not a tested path.
- Numbers marked (design) are choices, not measurements.

## 1. Per-plugin findings

### agent-army 1.0.0, MIT
- **Parts:** 1 skill (instructions only). 0 hooks, 0 MCP, 0 commands.
- **What it does:**

  | Rule | Line |
  |---|---|
  | Explicit `model:` on every Agent call | `SKILL.md:45` |
  | Deployment gate checklist | `:125-139` |
  | Phantom-completion check: `git diff --stat` against agent reports | `:151` |
  | Max 4 waves | `:163` |
  | `.army-state.md` for resume | `:176` |

- **Keep:**
  - Rules 2, 2b, 4 and 6 (`:44-49`), where 6 is "a green report from an agent is a claim, not proof".
  - The Deployment Gate (`:129-137`) and Verify (`:148-159`).
  - The anti-patterns (`:237-`).
  - The `.army-state.md` idea (`:176`).
- **Cut:**
  - Rule 1, "every L1 MUST spawn 2+ sub-agents" (`:43`). The worker has no Agent tool anyway (section 0).
  - The git checkpoint branch (`:96-100`). The vault is public and synced; use the ledger instead.
  - "Audit waves run on Opus" (`:86`), against work-order rule 6.
  - `.claude-plugin/` (848 KB of icon).
- **Trimmed draft `batch-dispatch`:**
  ```
  Rules: 1 batch = 1 worker, disjoint docs (each doc owned once, no gap). Pass model: on every
  Agent call. Print the gate before deploying: [ ] every doc in exactly one batch  [ ] model set
  [ ] ledger row written  [ ] size-gate applied. After every batch: a worker report is a claim;
  trust files on disk + ledger + verify.py, not the report. Re-dispatch any worker whose report
  says COMPLETE but whose md files are absent/empty. Never shrink the fleet silently.
  Write the ledger (section 3) after every batch.
  ```
- **Conflicts:** overlaps the harness patterns and the built-in Workflow tool. Winner: this trimmed skill for rules, Workflow for execution.

### harness 2.1.0, Apache-2.0
- **Parts:** 2 skills (`harness` 405 lines, `evolve` 89), 9 references (~2,460 lines). 0 hooks, 0 MCP. Text is in Korean. It generates agent teams for a domain. Wiki-admin needs one fixed team, so the generator itself isn't needed.
- **Keep these ideas.** Rewrite them in English in our own words. Apache-2.0 requires keeping the NOTICE if text is copied.
  1. **Model by job, not by importance.** Sources: `references/model-selection-guide.md:117-120`.
     - Rule 1: choose by the work, never "because it's an important agent".
     - Rule 2: never blanket-assign one model.
     - Rule 3: a Fable coordinator doesn't make the workers Fable.
     - Rule 4: per Workflow step, sonnet for repetitive collection and conversion, opus for deep verification and judgement.
     - Rule 4 conflicts with work-order rule 6 only if a "verification" step re-reads documents. Keep verification to reading the worker's output and its cited lines.
  2. **Error policy** (`SKILL.md:258-266`):
     - Retry once, then go on without that result and record the gap.
     - Never retry usage-limit, auth or permission failures; open the partial output to see how far it got.
     - The orchestrator fills gaps only with facts it checked itself, never with an agent's guessed reasoning ("that would forge the audit record").
     - A failed `agent()` returns `null`: `.filter(Boolean)` the results and `log()` the missing count.
     - An unresponsive persistent agent gets a status message first, then a fresh instance with the context passed in.
  3. **Scale table** (`SKILL.md:270-278`): more than 20 tasks means a supervisor plus 3-5 workers. The Workflow total cap is 1,000 agent calls.
  4. **Record cost at completion** (pass 2; `references/skill-testing-guide.md:79`, `skill-writing-guide.md:221`). Save `total_tokens` and `duration_ms` the moment a subagent's completion notice arrives; they can't be recovered later. Add both fields to the ledger (section 3).
- **Cut:** the `harness` and `evolve` skills as shipped, team-examples and team-patterns, the README, GIFs and docs.
- **Bloat:** two GIFs (7.5 MB + 7.2 MB) and `docs/` (6.0 MB); the whole plugin is 21 MB.
- **Conflict:** the built-in `workflow-authoring` covers pipeline, adversarial verify and loop-until-dry. Winner: workflow-authoring; harness contributes only the ideas above.

### agent-discussion 0.1.0, MIT
- **Parts:** 1 skill (156 lines), `scripts/watch_turn.sh` (76), evals. 0 hooks, 0 MCP.
- **What it does:**
  - Two agents alternate turns in one file, using a `[TURN: name]` marker.
  - It ends on `[AGREED:…]` or `[DEADLOCKED]`.
  - Concurrent-write guard: re-read the last 10 lines before appending (`SKILL.md:70`).
- **Verdict:** cut as a skill. Keep only the turn-marker envelope for the Gemini app / Spark handoff (section 4). Don't ship `watch_turn.sh`.

### CrewMarshal 0.24.0, MIT
- **Parts:** 12 skills (3,392 lines with references), 4 hooks, no MCP.
- **Hooks** (`hooks/`; switched off on the phone as `hooks.off-20261028`):

  | Event | Script | Job | Can block |
  |---|---|---|---|
  | SessionStart | `session_context.py` | injects `docs/working-agreement.md` (cut at 10,000 chars) | no |
  | PreToolUse Bash | `dispatch_gate.py` | one reminder if an executor is launched in the foreground; fails open | no |
  | PreToolUse Edit/Write | `lane_commons_gate.py` | reminds a lane not to edit shared docs; fails open | no |
  | Stop | `pointer_gate.py` | `"decision": "block"` once per HEAD when the pointer is behind (`pointer_gate.py:61-63`) | **yes** |

  README says "None refuses anything; all fail open" (`README.md:80`). That's true for three hooks, but `pointer_gate.py` does block Stop. This was a pass-2 finding.
- **Keep:**
  - `checkpoint-verification` (62 lines): "green tests are not acceptance"; inspect the call site and drive the real path. For the wiki: a page isn't staged because the worker said so; open the file and check that the manifest row exists.
  - From `orchestrating-executors/SKILL.md`:

    | Idea | Lines |
    |---|---|
    | Silent quota exhaustion: an executor "exits 0 with near-empty output" | `:134-144` |
    | Re-check quota after a suspiciously fast or empty result | `:143-144` |
    | "A dispatch is complete only with evidence of all three": started, monitor attached, run recorded | `:193-200` |
    | Before relaunching after a monitor failure, confirm the executor isn't already running ("two facts") | `:218-220` |
    | When a notification arrives, match it to the task and run, and drop duplicates and events from an older run | `:233-242` |
    | Named task states | `:246-` |

  - The `references/executor-roster.md` template: "the ONLY machine-specific part" (`:1-5`). Re-fill it with our lanes.
  - From `multi-lane-coordination` (pass 2; `SKILL.md:98-99,124-145,182`):
    - Each lane has a charter, an `inbox.md` (the chief writes) and an `outbox.md` (the lane writes).
    - Every run is a new headless session, never resumed (`:129-131`).
    - A run reads the inbox from the entry after the last one acknowledged (`:142`).
    - Reset a lane at ~300k tokens of context (`:182`; also `pointer-handoff/SKILL.md:113`).
    - This maps directly to the Gemini CLI and Spark lanes in section 4.
  - From `adversarial-review-to-go` (pass 2; `SKILL.md:26-31,74,199-209`):
    - Diffs loop until a round has zero surviving findings.
    - Specs and plans stop at a round with fewer than 5 findings, mostly low severity.
    - Use a fresh reviewer thread each round.
    - Seed mutations to test the reviewer.
    - Use it for the sampled skeptic in section 3.
  - From `project-working-agreement` (pass 2; `SKILL.md:47,61-63`): the cadence (when to stop) and the execution mode (how many executors at once) are always asked of the operator, never assumed. The director must ask both before a run starts.
- **Cut:**
  - The other skills (concept-briefing, planning-for-delegation, lessons-ledger, pointer-handoff, convention-commit-gate): code-delivery workflow.
  - All 4 hooks. `pointer_gate` blocks the end of a turn, which violates work-order rule 8.
- **Bloat:** 517 KB in total, small.

### cc 0.6.0, MIT
- **Parts:** commands `/cc` and `/batch`; MCP `cc` (`server.ts`, 468 lines: `cc_peers`, `cc_roster`, `cc_send`); `scripts/batch.py` (607), `batch_report.py` (194), `roster.sh`; evals.
- **Hooks** (`hooks/hooks.json`, 52 lines):

  | Event | What it runs |
  |---|---|
  | SessionStart | `npm install` (an install; not allowed) |
  | UserPromptSubmit | `cc.py roster`, every prompt |
  | PostToolUse | `cc.py touch` |
  | SessionEnd | `cc.py cleanup` |

  **None of them can block** (pass 3, upgraded from "unconfirmed"). `cc.py` exits only 0 or 1 (`hooks/cc.py:453-481`) and prints no decision JSON; Claude Code blocks only on exit 2 or a block decision.
- **`/batch`:**
  - `batch.py` spawns headless `claude -p` workers with `subprocess.Popen` (`batch.py:167`, inside `run_worker` at `:124-175`).
  - Default 20 workers (`:278`), via a `ProcessPoolExecutor` (`:309`), with a 60 s timeout (`:128`).
  - It's an eval runner for skill triggers (`commands/batch.md:2`).
  - No resume, checkpoint or retry: grep finds 0 matches.
- **Verdict:**
  - Cut the plugin.
  - Keep the idea that headless workers can be OS processes, which is how a Gemini CLI worker would run.
  - Don't self-host the MCP.
- **Bloat:** 229 KB, mostly `package-lock.json`.

### noetic-control-room 0.3.4, Apache-2.0
- **Parts:** 4 skills (`brief-worker`, `land-ready`, `run-desk`, `start-cloud-worker`) and scripts `ready-check` and `gh-desk`. No hooks, no MCP.
- **Ideas to adopt** (the plugin itself is git/PR-specific):
  - **A worker's READY line "is a claim, not a verdict: check it"** (`land-ready/SKILL.md:9`). Use `BATCH <id> READY <n_pages> <n_failed>` or `BLOCKED <reason>`.
  - **Acceptance must be "checks that can fail"; "Tests pass" is not one** (`brief-worker/SKILL.md:28-30`).
  - **A silent worker gets a status question, "never a new brief"** (`brief-worker/SKILL.md:91-98`).
  - **A read-only mechanical checker runs before a human reads** (`scripts/ready-check`). Its exits are 0 ok, 1 fail, 2 usage, 3 already landed (`:33,90-99,161`); pass 1 listed only 0/1/3. Adopt it as `batch_ledger.py reconcile`.
  - **The brief is delivered as a user message, not relayed.** This matters for the Gemini app.
- **Verdict:** cut as a plugin.
- **Bloat:** 138 KB.

### backlog 2.4.3, MIT
- **Parts:**
  - 7 skills and agent `task-planner`.
  - MCP server `tasks`, 24 tools.
  - 4 hooks.
- **Hooks** (`hooks/hooks.json`):

  | Event | Script |
  |---|---|
  | SessionStart | `session-start.sh` (prints the pending count) |
  | TaskCreated | `sync-task-created.sh` |
  | TaskCompleted | `sync-task-completed.sh` |
  | SubagentStart | `sync-subagent-start.sh` |

  **All four are confirmed non-blocking** (pass 3). Every exit path in the four scripts is `exit 0` or `process.exit(0)`. The three sync hooks only append to `sync-queue.jsonl`.
- **MCP self-host:**
  - `scripts/start-server.sh:9-13` runs `npm ci` on first launch, then `node dist/index.js`.
  - Deps: `@backloghq/agentdb` and `@modelcontextprotocol/server@2.0.0-alpha`, an alpha.
- **Defects** (pass 2 and pass 3, `src/engine/index.ts`):
  1. **A subagent claims every task.** The SubagentStart drain assigns *every* unassigned pending task to whichever subagent started (`:179-186`).
  2. **Completion matching is by description text.** A completion with two matches is skipped (`:171-178`).
  3. **Malformed queue lines are lost.** They are silently dropped (`:187-189`), and the queue file is deleted afterwards (`:191`).
  4. **An empty filter edits everything.** `modifyTask` with an empty filter modifies *all* tasks (`:374-376`).
  5. **Descriptions are capped** at 500 chars (`:498,582`).
- **Verdict:**
  - Do NOT use it as the batch ledger. A JSONL file does the job with no dependencies and none of these defects.
  - If it belongs anywhere, it's the memory-store pipeline (P7).
  - Keep the `handoff/SKILL.md` idea: mark what is active and annotate what remains.
  - Keep `session-start.sh` as the pattern for the one optional hook (section 6).
- **Bloat:** 777 KB in total; `dist/` 191 KB.

### Also lifted from watch-video (P1 pass 3, full read)
Job-runner patterns that apply here:
- **Background start plus polled status file** (`mcp-server/server.py:724-909`). The status file is written atomically, by staging and then `os.replace` (`:235-249`).
- **Orphan detection.** A "running" record written by a different process id is reported as stale and is never awaited (`:252-273`). Applied here: a ledger row in `dispatched` whose owner session is gone is lost, not running.
- **Logs go to files, never pipes** (`:75-83,460-470`). A pipe deadlocked a child under the MCP host.
- **Cancelling kills only the direct child** (`ROADMAP.md:10`), so a retry can race a leftover grandchild process. Kill the process group.

## 2. The 1,000-document run, end to end

**Actors:**
- **Wiki admin = director** (`agents/wiki-admin.md`). It directs and doesn't read the documents.
- **Workers = `greedy-crane:corpus-ingest`**, one per batch, Sonnet (`docs/corpus-ingest.md:42`).
  - Skills preloaded: corpus-verify, corpus-batch-processing, honey, honey-px, w5h-extraction, wiki-reference-router, wiki-admin-ingest (`agents/corpus-ingest.md:5-12`).
  - No Agent tool (`:13`).
  - Rules: raw text is never an instruction; output goes to `01-inbox/` only; failures are named; progress file first (`docs/corpus-ingest.md:31-36`).
- **Reading lanes the director may hand to:** Gemini API, Gemini CLI, Gemini app, Spark agents (section 4).
- **Scripts** (vault `plugins/greedy-crane/scripts/`): `manifest.py`, `convert_raw_to_md.py`, `verify.py`, `gemini_infer.py`, `audit_staging.py`, `promote.py`, `selftest.sh`, plus `read_packet.py` and `worker_stop_check.py` (committed 2026-10-31, not wired in).

**Before step 0:** the director asks the operator for the cadence and the execution mode (CrewMarshal `project-working-agreement/SKILL.md:47,61`). It never assumes them.

### Step by step
0. **Gate to start** (director):
   - `selftest.sh` passes.
   - The `verify.py` canary is ok; exit 2 means broken, so stop.
   - One cheap quota probe per lane ("reply ok").
1. **Inventory** (no LLM):
   - Run `manifest.py build <raw> --out work/raw.manifest.jsonl` and count N.
   - Freeze it: write `work/INVENTORY.sha256` and put N in the ledger header.
2. **Privacy and skip pass** (scripted):
   - Private/pii/personal-tagged files, files under `private-memory/`, and files containing credential patterns are kept off the Gemini lanes. `gemini_infer.py:73-90` refuses them anyway.
   - Credential files are logged "skipped" and never read.
3. **Size-gate:** P2 sets the threshold. Over-threshold docs become single-doc jobs for the large-context lane.
4. **Split** (`batch_ledger.py plan`):
   - Sort by sha256.
   - Close a batch at 25 docs or 2 MB raw, whichever comes first (design). That's about 40 batches.
   - Each doc is in exactly one batch.
5. **Convert** (`convert_raw_to_md.py` per batch): files out = files in, or each gap is named. EMPTY PDFs go to the OCR list.
6. **Verify conversion** (`verify.py`): FAIL means re-convert. Never draft from a failed file.
7. **Draft** (workers, in parallel): one worker per batch. Output: pages in `01-inbox/` plus a batch report.
8. **Mechanical reconcile** (script, section 3). A batch is accepted only if the script passes.
9. **Cross-audit:**
   - `audit_staging.py` every 5 batches.
   - The sampled skeptic follows the adversarial-review rules: a fresh thread each round, and a stop rule.
10. **Show the operator** the staged, failed and quarantined lists by name, then stop. `promote.py` runs only on explicit approval of named files.

### Concurrency
- Start at 4 workers in a rolling window (design). An earlier session saw 2 of 4 dispatches fail together on one shared rate limit.
- Raise to 8 only after 2 clean batches. The Workflow cap is min(16, CPUs-2).
- Use a rolling window, not wave barriers. 40 batches at 4 concurrent is about 10 rounds.

### Model per role
| Role | Model | Why |
|---|---|---|
| Director | session model | coordinates, never reads docs (harness guide rule 3, `:119`; agent-army `SKILL.md:83`) |
| Worker | Sonnet | `docs/corpus-ingest.md:42`; work-order rule 6 |
| Inventory, ledger, reconcile, convert, verify | no LLM; Haiku only to summarise a failure list | deterministic work stays in code |
| Sampled skeptic | Sonnet, on a different lane than the worker when possible | "refute; default refuted if unsure"; never Opus for reading |
| Bulk draft on API | `gemini-3.8-flash` | `gemini_infer.py:35` |
| Big single docs | `gemini-4-argon` (1M context) | `gemini_infer.py:35` |
| Disputes | the operator | no agent message counts as approval |

## 3. Checkpoints, fake completion, crash resume

### Ledger
- **Files:**
  - `work/ledger/header.json`: N, inventory hash, plan version.
  - `work/ledger/B###.json`, one per batch, written only by `batch_ledger.py` (atomic: temp file, then rename).
- **Fields:**
  - `batch`, `docs[sha256]`, `state`, `lane`, `model`, `attempt`
  - `owner_session` (new; used for orphan detection)
  - `dispatched_at`, `returned_at`
  - `total_tokens`, `duration_ms` (new; harness "record at completion")
  - `md_ok`, `md_empty`, `verify_pass`, `verify_fail`
  - `staged[]`, `failed[{sha256,reason}]`, `reconcile{pass,notes}`
- **State machine** (forward only, plus `retry`): `planned`, then `converted`, `verified`, `dispatched`, `returned`, `reconciled`, `audited`, `staged`. `failed` and `quarantined` are terminal per doc and carry a reason.
- **Gap in `manifest.py`:** it writes `id, file, path, tier, category, sha256, size, tokens, title` (`manifest.py:15,99-103`). It has no `status`, `converted_by`, `source`, `md_path` or `extracted`. The ledger step, or a post-step, must add them.
- `audit_staging.py:116` already blocks `dry_run: true` drafts.

### Checkpoints
| # | When | Evidence required |
|---|---|---|
| C0 | after inventory | N and the inventory hash recorded; cadence and execution mode answered by the operator |
| C1 | per batch after convert | files out = files in, or each gap named |
| C2 | per batch after verify | `verify.py` exit 0 for every non-failed doc |
| C3 | per batch on return | reconcile passes |
| C4 | every 5 batches | `audit_staging.py` clean; director reads 3 random pages against their raw source |
| C5 | end | ok + failed + quarantined = N; a manifest row for every sha; failed list to the operator |

### Catching fake completion (cheapest check first)
1. **File on disk, not the report.** Every md file must exist and be over 200 bytes after frontmatter (design). Source: agent-army `SKILL.md:151`.
2. **Count.** Pages staged plus failed-with-reason must equal the batch size; otherwise the batch is PARTIAL.
3. **Raw hash.** The page's `sources:` sha256 must match the frozen inventory.
4. **Independent extractor.** `verify.py` runs `check.py`, which uses different libraries.
5. **Dry-run and stub drafts.** Blocked by `audit_staging.py`. Also flag a page under 5% of its source length for a doc over 2 KB (design).
6. **Silent quota exhaustion.** CrewMarshal `orchestrating-executors:134-144`. Re-probe after a suspiciously fast batch.
7. **Citation spot check.** The skeptic samples 1 page per batch, plus every page from the Gemini-app and Spark lanes, and quotes 3 facts verbatim from the source. The idea comes from watch-video `highlights.py:160-181`: drop any model-returned anchor that isn't in the source.
8. **READY is a claim.** Source: noetic `land-ready:9`. Compare the worker's last line with the ledger.
9. **Silent worker.** After 20 minutes with no ledger change (design):
   - Send a status question, never a second brief (noetic `brief-worker:91-98`; harness `SKILL.md:266`).
   - After another 10 minutes, mark the attempt failed, check quota, and redispatch.
10. **Duplicate or stale notifications.** Drop events from an older run of the same batch (CrewMarshal `orchestrating-executors:233-242`).

### Retry policy
Source: harness `SKILL.md:260-264`; work-order rule 10.
- Retry a failed batch once. On a second failure, split it into single-doc jobs.
- A doc that fails twice becomes `failed`, with a reason, and goes to the operator by name.
- Quota, auth and permission errors are never retried. Stop the lane, record the lost range and report the reset time.
- Never fill a gap with a guess.

### Crash resume
- Everything lives on disk: the frozen inventory, the ledger and the md files. The director's context is disposable.
- `batch_ledger.py resume`:
  1. Verify the inventory hash.
  2. A batch that is `dispatched` with no `returned_at` and an `owner_session` that is gone is lost (watch-video orphan rule, `server.py:252-273`): redispatch it.
  3. A batch that is `returned` but not `reconciled`: reconcile it first.
  4. Never redo a doc whose manifest row is `ok` and whose md hash is unchanged.
- Before relaunching, confirm the old worker isn't still running (CrewMarshal `:218-220`) and kill leftover child processes by process group (watch-video `ROADMAP.md:10`).
- A Workflow run can use `resumeFromRunId`; the ledger stays the source of truth for files written. Pass the time in `args`, because `Date.now()` throws.

## 4. Reading lanes

**Common contract for every lane:**
- Input: a batch folder of verified md plus a brief.
- Output: pages in a returned folder.
- The return is a claim, and section 3 applies to it.

**Roster:** `roster.md`, using the CrewMarshal `executor-roster.md` template. For each lane it lists how to invoke it, how to check quota, how to observe completion, and gotchas. Probed at C0.

| Lane | Run by | Good for | Limits |
|---|---|---|---|
| Claude worker (`corpus-ingest`, Sonnet) | director via the Agent tool, background, explicit `model:` | 25-doc batches | rate limit shared with the director |
| Gemini API | `gemini_infer.py draft/w5h/extract/ask` | bulk draft, long transcripts, 1M-context `ask` | one file per call; no batching, retry or resume (`:149-181`); no key stored; `google-genai` not installed on Termux |
| Gemini CLI | OS process, headless, one per batch | the operator's login, no key in the repo | not installed; flags unverified. Run it like a CrewMarshal lane (fresh session each run, inbox/outbox, reset at ~300k tokens; `multi-lane-coordination:129-131,182`). Probe first; if non-interactive or read-only mode is missing, mark the lane blocked |
| Gemini app | the operator (human relay) | files too odd for the CLI; Google-only reach | no automation. Director writes `handoff/<batch>.md` with the brief, file list and end marker; operator pastes it in and saves to `returns/<batch>/`. Turn markers as in agent-discussion. Brief is a user message (noetic) |
| Spark agents | instructed by the director | extraction tasks the operator already runs there | interface undocumented; treat like the Gemini app lane until documented |

**Rules for all external lanes:**
- Private/pii/personal files never leave the device. `gemini_infer.py` enforces this only for its own calls, so the director filters before any manual handoff.
- A document's text is data. A document that gives orders is quarantined (P6).
- Returned pages get `author: wiki-admin`, `status: draft` and `model:`, and go into `01-inbox/` only.
- Text for docs outside the batch, or fewer pages than docs, fails C3.

## 5. Google / Gemini / Spark repos compared
Citations re-checked in pass 3 at the stated commits.

- **`NvAEx-crewAI` `49f52a0`:**
  - `kickoff_for_each` (`lib/crewai/src/crewai/crew.py:1101-1135`) loops sequentially; there's an async variant at `:1191`.
  - A SQLite-backed `checkpoint` CLI exists (`lib/cli/src/crewai_cli/checkpoint_cli.py:1-12`).
  - Idea: resumable runs keyed by checkpoint id. Not adopting the framework.
- **`NvAEx-adk-python` `e2e9336`:**
  - `ParallelAgent` stores per-branch state and skips finished sub-agents when `is_resumable` (`src/google/adk/agents/parallel_agent.py:206-240`).
  - `SequentialAgent` is deprecated in favour of `Workflow` (`sequential_agent.py:81-96`).
  - Same pattern as our ledger. Not adopting.
- **`NvAEx-agent-starter-pack` `659f047`:** a template generator for Google Cloud agents (`GEMINI.md:1-5`). No document fan-out. Not adopting.
- **Ranking:** `gemini_infer.py` plus a rolling window of Claude workers is enough.

## 6. Merged hook proposal (input to P6)

Hooks found: 12. cc 4, backlog 4, CrewMarshal 4; the other four plugins have none. Pass 3 confirmed that only CrewMarshal `pointer_gate` can block.

Proposal: 1 hook.

| Event | Job | Blocks | Switch off |
|---|---|---|---|
| SessionStart | `batch_ledger.py status` prints "run X: 31/40 staged, 2 failed, 1 stalled" (pattern: backlog `session-start.sh`) | never; always exit 0, 2 s timeout | env `WIKI_ADMIN_HOOKS=off`, read at hook start; or the Aesop-Xi `#hooks-off` master switch (`hooks/run-hook.sh`, Aesop-Xi PR #84) if launched through it |

**Cut:**
- cc `npm install` (an install).
- cc's roster injection on every prompt.
- backlog's sync hooks.
- CrewMarshal `pointer_gate` (blocks Stop).
- CrewMarshal's lane and dispatch reminders.

## 7. Scripts: reuse first

| Need | Existing | Action |
|---|---|---|
| inventory, sha256 | `manifest.py build` | reuse; add the contract fields |
| convert | `convert_raw_to_md.py` | reuse (P1 section 4 adds rows) |
| independent check | `verify.py` | reuse |
| Gemini calls | `gemini_infer.py` | reuse; wrap with a batch loop, retry-once and a per-call timeout |
| audit, promote | `audit_staging.py`, `promote.py` | reuse |
| worker stop check | `worker_stop_check.py`, `read_packet.py` (2026-10-31, not wired) | fold into `batch_ledger.py` (vault RESUME item 5) |
| split, ledger, reconcile, resume, status | none in `extraction-index.txt` | new `batch_ledger.py` with `plan`, `status`, `reconcile` and `resume`, stdlib only (~150 lines) |
| headless parallel runner | cc `batch.py` (cut) | not needed |

**Director launch sketch** (design; not run; Workflow needs the operator's opt-in):
```javascript
export const meta = { name: 'ingest-1000', description: 'Fan out verified batches to corpus-ingest workers',
  phases: [{ title: 'Draft', detail: 'one worker per batch' }, { title: 'Reconcile', detail: 'script check per batch' }] }
// args.batches = [{id, files}] from batch_ledger.py plan; args.now passed in
const out = await pipeline(args.batches,
  b => agent(`Brief for ${b.id}: ... files: ${b.files.join(',')}`,
             { label: b.id, phase: 'Draft', model: 'sonnet', agentType: 'greedy-crane:corpus-ingest',
               schema: { type: 'object', properties: { batch: {type:'string'}, pages: {type:'number'}, failed: {type:'number'} }, required: ['batch','pages','failed'] } }),
  (r, b) => agent(`Run: python3 batch_ledger.py reconcile ${b.id}; return its verdict`, { phase: 'Reconcile', model: 'haiku' }))
log(`returned ${out.filter(Boolean).length}/${args.batches.length}; missing batches go back through the ledger`)
return out
```

## 8. Open items for the operator

1. Gemini CLI: which machine runs the batch, and with which login and flags? Unverified.
2. Spark agents: what is the interface? Undocumented.
3. Is a live Gemini key set? `STATUS.md` says no, and `google-genai` isn't installed on Termux. Every Gemini call is a dry run until then.
4. The vault is a public repo. Is a work directory outside it acceptable for the ledger and returned files?
5. Cadence and execution mode for the first real run (CrewMarshal rule: asked, never assumed).

(Pass 1's open item "where are corpus-ingest.md and TOOLS.md" is closed: they are in `plugins/greedy-crane/docs/`.)

## 9. Claims check

**Re-run in pass 3:**
- agent-army `SKILL.md:43,44-49,83,86,96-100,125-139,148-159,163,176,237`.
- harness `SKILL.md:258-266,270-278`; `model-selection-guide.md:117-120`.
- CrewMarshal `orchestrating-executors:134-144,193-200,218-220`; `executor-roster.md:1-5`; `pointer_gate.py:61-63`; `checkpoint-verification` 62 lines.
- cc `batch.py:124-175,167,278,309`; `hooks.json`; `cc.py:453-481`; `batch.md:2`.
- agent-discussion `SKILL.md:70`.
- noetic `land-ready:9`; `brief-worker:28-30,91-98`; `ready-check` exits.
- backlog `start-server.sh:9-13`, all 4 hook scripts, `engine/index.ts:146-191,374-376,498,582`.
- `gemini_infer.py:35,73-90`; `manifest.py:15,99-103`; `audit_staging.py:116`.
- crewAI, ADK and starter-pack lines at their commits.

**Corrections from pass 1:**
- noetic `ready-check` also exits 2.
- `gemini_infer.py` privacy check runs to line 90, not 76.
- The "cc hooks cannot block" and "backlog hooks non-blocking" claims are now confirmed; they were weak in pass 1.

**Not re-checkable from the cloud:**
- `STATUS.md` (phone workspace).
- `parallel-session-orchestration` and `workflow-authoring` skill text (built-in, phone session).
- The old `~/repos/NvAEx-harness-skills/README.md:1-3`.

Design numbers (25 docs, 4 workers, 200 bytes, 5%, 20 minutes) are not measured.
