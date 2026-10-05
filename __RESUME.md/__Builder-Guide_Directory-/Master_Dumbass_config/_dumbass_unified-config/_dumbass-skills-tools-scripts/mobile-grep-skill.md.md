

## Page 1

# name: mobile-grep-skill description: Heuristic for localized text
# search across mobile markdown documents and JSONL logs
# using grep and dynamic prompt variables.
# Mobile File Text Search & Grep Skill
# System Intent
Autonomous operations agent with localized workspace access for parsing document structures, raw data payloads, and executing search tools.
# Workspace Partitioning
- PDF/ -> Static records, signed contracts, official whitepapers. - MD/ -> Standard Operating Procedures (SOPs), system manuals, wiki notes. - JSONL/ -> Raw execution logs, conversational history, retrieval chunks.
# Core Search Directives
.md 1. Primary Target: Scan and .jsonl formats first before deep archive traversal. 2. JSONL Unpacking: If a match is found in a .jsonl record, unpack the line and return only the matching key-value pairs to the user without dumping raw JSON boilerplate. 3. Dynamic Context Injection: - {{CURRENT_AGENT}}: Restrict file access to rows matching the active Agent ID unless clearance is Admin. - {{DEVICE_LOC}}: Log device coordinates with automated execution traces. - {{TARGET_DATE}}: Auto-filter JSONL logs matching the target ISO-8601 date prefix.
# Tool Invocation Contract
grep -rn --color=auto "<query>" ~/AgentWorkspace/*.md ~/AgentWorkspace/*.jsonl