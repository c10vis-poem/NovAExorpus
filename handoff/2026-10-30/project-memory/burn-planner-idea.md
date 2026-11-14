---
name: burn-planner-idea
description: User wants unspent weekly usage turned into big pre-approved jobs before reset (burn-baby-burn + heavy-usage + notify); proposal 2026-10-30
metadata:
  type: project
  modified: 2026-10-30T00:45:32.162Z
---

2026-10-30: The user often lets large usage allowances expire when they could have run a big multi-tier job. They asked for a way to use burn-baby-burn: phone notifications, suggestions inside active sessions, and pre-compiled automations.

Proposal (not built): /mnt/project-files/inventory/burn-planner-proposal-2026-10-30.md. It combines:
- burn-baby-burn's tier signal (72h, 24h and 6h before the reset, with 25%+ of the week left).
- A burn-queue file of pre-approved jobs, each gated suggest, ask or auto.
- notify #1 (Telegram or webhook) for phone messages.
- heavy-usage's reply footer, plus its wind-down as the brake.
- cache-caffeine's $.prompt.submit to start `auto` jobs.

Off by default, `/burn off` kill switch, nothing blocks.

Unverified: whether mods run in cloud project threads. Plan to run v1 in Termux or on a PC terminal. Moves burn-baby-burn to keep. See [[rules-hooks-inventory]].
2026-10-30: The user prefers lean custom plugins built from stripped parts over stacking several plugins. Decision: one mod, `nvaex-burn` (about 200 lines), built from burn-baby-burn's burn.ts, caffeine's wake and prompt.submit, an in-mod brake reading $.session.usage(), and a Telegram POST.
