# Global agent instructions (shared)
<!-- Lives at ~/.agents/AGENTS.md. Rules any agent follows (Hermes, DeepSeek harness,
Codex, Gemini, Claude Code). Claude Code reads it only through the `@~/.agents/AGENTS.md`
line in ~/.claude/CLAUDE.md. Claude-Code-only rules stay in ~/.claude/CLAUDE.md. -->

# Instruction files: where rules go (operator, 2026-10-23)
- A Claude-only rule (hooks, skills, subagents/Agent tool, `!` prefix, --add-dir, plugins,
  settings) goes in CLAUDE.md. Anything any agent can follow goes in AGENTS.md, and is
  written there from now on.
- If a repo has no AGENTS.md but one could replace its CLAUDE.md, create the AGENTS.md and
  remove the CLAUDE.md (Claude Code reads a repo AGENTS.md only when no CLAUDE.md exists
  in that directory or above). Upstream forks' own CLAUDE.md are left alone.

# Execution workflow: discuss first (operator, 2026-11-08)
- Discuss first. After the operator approves ("yes"), plan execution, stack tool calls, and ask permission once to cover all actions.

# task-observer workspace (shared by every agent)
The task-observer workspace (ONE log shared by every agent and device: Claude Code,
Hermes, DeepSeek harness; phone, tablet, VM) is the vault, synced by GitSync to
c10vis-poem/NovAExorpus:
  /data/data/com.termux/files/home/storage/shared/Documents/NovAExorpus
Every path derives from that root: skill-observations/observation-log/ (the log),
skill-observations/cross-cutting-principles.md, skill-updates/ (staging),
skill-updates/PENDING.md. Never derive it from cwd or ~/.claude/projects/...; the
old logs there are pointers (MOVED.md). The vault repo is PUBLIC: never write
secrets, keys, or private task content into observation bodies.

# GitHub Fork Workflow (MANDATORY — user has repeated this 12-15 times)
Every tool in the stack comes from the user's own fork under `github.com/c10vis-poem/`.
1. **Sync before install.** Before installing/cloning/building any fork anywhere
   (phone, VM, tablet, home node): `gh repo sync c10vis-poem/<repo>` so the fork matches
   upstream's default branch, then pull and install from the fork — never from upstream,
   npm, or a stale local clone. Report the synced commit.
2. **Every code change ships through this pipeline** — never left local, never pushed
   straight to main:
   branch → commit → secret scan (no exposed keys/tokens) → push → PR →
   CI runs → auto-merge enabled (`gh pr merge --auto --squash`) → merges to main when green.
   If a repo has no CI or no secret scan, say so and set one up rather than skipping the step.
   - Preflight before auto-merge: `gh api repos/O/R/branches/B/protection` shows required
     status checks AND at least one workflow has run on the fork. If not, do not enable
     auto-merge: wait for green, merge by hand, ask the operator to set protection.
     Auto-merge on a branch with no required checks means "merge now". (obs 0026)
   A repo's own CLAUDE.md rules (e.g. commit-attribution bans) override defaults here.
   (A repo's own AGENTS.md rules count the same.)

# Long CI jobs (obs 0027)
- Before dispatching CI expected to run over ~10 minutes, validate every input the job
  resolves (package names, paths, secrets, refs) against the source tree in a cheap
  preflight; add caching so a failure resumes. Never push to a ref with
  cancel-in-progress while a useful run is active on it.

# Behavioral Constraints — Derived from Failure Audit Sessions b/c/d (2026-09-06–07)

## Read Before Claim (CRITICAL)
Any assertion about a count, a state, or file content MUST cite the file
and line it was read from. "From summary," "from memory," or "from prior
context" is not a valid source. If the source file has not been opened
this session, the claim cannot be made.

Canonical example of this rule being violated: "There are 22 hooks" —
stated from memory before settings.json was read. Actual count: 43 logical
hooks (22 settings.json entries + 21 dispatcher sub-hooks). Wrong by
nearly 2×. The correct number was one file-read away the entire time.

## Verification Requires Round-Trip
"Working" means a mechanical test produced expected output.
- A process running ≠ a service responding (curl the port)
- A config file present ≠ the feature active (check state files)
- A banner printing ≠ a REPL completing a prompt/response cycle
Never use process existence or config presence as verification evidence.

## Handoffs Require Source Reads
Before writing any handoff, RESUME.md, or memory doc, explicitly state:
(a) what source files were read this session, and
(b) what was NOT read.
Writing from compaction summary data is prohibited. If nothing has been
read, say so — do not repackage prior session output as new work.

## Session Start — Read RESUME.md
If the active project or any of ~/repos/* contains a RESUME.md,
read it before proceeding to any task. Not ls — Read.

## MCP/Agent Dismissal Requires Attempt
Before dismissing any MCP server or agent as inapplicable:
1. Attempt to connect/invoke it
2. Report the actual error message
"Checked the name, doesn't seem applicable" is not a valid dismissal.

## Behavioral Constraints — from session 2026-10-02 (observations 0019–0021)
- **Keep the newest version.** Never delete the newer of two versions and keep the
  older; "nothing references it" is not a reason — repoint scripts instead.
- **Approval is per item.** A general "yeah" to a message with several numbered
  questions approves nothing specific — ask the questions again before deleting.
- **Duplicates = same model identity**, not same whole-file hash: compare name
  (chip/quant/version), inner weights, and a differing-byte count. Re-downloads of
  the same model often differ by a few KB.
- **Fix it now.** A defect found in code this session owns is fixed this session;
  "later" needs a named blocking reason.

## Behavioral Constraints — from observations (added 2026-10-22)
- **Absence claims name their probes** (obs 0007, 0016, 0024). Before saying X "doesn't
  exist / was never decided / isn't installed", check the record that would hold it:
  decision docs (RESUME, PENDING, memory), `ls`/config for installed tools, and for repos
  the default branch plus other branches plus open PRs. Report "not found by <probes>",
  never "does not exist". Subagent reports say what their batch contained, not what exists.
- **A defect is gone only when checked where it happens** (obs 0035). Before saying a known
  bug is fixed, find where it was reported (open PRs, branches, observations, the
  operator's words) and test in the environment where it occurs. A clean run on another
  path is not evidence.
- **Use the operator's words** (obs 0034). Quote their ask before restating it; define any
  technical term in one plain sentence the first time; confirm ("you asked X; I'll do Y"),
  never re-propose it under a new name. Unknown operator term → search local notes and
  memory before substituting a guess.

# Shared memory (memory as a skill; operator, 2026-10-28)
Cross-project memory for every agent and device lives in the private repo
`c10vis-poem/NvAEx-Recaps`, folder `memory/` (local: ~/repos/NvAEx-Recaps/memory/).
Session start: read `memory/general.md`, then only `memory/active/<project>.md` for the work at
hand (never `archive/`). Respect `<!-- STOP -->` and `<!-- SCOPE -->` markers. Session end:
update that active file (decisions, state, next step). Rules: `memory/README.md`.

# Nothing permanent that can't be deleted (operator, 2026-11-05)
- Never write, install, enable or register anything an agent cannot immediately delete
  again. If removal is impossible or only a "switch" can work around it, do not write it.
- A switch that hides or vetoes a thing is not removal. Anything an agent added that did
  not exist before is deleted outright, not toggled off.
- Never enable or add plugins, skills or marketplaces from the operator's online account
  (no auto-sync from claude.ai). Any install is local, named by the operator, and removable.
- Before adding anything that persists (settings keys, hooks, daemons, sync links), state
  in one line how it is deleted. No answer, no write.

# Interaction & Questions (operator, 2026-11-08)
- Never ask a yes/no question. Always provide explicit multiple-choice options with a write-in / "Other" option.
- Avoid triggering interactive permission popups: do not run ad-hoc unsandboxed shell commands that surface confirmation dialogs in the TUI unless explicitly requested.

# Memory files and session flow (operator, 2026-11-09; there is no NOTES.md)
- **Five session-start files, flat in the launch folder root:** AGENTS.md, MEMORY.md,
  RESUME.md, HANDOFF.md, PENDING.md. Large stores get their own folder, pointed at from the
  file that owns them (MEMORY.md → its memory bank folder; AGENTS.md → settings, rules and
  the rest of its usual items). Any of them may point at session logs.
  - **AGENTS.md:** rules, settings, governance, runtime protocols, output style, and the
    pointers to MAP.md, manifest.jsonl, skills.json and chunk JSONL. Agent directions live
    here, never in CLAUDE.md.
  - **MEMORY.md:** static semantic and structural memory: memory guides, skill pointers,
    lasting facts.
  - **RESUME.md:** project-persistent episodic memory: the project's task list, including
    this session's tasks. Rewritten from scratch at wrap-up.
  - **HANDOFF.md:** session-to-session episodic memory: the specific context and direction
    for the next session.
  - **PENDING.md:** whatever was not done when RESUME.md is rewritten.
- **One purpose per file.** Operator directions go only in AGENTS.md. A user guide is for
  the user, an orchestration file only for orchestration, an output-style file only for
  output style; no second copy of the directions under another name. Similar rules for
  different agents in different places are intentional (this environment serves many
  kinds of agents), not a defect.
- **During a session** the agent keeps its running notes in its own scratchpad, with no
  permission needed. The scratchpad, the task log and the skill log are the session's "notes".
- **Wrap-up routes the notes:** scratchpad, task and skill logs → a session-log folder in
  NvAEx-Recaps `session-logs/<date>-<session>/`. In the repo the work was in: structural
  or semantic changes → MEMORY.md; changes to rules, settings, manifest.jsonl, runtime
  protocols or output style → AGENTS.md; project memory → RESUME.md (rewritten);
  unfinished → PENDING.md. Next-session context → the handoff in NvAEx-Recaps
  `handoff/<date>/`, which the repo's HANDOFF.md points at.
- **What lives where (operator, 2026-11-09 21:32):**
  - **Every repo carries its own:** AGENTS.md, `.agents/` (agent settings and the plugins
    that repo requires), `.claude/settings.json`, `.mcp.json`, its static memory
    (MEMORY.md) and its project-persistent episodic memory (RESUME.md and PENDING.md).
    Each repo has its own RESUME.md; there is no single universal one. HANDOFF.md in the
    repo is a pointer to that repo's handoffs in NvAEx-Recaps.
  - **NvAEx-Recaps only:** handoffs, individual session history, session and episodic logs,
    and personal information. Project episodic memory never goes here.
  - **Context budget:** opening reads and per-prompt loads stay small. The routing and the
    pointers (manifest.jsonl, MAP.md, skills.json) are how agents find the rest without
    ingesting it. Plugins and skills sit at most two folders deep.
  - **Memory as a skill:** one agent skill per repo, loaded in that repo and covering only
    that repo. Separate memory-as-a-skill SKILL.md files go into each agent package, for
    that agent's own harness.
  - **Each agent harness** gets its own SQLite, Postgres, SHA-256 store and Supabase
    database, plus the universal memory bank across split services.
  - **Repo level:** tree-sitter code graphs, ASR graphs and similar graphs attach to the repo.
  - **Vault indexes (operator, 2026-11-10; the vault is public):** `Vendor-Registries/` is the
    vendor directory: a standalone vendor document sits next to its raw files there, with its
    manifest. `Assets-Index/` points at the forked repos not yet reverse-engineered (one folder
    per repo: POINTER.md, manifest.jsonl, and the analyzed doc partitions) and holds the custom
    compiled or from-scratch assets. `Marketplace-Index/` holds the pre-assembled dynamic
    workflows, plugins and agent packages built from all of these.
- **Read the source first (Rule 12):** before an install, a fork's feature or any claim about
  an asset, read its source first, once per session. Deep (breakdown, full install,
  comparison, user guide): every clean MD document in its index folder, or its tree and every
  doc file when none exist yet. Brief (rundown, yes/no, fact check): its chunk.jsonl, or its
  current manifest.jsonl plus a file it points to. The wiki admin's extraction writes
  chunk.jsonl, manifest.jsonl, MAP.md and clean MD (furniture and bloat removed) per asset.
  Training data and another model's word are not sources.
- **Settings go to both places:** `.claude/settings.json` and the root agent settings for
  every other agent (`.mcp.json`, `.agents/plugins.json`, ...).
- Operational layers and the planned router build: NvAEx-Recaps `memory/general.md`.

# When something blocks you (operator, 2026-11-10)
- Stop and read the directions, and follow them; otherwise the hooks keep blocking you. Never try another tool, path
  or phrasing to reach what was blocked.
