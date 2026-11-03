# Sprint 4 Handoff

## What Was Implemented
- **Month calendar** (`#/calendar`, `#/calendar?habit=<id>&month=YYYY-MM`): habit select, previous/next month, 8 day states each with a distinct shape plus text (never color only), legend, per-habit current/longest streak, click a day to check, skip, or edit its note. Locked days (future, before start) are `aria-disabled`. Week start follows the setting.
- **Year heatmap** (`#/calendar/year`): 371 `heatmap-cell` role=img cells, scrolls inside a focusable region, today outlined.
- **Activity log** (`#/calendar/log`): filters (habit, kind, notes only, date), `log-count`, 50 rows at a time ("Show 50 more").
- **Export / import**: version 1 JSON export; import validates everything, shows a preview, Merge (default, local wins) or Replace (confirm dialog), all-or-nothing, messages per contract.
- **Settings**: Theme (System/Light/Dark, no flash via inline head script), Week start, Data card, Shortcuts card, Reset (type RESET).
- **Intelligence (on device)**: Quick Add on Today (preview, then prefilled habit form), Smart Reminder Timing and Schedule Fit suggestions on habit cards (accept/dismiss, 30 day dismissal), Weekly Insights on Insights.
- **Accessibility/polish**: skip link, h1 focus and document title per route, shortcuts `n t h c i s / ?`, reduced motion, AA contrast (`--accent-text`), axe in tests.
- **Atomic reminder delivery (F21/F22)**: claim plus pending row in one transaction, notify, then settle; orphaned pending rows are recovered into the banner on next page start.

## How to Run
```
npm install
npm run dev                        # http://localhost:5173
npm run build && npm run preview   # http://localhost:4173
npm test                           # unit
npx playwright install chromium    # once
npm run test:e2e                   # starts both servers (5173, 4173 must be free)
npm run fixtures                   # regenerate e2e/fixtures/data/*.json
```
Test hooks: `?now=YYYY-MM-DDTHH:mm`, `window.__cadenceTest.{setNow,advanceMinutes,clickNotification}`, `window.__cadenceNotifications`.

## New identifiers
Calendar: `calendar-month`, `calendar-day` (data-date/state/shape/today/has-note), `calendar-pad`, `calendar-day-detail`, `calendar-day-status`, `calendar-note-text`, `calendar-legend`, `streak-current`, `streak-longest`, `heatmap-cell`, `log-row`, `log-count`. Data: `export-status`, `import-error`, `preview-exported|habits|checkins|merge`, `import-result`, `theme-status`. Intelligence: `reminder-suggestion` (data-time), `schedule-fit-suggestion`, `weekly-insights`, `weekly-insights-range`, `weekly-insight`, `quickadd-explain`. `localStorage`: `cadence.theme`, `cadence.weekStart`; `data-theme` on `<html>`.

Export format v1: `{format:"cadence-export", version:1, exportedAt, habits[], checkins[], settings{theme,weekStart,remindersPaused,quietHours{enabled,start,end},streakAtRisk{hour,reminder}}, suggestionDismissals[]}`; file name `cadence-backup-YYYY-MM-DD.json`; 2-space indent. Full description in README.md.

## Deviations
- The habit card's Calendar link is `<a role="button">` (with Space handler) so Sprint 3 strict-mode locators for the link named "Calendar" still resolve to one element.
- A completed day with a note is selected on first click rather than toggled off, to protect the note.
- Edited earlier tests only for the removed "Coming soon" placeholders and the privacy note (checkins.spec.ts, habits.spec.ts layout expectations).
- Only added dev dependency: `@axe-core/playwright`.

## Self-Evaluation
| Criterion | Status | Notes |
|-----------|--------|-------|
| Month calendar, 8 states, navigation, click-to-edit | PASS | calendar.spec.ts 9/9 |
| Year heatmap and filterable activity log | PASS | calendar.spec.ts, visual V3 |
| Export, import preview, Replace/Merge, validation, messages | PASS | data.spec.ts 11/11 |
| Settings: theme, week start, reset | PASS | data.spec.ts, accessibility.spec.ts |
| Quick Add, Smart Reminder Timing, Schedule Fit, Weekly Insights | PASS | intelligence.spec.ts 14/14, 260 unit tests |
| Accessibility: shortcuts, skip link, titles, reduced motion, AA contrast | PASS | accessibility.spec.ts incl. axe light/dark at 1280 and 375 |
| Atomic reminder delivery F21/F22 | PASS | hardening.spec.ts 4/4, delivery.test.ts |
| Visual (no overflow at 375/1280, light/dark, grayscale distinguishable) | PASS | visual.spec.ts; screenshots reviewed |
| Sprints 1-3 unbroken | PASS | full e2e green on dev and preview |
| Build / unit / e2e | PASS | build clean; 260 unit tests; 342 e2e (dev + preview) |

## Known Limitations
- Export/import covers app data only; browser notification permission is not exported.
- Heatmap and calendar are computed from the current schedule history; no per-day editing of schedules.
- Quiet-hours reminders are skipped, not deferred to when quiet hours end (by design in Sprint 3).
- Intelligence suggestions are heuristic (thresholds documented in `src/domain/*.ts`).
- Counts: unit 260 (17 files); e2e 342 runs = 171 tests x dev and preview.
