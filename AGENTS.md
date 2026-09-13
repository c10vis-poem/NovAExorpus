# AGENTS.md

Repository: `novae-xorpus`

Authority: NovÆxorpus Master Canon Specifications

## RULE 0 — TAKE NO ACTION WITHOUT AN EXPLICIT ORDER

A skipped or unanswered question is NOT consent. Before any state-changing
action — writing or editing a file, `git clone`, `chmod`, creating config,
committing, pushing, anything beyond read-only investigation (reading files,
`gh`/API GETs, searches) — state the concrete plan and get an explicit go-ahead.

This holds even when the action is local and easily reversible. "It's just a
local file, I can undo it" is not a license to skip asking — do the
investigation, lay out exactly what you're about to do, then wait.

## RULE 1 — READ THE REPO'S OWN CLAUDE.MD AND RESUME.MD FIRST

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
4. On green CI, auto-merge into the default branch immediately.
5. Leave the branch in place after merge — do not delete it.
6. Forked repos: at the start of every session, sync the fork's default
   branch from `upstream` before any other work.

Source: operator-confirmed 2026-09-13, cross-linked in `~/.claude/CLAUDE.md`
on the operator's device and in the `gh-workflow-convention` memory entry.
