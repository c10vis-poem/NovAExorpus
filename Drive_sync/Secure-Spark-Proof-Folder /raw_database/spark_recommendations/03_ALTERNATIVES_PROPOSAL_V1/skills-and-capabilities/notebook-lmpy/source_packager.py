#!/usr/bin/env python3
"""
source_packager.py — Multi-Document Source Bundler (notebook-lmpy)

Traverses markdown repositories, cleans formatting artifacts, validates
structure, and packages notes into curated analytical source bundles for
NotebookLM, LLM RAG pipelines, or offline vector ingestion.

Usage:
    python3 source_packager.py --dir /path/to/notes --output bundle.md
    python3 source_packager.py --dir /path/to/notes --format jsonl --output sources.jsonl
"""

import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, List


def calculate_sha256(content: str) -> str:
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def clean_markdown_content(raw_text: str, strip_yaml: bool = False) -> str:
    text = raw_text
    if strip_yaml and text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            text = parts[2].strip()
    
    # Normalize multiple blank lines
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def package_sources(source_dir: Path, max_tokens_per_file: int = 4000, strip_yaml: bool = False) -> List[Dict[str, Any]]:
    packaged_items = []
    if not source_dir.exists():
        sys.stderr.write(f"Source directory does not exist: {source_dir}\n")
        return packaged_items

    for file_path in sorted(source_dir.rglob("*.md")):
        if any(part.startswith(".") for part in file_path.parts):
            continue
        try:
            raw_text = file_path.read_text(encoding="utf-8", errors="replace")
            cleaned = clean_markdown_content(raw_text, strip_yaml=strip_yaml)
            approx_tokens = len(cleaned.split()) * 4 // 3
            
            item = {
                "filename": file_path.name,
                "relative_path": str(file_path.relative_to(source_dir)),
                "sha256": calculate_sha256(cleaned),
                "approx_tokens": approx_tokens,
                "content": cleaned
            }
            packaged_items.append(item)
        except Exception as err:
            sys.stderr.write(f"Warning: Failed to process {file_path}: {err}\n")

    return packaged_items


def main():
    parser = argparse.ArgumentParser(description="Curated Source Packager for NotebookLM")
    parser.add_argument("--dir", type=str, required=True, help="Input directory containing markdown files")
    parser.add_argument("--output", type=str, required=True, help="Output bundle file path")
    parser.add_argument("--format", type=str, choices=["md", "jsonl", "manifest"], default="md", help="Bundle output format")
    parser.add_argument("--strip-yaml", action="store_true", help="Remove YAML frontmatter from packaged notes")

    args = parser.parse_args()
    input_path = Path(args.dir)

    sources = package_sources(input_path, strip_yaml=args.strip_yaml)
    if not sources:
        sys.stderr.write("No markdown files found to package.\n")
        sys.exit(1)

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if args.format == "md":
        bundle_lines = [
            f"# Curated Source Bundle: {input_path.name}",
            f"**Generated Sources Count:** {len(sources)}  ",
            f"**Total Approx Tokens:** {sum(s['approx_tokens'] for s in sources)}\n",
            "---\n"
        ]
        for s in sources:
            bundle_lines.append(f"## SOURCE FILE: {s['relative_path']}")
            bundle_lines.append(f"*SHA-256:* `{s['sha256']}` | *Tokens:* ~{s['approx_tokens']}\n")
            bundle_lines.append(s["content"])
            bundle_lines.append("\n---\n")
        out_path.write_text("\n".join(bundle_lines), encoding="utf-8")

    elif args.format == "jsonl":
        with out_path.open("w", encoding="utf-8") as f:
            for s in sources:
                f.write(json.dumps(s) + "\n")

    elif args.format == "manifest":
        manifest_data = [{
            "filename": s["filename"],
            "relative_path": s["relative_path"],
            "sha256": s["sha256"],
            "approx_tokens": s["approx_tokens"]
        } for s in sources]
        out_path.write_text(json.dumps(manifest_data, indent=2), encoding="utf-8")

    print(f"Packaged {len(sources)} sources into {args.output} (Format: {args.format})")
    sys.exit(0)


if __name__ == "__main__":
    main()
