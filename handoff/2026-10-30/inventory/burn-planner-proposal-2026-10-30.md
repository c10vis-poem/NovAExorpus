# Burn Planner: putting unspent usage to work before it resets

*Proposal only. Nothing gets built, installed or switched on until you say so.*

## The idea in one line

When a big share of your weekly usage is about to expire unused, the system warns you on your phone, suggests jobs inside your open session, and, if you've approved it ahead of time, starts a ready-made big job that stops itself safely before the limit.

## What the three existing parts actually do

I read the code of all three.

| Part | Plugin and file | What it really does today |
|---|---|---|
| **The signal** | burn-baby-burn: `hooks/burn.ts` and `hooks/register.ts` | Reads Claude Code's weekly limit (`seven_day`: percent used and reset time) once a minute.<br>Within 72 hours of the reset, with **25% or more left**, it moves through three tiers: smoulder (72h, a nag every 6h), blaze (24h, every 2h) and inferno (6h, every 30 min).<br>It only shows a status line, a toast and `/burn`. It sends nothing and runs nothing. The thresholds are the `MIN_LEFT` and `TIERS` constants in `burn.ts`. |
| **The safe stop** | heavy-usage: `scripts/usage-meter.js` and `skills/sweep` | Its UserPromptSubmit hook tells Claude to commit, write a resume note and stop before the 5-hour or weekly wall (defaults: 5h at 90%, weekly at 95%).<br>`/sweep` sets how many subagents to fan out based on remaining headroom, and drops to one serial pass near the wall.<br>Its "pace" figure flags **"won't reach"**, meaning you're under-spending. |
| **The trigger** | cache-caffeine: `hooks/wake.ts` and `hooks/register.tsx` | Shows that a mod **can send a real prompt into the open session** (`$.prompt.submit`) at a booked time, for example "wake Claude at 14:12 and check the build". It only works while that session is open. |

**What none of them do yet:** turn "you have 60% left and 20 hours" into an actual job. That's the gap the Burn Planner fills.

## How it would work

### 1. Pre-compiled jobs (the burn queue)

You keep one file of ready-to-run big jobs, for example `NovAExorpus/burn-queue.md`, or the backlog plugin's task store. Each job has:

- **The prompt or command**, for example:
  - `/loop /sweep bugs` on Aesop-Xi.
  - An agent-army batch of 200 corpus docs into the LLM wiki.
  - A claude-war-room pass on NovusAExenti.
  - A code-map of NovAExopia.
- **A size**: S, M or L, matched to roughly how much of the week it needs.
- **A gate**:
  - `suggest`: only ever suggested to you.
  - `ask`: I ask before starting.
  - `auto`: you pre-approved it to start by itself in the inferno tier.
- **Where it runs**: your open terminal session (phone or PC), or a cloud thread.

Nothing runs that isn't in this file, and only you add jobs to it.

### 2. Three ways to reach you, matched to the tiers

| Tier | Window and amount left | Phone notification | Inside your active session | Pre-compiled automation |
|---|---|---|---|---|
| Smoulder | 72h before reset, 25%+ left | One message a day: the % left, the reset time and the top 3 queue jobs that fit | The status line, plus a one-line footer on replies (heavy-usage's footer method): `🔥 58% weekly left · resets in 2d 4h · queue: 3 jobs fit` | None |
| Blaze | 24h before reset | Every few hours, with the jobs that still fit | `/burn` lists the fitting jobs with sizes. You pick one and it starts | `ask` jobs are offered to start now |
| Inferno | 6h before reset | Every 30 min: the final call | Same as blaze | `auto` jobs you pre-approved start through `$.prompt.submit`, the way cache-caffeine starts a wake. heavy-usage's wind-down stops them cleanly: commit, resume note, then stop |

**Phone notifications** go through notify #1 (Telegram, Slack or a webhook), which reaches your phone. That plugin is already on the keep list.

**Messages inside messages** use the footer. It's informational only and never changes what I'm doing.

### 3. Safety rules built in, per your standing rules

- Everything is **off by default**. You turn it on per machine.
- One switch turns it all off mid-session: `/burn off`.
- **It never blocks anything.** It only shows, suggests or starts jobs you listed.
- **No job starts by itself** unless you marked it `auto`.
- heavy-usage's wind-down is the brake, so a burn job can't run you into the wall mid-edit.
- Every start, stop and skip is logged to one file you can read.

## Build approach (decided 2026-10-30): one lean custom plugin

The Builder asked for the leanest option that still works. That's **one custom mod plugin, `nvaex-burn`, built from stripped parts.** It replaces installing four plugins. All three sources are MIT licensed, so credit them in the README.

| Part needed | Taken from | Approximate size |
|---|---|---|
| The tier signal and nag timing | burn-baby-burn `burn.ts` (`weekly`, `assess`, `isNagDue`, `TIERS`) | about 60 lines |
| Starting a job at a set time | cache-caffeine `wake.ts` (`wakeAfter`, `parseWhen`) plus its `$.prompt.submit` call | about 40 lines |
| The brake | Re-implemented inside the mod. It reads `$.session.usage().rateLimits` directly, so it needs **no statusline wiring and no edits to your settings.json or CLAUDE.md**, which heavy-usage's setup does | about 30 lines |
| Phone messages | One HTTPS POST to your Telegram bot or webhook. This assumes mods can make HTTP calls; the jev mod's description mentions `$.http`. **[VERIFY]** | about 20 lines |
| The queue reader | New: reads the burn-queue file | about 40 lines |

That comes to roughly 200 lines in one plugin, with one `/burn` command and one kill switch.

**What it drops:**
- burn-baby-burn's joke quotes.
- caffeine's cache-warming pokes, which spend usage.
- heavy-usage's statusline capture and its global-file edits.
- notify's 6 hook events.

**What stays separate:** heavy-usage's `/sweep` skill can still be one of the queue jobs if you want it. It's a skill, not a dependency.

**[VERIFY] before building:** whether a mod can inject the wind-down line into a turn. harness-scope's `prompt.context` hook suggests it can.

## The changes needed (shown before anything is written)

1. **burn-baby-burn fork**:
   - Keep `assess()` and the tiers.
   - Add reading the queue file, pick the jobs that fit the % left, and put them in `/burn` and the toast.
   - Add an optional webhook POST to notify.
   - Add `/burn off`.
   - Add the `auto` start through `$.prompt.submit`, copied from cache-caffeine's wake.
2. **heavy-usage**: install as-is, and use `/sweep` as one of the standard queue jobs.
3. **notify #1**: set up your Telegram bot or webhook.
4. **The queue file**: you write the first jobs, or I draft them for your approval.

## Limits I verified, and what I haven't

- **Verified from the code:**
  - All three read Claude Code's own rate-limit data.
  - burn-baby-burn needs Claude Code 2.1.287 or newer and a plan with a weekly limit.
  - caffeine's prompt-sending works only while the session stays open.
- **Not verified:**
  - Whether mods (burn-baby-burn and caffeine are mods) run in cloud project threads like this one. They're built for the interactive terminal.
  - Whether a scheduled cloud routine can see your usage numbers.
  
  Until those are tested, the first version should run on your phone's Termux session or a PC terminal.

## Overlap check

This replaces the need for cache-caffeine's wake as a separate plugin. It uses burn-baby-burn, heavy-usage and notify, and would move burn-baby-burn from the cut list to the keep list. cache-caffeine stays cut, and its wake code is borrowed.
