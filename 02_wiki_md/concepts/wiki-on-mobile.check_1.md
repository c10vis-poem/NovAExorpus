---
source: wiki-on-mobile.check (1).md
type: markdown
cleaned: 2026-09-11
cleaner: tools/clean.py (mutool)
---

# Check — Llm wiki/wiki on mobile.txt

## Verdict: PASS + UPSTREAM DEFECT

| | |
|---|---|
| encoding | utf-8-sig |
| bom | False |
| bytes | 1812 |
| atoms judged | 6 |
| atoms set aside (fused by the checker's own extractor) | 4 |
| segments checked | 22 |
| furniture lines found by the checker | 0 |
| end of source survives | yes |
| start of source survives | yes |

## Upstream defects — 1

Already wrong in the source before this repo touched it. Reported, not repaired — hard rule 1.

### SOURCE TRUNCATED — the SOURCE itself stops mid-sentence — an upstream defect, not a cleaning defect

its own last words: `Here is how you can use both apps on your phone to b` — the cleaned file reproduces that ending faithfully. Nothing in this repo can repair this; it needs re-retrieving at the origin.
