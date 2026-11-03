APPROVED

# Sprint 4 Contract

## Scope

All Sprint 4 features from the spec, plus one Sprint 3 hardening item:

1. Per-habit month calendar (eight day states, month navigation, "Today" jump, click-to-edit past days)
2. Year heatmap across all habits
3. Filterable activity log with notes
4. Export of all data to a versioned, dated JSON file
5. Import with preview, "Replace all data" and "Merge" modes, deduplication, schema and version validation, and no change on failure
6. Settings: theme choice (System, Light, Dark), week start (Monday or Sunday), reset all data with typed confirmation
7. On-device intelligence, each with a visible reason: Quick Add parser, Smart Reminder Timing, Weekly Insights card, Schedule Fit suggestions
8. Accessibility and polish pass: keyboard shortcuts, screen reader labels, reduced motion, AA contrast in both themes, mobile bottom navigation
9. Hardening: a reminder is never claimed without either a shown notification or a stored banner entry (atomic or ordered delivery)

Sprint 1 to 3 behavior is unchanged except where this contract says otherwise. Allowed edits to earlier e2e tests are limited to text this contract changes: the Calendar and Settings "Coming soon" placeholders disappear, and the empty-state privacy note no longer says export is "coming" (it must say the data stays on this device and that "Export data" in Settings creates a backup).

## Deliverables

- Routes (hash): `#/calendar` (Month tab), `#/calendar/year` (Year tab), `#/calendar/log` (Activity log tab). The Month tab accepts `?habit=<habit id>&month=YYYY-MM` after the hash path, for example `#/calendar?habit=h2&month=2026-03`.
- Calendar page: tablist named "Calendar views" with tabs "Month", "Year", "Activity log" (`aria-selected`).
- Settings page sections, in order: Theme, Week start, Notifications, Reminder controls, Streak at risk, Data (Export data, Import data file), Keyboard shortcuts, Reset all data.
- Today page: a text field named "Quick add a habit" with a button "Preview habit" (always shown, including in the empty state).
- Habits page cards: `reminder-suggestion` and `schedule-fit-suggestion` regions when applicable, and a link named `Calendar for <habit>` to `#/calendar?habit=<id>`.
- Insights page: a "Weekly insights" card (`weekly-insights`) below the existing dashboard.
- Keyboard shortcuts dialog (`role=dialog`, named "Keyboard shortcuts").
- Skip link "Skip to main content", landmark roles, per-route page titles.
- Export file format version 1 (defined below) and import validation messages (defined below).
- Unit tests for every pure rule in this contract. README section documenting the export format, shortcuts, and the new test identifiers.
- Test fixtures under `e2e/fixtures/` generated from the dataset definitions below.

### Export file format, version 1

File name: `cadence-backup-YYYY-MM-DD.json`, where the date is the app's "today" (the `?now=` override when present). Content is pretty-printed JSON, 2-space indent, UTF-8. Two exports taken with the same clock and the same data are byte-identical.

```json
{
  "format": "cadence-export",
  "version": 1,
  "exportedAt": "2026-03-04T09:00:00",
  "habits": [
    {
      "id": "h2", "name": "Gym", "description": "Lift", "color": "coral", "emoji": "🏋️",
      "startDate": "2026-03-01", "timeOfDay": "evening",
      "schedule": { "type": "weekdays", "days": [0, 2, 4] },
      "scheduleHistory": [ { "from": "2026-03-01", "schedule": { "type": "daily" } } ],
      "reminders": ["18:30"], "archived": false, "order": 1,
      "createdAt": "2026-03-01T08:01:00Z"
    }
  ],
  "checkins": [
    { "habitId": "h2", "date": "2026-03-02", "kind": "done", "note": "", "checkedAt": "2026-03-02T18:45:00" }
  ],
  "settings": {
    "theme": "dark",
    "weekStart": "sunday",
    "remindersPaused": false,
    "quietHours": { "enabled": true, "start": "22:00", "end": "07:00" },
    "streakAtRisk": { "hour": 21, "reminder": true }
  },
  "suggestionDismissals": [ { "habitId": "h3", "dismissedOn": "2026-03-01" } ]
}
```

- `exportedAt` and `checkedAt` are local wall-clock strings `YYYY-MM-DDTHH:mm:ss` read from the app clock, with no zone. `checkedAt` is the moment a done check-in was created through a check action. It is `null` for skips and for records that never had one (all Sprint 2 data, imported data without it).
- `schedule.days` use 0 = Monday through 6 = Sunday, independent of the week-start setting. `reminders` is a list of `HH:mm` strings (no delivery state, no banner entries, no claim records are exported).
- Habits are sorted by `order` ascending. Check-ins are sorted by `date` ascending, then `habitId` ascending (plain string comparison). Optional on import: `description` (default ""), `emoji` (default "✅"), `scheduleHistory` (default []), `reminders` (default []), `createdAt` (default the import moment), `checkedAt` (default null), `note` (default ""), `suggestionDismissals` (default []), and any `settings` key (default is the fresh-install value). Unknown extra keys are ignored.
- A done check-in gets `checkedAt` = the app clock at the moment of the check, on every path that creates a done check-in (Today check, banner "Mark done", History dialog, calendar click). Un-checking removes it; Undo restores the previous value; editing a note keeps it.
- Imported reminder times are treated as added at the import moment, so importing never delivers a reminder for a time that already passed.

### Import validation messages (exact text, shown in an element with `role=alert` and `data-testid="import-error"`; no data changes)

| Case | Message |
|------|---------|
| Not parseable JSON, including an empty file | `This file is not valid JSON. Nothing was imported.` |
| Valid JSON but not an object, or `format` is not "cadence-export" | `This file is not a Cadence export. Nothing was imported.` |
| `format` is right, `version` absent | `This export has no version number, which this app cannot read (supported: 1). Nothing was imported.` |
| `format` is right, `version` is anything other than the number 1 (value shown as JSON, e.g. `2` or `"1"`) | `This export uses version 2, which this app cannot read (supported: 1). Nothing was imported.` |
| Right format and version, a structural problem | `This export is damaged: <reason>. Nothing was imported.` |

Damaged reasons use zero-based indexes; only the first problem is reported, checking habits in list order (fields in the order listed), then check-ins in list order, then settings, then dismissals:

- `habits is missing or not a list`, `checkins is missing or not a list`, `settings is missing or not an object`
- `habits[i] is not an object`, `habits[i].id is missing`, `habits[i].id duplicates habits[j].id`, `habits[i].name is empty` (name is trimmed, 1 to 60 characters), `habits[i].color is invalid` (one of the 10 palette ids), `habits[i].startDate is not a valid date`, `habits[i].timeOfDay is invalid`, `habits[i].schedule is invalid` (daily, or weekdays with a non-empty list of distinct integers 0 to 6), `habits[i].scheduleHistory is invalid`, `habits[i].reminders is invalid` (each `HH:mm`, distinct, at most 5), `habits[i].archived is not true or false`, `habits[i].order is not a number`
- `checkins[j] is not an object`, `checkins[j] refers to an unknown habit`, `checkins[j].date is not a valid date`, `checkins[j].kind is invalid` (done or skip), `checkins[j].note is too long` (over 200 characters), `checkins[j].checkedAt is invalid`, `checkins[j].date is before the habit's start date`, `checkins[j].date is in the future` (after the app's today), `checkins[j] duplicates checkins[k]` (same habit and date)
- `settings.<key> is invalid` for a present known key with a bad value; `suggestionDismissals[i] is invalid` (bad date or habit id not in the file)
- A skip record with a non-empty note is accepted and its note is stored as empty.

### Merge rules (exact)

1. Habit identity is the `id`. A file habit whose id does not exist locally is added with its file data, and gets `order` values after all existing habits, keeping the file's relative order by (`order`, file position) (in the MERGE fixture: h5 -> 4, x6 -> 5). Names are never compared: a file habit named "Gym" with a new id is added next to an existing "Gym".
2. A file habit whose id exists locally is not changed in any field (local wins: name, schedule, reminders, archived flag, order, color).
3. A file check-in (habit id + date) that does not exist locally is added. A file check-in whose habit id + date already exists locally is left unchanged, whether or not kind or note differ (local wins).
4. Local settings are not changed by Merge. Suggestion dismissals are unioned; for the same habit the later `dismissedOn` is kept.
5. Merge and Replace validate the whole file first, then apply all changes as one all-or-nothing write. A failure at any point leaves every store untouched.
6. Replace deletes all local habits, check-ins, reminder claim records, banner entries, and dismissals, then loads the file. Settings come from the file (missing keys take defaults) and apply immediately.

### Import UI

- File input with accessible name "Import data file" (keyboard operable). Choosing a file shows a region named "Import preview" (or the error above), never both. Choosing another file replaces the previous result.
- Preview shows `preview-exported` (`Exported: 2026-03-04T09:00:00`), `preview-habits` (`Habits: 4`), `preview-checkins` (`Check-ins: 9`, counts every record, done and skip).
- Singular/plural rule for every count-bearing message below: a noun is singular only when its count is exactly 1; 0 and 2 or more are plural ("0 new habits").
- Radiogroup "Import mode": "Replace all data" and "Merge" (default "Merge"). With Merge selected, `preview-merge` shows `Merge would add {A} new {habit|habits} and {B} new {check-in|check-ins}; {C} {check-in already exists|check-ins already exist} and would be left unchanged.`
  - Plural example (A=2, B=3, C=2): `Merge would add 2 new habits and 3 new check-ins; 2 check-ins already exist and would be left unchanged.`
  - Singular example (A=1, B=1, C=1): `Merge would add 1 new habit and 1 new check-in; 1 check-in already exists and would be left unchanged.`
  - Zero example (A=0, B=0, C=1): `Merge would add 0 new habits and 0 new check-ins; 1 check-in already exists and would be left unchanged.`
- Buttons "Import" and "Cancel import". "Import" with Replace opens an `alertdialog` titled "Replace all data?" with the text `This deletes your current {N} {habit|habits} and {M} {check-in|check-ins} and replaces them with the contents of the file.` (current counts; plural e.g. `This deletes your current 4 habits and 9 check-ins and replaces them with the contents of the file.`; singular e.g. `...your current 1 habit and 1 check-in and replaces them...`) and buttons "Cancel" and "Confirm replace". Merge applies immediately.
- Success, in `import-result` (`role=status`); the preview closes:
  - Replace: `Replaced all data: {N} {habit|habits} and {M} {check-in|check-ins} imported.` (e.g. `Replaced all data: 1 habit and 1 check-in imported.`; `Replaced all data: 3 habits and 5 check-ins imported.`)
  - Merge: `Merged: {A} new {habit|habits} and {B} new {check-in|check-ins} added; {C} {check-in already existed and was|check-ins already existed and were} left unchanged.` Plural: `Merged: 2 new habits and 3 new check-ins added; 2 check-ins already existed and were left unchanged.` Singular: `Merged: 1 new habit and 1 new check-in added; 1 check-in already existed and was left unchanged.`
- Export: button "Export data". On click a file download starts and `export-status` (`role=status`) reads `Exported {N} {habit|habits} and {M} {check-in|check-ins} to cadence-backup-YYYY-MM-DD.json.` (e.g. `Exported 4 habits and 9 check-ins to cadence-backup-2026-03-04.json.`; `Exported 1 habit and 1 check-in to cadence-backup-2026-03-04.json.`). Export makes no network request.
- Ordering rule: habits with equal `order` values keep their file-list order; `order` values are stored as given on Replace.

### Reset, theme, week start

- "Reset all data" opens an `alertdialog` "Reset all data?" with a text field labeled "Type RESET to confirm", a "Cancel" button, and a "Reset everything" button that stays disabled until the field equals `RESET` exactly (case-sensitive). Confirming deletes all habits, check-ins, reminder state, dismissals, and settings (back to fresh-install defaults), shows status `All data was reset.`, and Today shows the empty state. An export taken right after a reset equals an export from a fresh browser context (apart from `exportedAt`).
- Radiogroup "Theme": "System" (default), "Light", "Dark". Applies immediately and on first paint after reload. `theme-status` reads `Following your system: currently light.` (or dark) for System, and `Using the dark theme.` (or light) when forced.
- Radiogroup "Week starts on": "Monday" (default), "Sunday". Affects the order of the weekday picker in the habit form, the weekday header and padding of the month calendar, and the rows of the heatmap. It does not change schedule labels (always Mon first, e.g. "Mon, Wed, Fri"), streaks, or stats.

### Calendar day states (Month tab)

Month grid, 7 columns, week start per setting, leading padding cells (`calendar-pad`, `aria-hidden`) up to the first weekday. Each date is one `button` with `data-testid="calendar-day"`, `data-date`, `data-state`, `data-shape`, `data-today` (`true` on today), `data-has-note`.

| `data-state` | When | Accessible label suffix | `data-shape` |
|---|---|---|---|
| `completed` | done on a scheduled day | `Completed` | `filled-check` |
| `missed` | scheduled, past, nothing logged | `Missed` | `ring` |
| `excused` | excused skip | `Excused skip` | `hatch` |
| `unscheduled` | not scheduled, nothing logged | `Not scheduled` | `none` |
| `bonus` | done on an unscheduled day | `Bonus completion` | `dot` |
| `future` | after today | `Future` | `faint` |
| `before-start` | before the habit's start date | `Before start` | `dash` |
| `today` | today, scheduled, not done and not skipped | `Today, not done yet` | `dashed-ring` |

Accessible name of each day: `<Weekday>, <D> <Month> <YYYY>: <suffix>` (same long-date style as the Today heading, e.g. `Wednesday, 4 March 2026: Completed`), with `, has note` appended for done days that carry a note. Today that is done shows `Completed`. A legend (`calendar-legend`) lists all eight states with their shapes and labels as visible text. Future and before-start days have `aria-disabled="true"`.

Header: habit select labeled "Habit" (all habits in Habits-page order, archived ones labeled "<name> (archived)"; default the first active habit), `calendar-month` heading (`March 2026`), buttons "Previous month", "Next month", "Today". "Previous month" is disabled when the displayed month is the month before the habit's start month (one fully before-start month stays browsable); "Next month" is disabled in the current month; "Today" jumps to the current month and is disabled there. A `month` query value outside [month before start month, current month], or not in YYYY-MM form, is clamped to that range (invalid form: current month). Above the grid: `streak-current` and `streak-longest` for the selected habit (text is the bare integer).

Interaction (days from the start date through today): clicking a day selects it and shows `calendar-day-detail` (date, status text `calendar-day-status`, note text `calendar-note-text` when present). Clicking toggles done and cleared for `completed`, `missed`, `today`, `unscheduled`, `bonus` days (clearing removes the note, as in Sprint 2). Clicking an `excused` day only selects it. The detail panel offers, with the same labels and rules as the History dialog: `Skip <habit> on YYYY-MM-DD` / its "Clear skip" state, and for done days `Note for <habit> on YYYY-MM-DD` (inline editor with "Save note" and "Cancel", 200 characters). Clicking a future or before-start day changes nothing and shows no panel. No Undo or milestone toasts from the calendar.

### Heatmap (Year tab)

53 week columns ending with the current week, 7 rows, week start per setting: always exactly 371 cells (`heatmap-cell`, with `data-date`, `data-level`), in DOM order oldest to newest. For each date, over active (non-archived) habits only: S = habits scheduled that day, on or after their start date, not excused-skipped; D = those of them with a done check-in. Today counts as it stands (no pending exclusion). Bonus check-ins on unscheduled days are ignored.

| `data-level` | Rule |
|---|---|
| `none` | S = 0, or the date is before every habit's start date |
| `future` | after today |
| `0` | S > 0 and D = 0 |
| `1` | D > 0 and D/S < 0.5 |
| `2` | 0.5 <= D/S < 0.75 |
| `3` | 0.75 <= D/S < 1 |
| `4` | D = S |

Cell accessible name (`role=img`): `<Weekday>, <D> <Month> <YYYY>: <D> of <S> scheduled habit(s) done` (singular "habit" only when S is 1), `...: No habits scheduled` for `none`, `...: Future` for `future`. Month labels above the first column of each month, weekday labels at the left, a legend "Less" to "More" with the five filled levels. The cell scroll container is focusable, named "Year heatmap", scrolled so the current week is visible on load, and uses the accent teal at different intensities (level 0 is a bordered empty cell, not a color fill).

### Activity log (Activity log tab)

Rows (`log-row`, with `data-date`) for every done check-in of every habit, archived included (skips are not listed), newest date first; same date ordered by Habits-page order. Each row: emoji, habit name (`log-habit`), date `YYYY-MM-DD` (`log-date`), note (`log-note`, absent when empty). Controls: select "Filter by habit" ("All habits" first, then every habit, archived ones labeled "<name> (archived)"), checkbox "Only check-ins with notes". `log-count` reads `8 check-ins` (`1 check-in` when one). 50 rows at a time with a "Show 50 more" button. Empty result: `No check-ins to show.`

### Quick Add parser (Today)

Typing a sentence and pressing Enter in "Quick add a habit", or clicking "Preview habit", opens the existing "New habit" form pre-filled with name, schedule, and reminder time; nothing is saved until the user presses the form's Save. Above the fields, `quickadd-explain` lists the reasons, one line each: `Name: Gym`, `Days: Mon, Wed, Fri (from "mon wed fri")`, `Reminder: 07:00 (from "7am")`; when no schedule words were found: `Days: Every day (no days recognized)`; when no time: `Reminder: none`. An empty or whitespace-only field shows the `role=alert` text `Type a habit first, for example "Gym mon wed fri 7am".` and opens nothing. Format rule for `quickadd-explain` (applies to all parses): the quoted text in `(from "...")` is the consumed schedule tokens (including consumed `every`/`on`, with connectors `and`, `&`, and commas removed from word ends) in input order, original casing, joined by single spaces; for the time it is the consumed time tokens including a consumed `at`. Lines are `Name: <name>` (empty name: `Name: (empty)`); `Days: <label> (from "<quote>")` or `Days: Every day (no days recognized)`; `Reminder: <HH:mm> (from "<quote>")` or `Reminder: none`. In the required-parses list below, "Every day (none recognized)" is shorthand for the line `Days: Every day (no days recognized)`. Examples: parse 3 -> `Name: Read 20 minutes`, `Days: Mon, Tue, Wed, Thu, Fri (from "every weekday")`, `Reminder: 21:00 (from "at 9pm")`; parse 4 -> `Days: Sun (from "on sunday")`, `Reminder: 18:30 (from "at 6:30 pm")`; parse 11 -> `Days: Mon, Wed, Fri (from "mon wed and fri")`; parse 15 -> `Name: GYM`, `Days: Mon, Wed, Fri (from "MON WED FRI")`, `Reminder: 07:00 (from "7AM")`; parse 17 -> `Name: (empty)`, `Days: Every day (from "daily")`, `Reminder: 07:00 (from "7am")`; parse 18 -> `Days: Mon (from "every mon")`, `Reminder: 00:00 (from "at 12am")`. Saving a quick-added habit that has a reminder counts as adding the first reminder: if the permission is "Not asked" the permission request happens on that Save (once), never earlier.

Rules (case-insensitive, matching on whole words, trailing commas and periods on a word are treated as separators, runs of spaces collapse):

- Schedule words: `daily`, `everyday`, `every day` mean every day; `weekday`, `weekdays`, `every weekday` mean Mon to Fri; `weekend`, `weekends`, `every weekend` mean Sat and Sun; day words `mon monday tue tues tuesday wed wednesday thu thur thurs thursday fri friday sat saturday sun sunday` and the plurals of the full names (`mondays` ... `sundays`). `every` and `on` are consumed only when directly followed by a schedule word; `and`, `&`, and commas only between two day words.
- Only the first run of consecutive schedule words (with their connectors) is used; the union of its days applies, and `daily` inside it means every day. Later schedule words stay in the name. No schedule words means every day.
- Time: `7am`, `7 am`, `7:30pm`, `7:30 pm`, `19:30`, `07:05`, `noon` (12:00), `midnight` (00:00), optionally preceded by `at` (consumed only when followed by a valid time). 12-hour hours 1 to 12; 24-hour hours 0 to 23, minutes 00 to 59; `12am` is 00:00, `12pm` is 12:00. Bare numbers (`20`) and invalid times (`25:00`, `13pm`) are not times and stay in the name. Only the first time is used; later times stay in the name.
- Everything not consumed, in its original order and casing, joined by single spaces, is the name. Nothing is guessed or invented; an empty name stays empty (Save then shows the existing inline name error).

Required parses (input -> name | days | reminder):

1. `Gym mon wed fri 7am` -> Gym | Mon, Wed, Fri | 07:00
2. `Stretch daily` -> Stretch | Every day | none
3. `Read 20 minutes every weekday at 9pm` -> Read 20 minutes | Mon, Tue, Wed, Thu, Fri | 21:00
4. `Call mom on sunday at 6:30 pm` -> Call mom | Sun | 18:30
5. `Long run saturdays 8am` -> Long run | Sat | 08:00
6. `Meditate weekends 6:45am` -> Meditate | Sat, Sun | 06:45
7. `Take vitamins 08:00` -> Take vitamins | Every day (none recognized) | 08:00
8. `Drink water` -> Drink water | Every day (none recognized) | none
9. `Read 20 pages` -> Read 20 pages | Every day (none recognized) | none
10. `Journal at noon every day` -> Journal | Every day | 12:00
11. `Review mon, wed and fri` -> Review | Mon, Wed, Fri | none
12. `Gym at 25:00` -> Gym at 25:00 | Every day (none recognized) | none
13. `Yoga 7am 9pm` -> Yoga 9pm | Every day (none recognized) | 07:00
14. `mon wed gym` -> gym | Mon, Wed | none
15. `GYM MON WED FRI 7AM` -> GYM | Mon, Wed, Fri | 07:00
16. `   Stretch    daily  ` -> Stretch | Every day | none
17. `daily 7am` -> (empty name) | Every day | 07:00
18. `Meeting every mon at 12am` -> Meeting | Mon | 00:00

### Smart Reminder Timing (Habits page cards)

- Qualifying check-ins: done check-ins whose `checkedAt` falls on the same date as the check-in `date`, dated within the 60 days up to and including today. Backfilled records, records without `checkedAt`, and skips never qualify.
- At least 7 qualifying check-ins are needed. Typical time = the median minute-of-day of the qualifying check-ins (for an even count, the average of the two middle values, rounded down to the minute). Suggested time = typical time minus 30 minutes; if that is before 00:00 no suggestion is shown.
- Not shown when the habit is archived, already has 5 reminders, or already has a reminder within 30 minutes (inclusive) of the suggested time, or the suggestion was dismissed less than 30 days ago (dismissed on D: hidden on D through D+29, shown again on D+30).
- Region `reminder-suggestion` (inside the habit's card) with text exactly `You usually check this in around 8:10 pm (based on 8 check-ins in the last 60 days). Remind at 7:40 pm?` (12-hour `h:mm am/pm`, lowercase), `data-time="19:40"`, and buttons `Accept reminder suggestion: <habit>` and `Dismiss reminder suggestion: <habit>`. Accept adds that reminder exactly as the form would (card line `Reminders: ...`, same permission rule as "Add reminder": requested once if "Not asked") and the suggestion disappears. Dismiss hides it and records the dismissal date, persisting across reloads and in exports.

### Schedule Fit suggestions (Habits page cards)

For each active habit, over the dates from max(start date, today minus 83 days) through yesterday, plus today if the habit is already done today (scheduled days only, using the schedule in force on each date; excused skips excluded): for each scheduled weekday W, n = scheduled occurrences, d = done. W is weak when n >= 4 and d/n < 0.40 (exclusive) and the pooled rate over all other scheduled weekdays of the habit is greater than 70% (exclusive, needs at least one other evaluated day). If several weekdays are weak, the lowest rate wins; ties go to the earlier weekday (Mon first). `schedule-fit-suggestion` text: `Thursdays are your weak spot for Gym: 1 of 8 done (13%), while your other days are at 100%. Consider removing Thursday or swapping it for another day.` (percentages rounded half up). Button `Adjust schedule for <habit>` opens that habit's edit form. No suggestion for a habit with a single scheduled weekday.

### Weekly Insights (Insights page)

Window W = the 7 days ending today (today minus 6 through today); prior window P = the 7 days before that. Rates use the existing completion-rate rules (scheduled days only, excused skips and a still-pending today excluded, rounded half up), over active habits. `weekly-insights-range` reads `Last 7 days: 2026-03-02 to 2026-03-08`. Four items, each a `weekly-insight` with a link:

1. `insight-consistent`: among habits with at least 3 evaluated days in W, the highest rate (ties: more done days, then Habits-page order). `Most consistent: Read at 100% (7 of 7 scheduled days).` Link `View calendar for Read` -> `#/calendar?habit=<id>`. None qualifying: `Not enough scheduled days this week to pick a most consistent habit.` (no link).
2. `insight-slipped`: among habits with at least 3 evaluated days in both W and P, the largest drop of rounded rate (P minus W) that is at least 15 points (ties: Habits-page order). `Slipped most: Gym fell from 100% to 67% compared with the prior week.` Link `View calendar for Gym`. None: `No habit slipped compared with the prior week.`
3. `insight-weakest-day`: pooled over active habits per day of W (done over evaluated), the lowest rate among days with evaluated habits (ties: the earlier date). `Weakest day: Thursday at 33% (1 of 3 scheduled check-ins).` (`check-in` singular when the denominator is 1: `1 of 1 scheduled check-in`) Link `View year heatmap` -> `#/calendar/year`. None: `No scheduled habits this week.`
4. `insight-suggestion`, first match wins: (a) any active habit with a Schedule Fit suggestion (first in Habits-page order): `Suggestion: <the habit's Schedule Fit sentence>` with link `Adjust schedule for <habit>` opening the Habits page edit form for it; (b) a slipped habit from item 2: `Suggestion: Gym slipped this week. Open its calendar to see which days were missed.` with link `See Gym's missed days` -> its calendar; (c) a weakest day below 100%: `Suggestion: Thursday is your weakest day. Consider an extra reminder on Thursdays.` with link `View year heatmap`; (d) otherwise `Suggestion: Everything scheduled was done. Keep your current schedule.` (no link).

With no active habits the card reads `Add a habit to see your weekly insights.` Following a calendar link opens the Month tab on that habit in the current month.

### Keyboard shortcuts, accessibility

- Shortcuts (ignored when Ctrl, Meta, or Alt is held, when focus is in an input, textarea, select, or editable element, and while a dialog is open): `n` opens the New habit form on any page (stays on the page), `t` Today, `h` Habits, `c` Calendar, `i` Insights, `s` Settings, `/` focuses "Quick add a habit" (navigating to Today first), `?` opens "Keyboard shortcuts", which lists every shortcut. Settings has a button "Show keyboard shortcuts" for the same dialog.
- Dialogs: focus moves to the first field or button on open, Tab stays inside, Escape closes, focus returns to the element that opened it (for shortcut-opened dialogs, the page heading).
- On every route change focus moves to the page `h1` and `document.title` becomes `<Page> - Cadence` (Today, Habits, Calendar, Insights, Settings). The first Tab stop on every page is "Skip to main content", which moves focus into `main`. The primary navigation is a `nav` named "Main"; the current page has `aria-current="page"` (rail and bottom bar).
- Check controls keep their name `Check in <habit>` and `aria-pressed`, and gain an accessible description of the form `Not done. Current streak: 3 days.` / `Done. Current streak: 1 day.` / `Skipped (excused). Current streak: 0 days.` (singular "day" only for 1).
- Focus indicator: every interactive element shows an outline of at least 2 px on keyboard focus. Touch targets in the bottom bar are at least 44 px tall.
- Under `prefers-reduced-motion: reduce`, no transform animation runs anywhere (check, dialogs, toasts, banner, month change); motion becomes fades or nothing. Confetti stays hidden.
- Status is never color alone in calendar, heatmap legend, suggestions, or settings states.

### Dataset definitions (for fixtures)

All fixtures are valid export files (version 1). Habit ids as given.

**MAIN** (`?now=2026-03-04T09:00`, Wednesday). Settings: theme dark, weekStart sunday, remindersPaused false, quietHours enabled 22:00 to 07:00, streakAtRisk hour 21 reminder true. Dismissals: h3 on 2026-03-01.
- h1 Water, emoji 💧, teal, daily, morning, start 2026-03-01, order 0
- h2 Gym, 🏋️, coral, Mon/Wed/Fri (days 0,2,4), evening, start 2026-03-01, order 1, description "Lift", reminders ["18:30"], `scheduleHistory` `[]` (the export-format example's `scheduleHistory` entry is illustrative only and must not be used for MAIN, otherwise 2026-03-03 would not be a bonus day)
- h3 Read, 📚, sky, daily, anytime, start 2026-03-01, order 2
- h4 Old habit, 🗃️, slate, daily, anytime, start 2026-02-20, order 3, archived
- Check-ins (9): h4 02-20 done; h1 03-01 done; h3 03-01 done; h1 03-02 done note `2 litres`; h2 03-02 done; h3 03-02 skip; h1 03-03 done; h2 03-03 done note `bonus run` (Tuesday, bonus); h3 03-03 done. `checkedAt`: h4 02-20 21:00:00, h1 03-01 08:00:00, h1 03-02 08:10:00, h2 03-02 18:45:00, h1 03-03 08:05:00, h2 03-03 19:00:00 (all on their own date); h3 records null.
- Expected on 2026-03-04: Water current 3, longest 3; Gym current 1, longest 1; Read current 2, longest 2.

**MERGE** (same clock as MAIN; settings theme light): the `habits` array is in this order [h5, x6, h1]: h5 Stretch (🧘, plum, daily, anytime, start 2026-03-01, order 0); x6 named "Gym" (🏃, olive, daily, evening, start 2026-03-01, order 1); h1 "Water renamed" (same id as MAIN's h1, other fields as MAIN, order 2). Check-ins: h1 03-03 done (identical to local), h1 03-04 done checkedAt 2026-03-04T08:30:00 (new), h1 03-02 done note `different note` (exists locally, differs), h5 03-03 done (new), x6 03-01 done (new). Preview in Merge mode: 2 new habits, 3 new check-ins, 2 already exist.

**CAL** (`?now=2026-03-18T10:00`, Wednesday): one habit c1 "Gym", coral, Mon/Wed/Fri, start 2026-03-04 (Wednesday). Check-ins: 03-04 done, 03-07 done (Saturday, bonus), 03-09 skip, 03-11 done note `5 km`, 03-16 done. Expected March 2026 states: 1,2,3 before-start; 4 completed; 5 not scheduled; 6 missed; 7 bonus; 8 not scheduled; 9 excused; 10 not scheduled; 11 completed with note; 12 not scheduled; 13 missed; 14, 15 not scheduled; 16 completed; 17 not scheduled; 18 today (not done yet); 19 to 31 future. Streaks: current 1, longest 1. After clicking 13 (done): current 3, longest 3.

**WEEK** (`?now=2026-03-08T22:00`, Sunday). Habits in order: Read (daily), Gym (Mon/Wed/Fri), Stretch (daily), Journal (daily); all start 2026-02-02, active. Every scheduled day from 2026-02-02 through 2026-03-08 is done except: Gym misses 2026-03-06; Stretch misses 2026-02-24, 2026-03-04, 2026-03-05; Journal misses 2026-02-25, 2026-02-26, 2026-03-01, 2026-03-04, 2026-03-05. All `checkedAt` null. Expected: window 2026-03-02 to 2026-03-08; Read 7 of 7 (100%), Gym 2 of 3 (67%) vs 3 of 3 prior (100%), Stretch 5 of 7 (71%) vs 6 of 7 prior (86%), Journal 5 of 7 (71%) vs 4 of 7 prior (57%). Per day done/scheduled: Mar 2 4/4, Mar 3 3/3, Mar 4 2/4, Mar 5 1/3, Mar 6 3/4, Mar 7 3/3, Mar 8 3/3. No Schedule Fit suggestion for any habit. Heatmap levels: Mar 2 `4`, Mar 3 `4`, Mar 4 `2`, Mar 5 `1`, Mar 6 `3`, Mar 7 `4`, Mar 8 `4`, Mar 9 `future`, Feb 1 `none`. With Monday start the last cell is 2026-03-08 and the first is 2025-03-03; with Sunday start the first is 2025-03-09 and the last week holds 2026-03-08 followed by six `future` cells.

**FIT-A** (`?now=2026-03-04T09:00`): one habit Gym, Mon to Fri (days 0 to 4), start 2026-01-05; every scheduled day through 2026-03-03 done except all Thursdays except 2026-01-08. Thursdays evaluated: 8, done 1. Suggestion expected: `Thursdays are your weak spot for Gym: 1 of 8 done (13%), while your other days are at 100%. Consider removing Thursday or swapping it for another day.`
**FIT-B** (same clock): Gym Mon to Fri, start 2026-02-09, all done except Thursdays (none done). Thursdays evaluated: 3 (Feb 12, 19, 26). No suggestion.
**FIT-C** (same clock): Gym Mon to Fri, start 2026-01-26, all done except Thursdays, of which exactly 2 of 5 (Jan 29, Feb 5) are done. Thursdays: Jan 29, Feb 5, 12, 19, 26 -> 2 of 5 = 40%, not below 40. No suggestion.

**TIMING** (`?now=2026-03-09T09:00`, Monday): habit t1 "Read", daily, anytime, start 2026-02-27. Done check-ins on 03-01 to 03-08 with `checkedAt` on the same date at 20:10, 20:00, 20:20, 20:10, 19:55, 20:25, 20:10, 20:10 (in date order). Two non-qualifying records: 02-27 done with `checkedAt` 2026-03-08T09:00:00 (backfilled), 02-28 done with `checkedAt` null. Expected: typical time 20:10, suggestion 19:40, "8 check-ins".
**TIMING-6**: as TIMING but only the first six dated check-ins carry a qualifying `checkedAt` (03-07 and 03-08 have null). No suggestion.

## Pass/Fail Criteria

### Functionality (PASS threshold: all core flows work)

Calendar
- [ ] F1 With CAL, the Month tab for "Gym" shows `March 2026` and the eight states on the dates listed in the CAL definition, each with the exact accessible name, distinct `data-state`, and distinct `data-shape`; the legend lists all eight.
- [ ] F2 Clicking March 13 (missed) makes it `completed` and the page's `streak-current` and `streak-longest` change from 1 and 1 to 3 and 3; clicking it again restores `missed` and 1 and 1. Clicking March 5 (not scheduled) makes it `bonus` with the streak values unchanged. The changes persist after reload and appear on the Habits page card.
- [ ] F3 Clicking March 9 (excused) changes nothing and opens its detail panel with the clear-skip control; clicking a future day (March 19) or before-start day (March 2) changes nothing and opens no panel. `Note for Gym on 2026-03-11` shows the note "5 km", can be edited and saved, and the day label keeps ", has note".
- [ ] F4 Month navigation: "Previous month" goes to February 2026 (every day `before-start`) and is disabled there; "Next month" returns; in March "Next month" is disabled and "Today" is disabled; navigating back one month then "Today" returns to March 2026. The URL query (`habit`, `month`) reflects the view and a reload restores it. `#/calendar?habit=c1&month=2025-12` shows February 2026 and `#/calendar?habit=c1&month=2027-01` shows March 2026.
- [ ] F5 Week start Sunday puts Mar 1 in the first column (no padding) with header Sun, Mon, ..., Sat; Monday puts six padding cells before Mar 1 with header Mon ... Sun; the habit form's weekday picker orders its buttons Sun, Mon, Tue, Wed, Thu, Fri, Sat under Sunday and Mon ... Sun under Monday; the heatmap's first cell date follows the week-start values given in WEEK; the setting persists after reload.

Heatmap and log
- [ ] F6 With WEEK on the Year tab: 371 `heatmap-cell` elements in ascending date order, the `data-level` values listed in WEEK, accessible names such as `Thursday, 5 March 2026: 1 of 3 scheduled habits done`, `Sunday, 1 February 2026: No habits scheduled`, `Monday, 9 March 2026: Future`. An archived habit does not affect any level (checked with MAIN: Mar 1, 2 and 3 are `4` with names `2 of 2 scheduled habits done`, Mar 4 is `0` with `0 of 3 scheduled habits done`, Feb 28 is `none`).
- [ ] F7 With MAIN on the Activity log tab: `log-count` is `8 check-ins`; row order is (03-03: Water, Gym, Read), (03-02: Water, Gym), (03-01: Water, Read), (02-20: Old habit); notes show `2 litres` and `bonus run`; filter "Gym" gives 2 rows; "Old habit (archived)" gives 1; "Only check-ins with notes" gives Gym 03-03 then Water 03-02; with "Only check-ins with notes" checked and filter "Gym": 1 row (Gym 2026-03-03), then uncheck it; a filter with no results shows `No check-ins to show.`; the skip on 03-02 for Read is not listed.

Export, reset, import
- [ ] F8 Export downloads `cadence-backup-2026-03-04.json` (with the `?now` of MAIN); the content parses as format version 1 with exactly the MAIN habits, check-ins (9, sorted as specified, `checkedAt` as defined), settings, and dismissals; `export-status` shows `Exported 4 habits and 9 check-ins to cadence-backup-2026-03-04.json.`; two exports in a row are byte-identical; no network request is made.
- [ ] F9 Reset: typing anything but `RESET` (including `reset`) keeps "Reset everything" disabled; "Cancel" changes nothing; `RESET` then confirm empties the app (empty state on Today, no habits on Habits, theme System, week start Monday) and the post-reset export equals one from a fresh context apart from `exportedAt`; the state persists after reload.
- [ ] F10 Round trip: load MAIN via import (Replace), export (E1), reset all data, import E1 with Replace, export again (E2). E1 and E2 are byte-identical, and Today, Habits (names, schedule labels, groups, order, archived section, `Reminders: 18:30`), the dark theme, Sunday week start, streak values (Water 3/3, Gym 1/1, Read 2/2), totals, and the activity log match before and after.
- [ ] F11 Preview: after choosing the MAIN file, "Import preview" shows `Habits: 4`, `Check-ins: 9` and the `Exported:` line, default mode Merge; before pressing "Import" nothing in the app has changed (verified by an unchanged export). "Cancel import" closes the preview with no change.
- [ ] F12 Replace safety: "Import" in Replace mode opens "Replace all data?" with the current counts; "Cancel" keeps the old data and the preview; "Confirm replace" replaces everything and shows the Replace result text.
- [ ] F13 Merge idempotence: after loading MAIN, merging MAIN again shows `preview-merge` as `Merge would add 0 new habits and 0 new check-ins; 9 check-ins already exist and would be left unchanged.`, the result text `Merged: 0 new habits and 0 new check-ins added; 9 check-ins already existed and were left unchanged.`, and the export is byte-identical before and after.
- [ ] F14 Merge rules: after loading MAIN, merging MERGE shows the preview and result texts defined in Import UI (2 new habits, 3 new check-ins, 2 existing); then Water keeps its name "Water" (not renamed), its 03-02 note stays `2 litres`, a new check-in on 03-04 makes Water's streak 4 and sets it done on Today, "Stretch" and a second "Gym" appear on the Habits page after the existing four (order 4 then 5), the theme stays dark and week start Sunday, and the total number of habits is 6.
- [ ] F15 Rejection: for each of the invalid inputs in the table (empty file, `{not json`, `[]`, `{"hello":"world"}`, wrong format value, version absent, version 2, version `"1"`) and for the damaged files D1 to D9 below, the exact message appears in `import-error`, no preview or result appears, and an export taken afterwards is byte-identical to the export taken before (with data loaded from MAIN). Importing a valid file after a rejected one works. Each damaged file is the MAIN file with exactly these edits (MAIN's Gym `scheduleHistory` is `[]`). D1: set `checkins[0].habitId` to "zz" -> `This export is damaged: checkins[0] refers to an unknown habit. Nothing was imported.` D2: set `habits[1].name` to "" -> `habits[1].name is empty`. D3: set `habits[0].startDate` to "2026-02-30" -> `habits[0].startDate is not a valid date`. D4: set `habits[0].schedule` to `{"type":"weekdays","days":[]}` -> `habits[0].schedule is invalid`. D5: set `habits[1].id` to "h1" -> `habits[1].id duplicates habits[0].id`. D6: set `checkins[1].habitId` to "h4" and `checkins[1].date` to "2026-02-20" (a copy of checkins[0]'s key) -> `checkins[1] duplicates checkins[0]`. D7: set `checkins[0].date` to "2026-03-05" (now is 2026-03-04) -> `checkins[0].date is in the future`. D8: set `checkins[0].date` to "2026-02-19" (before h4's start 2026-02-20) -> `checkins[0].date is before the habit's start date`. D9: set `checkins[3].kind` to "maybe" -> `checkins[3].kind is invalid`. A file whose first fault is valid but a later check-in is bad (habits fine, `checkins[3]` invalid) must change nothing, including its habits.

Settings
- [ ] F16 Theme: choosing "Dark" gives computed background `rgb(22, 24, 28)` on a light-preferring browser, "Light" gives `rgb(250, 248, 245)` on a dark-preferring browser, and "System" follows `emulateMedia` changes; the choice survives reload with the right colors immediately after `domcontentloaded`; `theme-status` texts are exact.

Intelligence
- [ ] F17 Quick Add: every parse 1 to 18 above shows the pre-filled form with the stated name, days, and reminder and the matching `quickadd-explain` lines; nothing is saved until Save (Habits page unchanged after Cancel); after Save for parse 1 the Habits page shows "Gym", `Mon, Wed, Fri`, `Reminders: 07:00`; after Save for parse 2 it shows "Stretch" and `Every day`. Empty input shows the exact alert. Saving parse 1 with a stubbed "Not asked" permission makes exactly one permission request, at Save and not before; saving parse 2 makes none.
- [ ] F18 Smart Reminder Timing: with TIMING the Habits card for Read shows the exact text and `data-time="19:40"`; TIMING-6 shows no suggestion; checking in through the UI at 20:10 on seven consecutive days (2026-03-02 to 2026-03-08 via `?now`) on a fresh habit also yields exactly such a suggestion on 2026-03-09 (so `checkedAt` is recorded); accepting adds `Reminders: 19:40` and removes the suggestion, persisting after reload; dismissing hides it, it stays hidden after reload and at `?now=2026-04-07T09:00`, and is shown again at `?now=2026-04-08T09:00`; a habit that already has a reminder at 19:10 or 20:10 (within 30 minutes) shows none, one at 19:09 does.
- [ ] F19 Schedule Fit: FIT-A shows the exact sentence; FIT-B and FIT-C show none; "Adjust schedule for Gym" opens the edit form for that habit.
- [ ] F20 Weekly Insights: with WEEK the card shows exactly the range line and the four sentences and link names in the Weekly Insights definition, and each link navigates to the stated target (`View calendar for Read` opens the Month tab with "Read" selected in the current month; `View year heatmap` opens the Year tab); with FIT-A the suggestion is the Schedule Fit sentence; with no habits the empty text shows; changing a WEEK input (checking Gym on 2026-03-06 via the calendar) changes Gym to 3 of 3 and the "Slipped most" sentence to `Slipped most: Stretch fell from 86% to 71% compared with the prior week.`

Hardening
- [ ] F21 Atomic reminder delivery, normal paths: with permission granted (stand-in), a 09:00 reminder due produces exactly one notification and no banner entry, and a reload creates neither; with permission denied the same reminder produces exactly one banner entry that survives reload and "Mark done" still works.
- [ ] F23 Singular wording: with the ONE dataset (`?now=2026-03-04T09:00`; one habit o1 "Solo", daily, anytime, teal, start 2026-03-01, order 0; one done check-in o1 2026-03-03) in a fresh context, choosing ONE (Merge default) shows `preview-merge` = `Merge would add 1 new habit and 1 new check-in; 0 check-ins already exist and would be left unchanged.`; selecting Replace and "Import" shows alertdialog text `This deletes your current 0 habits and 0 check-ins and replaces them with the contents of the file.`; confirming gives `Replaced all data: 1 habit and 1 check-in imported.`; `export-status` after exporting reads `Exported 1 habit and 1 check-in to cadence-backup-2026-03-04.json.`; choosing ONE again in Merge shows `Merge would add 0 new habits and 0 new check-ins; 1 check-in already exists and would be left unchanged.` and Import gives `Merged: 0 new habits and 0 new check-ins added; 1 check-in already existed and was left unchanged.`; Replace-importing ONE again shows the dialog text `This deletes your current 1 habit and 1 check-in and replaces them with the contents of the file.`
- [ ] F22 Atomic reminder delivery, interrupted: with a notification stand-in whose first construction call reloads the page and then throws, a reminder that was due at page load is afterwards visible as exactly one banner entry for the habit after the reload (not zero), no further notification is constructed for it, and a second reload still shows the one entry until dismissed. All Sprint 3 reminder tests still pass.

### Product Depth (PASS threshold: at least 3 meaningful interactions)

- [ ] D1 Calendar editing loop: from the Habits page open a habit's calendar, back-fill a missed day by clicking it, add a note on it, see the streak change, open the Activity log and find that note, then follow the Weekly Insights link back to the calendar.
- [ ] D2 Backup and restore story: build data with a Quick Add habit and several check-ins, export, reset, import in Merge mode into the empty app (preview says all new), and find everything intact including the quick-added reminder and notes.
- [ ] D3 Suggestions are explainable and actionable: each of Quick Add, Smart Reminder Timing, Schedule Fit, and Weekly Insights displays the data behind it and offers an action (save, accept/dismiss, adjust schedule, open linked view).
- [ ] D4 Dismissal memory: a dismissed reminder suggestion stays dismissed across reload, survives export and Replace import, and returns exactly on day 30.
- [ ] D5 Week start is respected consistently in calendar, heatmap, and weekday picker, and changing it with the calendar open reorders it without a reload.

### Visual Design (PASS threshold: no placeholder UI, consistent styling)

- [ ] V1 The Calendar and Settings placeholders are gone; no "Coming soon" text remains anywhere, and the empty-state privacy note points to Settings > Export data.
- [ ] V2 Month calendar: rounded day cells; completed = filled circle with a check in the habit's color; missed = hollow ring in neutral gray (never red); excused = diagonal hatch; bonus = small dot; today has an outline; notes show a small corner mark; the legend is visible; no state differs by color alone (verified by rendering the calendar in forced grayscale and still telling all eight states apart by shape, and by the distinct `data-shape` values).
- [ ] V3 Heatmap: five intensity levels in teal-green on the warm canvas, level 0 as a bordered empty cell, month and weekday labels, legend; at 375 px width the page has no horizontal scroll, the heatmap scrolls inside its own container, and today's cell is inside the viewport on load.
- [ ] V4 Settings, activity log, import preview, dialogs, suggestions, and insights card use the same card radius, spacing, type, and tokens as earlier sprints in both themes; the bottom bar is used below 1024 px and the left rail above; no clipped or overlapping text at 375 px and 1280 px (screenshots of Calendar Month, Year, Log, Insights, Settings, and an open import preview in both themes).
- [ ] V5 Reduced motion: with reduced motion enabled no transform animation is running after a check-in, opening a dialog, showing the banner, or changing month; confetti is absent.
- [ ] V6 Contrast and focus: an axe-based scan of Today, Habits, Calendar (Month, Year, Log), Insights, Settings, the New habit dialog, the shortcuts dialog, and the import preview, with WEEK data, in light and dark, at 1280 and 375 px, reports no critical or serious violations (WCAG 2 A/AA and 2.1 A/AA rules, including color contrast). Keyboard focus shows a visible outline of at least 2 px on the controls sampled in the test method.

### Code Quality (PASS threshold: no critical errors, no stubs)

- [ ] C1 `npm run build`, `npm test`, and `npm run test:e2e` pass on dev and preview, including every Sprint 1 to 3 test (with only the text edits allowed above).
- [ ] C2 No console errors and no non-local network requests in any test (the automatic fixture still applies), including export, import, and download.
- [ ] C3 Unit tests cover: calendar day-state classification (all eight states, start boundary, today done or pending), heatmap levels (every threshold: 0.49/0.5/0.74/0.75/0.99/1, S=0, skip exclusion), Quick Add (all 18 parses plus punctuation and no-guess cases), Smart Timing (6 vs 7 qualifying, even count median, backfill exclusion, 60-day window edge, before-midnight, 30-minute proximity edge inclusive, dismissal day 29 vs 30), Schedule Fit (n=3 vs 4, 39% vs 40%, other days 70% vs 71%, ties), Weekly Insights (tie-breaks, 14.x vs 15 point drop, empty cases), export/import validation (every message above), the count-message formatter (counts 0, 1, and 2 for every singular/plural message), merge planning (all merge rules), and the reminder claim/banner write ordering.
- [ ] C4 No stubs: suggestions and insights are computed from stored data on the device; export and import use real files; no hidden test-only behavior other than the existing `?now=` and `__cadenceTest` hooks; no network requests; no new runtime dependencies (a dev-only accessibility-scan package is allowed).
- [ ] C5 Data model: the logical schema version stays compatible (Sprint 1 to 3 data loads unchanged, the new `checkedAt` and dismissals are additive), verified by loading a store without them.

## Test Method

Common rules. Every test runs in a new browser context with empty storage, against both `npm run dev` (5173) and `npm run preview` (4173). Time is always `http://localhost:<port>/?now=<ISO>#/...` with the `now` given in the dataset. Download and import use real headless Chromium features: `page.waitForEvent('download')` then read `download.path()`; `page.getByLabel('Import data file').setInputFiles({ name, mimeType: 'application/json', buffer })`. Seeding helper SEED(file, now): open `/?now=<now>#/settings`, choose the file in "Import data file", select the radio "Replace all data", click "Import", click "Confirm replace", expect `import-result` to read `Replaced all data: ...`. Export helper EXPORT(): click "Export data" while waiting for the download, return the file text. Notification stand-ins are installed with an init script as in Sprint 3 (static `permission`, a counting `requestPermission`, a constructor that records into a list).

F1. SEED(CAL). Open `#/calendar`. Expect `calendar-month` "March 2026", select "Habit" = Gym. For each date in the CAL list expect `getByTestId('calendar-day')` with `data-date` and the stated `data-state`, and `getByRole('button', { name: 'Wednesday, 4 March 2026: Completed', exact: true })` (and the other labels: `Friday, 6 March 2026: Missed`, `Thursday, 5 March 2026: Not scheduled`, `Saturday, 7 March 2026: Bonus completion`, `Monday, 9 March 2026: Excused skip`, `Wednesday, 11 March 2026: Completed, has note`, `Wednesday, 18 March 2026: Today, not done yet`, `Thursday, 19 March 2026: Future`, `Monday, 2 March 2026: Before start`). Collect `data-shape` of one cell per state and expect eight distinct values matching the table. Expect `calendar-legend` to contain the eight label strings.
F2. Expect `streak-current` "1" and `streak-longest` "1". Click the March 13 cell: expect `data-state="completed"`, streaks "3" and "3". Reload (same URL): same. Open `#/habits`: Gym card `streak-current` "3". Back to the calendar, click March 13 again: `missed`, "1" and "1". Click March 5: `bonus`, streaks "1" and "1"; reload and expect it persists.
F3. Click March 9: `data-state` stays `excused`, `calendar-day-detail` visible with a "Clear skip" control (or the History-style skip control). Click March 19 and March 2: states unchanged, `calendar-day-detail` count 0. Click March 11, click "Note for Gym on 2026-03-11": editor opens with "5 km"; replace with "6 km", "Save note"; `calendar-note-text` "6 km" and the cell label still ends ", has note". Reload: note kept. Cancel path: edit and "Cancel", note unchanged.
F4. Click "Previous month": `calendar-month` "February 2026", all `calendar-day` `data-state="before-start"`, "Previous month" disabled. "Next month": March; expect "Next month" and "Today" disabled. Go back to February, click "Today": March, "Today" disabled. Navigate to `#/calendar?habit=c1&month=2026-02` (use the id from the fixture) and expect February selected; reload keeps it; `month=2025-12` shows February 2026 and `month=2027-01` shows March 2026 (clamping); `month=abc` shows March 2026; the URL contains `month=2026-02` after clicking Previous month.
F5. SEED(CAL). On `#/settings` select radio "Sunday". Open `#/calendar`: weekday header texts Sun, Mon, Tue, Wed, Thu, Fri, Sat; first `calendar-day` in DOM is March 1 and `calendar-pad` count is 0. Select "Monday": header Mon ... Sun, `calendar-pad` count 6, first day cell March 1 after six pads. Open `n` shortcut dialog or Habits > "New habit": weekday group buttons in text order for each setting. On `#/calendar/year` read the first and last `heatmap-cell` `data-date` under both settings with the WEEK data (SEED(WEEK)): Monday `2025-03-03` / `2026-03-08`; Sunday `2025-03-09` and the last week ends with six `future` cells. Reload with Sunday selected: still Sunday. With the calendar open, switch the setting in Settings and return: no reload needed to see the new order.
F6. SEED(WEEK). Open `#/calendar/year`. Count `heatmap-cell` = 371; map `data-date` values are strictly ascending. Assert `data-level` for 2026-03-02 ... 03-08, 03-09, 02-01 as listed. Assert accessible names for 2026-03-05 (`Thursday, 5 March 2026: 1 of 3 scheduled habits done`), 2026-02-01 and 2026-03-09. Then SEED(MAIN) in a new context at the MAIN clock and assert Mar 1, 2, 3 level `4` with `2 of 2 scheduled habits done`, Mar 4 level `0` with `0 of 3 scheduled habits done`, Feb 28 level `none`.
F7. SEED(MAIN) then `#/calendar/log`. Expect `log-count` "8 check-ins" and `log-row` `data-date`/`log-habit` sequence as listed; `log-note` texts; select "Filter by habit" = "Gym": two rows; = "Old habit (archived)": one; check "Only check-ins with notes" with "All habits": rows Gym (2026-03-03) then Water (2026-03-02); select Water + notes-only + Gym? (use Gym with the notes box, expect 1 row), then uncheck. Create a state with no match (filter "Read" with notes-only) and expect `No check-ins to show.`.
F8. SEED(MAIN). EXPORT(); expect `download.suggestedFilename()` equals `cadence-backup-2026-03-04.json`. Parse JSON: `format`, `version` 1, `exportedAt` `2026-03-04T09:00:00`, habits ids [h1,h2,h3,h4] in order with the MAIN fields (Gym `schedule.days` [0,2,4], `reminders` ["18:30"], h4 `archived` true), `checkins` length 9 sorted by date then habit id with the stated `checkedAt` values and null for h3, settings equal to the MAIN settings, dismissals equal. Expect `export-status` text. Export twice: strings equal. Record all request URLs during the action: none beyond the local origin.
F9. SEED(MAIN). In Settings click "Reset all data": expect `alertdialog`, "Reset everything" disabled; fill "reset", still disabled; fill "RESET " (trailing space), still disabled; "Cancel": EXPORT() equals the earlier export. Reopen, fill "RESET", click "Reset everything": `All data was reset.`; `#/today` shows "Create your first habit"; `#/habits` has no cards; Theme radio "System" checked; Week radio "Monday" checked. EXPORT() compared with an export from another fresh context at the same `now`, after replacing `exportedAt`: equal. Reload: still empty.
F10. SEED(MAIN). E1 = EXPORT(). Reset (F9 steps). Import E1 via `setInputFiles` with Replace + confirm. E2 = EXPORT(). Expect E1 === E2. Check `#/habits` (four names in order, schedule labels `Every day`, `Mon, Wed, Fri`, `Every day`, archived section "Old habit", `Reminders: 18:30` on Gym), background `rgb(22, 24, 28)` (dark), `#/today` Water/Gym/Read statuses, `streak-current`/`streak-longest` on `#/habits` for Water 3/3, Gym 1/1, Read 2/2, `total-completions`, and the log of F7.
F11. In a fresh context open `#/settings`, choose the MAIN file. Expect "Import preview" region, `preview-habits` "Habits: 4", `preview-checkins` "Check-ins: 9", `preview-exported` "Exported: 2026-03-04T09:00:00", radio "Merge" checked. Navigate to `#/habits`: empty state (nothing imported); go back to Settings (the preview may be gone, which is fine) and choose the file again; click "Cancel import": preview gone; EXPORT() shows zero habits and zero check-ins.
F12. SEED(MAIN). Choose MERGE file, select "Replace all data", click "Import": expect `alertdialog` with "Replace all data?" and `This deletes your current 4 habits and 9 check-ins and replaces them with the contents of the file.` Click "Cancel": EXPORT() unchanged and preview still shown. Click "Import" again, "Confirm replace": `Replaced all data: 3 habits and 5 check-ins imported.`; Habits page lists Stretch, Gym, Water renamed in file order; settings theme light (background `rgb(250, 248, 245)` on a light browser).
F13. SEED(MAIN), E1 = EXPORT(). Choose MAIN, keep Merge: `preview-merge` text exact; "Import": `import-result` exact; E2 = EXPORT(); expect E1 === E2.
F14. SEED(MAIN). Choose MERGE, Merge: `preview-merge` = `Merge would add 2 new habits and 3 new check-ins; 2 check-ins already exist and would be left unchanged.`; "Import": `Merged: 2 new habits and 3 new check-ins added; 2 check-ins already existed and were left unchanged.` Then EXPORT(): 6 habits, habits order values 0 to 5 with Stretch at 4 and the new Gym at 5; h1 name "Water", h1 03-02 note "2 litres"; check-ins 12; `settings.theme` "dark", `weekStart` "sunday". Today at the MAIN clock: Water is checked and its card `streak-current` "4". `#/habits`: two cards named "Gym".
F15. SEED(MAIN), E1 = EXPORT(). For each bad file (build buffers in the test): `''`, `{not json`, `[]`, `{"hello":"world"}`, `{"format":"other","version":1}`, `{"format":"cadence-export"}`, `{"format":"cadence-export","version":2}`, `{"format":"cadence-export","version":"1"}`, and D1 to D8 (derived from the MAIN file by the exact edits listed in F15's definition), including D9 (`checkins[3].kind is invalid`). Choose each file: expect `import-error` with the exact message, "Import preview" count 0, `import-result` count 0, then EXPORT() equals E1. After the last bad file choose MAIN and Merge-import it: succeeds with `Merged: 0 new habits ...`.
F16. For Dark: `page.emulateMedia({ colorScheme: 'light' })`, SEED nothing, open `#/settings`, check radio "Dark": `getComputedStyle(document.body).backgroundColor` is `rgb(22, 24, 28)`; reload and read the same value immediately after `waitUntil: 'domcontentloaded'`. For Light with `colorScheme: 'dark'`: `rgb(250, 248, 245)`. For System: switch `emulateMedia` between light and dark and expect the color to follow; `theme-status` exact strings in each mode.
F17. Open `/?now=2026-03-04T09:00#/today` (empty app is fine). For each of parses 1 to 18: fill "Quick add a habit", press Enter; in the dialog assert Name input value, the pressed weekday buttons (`aria-pressed`) or the "Every day" state, and the reminder time input value (or no reminder rows), and the `quickadd-explain` text lines; click "Cancel" and check `#/habits` has no new card. For parse 1 and 2: Save; `#/habits` card "Gym" has `habit-schedule` "Mon, Wed, Fri" and `habit-reminders` "Reminders: 07:00"; card "Stretch" has "Every day". Empty field + Enter: `role=alert` with the exact text and no dialog. Permission: a context with a "Not asked" stand-in whose `requestPermission` counter starts at 0: counter is 0 after loading Today, typing, pressing Enter, and opening the form; saving parse 1 makes it 1; saving parse 2 afterwards leaves it at 1; in a second fresh context saving parse 2 first leaves it at 0.
F18. SEED(TIMING). Open `#/habits`: Read card `reminder-suggestion` text exact, `data-time="19:40"`. SEED(TIMING-6): no `reminder-suggestion`. UI timestamps: in a fresh context create habit "Read" (start 2026-03-01, daily) at `?now=2026-03-01T09:00`; for each date 2026-03-02 ... 03-08 `page.goto('/?now=<date>T20:10#/today')` and click "Check in Read"; then `/?now=2026-03-09T09:00#/habits`: suggestion appears (text with `7:40 pm` and `8:10 pm`, "7 check-ins"); EXPORT() contains `checkedAt` `2026-03-02T20:10:00`. Accept (stub "Not asked": one permission request): `habit-reminders` "Reminders: 19:40", suggestion gone, persists after reload. Dismiss path with a SEED(TIMING) context: click Dismiss; gone; reload at the same URL: gone; `?now=2026-04-07T09:00`: gone; `?now=2026-04-08T09:00`: present. Proximity: edit Read to add a reminder at 19:10, load Habits: none; replace with 20:10: none; replace with 19:09: shown. EXPORT shows `suggestionDismissals` after dismissing; reset and Replace-import it back: dismissal still applies (D4).
F19. SEED(FIT-A) at its clock: Gym card shows `schedule-fit-suggestion` with the exact text. SEED(FIT-B), SEED(FIT-C) (new contexts): none. In FIT-A click "Adjust schedule for Gym": dialog "Edit habit" with name "Gym".
F20. SEED(WEEK), open `#/insights`: `weekly-insights-range`, `insight-consistent`, `insight-slipped`, `insight-weakest-day`, `insight-suggestion` texts exact; link names exact. Click `View calendar for Read`: URL `#/calendar?habit=...`, "Habit" select shows Read, `calendar-month` "March 2026". Back, click `View year heatmap`: Year tab selected. Back, click `See Gym's missed days`: Gym selected. In the calendar for Gym click March 6 (missed) to complete it; reopen Insights: `Slipped most: Stretch fell from 86% to 71% compared with the prior week.`, suggestion item now about Stretch (`Suggestion: Stretch slipped this week. Open its calendar to see which days were missed.`). SEED(FIT-A): suggestion starts with `Suggestion: Thursdays are your weak spot for Gym:` and its link is `Adjust schedule for Gym`. Fresh context: `Add a habit to see your weekly insights.`
F21. Granted stand-in: create habit "Water" at `?now=2026-03-04T08:00` with reminder 09:00 (Add reminder, no request since granted), then `page.goto('/?now=2026-03-04T09:00#/today')`: the recorded construction count is 1, `reminder-banner` count 0 (wait 1 s), reload: still no new construction and no banner. Denied stand-in: same flow ends with one `reminder-banner-item` "Water" that survives reload, and "Mark done: Water" removes it and checks the habit.
F22. Install the crash stand-in: permission "granted"; on the first construction call it sets a session flag, calls `location.reload()`, then throws; later calls record normally. Create Water with a 09:00 reminder at 08:00 (no construction yet), then `page.goto('/?now=2026-03-04T09:00#/today')`; wait for the post-reload load. Expect exactly one `reminder-banner-item` named Water within 3 s, the recorded construction count 0 after the reload, and after `page.reload()` again exactly one entry (until "Dismiss: Water" is clicked, then none even after reload). Re-run the Sprint 3 reminder tests as part of C1.

D1. SEED(CAL), open `#/habits`, click the Gym card's calendar link (a link or button named "Calendar for Gym" on the card, going to `#/calendar?habit=...`), click March 13, add note "made up", open `#/calendar/log` and expect a row for Gym 2026-03-13 with `log-note` "made up", then `#/insights` and click a calendar link, expect the Month tab. (The Gym card gains this link, `Calendar for Gym`.)
D2. Fresh context at `/?now=2026-03-04T09:00#/today` (Wednesday): Quick add "Gym mon wed fri 7am", Save, check it in on Today, add a note, export (E1), reset, import E1 choosing Merge (every later step at the same clock): `preview-merge` reads `Merge would add 1 new habit and 1 new check-in; 0 check-ins already exist and would be left unchanged.`; import; the Habits page shows Gym with `Reminders: 07:00` and the log shows the note.
D3. Verified by F17 to F20 (each shows its reason text and an action).
D4. Combined in F18 (reload, export, Replace import, day 29 and day 30).
D5. In Sunday mode open a form, the calendar, and the Year tab; switch to Monday in Settings; return to each: new order.
V1. Visit Calendar and Settings and search the text for "Coming soon": none. Empty-state privacy note contains `Export data`.
V2. SEED(CAL), calendar Month, screenshot in light and dark at 1280 px; read the image: confirm the shapes, the legend, the today outline, the note corner mark, gray missed rings. Run the page with `filter: grayscale(1)` applied to `html` and screenshot again: states still distinguishable by shape. Assert `data-shape` uniqueness (F1).
V3. SEED(WEEK), Year tab at 1280 and at 375 px (`setViewportSize`): screenshot; assert `document.documentElement.scrollWidth <= innerWidth` at 375; the cell for 2026-03-08 `toBeInViewport()`; the container named "Year heatmap" has `overflow-x` auto or scroll.
V4. SEED(MAIN), screenshots at 1280 and 375 of Calendar Month, Year, Log, Insights, Settings, and Settings with an import preview open, light and dark; read each image for overlap, clipping, and token consistency. Assert the left rail visible at 1280 and the bottom bar visible with five items at 375 (heights >= 44 px).
V5. `browser.newContext({ reducedMotion: 'reduce' })`, SEED(MAIN) at the MAIN clock: check in on Today, open and close the New habit dialog, change calendar month, then evaluate `document.getAnimations().filter(a => a.effect.getKeyframes().some(k => 'transform' in k && k.transform !== 'none')).length === 0`; `confetti` count 0 after completing the day.
V6. For each page and dialog and theme and viewport in V6, load WEEK data and run an axe scan (WCAG 2 A/AA, 2.1 A/AA tags) through Playwright; expect no violation with impact critical or serious. Focus sample: press Tab from the page top 12 times and assert that every element that received focus shows `outline-style` not `none` and `outline-width` >= 2 px (computed), including calendar day buttons and the heatmap container.
F23. Define ONE as a valid export file per the F23 criterion. In a fresh context at `/?now=2026-03-04T09:00#/settings`, run the steps in the criterion in order, asserting each exact string (`preview-merge`, alertdialog text, `import-result`, `export-status`).
C1. Run `npm run build`, `npm test`, `npm run test:e2e`; all green; unit and e2e counts reported in the handoff.
C2. The automatic fixture fails any test with a console error, page error, or non-local request; download via blob or data URL is not a network request.
C3. Evaluator inspects the unit test files for the listed cases and runs `npm test`.
C4. Evaluator greps the source for hard-coded suggestion text without data and for added runtime dependencies; confirms the only test hooks are `?now=` and `window.__cadenceTest` / `__cadenceNotifications`.
C5. Seed IndexedDB with a Sprint 3 shaped database (no `checkedAt`, no dismissals), reload, and confirm all pages render without errors and EXPORT() succeeds with `checkedAt` null.

Keyboard-only flow (criterion KB; part of Functionality, counted with F1 to F23). In a fresh context at `/?now=2026-03-04T09:00#/today` use only `page.keyboard` (no click, no direct `fill`, no `locator.press`): (1) press Tab once and expect focus on "Skip to main content"; press Enter and expect focus inside `main`. (2) Press `n`; expect the New habit dialog and focus on the Name field; type "Walk"; press Enter; expect the dialog closed (focus returned) and, after `h`, a card "Walk". (3) Press `t`; Tab until the focused element's accessible name is "Check in Walk" (at most 40 Tabs); expect `toHaveAccessibleDescription('Not done. Current streak: 0 days.')`; press Space; expect `aria-pressed="true"` and the description `Done. Current streak: 1 day.`. (4) Press `c`; expect the Calendar heading focused and `document.title` "Calendar - Cadence"; Tab until a calendar-day button for 2026-03-04 is focused; press Enter; expect the day detail panel to show. (Enter toggles Walk's check-in off, which does not affect steps (5) to (8).) (5) Press `s`; Tab until the focused element is "Export data" (at most 80 Tabs); start waiting for a download and press Enter; expect a file named `cadence-backup-2026-03-04.json`. (6) Press `?`: expect the "Keyboard shortcuts" dialog listing n, t, h, c, i, s, /, ?; press Escape: the dialog closes. (7) Press `/` on `#/calendar`: Today opens with the Quick add field focused. (8) Typing "n" inside the Quick add field does not open a dialog. Also run an axe scan for the same pages as in V6 (counted there).
