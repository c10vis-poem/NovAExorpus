
## Page 1

## skills-and-capabilities — Procedural Skill & MCP Tool Registry
##  
### System Role & Authority
This repository serves as the central procedural knowledge base. It contains
standardized SKILL.md packages, Model Context Protocol MCP server
definitions, and reusable prompt templates.
### Architecture & Subsystems
The repository is organized into the following directories and subsystems:
### skills/
Procedural skills adhering to the SKILL.md specification:
Skill Description
memory-as-skill Scoped Markdown memory
management with strict stop comments.
mobile-grep Low-overhead grep search with
dynamic prompt variable injection.
task-observer One Skill to Rule Them All behavioral
supervisor and staged proposals.
obsidian-skills Obsidian markdown, Bases, and JSON
Canvas processing suite.
notebooklm-sync Bi-directional AST code graph sync with
Google NotebookLM.

---

## Page 2

## mcp/
Contains server configuration JSON schemas for the following:
● Code Review Graph
● Mem0
● Terrestrial Brain
● Filesystem
## Additional Subsystems
● prompt_templates/: Reusable agent prompt templates and
chain-of-thought scaffolds.
● tools/: Extracted helper tools and CLI wrappers.
● scripts/: Skill deployment and verification scripts.
● archive/: Deprecated or superseded skills.