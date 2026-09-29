Session files: [[AGENTS]] · [[PENDING]] · [[MAP]] · [[GRILL-MANIFEST]] · [[NAMING-CANON]]

# RESUME.md — Session Ledger

Repository: NovÆxorpus (`c10vis-poem/NovAExorpus`), the master wiki and vault.
Last session: 2026-09-28 → 2026-09-29 (phone, Claude Code, Opus 5.5). It ended mid-grill, at the operator's call, to start fresh.
This file is rewritten top to bottom at the end of every session. Anything unresolved also goes to `PENDING.md`.

## NEXT SESSION — START HERE

1. Open Claude Code in the vault: `cd ~/storage/shared/Documents/NovAExorpus && claude`. It loads `AGENTS.md` by itself.
2. Read this file, `grill/DECISIONS.md` (today's decisions), `grill/research-notes-2026-09-29.md` (sourced facts on OmniRoute, ReasoningBank, the Continual Harness paper and the Æsop-Xi doc conflicts) and `CONTEXT.md` (the glossary). The OB1 and Continual Harness code facts are in `grill/ob1-read-ledger.md` and `grill/continual-harness-read-ledger.md`. Don't re-read sources those files already cover; read only what they list as unread.
3. Work the open items below in order, then resume `/grill-with-docs`. The agenda is `GRILL-MANIFEST.md`; the grill was on the Continual Harness definition.

## OPEN ITEMS, IN ORDER

1. **PR #21 (`vault-sync` → `main`, "vault: first full sync from phone") is blocked by the secret scan.** This is the PR that brings the phone's vault into `main`.
   - gitleaks found 8 things. 7 are false positives:
     - a CSS class name in `__RESUME.md/_inbox/Tickets.mht:9907`;
     - an example `TKN-AESOP-…` id in three copies of `aesop_arbitration_and_governance.md`;
     - public reCAPTCHA site keys in `Drive_sync/__RESUME.md/Housekeeping/llm-wiki/Deception Pass Volunteer Form….mht`.
   - The 8th is a GitHub fine-grained token that sat in an archived Drive filename, listed in `__RESUME.md/_whatisit/files_cleanup/z.st_/index.jsonl:67`. The operator doubts it still exists and does not want to be forced to revoke it.
   - Done: `__RESUME.md/_whatisit/files_cleanup/` is untracked and gitignored on `vault-sync` (commit `c915243`). The files stay on the phone.
   - Not done: a `.gitleaksignore` listing the 8 reviewed findings. Claude Code's automatic safety check refused it as a CI bypass because of the token. The finding list (commit/file/rule/line, no secret values) is saved at `~/NovAExorpus-PR21-gitleaks-fingerprints.txt` on the phone.
   - To clear it, pick one:
     - the operator checks github.com/settings/personal-access-tokens and confirms the token is gone, then an agent retries;
     - or the operator commits the `.gitleaksignore` themselves.
   - #21 then re-runs its checks and auto-merges. Its merge conflict (AGENTS.md) is already resolved (`vault-sync` commit `56eb9b9`, keeping the phone's newer AGENTS.md), so the secret scan is the only blocker.
2. **`master` → `main`.** The operator wants `main` only. GitHub has a stale `master` branch: last commit 2026-09-06, 41 behind `main`, and 6 commits that never reached `main` (newest `d6510a1` "Retire hard rule 2 …"). Review those 6, carry anything worth keeping into `main` by PR, then delete `master`. The phone's local `.git` is an unrelated leftover (GitSync works through the GitHub API), so its `master` branch doesn't matter.
3. **Finish reading the Continual Harness code.**
   - Fork: `c10vis-poem/AEsops-continual-harness` @ `bbab97a`, clone at `~/repos/AEsops-continual-harness`. Paper: arXiv 2605.09998.
   - Ledger: `grill/continual-harness-read-ledger.md`. It lists what is read (core harness, `agents/`, `utils/stores/`, docs, run scripts, containers) and what isn't: the rest of `utils/`, `server/`, `tests/`, and the game environment code.
   - Findings so far, all verified in source:
     - The code "sandbox" hands model-written code `__import__`, so any skill can take over the host, and there's no timeout (`agents/PokeAgent.py:491, 586`).
     - Trajectory logs drop tool results and mark every step a success (`agents/PokeAgent.py:2924-2937`), so the Refiner never sees tool failures.
     - Every self-evolved "create" is reported as failed; self-evolved new skills get no code.
     - There is no rollback feature, but the pieces exist (per-field change history, a file for every prompt version, backups).
     - A fixed system prompt versus rewritable strategy is a real guardrail.
     - Objective completion is self-declared; emulator milestones are the only ground truth.
4. **Æsop-Xi CLAUDE.md** (`~/repos/aesop-xi`, §Runtime memory stack) says ReasoningBank does "crash recovery (resume from step N+1)". The ReasoningBank repo never claims that, so it was invented. Put its removal to the operator, along with the other agent-written "never/must" rules there.
5. **Resume the grill:** what the Continual Harness is for us, then the rest of `GRILL-MANIFEST.md`.

## WHAT HAPPENED THIS SESSION

- **OB1 fork read in full.** Every file in `c10vis-poem/OB1` @ `238df6c` has a row in `grill/ob1-read-ledger.md`, with a summary at the end. Merged to `main` (#22, #25).
- **Grill decisions** (`grill/DECISIONS.md`):
  - OmniRoute keeps its own SQLite and memory tables.
  - The four memory layers (mem0, OB1, Graphify, code-review-graph) are separate MCP servers.
  - ReasoningBank is an OmniRoute plugin with its own judge and store.
    - It judges against ground truth, never the agent's word. That covers the task outcome and whether the pipeline ran properly: routing, ignored tools, unused skills, the mem0 write, the OB1/Supabase row, and whether the expected path was followed.
    - It keeps ReasoningBank's own lesson-writing rules and its own model settings.
    - It has no crash recovery.
  - Æsop-Xi (Agentic Executions Split Operation Protocol) is the home of the whole runtime system.
  - The on-device Auditor only flags prompts that weren't done as told; it stores nothing.
  - ECC is parked.
- **CONTEXT.md** now defines Æsop-Xi, ReasoningBank and Auditor.
- **33 vendor files restored** to `02_wiki_md/vendors/github/`. They had been moved into the gitignored nested `NovAExorpus/` folder.
- **ECC parked** at `~/.claude/ecc-parked/` (its README explains how to bring it back). It no longer loads from `~/.claude/rules/`, and its "mandatory agents" block is out of `~/.claude/CLAUDE.md`.
- **Claude memory notes added:**
  - push, PR and merge once, at session end;
  - no invented hard rules and no "canonical" in docs;
  - ECC parked;
  - the Auditor.
- **PRs:** #22, #25, #24, #26 and #28 merged. #24 was empty, because #23 had merged `main` *into* `happy-ending-unresolved-updates`. #26 and #28 carry this session's docs. #27 was closed as a duplicate of #28. Open: #21 (secret scan) and #7 (operator review).

## OPERATOR TO-DO

1. PR #21: confirm the token is gone, or commit `.gitleaksignore` yourself (item 1 above).
2. Register the session hooks (makes `sync-forks` / `ship-session` automatic). Paste in Claude Code:
   `! f=~/.claude/settings.json; jq '.hooks.SessionStart=[{"hooks":[{"type":"command","command":"jq -r .session_id | { read -r s; nohup ~/bin/sync-forks \"$s\" >/dev/null 2>&1 & }","timeout":10}]}] | .hooks.SessionEnd[0].hooks+=[{"type":"command","command":"jq -r .session_id | { read -r s; nohup ~/bin/ship-session \"$s\" >/dev/null 2>&1 & }","timeout":10}]' $f > $f.tmp && mv $f.tmp $f && jq '.hooks|keys' $f`
3. PR #7 (`restructure/drive-file-tree`, open since 2026-09-06, deletes about 37,000 lines across 334 files, no checks): review, then merge or close.

## VM REFERENCE

- Instance `omniroute-brain`, zone `us-central1-a`, project `project-alchemist-490416`. From the phone: `~/bin/vm on|off|status|ssh`.
- The external IP is ephemeral and changes on every start (`vm on` prints it). `34.31.112.77` in `tools/launch.sh` and `router-guard.sh` is stale.
- Idle auto-off after 30 minutes; 4 AM backstop.

## ENVIRONMENT NOTES

- `!` works only inside the Claude Code chat box. In a plain Termux shell, paste the command without it.
- zsh: never name a loop variable `path`, because it overwrites `PATH`.
- GitSync Portal syncs through the GitHub API to `vault-sync`, on startup only. The vault's local `.git` is a leftover.
- Claude Code MCP connections that failed this session: `omniroute` (invalid URL in its config) and `terrestrial-brain` (timeout).

## HANDOFF SOURCES

Read this session:
- **Vault:** AGENTS.md, CONTEXT.md, RESUME.md, PENDING.md, `recovered/2026-09-26-ob1/` (README, the continual-harness plugin draft, the orchestration contract via grep), `_dumbass_unified-config/continual_harness/POINTER.md`, `02_wiki_md/vendors/POINTER.md`.
- **OB1:** the whole fork.
- **Continual Harness:** as listed in its ledger.
- **aesop-xi:** AGENTS.md, CLAUDE.md, RESUME.md.
- **OmniRoute:** AGENTS.md, `docs/routing/AUTO-COMBO.md` (partly), and a search of the source for "Continual Harness" and "Reasoning Bank" (0 hits).
- **reasoning-bank:** README, the judge prompts, the lesson-writing prompts, and the SWE-Bench outcome code.
- **GitHub:** state of PRs #7, #21, #23 and #24, and the gitleaks logs.

Not read:
- documents 00–05;
- `_dumbass_unified-config/` (beyond one pointer file);
- MAP.md, MASTER-CLAUDE.md, MASTER-RESUME.md, SOURCE-RETRIEVAL-MAP.md;
- most of the vault (AGENTS.md Rule 4).
