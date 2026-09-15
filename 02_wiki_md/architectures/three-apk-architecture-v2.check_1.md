---
source: three-apk-architecture-v2.check (1).md
type: markdown
cleaned: 2026-09-11
cleaner: tools/clean.py (mutool)
---

# Check — Three-APK Architecture (v2).pdf

## Verdict: PASS WITH WARNINGS + UPSTREAM DEFECT

| | |
|---|---|
| pages | 4 |
| atoms judged | 50 |
| atoms set aside (fused by the checker's own extractor) | 13 |
| segments checked | 61 |
| furniture lines found by the checker | 0 |
| end of source survives | yes |
| start of source survives | yes |

## Warnings — 1

The detail survived; something about its shape did not.

### RESPACED VALUE — the path `GUIspeech/vision` survives with its internal spacing changed

source line 60

## Upstream defects — 1

Already wrong in the source before this repo touched it. Reported, not repaired — hard rule 1.

### SOURCE TRUNCATED — the SOURCE itself stops mid-sentence — an upstream defect, not a cleaning defect

its own last words: `captured from session · reference material, not a build-out session on its own` — the cleaned file reproduces that ending faithfully. Nothing in this repo can repair this; it needs re-retrieving at the origin.
