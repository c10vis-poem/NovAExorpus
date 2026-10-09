#!/usr/bin/env python3
"""
AESOP XI JSONL Marker Generator — Phone-Only, Termux-Native
Reads markdown files from vault, outputs universal-index.jsonl
Usage: generate_jsonl_markers.py [VAULT_DIR] [OUTPUT_FILE]
Independent second indexer (one record per whole document) used to cross-check
build_rag_chunks.py output: a tool never verifies its own work.
Source: Drive_sync/.../3-FILES-MGMT16-SCRIPTS-(16-files)/JSONL labeling .txt
"""
import json
from pathlib import Path
import sys
from datetime import datetime, timezone

VAULT_DIR = Path(sys.argv[1] if len(sys.argv) > 1 else "~/obsidian-vault-new").expanduser()
OUTPUT_FILE = Path(sys.argv[2] if len(sys.argv) > 2 else "~/file-management-and-skills/universal-index.jsonl").expanduser()

def extract_metadata(md_path: Path) -> dict:
    """Parse markdown headers and first paragraph for metadata."""
    content = md_path.read_text(encoding="utf-8")
    lines = content.split("\n")
    
    title = md_path.stem
    description = ""
    headers = []
    retrieval_tokens = set()
    
    in_code, have_title = False, False
    for i, line in enumerate(lines):
        if line.lstrip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue                      # code comments are not headings
        if line.startswith("# "):
            if not have_title:            # first H1 is the title
                title, have_title = line.lstrip("# ").strip(), True
        elif line.startswith("## ") or line.startswith("### "):
            headers.append(line.lstrip("# ").strip())
            # Add header words as retrieval tokens
            for word in line.lstrip("# ").strip().lower().split():
                if len(word) > 3:
                    retrieval_tokens.add(word)
        elif not description and line.strip() and not line.startswith("#"):
            description = line.strip()[:200]
    
    return {
        "title": title,
        "description": description,
        "headers": headers,
        "retrieval_tokens": list(retrieval_tokens)[:10],
        "content_chunk": content
    }

def generate_record(md_path: Path, idx: int) -> dict:
    meta = extract_metadata(md_path)
    return {
        "record_id": f"DOC_{md_path.stem.upper()[:40]}_{idx:03d}",
        "document_path": str(md_path),
        "category": "TECHNICAL_REFERENCE",
        "target_runtime": "QUERY_CORE_9B",
        "metadata": {
            "title": meta["title"],
            "description": meta["description"],
            "primary_tools": [],
            "required_context_keys": meta["headers"][:5]
        },
        "retrieval_tokens": meta["retrieval_tokens"],
        "entry_points": {
            "repl_command": f"/skill run {meta['title'].lower().replace(' ', '-')}",
            "jsonrpc_method": "agent.skills.execute"
        },
        "content_chunk": meta["content_chunk"],
        "generated_at": datetime.now(timezone.utc).isoformat()
    }

def main():
    md_files = list(VAULT_DIR.rglob("*.md"))
    print(f"Found {len(md_files)} markdown files")
    
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for i, md_path in enumerate(md_files):
            record = generate_record(md_path, i)
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
            print(f"  [{i+1}/{len(md_files)}] {md_path.name}")
    
    print(f"\nDone. Output: {OUTPUT_FILE}")
    print(f"Records: {len(md_files)}")

if __name__ == "__main__":
    main()
