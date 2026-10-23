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
