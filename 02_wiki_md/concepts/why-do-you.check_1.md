---
source: why-do-you.check (1).md
type: markdown
cleaned: 2026-09-11
cleaner: tools/clean.py (mutool)
---

# Check — Llm wiki/Why do you.txt

## Verdict: PASS + UPSTREAM DEFECT

| | |
|---|---|
| encoding | utf-8-sig |
| bom | False |
| bytes | 4757 |
| atoms judged | 9 |
| atoms set aside (fused by the checker's own extractor) | 9 |
| segments checked | 48 |
| furniture lines found by the checker | 2 |
| end of source survives | yes |
| start of source survives | yes |

## Upstream defects — 1

Already wrong in the source before this repo touched it. Reported, not repaired — hard rule 1.

### SOURCE TRUNCATED — the SOURCE itself stops mid-sentence — an upstream defect, not a cleaning defect

its own last words: `No, it will not erase your information. Your or` — the cleaned file reproduces that ending faithfully. Nothing in this repo can repair this; it needs re-retrieving at the origin.

## Furniture, audited independently — 2 line(s)

Every line the *checker* judges furniture under the strip policy in `README.md` → "The one job", and what actually became of it. This is not the cleaner's own report of what it removed.

- removed, and it is furniture — browser/app chrome, source line 2: `11 sites`
- removed, and it is furniture — browser/app chrome, source line 59: `9 sites`
