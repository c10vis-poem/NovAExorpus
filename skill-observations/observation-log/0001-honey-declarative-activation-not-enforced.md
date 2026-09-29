---
id: 1
title: Honey mode stayed declared-active but unenforced through a long investigation session
status: open
type: open-source
skill: [honey]
proposes_skill: []
siblings_checked: "no skill-families.md registry exists yet; evaluated honey-ccr, honey-chat, honey-compress, honey-debt, honey-design, honey-eco, honey-gain, honey-hive, honey-loop, honey-memory, honey-px, honey-review, honey-superpowers — instance-specific to honey's own declarative-activation mechanism (a SessionStart reminder saying 'Honey mode is ACTIVE'), no propagation: the siblings govern different concerns (compression, cost accounting, review, cross-project memory) and don't rely on the same passive announcement pattern to enforce terseness."
area: activation / enforcement mechanism
date: 2026-09-18
session_context: "Long multi-hour infrastructure investigation session (OmniRoute/Mem0/Terrestrial Brain/GCP). A SessionStart hook declared 'Honey mode is ACTIVE (intensity: ultra)' at the very start, but responses grew into multi-paragraph recaps and citations as the session lengthened. User: 'you need to set up that honey for devs and actually start using it cuz you are producing way too many fucking words I did not need six paragraphs about something that doesn't exist.'"
parked_until:
resolved:
resolution:
reference:
---

**Issue:** A SessionStart reminder declaring a behavioral mode "ACTIVE" does not by itself keep that behavior enforced across a long session — verbosity crept back in specifically during multi-tool investigation turns, where the temptation to narrate findings and cite sources grows with the amount of work done. The declaration was present in context the whole time; it was not checked against before each response.

**Suggested improvement:** Honey's activation reminder could name the specific failure mode explicitly ("after any multi-tool investigation turn, compress the report to a list — no recap of what the user already said, no restating of internal doc paths") rather than a general intensity setting, since the general framing didn't survive contact with a long session. A structural self-check before sending a response that follows 3+ tool calls (similar to task-observer's "checkpoint after every 3rd completed todo item" pattern) would catch this without relying on remembering a session-start banner.

**Principle:** A behavior declared "active" in a passive context injection is not the same as a behavior enforced — anything meant to hold across a long session needs a structural trigger tied to an event in the tool record (like task-observer's checkpoint pattern), not just a standing instruction the agent is expected to keep re-noticing on its own.
