---
name: claw-toolkit-project
description: User's planned "claw" toolkit: one MCP server replacing Playwright + their pplx Perplexity CLI; "claw hooks" = callable device/browser functions
metadata:
  type: project
  modified: 2026-10-25T21:06:07.053Z
---

Started 2026-10-25. User wants one custom toolkit that combines Perplexity search, Chrome DevTools (CDP), their Android device control, and Playwright-like browser tools, and it must REPLACE Playwright and their standalone Perplexity CLI repo (c10vis-poem/Novus-perplexity-cli, a fork of perplexityai/perplexity-cli `pplx`).

"Claw hooks" does NOT mean Claude Code hooks. It means executable functions the agent calls that act on the user's own devices and browsers. Needs headless and in-session (live browser/device) modes, and inference through their Claude Pro, Gemini/Google AI Pro, GCP and other APIs.

User pointed at browser-use and Firecrawl as worth reverse engineering (forks: NovA-browser-use, Novus-firecrawl).

Must also run OUTSIDE Termux, embedded in the user's APK: AEthX-AEsc (termux-app fork renamed `aethx.aesc` + Æsc core, plain JVM Kotlin, AgentTool/AgentLoop; IPC = AF_UNIX, WebSocket to Horizons-UI, ADB loopback 127.0.0.1:5555 UID 2000). Device control goes through "the ADB debug web loop" (STT once rendered it "red blue ATB") = app pairs with its own adbd over wireless debugging, no PC/root (reading sent to user to confirm). Proposed Kotlin core + official Kotlin MCP SDK ("no JS MCP"); user forked kotlin-sdk.

No Android MCP was found in their GitHub (checked list_repos for "mcp" and "android"); asked the user where it lives.

Proposal doc (unapproved, nothing built): https://claude.ai/artifact/2a9BgPvtCLSFSTrevUM6oT

**How to apply:** Build nothing until the user explicitly says to build ([[feedback-mods-only-on-request]]). Don't scrape claude.ai/gemini web apps for inference; use supported routes.
