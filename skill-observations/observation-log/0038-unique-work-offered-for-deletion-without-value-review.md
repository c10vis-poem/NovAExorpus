---
id: 38
title: "Cleanup lists offered unique branches for deletion without saying what they provide; later questions churned and lost detail"
status: open
type: open-source
skill: []
proposes_skill: []
target_file: ["~/.claude/CLAUDE.md"]
siblings_checked: "none: target is an instructions file; related 0019-0021 keep-newest rules and feedback_keep_newest_version memory"
area: "housekeeping deletes; operator decision lists"
date: 2026-10-23
session_context: "Pre-grill housekeeping. Branch audit put 28 'unique' branches and 177 adk-docs branches up for deletion; operator: 'Why would we delete it if they're unique and what do they provide that is helpful', 'instead of deleting them why don't you just merge it or sync it', 'anything after 45 you're going to have to reconfigure with more detailed questions and options'. Friction event e23791."
parked_until:
resolved:
resolution:
reference: "~/.claude/session-work/2026-10-23/branches-report.md, delete-branches.sh"
commands_verified: none
---

**Issue:** "Clean everything up" was read as "delete everything not in main". The agent sorted branches by git ancestry only (in main / has a purpose / unique) and offered the unique ones for deletion with an archive tag, without first saying what each one contains, whether it's worth merging, or whether upstream already has it. For a fork's copied upstream branches, it proposed deletion instead of a sync. Separately, decision items 46+ went back and forth until the operator couldn't follow them.

**Suggested improvement:** A rule (later a check in the delete-script generator): a branch or file with unique content is never offered for deletion until a review states what it provides, whether something uses it, and whether it is merged or superseded elsewhere (by which commit). The default verdicts are MERGE / KEEP / SUPERSEDED-then-archive, and deletion is only the last of these. For upstream copies in a fork, offer a sync first. Each operator decision is written as one question with 2-4 options and their consequences, never a follow-up that changes an earlier question.

**Principle:** Cleanup means making each item's value explicit, not removing everything that lacks an obvious purpose. Unique content needs a stated value judgement before any delete is offered, and a decision request needs fixed options the reader can answer once.
