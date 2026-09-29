---
source: system-mapping.check (1).md
type: markdown
cleaned: 2026-09-11
cleaner: tools/clean.py (mutool)
---

# Check — Llm wiki/System Mapping.txt

## Verdict: PASS + UPSTREAM DEFECT

| | |
|---|---|
| encoding | utf-8-sig |
| bom | False |
| bytes | 5410 |
| atoms judged | 29 |
| atoms set aside (fused by the checker's own extractor) | 37 |
| segments checked | 61 |
| furniture lines found by the checker | 4 |
| end of source survives | yes |
| start of source survives | yes |

## Upstream defects — 1

Already wrong in the source before this repo touched it. Reported, not repaired — hard rule 1.

### SOURCE TRUNCATED — the SOURCE itself stops mid-sentence — an upstream defect, not a cleaning defect

its own last words: `Success: If your terminal immediately prints ou` — the cleaned file reproduces that ending faithfully. Nothing in this repo can repair this; it needs re-retrieving at the origin.

## Furniture, audited independently — 4 line(s)

Every line the *checker* judges furniture under the strip policy in `README.md` → "The one job", and what actually became of it. This is not the cleaner's own report of what it removed.

- removed, and it is furniture — browser/app chrome, source line 16: `3 sites`
- removed, and it is furniture — browser/app chrome, source line 66: `Use code with caution.`
- removed, and it is furniture — browser/app chrome, source line 89: `Use code with caution.`
- removed, and it is furniture — browser/app chrome, source line 112: `Use code with caution.`
