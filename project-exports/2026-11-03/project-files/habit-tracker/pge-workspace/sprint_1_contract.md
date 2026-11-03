# Sprint 1 Contract

## Scope
Sprint 1 of the spec: "Foundation, Habits, Schedules, and Persistence". All of the following are in scope:

1. Project foundation: a front-end app runnable on Node 22 with scripts `dev`, `build`, `preview`, `test` (unit), `test:e2e` (Playwright), and no external services, accounts, or API keys.
2. App shell: navigation with Today, Habits, Calendar, Insights, Settings (Today and Habits functional; Calendar, Insights, Settings are placeholders), light/dark theme following the system preference, responsive layout (left rail on desktop, bottom tab bar on phone width).
3. Local persistence with a versioned data model for habits (data survives reloads and browser restarts).
4. Habit CRUD: create, edit, archive, restore, delete with confirmation; name validation; color; emoji; start date; time-of-day grouping; reorder.
5. Schedules: daily and specific weekdays, plain-language schedule labels, at least one day required.
6. Empty-state onboarding with one-click templates and "Load sample data", plus the short "data stays on this device" note.
7. A documented, test-controllable notion of "today".

Explicitly out of scope (later sprints): check-ins, streaks, statistics, reminders, calendar contents, import/export, week-start setting, quick add, insights.

## Deliverables
- `package.json` with scripts `dev`, `build`, `preview`, `test`, `test:e2e`; app serves with `npm run dev` and `npm run preview` on Node 22.
- App shell with five navigation destinations: Today (`/#/today` or equivalent route), Habits, Calendar, Insights, Settings. Calendar, Insights, and Settings show a clearly labeled "coming soon" placeholder; the Settings page additionally shows the current theme following the system.
- Habits page listing active habits (grouped by time of day: Morning, Afternoon, Evening, Anytime) and a separate Archived section.
- Habit form (create and edit) with fields: Name (required), Description (optional), Color (palette of 10: coral, amber, olive, teal, sky, indigo, plum, rose, slate, sand), Emoji (a plain text input labeled "Emoji"; see Emoji handling below), Start date (default today), Time of day (Morning/Afternoon/Evening/Anytime, default Anytime), Schedule (Every day, or specific weekdays Mon-Sun toggle buttons).
- Emoji handling: the form contains a text input labeled "Emoji" that accepts typed or pasted emoji. Optional quick-pick emoji buttons may be offered in addition, but the labeled text input is always present and is the control tests use. The input holds at most one emoji: any input beyond the first emoji (a second emoji or any trailing text) is truncated to the first emoji, silently and without an error. Non-emoji text (for example "abc") is not accepted as the emoji: it is discarded and the field falls back to the default emoji "✅" on save. Leaving the field empty also saves the default "✅". The saved emoji is shown on the habit's card and in the edit form.
- Habit cards showing emoji, name, color edge, schedule label, and actions: Edit, Archive/Restore, Delete, Move up, Move down.
- Delete confirmation dialog.
- Empty state with "Create your first habit" button, four template buttons (Drink water, Read 20 min, Exercise Mon/Wed/Fri, Meditate), a "Load sample data" button, and the privacy/backup note.
- Documented "today" override (documented in the README and the handoff): app honors Playwright clock control, and additionally a `?now=YYYY-MM-DDTHH:mm` URL parameter that fixes the app's notion of "now" for the session.
- Unit tests for pure logic added this sprint (schedule labels, schedule validation, ordering) and a Playwright suite covering every criterion below.
- Stable accessible names / test ids on every interactive element used by the test method (listed in Test Method).

## Pass/Fail Criteria

### Functionality (PASS threshold: all core flows work)
- [ ] `npm run dev` and `npm run preview` (after `npm run build`) each serve the app on Node 22, and during load plus all core flows the browser makes no network requests other than to the local server (no third-party fonts, CDNs, analytics, or APIs).
- [ ] The app requires no login, account, or API key; it opens directly to a usable screen.
- [ ] A new user (no data) sees an empty state with "Create your first habit", four templates, "Load sample data", and a note stating data stays on this device and can be backed up.
- [ ] Creating a habit with name, color, emoji, time of day, and schedule adds it to the Habits list; after a full page reload it still appears with the same name, emoji, color, time-of-day group, and schedule label.
- [ ] The form's "Emoji" control is a text input; typing one emoji saves it and the card shows it; typing two emoji or an emoji followed by text saves and shows only the first emoji; leaving it empty saves and shows the default "✅"; after reload the saved emoji is unchanged.
- [ ] Submitting the form with an empty or whitespace-only name shows an inline error next to the name field and creates no habit.
- [ ] Deselecting every weekday in the weekday schedule shows an inline error and the habit cannot be saved; nothing is created.
- [ ] Start date defaults to today (per the controlled "today") and can be changed; the chosen start date is retained after reload and shown when editing.
- [ ] Editing a habit's name and schedule persists after reload, and the habit's position in the list is unchanged by the edit.
- [ ] Archiving a habit removes it from the active list and shows it in the Archived section; reloading keeps it archived; Restore returns it to the active list.
- [ ] Deleting a habit opens a confirmation dialog; Cancel keeps the habit; Confirm removes it permanently (still gone after reload, and absent from Archived too). A habit can be deleted from the Archived section as well.
- [ ] Schedule labels read "Every day" for daily, and list the chosen days in week order for weekday schedules (e.g. "Mon, Wed, Fri"; "Sat, Sun"; a single day reads "Tue").
- [ ] Clicking a template creates a correctly scheduled habit in one click: Drink water (Every day), Read 20 min (Every day), Exercise (Mon, Wed, Fri), Meditate (Every day); each with an emoji and color, visible on the Habits list immediately and after reload.
- [ ] "Load sample data" creates several (at least 4) varied habits with different schedules and times of day; they persist after reload; the empty state disappears.
- [ ] No console errors or uncaught exceptions occur during create, edit, archive, restore, delete, reorder, template, sample-data, and reload flows.

### Product Depth (PASS threshold: at least 3 meaningful interactions)
- [ ] Reordering: Order is maintained within each time-of-day group. Move up / Move down change the order of habits within their own group only and never move a habit across groups (a habit changes group only by editing its Time of day). Move up is disabled on the first habit of its group and Move down is disabled on the last habit of its group, so the first habit of a later group has Move up disabled even though habits exist in earlier groups. Reordering within one group does not alter the order of any other group. The new order persists after reload.
- [ ] Time-of-day grouping: Habits are shown under Morning, Afternoon, Evening, and Anytime headings, only non-empty groups are displayed, and changing a habit's time of day moves it to the new group.
- [ ] The Today screen lists only habits scheduled for the controlled "today" (grouped by time of day), and a "Show unscheduled habits" toggle reveals the others, labeled as not scheduled today. (Listing only; no check control this sprint.) Archived habits never appear on Today. A habit whose start date is after the controlled today never appears on Today, with or without "Show unscheduled habits" enabled.
- [ ] The controlled "today": opening the app with `?now=2026-03-04T09:00` (a Wednesday) makes Today show the date as Wednesday, 4 March 2026 and the new-habit start date default to 2026-03-04; Mon/Wed/Fri habits appear by default, Tue/Thu-only habits only after enabling the toggle.
- [ ] Edit form is pre-filled with the habit's current values (including schedule days and color), and cancelling the edit leaves the habit unchanged.
- [ ] Theme: with the browser's color scheme emulated as light, the canvas is warm off-white and text dark; with dark emulated, the canvas is dark charcoal and text light, without reload being required to be correct on first load.

### Visual Design (PASS threshold: no placeholder UI, consistent styling)
- [ ] Navigation shows Today, Habits, Calendar, Insights, Settings as a left rail at desktop width (>= 1024px) and a bottom tab bar at phone width (<= 480px) with content collapsing to a single column; no horizontal scrolling at 375px width.
- [ ] Habit cards have rounded corners, soft shadow, roomy padding, and a left color edge in the habit's chosen color; the emoji and schedule label are visible on each card.
- [ ] The 10-color palette is presented as selectable swatches with visible selected state that does not rely on color alone (e.g. checkmark and accessible name for each color).
- [ ] The warm off-white / deep ink light theme and soft charcoal dark theme are applied consistently across Today, Habits, form, dialog, and placeholders; text remains legible in both.
- [ ] Calendar, Insights, and Settings placeholders contain intentional "coming soon" copy rather than blank or lorem-ipsum content; no unstyled default browser controls on main screens.
- [ ] The weekday picker buttons clearly indicate selected vs unselected state with more than color (e.g. filled plus checkmark, `aria-pressed`).

### Code Quality (PASS threshold: no critical errors, no stubs)
- [ ] `npm run build` completes without errors on Node 22 and type checking passes.
- [ ] `npm test` (unit) passes and covers: schedule label generation (daily, multiple days, single day, week ordering), schedule validation (empty weekday set rejected), name validation (empty and whitespace rejected), and ordering/reorder logic.
- [ ] `npm run test:e2e` passes against the running app and covers every functional criterion above.
- [ ] Data model is versioned (a schema version is stored with the data) and persistence is wired so reload never loses habits; no placeholder or stubbed persistence (e.g. in-memory only state) is used for habits.
- [ ] No TODO/stub code for in-scope features; the README documents install, run, test commands and the "today" override.

## Test Method
All steps run in Playwright against `npm run dev` (and the key reload/persistence scenarios again against `npm run build && npm run preview`). Each test starts with a fresh browser context (empty storage). Fixed time is set by opening the app with `?now=2026-03-04T09:00` (Wednesday) or by Playwright clock control. Console and page errors are collected in every test, and the test fails if any appear. Request listener records every request URL.

Accessible names / identifiers the tests rely on: nav links named "Today", "Habits", "Calendar", "Insights", "Settings"; buttons "Create your first habit", "New habit", "Load sample data", "Save habit", "Cancel", "Edit <habit name>", "Archive <habit name>", "Restore <habit name>", "Delete <habit name>", "Move up <habit name>", "Move down <habit name>", "Confirm delete", template buttons named by template text; form fields labeled "Name", "Description", "Start date", "Time of day", and a text input labeled "Emoji"; color swatches named by color (e.g. "Color teal"); schedule control with "Every day" option and weekday buttons "Mon" to "Sun"; inline errors with role alert; toggle "Show unscheduled habits".

1. Network and no-account (criteria: serves on dev/preview, no network requests, no login)
   - Start the dev server; navigate to `/`. Assert page loads to the app shell directly (no login form). Record all requests through load, creating a habit, and reloading. Assert every request host equals the local server host. Repeat against the preview server.
2. Empty state
   - Fresh context, open `/`. Assert visible: button "Create your first habit", four template buttons ("Drink water", "Read 20 min", "Exercise Mon/Wed/Fri", "Meditate"), "Load sample data", and text mentioning that data stays on this device and how to back it up (export).
3. Create + persist
   - Click "Create your first habit". Fill Name "Morning Run", Description "Around the park", choose "Color coral", fill the text input labeled "Emoji" with "🏃", Time of day "Morning", schedule weekday buttons Mon, Wed, Fri, Start date left default. Click "Save habit". Navigate to Habits: assert card "Morning Run" under the "Morning" heading with schedule text "Mon, Wed, Fri" and emoji "🏃". Reload the page. Assert the card is still present with identical name, emoji, label, group; open Edit and assert color coral is selected and the weekdays Mon/Wed/Fri are pressed.
4. Validation
   - Open New habit; leave Name empty and click "Save habit": assert an inline error (role alert) near Name and the Habits list remains empty. Enter spaces only: same result. Enter a valid name, press every selected weekday button to deselect all (after choosing weekdays), click "Save habit": assert inline schedule error and no habit created. Reload: Habits list still empty.
5. Start date
   - With `?now=2026-03-04T09:00`, open New habit: assert Start date input value is 2026-03-04. Change it to 2026-03-01, save "Floss"; reload; open Edit and assert 2026-03-01.
6. Edit + persist
   - Create "Read" (Every day). Click "Edit Read"; assert form prefilled; change name to "Read Books" and schedule to Tue, Thu; save. Assert card shows "Read Books" and "Tue, Thu". Reload; assert the same. Click Edit again, change a field, click "Cancel"; assert nothing changed. Assert the edit did not move the card's position among other habits (create two habits first and edit the first).
7. Archive / Restore
   - Click "Archive Read Books": assert it disappears from active list and appears in the Archived section; open Today with unscheduled toggle on and assert it is absent. Reload; assert still archived. Click "Restore Read Books": assert it is back in the active list and gone from Archived; reload and assert.
8. Delete with confirmation
   - Click "Delete Read Books": assert a confirmation dialog naming the habit. Click "Cancel": habit remains. Click Delete again then "Confirm delete": habit disappears; reload: still gone. Archive another habit and delete it from the Archived section; assert permanently removed after reload.
9. Schedule labels
   - Create habits: Every day; Mon, Wed, Fri selected out of order (click Fri then Mon then Wed); Sat and Sun; Tue only. Assert labels exactly "Every day", "Mon, Wed, Fri", "Sat, Sun", "Tue".
10. Templates
    - Fresh context, click template "Exercise Mon/Wed/Fri": assert one click navigates/shows a habit named "Exercise" with label "Mon, Wed, Fri" and an emoji; reload and assert persisted. Clear storage in a fresh context and click each of "Drink water", "Read 20 min", "Meditate": assert each habit exists with label "Every day".
11. Sample data
    - Fresh context, click "Load sample data": assert at least 4 habits listed on Habits with at least two different schedule labels and at least two different time-of-day groups; assert the empty state is no longer shown; reload and assert same habits.
12. Reorder
    - Single group: create A, B, C in the same time-of-day group (Morning). Click "Move down A": assert order B, A, C. Click "Move up C": assert B, C, A. Assert "Move up B" is disabled and "Move down A" is disabled (first/last of the group). Reload and assert order B, C, A.
    - Two groups: additionally create D and E in the Evening group (Morning: B, C, A; Evening: D, E). Assert "Move up D" is disabled (first of the Evening group, even though Morning habits exist above it) and "Move down A" is still disabled (last of Morning, it cannot move into Evening). Click "Move down D": assert Evening order is E, D and Morning order is still B, C, A. Click "Move up C": assert Morning order is C, B, A and Evening order is still E, D. Assert no habit changed group heading. Reload and assert Morning C, B, A and Evening E, D.
13. Time-of-day grouping
    - Create habits with Morning, Afternoon, Evening, Anytime. Assert four headings in order Morning, Afternoon, Evening, Anytime with the right habit under each; with only some present, assert absent groups' headings are not rendered. Edit one habit from Morning to Evening and assert it moves under Evening.
14. Today view and controlled today
    - Open `/?now=2026-03-04T09:00` with habits: "MWF" (Mon, Wed, Fri), "TT" (Tue, Thu), "Daily" (Every day), "Future" (start date 2026-03-10), and an archived habit. Navigate to Today: assert the heading shows Wednesday and 4 March 2026; assert "MWF" and "Daily" are listed, "TT", "Future" and the archived habit are not. Toggle "Show unscheduled habits": assert "TT" appears labeled as not scheduled today; the archived habit and "Future" are still absent from Today (a habit whose start date is after the controlled today never appears on Today, with or without the toggle). Also confirm the default Start date in a new habit form is 2026-03-04. Repeat with the Playwright clock set instead of the URL parameter and confirm the same result.
15. Theme
    - Emulate `colorScheme: 'light'`, open `/`, read computed background and text colors of the page: background is a warm off-white (approximately #FAF8F5) and text dark (approximately #1F2328). Emulate `dark` in a new context: background dark charcoal (approximately #16181C) and text light. No toggle/reload needed to see the correct theme on first load.
16. Responsive layout
    - Viewport 1280x800: assert navigation is a vertical left rail containing all five links positioned left of the content, content column width roughly 720px max. Viewport 375x700: assert navigation is a bottom bar fixed along the bottom of the viewport with all five links visible, the document has no horizontal scroll (scrollWidth <= clientWidth), and the Habits list is a single column. Navigate to each of Today, Habits, Calendar, Insights, Settings and assert each renders a non-empty page with its heading; Calendar, Insights, Settings show "coming soon" copy.
17. Visual inspection of cards and form
    - Take screenshots at desktop and phone width of Habits with 4 or more habits (light and dark), the open form, the delete dialog, and the empty state. Verify: cards show color edge, emoji, schedule label, rounded corners and shadow; swatches show a visible selected indicator (checkmark) and each swatch has an accessible name; weekday buttons expose pressed state via `aria-pressed` and show a non-color selected indicator; text is legible in both themes.
18. Console cleanliness
    - Across tests 3 to 14, assert zero `console.error` messages, zero `pageerror` events, and no failed requests.
19. Build, unit, and e2e scripts
    - Run `npm run build` (exit 0), `npm test` (exit 0; output shows tests for schedule labels, schedule validation, name validation, ordering), and `npm run test:e2e` (exit 0). Confirm `package.json` declares scripts `dev`, `build`, `preview`, `test`, `test:e2e`, and the README documents the `?now=` override.
20. Persistence layer sanity
    - After creating a habit, inspect the browser's storage in Playwright (evaluate in page) and assert habits are persisted in browser storage (not only in memory) and that a stored schema version value exists; close the page and open a new page in the same context (simulating restart) and assert the habit remains.
21. Emoji input handling
    - Open New habit. Fill the text input labeled "Emoji" with "🔥🏃" (two emoji), name "Two", save; assert the card for "Two" shows "🔥" and not "🏃". Create "Texty" with Emoji "🏃abc": card shows "🏃" only. Create "Blank" leaving Emoji empty: card shows "✅". Create "Letters" with Emoji "abc": card shows "✅". Reload and assert all four cards show the same emoji; open Edit on "Two" and assert the Emoji input value is "🔥".
