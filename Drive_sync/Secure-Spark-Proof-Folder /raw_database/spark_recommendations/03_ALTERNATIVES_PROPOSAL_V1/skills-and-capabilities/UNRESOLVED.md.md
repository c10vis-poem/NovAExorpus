---
title: "UNRESOLVED.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/03_ALTERNATIVES_PROPOSAL_V1/skills-and-capabilities/UNRESOLVED.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

UNRESOLVED.md — Backlog, Pending
Enhancements & Tickets
Subsystem: skills-and-capabilities

Active Backlog & Future Enhancements
[TICKET-SKILLS-01] TypeScript AST Full Parser Integration
-​
Subsystem: code-review-graph/
-​
Issue: graph_builder.py currently uses regex heuristics for JavaScript and
TypeScript imports and functions. While fast and zero-dependency, complex TypeScript
type declarations and dynamic re-exports can be missed.
-​
Proposal: Add an optional Node.js bridge to @babel/parser or typescript when
Node.js runtime is detected, falling back to Python regex on edge runtimes.
-​
Status: PENDING
[TICKET-SKILLS-02] Live NotebookLM API Remote Connector
-​
Subsystem: notebook-lmpy/
-​
Issue: query_notebook.py currently executes against local curated markdown
sources. A remote bridge to Google Workspace Gemini Notebook API endpoints can be
configured for live multi-document querying when network is enabled.
-​
Status: PENDING
[TICKET-SKILLS-03] Obsidian Canvas JSON Export
-​
Subsystem: obsidian-skills/
-​
Issue: graph_sync.py outputs standard JSON adjacency lists and Markdown tables.
Support for native Obsidian Canvas (.canvas) JSON layouts would allow visual node
drag-and-drop on desktop.
-​
Status: PENDING
[TICKET-SKILLS-04] Pre-Trend Scraper Daemon Automation
-​
Subsystem: early-trend-scraper/
-​
Issue: Implement background scheduled crontab hooks for daily_scraper.py and
tie its output telemetry directly into trending_databank.jsonl.
-​
Status: PENDING
