---
name: memory-as-skill
description: "User-controlled persistent memory system using plain Markdown files that the user can directly read, edit, and scope. Replaces reliance on opaque background memory with inspectable, editable files the user owns. Use this skill at the START of every session — read the memory files BEFORE doing anything else. Use at the END of any session with meaningful progress to update the relevant file."
---

# Memory As A Skill

## Why this exists

The built-in memory system is opaque — the user can't see what's stored, can't edit it, can't scope it, and can't stop old irrelevant context from bleeding into new work. This skill adds a user-controlled layer on top: plain Markdown files the user owns, reads, and edits directly.

## Structure

```
memory/
├── general.md           — builder profile, cross-project rules, standing preferences
├── active/
│   ├── <project>.md     — one file per in-flight project
│   └── <subtopic>.md    — optional deep-dive files within a project scope
└── archive/
    └── <project>.md     — compacted finished projects (DO NOT LOAD unless asked)
```

## Session start (mandatory)

1. Read `memory/general.md`. It's small, always relevant.
2. Identify which project the user is working on. Read ONLY `memory/active/<that-project>.md`.
3. If a relevant subtopic file exists, read that too.
4. **DO NOT read `archive/` at session start.**

## Stop blocks

```
<!-- STOP: Do not reference anything below this line unless explicitly asked -->
<!-- SCOPE: compiling only -->
```

If a stop block exists, read only above it. Respect scope markers — they prevent context bleed.

## During the session

Apply loaded context silently. No "according to my memory file." Just know it.

## Session end / meaningful checkpoint

Update `active/<project>.md` with decisions made, current state/blockers, next concrete step. Don't log failures unless they convert to a reusable rule. Keep each active file under ~150 lines.

## Archiving (fold-over)

When a project is done: compact to dense summary, merge cross-project lessons into `general.md`, move to `archive/`, remove the `active/` version.

## Naming Convention

| Pattern | Scope |
|---------|-------|
| `<project>-wiki` | Project-specific architecture, decisions, current state |
| descriptive name | Cross-project utility (termux-helper, defuddle, etc.) |

Project wikis reference utility skills, never duplicate them.