<!-- Converted from c10vis-poem_NvAEx-llm-wiki-nocode_ No-code LLM Wiki implementation (Karpathy pattern)_ dual support for GitHub Copilot (.github_) and Claude Code (.claude_).pdf — 7 pages -->

## Page 1

NvAEx-llm-wiki-nocode
Code Pull requests Agents Actions Projects Wiki Security and quality Insights
Settings
Watch 0 Fork 0
## No-code LLM Wiki implementation (Karpathy pattern): dual support for GitHub Copilot (.github/) and Claude Code
## (.claude/)
0 stars 0 forks 0 watching 1 branch 0 tags Activity
Public repository · Forked from rosidotidev/llm-wiki-nocode
1 Branch 0 Tags Go to file T Go to file Add file Code
This branch is up to date with rosidotidev/llm-wiki-nocode:main . Contribute Sync fork
| Code | Issues | Pull requests |  |
|---|---|---|---|
| rosidotidev added more details in readme.md |  |  | fe25345 · 4 months ago |
| .claude | first commit of a working solution f … | 4 months ago |  |
| .github | first commit of a working solution f … | 4 months ago |  |
| bak | changed readme.md | 4 months ago |  |
| docs | changed readme.md | 4 months ago |  |
| lint_approved | first commit of a working solution f … | 4 months ago |  |
| lint_pending | first commit of a working solution f … | 4 months ago |  |
| questions_approved | first commit of a working solution f … | 4 months ago |  |
| questions_pending | first commit of a working solution f … | 4 months ago |  |
| raw | first commit of a working solution f … | 4 months ago |  |
| wiki | first commit of a working solution f … | 4 months ago |  |
| .gitignore | Initial commit | 4 months ago |  |
| BOOTSTRAP.md | first commit of a working solution f … | 4 months ago |  |
| COMMAND_MAPPING.md | first commit of a working solution f … | 4 months ago |  |
| MAPPING_COPILOT_TO_CLA … | first commit of a working solution f … | 4 months ago |  |
| README.md | added more details in readme.md | 4 months ago |  |
 
 
 
bak changed readme.md 4 months ago
 
 
 
 
 
 
 
.gitignore Initial commit 4 months ago

---

## Page 2

README
## LLM Wiki — No-Code Knowledge Management
## System
A no-code implementation of Andrej Karpathy's LLM Wiki concept for Claude Code and GitHub Copilot.
Ingest documents. Ask questions. Maintain a living knowledge base — all without writing a single line of code.
## What Is This?
LLM Wiki is a structured knowledge management system where an LLM:
Ingests raw documents and extracts entities, concepts, and relationships
Queries its own knowledge base to answer questions (retrieval-only, no hallucinations)
Maintains its own integrity through automated health checks
Compounds knowledge as humans review and curate the best answers
Key principle: Everything the wiki knows comes from what you feed it. No external knowledge. No training data pollution.
## No-Code System
This implementation requires zero code. All operations are driven through natural language commands:
/wiki-ingest — Ingest a new document
/wiki-query — Ask a question
/wiki-lint — Check wiki health
No Python. No dependencies. No installation. Just natural language commands that drive intelligent agents.
## Human-Centric Workflow
### Humans Review Everything
The wiki's human-gated compounding loop ensures quality:
Automated generation → Human review → Integration ↓ ↓ ↓

---

## Page 3

@wiki-querier questions_pending/ wiki/synthesis/ @wiki-linter lint_pending/ wiki pages updated
You decide:
Which auto-generated answers are good enough to integrate
Which lint suggestions should be applied
Which questions deserve synthesis pages
### Manual Editing (Advanced)
While the system is designed for no-code operation, you can manually edit markdown files if needed:
Edit , , wiki/sources/*.md wiki/entities/*.md wiki/concepts/*.md directly
Add connections, refine definitions, clarify relationships
Fix formatting, update updated: timestamps
Discouraged but feasible — Manual edits bypass the structure-checking that the ingestor provides. Use only when you understand the page format and wiki conventions. For most use cases, let the automated agents handle ingestion.
### Quick Start
1. Open the project in your IDE (Claude Code or VS Code with appropriate LLM integration)
2. Place a document in raw/my-guide.md
3. Ingest it:
/wiki-ingest
4. Ask questions:
/wiki-query What are the key concepts?
5. Check health:
/wiki-lint
Move answers from questions_pending/ → questions_approved/
Run /wiki-ingest to integrate them as synthesis pages
### Example Files
The bak/ directory contains ready-to-use example documents for testing the wiki:
1. afw-instructions.md — Technical documentation (Microsoft Agent Framework best practices)

---

## Page 4

### 2. mfa_agents_howto.md — How-to guide documentation (Microsoft Agent Framework agents)
### 3. ARCH_BOOKING_PLATFORM.md — Simulated application requirements (Corporate Booking Platform
### architecture)
To test the wiki, copy any of these files to raw/ and ingest:
cp bak/ARCH_BOOKING_PLATFORM.md raw/ /wiki-ingest
### These examples demonstrate how the wiki extracts entities, concepts, and relationships from diverse source
### documents.
## Directory Layout
| wiki/ | ← Living knowledge base |
|---|---|
| ├── index.md | ← Catalog of all pages |
| ├── log.md | ← Operation audit trail |
| ├── sources/ | ← One page per ingested document |
| ├── entities/ | ← Named, identifiable things (tools, people, companies) |
| ├── concepts/ | ← Abstract ideas and patterns |
| └── synthesis/ | ← Approved answers from your questions |
| raw/ | ← Documents awaiting ingestion (immutable) |
| questions_pending/ | ← Auto-generated answers (awaiting your review) |
| questions_approved/ | ← Answers you've validated (ready to integrate) |
| lint_pending/ | ← Wiki health reports (awaiting your review) |
| lint_approved/ | ← Fixes you've approved (ready to apply) |
| docs/ | ← Specifications and planning |
wiki/ ← Living knowledge base
raw/ ← Documents awaiting ingestion (immutable)
questions_pending/ ← Auto-generated answers (awaiting your review) questions_approved/ ← Answers you've validated (ready to integrate)
lint_pending/ ← Wiki health reports (awaiting your review) lint_approved/ ← Fixes you've approved (ready to apply)
docs/ ← Specifications and planning
## The Three Operations
## /wiki-ingest — Build Your Knowledge Base
### Ingests raw documents and creates/updates wiki pages:
### Extracts entities (tools, companies, frameworks, etc.) and concepts (patterns, methodologies, ideas)
### Merges new information with existing pages
### Detects contradictions and flags them for review
### Updates the index and operation log
scan Input: File path, or for auto-ingest, or --RESET-ALL for destructive reset
## /wiki-query — Ask Questions

---

## Page 5

Answers your questions exclusively from wiki content:
Reads 3–8 relevant pages
Cites every claim with wikilinks
Never uses external knowledge or training data
Saves the answer for your review before integration
Input: A natural language question
## /wiki-lint — Maintain Health
Two-phase validation:
Phase 1 (Deterministic): Broken links, orphaned pages, missing frontmatter, empty sections
Phase 2 (Semantic): Contradictions, stale claims, missing pages, missing connections
Output: Detailed report with suggested fixes
## Key Features
Retrieval-only queries — No hallucinations, only what's in the wiki Human-gated approval — All auto-generated content requires review before integration Knowledge graph — Entities and concepts interconnect; trace relationships and sources Evergreen content — Track creation/update dates, detect stale information Zero information loss — Preserve code blocks verbatim, include full context Structured extraction — Entities vs. concepts, clear page types and relationships Audit trail — Every operation logged with timestamps and pages touched English-only wiki — Consistent language for cross-source comparison (translates non-English inputs)
## Specifications & Documentation
SPEC_LLM_WIKI_CC.md — Complete technical specification
SPEC_LLM_WIKI_GHB.md — Reference implementation (GitHub Copilot version)
COMPATIBILITY_ANALYSIS.md — Comparison and migration guide
## Project Configuration Files
## .claude/ — Claude Code Configuration
File Purpose
CLAUDE.md Project instructions and behavioral constraints
settings.json Command registration and harness configuration

---

## Page 6

File Purpose
commands/wiki-ingest.md /wiki-ingest command workflow definition
commands/wiki-query.md /wiki-query command workflow definition
commands/wiki-lint.md /wiki-lint command workflow definition
## .github/ — GitHub Copilot Configuration
File Purpose
prompts/wiki-ingest.prompt.md LLM prompt for ingest command
prompts/wiki-query.prompt.md LLM prompt for query command
prompts/wiki-lint.prompt.md LLM prompt for lint command
instructions/wiki-schema.instructions.md Shared page format and schema documentation
agents/wiki-ingestor.agent.md Ingestor agent definition
agents/wiki-querier.agent.md Querier agent definition
agents/wiki-linter.agent.md Linter agent definition
## Design Philosophy
Knowledge without pollution — Your wiki grows only from sources you feed it. No training data, no synthesis, no hallucinations.
Structured for retrieval — Entities, concepts, and sources are distinct. You know where every claim came from.
Human in the loop — Machines generate, humans decide. Before any auto-generated content enters the wiki, you review it.
Audit everything — Every ingest, query, and lint operation is logged. You can trace what was added, when, and from where.
## Getting Started
1. Read SPEC_LLM_WIKI_CC.md for a quick overview
2. Place your first document in raw/
3. Run /wiki-ingest and watch your wiki grow
4. Run /wiki-query to test retrieval
5. Use /wiki-lint to maintain quality

---

## Page 7

### Based On
Andrej Karpathy's LLM Wiki Gist — The foundational vision for building a personal knowledge base that grows through ingestion, connection, and curation.
Releases
No releases published Create a new release
Packages
No packages published Publish your first package
Contributors
No contributors