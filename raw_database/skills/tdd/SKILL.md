---
name: tdd
description: Enforce test-driven development loop (red -> green -> refactor) focusing on behavior through public interfaces. Use when building features or fixing bugs test-first, or when the user mentions "red-green-refactor".
source_doc: raw_database/raw/code-review.md
note: "Source filename says code-review, but its actual content is this tdd skill — kept verbatim under its real content, not the misleading filename."
---

# Test-Driven Development (TDD)

Execute feature construction using a strict Test-Driven Development loop.

## Loop Rules

1. **Planning:**
   - Define public interface boundaries and primary behavior list.

2. **RED:**
   - Write **one** failing integration/behavior test targeting public interfaces.
   - Confirm test fails for expected reason.

3. **GREEN:**
   - Write minimal implementation code necessary to pass the test.

4. **REFACTOR:**
   - Clean implementation details while staying strictly green. Never refactor on red.
   - Repeat loop per behavior slice.
