# Sprint 3 Handoff

## What Was Implemented

**Reminder times (F1).** The habit form has a "Reminders" section: "Add reminder" (disabled at 5 rows), one `input type=time` per row labelled "Reminder time N", and "Remove reminder N". The first row defaults to 09:00, later rows to the first free of 09:00, 12:00, 15:00, 18:00, 21:00. Save rejects an empty time ("Enter a time for every reminder.") or a duplicate ("Each reminder time must be different."), `role=alert`, and nothing is saved. Times are stored ascending as `{ time, addedAt }` on the habit; a time already on the habit keeps its original `addedAt`, a new or edited time gets "now" (rule R2). The Habits card shows `habit-reminders` ("Reminders: 07:00, 19:30"), absent with none. Sprint 1 and 2 data without `reminders` loads unchanged (e2e C5 deletes the field from stored habits and reloads).

**Scheduler (R1 to R7, R12 to R14).** All rules are pure functions in `src/domain/reminders.ts` (`planEvaluation`, `isDue`, `inQuietHours`, `atRiskStreak`, banner helpers, content builders). `src/data/reminders.tsx` runs evaluations; `src/data/reminderDb.ts` performs each one as a single IndexedDB read-write transaction over habits, check-ins, meta and reminders, so the claim of each (habit, date, time) is atomic across reloads, `?now=` loads and tabs. Due times that are ineligible are stored as consumed. All newly due times of one habit (plus the at-risk reminder if due) merge into one delivery. Triggers: load after data, every 15 s real time, `visibilitychange` to visible, window focus, `setNow`/`advanceMinutes`, and any habit, check-in or settings change. Only today's times are ever considered.

**Delivery channel (R7), permission (R15), Settings (F10).** Permission is read at delivery time. Granted creates a real `Notification` (tag, body, click handler) and pushes to `window.__cadenceNotifications`; anything else, or a throwing constructor, creates a banner entry. "Add reminder" is the only caller of `requestPermission()` and only while permission is "Not asked"; after a granted/denied answer it is not asked again in the page session. Settings sections: "Notifications" (`notification-permission`: Granted, Denied, Not asked, Unsupported with icon; `notification-guidance` with the exact texts; refreshed on visible/focus), "Reminder controls" (Pause all reminders, Enable quiet hours, Quiet hours start/end), "Streak at risk" (Streak at risk hour select, Streak-at-risk reminder switch). Equal quiet hours are rejected with the exact error and the stored values stay (the inputs show the stored value).

**Banner (R8 to R11).** `reminder-banner` (`role=region`, name "Due reminders") at the top of the content on every route, title `reminder-banner-title`, one `reminder-banner-item` per habit in Habits-page order, buttons "Mark done: X", "Snooze 10 min: X", "Dismiss: X". It is not in the DOM when nothing is visible. Entries persist (reload shows each once without a notification), disappear when the habit is done, skipped, archived, deleted, or the date changes, and a new delivery revives a snoozed or dismissed entry. Snooze hides until click time + 10 min (visible again at exactly +10:00 with `?now=`; with the real clock within the 15 s tick) and stays hidden while paused or quiet. Mark done uses the same code as the Today check (`src/useCheckIn.ts`): Undo toast, milestone toast, progress and streak update.

**Notification click (R19).** `window.focus()`, navigate to Today, scroll the card into view, set `data-highlighted="true"` on it (ends on route change or after 5 s), focus its "Check in <name>" button. A habit that is no longer shown opens Today with no highlight and no error.

**Pause and quiet hours (F14).** Global pause plus quiet hours (start inclusive, end exclusive, midnight wrap) are stored in settings, shown as `paused-notice` ("All reminders are paused.") on Today, and take effect on the next evaluation without a reload.

**Streak at risk (F15 to F17).** `streak-at-risk-badge` ("Streak at risk", amber outline plus icon) on a Today card when the habit is scheduled today, not done or skipped, streak shown on the card >= 3, and now >= the configured hour. Independent of pause, quiet hours, permission and reminders. The extra reminder is delivered once per habit and day through the same rules (title `Streak at risk: <name>`, body `Your <N>-day streak ends today unless you check in.`), merges with a regular reminder, and is consumed by pause or quiet hours. With the switch off nothing is created and nothing is consumed.

**Clock.** `src/data/clock.ts` can now move the pinned "now" and notifies subscribers; `useNow` follows it, so `setNow` re-renders every page. `?now=` accepts optional seconds.

## How to Run

```
cd /home/user/habit-tracker
npm install
npm run dev                        # http://localhost:5173
npm run build && npm run preview   # http://localhost:4173
npm test                           # 117 unit tests (44 new in src/domain/reminders.test.ts)
npm run test:e2e                   # 234 tests: 117 on dev (5173) and 117 on preview (4173); starts and stops both servers
```
Ports 5173 and 4173 must be free. No servers are left running by me.

## Test hooks (both dev and preview)

- `window.__cadenceNotifications`: reset on every page load; entries `{ title, body, tag, habitName, kind, dueTimes, firedAt }`, pushed only after the notification was created.
- `window.__cadenceTest.setNow("YYYY-MM-DDTHH:mm[:ss]")`, `advanceMinutes(n)`: only in `?now=` mode (they throw otherwise). They replace the pinned now, re-render, and run one evaluation whether the page is visible or hidden. They return a promise that resolves when that evaluation is finished, so `await page.evaluate(...)` is enough, no polling needed.
- `window.__cadenceTest.clickNotification(i)`: runs the same handler as a click on `window.__cadenceNotifications[i]`.
- No other hooks. Permission is stubbed by tests with `addInitScript` as described in the contract; the app reads `Notification.permission` and `"Notification" in window` at call time and calls `Notification.requestPermission()` only from "Add reminder".

New test identifiers: `reminder-banner`, `reminder-banner-title`, `reminder-banner-item`, `habit-reminders`, `notification-permission`, `notification-guidance`, `paused-notice`, `streak-at-risk-badge`, `data-highlighted` and `data-habit-id` on the Today `article`. Buttons and inputs use the exact labels of the contract. New e2e file: `e2e/reminders.spec.ts` (62 tests per project covering F1 to F17, D1 to D4, V1 to V4, C5).

## F11 frozen-timer variant (how hidden evaluation is suspended)

There is no separate "suspend" hook (the contract defines none). Hidden pages are treated like visible ones by the scheduler: whenever a timer runs, or `setNow`/`advanceMinutes` is called, an evaluation runs and delivers. The "frozen" case therefore means that no timer ran in between:

- With `?now=`: jump straight from 08:00 to 13:00 in one `setNow` while hidden. That single evaluation is the catch-up and delivers one merged notification with `dueTimes` ["09:00","12:00"]; the later `visibilitychange` to visible runs another evaluation that finds both times recorded and delivers nothing.
- With the real clock (e2e does this): `page.clock.install`, create the habit, hide the tab, `page.clock.pauseAt(...)` (no timer can fire, so no evaluation runs), `page.clock.setFixedTime(13:00)`, then dispatch `visibilitychange` to visible. The visible evaluation is the only one and delivers the merged notification.

## Self-Evaluation

| Criterion | Status | Notes |
|-----------|--------|-------|
| F1 Reminder times in the form, persistence, card line, limits, errors, cancel | PASS | e2e (2 tests) |
| F2 Granted: one notification, exact title/body/kind, no banner, still one later | PASS | e2e with stand-in and with real `permissions: ['notifications']` |
| F3 Denied: banner "1 reminder due", "Due 09:00", Mark done removes it, Undo works | PASS | e2e; also unsupported API and a throwing constructor |
| F4 Snooze 09:00 / 09:09 / 09:10, reload persistence, real-clock variant | PASS | e2e |
| F5 Dismiss, not back after reload or later | PASS | e2e |
| F6 Stacking: one banner "2 reminders due" in Habits order; granted gives two notifications | PASS | e2e |
| F7 No fire: unscheduled, completed (also after uncheck), skipped, paused (also after unpause), quiet hours edges and wrap, archived, future start, delete with pending entry | PASS | e2e (a) to (h) |
| F8 Dedupe across loads, edits, remove/re-add, two tabs (notification and banner) | PASS | e2e |
| F9 Permission timing: zero requests on load, pages, plain habit, Settings; one on first Add reminder; none after an answer | PASS | e2e |
| F10 Status and exact guidance for four states, live refresh | PASS | e2e, including real grant |
| F11 Hidden tab, catch-up, midnight, quiet hours, frozen timers | PASS | e2e; see section above |
| F12 Real timers: runFor 01:05, fastForward 2.5 h merged | PASS | e2e with `page.clock` |
| F13 Notification click: Today, highlighted, button focused, highlight ends | PASS | e2e |
| F14 Pause and quiet hours persist, notice, equal times rejected | PASS | e2e |
| F15 Streak at risk badge and notification, none after fresh load | PASS | e2e (granted and denied) |
| F16 Badge exclusions (streak 2, excused, unscheduled day, done) | PASS | e2e |
| F17 At-risk hour, switch off, pause/quiet, merge with 20:00 reminder | PASS | e2e |
| D1 to D4 | PASS | e2e |
| V1 banner placement, style, animation, reduced motion, 375 px, nav visible | PASS | screenshots reviewed (light, dark, 1280 and 375 px); reduced motion asserted via computed animation name |
| V2 banner buttons text, at least 40 px (44 px), AA contrast | PASS | measured height; amber and teal tokens reuse the existing AA palette in both themes |
| V3 badge amber outline plus icon plus text; permission status icon plus text | PASS | e2e asserts svg and 2 px border |
| V4 form, Settings and card line match existing styling | PASS | screenshots reviewed |
| C1 build, unit and e2e on dev and preview, including all Sprint 1 and 2 tests | PASS | build clean; 117 of 117 unit; 234 of 234 e2e (also 124 of 124 reminders tests with 4 workers) |
| C2 no console errors or non-local requests | PASS | the automatic fixture asserts it in every test |
| C3 pure logic with unit tests for R1 to R6, R11, R12, R17, R18 | PASS | 44 unit tests |
| C4 no stubs, real Notification API, persisted state, hooks only observe or move time | PASS | |
| C5 Reminder data in stored habits and settings, old data loads | PASS | e2e removes `reminders` from stored habits and reloads |

## Deviations and Notes

- **Headless permission quirk.** In this Chromium (156) headless, `Notification.permission` reports "denied" even with `permissions: ['notifications']`, while `navigator.permissions.query` reports "granted". The app upgrades "denied" to granted only in that exact disagreement (`getPermission` in `src/data/notifications.ts`), so the contract's real-grant test (F2, F10) works. In real browsers both values agree and nothing changes. Stand-ins (static `permission`) are unaffected because their Permissions API state is never "granted" without a grant.
- **Frozen-timer variant.** No extra hook; see the F11 section.
- **`setNow` returns a promise** that resolves after the evaluation (the contract only says it runs one). Callers that ignore it behave as specified.
- **Quiet hours inputs** show the stored value at all times; an equal start/end shows the error and does not change the input or storage.
- **Switch off is not consumption.** With "Streak-at-risk reminder" off, evaluations neither deliver nor consume the at-risk slot, so turning it on later the same day still delivers once (pause and quiet hours do consume, per R3).
- **Notification tag** is `cadence:<kind>:<habitId>:<date>:<times joined by +>`, so a regular and an at-risk notification of the same habit never replace each other.
- **Schema.** IndexedDB version 3 (adds `reminders`); logical `schemaVersion` stays 1 (additive).
- **Today unchanged otherwise.** The check logic moved to `src/useCheckIn.ts` (shared with the banner); Undo and milestone behavior are identical and the Sprint 2 e2e tests pass untouched.
- Commits are local only; `pge-workspace/` is untracked.

## Known Limitations

- Habits and check-ins changed in one tab are not pushed live to another open tab's screen (as in Sprint 2). Reminder evaluation always reads fresh data from IndexedDB, so a reminder never fires for a habit completed in another tab; banner and settings state of the other tab refreshes at its next evaluation (at most 15 s, or on focus/visible).
- With the real clock, a snoozed entry reappears on the next 15 s tick after +10:00 (within the contract's 30 s).
- Calendar, heatmap, activity log, export/import, week start, quick add, smart timing, weekly insights and schedule-fit stay out of scope.
