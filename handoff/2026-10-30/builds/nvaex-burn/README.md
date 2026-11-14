# nvaex-burn

nvaex-burn turns weekly usage that would otherwise expire unspent into jobs you approved ahead of time. It's one Claude Code mod with no dependencies.

## What it does

- **Warns.** Within 72 hours of your weekly reset, with 25% or more of the week left, it shows a status line. It nags in three tiers:
  - smoulder: once a day;
  - blaze: every 2 hours, inside the last 24 hours;
  - inferno: every 30 minutes, inside the last 6 hours.
- **Where nags go:**
  - a toast;
  - a native notification through your own notification channel;
  - optionally, a POST to a webhook. An ntfy.sh topic URL works, and so do phone automation apps (Tasker, MacroDroid, Android routines) that react to ntfy notifications.
- **Suggests.** It reads your burn queue and lists the jobs that fit what's left, biggest first.
- **Starts only what you allowed:**
  - `suggest` jobs are only ever listed.
  - `ask` jobs start when you run `/burn start <id>`.
  - `auto` jobs start by themselves, in the inferno tier only, one at a time, and once per weekly window.
- **Brakes.** While a burn job runs, once the 5-hour window reaches 90% or the weekly one reaches 95%, it adds one wind-down instruction to the conversation: commit, write a resume note, stop. It also tells you.
- **Never blocks.** It never refuses a tool, a prompt or a stop. Every failure is swallowed.

## Commands

- `/burn`: status, plus the jobs that fit.
- `/burn start <id>`: run an `ask` or `auto` job now.
- `/burn off` and `/burn on`: the kill switch.
- `/burn done`: clear the running job.

Creating the file `~/.nvaex/off` also silences it, along with every other nvaex hook.

## Burn queue

The queue lives at `~/.nvaex/burn-queue.json` by default, or wherever the `queueFile` option points. See `burn-queue.example.json`.

```json
{ "jobs": [ { "id": "aesop-bugs", "title": "Bug sweep, Aesop-Xi", "prompt": "Run a full bug sweep of Aesop-Xi and record findings in heavy-usage-sweep/FINDINGS.md", "size": "L", "gate": "auto", "repo": "Aesop-Xi" } ] }
```

`size` is roughly the share of the week a job spends: S = 5%, M = 15%, L = 30%.

## Options

Set these in `/config`:

| Option | Default |
|---|---|
| `queueFile` | `~/.nvaex/burn-queue.json` |
| `webhookUrl` | Empty (none) |
| `appNotify` | On |
| `minLeftPercent` | 25 |
| `brakeFiveHour` | 90 |
| `brakeWeekly` | 95 |

## Requirements

- Claude Code 2.1.287 or newer, with mods enabled.
- A plan with a weekly limit.
- An interactive session: a terminal, Termux, or the desktop app. It works only while that session is open.

## Credits

- The tier logic is adapted from burn-baby-burn (eel-brah, MIT).
- The job-start pattern is from cache-caffeine (lperezmo, MIT).
- The brake idea is from heavy-usage (heavyc-dev, MIT).

The license is MIT.
