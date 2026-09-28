#!/usr/bin/env python3
import json, os, sys

root = sys.argv[1] if len(sys.argv) > 1 else "RAG_LIBRARY"
total_files = 0
total_lines = 0
broken = []
for dirpath, dirnames, filenames in os.walk(root):
    for fn in filenames:
        if not fn.endswith(".jsonl"):
            continue
        path = os.path.join(dirpath, fn)
        total_files += 1
        try:
            with open(path, encoding="utf-8") as f:
                n = 0
                for line in f:
                    if line.strip():
                        json.loads(line)
                        n += 1
                total_lines += n
                if n == 0:
                    broken.append((path, "zero valid lines"))
        except Exception as e:
            broken.append((path, str(e)))

print(f"Checked {total_files} jsonl files, {total_lines} total chunk lines")
if broken:
    print(f"BROKEN ({len(broken)}):")
    for p, e in broken:
        print(f"  {p}: {e}")
else:
    print("All files valid.")
