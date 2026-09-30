#!/usr/bin/env python3
"""
graph_sync.py — Obsidian Graph View & Wikilink Synchronizer (obsidian-skills)

Scans markdown vaults, extracts [[wikilinks]] and #tags, verifies graph integrity,
detects dangling references, and generates Obsidian graph visualization metadata.

Usage:
    python3 graph_sync.py --dir /path/to/vault --format md --output graph_report.md
    python3 graph_sync.py --dir /path/to/vault --format json --output obsidian_graph.json
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Set


def extract_wikilinks(text: str) -> List[str]:
    # Match [[target]] or [[target|alias]]
    pattern = r'\[\[(.*?)\]\]'
    matches = re.findall(pattern, text)
    links = []
    for m in matches:
        target = m.split('|')[0].split('#')[0].strip()
        if target:
            links.append(target)
    return links


def extract_tags(text: str) -> List[str]:
    # Inline hashtags: #concept/architecture (excluding header lines '# Header')
    pattern = r'(?<!\S)#([a-zA-Z0-9_\-\/]+)'
    raw_tags = re.findall(pattern, text)
    return sorted(list(set(raw_tags)))


def audit_vault_graph(vault_dir: Path) -> Dict[str, Any]:
    nodes: Dict[str, Dict[str, Any]] = {}
    edges: List[Dict[str, str]] = []
    all_note_names: Set[str] = set()

    # Pass 1: Index existing note stems
    for path in vault_dir.rglob("*.md"):
        if any(p.startswith(".") for p in path.parts):
            continue
        all_note_names.add(path.stem)
        rel = str(path.relative_to(vault_dir))
        nodes[path.stem] = {
            "relative_path": rel,
            "title": path.stem,
            "links": [],
            "tags": [],
            "dangling_links": []
        }

    # Pass 2: Extract links and check targets
    for path in vault_dir.rglob("*.md"):
        if any(p.startswith(".") for p in path.parts):
            continue
        stem = path.stem
        try:
            content = path.read_text(encoding="utf-8", errors="replace")
            links = extract_wikilinks(content)
            tags = extract_tags(content)
            nodes[stem]["tags"] = tags

            for target in links:
                nodes[stem]["links"].append(target)
                if target in all_note_names:
                    edges.append({"source": stem, "target": target})
                else:
                    nodes[stem]["dangling_links"].append(target)
        except Exception as e:
            nodes[stem]["error"] = str(e)

    total_dangling = sum(len(n["dangling_links"]) for n in nodes.values())

    return {
        "vault_path": str(vault_dir.resolve()),
        "total_notes": len(nodes),
        "total_edges": len(edges),
        "total_dangling_links": total_dangling,
        "nodes": nodes,
        "edges": edges
    }


def format_markdown(data: Dict[str, Any]) -> str:
    md = [
        f"# Obsidian Vault Graph Synchronization Report",
        f"**Vault Path:** `{data['vault_path']}`  ",
        f"**Indexed Notes:** {data['total_notes']} | **Active Links:** {data['total_edges']} | **Dangling Links:** {data['total_dangling_links']}\n",
        "## Vault Network Density",
        "| Note | In-Vault Links | Tags | Dangling References |",
        "| :--- | :--- | :--- | :--- |"
    ]
    for stem, info in sorted(data["nodes"].items()):
        links_count = len(info["links"]) - len(info["dangling_links"])
        tags_str = ", ".join(info["tags"][:3]) or "-"
        dangling_str = ", ".join([f"`[[{d}]]`" for d in info["dangling_links"]]) or "None"
        md.append(f"| **{stem}** | {links_count} | {tags_str} | {dangling_str} |")

    return "\n".join(md)


def main():
    parser = argparse.ArgumentParser(description="Obsidian Graph Synchronization Engine")
    parser.add_argument("--dir", type=str, required=True, help="Path to markdown vault")
    parser.add_argument("--format", type=str, choices=["json", "md"], default="md", help="Output format")
    parser.add_argument("--output", type=str, default=None, help="Output destination file")

    args = parser.parse_args()
    vault = Path(args.dir)
    if not vault.is_dir():
        sys.stderr.write(f"Error: Vault path is not a directory: {args.dir}\n")
        sys.exit(1)

    graph_data = audit_vault_graph(vault)

    if args.format == "json":
        output = json.dumps(graph_data, indent=2)
    else:
        output = format_markdown(graph_data)

    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
        print(f"Graph sync report written to {args.output}")
    else:
        print(output)

    sys.exit(0)


if __name__ == "__main__":
    main()
