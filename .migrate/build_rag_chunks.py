#!/usr/bin/env python3
"""Chunk large/dense Markdown docs into JSONL for a RAG retrieval library.
Dedupes by content hash across the WHOLE vault (not per-folder) since the
same reference doc landing in 5 folders shouldn't produce 5x redundant
chunks in the retrieval index."""
import os, sys, re, json, hashlib, collections

WORD_THRESHOLD = 3000
CHUNK_WORDS = 500
OVERLAP_WORDS = 50
SKIP_DIRS = {".git", ".migrate", "_DUPLICATES_REVIEW", "RAG_LIBRARY"}

def iter_md_files(root):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if fn.endswith(".md"):
                yield os.path.join(dirpath, fn)

def split_by_headings(text):
    """Split on markdown ## headings; returns list of (heading, body)."""
    lines = text.split("\n")
    sections = []
    cur_heading, cur_lines = None, []
    for line in lines:
        if re.match(r"^#{1,3}\s+", line):
            if cur_lines:
                sections.append((cur_heading, "\n".join(cur_lines)))
            cur_heading = line.lstrip("#").strip()
            cur_lines = []
        else:
            cur_lines.append(line)
    if cur_lines:
        sections.append((cur_heading, "\n".join(cur_lines)))
    return sections if len(sections) > 1 else None

def chunk_words(text, size, overlap):
    words = text.split()
    if not words:
        return []
    chunks = []
    i = 0
    while i < len(words):
        chunks.append(" ".join(words[i:i + size]))
        i += size - overlap
    return chunks

def main(root, out_root):
    seen_hash = {}
    total_docs = 0
    total_chunks = 0
    for path in iter_md_files(root):
        with open(path, encoding="utf-8", errors="replace") as f:
            text = f.read()
        wc = len(text.split())
        if wc < WORD_THRESHOLD:
            continue
        h = hashlib.sha256(text.encode()).hexdigest()
        if h in seen_hash:
            continue  # same content already chunked from another folder
        seen_hash[h] = path

        rel = os.path.relpath(path, root)
        sections = split_by_headings(text)
        records = []
        if sections:
            idx = 0
            for heading, body in sections:
                for piece in chunk_words(body, CHUNK_WORDS, OVERLAP_WORDS):
                    if piece.strip():
                        records.append({"source": rel, "chunk_index": idx, "heading": heading, "text": piece})
                        idx += 1
        else:
            for idx, piece in enumerate(chunk_words(text, CHUNK_WORDS, OVERLAP_WORDS)):
                records.append({"source": rel, "chunk_index": idx, "heading": None, "text": piece})

        if not records:
            continue
        out_path = os.path.join(out_root, rel[:-3] + ".jsonl")
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w") as f:
            for r in records:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        total_docs += 1
        total_chunks += len(records)
        print(f"{rel}: {wc} words -> {len(records)} chunks")

    print(f"\nTOTAL: {total_docs} unique large docs chunked, {total_chunks} chunks written")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
