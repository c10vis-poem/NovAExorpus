---
id: 7
title: Absence claims need fork/branch/PR search, not just main
status: open
type: open-source
skill: []
proposes_skill: []
siblings_checked: none
area: repo reading / verification
date: 2026-09-26
session_context: full read-through of OB1 (Open Brain) before install
parked_until:
resolved:
resolution:
reference:
---

**Issue:** While reading a community repo, the agent declared an RPC, a table, and a schema directory "nonexistent" after grepping only the default branch. The operator challenged it. All three existed: on the contributor's fork branches and in closed upstream PRs (files dropped during a merge/consolidation). One claim, a missing API route, did hold up.

**Improvement:** Before asserting anything is absent from a multi-contributor repo, check the default branch, the author's fork (all branches), and upstream PR heads (open and closed). GitHub code search indexes default branches only, so it can't prove absence. Mirror the fork, fetch `refs/pull/*/head`, and `git grep` per ref. Note: `origin` may be the operator's fork rather than upstream.

**Principle:** "Not on main" ≠ "doesn't exist". An absence claim needs the same evidence as a presence claim.

**Further instance (2026-09-27/28):** agent said installed Pocock skills (setup, grill-with-docs, to-spec, implement) were missing because `disable-model-invocation: true` hides them from the agent's skill listing; also said Claude Code can't read AGENTS.md natively when the installed version (2.1.283) does since 2.1.277. Both claims were one `ls`/binary check away. Absence and capability claims need a check of the actual install, not the agent's own listing or training memory.
