---
source: raw/code review.md
cleaned: 2026-09-09
converter: Read tool (plain text)
note: "Filename collides with raw/code-review.md under the slug algorithm (both -> code-review-md); disambiguated as -1 (this file, source has a space) / -2 (source has a hyphen). See raw_database/clean_md/code-review-md-2.md."
disposition: "COMBINE — compact earlier draft of the same code-review skill. The more complete version (raw/code review.docx.txt) is canonical, extracted to skills/code-review/SKILL.md. This draft is kept as-is, not deleted."
---

---
name: code-review
description: Review the changes since a fixed point along two axes — Standards (does the code follow this repo's documented coding standards?) and Spec (does the code match what the originating issue/spec asked for?).
disable-model-invocation: true
---

# Code Review

Perform a dual-axis review comparing latest workspace diffs against coding standards and project specs.

## Process

1. **Pin Reference**:
   - Determine comparison base (`git diff <target>...HEAD`) and verify non-empty diff.

2. **Parallel Sub-Agent Review**:
   - **Standards Agent**: Audits changes for Fowler code smells, type safety, performance bugs, and adherence to `CODING_STANDARDS.md`.
   - **Spec Agent**: Audits diff against originating ticket/spec to confirm acceptance criteria are met without undocumented scope creep.

3. **Structured Reporting**:
   - Report findings categorized by severity: **Critical**, **Major**, **Minor**, or **Nitpick**.
   - Provide explicit file paths, line references, and runnable code patches for fixes.
