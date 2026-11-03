# Sprint 2 Evaluation

## Verdict: PASS

| Criterion | Score | Verdict | Notes |
|-----------|-------|---------|-------|
| Functionality | 5/5 | PASS | Independent Playwright script (/tmp/claude-0/eval2/t.js) reproduced S1-S7, T1-T5, M1-M3, D1, F1-F9 spot checks with exact contract numbers via ?now=. All matched. |
| Product Depth | 5/5 | PASS | Full daily loop (check, note, uncheck, Undo restoring note, skip, celebration, reload, dashboard 1/A/18%) works. Backfill via History updates numbers at once. |
| Visual Design | 4/5 | PASS | Screenshots (light 1280px, dark 375px) read: large Done pill (112x52), 36px/800 tabular streak with amber flame, gray Missed, teal ring, no horizontal scroll at 375px. |
| Code Quality | 5/5 | PASS | build clean; 73/73 unit tests; 110/110 e2e (dev + preview); zero console errors and zero non-local requests in my flows; streaks.ts is pure. |

## Detailed Findings
- Exact values verified: Gym 3/3 and 100% rates; Read 71/71/71, total 5, 1/3, then 67%, total 4, 0/3 after unchecking today; Run 4/4, 0/4, 1/4; Walk 3, 4, 3; Stretch (skip) 3, 4, 2 after clearing skip; Swim schedule edit (Done / Not scheduled / Not scheduled, current 1, 1, 0, 03-05 Missed); Late 3 / 100% / 3 with 3 history rows and no "Show 14 more days"; Stretch7 badges 3 and 7, then only 3 after unchecking 03-07; Dashboard 3/Gym/80%, archived Gym gives Read/71%; D1 gives 1/A/18%.
- Bonus (History and Today) leaves streaks and today-progress unchanged; total completions goes to 4.
- Future date alert, pre-start alert and date max=2026-03-07 behave per contract. Delete then recreate "Read" starts at 0 streak and 0 completions. State persists across reload.
- Note limit 200 enforced; Undo restores note; confetti shown once after the check and absent after reload; with reduced motion the text shows and no confetti.
- Empty states: Today shows onboarding; Insights shows a friendly empty message.
- Minor: re-checking Plank after an uncheck leaves the earlier milestone toast visible, so two identical milestone toasts stack briefly. Contract allows stacking, so not blocking.

## Required Fixes
(none)

## Optional Improvements
- De-duplicate identical milestone toasts shown within the 6 s window.
