---
source: original-directions-2026-08-18.check (1).md
type: markdown
cleaned: 2026-09-11
cleaner: tools/clean.py (mutool)
---

# Check — ORIGINAL-DIRECTIONS-2026-08-18.md

## Verdict: PASS + UPSTREAM DEFECT

| | |
|---|---|
| encoding | utf-8-sig |
| bom | False |
| bytes | 24169 |
| atoms judged | 69 |
| atoms set aside (fused by the checker's own extractor) | 52 |
| segments checked | 183 |
| furniture lines found by the checker | 0 |
| end of source survives | yes |
| start of source survives | yes |

## Upstream defects — 1

Already wrong in the source before this repo touched it. Reported, not repaired — hard rule 1.

### SOURCE TRUNCATED — the SOURCE itself stops mid-sentence — an upstream defect, not a cleaning defect

its own last words: `Can't move screen equals can't sign in` — the cleaned file reproduces that ending faithfully. Nothing in this repo can repair this; it needs re-retrieving at the origin.
