---
id: 24
title: "Claimed 'no wiki engine chosen' from subagent summaries while the decision doc existed in the vault"
status: open
type: internal
skill: []
proposes_skill: []
target_file: ["~/.claude/CLAUDE.md"]
siblings_checked: "none — CLAUDE.md read-before-claim rule, not a skill family; related absence-claim entries 0007, 0016"
area: "absence claims built from delegated reading"
date: 2026-10-05
session_context: "Synthesizing 11 reader reports on the LLM-wiki corpus"
parked_until:
resolved:
resolution:
reference:
---

**Issue:** I wrote "Wiki engine: 5 candidates, none chosen" in a synthesis and told the operator. The choice was made on 2026-10-02 and is recorded in `docs/WIKI-ADMIN-GUIDE.md`: the `wiki-admin` launcher loads obsidian-wiki, OpenWiki for Claude Code and llm-wiki-compiler. A reader had even cited that guide. The operator had to correct me. This is the third absence claim of this shape (see 0007, 0016).

**Suggested improvement:** Before stating "X was never decided/installed", grep the decision docs (RESUME, PENDING, docs/*GUIDE*, memory) for X, and run `ls`/config checks for installed tools. Structural barrier: the absence claims keep recurring, so a Stop-hook check could flag "none chosen / never / not installed" phrases in a reply that has no matching Read or grep in the same turn.

**Principle:** Subagents report what their batch contains; the absence of a decision in a batch is not the absence of a decision. Absence claims need a direct check against the decision record, not an aggregation of partial reads.
