---
source: wiki-marcor-obsidian.check (1).md
type: markdown
cleaned: 2026-09-11
cleaner: tools/clean.py (mutool)
---

# Check — Llm wiki/wiki marcor obsidian.txt

## Verdict: PASS + UPSTREAM DEFECT

| | |
|---|---|
| encoding | utf-8-sig |
| bom | False |
| bytes | 1982 |
| atoms judged | 4 |
| atoms set aside (fused by the checker's own extractor) | 5 |
| segments checked | 23 |
| furniture lines found by the checker | 1 |
| end of source survives | yes |
| start of source survives | yes |

## Upstream defects — 1

Already wrong in the source before this repo touched it. Reported, not repaired — hard rule 1.

### SOURCE TRUNCATED — the SOURCE itself stops mid-sentence — an upstream defect, not a cleaning defect

its own last words: `You are the dedicated AI compiler for my personal LLM Wiki. I a` — the cleaned file reproduces that ending faithfully. Nothing in this repo can repair this; it needs re-retrieving at the origin.

## Furniture, audited independently — 1 line(s)

Every line the *checker* judges furniture under the strip policy in `README.md` → "The one job", and what actually became of it. This is not the cleaner's own report of what it removed.

- removed, and it is furniture — browser/app chrome, source line 9: `16 sites`
