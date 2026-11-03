APPROVED

# Sprint 2 Contract

## Scope

Sprint 2 of the spec: "Check-ins, Schedule-Aware Streaks, and Statistics". Every Sprint 2 deliverable is listed here.

1. Today view check-ins: scheduled habits grouped by time of day, a "Show unscheduled habits" toggle, one-tap check and uncheck, an Undo toast, a daily progress count and ring, and a full-day celebration.
2. Check-in notes and excused skip days.
3. Backfill of past dates, with future dates locked.
4. Streak engine: current streak and longest streak over scheduled days only, with these rules:
   - Today stays pending until the day ends.
   - Bonus completions never change a streak.
   - Excused skips are passed over.
   - Schedule changes apply from today forward.
   - Nothing counts before the start date.
5. Statistics: 7-day, 30-day, and all-time completion rates; total completions; a dashboard summary.
6. Milestone badges (3, 7, 14, 30, 60, 100, 365) and the milestone toast.

Out of scope (later sprints): reminders, the streak-at-risk badge, the month calendar, heatmap, activity log, export/import, week-start setting, and the intelligence features.

## Deliverables

### UI surfaces, labels and test identifiers

All dates below are local calendar days. "ISO date" means YYYY-MM-DD. The `?now=` override from Sprint 1 keeps working and is the only way tests move time.

**Today page (`#/today`)**
- Each listed habit is an `article` named by the habit name. It shows a large check button, the current streak, the longest streak, and the schedule label.
  - The check button has the accessible name `Check in <habit name>` and `aria-pressed` true or false. Its name does not change with state.
  - When checked, the button shows a checkmark icon and the visible word "Done". State is not shown by color alone.
  - The button is at least 44 x 44 px.
- Streak hooks: `data-testid="streak-current"` and `data-testid="streak-longest"` each contain only the number, for example `3`. Visible labels read "Current streak" and "Longest streak".
- Progress text: `data-testid="today-progress"` reads exactly `<done> of <total> done`, for example `3 of 5 done`.
  - `total` counts habits scheduled today that are not skipped.
  - `done` counts those that are checked.
  - Bonus check-ins and skipped habits are in neither number.
  - Progress ring: an element with `role="progressbar"` and the accessible name "Daily progress", with `aria-valuenow` = done and `aria-valuemax` = total.
  - When total is 0 the text is `0 of 0 done` and there is no celebration.
- Celebration: when done = total and total >= 1, the progress area shows the text "All done for today".
  - The text appears as soon as the last habit is checked. It stays while the state holds, including after a reload, and disappears if a habit is unchecked.
  - Right after the checking action only, a decorative burst (`data-testid="confetti"`, `aria-hidden`) shows for about 2 seconds. It is not shown after a reload.
  - With `prefers-reduced-motion: reduce`, the burst is never rendered and the text still appears with a simple fade.
- Undo toast: after every check or uncheck on Today, a toast with `role="status"` appears.
  - Its text is `Checked <habit name>` or `Unchecked <habit name>`, and it has a button named "Undo".
  - One Undo toast shows at a time; a new action replaces it.
  - It disappears on its own after about 6 seconds.
  - Clicking "Undo" restores the exact prior state (including the note and skip state) and removes the toast.
- Note: a checked item shows a button `Add note for <habit name>`.
  - It opens an inline text area labeled `Note for <habit name>` (max 200 characters) with buttons "Save note" and "Cancel".
  - After saving, the note text shows on the item and the button is renamed `Edit note for <habit name>`.
  - Saving an empty note clears it.
  - Unchecking a habit deletes its check-in and note, and Undo restores both.
  - An unchecked item has no note button.
- Skip: an unchecked, scheduled item shows a button `Skip <habit name> today`.
  - After skipping, the item shows a "Skipped (excused)" badge with an icon, the button becomes `Clear skip for <habit name>`, and the habit leaves the progress numbers.
  - Checking a skipped habit clears the skip and checks it.
  - A checked habit has no skip button.
  - An unscheduled item (visible through the toggle) has no skip button.
- Bonus: with "Show unscheduled habits" on, an unscheduled item shows "Not scheduled today" and a working check button.
  - Once checked, it also shows a "Bonus" badge with an icon.
  - A bonus check never changes `today-progress` or any streak.
- Milestone toast: when a check on Today raises the current streak so that a milestone M satisfies previous streak < M <= new streak, a toast with `role="status"` appears with the text `Milestone reached: <M>-day streak on <habit name>`.
  - If several milestones are crossed, only the highest is announced.
  - It stacks with, and does not replace, the Undo toast.
  - It is shown only for Today checks, not backfill.

**Habits page (`#/habits`), on each active habit card**
- Streak hooks as above: `streak-current` and `streak-longest`.
- A stats region with these hooks. Each hook contains only the value, with a visible label:
  - `rate-7d` ("7-day rate")
  - `rate-30d` ("30-day rate")
  - `rate-all` ("All-time rate")
  - `total-completions` ("Total completions")
  - Rates show an integer percent such as `71%`, or `N/A` when the window has no evaluated scheduled days.
- Milestone badges: one badge for each milestone <= the habit's longest streak, with the accessible name `Milestone: <M>-day streak`. They are derived from current data, so unchecking can remove a badge. No badge is shown for milestones not reached.
- A button `History for <habit name>` that opens the History dialog.

**History dialog**
- It is `role="dialog"` named `History: <habit name>`, with a "Close" button.
- It contains a day list, newest first, starting with today and covering 14 days (or fewer if the start date comes sooner).
  - Days before the start date are never listed.
  - A button "Show 14 more days" extends the list. It is absent once the start date is reached.
- Each row has `data-testid="history-row"` and `data-date="<ISO date>"`, plus the human date and a status text in `data-testid="history-status"`. The status is one of:
  - "Done"
  - "Missed"
  - "Pending" (today, scheduled, unchecked)
  - "Skipped (excused)"
  - "Not scheduled"
  - "Bonus"
- Each row has these buttons:
  - `Check in <habit name> on <ISO date>` (`aria-pressed`)
  - `Skip <habit name> on <ISO date>` (`aria-pressed` true when skipped; disabled on checked days and on unscheduled days)
  - `Note for <habit name> on <ISO date>` (disabled unless the day is checked; opens the same inline note editor)
- A date field labeled "Jump to date" has min = start date and max = today. Entering a valid date in range shows one row, with the same controls and hooks, in a "Selected date" area.
  - A future date shows an alert "Future dates can't be edited" and no row.
  - A date before the start date shows an alert "Before this habit's start date" and no row.
- Checking a skipped row clears the skip and records a check-in, the same as on Today. The row then reads "Done" and its Skip button is `aria-pressed="false"` and disabled.
- Changes made in the dialog take effect immediately in all streak and stat numbers on the page behind it. They persist across reload. They do not show an Undo toast. Clicking the control again reverses them.

**Insights page (`#/insights`), "Dashboard" section** (replaces the placeholder; other Insights content stays out of scope)
- It covers active habits only.
- `dash-best-streak` holds the highest current streak among active habits, and `dash-best-streak-habit` holds that habit's name. With no habits or all streaks at 0, they show `0` and `None`.
  - Tie-break: when several habits share the highest current streak, `dash-best-streak-habit` shows the first of them in Habits-page order (the user's reorder sequence).
- `dash-week-rate` is the pooled 7-day completion rate: the sum of completed scheduled days over the sum of evaluated scheduled days, across all active habits, as an integer percent, or `N/A`.
- An empty app (no habits) shows a friendly empty message instead of numbers.

### Precise definitions (these are the contract; the evaluator should test against them)

- **Scheduled day**: a day on or after the start date whose weekday is in the schedule in effect on that day.
  - Edits apply from the day of the edit onward, including that day.
  - Earlier days keep the schedule they had when they occurred.
  - Days before the start date are neither scheduled nor listed.
- **Day outcomes**: a scheduled day is Done (checked), Skipped (excused), Pending (today only, unchecked and not skipped), or Missed (a past day, unchecked and not skipped). An unscheduled day is Not scheduled, or Bonus if checked.
- **Current streak**: walk back from today over scheduled days. Pending today is ignored; if today is Done it counts. Done adds 1. Skipped is passed over (adds 0, does not stop the walk). Missed stops the walk. Unscheduled days and Bonus days are invisible to the walk. Nothing before the start date counts.
- **Longest streak**: the maximum value the same walk yields for any run in the habit's history. Pending today does not end a run. It is always >= the current streak.
- **Completion rate** over a window (the last 7 or 30 calendar days ending today, or start date through today):
  - Rate = Done scheduled days / evaluated scheduled days, rounded to the nearest whole percent (half rounds up).
  - Evaluated scheduled days are scheduled days in the window and on or after the start date, excluding Skipped days and excluding Pending today.
  - Bonus check-ins are not in the numerator or denominator.
  - If there are no evaluated days the value is `N/A`.
- **Total completions**: the count of all check-ins for the habit, including Bonus.
- **Delete**: deleting a habit removes its check-ins, notes, and skips. A habit later created with the same name starts with no history. **Archive** keeps all history, and Restore brings the same streaks and stats back.

### Shared fixtures used by the test method

All habits are created on the Habits page with the Sprint 1 form (Name, Start date, weekday buttons). Past check-ins are entered through the History dialog. Dates are in March 2026; 2026-03-02 is a Monday.

- **FX-GYM**: "Gym", Mon/Wed/Fri, start 2026-03-02. Checked on 03-02, 03-04, 03-06.
- **FX-READ**: "Read", every day, start 2026-03-01. Checked on 03-01, 03-02, 03-03, 03-05, 03-07.
  - Missed 03-04 and 03-06.
  - Viewed at `?now=2026-03-07T20:00`.
- **FX-WALK**: "Walk", every day, start 2026-03-01. Checked on 03-01, 03-02, 03-03. Viewed at `?now=2026-03-04T08:00`, with 03-04 unchecked.

## Pass/Fail Criteria

### Functionality (PASS threshold: all core flows work)

Check-ins and Today view
- [ ] F1. Tapping `Check in <habit>` on Today marks the habit Done (`aria-pressed="true"`, visible "Done"), and `today-progress` updates immediately (for example `1 of 3 done`). Tapping again unchecks it and restores the previous progress text.
- [ ] F2. Check and uncheck states persist across a page reload.
- [ ] F3. Undo toast: after a check, an Undo toast `Checked <habit>` appears and "Undo" restores the unchecked state. After an uncheck, the toast `Unchecked <habit>` appears and "Undo" restores the checked state, including its note. The toast disappears by itself within 10 seconds. The outcome of Undo persists across reload.
- [ ] F4. Today lists only habits scheduled today, grouped Morning / Afternoon / Evening / Anytime (empty groups hidden). The "Show unscheduled habits" toggle adds unscheduled habits with "Not scheduled today". Archived habits and habits whose start date is after today never appear.
- [ ] F5. Progress and celebration: `today-progress` and the ring (`aria-valuenow`, `aria-valuemax`) match the scheduled, non-skipped counts. Checking the last one shows "All done for today" and the burst; unchecking one hides the text. After a reload with all done, the text shows and the burst does not. With reduced motion emulated, the burst never renders.
- [ ] F6. Notes: a note saved on a checked habit shows on Today, the button changes to `Edit note for <habit>`, and the note persists across reload. A note can be edited and cleared. Unchecking removes the note, and Undo brings it back. The text area refuses input beyond 200 characters.
- [ ] F7. Skip: skipping a scheduled, unchecked habit shows "Skipped (excused)", removes it from the progress numbers, and persists across reload. "Clear skip" returns it to Pending. Checking a skipped habit replaces the skip with a check-in. A checked habit cannot be skipped. An unscheduled habit has no skip button.
- [ ] F8. Backfill: in the History dialog, `Check in <habit> on <ISO date>` toggles any listed past day and any day reached through "Jump to date" (back to the start date), and updates row status, streaks, and stats immediately. Past notes and skips can be set and cleared. Checking a skipped row clears the skip and checks the day. "Show 14 more days" reveals older days up to the start date and then disappears. Days before the start date are never listed. Everything persists across reload.
- [ ] F9. Future dates are locked: "Jump to date" with a date after today shows "Future dates can't be edited" and no controls. The date field's max equals today. Today and the History list expose no way to check in a future date. A date before the start date shows "Before this habit's start date" and no controls.

Streak engine (all numbers below are exact; they use the fixtures above)
- [ ] S1. FX-GYM, viewed at `?now=2026-03-07T10:00` (Saturday), shows `streak-current` = 3 and `streak-longest` = 3. At `?now=2026-03-08T10:00` (Sunday) it still shows 3. At `?now=2026-03-09T08:00` (Monday, unchecked) it shows 3. After checking Monday on Today it shows 4.
- [ ] S2. Missed Wednesday: a Mon/Wed/Fri habit "Run", start 2026-02-23, checked on 02-23, 02-25, 02-27, 03-02 and not on 03-04.
  - At `?now=2026-03-04T21:00` (Wednesday evening, unchecked) the current streak is 4 and the longest is 4.
  - At `?now=2026-03-05T09:00` the current streak is 0 and the longest is still 4.
  - At `?now=2026-03-06T09:00`, after checking Friday on Today, the current streak is 1 and the longest is 4.
- [ ] S3. Pending today does not reset: FX-WALK at `?now=2026-03-04T08:00` shows current = 3 (yesterday's value) and its History row for 03-04 says "Pending". Checking it gives 4. Unchecking it gives 3 again.
- [ ] S4. Bonus: with FX-GYM at `?now=2026-03-07T10:00` (current = 3), checking Tuesday 03-03 in History marks the row "Bonus". `streak-current` and `streak-longest` stay 3, and `total-completions` goes from 3 to 4. `rate-7d` stays 100%.
  - On Today at the same time (Saturday), with the toggle on, the Gym item shows "Not scheduled today". Checking it shows "Bonus", the streak stays 3, and `today-progress` does not change.
- [ ] S5. Excused skip: a daily habit "Stretch" with start 2026-03-01 is checked on 03-01, 03-02, 03-04, with 03-03 skipped (excused). At `?now=2026-03-05T09:00` its current streak is 3, not 4, and not 1. Checking 03-05 on Today gives 4. Clearing the skip on 03-03 (leaving it unchecked) changes the current streak to 2 after the 03-05 check.
- [ ] S6. Schedule changes apply from today forward: "Swim", Mon/Wed/Fri, start 2026-03-02, checked on 03-02. At `?now=2026-03-04T09:00`, edit its schedule to Tue/Thu only.
  - History for 03-02 stays "Done", and 03-03 reads "Not scheduled" (not "Missed"), as it was under the old schedule.
  - 03-04 reads "Not scheduled" because it is the edit day.
  - Current streak = 1.
  - At `?now=2026-03-05T09:00` (Thursday, pending) the current streak is still 1. At `?now=2026-03-06T09:00` it is 0, because Thursday was scheduled and missed.
- [ ] S7. Start date: "Late", every day, start 2026-03-05, checked on 03-05, 03-06, 03-07, viewed at `?now=2026-03-07T20:00`. The current streak is 3, `rate-all` is 100%, and `total-completions` is 3. The History list stops at 03-05.
- [ ] S8. The unit test suite for the streak engine passes and covers every rule from S1 to S7: schedule-aware counting, pending today, missed resets current but not longest, bonus ignored, skip passed over, schedule change from today forward, start date. It also covers the rate rules (rounding, skip exclusion, pending-today exclusion, `N/A`) and the milestone thresholds.

Statistics and dashboard
- [ ] T1. FX-READ at `?now=2026-03-07T20:00`: `rate-7d` = `71%`, `rate-30d` = `71%`, `rate-all` = `71%`, `total-completions` = 5, `streak-current` = 1, `streak-longest` = 3. After unchecking 03-07 (today becomes Pending): `rate-7d` = `67%`, `total-completions` = 4, `streak-current` = 0, `streak-longest` = 3.
- [ ] T2. FX-GYM at `?now=2026-03-07T10:00`: `rate-7d` = `100%`, `rate-30d` = `100%`, `rate-all` = `100%`, `total-completions` = 3. Skipped days are excluded: skipping the Wednesday 03-04 instead of checking it makes `rate-7d` 2/2 = `100%` and streaks pass over it.
- [ ] T3. A brand-new habit with no evaluated days (start date today, today unchecked) shows `N/A` for all three rates and `0` for `total-completions`.
- [ ] T4. Insights "Dashboard", with FX-READ and FX-GYM both present at `?now=2026-03-07T20:00`: `dash-best-streak` = 3 and `dash-best-streak-habit` = "Gym". `dash-week-rate` = `80%` (Read 5/7 plus Gym 3/3 = 8/10). An archived habit is excluded from all three values and returns when restored.
- [ ] T5. Delete and archive: archiving FX-READ and restoring it returns the same streaks and stats. Deleting FX-READ (after confirmation) and creating "Read" again with the same start date shows `streak-current` = 0, `total-completions` = 0, and an empty History.

Milestones
- [ ] M1. A daily habit "Plank", start 2026-03-01, checked on 03-01 and 03-02 in History. At `?now=2026-03-03T09:00`, checking it on Today shows the toast `Milestone reached: 3-day streak on Plank` together with the `Checked Plank` Undo toast. Unchecking and checking again shows the milestone toast again.
- [ ] M2. A Today check that raises the streak from 3 to 4 (no milestone crossed) shows no milestone toast. Backfilling checks in History that bring a streak to 3 never shows a milestone toast or an Undo toast.
- [ ] M3. A daily habit "Stretch7", start 2026-03-01, checked on 03-01 through 03-07, viewed at `?now=2026-03-07T20:00`. Its Habits card shows badges `Milestone: 3-day streak` and `Milestone: 7-day streak` and no 14-, 30-, 60-, 100-, or 365-day badge. Unchecking 03-07 (longest becomes 6) removes the 7-day badge and keeps the 3-day badge.

### Product Depth (PASS threshold: at least 3 meaningful interactions)

- [ ] D1. The complete daily loop works in one session. Setup: habits A, B, C (every day, start 2026-03-01, created in that order, no backfill), at `?now=2026-03-04T09:00`.
  - check A, add a note, uncheck A by mistake, Undo;
  - skip B;
  - check C and see the celebration (`2 of 2 done`, "All done for today");
  - reload and see the same state;
  - Today streaks are A = 1, B = 0, C = 1.
  - Insights Dashboard shows `dash-best-streak` = 1, `dash-best-streak-habit` = "A" (tie with C, A is first in Habits-page order), and `dash-week-rate` = `18%` (A 1/4 + B 0/3 + C 1/4 = 2/11; 03-01 to 03-03 are Missed for all three, B's skipped today is excluded, A and C are Done today).
- [ ] D2. A user can fix a forgotten day through History (check in yesterday), see the streak change at once, and see the same value on the Today item, the Habits card, and the Dashboard.
- [ ] D3. Persistence of everything new: checks, notes, skips, and backfilled days all survive a reload. Data created in Sprint 1 (habits, order, archive state) is unaffected.

### Visual Design (PASS threshold: no placeholder UI, consistent styling)

- [ ] V1. The check button is large (at least 44 x 44 px) and fills with the habit's color when checked, with a checkmark and "Done". Done, Skipped, Bonus, Missed, Pending, and Not scheduled statuses are each distinguished by an icon and a text label, never by color alone.
- [ ] V2. The streak number is the visual hero of the item: font size at least 32 px, bold, tabular numerals, with an amber flame icon. The Longest streak is visibly secondary.
- [ ] V3. Missed days use a neutral gray, not red. The progress ring uses the teal-green accent. Milestone badges use amber.
- [ ] V4. Toasts and the celebration are styled consistently with the Sprint 1 cards (rounded corners, soft shadow). In dark mode, text and controls in the new UI stay readable (visually reviewed on screenshots in both themes at desktop and 375 px width, with no clipped text and no horizontal scroll).
- [ ] V5. No "Coming soon" placeholder remains on the Insights page (the Dashboard replaces it). The Calendar and Settings placeholders from Sprint 1 are unchanged.

### Code Quality (PASS threshold: no critical errors, no stubs)

- [ ] C1. `npm run build` (including the type check) succeeds. `npm test` passes, including the new streak-engine and statistics unit tests (S8). `npm run test:e2e` passes for all Sprint 1 and Sprint 2 tests against both dev and preview.
- [ ] C2. No console errors and no failed or non-local network requests occur in any Sprint 2 flow.
- [ ] C3. No stubbed behavior, mock numbers, or TODO placeholders for in-scope features. The streak and rate values come from the stored check-ins.
- [ ] C4. The streak engine is a pure module separate from the UI (no storage or clock reads inside it), so that it can be unit tested directly.

## Test Method

General: each test starts with a clean browser context and uses `page.goto('/?now=<ISO>#/habits')`. Fill the `now` value exactly as written in each criterion. A new `?now` navigation on the same origin keeps the stored data. Use `exact: true` for weekday buttons. Collect `console` errors and `request` hosts in a fixture for every test.

Shared setup helpers (used by many steps):
- `createHabit(name, startISO, days)`: on `#/habits`, click "New habit", fill "Name", fill "Start date", press the weekday buttons exactly (or "Every day"), and submit. Expect an `article` named `name`.
- `backfill(name, [ISO dates])`: on `#/habits`, click `History for <name>`.
  - For each date, if the row exists click `Check in <name> on <date>`.
  - Otherwise click "Show 14 more days" (or fill "Jump to date" with the date) first.
  - Close the dialog.
- `read(name, id)`: return the text of `getByRole('article', {name}).getByTestId(id)`.

1. **F1.** `?now=2026-03-04T09:00#/today`. Create "A", "B", "C" (every day, start 2026-03-01). Expect `today-progress` = `0 of 3 done`. Click `Check in A`. Expect `aria-pressed="true"`, text "Done" in A's article, and `1 of 3 done`. Click `Check in A` again. Expect `0 of 3 done` and `aria-pressed="false"`.
2. **F2.** Check A and B, reload. Expect `2 of 3 done`, A and B pressed. Uncheck B, reload. Expect `1 of 3 done`.
3. **F3.** Click `Check in A`. Expect `role=status` text `Checked A` with a visible "Undo" button. Click "Undo". Expect A unpressed and the toast gone. Reload and expect A unpressed. Check A, add note "ran 5 km" via `Add note for A`, then click `Check in A` to uncheck. Expect toast `Unchecked A`. Click "Undo". Expect A pressed and the note "ran 5 km" back. Reload and verify. Click `Check in B`, wait without clicking, and expect the toast to be gone within 10 s.
4. **F4.** At `?now=2026-03-07T10:00#/habits` create "Gym" (Mon/Wed/Fri, Morning, start 2026-03-01), "Read" (every day, Evening, start 2026-03-01), "Old" (every day, start 2026-03-01), and "Future" (every day, start 2026-03-20). Archive "Old" by clicking the "Archive" button on its card on the Habits page, and expect it to leave the active list. At `?now=2026-03-07T10:00#/today` (Saturday) expect Read under the Evening region only. Gym, Old, and Future do not appear. Expect no Morning region. Tick "Show unscheduled habits" and expect Gym with "Not scheduled today" under Morning. Old and Future still do not appear.
5. **F5.** With A, B, C: check A and B, expect the ring `aria-valuenow="2"` and `aria-valuemax="3"`, and no "All done for today". Check C. Expect "All done for today" and `confetti` visible, then gone within 5 s. Reload. Expect the text and no `confetti`. Uncheck C. Expect the text gone. Emulate `reducedMotion: 'reduce'`, check C again. Expect the text visible and `confetti` count 0 (assert at once and after 500 ms).
6. **F6.** Check A, click `Add note for A`, type 201+ characters and expect the field value length to be 200. Replace with "skipped dessert", click "Save note". Expect the text on the item and the button `Edit note for A`. Reload and expect the note. Edit to "ran 5 km", save. Edit, clear the field, save. Expect no note text and the button `Add note for A`. Uncheck B and expect no note button on B.
7. **F7.** Click `Skip B today`. Expect "Skipped (excused)", the button `Clear skip for B`, and `today-progress` = `0 of 2 done` (A and C scheduled). Reload and expect the same. Click `Clear skip for B`. Expect `0 of 3 done`. Skip B again, then click `Check in B`. Expect the badge gone, B pressed, and `1 of 3 done`. Expect no `Skip B today` button on the checked B. Tick the toggle on a Saturday with an unscheduled Gym and expect no `Skip Gym today`.
8. **F8.** Create FX-READ's habit with start 2026-01-01. At `?now=2026-03-07T20:00#/habits`, open `History for Read`. Expect 14 `history-row`s with dates 2026-03-07 down to 2026-02-22 in order. Click `Check in Read on 2026-03-05`. Expect the row status "Done" and the card `total-completions` = 1 (checked behind the dialog after closing). Click "Show 14 more days" and expect 28 rows. Fill "Jump to date" with 2026-01-15, click `Check in Read on 2026-01-15`, and expect `total-completions` = 2. Add a note via `Note for Read on 2026-03-05`. Skip 2026-03-03 and expect "Skipped (excused)". Click `Check in Read on 2026-03-03` and expect the row "Done", the Skip button `aria-pressed="false"` and disabled, and `total-completions` up by 1. Click `Check in Read on 2026-03-03` again to uncheck and expect "Missed". Skip 2026-03-03 again. Clear the note, the skip, and the check on 2026-03-05 in turn. Reload and expect the changes persisted. Repeat "Show 14 more days" until the button disappears and expect the oldest row to be 2026-01-01. Create "Late" with start 2026-03-05 and expect its list to end at 2026-03-05.
9. **F9.** In `History for Read`, fill "Jump to date" with 2026-03-08. Expect the alert "Future dates can't be edited" and no `Check in Read on 2026-03-08`. Confirm the input's `max` attribute is `2026-03-07`. Fill 2025-12-31 and expect "Before this habit's start date" and no row. Confirm no row with `data-date` after 2026-03-07 exists in the list. Confirm Today has no check button for any future date.
10. **S1.** Create FX-GYM and `backfill('Gym', ['2026-03-02','2026-03-04','2026-03-06'])` at `?now=2026-03-07T10:00`. Read `streak-current` and `streak-longest` on the Habits card and expect 3 and 3. Open `?now=2026-03-08T10:00#/today` and expect 3 in the Gym item. Open `?now=2026-03-09T08:00#/today` and expect 3. Click `Check in Gym` and expect 4.
11. **S2.** Create "Run" (Mon/Wed/Fri, start 2026-02-23). At `?now=2026-03-04T21:00` backfill 02-23, 02-25, 02-27, 03-02 (use "Show 14 more days" as needed). Expect current 4, longest 4 on Today. Open `?now=2026-03-05T09:00#/today` with the toggle on or open Habits, and expect current 0 and longest 4. Open `?now=2026-03-06T09:00#/today`, check Run, and expect current 1 and longest 4.
12. **S3.** Create FX-WALK and `backfill('Walk', ['2026-03-01','2026-03-02','2026-03-03'])` at `?now=2026-03-04T08:00`. Expect current 3 on Today and the 03-04 History row "Pending". Click `Check in Walk` and expect 4. Click again and expect 3.
13. **S4.** With FX-GYM at `?now=2026-03-07T10:00`, open History, click `Check in Gym on 2026-03-03`. Expect that row "Bonus", `streak-current` = 3, `streak-longest` = 3, `total-completions` = 4, `rate-7d` = `100%`. On Today, tick the toggle (Saturday, Gym unscheduled with "Not scheduled today"). Click `Check in Gym` and expect the "Bonus" badge, streak 3, and `today-progress` unchanged.
14. **S5.** Create "Stretch" (every day, start 2026-03-01). At `?now=2026-03-05T09:00` backfill 03-01, 03-02, 03-04 and click `Skip Stretch on 2026-03-03`. Expect current 3 on Today. Click `Check in Stretch` and expect 4. In History, click `Skip Stretch on 2026-03-03` again to clear it. Expect the 03-03 row "Missed" and, with 03-04 and 03-05 done, current 2.
15. **S6.** Create "Swim" (Mon/Wed/Fri, start 2026-03-02). At `?now=2026-03-04T09:00` backfill 03-02. Edit Swim: deselect Mon, Wed, Fri, select Tue, Thu, save. Open History and expect 03-02 "Done", 03-03 "Not scheduled", 03-04 "Not scheduled". Expect current 1. Open `?now=2026-03-05T09:00#/today` and expect Swim listed and current 1. Open `?now=2026-03-06T09:00#/habits` and expect current 0, and the 03-05 History row "Missed".
16. **S7.** Create "Late" (every day, start 2026-03-05). At `?now=2026-03-07T20:00` backfill 03-05, 03-06, 03-07. Expect current 3, `rate-all` `100%`, `total-completions` 3, and the last History row dated 2026-03-05.
17. **S8.** Run `npm test`. Inspect the output and the unit test names for coverage of every rule (S1 to S7, rates, milestone thresholds). Expect zero failures.
18. **T1.** Create FX-READ and `backfill` the five dates at `?now=2026-03-07T20:00`. Expect `rate-7d`, `rate-30d`, `rate-all` all `71%`, `total-completions` 5, current 1, longest 3. In History, uncheck 2026-03-07. Expect `rate-7d` = `67%`, `total-completions` = 4, current 0, longest 3.
19. **T2.** With FX-GYM, expect `100%` ×3 and `total-completions` 3. Uncheck 03-04 and click `Skip Gym on 2026-03-04`. Expect `rate-7d` = `100%`, and current streak = 2 (03-02, 03-06, with 03-04 passed over).
20. **T3.** At `?now=2026-03-07T09:00` create "Fresh" (every day, start 2026-03-07) and leave it unchecked. Expect `rate-7d`, `rate-30d`, `rate-all` = `N/A` and `total-completions` = 0.
21. **T4.** With FX-READ and FX-GYM at `?now=2026-03-07T20:00`, open `#/insights`. Expect `dash-best-streak` = 3, `dash-best-streak-habit` = "Gym", `dash-week-rate` = `80%`. Archive Gym and expect `dash-best-streak` = 1 (Read), `dash-best-streak-habit` = "Read", `dash-week-rate` = `71%`. Restore Gym and expect the values from before.
22. **T5.** Archive Read, restore it, and expect the same streak and stats values as in T1. Delete Read (confirm). Create "Read" again with start 2026-03-01. Expect `streak-current` = 0, `total-completions` = 0, and every History row without "Done".
23. **M1.** Create "Plank" (every day, start 2026-03-01). At `?now=2026-03-03T09:00` backfill 03-01 and 03-02 (no milestone toast appears while backfilling). On Today click `Check in Plank`. Expect a toast containing `Milestone reached: 3-day streak on Plank` and a toast `Checked Plank`. Uncheck, then check again, and expect the milestone toast again.
24. **M2.** Create "Plank" (every day, start 2026-03-01). At `?now=2026-03-04T09:00` backfill 03-01, 03-02, 03-03 in History, then on Today click `Check in Plank` (streak goes 3 to 4). Expect the `Checked Plank` toast and no toast containing "Milestone reached". Then create "Backfill3" (every day, start 2026-03-01). At `?now=2026-03-03T09:00` backfill 03-01, 03-02 and 03-03 in History, so the streak reaches 3 via backfill. Expect no toast containing "Milestone reached" at any point and no Undo toast.
25. **M3.** Create "Stretch7" (every day, start 2026-03-01), backfill 03-01 to 03-07 at `?now=2026-03-07T20:00`. On Habits, expect the card to contain `Milestone: 3-day streak` and `Milestone: 7-day streak`, and none for 14, 30, 60, 100, 365. Uncheck 03-07 in History and expect `Milestone: 7-day streak` gone and `Milestone: 3-day streak` present.
26. **D1.** Create A, B, C (every day, start 2026-03-01, in that order, no backfill) at `?now=2026-03-04T09:00#/today`. Check A, add the note "ran 5 km", uncheck A, click "Undo" (A is checked again with its note), click `Skip B today`, check C. Expect `2 of 2 done` and "All done for today". Reload and expect the same state and the note. Expect `streak-current` on Today: A = 1, B = 0, C = 1. Open `#/insights` and expect `dash-best-streak` = `1`, `dash-best-streak-habit` = "A", `dash-week-rate` = `18%`.
27. **D2.** Create "Walk" and check yesterday's date in History. Expect the streak value to change at once. Compare the same value on the Today item, the Habits card, and `dash-best-streak`.
28. **D3.** After running F1 to F9, reload each page (`#/today`, `#/habits`, `#/insights`) and confirm all data is unchanged. Confirm Sprint 1 data (habits, order, archived list) remains intact.
29. **V1.** On Today, measure the check button's bounding box (width and height >= 44). Check it and expect a checkmark icon plus the text "Done". In the History dialog, confirm each status text is present on every row next to an icon. View screenshots and read them.
30. **V2.** Read computed styles on `streak-current`: font-size >= 32px, font-weight >= 600, and `font-variant-numeric` including `tabular-nums`. Inspect screenshots for the flame icon and for the longest streak looking secondary.
31. **V3.** Inspect screenshots of History (with Missed rows) for gray, non-red styling. Inspect the ring and the milestone badges for teal-green and amber.
32. **V4.** Take screenshots of Today, Habits (with stats and badges), the History dialog, the toasts, and Insights Dashboard, in light and dark and at 1280 px and 375 px width. Open and read them. Assert no horizontal scroll at 375 px (`scrollWidth <= clientWidth`).
33. **V5.** Open `#/insights` and expect no "Coming soon" text. Open `#/calendar` and `#/settings` and expect their Sprint 1 placeholders.
34. **C1.** Run `npm run build`, `npm test`, and `npm run test:e2e` and expect zero failures against both servers.
35. **C2.** In every test above, assert zero console errors and that all request hosts equal the local host.
36. **C3.** Search the delivered app by behavior: change check-ins and confirm that every number changes with them, and that no number is constant. Check that no "TODO" or placeholder text is visible in the UI.
37. **C4.** Review the repository: the streak and statistics code lives in a module that imports neither storage nor the clock, and its unit tests call it directly with plain data.

## Notes for the evaluator

- Two choices where the spec allowed alternatives are stated above:
  - The backfill UI is a day list plus a "Jump to date" field.
  - Today's pending, unchecked state is left out of rate denominators (so FX-READ shows 71% with today done and 67% with today pending).
- Please check both numbers, since they follow directly from the definitions.
- Milestone toasts fire for Today checks only, and badges are derived from the current longest streak.
