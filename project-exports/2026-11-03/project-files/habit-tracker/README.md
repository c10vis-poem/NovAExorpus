# Cadence

A local-first habit tracker. Single user, no accounts, no backend, no network calls: everything is stored in your browser (IndexedDB) on your own machine.

## Features

- **Habits**: daily or chosen weekdays, time of day, emoji, color, archive, delete, reorder, up to five reminders each.
- **Today**: check in, add a note, excuse a day (skip), backfill past days, undo. Streaks, milestones and a statistics dashboard on Insights.
- **Calendar**: a month view per habit (eight day states, each with its own shape and text, not only color), month navigation, click a day to check it, skip it or edit its note. A year heatmap of all habits and a filterable activity log (50 rows at a time).
- **Quick Add**: type a sentence such as "Meditate every weekday at 7am" on Today, preview the habit it understood, then edit and save.
- **Smart Reminder Timing**: when you usually check in well after a reminder, the habit card suggests a better time. Accept or dismiss (hidden for 30 days).
- **Schedule Fit**: flags a scheduled weekday you keep missing while your other days go well.
- **Weekly Insights**: most consistent habit, biggest slip, weakest day and one suggestion, for the last 7 days.
- **Reminders**: system notifications with an in-app banner fallback, pause, quiet hours, streak at risk.
- **Settings**: theme (System, Light, Dark), week start (Monday or Sunday), notifications, data export and import, reset.
- **Accessibility**: skip link, one h1 per page that takes focus on navigation, per-page document titles, keyboard shortcuts, reduced motion support, WCAG AA contrast (checked with axe in the test suite).

All intelligence features run on your device from your stored check-ins. Nothing is sent anywhere.

## Requirements

Node 22 (tested on 22.22) and npm.

## Install and run

```bash
npm install
npm run dev                        # http://localhost:5173
npm run build && npm run preview   # http://localhost:4173
```

## Privacy

No accounts, no backend, no analytics, no network calls. Everything lives in this browser's IndexedDB. Clearing site data deletes it, so use Settings > Export data for backups.

## Export and import

Settings > Data > **Export data** downloads a pretty-printed (2-space) JSON file named `cadence-backup-YYYY-MM-DD.json` (see `exportFileName` in `src/domain/messages.ts`). Version 1 format:

```json
{
  "format": "cadence-export",
  "version": 1,
  "exportedAt": "2026-03-04T09:00:00",
  "habits": [{ "id", "name", "description", "color", "emoji", "startDate", "timeOfDay", "schedule", "scheduleHistory", "reminders": ["HH:mm"], "archived", "order", "createdAt" }],
  "checkins": [{ "habitId", "date", "kind": "done|skip", "note", "checkedAt" }],
  "settings": { "theme", "weekStart", "remindersPaused", "quietHours": { "enabled", "start", "end" }, "streakAtRisk": { "hour", "reminder" } },
  "suggestionDismissals": [{ "habitId", "dismissedOn" }]
}
```

**Import data file** reads a file, validates all of it, and shows a preview (export time, habit and check-in counts, and what Merge would do). Nothing changes until you press **Import**. Modes: **Merge** (default; adds missing habits and check-ins, local data wins on conflicts) and **Replace all data** (asks for confirmation first). A file with any problem (not JSON, wrong format, unknown version, bad field) is rejected whole with a message; imports are all-or-nothing. **Reset all data** (type RESET to confirm) clears everything.

## Keyboard shortcuts

`n` new habit, `t` Today, `h` Habits, `c` Calendar, `i` Insights, `s` Settings, `/` Quick Add, `?` list shortcuts. Ignored while typing, with Ctrl/Cmd/Alt, or while a dialog is open.

## Tests

```bash
npm test                 # unit tests (Vitest): schedules, validation, ordering, emoji, today filtering, streak engine and statistics, reminder rules
npx playwright install chromium   # once, to download the browser
npm run test:e2e         # Playwright suite, run against both `npm run dev` and `npm run preview`
npm run fixtures         # rewrites e2e/fixtures/data/*.json from e2e/fixtures/datasets.ts
```

`npm run test:e2e` starts both servers itself (ports 5173 and 4173, which must be free) and runs every test in a `dev` and a `preview` project.

## Controlling "today"

The app's notion of "now" is deterministic in tests, two ways:

1. **URL parameter**: open `/?now=YYYY-MM-DDTHH:mm` (local time), for example `/?now=2026-03-04T09:00` (a Wednesday). The value fixes "now" for the whole session and survives hash navigation and reloads of that URL. Today shows "Wednesday, 4 March 2026" and the new-habit start date defaults to `2026-03-04`. Malformed values are ignored.
2. **Playwright clock control**: without the parameter the app reads `new Date()` (and re-reads each minute), so `page.clock.install({ time })` works as expected.

All time reads go through `src/data/clock.ts`.

## Data

- IndexedDB database `cadence`: object store `habits` (one record per habit) and `meta` (holds `schemaVersion`, currently `1`). The schema version is also mirrored in `localStorage` as `cadence.schemaVersion`.
- Habit fields: `id`, `name`, `description`, `color`, `emoji`, `startDate` (YYYY-MM-DD), `timeOfDay`, `schedule` (`daily` or `weekdays` with days 0 = Mon .. 6 = Sun), `archived`, `order`, `createdAt`.

## Layout

- `src/domain/`: pure logic (schedules, validation, ordering, emoji, templates, Today filtering) with unit tests
- `src/data/`: IndexedDB access, the habit store, the app clock
- `src/components/`, `src/pages/`: UI

## Streak engine

`src/domain/streaks.ts` is a pure module (no storage, no clock): `computeStreaks`, `completionRate`, `habitStats`, `milestoneCrossed`, `summarizeDashboard`. Tests: `src/domain/streaks.test.ts`. Schedule edits are kept in `habit.scheduleHistory` and apply from the day of the edit; earlier days keep the schedule they had.

## Reminders

Each habit can have up to five daily reminder times (habit form, section "Reminders"). While the app is open, a scheduler delivers every due time at most once per habit, time and day, on scheduled days only, and only while the habit is not done or excused. Delivery uses a real browser notification when permission is granted, and an in-app banner ("Due reminders", with Mark done, Snooze 10 min, Dismiss) in every other case, including when the notification constructor throws. Permission is requested only by the first "Add reminder" click while it is "Not asked". Settings has Notifications (permission status and guidance), Reminder controls (pause all, quiet hours) and Streak at risk (hour, extra reminder switch).

- Code: pure rules in `src/domain/reminders.ts` (unit tests in `reminders.test.ts`), storage and the atomic claim in `src/data/reminderDb.ts`, the scheduler in `src/data/reminders.tsx`, notifications in `src/data/notifications.ts`.
- Storage: IndexedDB version 3 adds the `reminders` store (delivery records and banner entries); settings live in `meta`. Habits gain an optional `reminders` list (`{ time, addedAt }`); older data without it loads unchanged.
- Dedupe: one evaluation is one read-write IndexedDB transaction over all stores, so reloads, new loads with a different `?now=`, and several tabs of the same browser profile claim each (habit, date, time) exactly once.
- Evaluation triggers: page load (after data loads), a timer every 15 seconds of real time, `visibilitychange` to visible, window `focus`, every `setNow` / `advanceMinutes`, and every habit, check-in, or settings change. Hidden pages keep evaluating whenever their timers run and deliver then; the visible/focus evaluation is the catch-up for throttled or frozen timers, and per-time dedupe keeps it from repeating anything. Times of earlier days are never delivered.
- Permission is always read live (`Notification.permission` and `"Notification" in window` at call time). One exception: when `Notification.permission` says "denied" but the Permissions API says "granted" (headless Chromium reports it that way after `permissions: ['notifications']`), Cadence treats it as granted.

### Test hooks (present in `npm run dev` and `npm run preview`)

- `window.__cadenceNotifications`: array reset on every page load; one entry per system notification the app created: `title`, `body`, `tag`, `habitName`, `kind` (`"reminder"` or `"streak-at-risk"`), `dueTimes` (`["HH:mm"]`; `["HH:00"]` for an at-risk-only entry), `firedAt` (app-time ISO). Pushed only after the notification was created.
- `window.__cadenceTest.setNow("YYYY-MM-DDTHH:mm[:ss]")`: in `?now=` mode, replaces the pinned now (forward or backward), re-renders every page, and runs one scheduler evaluation (also while the tab is hidden). Returns a promise that resolves when that evaluation has finished. Outside `?now=` mode it throws.
- `window.__cadenceTest.advanceMinutes(n)`: `setNow` with now plus n minutes.
- `window.__cadenceTest.clickNotification(i)`: runs exactly the handler of `window.__cadenceNotifications[i]` (focus the window, open Today, highlight the card for 5 seconds, focus its check button).

Tests stub permission with `context.addInitScript`: a stand-in `window.Notification` with a static `permission` getter ("granted", "denied", "default") and a `requestPermission()` that counts calls, or `delete window.Notification` for "unsupported". A real grant is `browser.newContext({ permissions: ['notifications'] })`. See `e2e/reminders.spec.ts`.

### Sprint 4 test identifiers

Calendar: `calendar-month`, `calendar-day` (`data-date`, `data-state`, `data-shape`, `data-today`, `data-has-note`), `calendar-pad`, `calendar-day-detail`, `calendar-day-status`, `calendar-note-text`, `calendar-legend`, `streak-current`, `streak-longest`, `heatmap-cell`, `log-row`, `log-count`. Data: `export-status`, `import-error`, `preview-exported`, `preview-habits`, `preview-checkins`, `preview-merge`, `import-result`, `theme-status`. Intelligence: `reminder-suggestion` (`data-time`), `schedule-fit-suggestion`, `weekly-insights`, `weekly-insights-range`, `weekly-insight`, `quickadd-explain`. Theme is `data-theme` on `<html>`; settings are mirrored in `localStorage` as `cadence.theme` and `cadence.weekStart`.
