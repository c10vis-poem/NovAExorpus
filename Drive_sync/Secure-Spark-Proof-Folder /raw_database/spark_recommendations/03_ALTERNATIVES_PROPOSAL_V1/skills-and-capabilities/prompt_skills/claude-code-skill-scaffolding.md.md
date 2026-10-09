---
title: "claude-code-skill-scaffolding.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/03_ALTERNATIVES_PROPOSAL_V1/skills-and-capabilities/prompt_skills/claude-code-skill-scaffolding.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

---
name: claude-code-skill-scaffolding
description: Standardized procedure for scaffolding, structuring, and registering custom Claude
Code / Gemini skills into .claude/skills/ or repository skill planes.
---

# Instructions

## 1. Skill Directory Resolution
- Check if `.claude/skills/` exists in the current repo root.
- If absent, create it: `mkdir -p .claude/skills/`.

## 2. YAML Frontmatter Requirements
Every skill file MUST begin with strict YAML frontmatter:
```yaml
---
name: <kebab-case-name>
description: <concise summary of functionality and triggers>
---
```

## 3. Slash Command Registration
- When saved as `.claude/skills/<name>.md`, Claude Code automatically maps it to `/<name>`.
- The markdown body defines the step-by-step reasoning steps, tool usage constraints, and
output contract.
