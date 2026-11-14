---
id: 61
title: "Plugin data deleted while its sync sources were still on, so the next session start re-downloaded all of it"
status: open
type: open-source
skill: []
proposes_skill: []
target_file: ["~/.claude/settings.json"]
siblings_checked: "none: target is a settings file; principle 4 (a defect is fixed only where it happens) is related"
area: "removing auto-installed content; verifying a removal"
date: 2026-11-06
session_context: "Operator ordered all synced plugins deleted. A parallel session deleted the folders at 03:41Z and turned the sync setting off only at 03:47:47Z; the folders came back 03:47:19-38Z, just before a new session's first record at 03:47:39Z."
parked_until:
resolved:
resolution:
reference:
commands_verified: "run: stat and git reflog of plugins/synced and plugins/marketplaces showed the 03:47Z re-creation and fresh clones; run: settings.json read shows syncClaudeAiPlugins false and 13 extraKnownMarketplaces still listed"
---

**Issue:** Generated plugin folders were deleted first and the setting that regenerates them was changed six minutes later. A session starting in that window re-downloaded 327M of synced plugins and re-cloned the marketplaces. The 13 marketplace entries in settings were not removed at all.

**Suggested improvement:** When removing anything a program regenerates, turn off every source first, then delete, then start a fresh session and check the folders stayed empty. Warn about other sessions starting in between.

**Principle:** Stop the source before deleting the output, and count a removal as done only after a restart leaves it gone.

**Restart check (2026-11-06):** with the setting off since 19:47Z-local, a later session start moved the synced plugin folders to `plugins/.trash` at 00:01:31 local (227 entries), leaving `plugins/synced/<bucket>/` holding only an empty `.staging`, and `installed_plugins.json` empty. Dangling left behind: `statusLine` in settings.json still points at a `plugins/synced/.../statusline.sh` that no longer exists, and `pluginConfigs` still names `claudinator@synced`.
