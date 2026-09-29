---
source: wiki-on-desktop.check (1).md
type: markdown
cleaned: 2026-09-11
cleaner: tools/clean.py (mutool)
---

# Check — Llm wiki/wiki on desktop.txt

## Verdict: PASS + UPSTREAM DEFECT

| | |
|---|---|
| encoding | utf-8-sig |
| bom | False |
| bytes | 3016 |
| atoms judged | 11 |
| atoms set aside (fused by the checker's own extractor) | 8 |
| segments checked | 33 |
| furniture lines found by the checker | 1 |
| end of source survives | yes |
| start of source survives | yes |

## Upstream defects — 1

Already wrong in the source before this repo touched it. Reported, not repaired — hard rule 1.

### SOURCE TRUNCATED — the SOURCE itself stops mid-sentence — an upstream defect, not a cleaning defect

its own last words: `Do you want a specific, copy-pasteable prompt you ca` — the cleaned file reproduces that ending faithfully. Nothing in this repo can repair this; it needs re-retrieving at the origin.

## Furniture, audited independently — 1 line(s)

Every line the *checker* judges furniture under the strip policy in `README.md` → "The one job", and what actually became of it. This is not the cleaner's own report of what it removed.

- removed, and it is furniture — browser/app chrome, source line 4: `4 sites`
