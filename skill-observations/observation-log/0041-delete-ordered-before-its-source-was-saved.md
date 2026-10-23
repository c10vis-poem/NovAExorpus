---
id: 41
title: "A delete that depended on an earlier step was listed where it could run first, and a key was lost"
status: open
type: open-source
skill: []
proposes_skill: []
target_file: ["~/.agents/AGENTS.md"]
siblings_checked: "none: target is the shared instructions file (operator command lists)"
area: "operator command lists; destructive step ordering"
date: 2026-10-23
session_context: "Pre-grill housekeeping. A command list put `rm -rf ~/openwiki ~/.openwiki` in the deletes block with a note 'run after step 4' (secrets import). The operator ran the deletes first; the OpenRouter key in ~/.openwiki was never imported and is gone (new key needed). The agent's own reordering mid-session moved the delete above the import."
parked_until:
resolved:
resolution:
reference: "~/.claude/session-work/2026-10-23/import-secrets.sh"
commands_verified: "run: grep for sk-or-v1- across home (excluding storage, .git, transcripts) → no other copy"
---

**Issue:** A destructive command depended on a non-destructive one (import the key, then delete its source). The dependency lived in a prose note, and the delete appeared in an earlier block than the import, so the operator ran them in the order shown.

**Suggested improvement:** A delete that depends on another step goes inside that step's block, after it, guarded mechanically (e.g. `nvaex-secret list | grep -qx OPENROUTER_API_KEY && rm -rf ~/.openwiki`). Never rely on a "run after X" note. When reordering a list, re-check every dependency.

**Principle:** Encode ordering in the command, not in a note beside it. A human working through a list follows the order on the page.
