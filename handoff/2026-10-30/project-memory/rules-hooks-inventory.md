---
name: rules-hooks-inventory
description: Where the 2026-10-29 account-wide rules/hooks/skills/plugins inventory lives and its key findings
metadata:
  type: project
  modified: 2026-10-29T07:35:01.884Z
---

2026-10-29: Read-only inventory, organized by category, for the user's skill/rule repair work: https://claude.ai/artifact/7VegGyMfpKpr9MUWRsQp1h (supersedes the first draft https://claude.ai/artifact/MwTP7DndWUYMQvWJ7H6kFg). The user reviews it and marks keep/cut/rewrite. Nothing gets changed until they sign off.

Key findings:
- Aesop-Xi `.claude/settings.json` registers 35 live hooks (gates: resume, checkin, enforce, git, state, settings, delegation-tripwire, stop, absence...). `hooks/settings.hooks.json` installs the same set into ~/.claude on devices.
- 8 account plugins add 22 hooks that load every session. superpowers injects "MUST invoke skills", which conflicts with the user's rules.
- 483 synced plugins: 35 on (7 of them have no files), 406 off but downloaded (124 with 412 hooks), 42 off and not downloaded.
- The user's own (non-fork) repos are NovAExorpus, NovAExopia (26-plugin marketplace + wiki-admin), NovusAExenti, Aesop-Xi, AEthX-AEsc, CloviX-AEyre, Hyperion-XI (rules/), raw-databank, NvAEx-agentk, Horizon-s-home-grid, and NvAEx-Recaps (private). About 180 other repos are forks.
- 5-day error timeline (Oct 23-29), with audit and prevention picks: https://claude.ai/artifact/3WJxZSKpCHAuG5hzEF353f. Root causes: Aesop-Xi PR #81 (merged Oct 28) made every gate run in the cloud; Aesop-Xi MEMORY.md holds contradictory hook rules (all off vs never disabled); only the phone's hook copies were stubbed, not the repo's. The error ledger is NovAExorpus skill-observations 0042-0051.
- The account skill memory-as-skill is a 2026-07-05 upload snapshot with its memory files bundled inside, and it never syncs back. The live memory is NvAEx-Recaps/memory/ (Oct 28). Recommended fix (awaiting user choice): re-upload the skill as a pointer to that folder. The user rejected editing cowork-plugin-management ("lipstick on a pig").
- Not reached yet: the second account, devices, Drive, account memory.
See [[plugin-sync-across-accounts]].
2026-10-29 check: this cloud container's ~/.claude/settings.json holds only enabledPlugins and no hooks. Its mtime (Oct 28 02:49) is older than the container (Oct 29 06:34), so user-level ~/.claude files persist across threads via the cached environment. Hooks reach a thread four ways: account plugin, repo settings (non-project sessions only), cached ~/.claude, and the setup script. The user says the Aesop-Xi breakage is fixed.
2026-10-30 snapshot: /mnt/project-files/inventory/active-rules-hooks-plugins-2026-10-30.md (what is live in a thread: 35 on, 9 with hooks; only cco read-cache.js can block Reads) and all-account-skills-2026-10-30.md (365 synced plugins, 1568 plugin skills, 84 in enabled plugins, 20 account skills).
2026-10-30 plugin triage (description-level, not deep-read): /mnt/project-files/inventory/plugin-recommendations-2026-10-30.md recommends keeping 116 and cutting 249 of the 365 synced plugins, with a reason for every cut, overlap clusters, and combine ideas (one memory plugin, one Jev plugin, non-blocking verification pack, wiki-admin from parts, Gemini/voice/Android lanes, harness-scope profiles). The user set the target at 80-120 and requires a reason for every cut. Awaiting their review; nothing toggled.
