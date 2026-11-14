# Sprint 2 Handoff

## What Was Implemented

**Streak engine (pure).** `src/domain/streaks.ts` imports no storage and no clock. It exposes `dayStatus`, `computeStreaks`, `completionRate`, `totalCompletions`, `habitStats`, `milestonesReached`, `milestoneCrossed`, `summarizeDashboard` and `withDay`. One forward walk from the start date to today: Done adds 1, Skipped is passed over, Missed resets the run, and Pending today, unscheduled days and Bonus days are invisible. Longest is the maximum run seen. Rates exclude Skipped days and Pending today, round half up, and return `N/A` with no evaluated days. 42 new unit tests in `src/domain/streaks.test.ts` are named after contract items S1 to S7, T1 to T4, D1 and M3, and cover rounding, skip and pending exclusion, `N/A`, and milestone thresholds.

**Schedule history.** Habits gain an optional `scheduleHistory` (`from` date plus schedule). `scheduleOn(habit, date)` returns the schedule in force on a day. Editing a schedule adds an entry that starts on the day of the edit (a second edit that day replaces it), so earlier days keep their old schedule. Sprint 1 habits without history fall back to their current schedule.

**Storage.** IndexedDB version 2 adds a `checkins` store (key `habitId|date`, index on `habitId`; kind `done` or `skip`, plus an optional note). Deleting a habit deletes its check-ins in the same transaction. Writes to future dates and to dates before the start date are ignored by the store.

**Today page.** Progress card with ring (`role=progressbar`, name "Daily progress"), `today-progress` ("N of M done", skipped habits excluded) and "All done for today" (persists after reload, hides on uncheck). A burst (`data-testid="confetti"`, `aria-hidden`) shows for 2 seconds only right after the user's own check completes the day, never after a reload, and never under reduced motion. Each habit is an `article` with a large check button (`Check in <name>`, `aria-pressed`, checkmark and "Done" when checked), streak hero (36px bold, tabular numerals, amber flame), longest streak, Skip / Clear skip, Add / Edit note (inline editor, 200 character limit, Save note / Cancel), "Not scheduled today" and "Bonus" badges. Undo toast (6 s, one at a time, restores the exact prior state including note or skip) and stacking milestone toast (highest milestone only, Today checks only).

**Habits page.** Every active card shows `streak-current`, `streak-longest`, `rate-7d`, `rate-30d`, `rate-all`, `total-completions`, milestone badges (`role=img`, name `Milestone: N-day streak`, derived from the longest streak) and a `History for <name>` button.

**History dialog.** `role=dialog` named `History: <name>`; newest-first day list (14 days, "Show 14 more days" until the start date), rows with `history-row` / `data-date` / `history-status`, `Check in … on <date>`, `Skip … on <date>`, `Note for … on <date>` buttons, "Jump to date" (min start date, max today) with a "Selected date" region, and the two alerts for future and pre-start dates. No Undo or milestone toasts from here.

**Insights.** The placeholder is replaced by a Dashboard: `dash-best-streak`, `dash-best-streak-habit` (ties go to the first habit in Habits-page order), `dash-week-rate` (pooled 7-day rate over active habits), and an empty message with no habits.

## How to Run

```
cd /home/user/habit-tracker
npm install
npm run dev                        # http://localhost:5173
npm run build && npm run preview   # http://localhost:4173
npm test                           # 73 unit tests (42 new for streaks and stats)
npm run test:e2e                   # 110 tests: 55 run against dev (5173) and 55 against preview (4173)
```

`npm run test:e2e` starts and stops both servers itself; ports 5173 and 4173 must be free. Chromium is already installed (`npx playwright install chromium` otherwise).

### Controlling "today"

`/?now=YYYY-MM-DDTHH:mm` (local time), e.g. `http://localhost:5173/?now=2026-03-07T20:00#/today`. A new `?now` navigation on the same origin keeps stored data. Playwright's clock also works (no override read by the app).

### New test identifiers

- Today: `today-progress`, `today-item` (on the `article`), `streak-current`, `streak-longest`, `note-text`, `confetti`; ring `getByRole('progressbar', {name: 'Daily progress'})`; toasts are `role=status`.
- Habits cards: `streak-current`, `streak-longest`, `rate-7d`, `rate-30d`, `rate-all`, `total-completions`.
- History dialog: `history-row` (+ `data-date`), `history-status`; list is named "Recent days", the jump result region is "Selected date".
- Insights: `dash-best-streak`, `dash-best-streak-habit`, `dash-week-rate`.
- New e2e file: `e2e/checkins.spec.ts` (31 tests per project, covering F1 to F9, S1 to S7, T1 to T5, M1 to M3, D1 to D3, V1, V2, V4, V5).

## Self-Evaluation

| Criterion | Status | Notes |
|-----------|--------|-------|
| F1 Check/uncheck, progress text | PASS | e2e |
| F2 Persistence across reload | PASS | e2e |
| F3 Undo toast incl. note, auto-dismiss under 10 s | PASS | e2e; toast lasts 6 s |
| F4 Grouping, toggle, archived and future-start hidden | PASS | e2e |
| F5 Progress ring, celebration, burst rules, reduced motion | PASS | e2e |
| F6 Notes (add, edit, clear, 200 limit, removed on uncheck) | PASS | e2e |
| F7 Skip rules | PASS | e2e |
| F8 Backfill in History (paging, jump, notes, skips) | PASS | e2e |
| F9 Future dates locked, pre-start locked | PASS | e2e |
| S1 to S7 streak scenarios | PASS | e2e and unit tests with exact contract numbers |
| S8 Unit tests cover every rule | PASS | `src/domain/streaks.test.ts` |
| T1 to T5 stats, dashboard, archive/delete | PASS | e2e; deletion also verified to leave zero check-in records |
| M1 to M3 milestones | PASS | e2e |
| D1 to D3 product depth | PASS | e2e |
| V1 to V5 visual | PASS | Reviewed screenshots, light and dark, 1280 px and 375 px; no horizontal scroll asserted; missed days gray; ring teal-green; milestone badges amber |
| C1 build, unit, e2e on dev and preview | PASS | 110 of 110 e2e, 73 of 73 unit, build clean |
| C2 no console errors or non-local requests | PASS | The auto fixture asserts it in every test |
| C3 no stubs | PASS | All numbers derive from stored check-ins |
| C4 engine is a pure module | PASS | `streaks.ts` imports only `dates` and `schedule` |

## Deviations and Notes

- **Schema version stays 1.** IndexedDB version is 2 (new store), but the logical `schemaVersion` in `meta` and localStorage is unchanged because the change is additive and Sprint 1 data is valid as is. This keeps the Sprint 1 storage test valid.
- **Sprint 1 e2e change.** The only edit to `e2e/habits.spec.ts` is the Insights entry in the placeholder test: it now expects "Dashboard" instead of "Coming soon" (contract V5).
- **Toggle needed on off days.** Today lists only scheduled habits, so on a day when Gym is not scheduled (S1 Saturday or Sunday) the "Show unscheduled habits" toggle must be on to see its streak on Today. The Habits card always shows it.
- **Label overlap.** On Today the button `Add note for A` and the text area `Note for A` share the phrase "Note for A". The button is hidden while the editor is open, so `getByLabel('Note for A')` is unique while editing. Use `exact: true` when the editor is closed.
- **Selected date vs list.** When "Jump to date" selects a date that is also in the day list, that date is shown only in the "Selected date" area so each control stays unique.
- **Total completions** counts check-ins from the start date through today (bonus included).
- **Toast scope.** Undo and milestone toasts live in the app shell, so they can remain visible for their 6 seconds after navigating to another page.
- Skip and note changes do not show an Undo toast (the contract asks for it on check and uncheck only).

## Known Limitations

- If the app clock is set earlier than existing check-ins, those later dates are ignored by every number until time reaches them.
- Week-start setting, calendar, heatmap, activity log, export/import, reminders and the intelligence features stay out of scope, per the contract.
- `pge-workspace/` is left untracked.
