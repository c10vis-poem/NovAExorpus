# Sprint 1 Handoff

## What Was Implemented

**Foundation.** Vite + React + TypeScript app at the repo root (Node 22). Scripts: `dev`, `build` (type check + bundle), `preview`, `test` (Vitest unit), `test:e2e` (Playwright). No backend, accounts, API keys, web fonts, or CDN assets; the only requests are to the local server. The favicon is an inline data URI.

**App shell.** Hash routes `#/today`, `#/habits`, `#/calendar`, `#/insights`, `#/settings` (`/` goes to Today). Nav is a left rail at >= 1024px and a fixed bottom tab bar below that (phone width included). Content column is max 720px. Calendar, Insights, and Settings show a "Coming soon" placeholder with intentional copy; Settings also shows "Following your system: currently light/dark". Light theme is #FAF8F5 canvas with #1F2328 text; dark is #16181C canvas with light warm text; both come from `prefers-color-scheme` in CSS, so the first paint is correct.

**Persistence.** IndexedDB database `cadence` with object stores `habits` and `meta`. `meta.schemaVersion` is 1 and is mirrored to `localStorage["cadence.schemaVersion"]`. A migration hook rejects data from a newer schema. The UI updates immediately and the write is queued right behind it. If a write fails, the list reloads from storage and an alert banner is shown.

**Habit CRUD.** The "New habit" / "Edit habit" form is a modal with Name (required, max 60), Description, Color (10 swatches, each "Color <name>", `aria-pressed` plus a checkmark), Emoji (text input labeled "Emoji", plus quick-pick buttons named "Pick <emoji>"), Start date (defaults to the controlled today), Time of day (select), and Schedule ("Every day" button plus Mon..Sun toggle buttons with `aria-pressed` and a checkmark). Empty or whitespace-only names and an empty weekday set show inline `role="alert"` errors and create nothing. Editing keeps the habit's position unless Time of day changes, in which case it goes to the end of the new group. Archive, Restore, and Delete (confirmation `alertdialog` with "Cancel" and "Confirm delete") work, including Delete from the Archived section.

**Emoji rule.** On save the first grapheme is kept if it is an emoji, so "🔥🏃" saves 🔥 and "🏃abc" saves 🏃. Non-emoji text such as "abc" and empty input save "✅". This is silent, with no error.

**Schedules.** Labels are "Every day", or the chosen days in week order ("Mon, Wed, Fri", "Sat, Sun", "Tue"). Selecting all 7 weekdays is normalised to "Every day".

**Habits page.** Active habits are grouped under Morning, Afternoon, Evening, Anytime (empty groups are not rendered), then an "Archived" section. Move up / Move down act within the habit's own group only and are `disabled` at the group's first / last habit. Cards show a color edge, emoji, name, schedule label, description, rounded corners, and a soft shadow.

**Today page.** Shows the long date ("Wednesday, 4 March 2026"), scheduled habits grouped by time of day, and a "Show unscheduled habits" checkbox. Unscheduled habits get a "Not scheduled today" badge. Archived habits and habits starting after today never appear. There is no check control this sprint.

**Onboarding.** With no habits, Today and Habits show the empty state: "Create your first habit", four template buttons ("Drink water", "Read 20 min", "Exercise Mon/Wed/Fri", "Meditate"), "Load sample data" (7 varied habits), and the privacy and backup note. One click on a template creates the habit and goes to the Habits page. The note says export is "coming" because it is not built yet.

## How to Run

```
cd /home/user/habit-tracker
npm install
npm run dev                        # http://localhost:5173
npm run build && npm run preview   # http://localhost:4173
npm test                           # 31 unit tests
npx playwright install chromium    # once, if the browser is not installed
npm run test:e2e                   # 48 tests: 24 run against dev (5173) and 24 against preview (4173)
```

`npm run test:e2e` starts both servers itself and stops them afterwards; ports 5173 and 4173 must be free.

### Controlling "today" (also in README)

- URL: `http://localhost:5173/?now=2026-03-04T09:00` (local time, YYYY-MM-DDTHH:mm). It pins "now" for the session and is preserved across hash navigation and reload. Invalid values are ignored.
- Playwright clock: without the parameter the app reads `new Date()`, so `page.clock.install({ time })` works (covered by a test).
- All time reads go through `src/data/clock.ts`.

### Test hooks

- Cards: `<article>` named by habit name (`getByRole('article', { name })`); `data-testid` values `habit-card`, `habit-emoji`, `habit-schedule`, `today-item`, `today-date`, `theme-status`.
- Group sections are regions named "Morning" / "Afternoon" / "Evening" / "Anytime" / "Archived".
- The delete dialog is `role="alertdialog"`; the form is `role="dialog"`.

## Self-Evaluation

| Criterion | Status | Notes |
|-----------|--------|-------|
| dev and preview serve; no non-local requests | PASS | Every e2e test asserts all request hosts equal the local host, on both servers |
| No login, account, or API key | PASS | Opens straight to Today |
| Empty state content (create, 4 templates, sample data, privacy/backup note) | PASS | Covered by e2e |
| Create habit persists name, emoji, color, group, schedule across reload | PASS | e2e reload and edit-form checks |
| Emoji input rules (first emoji, default ✅, persisted) | PASS | Unit and e2e (Two, Texty, Blank, Letters) |
| Empty or whitespace name shows inline error, creates nothing | PASS | e2e |
| Empty weekday set shows inline error, creates nothing | PASS | e2e |
| Start date defaults to controlled today, retained after reload | PASS | e2e |
| Edit persists and keeps position; Cancel changes nothing | PASS | e2e |
| Archive / Restore persist across reload | PASS | e2e |
| Delete confirmation; Cancel keeps; Confirm removes permanently; works from Archived | PASS | e2e |
| Schedule labels | PASS | Unit and e2e |
| Templates create correctly scheduled habits in one click | PASS | e2e for all four |
| Sample data (7 habits, varied schedules and groups, persists) | PASS | e2e |
| No console errors or failed requests in core flows | PASS | Asserted by an automatic fixture in every e2e test |
| Reorder within groups only; disabled at group edges; persists | PASS | e2e covers the single-group and two-group scenarios |
| Time-of-day grouping; empty groups hidden; regroup on edit | PASS | e2e |
| Today filtering (scheduled, toggle, archived, future start) | PASS | e2e with both `?now=` and Playwright clock; unit tests too |
| Controlled today shows "Wednesday, 4 March 2026"; new-habit start date 2026-03-04 | PASS | e2e |
| Edit form prefilled (days, color); cancel leaves habit unchanged | PASS | e2e |
| Theme light/dark on first load | PASS | e2e computed colors: light rgb(250,248,245) / rgb(31,35,40); dark rgb(22,24,28) |
| Left rail at desktop, bottom bar at 375px, no horizontal scroll, single column | PASS | e2e geometry checks; I also viewed screenshots |
| Card styling; swatches with checkmark and accessible names; weekday buttons with aria-pressed and checkmark | PASS | Reviewed screenshots (light and dark, desktop and phone) |
| Placeholders have "coming soon" copy | PASS | e2e |
| Build and type check pass | PASS | `npm run build` runs `tsc --noEmit` first |
| Unit tests cover labels, schedule validation, name validation, ordering | PASS | 31 tests in `src/domain/*.test.ts` |
| e2e suite passes | PASS | 48 of 48 |
| Versioned data model, real persistence, README documents `?now=` | PASS | Stored schema version asserted in e2e |

## Known Limitations

- "New habit" appears on the Habits page only. On Today, the empty state offers creation.
- The weekday buttons are always visible. Pressing one while "Every day" is selected switches to a specific-days schedule containing just that day. Pressing "Every day" clears any selected days.
- Archived habits offer Restore and Delete only, not Edit.
- The privacy note says export is coming, because export is out of scope for this sprint.
- The week starts on Monday (the week-start setting is a later sprint).
- Playwright needs its Chromium download (`npx playwright install chromium`). It is already installed in this environment.
- `pge-workspace/` is left untracked and was not committed.

## For the Evaluator

- Reload-after-click timing: React state and the IndexedDB write happen together, so reloading immediately after a click is safe in my runs (the whole suite does this).
- Use `exact: true` when locating weekday buttons ("Mon" .. "Sun") and "Every day", since the card schedule labels contain the same words.
