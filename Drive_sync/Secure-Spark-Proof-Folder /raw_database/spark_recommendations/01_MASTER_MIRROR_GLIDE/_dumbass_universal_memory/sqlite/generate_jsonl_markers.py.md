---
title: "generate_jsonl_markers.py"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/01_MASTER_MIRROR_GLIDE/_dumbass_universal_memory/sqlite/generate_jsonl_markers.py.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

#!/usr/bin/env python3
"""
AESOP XI JSONL Marker Generator — Termux Native & Local Node
Reads markdown files from vault, extracts metadata and headers,
and outputs standardized universal-index.jsonl markers.
"""
import hashlib
import json
import os
import sys
from datetime import datetime
from pathlib import Path

def extract_metadata(file_path: Path) -> dict:
    content = file_path.read_text(encoding="utf-8", errors="ignore")
    title = file_path.stem
    headers = [line.strip("# ").strip() for line in content.splitlines() if line.startswith("#")]
    sha256 = hashlib.sha256(content.encode("utf-8")).hexdigest()

    return {
        "record_id": f"REC_{title.upper()[:16]}_{sha256[:8]}",
        "file_name": file_path.name,
        "path": str(file_path),
        "sha256": sha256,
        "title": headers[0] if headers else title,
        "section_count": len(headers),
        "file_size": len(content),
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

def process_directory(source_dir: str, output_file: str):
    p = Path(os.path.expanduser(source_dir))
    out = Path(os.path.expanduser(output_file))
    out.parent.mkdir(parents=True, exist_ok=True)

    with open(out, "w", encoding="utf-8") as f:
        for md_file in p.glob("**/*.md"):
            meta = extract_metadata(md_file)
            f.write(json.dumps(meta) + "\n")
    print(f"[✓] Generated JSONL markers in: {out}")

if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "."


    dest = sys.argv[2] if len(sys.argv) > 2 else "universal-index.jsonl"
    process_directory(src, dest)
