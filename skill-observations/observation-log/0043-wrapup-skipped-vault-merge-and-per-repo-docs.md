---
id: 43
title: "Wrap-up left the vault unshipped and skipped per-repo docs; the next agent misread what finishing it meant"
status: open
type: internal
skill: [task-observer]
proposes_skill: []
target_file: ["~/.claude/WRAP-UP.md", "c10vis-poem/Aesop-Xi/hooks/stop-gate.sh"]
siblings_checked: "none: wrap-up protocol and hooks are not a skill family; task-observer listed only for the logging part"
area: "session wrap-up: vault shipping and step 4b per-repo docs"
date: 2026-10-23
session_context: "finishing the /wrapup of session 7cb1c8c0 from session ac090dde"
parked_until:
resolved:
resolution:
reference: "vault _recaps/2026-10-18-7cb1c8c0.md (## Shipped: NOT SHIPPED); ~/.claude/hooks/README.md vault-ship.sh row"
commands_verified: "run: git log origin/main -1 = 2026-10-21; git status = 56 uncommitted vault changes incl. RESUME.md; vault-ship --dry-run = 60 changes to commit"
---

**Issue:** Session 7cb1c8c0 rewrote the vault RESUME.md but never shipped the vault: last commit on GitHub was 2026-10-21, so the operator saw today's RESUME in Obsidian and nowhere on GitHub. It also skipped WRAP-UP step 4b (RESUME/MEMORY/PENDING/AGENTS) in Aesop-Xi and the other repos it touched. The next agent then (1) treated `ship-session.sh --now` as the fix, though that script excludes the vault; (2) planned a vault topic branch instead of the existing `vault-ship` tool listed in the hooks README; (3) planned to rewrite a RESUME the operator had already finalised; (4) planned to put NPU results in the vault RESUME when they belong in the AEthX-AEsc repo; (5) went looking for a NovA-Corpus backup the operator had already handled. Operator words: "What needed to happen was the vault sync needed to get merged with main", "It's supposed to update every repo on wrap up that had anything done to it", "these tests are being run for aesc repo".

**Suggested improvement:** WRAP-UP.md step 6 names `vault-ship` explicitly for the vault (ship-session never ships it) and step 4b says results go to the repo the work is for. stop-gate in wrap-up mode refuses to end while the vault has uncommitted changes or a touched repo lacks a dated RESUME/MEMORY update this session. Agents read the hooks README tool list before choosing a ship path.

**Principle:** A wrap-up is finished when every artefact is where it is read from (the remote, the repo it belongs to), not when the local files are written. Before redoing or rerouting a step, check what the operator already finished and which tool already exists for it.
