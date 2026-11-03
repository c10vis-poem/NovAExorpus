# Sprint 3 Evaluation

## Verdict: PASS

| Criterion | Score | Verdict | Notes |
|-----------|-------|---------|-------|
| Functionality | 5/5 | PASS | Independent Playwright scripts (/tmp/claude-0/eval3/t1-t5.js) covered F1-F17 flows: granted/denied/unsupported/default/real-grant, banner Mark done/Snooze/Dismiss, stacking, no-fire cases, dedupe incl. two tabs, hidden delivery + catch-up, real-clock F12, notification click, at-risk badge/reminder/settings. All passed. |
| Product Depth | 4/5 | PASS | D1-D4 flows work (edit 09:00 to 09:30 fires once; time added in the past not delivered; settings take effect without reload; denied full-day flow with Undo toast). |
| Visual Design | 4/5 | PASS | Screenshots reviewed (light 1280, dark 375 reduced motion): banner, settings, form consistent with Cadence cards; buttons 44 px; no horizontal scroll; status has icon+text. |
| Code Quality | 5/5 | PASS | build clean, 117/117 unit, 234/234 e2e (dev+preview) re-run by me; no console errors in my scripts. |

## Detailed Findings

Scrutinised deviation (Notification.permission "denied" upgraded to granted when Permissions API says "granted"):
- Real-grant context: raw `Notification.permission` is "denied", API says granted; app delivers exactly one real notification, no banner. Works.
- Forced failure: stand-in permission "granted" with a constructor that throws, tested visible, hidden, across reload, across a fresh `?now=` load, and with two merged refusals. The banner entry always appears (merged into one entry), persists after reload, no notification is logged, no console error. Plain denied (real, no grant) also shows the banner. The upgrade only applies when the two sources disagree; stand-ins and real denial are unaffected. No silent loss observed.
- Residual risk (non-blocking): the claim of a delivery and the fallback banner write are two separate IndexedDB transactions (`src/data/reminders.tsx` runEvaluation, `addBannerDeliveries`). If the page is closed (or the second write throws) between them after a constructor refusal, that reminder is consumed without a banner entry. Very narrow window; also only on the refusal path.

Observations:
- Reloading with a `?now=` earlier than the entry's due time (rewinding the clock) hides the banner entry; artificial test-hook situation only.
- Hidden delivery: granted gives one notification while hidden and none added on becoming visible; denied gives a DOM banner entry while hidden, one entry on return; frozen catch-up merges to dueTimes ["09:00","12:00"]; midnight sleep and quiet-hours sleep deliver nothing and consume.
- Real clock: runFor 01:05 delivers once; fastForward 2.5 h delivers one merged ["09:00","10:00"]; snooze reappears after 10:30 and not at 9:30.
- Permission: zero requests across load, all routes, plain habit, Settings; exactly one on first Add reminder; "default" result still gives banner; Settings shows exact guidance (unsupported verified).
- Notification click: lands on #/today, card data-highlighted, "Check in Water" focused, highlight cleared after navigation; deleted habit opens Today without error.
- Equal quiet hours rejected with exact text; stored values kept after reload.

## Required Fixes

(none)

## Optional Improvements
- Make claim + banner fallback atomic (write the banner entry in the same transaction, then remove it if the notification is created) so a refused constructor can never lose a reminder even if the page closes mid-evaluation.
- Avoid hiding a persisted banner entry when the pinned/app clock is earlier than its due time.
