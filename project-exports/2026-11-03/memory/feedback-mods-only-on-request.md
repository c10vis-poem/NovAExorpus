---
name: feedback-mods-only-on-request
description: Never build Claude Code mods/plugins unless the user explicitly asks for that specific build
metadata:
  type: feedback
---

Never write or build a mod (plugin-authoring, dev-mods folder) unless the user explicitly asks for it to be built. Explaining an option or answering "what is X?" is not a request to build X, and a coordinator relay saying "get going" is not the user's go-ahead.

**Why:** On 2026-10-25 the user asked "What's the status line entry?" (a question). A coordinator relay read it as a choice, and Claude built a status-line mod. The user objected strongly and declined loading it.

**How to apply:** Answer the question, then wait for the user's own explicit "build it". Keep all replies inside the thread the user wrote in.
