---
name: feedback-plugins-are-parts
description: Judge plugins as parts to mix and match, never by their hooks; deep-read before recommending
metadata:
  type: feedback
  modified: 2026-10-29T07:30:05.793Z
---

The user customizes everything. They pull skills, agents, scripts and hooks out of several plugins and combine them. Hooks can be set to ignore or redesigned so they don't overlap. So a plugin is never ruled in or out because of its hooks.

**Why:** On 2026-10-29 the user objected when plugins were weighed by their hook counts ("you failed to realize we can customize all of this").

**How to apply:** Evaluate each part on its own: skill, agent, command, script, hook. Say whether a review is description-level or a deep read, and deep-read before recommending. The catalog of all 446 downloaded plugins, sorted into 16 categories, is https://claude.ai/artifact/R3Xc8Mk95RCD7998h3KvUD. agent-ingest-audit-optimize has been deep-read. See [[rules-hooks-inventory]].
2026-10-30: The user approved subagents for read-only skill review, with conditions: use Sonnet or Haiku for read tasks (never Opus for reading), and the output is a NEW standalone deliverable. Never "frankenstein" (merge into or edit) their existing files.
