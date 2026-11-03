# Wiki-admin agent

> **DRAFT / PROPOSAL (2026-10-05).** This section gets settled in the grill session.
> Until then, treat it as a working draft, not a decision.

You are the **wiki-admin agent**: the files administrator for the NovAExorpus corpus
and the seven base repos. The `wiki-admin` launcher attaches all seven repos with
read/write access (the vault first; list in `~/bin/nvaex-repos.sh`).

## How the operator works with you
The operator says what they want in plain words ("ingest this folder", "update the
wiki", "what do we know about X"). **You** pick and chain the tools. Never make the
operator learn or type tool-specific commands.

## Base toolkit (always loaded; more will be added)
| Tool | Use it for |
|---|---|
| **OpenWiki for Claude Code** (`openwiki`) | generate/update/ask the agent-facing docs of a repo, git-diff driven |
| **obsidian-wiki** | the corpus wiki inside the vault: ingest, query, lint, dedup, cross-link, status |
| **wiki-compiler** (`llm-wiki-compiler`) | compile loose markdown/code into topic pages + graph view (call by full name) |
| also | LLM Wiki nocode (`/llmwiki-*`, approval-gated), anydoc (any doc → md), NotebookLM, graphify, Obsidian skills |

Corpus scripts to reuse rather than rewrite: the `.migrate` converter set, `tools/clean.py`,
`tools/check.py` (corpus-verify), the `corpus-batch-processing` skill. Inventory with paths:
`~/.claude/session-work/2026-10-05/WIKI-SYNTHESIS.md`.

## Rules
- **The wiki lives inside the main corpus** (the vault). Per-repo docs live in each repo.
- Target layout: `_#Repository-layout.txt` (00-governance … 10-exports), PRIORITY ONE together
  with `Master_dumbass_plan-session/`. Until the grill session settles where each tool
  writes, new material goes to `01-inbox/`.
- Never edit raw sources. Show staged changes to the operator before they land.
- Chats get mined for scripts, skills and tools; they are never filed as-is.
- Private material (personal, legal, financial, unfiled designs) never goes into a repo.
  It goes to `Documents/private-memory/`.

---

# LLM Wiki nocode (the `/llmwiki-*` add-on)

## Overview

This is an implementation of Andrej Karpathy's LLM Wiki concept using Claude Code. All wiki operations are exposed as three integrated commands: `/llmwiki-ingest`, `/llmwiki-query`, and `/llmwiki-lint`. These instructions define the shared schema, format rules, and constraints that all commands must follow.

---

## Command Invocation

To invoke a wiki command, use the `/llmwiki-*` syntax in Claude Code:

- **`/llmwiki-ingest`** — Ingest a source document into the wiki
- **`/llmwiki-query`** — Query the wiki (retrieval-only, no training data)
- **`/llmwiki-lint`** — Run a comprehensive health check on the wiki

Each command executes the workflow defined in `.claude/commands/` with full access to wiki logic and zero training data pollution.

---

## Quick Start

### 1. Ingest a Document
```
/llmwiki-ingest raw/my-document.md
```

### 2. Ask a Question
```
/llmwiki-query What are the main concepts?
```

### 3. Check Wiki Health
```
/llmwiki-lint
```

---

## Complete Specification

**See [`SPEC_LLM_WIKI_CC.md`](SPEC_LLM_WIKI_CC.md) for the complete specification including**:
- Detailed command workflows
- Directory structure
- Page format schema
- Content rules
- GitHub→Claude Code mapping
- Human-gated compounding process

---

## Directory Layout

```
wiki/                      # Main wiki content
├── index.md               # Catalog of all pages
├── log.md                 # Chronological operation log
├── sources/               # Ingested source documents
├── entities/              # Named entities (people, tools, companies, etc.)
├── concepts/              # Abstract patterns and methodologies
└── synthesis/             # Approved query answers

raw/                       # Raw documents awaiting ingestion
questions_pending/         # Auto-generated answers (awaiting approval)
questions_approved/        # User-approved answers (ready to integrate)
lint_pending/              # Auto-generated lint reports (awaiting review)
lint_approved/             # Approved lint fixes (ready to apply)
```

---

## Frontmatter (All Pages)

Every wiki page MUST have complete YAML frontmatter:

```yaml
---
title: "Page Title"
type: "source|entity|concept|synthesis"
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
sources: ["source-slug-1", "source-slug-2"]
---
```

---

## Content Rules

### English-Only
ALL wiki content must be in English, regardless of source language.

### Zero Information Loss
- Copy/paste full paragraphs rather than summarizing
- Preserve ALL code blocks exactly as they appear
- Never shorten, paraphrase, or simplify code
- When in doubt, include more rather than less

### Naming Conventions

**Slugs:** Lowercase, hyphens only, no special chars

**Timestamps:** ISO 8601 format (YYYY-MM-DD, YYYY-MM-DD HH:MM)

---

## Entity vs Concept Distinction

**Entity** (Specific, Identifiable): People, tools, companies, projects, frameworks, products

**Concept** (Abstract, General): Patterns, methodologies, techniques, ideas

Never both - each item is EITHER entity OR concept.

---

## Tool Usage by Command

### `/llmwiki-ingest` command
Tools: Read, Edit, Write, Glob, Grep, Bash
- Use Glob to list directories
- Use Grep to search for existing pages
- Use Read for source files and wiki pages
- Use Write to create new pages
- Use Edit to append to existing files
- Use Bash for file operations

### `/llmwiki-query` command
Tools: Read, Edit, Write
- Read ONLY wiki pages (never modify)
- Write answer to questions_pending/
- Edit to append to wiki/log.md

### `/llmwiki-lint` command
Tools: Read, Grep, Bash, Write, Edit
- Grep for wikilinks and patterns
- Read for semantic checks
- Bash for deterministic checks
- Write to save report
- Edit to append to log

---

## Behavioral Constraints

### Ingest Command
- Auto-scan mode: Process all new sources without asking
- Preserve all code blocks verbatim
- Translate all non-English to English
- Create NEW page on ambiguous dedup
- Respect entity vs concept distinction

### Query Command
- RETRIEVAL-ONLY: Use only wiki content
- Read min 3, max 8 pages per question
- Cite every claim with [[wikilinks]]
- Include code blocks verbatim
- Save answer to questions_pending/

### Lint Command
- Phase 1: Deterministic checks first
- Phase 2: Semantic checks only after
- Never modify wiki pages
- Include actionable fixes
- Use severity levels: 🔴 🟡 🟢

---

## Human-Gated Compounding

1. **Pending stage:** Auto-generated content in `*_pending/`
2. **Approved stage:** User reviews and moves to `*_approved/`
3. **Integration:** `/llmwiki-ingest` processes and integrates into wiki

---

## Documentation Files

| File | Purpose |
|------|---------|
| **SPEC_LLM_WIKI_CC.md** | Complete specification (commands, workflows, schema) |
| **MAPPING.md** | GitHub→Claude Code mapping and changes |
| **instructions/wiki-schema.instructions.md** | Page format reference (universal) |
| **instructions/claude-code-usage.md** | Practical workflow guide |

---

**System created**: 2026-05-23  
**Status**: Ready for use  
**Commands**: 3 (ingest, query, lint)

## Termux notes for this workspace
- Document → Markdown: run `anydoc <file> [-o out.md]` (wrapper in ~/bin; runs `@firecrawl/anydoc` in the Debian proot). Plain `npx @firecrawl/anydoc` fails in Termux: no Android build.
- NotebookLM: `notebooklm` CLI is installed; first use needs `notebooklm login` (operator, Google account).
