---
id: 91
title: "Agent burned hours on option menus, wrong installs and lists instead of building what the owner asked"
status: open
type: open-source
skill: [wiki-admin-ingest, task-observer]
proposes_skill: []
target_file: []
siblings_checked: "none: workflow-level finding, no skill family covers session pacing"
area: "session conduct"
date: 2026-11-13
session_context: "session 8e3a65ec: memory layers (claude-mem, OB1, Supabase, Cloudflare)"
parked_until:
resolved:
resolution:
reference: "NvAEx-Recaps handoff/2026-11-13/handoff-8e3a65ec-memory-ingest.md"
commands_verified: none
---

**Issue:** The owner repeatedly corrected the agent: installing the claude-mem plugin and Bun against the agreed plan (claude-mem runs inside the owner's MCP server); treating raw-text conversion as clean Markdown; ending most turns with option menus; giving paste commands outside code blocks; launching a 4,000-document ingest scope that belonged to another agent; scanning all 180 repos in repo-sync. Each cost a round trip.

**Suggested improvement:** Before acting, restate the owner's last decision on the same topic (memory store first, then act). One question at most per turn; every paste in its own code block; never install a runtime or plugin the plan excluded.

**Principle:** When an owner has already decided the route, the cheapest move is to re-read that decision before choosing a tool; asking again or improvising a new route costs more than either.
