---
id: 55
title: "Transcript recovery that reads only type=user records misses messages sent while the agent was busy"
status: open
type: open-source
skill: [task-observer]
proposes_skill: []
target_file: []
siblings_checked: "no family registry; checked — applies to session-history recovery generally, no skill sibling"
area: "first-run backfill; recovering a named past session"
date: 2026-11-05
session_context: "Operator asked to recover the directions from a session that vanished from the remote-control list."
parked_until:
resolved:
resolution:
reference:
commands_verified: "run: parsed the session jsonl for attachment type queued_command and queue-operation enqueue; found operator prompts absent from type=user records"
---

**Issue:** The first extraction took only type=user records and reported the operator's messages as complete. The two messages that actually requested the directions were missing, because messages sent during a running turn are stored as queued_command attachments and queue-operation records. An assistant reply answering a message that did not appear exposed the gap.

**Suggested improvement:** In the backfill procedure for a named past session, name the record types to read: type=user, plus attachment queued_command with commandMode=prompt. Enqueue records also hold task notifications and subagent reports, so filter those out. Also note that history.jsonl omits remote-control prompts.

**Principle:** A reply with no visible prompt means the extraction is incomplete. Check that every reply has its prompt before calling a recovered record whole.
