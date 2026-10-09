---
title: "file_mgmt_chunks.jsonl"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/03_ALTERNATIVES_PROPOSAL_V1/data_vault/03_recall_cache/file_mgmt_chunks.jsonl.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

{"chunk_id": "CHK_FM_001", "source":
"03_FILE_MANAGEMENT_AND_SCRIPTS_CANON.md", "topic": "rclone_mobile_sync",
"tokens": ["rclone", "sync", "termux", "gdrive", "oauth", "headless"], "content": "To pull cloud
documents into the local agent workspace without interactive browser popups, rclone operates
on Termux using pre-authenticated OAuth tokens: rclone sync
gdrive:Your_GDrive_Folder_Name ~/AgentWorkspace --fast-list --transfers 4"}
{"chunk_id": "CHK_FM_002", "source":
"03_FILE_MANAGEMENT_AND_SCRIPTS_CANON.md", "topic": "localized_grep_search",
"tokens": ["grep", "search", "mobile", "text", "regex"], "content": "Once synchronized, agents
execute localized grep searches across Markdown SOPs and JSONL logs, eliminating network
latency during real-time reasoning passes: grep -rn --color=auto '<keyword>'
~/AgentWorkspace/*.md ~/AgentWorkspace/*.jsonl"}
{"chunk_id": "CHK_FM_003", "source":
"03_FILE_MANAGEMENT_AND_SCRIPTS_CANON.md", "topic": "jsonl_marker_schema",
"tokens": ["jsonl", "marker", "schema", "record_id", "retrieval_tokens", "entry_points"], "content":
"Universal JSONL marker schema: record_id, document_path, category, target_runtime,
metadata (title, description, primary_tools, required_context_keys), retrieval_tokens,
entry_points"}
{"chunk_id": "CHK_FM_004", "source":
"03_FILE_MANAGEMENT_AND_SCRIPTS_CANON.md", "topic": "dumbass_git_hooks",
"tokens": ["git", "post_commit", "dumbass", "symlink", "regenerate_masters"], "content":
"Consumer repositories maintain synchronization with the Master Vault through automated Git
post-commit hooks: symlinks RESUME.md and CLAUDE.md into
~/novae-xorpus/projects/<consumer>/ and executes regenerate_masters.sh"}
