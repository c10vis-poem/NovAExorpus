---
source: github-docs-skill.check (1).md
type: markdown
cleaned: 2026-09-11
cleaner: tools/clean.py (mutool)
---

# Check — SKILLS.md/GitHub_Docs_SKILL.txt

## Verdict: PASS WITH WARNINGS

| | |
|---|---|
| encoding | utf-8-sig |
| bom | True |
| bytes | 9889 |
| atoms judged | 13 |
| atoms set aside (fused by the checker's own extractor) | 28 |
| segments checked | 77 |
| furniture lines found by the checker | 0 |
| end of source survives | yes |
| start of source survives | yes |

## Warnings — 1

The detail survived; something about its shape did not.

### STRAY BYTE-ORDER MARK — the source's UTF-8 BOM was carried into the middle of the cleaned file, after the frontmatter

U+FEFF now sits at the first character of the markdown body
