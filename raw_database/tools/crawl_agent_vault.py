#!/usr/bin/env python3
import os
import json
from datetime import datetime


def crawl_agent_vault(vault_path):
    audit_log = []

    # Critical folders to look out for duplication conflicts
    target_keywords = ['skill', 'migrate', 'duplicate', 'archive', 'depricated']

    print(f"🚀 Commencing Agent-OS Database Crawl across: {vault_path}\n")

    for root, dirs, files in os.walk(vault_path):
        # Exclude hidden system folders from wasting compute
        dirs[:] = [d for d in dirs if not d.startswith('.git') and not d == 'zARCHIVE']

        for directory in dirs:
            dir_path = os.path.join(root, directory)
            lowercase_name = directory.lower()

            # Check for structural anomalies or stale targets
            matched_flags = [word for word in target_keywords if word in lowercase_name]

            if matched_flags:
                stat_info = os.stat(dir_path)
                mod_time = datetime.fromtimestamp(stat_info.st_mtime).strftime('%Y-%m-%d')

                audit_entry = {
                    "path": os.path.relpath(dir_path, vault_path),
                    "detected_flags": matched_flags,
                    "last_modified": mod_time,
                    "action_required": "Review for redundancy / merge into Unified Core"
                }
                audit_log.append(audit_entry)
                print(f"⚠️  CONFLICT FOUND: [{directory}] -> Last Modified: {mod_time}")

    # Write out the results as an actionable JSONL payload for your agents
    output_path = os.path.join(vault_path, "potential_redundancies.jsonl")
    with open(output_path, "w", encoding="utf-8") as f:
        for entry in audit_log:
            f.write(json.dumps(entry) + "\n")

    print(f"\n🎯 Crawl finished! Structural redundancy report compiled to: {output_path}")


# To run this, replace with the absolute path to your cloned Drive workspace
# crawl_agent_vault("/path/to/__Lex-Novi-Æxentis-Copiæ")
