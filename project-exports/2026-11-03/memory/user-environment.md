---
name: user-environment
description: User runs Claude Code in Termux on Android, ~106 plugins synced from claude.ai, a local quota-hook plugin blocks prompts
metadata:
  type: user
  modified: 2026-10-24T12:29:59.658Z
---

User runs Claude Code (v2.1.310 as of 2026-10-24) in Termux on Android. They have about 106 plugins synced from claude.ai (list in /mnt/project-files/plugins/synced-plugins.md).

A plugin with hooks/enforce_quota.py (TOKEN_QUOTA_DAILY) blocks their prompts. It is NOT among the synced copies seen in cloud sessions, so it is installed locally on the phone. Documented fix: find it with grep in ~/.claude/plugins, then `claude plugin disable <name>@<marketplace>` from the shell.

**How to apply:** give verified, sourced commands only; the user gets frustrated by guesses. "Turlock skill" meant the termux-helper skill.
