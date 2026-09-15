# AGENTS.md

Repository: `novae-xorpus`

Authority: NovÆxorpus Master Canon Specifications

## RULE 1 — NO ACTION WITHOUT AN EXPLICIT PROMPT

A skipped or unanswered question is NOT consent. No action — reading,
searching, or anything else — without an explicit prompt or permitted
request. State-changing or not, it doesn't matter.

## RULE 2 — READ THE REPO'S OWN CLAUDE.MD AND RESUME.MD FIRST

Before doing anything else in any of the operator's repos — before
investigating, before answering a question about that project's state —
check for and read that repo's own CLAUDE.md and RESUME.md. This has been
the operator's standing convention for session handoff and current state
across their repos for months. It is not optional background reading; it is
step one, every session, every repo, no exceptions.

## GH workflow (every repo)

1. Feature branch (never commit to `main`/`master` directly).
2. Before every push, scan the diff for secrets/API keys; refuse to push if found.
3. Push, open a PR, track CI.
4. On green CI, auto-merge into `main` immediately.
5. Leave the branch in place after merge — do not delete it.
6. Forked repos: at the start of every session, sync the fork's default
   branch from `upstream` before any other work.

The point of this workflow is that everything reaches `main` — a branch
that never gets a PR opened, or a PR that never gets merged, is a failure
of this rule, not a valid alternative to it. Don't let work sit stranded.

Source: operator-confirmed 2026-09-13, cross-linked in `~/.claude/CLAUDE.md`
on the operator's device and in the `gh-workflow-convention` memory entry.

## Cross-engine compatibility (this file only — tool-agnostic)

This file is read by any agent, not just Claude Code. Two rules that follow
directly from testing across engines:

- **Honey for Devs applies universally** — natively in Claude Code, as a
  text-strip layer in Codex, as a Cordis plugin in DeepSeek Harness (dsh).
  Apply its rules regardless of which engine is running.
- **task-observer / GSD-style skill scaffolding is Claude-Code-only.** Codex
  cannot parse markdown skill wrappers or the dual-layer activation protocol;
  dsh's sandboxed plugin layer blocks task-observer's observation-log writes
  entirely. Do not expect either to work, or try to force them, under Codex
  or dsh — that's the `.claude/` directory's job, not this file's.
- Claude Code and any local engine (Prime Agent, Codex, dsh) are never active
  in the same repo directory at the same time — running two simultaneously
  causes git-lock and file-write races.
