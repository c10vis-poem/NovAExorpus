APPROVED

# Sprint 3 Contract

## Scope

All Sprint 3 features from the spec, none omitted:

1. Per-habit reminder times (zero or more) in the habit form
2. Reminder scheduler while the app is open (scheduled days only, not when completed, at most once per habit per time per day, no duplicates across reloads or tabs, catch-up after a hidden tab or sleep)
3. Notification permission requested only when the first reminder is added; permission status and guidance in Settings
4. In-app fallback banner (permission denied, not asked, or API unsupported) with "Mark done", "Snooze 10 min", "Dismiss", stacked into one banner
5. Clicking a system notification focuses the app on the relevant habit
6. Global pause and quiet hours
7. Streak-at-risk badge and optional evening reminder (configurable hour)

Sprint 1 and 2 behavior is unchanged. All 110 existing e2e tests and 73 unit tests still pass.

## Deliverables

- Habit form section "Reminders" with "Add reminder", time rows, and "Remove reminder N".
- Reminder times shown on the Habits-page card.
- Reminder scheduler, notification delivery, banner, persisted fired/pending/snooze state.
- Settings sections "Notifications" (permission status + guidance), "Reminder controls" (pause, quiet hours), "Streak at risk" (hour, extra-reminder switch).
- "Streak at risk" badge on Today cards.
- Documented test-only hooks (in README and in this contract). They exist in both `npm run dev` and `npm run preview`:
  - `window.__cadenceNotifications`: array, reset on every page load, one entry per system notification the app created. Entry fields: `title`, `body`, `tag`, `habitName`, `kind` (`"reminder"` or `"streak-at-risk"`), `dueTimes` (array of "HH:mm"; for streak-at-risk the at-risk hour as "HH:00"), `firedAt` (app-time ISO string). An entry is pushed only after the notification was created successfully.
  - `window.__cadenceTest.setNow("YYYY-MM-DDTHH:mm")` (optional `:ss`): in `?now=` mode, replaces the pinned now (forward or backward), re-renders every page with the new date, and runs one scheduler evaluation (whether the page is visible or hidden, see amended rule R14).
  - `window.__cadenceTest.advanceMinutes(n)`: same as `setNow` with now plus n minutes.
  - `window.__cadenceTest.clickNotification(i)`: runs exactly the handler that a click on `window.__cadenceNotifications[i]` runs.
- README section documenting the hooks, the evaluation triggers, and how tests stub permission.

## Exact labels and identifiers

| Thing | Identifier |
|---|---|
| Form section | heading "Reminders" |
| Add button | button "Add reminder" (disabled at 5 rows) |
| Time row | `input type=time` labelled "Reminder time 1", "Reminder time 2", ... |
| Remove row | button "Remove reminder 1", ... |
| Habits card reminders line | `data-testid="habit-reminders"`, text "Reminders: 09:00, 18:00" (24-hour, ascending). Absent when none. |
| Banner | `data-testid="reminder-banner"`, `role=region`, name "Due reminders". Absent from the DOM when it has no visible entries. |
| Banner title | `data-testid="reminder-banner-title"`: "1 reminder due" or "N reminders due" |
| Banner entry | `data-testid="reminder-banner-item"`: emoji, habit name, "Due HH:mm", and the tag "Streak at risk" when applicable |
| Entry buttons | "Mark done: <name>", "Snooze 10 min: <name>", "Dismiss: <name>" |
| Permission status | `data-testid="notification-permission"`, text exactly "Granted", "Denied", "Not asked", or "Unsupported" (with an icon) |
| Guidance | `data-testid="notification-guidance"` (texts below) |
| Pause | checkbox "Pause all reminders" |
| Pause notice | `data-testid="paused-notice"` on Today, text "All reminders are paused." Absent when not paused. |
| Quiet hours | checkbox "Enable quiet hours"; time inputs "Quiet hours start" (default 22:00), "Quiet hours end" (default 07:00); disabled until the checkbox is on |
| At-risk hour | select "Streak at risk hour", options "00:00" to "23:00", default "20:00" |
| At-risk reminder switch | checkbox "Streak-at-risk reminder", default checked |
| Badge | `data-testid="streak-at-risk-badge"`, text "Streak at risk", amber outline plus icon |
| Highlighted card | `data-highlighted="true"` on the Today `article` |

Guidance texts (exact):
- Not asked: "Cadence will ask for permission when you add your first reminder."
- Granted: "Reminders appear as browser notifications while Cadence is open."
- Denied: "Notifications are blocked in your browser settings. Reminders appear as an in-app banner instead. To change this, allow notifications for this site in your browser's site settings."
- Unsupported: "This browser does not support notifications. Reminders appear as an in-app banner instead."

Form error texts (exact, `role=alert`): "Each reminder time must be different." and "Enter a time for every reminder." and in Settings "Quiet hours start and end must be different."

Notification content (exact):
- Regular: title `Reminder: <name>`, body `Due at <latest due HH:mm>`.
- Streak at risk (alone or merged): title `Streak at risk: <name>`, body `Your <N>-day streak ends today unless you check in.`

## Behavior rules (tie-breaks and edge cases)

All times are the user's local time. "Now" is the app clock (the `?now=` value, or `new Date()` otherwise).

- R1 Due: a reminder time T on date D is due when now >= T on D (inclusive).
- R2 Eligible at evaluation: the habit is active (not archived, not deleted), D is on or after its start date, the habit is scheduled on D (schedule in force on D), it has no done check-in and no excused skip for D, reminders are not paused, neither T nor now is inside quiet hours, and T is later than the moment that reminder time was added to the habit (a time added or edited at 10:00 for 09:00 is not delivered that day; editing other fields keeps the original added moment).
- R3 Consumed: a due time that is evaluated as not eligible is consumed. It never fires later that day, even if the habit is then unchecked, the pause is lifted, or quiet hours end.
- R4 Quiet hours: start inclusive, end exclusive, may wrap midnight (22:00 to 07:00). Start equals end is rejected.
- R5 At most once: each (habit, date, time) delivers at most once, across reloads, new loads with a different `?now=`, and two tabs in the same browser profile. Removing and re-adding the same time does not re-fire it that day.
- R6 One delivery per habit per evaluation: all newly due times for one habit (and the streak-at-risk reminder, if also due) are merged into one notification or one banner entry. Every merged time is marked delivered.
- R7 Delivery channel is read at delivery time: permission "granted" and notification created successfully means a system notification and no banner entry. Any other case (denied, not asked, unsupported, or the notification constructor throws) means a banner entry. Nothing is dropped silently.
- R8 Banner: one entry per habit, ordered as on the Habits page. A new delivery for a habit already in the banner updates its entry and brings it back if it was snoozed or dismissed.
- R9 Banner persistence: pending entries survive reload and are shown once (not duplicated), without creating any notification. Dismissed entries never return. An entry disappears when its habit is completed (anywhere), skipped, archived, deleted, or when the local date changes.
- R10 Mark done checks the habit in for today exactly like the Today check (Undo toast, milestone toast, progress update) and removes the entry.
- R11 Snooze: hides the entry until click time plus 10 minutes (reappears at exactly +10:00 in `?now=` mode, and within 30 seconds of app time after +10:00 with the real clock). Snooze is persisted across reload. The reappearance is not a new fire. If paused or quiet at that moment, the entry stays hidden and reappears when the block ends the same day. If the date has changed or the habit is done, it is removed.
- R12 Catch-up: on every evaluation, all due times of today not yet delivered or consumed are processed under R2 to R7. Yesterday's times are never delivered. This includes page load (a time that came due while the app was closed is delivered once on load if still eligible).
- R13 Evaluation triggers: page load (after data loads), at least every 15 seconds of app time using the real clock, whenever the page becomes visible or focused, after `setNow` or `advanceMinutes`, and after any habit, check-in, or settings change.
- R14 (amended by orchestrator) Hidden pages still deliver. While `document.visibilityState` is "hidden" the scheduler keeps evaluating whenever its timers run (browsers may throttle them), and a due reminder is delivered then: a system notification when permission is granted, otherwise a banner entry the user sees on return. Because hidden-tab timers can be throttled or frozen (sleep), the app also runs an evaluation on every `visibilitychange` to "visible"; that evaluation is the catch-up (R12) for anything not yet delivered. Dedupe (R8 and the per-time-per-day rule) guarantees the visible-again evaluation never repeats a reminder already delivered while hidden.
- R15 Permission: the browser permission prompt is requested only when the user clicks "Add reminder" and permission is currently not asked. Never on load, never from Settings, never when saving a habit without reminders. After a granted or denied result it is not asked again. Settings status reads the live permission and updates when the page becomes visible or focused.
- R16 Form: first new row defaults to 09:00; later rows default to the first of 09:00, 12:00, 15:00, 18:00, 21:00 not already in the form. Maximum 5 rows. Duplicate or empty times show an inline error on Save and nothing is saved. Times are stored and shown sorted ascending. Cancel changes nothing.
- R17 Streak at risk, badge: shown on a Today card when all hold: habit active and scheduled today, not done and not excused-skipped today, the current streak (as shown on the card) is 3 or more, and now is at or after the configured at-risk hour. Independent of pause, quiet hours, permission, or reminders. It disappears at once when the habit is checked in.
- R18 Streak at risk, extra reminder: when the badge condition holds and "Streak-at-risk reminder" is on, it is delivered once per habit per day through R2 to R8 (pause and quiet hours suppress and consume it; it needs no per-habit reminder times). If the app first evaluates after the at-risk hour, it is still delivered once, subject to R2 to R7.
- R19 Notification click: runs the click handler: focuses the window, navigates to the Today page, scrolls the habit's card into view, sets `data-highlighted="true"` on it (until the route changes or 5 seconds of app time pass), and moves keyboard focus to its "Check in <name>" button. If the habit is no longer shown, Today opens with no highlight and no error.
- R20 Deleting or archiving a habit removes its pending banner entries; deleting also removes its delivery records.

## Pass/Fail Criteria

### Functionality (PASS threshold: all core flows work)

- [ ] F1 Reminder times: the form supports adding, editing, and removing reminder rows per R16, persists after reload, prefills on Edit, and the Habits card shows "Reminders: 07:00, 19:30". Zero reminders is valid and shows no reminders line.
- [ ] F2 Granted: daily habit "Water" with a 09:00 reminder, permission granted, now moves from 08:59 to 09:00 on Wednesday 2026-03-04: exactly one entry in `window.__cadenceNotifications` (kind "reminder", title "Reminder: Water", body "Due at 09:00"), no banner, still exactly one at 09:30 and 12:00.
- [ ] F3 Denied: same scenario with permission denied shows the banner naming "Water" ("1 reminder due", "Due 09:00") and creates no system notification. "Mark done: Water" checks Water in on Today and removes the banner from the DOM.
- [ ] F4 Snooze: "Snooze 10 min: Water" hides the entry (banner leaves the DOM) at 09:00, still hidden at 09:09, back at 09:10, and the hidden state persists across a reload at 09:05.
- [ ] F5 Dismiss: "Dismiss: Water" removes the entry; it does not return on reload or at later times that day.
- [ ] F6 Stacking: two habits due at 09:00 produce one banner ("2 reminders due") with two entries in Habits-page order. With permission granted they produce two notifications, one per habit.
- [ ] F7 No fire: no delivery on an unscheduled day, for a completed habit (also not after unchecking later), for an excused-skipped day, while paused (also not after unpausing), during quiet hours (start inclusive, end exclusive, midnight wrap), for an archived habit, or for a habit whose start date is in the future.
- [ ] F8 Dedupe: after a delivery at 09:00, a fresh load of the app at 09:05 and at 18:00 creates no new notification and no duplicate banner entry. Editing the habit name or removing and re-adding the 09:00 row does not re-fire it. Two tabs open on the same data produce a total of one notification.
- [ ] F9 Permission timing: first load, visiting every page, creating a habit without reminders, and opening Settings cause zero permission requests. The first "Add reminder" click causes exactly one request. A later "Add reminder" click after a granted or denied result causes no further request.
- [ ] F10 Settings: the status shows "Granted", "Denied", "Not asked", or "Unsupported" with the exact guidance text; the status never says "Not asked" after permission is granted.
- [ ] F11 Hidden tab and catch-up: with the tab hidden from 08:00 and now set to 09:30, exactly one delivery for the 09:00 reminder occurs while still hidden, and becoming visible does not add a second one. With reminders 09:00 and 12:00 and now set to 13:00 while hidden, becoming visible produces exactly one notification with `dueTimes` ["09:00","12:00"]. A sleep across midnight delivers nothing from the previous day. A sleep ending inside quiet hours delivers nothing and consumes the reminders.
- [ ] F12 Real timers: with the Playwright clock installed at 08:00 (no `?now=`), running the clock to 09:05 delivers the 09:00 reminder once; a clock fast-forward of 2.5 hours (08:00 to 10:30) with reminders 09:00 and 10:00 delivers exactly one notification with `dueTimes` ["09:00","10:00"].
- [ ] F13 Notification click: `clickNotification(0)` from the Habits page leads to Today with that habit's card `data-highlighted="true"` and the "Check in <name>" button focused.
- [ ] F14 Pause and quiet hours controls persist across reload, show/hide the "All reminders are paused." notice, and reject equal start and end with the exact error leaving saved values unchanged.
- [ ] F15 Streak at risk: habit "Read" (daily, start 2026-03-01, done 03-01, 03-02, 03-03) on Wednesday 2026-03-04 shows no badge at 19:59 and the "Streak at risk" badge at 20:00; checking in removes it. With permission granted exactly one entry (kind "streak-at-risk", title "Streak at risk: Read", body "Your 3-day streak ends today unless you check in.") appears at 20:00 and none after a fresh load at 20:30; denied shows a banner entry tagged "Streak at risk".
- [ ] F16 Badge exclusions: no badge for a streak of 2, for an unscheduled day, for an excused-skipped day, or after the habit is done. Mon/Wed/Fri habit "Gym" (start 2026-02-25, done 02-25, 02-27, 03-02) shows the badge Wednesday 03-04 at 20:00 and none on Thursday 03-05 at 21:00 (even with "Show unscheduled habits" on).
- [ ] F17 At-risk settings: setting "Streak at risk hour" to "18:00" moves the badge and the extra reminder to 18:00 and persists after reload; switching "Streak-at-risk reminder" off keeps the badge but creates no notification or entry; pause or quiet hours covering the hour keep the badge but suppress the reminder. A regular 20:00 reminder plus at-risk at 20:00 merges into one "Streak at risk: Read" notification (R6).

### Product Depth (PASS threshold: at least 3 meaningful interactions)

- [ ] D1 A user can add a reminder, accept the permission prompt, be notified, click the notification, land on the highlighted card, and check the habit in, all in one flow.
- [ ] D2 A denied-permission user can run a full day: banner entry appears, snooze, reappear, Mark done, and Undo toast works, with progress and streak updating on Today.
- [ ] D3 Editing a reminder time after the old time fired schedules only the new time (09:00 changed to 09:30 at 09:10 fires once at 09:30), and a time added after it has already passed that day is not delivered until the next scheduled day.
- [ ] D4 Settings changes (pause, quiet hours, at-risk hour) take effect on the next evaluation without a reload.

### Visual Design (PASS threshold: no placeholder UI, consistent styling)

- [ ] V1 The banner sits at the top of the content, above page content on every route, with the Cadence card style (12 px corners, soft shadow, warm canvas), slides down in 150 to 250 ms, and uses a fade under reduced motion. No horizontal scroll at 375 px and the bottom nav stays visible and unobstructed.
- [ ] V2 Banner buttons are visible text buttons (not icon-only), at least 40 px tall, readable in light and dark with AA contrast.
- [ ] V3 The "Streak at risk" badge uses an amber outline plus an icon and the text; status is never color alone. The permission status has an icon and text.
- [ ] V4 The Reminders form section, Settings sections, and the Habits-card reminders line match the existing form and card styling in both themes (checked with screenshots at 1280 px and 375 px).

### Code Quality (PASS threshold: no critical errors, no stubs)

- [ ] C1 `npm run build`, `npm test`, and `npm run test:e2e` pass on dev and preview, including all Sprint 1 and 2 tests.
- [ ] C2 No console errors and no non-local network requests in any new flow (the existing automatic fixture applies).
- [ ] C3 The due-time, eligibility, quiet-hours (including midnight wrap and boundaries), merge, dedupe-key, snooze, and at-risk rules are pure logic with unit tests for R1 to R6, R11, R12, R17, and R18.
- [ ] C4 No stubs: delivery uses the real browser notification API, banner and fired state are persisted, and the test hooks only observe or move time and never bypass the scheduler.
- [ ] C5 Reminder data lives in the stored habits and settings (schema stays loadable from Sprint 1 and 2 data with no reminders).

## Test Method

Create `e2e/reminders.spec.ts` (plus unit tests). Every test uses a fresh browser context (clean storage) and these settings: `timezoneId: "UTC"`, `locale: "en-US"`, viewport 1280x800 (375x812 for V1 and V4 phone checks). The base URL is the dev or preview server of the existing config. Reference dates: Wednesday 2026-03-04, Thursday 2026-03-05, Monday 2026-03-02.

### Permission control (headless Chromium)

- Real grant: `browser.newContext({ permissions: ["notifications"] })`, which makes the real `Notification.permission` "granted" (one test, F2 variant, plus F10 "Granted" check). Real deny: a context with no grant; headless Chromium reports "denied" (or "default"), and both must produce the banner.
- Deterministic states: `context.addInitScript` installs a stand-in `Notification` constructor with a static `permission` getter set to "granted", "denied", or "default", a `requestPermission()` that increments `window.__permissionRequests` and resolves to a configured value, and (for "unsupported") `delete window.Notification`. The app must read `Notification.permission` and call `Notification.requestPermission()` at call time (never cached at load), and detect support with `"Notification" in window` at call time. Tests assert system notifications only through `window.__cadenceNotifications`, never through the stand-in.
- Not asked maps to "default" and shows "Not asked".

### Time control

- Pinned mode (default): `page.goto("/?now=2026-03-04T08:00#/habits")`, create habits through the UI (reminder rows are created at 08:00), then `page.evaluate(() => window.__cadenceTest.setNow("2026-03-04T09:00"))` and `advanceMinutes(n)`. A "fresh load" is `page.goto("/?now=2026-03-04T09:05#/today")` (stored data is kept). Counters are checked with `page.evaluate(() => window.__cadenceNotifications.length)`.
- Real-clock mode (F12 only): `page.clock.install({ time: new Date("2026-03-04T08:00:00Z") })` before `page.goto("/")` (no `?now=`), then `page.clock.runFor("01:05:00")` and `page.clock.fastForward("02:30:00")`.
- Hidden tab: `page.evaluate` sets `Object.defineProperty(document, "visibilityState", { value: "hidden", configurable: true })` and `hidden: true`, then dispatches `new Event("visibilitychange")` on `document`; showing is the same with "visible" and `false`.
- Two tabs (F8): `context.newPage()` twice, same `?now=` URL, call `setNow("2026-03-04T09:00")` on both, expect the sum of both pages' `__cadenceNotifications` lengths to be 1; with permission denied each page shows exactly one entry after its next evaluation.

### Scenarios

1. F1: habits page, New habit "Water", click "Add reminder" (row 1 shows 09:00), click again (row 2 shows 12:00), set row 2 to 18:30, add a third row set to 09:00, Save: error "Each reminder time must be different." and no habit created; change it to 07:00, Save: card shows "Reminders: 07:00, 09:00, 18:30". Reload, Edit: three rows prefilled. Remove all rows, Save: no `habit-reminders`. Click "Add reminder" five times: the button is disabled. Clear a time input and Save: "Enter a time for every reminder.". Cancel leaves the habit unchanged.
2. F2: "Water", daily, reminder 09:00, granted. setNow 08:59: length 0. setNow 09:00: length 1 with the exact title/body/kind, `reminder-banner` count 0. setNow 09:30 and 12:00: length 1.
3. F3: same, denied. At 09:00 banner shows "1 reminder due", an item containing "Water" and "Due 09:00", `__cadenceNotifications` length 0. Click "Mark done: Water": banner count 0; Today shows "Check in Water" `aria-pressed=true` and "1 of 1 done"; Undo toast visible.
4. F4: denied; at 09:00 click "Snooze 10 min: Water": banner count 0. setNow 09:09: count 0. `page.goto` with `?now=2026-03-04T09:05`: count 0. setNow 09:10: banner with Water, `__cadenceNotifications` length 0. Real-clock variant: reappears after `runFor("10:30")`, hidden after `runFor("09:30")`.
5. F5: denied; at 09:00 "Dismiss: Water", reload at 09:05, setNow 12:00: count 0.
6. F6: "Water" and "Stretch" both daily with 09:00; denied: one `reminder-banner`, title "2 reminders due", two items in Habits-page order. Granted: two notifications with different `habitName`.
7. F7 (one test per case): (a) "Run" scheduled Tue only, reminder 09:00, now Wednesday: advance to 09:30, nothing. (b) check Water at 08:30, advance to 09:05, nothing; uncheck at 09:30, advance to 09:35, nothing. (c) Skip Water today (excused), nothing. (d) Settings "Pause all reminders" on, advance to 09:05 nothing, fresh load at 09:20 nothing, unpause at 09:30 nothing for 09:00; with an extra 18:00 reminder, setNow 18:00 delivers it. (e) Quiet hours 22:00 to 07:00 enabled, created at 05:00 with reminders 06:59, 07:00, 22:00: setNow 06:59 nothing, 07:00 length 1 (due "07:00"), 22:00 length stays 1. (f) archived habit with reminder 09:00: nothing. (g) habit with start date 2026-03-05 and reminder 09:00, now 2026-03-04: nothing. (h) delete a habit with a pending banner entry: entry removed, no console error.
8. F8: granted, fire at 09:00; fresh loads at 09:05 and 18:00 produce length 0 on the new page and no banner; edit name at 09:10 and advance: no re-fire; remove and re-add the 09:00 row at 09:12: no re-fire. Denied variant: after reload at 09:05 the banner shows exactly one entry. Two-tab check as above.
9. F9: stand-in with "default" permission and request counter: after `goto`, navigate all five routes, create habit "Plain" without reminders, open Settings: `__permissionRequests` is 0. New habit, click "Add reminder": 1. Click again: still 1 if the stand-in resolved "granted" or "denied". With the stand-in resolving "default" (prompt dismissed), reminders still produce the banner.
10. F10: for each state (stand-ins plus real grant) open `#/settings`: `notification-permission` text and `notification-guidance` text match the table above exactly.
11. F11: granted, "Water" at 09:00, created 08:00. Hide the tab, setNow 09:30: length 1 while hidden. Show: length 1; dispatch visible again: length 1. Denied variant: same steps; while hidden the banner entry for Water exists in the DOM (no system notification); show: the banner is visible with exactly one Water entry. Catch-up variant (frozen timers): reminders 09:00 and 12:00, hide, then use `page.clock` (or mark the scheduler suspended via the documented test hook) so no evaluation runs while hidden, advance to 13:00, show: length 1 and `dueTimes` ["09:00","12:00"]; the implementation must document in its handoff how this variant suspends hidden evaluation. Third: hide at 08:00, setNow 2026-03-05T07:00, show: length 0; setNow 2026-03-05T09:00: length 1. Fourth: quiet hours on, hide, setNow 23:00, show: length 0, setNow next day 09:00: length 1.
12. F12 as in the criterion.
13. F13: granted; on `#/habits`, setNow 09:00; `clickNotification(0)`; expect hash `#/today`, the `article` named "Water" has `data-highlighted="true"`, and `document.activeElement` is the "Check in Water" button; navigate away and back: no highlight.
14. F14: Settings: toggle pause (notice appears on Today), enable quiet hours, set start and end both 22:00: error and previous values kept; reload keeps saved values.
15. F15 and F16: seed with the History dialog (Sprint 2) using the `history-row` `data-date` rows. Pinned at 2026-03-04T19:59 then setNow 20:00. Capture `streak-current` equal to 3 before and after. Gym scenario as in the criterion.
16. F17: Settings select "18:00": badge at 18:00 and not at 17:59; reload keeps 18:00. Switch off the reminder: badge present, length 0, no banner (denied). Pause or quiet hours: badge present, length 0. Merge case: "Read" with its own 20:00 reminder: length 1, title "Streak at risk: Read".
17. D1 to D4: composite flows as described, reusing F-scenario helpers.
18. V1 to V4: full-page screenshots reviewed by the evaluator for banner (1 and 2 entries), badge, Settings, and form, in light and dark at 1280 px and 375 px. Run the banner once with `reducedMotion: "reduce"` and confirm no slide.
19. C1 to C5: run `npm run build`, `npm test`, `npm run test:e2e`; read the console and request logs; read the README for the hooks.

## Out of scope

Calendar, heatmap, activity log, export/import, week start, quick add, smart reminder timing suggestions, weekly insights, and schedule-fit suggestions (Sprint 4).


## Orchestrator amendment (post-ratification)

R14, F11 and the F11 test step were amended after ratification. Reason: the original rule suppressed all delivery while the tab was hidden, which defeats the main purpose of system notifications (an open app in a background tab). The spec requires catch-up for reminders missed while hidden or asleep; it does not forbid delivering while hidden. The amended rule delivers while hidden when timers run, and keeps catch-up on becoming visible for throttled or frozen timers. Quiet-hours behaviour (consume) is unchanged.
