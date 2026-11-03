---
name: plugins-panel-mod
description: plugins-panel mod lives in NvAEx-Recaps claude-code-workspace/, repo root is the nvaex-recaps marketplace (2026-10-25)
metadata:
  type: project
  modified: 2026-10-25T20:48:02.081Z
---

On 2026-10-25 the user explicitly asked for a plugins side panel mod. It lives in c10vis-poem/NvAEx-Recaps under `claude-code-workspace/plugins-panel/` (draft PR #6). The repo root `.claude-plugin/marketplace.json` makes the repo the `nvaex-recaps` marketplace. The user's "cloud code workspace folder" meant `claude-code-workspace/`, and new mods go there.

**Why:** the user runs Claude Code on Termux, so mods built in a cloud session must be pushed to a repo to reach the phone.

**How to apply:** for later mod changes, edit that folder and keep [[feedback-mods-only-on-request]]. The status line can't be clicked, and `/plugins` is a reserved command name.
