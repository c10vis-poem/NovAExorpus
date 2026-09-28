#!/usr/bin/env python3
"""
markor_sweeper.py — Unregistered Note Sweeper & Context Hygiene Daemon (obsidian-skills)

Scans incoming notes (e.g. mobile Markor scratchpads, quick notes) against
the repository manifest, detects unindexed assets, missing frontmatter,
and sensitive credential patterns to prevent context leaks into LLM prompts.

Usage:
    python3 markor_sweeper.py --dir /path/to/notes --manifest manifest.jsonl
    python3 markor_sweeper.py --dir /path/to/notes --quarantine /path/to/quarantine
"""

import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Set


SENSITIVE_PATTERNS = [
    (r'(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*[\'"][A-Za-z0-9_\-\.]{12,}[\'"]', "High-entropy API token/key"),
    (r'(?i)ya29\.[A-Za-z0-9_\-]+', "Google OAuth access token"),
    (r'(?i)ghp_[A-Za-z0-9]{36}', "GitHub Personal Access Token"),
    (r'(?i)-----BEGIN\s+(?:RSA\s+)?PRIVATE\s+KEY-----', "Private cryptographic key"),
]


def load_manifest_filenames(manifest_path: Path) -> Set[str]:
    registered = set()
    if not manifest_path.exists():
        return registered
    try:
        for line in manifest_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            record = json.loads(line)
            if "filename" in record:
                registered.add(record["filename"])
            elif "path" in record:
                registered.add(Path(record["path"]).name)
    except Exception as e:
        sys.stderr.write(f"Warning: Could not parse manifest {manifest_path}: {e}\n")
    return registered


def sweep_notes(notes_dir: Path, registered_files: Set[str]) -> Dict[str, Any]:
    unregistered: List[Dict[str, Any]] = []
    missing_frontmatter: List[str] = []
    sensitive_leaks: List[Dict[str, Any]] = []
    total_scanned = 0

    for file_path in notes_dir.rglob("*.md"):
        if any(p.startswith(".") for p in file_path.parts):
            continue
        total_scanned += 1
        rel_path = str(file_path.relative_to(notes_dir))
        
        # 1. Manifest check
        if file_path.name not in registered_files and rel_path not in registered_files:
            unregistered.append({
                "filename": file_path.name,
                "relative_path": rel_path,
                "size_bytes": file_path.stat().st_size
            })

        # 2. Content checks
        try:
            content = file_path.read_text(encoding="utf-8", errors="replace")
            if not content.startswith("---"):
                missing_frontmatter.append(rel_path)

            for pattern, desc in SENSITIVE_PATTERNS:
                matches = re.findall(pattern, content)
                if matches:
                    sensitive_leaks.append({
                        "file": rel_path,
                        "leak_type": desc,
                        "matches_count": len(matches)
                    })
        except Exception as err:
            sys.stderr.write(f"Warning: Failed reading {file_path}: {err}\n")

    return {
        "notes_directory": str(notes_dir.resolve()),
        "total_scanned": total_scanned,
        "unregistered_count": len(unregistered),
        "unregistered_files": unregistered,
        "missing_frontmatter_count": len(missing_frontmatter),
        "missing_frontmatter": missing_frontmatter,
        "sensitive_leaks_count": len(sensitive_leaks),
        "sensitive_leaks": sensitive_leaks
    }


def format_markdown(data: Dict[str, Any]) -> str:
    md = [
        f"# Markor Note Sweeper & Hygiene Report",
        f"**Scanned Directory:** `{data['notes_directory']}`  ",
        f"**Total Notes:** {data['total_scanned']} | **Unregistered:** {data['unregistered_count']} | **Missing Frontmatter:** {data['missing_frontmatter_count']} | **Sensitive Leaks:** {data['sensitive_leaks_count']}\n"
    ]

    if data["sensitive_leaks"]:
        md.append("## 🚨 SENSITIVE DATA DETECTED (QUARANTINE REQUIRED)")
        for leak in data["sensitive_leaks"]:
            md.append(f"- **{leak['file']}**: {leak['leak_type']} ({leak['matches_count']} occurrences)")
        md.append("")

    if data["unregistered_files"]:
        md.append("## Unregistered Notes (Missing from Manifest)")
        md.append("| Note Name | Relative Path | Size |")
        md.append("| :--- | :--- | :--- |")
        for u in data["unregistered_files"]:
            md.append(f"| `{u['filename']}` | `{u['relative_path']}` | {u['size_bytes']} B |")
        md.append("")

    if data["missing_frontmatter"]:
        md.append("## Notes Missing YAML Frontmatter")
        for f in data["missing_frontmatter"][:10]:
            md.append(f"- `{f}`")
        if len(data["missing_frontmatter"]) > 10:
            md.append(f"- *...and {len(data['missing_frontmatter']) - 10} more notes.*")

    return "\n".join(md)


def main():
    parser = argparse.ArgumentParser(description="Markor Sweeper & Context Hygiene Tool")
    parser.add_argument("--dir", type=str, required=True, help="Directory to scan")
    parser.add_argument("--manifest", type=str, default="manifest.jsonl", help="Path to manifest.jsonl")
    parser.add_argument("--format", type=str, choices=["json", "md"], default="md", help="Output format")
    parser.add_argument("--output", type=str, default=None, help="Output destination file")

    args = parser.parse_args()
    scan_dir = Path(args.dir)
    manifest_path = Path(args.manifest)

    if not scan_dir.is_dir():
        sys.stderr.write(f"Error: Target directory does not exist: {args.dir}\n")
        sys.exit(1)

    registered = load_manifest_filenames(manifest_path)
    report = sweep_notes(scan_dir, registered)

    if args.format == "json":
        output = json.dumps(report, indent=2)
    else:
        output = format_markdown(report)

    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
        print(f"Hygiene report written to {args.output}")
    else:
        print(output)

    # Exit with code 1 if critical sensitive leaks are found
    if report["sensitive_leaks_count"] > 0:
        sys.exit(2)
    sys.exit(0)


if __name__ == "__main__":
    main()
[markor_sweeper](_res/markor_sweeper.py)