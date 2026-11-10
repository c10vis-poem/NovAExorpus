---
id: 54
title: "Ad-hoc subagents built from scratch instead of the existing ingest worker: no preloaded skills, no stop gate, oversized slices, skill files that mixed workflow into knowledge"
status: open
type: open-source
skill: [task-observer, corpus-batch-processing]
proposes_skill: []
target_file: ["plugins/greedy-crane/agents/corpus-ingest.md", "plugins/greedy-crane/docs/TOOLS.md"]
siblings_checked: "no family registry entry; corpus-batch-processing added (it is the orchestration skill the readers should have run under); corpus-verify excluded: unchanged, only unused"
area: "subagent dispatch for bulk reading"
date: 2026-11-03
session_context: "Phone session, Claude Code: bulk read of shared Drive files, then a document search, then a review of what a previous model pushed"
parked_until:
resolved:
resolution:
reference: "~/.claude/session-work/2026-11-03/FAILURE-2026-11-03-drive-read.md"
commands_verified: "run: worker-stop-gate.sh fed 5 synthetic inputs (open steps + empty Blocked -> block; Blocked filled -> allow; all done -> allow; stop_hook_active -> allow; no progress file -> block)"
---

**Issue:** The agent wrote reader agents by hand (4, then 8, slices up to 1,500 files) with raw tool calls, while the operator's greedy-crane `corpus-ingest` worker already preloads the ingest skills, names a tool per stage, and requires a progress file. None of the operator's ~40 enabled plugins or ingest skills were loaded. A new "drive-find" skill first mixed workflow steps into knowledge. Workers had no task-write requirement enforced and no stop hook, so nothing held them to the plan. A newly written agent file was not launchable until the session restarted.

**Suggested improvement:** Improve the existing worker rather than build a rival: (1) corpus-ingest gains a Stop hook (worker-stop-gate.sh: blocks stopping while plan boxes are open and Blocked is empty, operator override, no loops); (2) its progress file adds `## Skills loaded` and `## Measures`; (3) drive-find joins its preloaded skills as knowledge only; (4) slices capped at ~40 unique documents; (5) new agent definitions are created at session start or followed by a restart before dispatch. Then retire drive-ingest (done).

**Principle:** Before dispatching workers, inventory and use the existing worker definition and its skills; enforce the plan with a gate, not a sentence; keep skills as knowledge and workflows in the agent.

**Second occurrence (2026-11-05):** bulk document reads were again spawned as general-purpose agents instead of the existing corpus-ingest worker, so the worker's Stop gate never fired, and one reader skipped most of its assigned files. Per the second-violation rule this needs a structural barrier: an agent-type check that routes full-read spawns to corpus-ingest, and a read ledger the Stop gate compares (lines read against total lines), because a checkbox alone does not prove a read.
