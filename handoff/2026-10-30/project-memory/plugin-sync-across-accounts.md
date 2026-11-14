---
name: plugin-sync-across-accounts
description: How claude.ai account plugins sync to devices/cloud and how to disable them per account and per machine (researched 2026-10-29)
metadata:
  type: reference
  modified: 2026-10-29T06:35:43.950Z
---

Researched 2026-10-29 from code.claude.com/docs/en/plugins/loading.md (#synced-plugins), discover-plugins.md, cloud-environments.md.

- Account plugins are per claude.ai account; turning one off on account A does nothing for account B.
- They land on a device as `<name>@synced`. Terminal Claude Code (v2.1.273+, signed in with claude.ai) syncs once per start: adds new, removes ones turned off on the account.
- Local off-switches live in `~/.claude/settings.json` (per machine, not per account): `"<name>@synced": false` or `"syncClaudeAiPlugins": false` (moves synced copies to ~/.claude/plugins/.trash/ on next start). Marketplace-installed plugins are NOT touched by account changes; need `claude plugin uninstall/disable`.
- Cloud sessions (this project's threads) do pull account plugins: on 2026-10-29 the container had 483 @synced entries, 35 enabled (superpowers, agentkeeper, pmm, searchoclock, etc.).
- Unverified third-party report: plugins removed on claude.ai get re-enabled server-side. Not confirmed.
User has two accounts; see [[user-standing-rules]].
