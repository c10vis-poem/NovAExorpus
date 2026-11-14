---
id: 47
title: "Treated the operator's partial reply to a numbered proposal as approval and started work, then proposed new items, while the operator was still answering"
status: open
type: open-source
skill: [task-observer]
proposes_skill: []
target_file: ["~/.agents/AGENTS.md", "~/repos/Aesop-Xi/hooks/checkin-gate.sh"]
siblings_checked: "no family registry entry for this; checked, applies to any agent proposing numbered plans, so the target is AGENTS.md and the check-in gate rather than one skill"
area: "proposal and approval flow"
date: 2026-10-28
session_context: "Session 37dc78ed: intake workflow spec plus hook congruence table proposal"
parked_until:
resolved:
resolution:
reference:
commands_verified: none
---

**Issue:** The agent proposed two items and asked "Go on 1 and 2?". The operator replied with corrections to item 1 only. The agent took that as a go: it wrote the spec, spawned a 77-repo audit subagent, and reported. The operator then sent notes on item 2 that were still incomplete, and also asked about mods and a workflow change. The agent spent several tool calls searching transcripts and proposed a new numbered list (1-4) plus "Go on 1-3?". The operator said: "When I'm still answering your fucking Item number two, don't start creating a fistful of other items and start burning a bunch of tokens on tasks that I never agreed to." This is a restatement of the memory rule "No renumbering mid-answer" and AGENTS Rule 1 (a skipped or unanswered question is not consent). The rule was written down and loaded, and it still failed.

**Suggested improvement:** This is the second violation of the same rule, so the fix is a barrier, not more text. The check-in gate (currently a stub) should treat an operator reply that comments on a numbered item as "under discussion", not approval. State-changing tools and Agent spawns stay blocked until an explicit `/ok N` for that item. Proposals need one item per turn, with no new numbered list while one is open.

**Principle:** A reply that edits a proposal is not approval of it. Until the operator explicitly approves an item, the only allowed actions are answering and revising that item. A new list or new work while one list is open overrides what the operator is still saying.

**Second instance (same session):** The operator's item 2 answer covered every asset: forked repos, scripts, skills and tools in the base repos, Drive, session threads, and all of Anthropic's assets. In replies, the agent restated it as "all the plugins" and never acknowledged the full scope until the operator pointed it out. Same root: answering a narrower version of the operator's words (AGENTS "Use the operator's words", observation 0034).
