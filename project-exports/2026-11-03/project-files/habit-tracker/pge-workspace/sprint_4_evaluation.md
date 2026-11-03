# Sprint 4 Evaluation

> Transcribed by the orchestrator from the Sprint 4 evaluator's final report. The evaluator finished testing and signalled PASS but left only its in-progress skeleton in this file. Verdict, scores and findings below are the evaluator's, not the orchestrator's. Its scratch scripts are in /tmp/claude-0/eval4/.

## Verdict: PASS

## Scores
| Criterion | Score | Pass (>=3) |
|-----------|-------|------------|
| Functionality | 5 | yes |
| Product Depth | 4 | yes |
| Visual Design | 4 | yes |
| Code Quality | 5 | yes |

## Evidence
- Independent Playwright scripts covering F1–F23, the keyboard-only flow, reduced motion, focus outlines and axe: all pass.
- 52 axe scans (light/dark, 375/1280 px, dialogs, import preview): no violations.
- About 45 bad or damaged import files: each gave the exact error message and left the existing data byte-identical.
- Export, then Replace re-import of the same file: E1 === E2 (no data loss). Merging the same file again is idempotent; merge rules behaved as specified.
- Atomic reminder delivery (F21/F22) passed, including a constructor-throws variant without reload.
- `npm run build` clean; 260 unit tests pass; generator e2e suite 342/342 on dev and preview.
- No console errors or non-local requests. Servers stopped.

## Deviations reviewed
1. Habit card Calendar control is `<a role="button">`: Enter and Space both navigate; accessible name "Calendar for <habit>"; axe clean. Minor semantic defect (announced as a button but navigates); a real `<a>` link would be better. Not blocking.
2. Clicking a completed day with a note selects it instead of toggling it off. The user can still uncheck via clearing the note then clicking, or from Today or the History dialog. Required by contract F3. A visible "Uncheck" button in the day detail would help discoverability.

## Minor observations
- With Monday week start the heatmap ends on 2026-03-08 (no 9 March cell); the `Future` label was verified under Sunday start.
- After saving a shortcut-opened New habit dialog with Enter, focus lands on `main` rather than the h1.
- Headless Chromium drops every 11th blob download; reproduced on a bare page, so not an app bug.

## Required Fixes
(none)
