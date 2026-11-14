#!/usr/bin/env python3
"""Universal JSONL manifest: one line per file (file, path, sha256, size, summary).
Usage: wiki_admin.py [ROOT] [OUT]   (defaults: the vault, ./manifest.jsonl)
Adopted from Drive_sync/.../01-sources/DRIVE_FILES_MGMT16/wiki_admin.py (2026-10-08):
root/out are arguments, sha256 + size added, .git/.obsidian skipped.
"""
import hashlib, json, os, sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else "/storage/emulated/0/Documents/NovAExorpus"
OUT = sys.argv[2] if len(sys.argv) > 2 else "manifest.jsonl"
EXTS = (".md", ".jsonl", ".py", ".js", ".sh", ".txt")
SKIP = {".git", ".obsidian", ".trash"}

def build_manifest():
    n = 0
    with open(OUT, "w", encoding="utf-8") as f:
        for root, dirs, files in os.walk(ROOT):
            dirs[:] = sorted(d for d in dirs if d not in SKIP)
            for file in sorted(files):
                if not file.endswith(EXTS):
                    continue
                full_path = os.path.join(root, file)
                with open(full_path, "rb") as doc:
                    data = doc.read()
                first_line = data.split(b"\n", 1)[0].decode("utf-8", "ignore").strip()[:100]
                f.write(json.dumps({
                    "file": file,
                    "path": os.path.relpath(full_path, ROOT),
                    "sha256": hashlib.sha256(data).hexdigest(),
                    "size": len(data),
                    "summary": first_line or "No header found.",
                }, ensure_ascii=False) + "\n")
                n += 1
    print(f"Universal JSONL manifest: {n} files -> {OUT}")

if __name__ == "__main__":
    build_manifest()
