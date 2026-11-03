# Product Specification: Cadence, a Local-First Habit Tracker

## Overview

Cadence is a single-user habit tracker that runs entirely in the browser on the user's own machine. It is for people who want to build routines (daily meditation, gym on Monday/Wednesday/Friday, a weekly review on Sunday) without accounts, subscriptions, or sending personal data anywhere. Its core value is streaks you can trust: a streak counts only the days a habit was actually scheduled, so a Monday/Wednesday/Friday gym habit does not "break" on Tuesday. Reminders arrive as browser notifications while the app is open, or as an in-app banner when notifications are blocked, and all data can be exported to a JSON file and imported again at any time.

### Hard Constraints (apply to every sprint)

- Single user, no login, no accounts, no backend server, no cloud sync, no third-party APIs or API keys. The app makes no network requests at runtime beyond loading its own assets.
- Runs locally on Node 22 with a simple front-end build: Vite with either vanilla TypeScript or React and TypeScript.
- All data is persisted in the browser (IndexedDB preferred for habits and check-ins, localStorage acceptable for small preferences). Data survives page reloads and browser restarts.
- Reminders use the browser Notification API and fire only while the app tab is open. When permission is denied, unsupported, or not yet granted, an in-app banner delivers the same reminder.
- All "intelligent" features are computed on the device with deterministic logic over the user's own history. No language models, no remote inference.
- The app must be testable with Playwright against `npm run dev` or `npm run preview`. Every interactive element that a test needs has a stable, accessible name or test identifier. Time-dependent behavior (today's date, reminder firing) must be controllable in tests, for example through Playwright's clock control or a documented developer override of "now".

## Features

### Module 1: Habit Management

1. Create a habit
   - As a user, I want to create a habit with a name, an optional description, a color, and an icon or emoji so that I can recognize it at a glance.
   - As a user, I want the form to reject an empty name and show an inline error so that I never create a blank habit.
   - As a user, I want to set a start date (default today) so that streaks and history do not count days before I began.
2. Edit a habit
   - As a user, I want to change any field of an existing habit so that I can refine it without losing history.
   - As a user, I want schedule changes to apply from today forward so that past streaks are not rewritten retroactively.
3. Archive and delete
   - As a user, I want to archive a habit so that it leaves my daily list but keeps its history for later review.
   - As a user, I want to restore an archived habit so that I can resume it.
   - As a user, I want deleting a habit to require confirmation and to remove its check-ins so that I do not lose data by accident and do not leave orphaned records.
4. Organize habits
   - As a user, I want to reorder habits by drag-and-drop or move-up/move-down controls so that my most important habits appear first.
   - As a user, I want to group habits by time of day (morning, afternoon, evening, anytime) so that my Today list reads like a plan for the day.

### Module 2: Schedules

1. Schedule types
   - As a user, I want to mark a habit as daily so that it is expected every day.
   - As a user, I want to pick specific weekdays (any subset of Monday through Sunday) so that a habit is expected only on those days.
   - As a user, I want a habit with no weekdays selected to be impossible to save so that every habit has at least one scheduled day.
2. Schedule awareness
   - As a user, I want the Today view to show only habits scheduled for today by default so that I am not distracted by off-day habits.
   - As a user, I want a toggle to show unscheduled habits too so that I can log a bonus completion on an off day.
   - As a user, I want each habit card to show its schedule in plain words ("Every day", "Mon, Wed, Fri") so that I always know what is expected.
3. Week start preference
   - As a user, I want to choose whether my week starts on Monday or Sunday so that the calendar and weekday picker match my locale.

### Module 3: Daily Check-ins

1. Today view
   - As a user, I want a Today screen listing my scheduled habits with a large one-tap check control so that logging takes a second.
   - As a user, I want a progress indicator ("3 of 5 done") and a progress ring for the day so that I can see how close I am to a full day.
   - As a user, I want a small celebratory animation when I complete every scheduled habit so that finishing the day feels rewarding.
2. Undo and correction
   - As a user, I want to uncheck a habit I checked by mistake so that my record stays accurate.
   - As a user, I want a short "Undo" toast after every check or uncheck so that I can reverse an accidental tap.
3. Backfill
   - As a user, I want to check in or clear a check-in on any past date since the habit's start date so that I can fix days I forgot to log.
   - As a user, I want future dates to be non-editable so that I cannot pre-log completions.
4. Notes
   - As a user, I want to attach an optional short note to a check-in so that I can record context ("ran 5 km", "skipped dessert").
5. Skip days
   - As a user, I want to mark a scheduled day as "skipped (excused)" for illness or travel so that it neither breaks nor extends my streak.

### Module 4: Streaks and Statistics

1. Schedule-aware streaks
   - As a user, I want my current streak to count consecutive scheduled days that I completed, ignoring unscheduled days, so that a Mon/Wed/Fri habit is not broken on Tuesday.
   - As a user, I want today to not break my current streak until the day is over, so that an unchecked habit in the morning still shows my streak from yesterday.
   - As a user, I want my longest streak ever to be shown next to my current streak so that I have a personal best to beat.
   - As a user, I want completions on unscheduled days to count as bonus completions that never break a streak and do not inflate it, so that the number stays honest.
   - As a user, I want excused skip days to be passed over (neither break nor extend), so that one sick day does not erase weeks of progress.
2. Statistics
   - As a user, I want a completion rate for the last 7 days, 30 days, and all time, calculated against scheduled days only, so that I know how consistent I really am.
   - As a user, I want total completions per habit so that I can see cumulative effort.
   - As a user, I want a dashboard summarizing all habits (best current streak, overall completion rate this week) so that I get a single health check.
3. Milestones
   - As a user, I want milestone badges at streak lengths 3, 7, 14, 30, 60, 100, and 365 so that I have intermediate goals.
   - As a user, I want a brief toast the moment I reach a milestone so that the achievement is noticed.

### Module 5: Reminders

1. Per-habit reminders
   - As a user, I want to set zero or more reminder times per habit so that I am nudged at the right moments.
   - As a user, I want reminders to fire only on the habit's scheduled days and only if the habit is not already completed that day, so that I am never nagged for nothing.
2. Notification permission
   - As a user, I want the app to ask for notification permission only when I add my first reminder (never on first load), so that the prompt makes sense in context.
   - As a user, I want a Settings panel showing current permission status (granted, denied, not asked, unsupported) with clear guidance, so that I know why I am or am not getting notifications.
3. In-app fallback
   - As a user whose notifications are denied or unsupported, I want reminders to appear as an in-app banner at the top of the screen so that I still get nudged while the app is open.
   - As a user, I want the banner to offer "Mark done", "Snooze 10 min", and "Dismiss" so that I can act immediately.
   - As a user, I want multiple due reminders to stack into one banner listing each habit, so that the screen is not flooded.
4. Reliability while open
   - As a user, I want reminders that came due while the tab was in the background or the laptop was asleep to be delivered once when the app becomes active again (if still relevant that day), so that I do not silently miss them.
   - As a user, I want each reminder to fire at most once per habit per scheduled time per day, so that reloads do not duplicate it.
5. Quiet hours and global controls
   - As a user, I want a global "pause all reminders" switch and optional quiet hours so that I can stop reminders on vacation or at night.

### Module 6: History and Calendar

1. Per-habit calendar
   - As a user, I want a month calendar for each habit that marks each day as completed, missed, skipped (excused), unscheduled, bonus, or future, so that I can read my pattern at a glance.
   - As a user, I want to move between months and jump back to the current month so that I can browse my full history.
   - As a user, I want to click a past day to toggle its check-in or open its note so that history doubles as an editing tool.
2. Year heatmap
   - As a user, I want a year-long contribution-style heatmap across all habits so that I can see my long-term consistency.
3. Activity log
   - As a user, I want a reverse-chronological log of check-ins with notes, filterable by habit, so that I can review what I wrote.

### Module 7: Data Portability and Settings

1. Export
   - As a user, I want to export all my data (habits, schedules, check-ins, notes, skips, reminders, settings) to a single versioned JSON file so that I own a backup.
   - As a user, I want the file name to include the date so that multiple backups are easy to tell apart.
2. Import
   - As a user, I want to import a previously exported JSON file and see a preview (number of habits and check-ins) before anything changes, so that I do not import the wrong file.
   - As a user, I want to choose between "Replace all data" and "Merge" (merging by habit identity and deduplicating check-ins), so that I can restore or combine data safely.
   - As a user, I want malformed, wrong-version, or non-Cadence files to be rejected with a clear message and no data change, so that a bad file never corrupts my tracker.
3. Settings
   - As a user, I want to choose light, dark, or system theme so that the app is comfortable at any hour.
   - As a user, I want a "Reset all data" action behind a typed confirmation so that I can start over deliberately.
   - As a user, I want to load sample data from the empty state so that I can explore the app before committing.

### Module 8: Onboarding and Accessibility

1. First run
   - As a new user, I want a friendly empty state with a primary "Create your first habit" action and a few one-click templates (Drink water, Read 20 min, Exercise Mon/Wed/Fri, Meditate) so that I can start in under 30 seconds.
   - As a new user, I want a short note explaining that my data stays on this device and how to back it up, so that I trust the app and understand export.
2. Keyboard and screen reader support
   - As a keyboard user, I want every action reachable with Tab, Enter, and Space, and shortcuts such as "n" for new habit and "t" for Today, so that I never need a mouse.
   - As a screen reader user, I want check controls to announce habit name, state, and streak, and calendar days to announce their date and status, so that the app is fully usable without sight.
3. Responsive layout
   - As a phone-browser user, I want the layout to collapse to a single column with a bottom navigation bar so that the app works on a small screen.

## AI Integration (On-Device Intelligence)

Cadence has no network access and no model inference, so its "intelligent" features are deterministic algorithms over the user's own history. They must be explainable: each suggestion shows the reason behind it.

1. Quick Add Parser. A single text field on the Today screen understands phrases like "Read 20 minutes every weekday at 9pm", "Gym mon wed fri 7am", or "Stretch daily". It extracts the habit name, schedule (daily, weekdays, weekends, or named days), and reminder time, then shows the parsed result as a pre-filled form for confirmation. Value: creating a habit becomes one sentence.
   - As a user, I want to type a habit in plain English and see the parsed name, days, and time before saving so that I can add habits faster than filling a form.
   - As a user, I want unrecognized parts to stay in the name field rather than be guessed, so that the parser never invents a schedule.
2. Smart Reminder Timing. After a habit has at least 7 timestamped check-ins, Cadence computes the typical time of day the user completes it and suggests a reminder 30 minutes earlier (for example, "You usually check this in around 8:10 pm. Remind at 7:40 pm?"). Value: reminders match real behavior instead of guesses.
   - As a user, I want a suggested reminder time based on when I actually complete the habit so that reminders land when they help.
   - As a user, I want to accept or dismiss each suggestion, and dismissed suggestions do not return for that habit for 30 days.
3. Streak-at-Risk Alerts. In the evening (default 8 pm, configurable), if a habit with a current streak of 3 or more is scheduled today and not yet done, the Today view highlights it with a "Streak at risk" badge, and, if reminders are enabled, one extra reminder fires. Value: protects the streaks users care about most.
   - As a user, I want habits with a streak on the line to be highlighted late in the day so that I do not lose a long streak by forgetting.
4. Weekly Insights. A dashboard card summarizes the last 7 days in generated plain sentences: the most consistent habit, the habit that slipped most compared to the prior week, the weekday with the lowest completion rate, and one actionable suggestion (for example, "Thursdays are your weakest day; consider moving 'Gym' from Thursday to Friday"). Value: turns raw data into a weekly review without manual analysis.
   - As a user, I want a short weekly summary of my strongest and weakest habits and days so that I know what to adjust.
   - As a user, I want each insight to link to the habit or calendar it refers to so that I can verify it.
5. Schedule Fit Suggestions. If a habit's completion rate on one scheduled weekday is below 40% over at least 4 occurrences while other days exceed 70%, Cadence suggests removing or swapping that day. Value: helps users design schedules they can keep.

## Visual Design Language

- Mood: calm, encouraging, and tactile. The app should feel like a well-made paper planner with a satisfying physical check-off, not a gamified dashboard. Friendly but grown-up; celebration is brief and tasteful.
- Color: warm off-white canvas (around #FAF8F5) with deep ink text (around #1F2328) in light mode; dark mode uses a soft charcoal canvas (around #16181C) with warm light text. A single primary accent in a confident teal-green signals completion and progress. Each habit carries a user-chosen color from a curated palette of 10 muted, accessible hues (coral, amber, olive, teal, sky, indigo, plum, rose, slate, sand) used for its card edge, calendar fills, and heatmap. Streak flames and milestone badges use a warm amber. Missed days use a neutral gray, never alarming red; "at risk" uses amber outline. All text and state colors meet WCAG AA contrast in both themes, and status is never conveyed by color alone (icons and labels accompany every state).
- Typography: a rounded humanist sans-serif for UI text, with tabular numerals for streak counts and statistics. Streak numbers are displayed large (around 32 to 40 px) and bold as the visual hero of each habit card. Body text 15 to 16 px; generous line height.
- Layout and density: medium-low density. Desktop uses a left navigation rail (Today, Habits, Calendar, Insights, Settings) and a centered content column of about 720 px; mobile uses a bottom tab bar. Habit cards have 12 px rounded corners, soft shadows, and roomy 16 to 20 px padding. Calendars use rounded day cells with filled circles for completions, hollow rings for scheduled but missed days, a diagonal hatch for excused skips, and a small dot for bonus completions.
- Motion: purposeful and quick (150 to 250 ms). The check control fills with the habit color in a springy circle animation; the streak number ticks up; completing the full day triggers a short confetti burst from the progress ring. Banners slide down from the top. All motion respects the reduced-motion preference by switching to simple fades.
- UX philosophy: one tap to log, zero surprises. Destructive actions confirm; every check is undoable; data ownership is stated plainly. Empty states teach rather than scold.

## Sprint Plan

Each sprint ends in a runnable app (`npm install` then `npm run dev` or `npm run build && npm run preview` on Node 22) and a passing Playwright suite covering that sprint's criteria plus all earlier sprints' criteria. Unit tests for pure logic (streaks, schedules, parsing, import validation) are expected alongside.

### Sprint 1: Foundation, Habits, Schedules, and Persistence

Theme: stand up the project and make habits real, durable objects.

Deliverables:
- Vite project with TypeScript (vanilla or React), scripts `dev`, `build`, `preview`, `test` (unit), and `test:e2e` (Playwright), runnable on Node 22 with no external services.
- App shell with navigation (Today, Habits, Calendar, Insights, Settings placeholders), light and dark theme following the system preference, responsive layout.
- Local persistence layer (IndexedDB for domain data, localStorage acceptable for preferences) with a versioned data model.
- Habit CRUD: create, edit, archive, restore, delete with confirmation; name validation; color and emoji; start date; time-of-day grouping; reorder.
- Schedules: daily and specific weekdays, with plain-language schedule labels; at least one day required.
- Empty-state onboarding with templates and "load sample data".
- A documented, test-controllable notion of "today" (Playwright clock control or a developer override).

Pass/fail criteria:
- PASS if `npm run dev` and `npm run preview` both serve the app on Node 22 and the browser makes no network requests other than to the local server.
- PASS if a Playwright test can create a habit, reload the page, and still see it with the same name, color, and schedule.
- PASS if submitting an empty name or a weekday schedule with no days shows an inline error and creates nothing.
- PASS if editing a habit's name and schedule persists after reload; archiving removes it from the active list and restoring brings it back; deleting requires confirmation and removes it permanently.
- PASS if schedule labels read "Every day" for daily and list chosen days (for example "Mon, Wed, Fri") for weekday schedules.
- PASS if choosing a template creates a correctly scheduled habit in one click.
- FAIL if any data is lost on reload, any console error appears during the core flows, or the app requires an account or API key.

### Sprint 2: Check-ins, Schedule-Aware Streaks, and Statistics

Theme: the core daily loop and streaks users can trust.

Deliverables:
- Today view showing habits scheduled today grouped by time of day, a toggle to show unscheduled habits, one-tap check and uncheck, an Undo toast, daily progress count and ring, full-day celebration.
- Check-in notes and excused skip days.
- Backfill for past dates via a per-habit date picker or day list (future dates locked).
- Streak engine as a pure, unit-tested module: current streak and longest streak computed over scheduled days only, today pending until the day ends, bonus completions on unscheduled days not affecting streaks, excused skips passed over, schedule changes applying from today forward, nothing counted before the start date.
- Statistics: 7-day, 30-day, and all-time completion rates against scheduled days; total completions; dashboard summary.
- Milestone badges and milestone toast.

Pass/fail criteria:
- PASS if, for a Mon/Wed/Fri habit completed on Monday, Wednesday, and Friday of one week, the current streak shows 3 when viewed on the following Saturday, Sunday, or Monday morning before checking in.
- PASS if missing a scheduled Wednesday resets the current streak to 0 after that Wednesday ends, while the longest streak keeps its prior maximum.
- PASS if an unchecked habit scheduled today does not reset the current streak during today; it shows yesterday's streak value.
- PASS if a check-in on an unscheduled day is shown as a bonus and does not change the current streak number.
- PASS if marking a scheduled day as excused skip keeps the streak intact across it without adding 1.
- PASS if a 7-day completion rate for a daily habit with 5 of 7 days done displays 71% (rounded), and a Mon/Wed/Fri habit with 3 of 3 done displays 100%.
- PASS if Undo after a check restores the prior state and both actions persist correctly after reload.
- PASS if future dates cannot be checked in.
- PASS if the streak engine unit tests cover all rules above and pass.
- FAIL if any streak value depends on unscheduled days, or if check-in state is lost on reload.

### Sprint 3: Reminders with Notification Fallback

Theme: timely nudges that work whether or not notifications are allowed.

Deliverables:
- Per-habit reminder times (zero or more) in the habit form.
- Reminder scheduler running while the app is open: fires only on scheduled days, only when the habit is not completed, at most once per habit per time per day (deduplicated across reloads), with catch-up delivery for reminders that came due while the tab was hidden or asleep.
- Notification permission requested only when the first reminder is added; permission status shown in Settings with guidance.
- In-app fallback banner when permission is denied, not granted, or the API is unsupported: stacked list of due habits with "Mark done", "Snooze 10 min", and "Dismiss".
- Clicking a system notification focuses the app on the relevant habit.
- Global pause and quiet hours.
- Streak-at-risk badge and optional evening reminder (on-device intelligence feature 3).

Pass/fail criteria:
- PASS if, with notification permission granted in Playwright and the clock advanced past a reminder time on a scheduled day for an incomplete habit, exactly one notification is created for that habit.
- PASS if, with permission denied, the same scenario shows the in-app banner naming the habit, and "Mark done" checks the habit in and removes it from the banner.
- PASS if "Snooze 10 min" hides the banner entry and it reappears after the clock advances 10 minutes.
- PASS if no reminder fires on an unscheduled day, for an already-completed habit, while paused, or during quiet hours.
- PASS if reloading the page after a reminder fired does not fire it again that day.
- PASS if two habits due at the same time produce one banner listing both.
- PASS if the first page load does not trigger a permission prompt.
- PASS if a habit with a streak of 3 or more, scheduled and not done after the at-risk hour, shows a "Streak at risk" badge.
- FAIL if any reminder is duplicated, fires for a completed habit, or is silently dropped when permission is denied.

### Sprint 4: History, Calendar, Import/Export, Intelligence, and Polish

Theme: look back, own your data, and get smarter suggestions.

Deliverables:
- Per-habit month calendar with day states (completed, missed, excused, unscheduled, bonus, future, before start), month navigation, "Today" jump, and click-to-edit past days.
- Year heatmap across all habits and a filterable activity log with notes.
- Export of all data to a versioned, dated JSON file.
- Import with preview, "Replace" and "Merge" modes, deduplication, schema and version validation, and no change on failure.
- Settings: theme choice, week start (Monday or Sunday), reset all data with typed confirmation.
- On-device intelligence: Quick Add parser, Smart Reminder Timing suggestions, Weekly Insights card, Schedule Fit suggestions, each showing the reason for its suggestion.
- Accessibility and polish pass: keyboard shortcuts, screen reader labels, reduced-motion support, AA contrast in both themes, mobile bottom navigation.

Pass/fail criteria:
- PASS if a habit's calendar marks a completed scheduled day, a missed scheduled day, an unscheduled day, an excused day, and a bonus day each with a distinct visual and accessible label, and clicking a past day toggles its check-in and updates the streak.
- PASS if exporting, resetting all data, and importing the exported file in "Replace" mode restores identical habits, check-ins, notes, and streak values.
- PASS if importing the same file in "Merge" mode creates no duplicate habits or check-ins.
- PASS if importing invalid JSON, a non-Cadence file, or an unsupported version shows an error and leaves existing data unchanged.
- PASS if Quick Add turns "Gym mon wed fri 7am" into a habit named "Gym" scheduled Monday, Wednesday, Friday with a 07:00 reminder after user confirmation, and "Stretch daily" into a daily habit named "Stretch".
- PASS if, after 7 or more check-ins clustered around one time, the habit shows a reminder suggestion with its reasoning, and accepting it adds the reminder.
- PASS if the Weekly Insights card names the most consistent habit correctly for seeded data.
- PASS if switching week start to Sunday reorders the calendar and weekday picker.
- PASS if all core flows (create, check in, open calendar, export) are completable using only the keyboard, and an automated accessibility scan of the main screens reports no critical violations.
- FAIL if import can partially corrupt data, any calendar state is conveyed by color alone, or any feature makes a network request.
