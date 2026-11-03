---
name: habit-tracker-cadence-build
description: "Cadence" habit tracker built via the PGE pipeline on 2026-10-24: complete; where the code lives and what is still open
metadata:
  type: project
  modified: 2026-10-24T14:56:49.135Z
---

On 2026-10-24 the user asked (via "/pge", which is not an installed command) to "build a habit tracker with streaks and reminders". It was run with the pge-orchestrator:pge skill, using the standard evaluator and the claude backend. **The pipeline is DONE: all 4 sprints passed independent Playwright evaluation with no required fixes.**

- **Product:** "Cadence" is a local-first web app built with Vite, React and TypeScript. Data lives in IndexedDB, with no accounts and no API keys. It has:
  - habits and schedules, check-ins, schedule-aware streaks and stats
  - reminders through the Notification API, with an in-app banner fallback, quiet hours, pause and streak-at-risk alerts
  - a calendar and heatmap, JSON export/import (Replace/Merge), rule-based suggestions, and an accessibility pass
- **Code:** /home/user/habit-tracker is a local git repo on master with no remote, and nothing has been pushed. The container is ephemeral, so the durable copy is /mnt/project-files/habit-tracker/cadence.bundle (`git clone cadence.bundle cadence`). The README user guide and pge-workspace/ (spec, contracts, evaluations, pge_summary.md) are also copied there.
- **Run:** `npm install && npm run dev` serves on 5173; `npm run build && npm run preview` serves on 4173.
- **Orchestrator decision:** the Sprint 3 contract was amended after ratification so reminders still fire while the app is in a background tab. The original rule held them until the tab was visible again.
- **Orchestrator transcription:** the Sprint 4 evaluator signalled PASS but left only a skeleton in sprint_4_evaluation.md. The orchestrator copied the evaluator's report into that file and labelled it as copied.
- **Open user decision:** reminders due during quiet hours are skipped, not deferred until quiet hours end.
- **Optional follow-ups from the evaluators:**
  - The Calendar control on habit cards is `<a role="button">`; it should be a real link.
  - Completed days that have a note need a visible "Uncheck" in the day detail.
  - After saving a dialog opened by keyboard shortcut, focus lands on `main` instead of the h1.
- **User not informed:** the hearthbot reply tools were unavailable for most of the run, including at completion. The user may not have received the usage-limit stop notice (HTTP 429 during the Sprint 1 evaluation), the progress updates, or the completion summary.

**Why:** a later thread may be asked about this app, to change it, or to push it to a repo.
**How to apply:** if /home/user/habit-tracker is gone, restore it from the bundle. Make sure the user has received the completion summary and the quiet-hours question.
