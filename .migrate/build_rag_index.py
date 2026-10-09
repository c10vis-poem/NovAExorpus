#!/usr/bin/env python3
"""Build a local BM25 search index over RAG_LIBRARY/*.jsonl chunks.

BM25 (pure statistical ranking) needs no external model or network access:
the standard retrieval baseline in most RAG systems. Stdlib only.

Writes:
  RAG_LIBRARY/_index/bm25.json  -- {"k1", "b", "avgdl", "df": {term: n}, "docs": [{term: tf}], "lens": [n]}
  RAG_LIBRARY/_index/meta.jsonl -- one line per chunk, same order,
                                    {source, chunk_index, heading, text}
JSON, not pickle: loading a pickle can run code hidden in the file.
Query with query_rag.py.
"""
import os, sys, json, glob, re
from collections import Counter

K1, B = 1.5, 0.75   # rank_bm25 BM25Okapi defaults

def load_chunks(rag_root):
    chunks = []
    for path in sorted(glob.glob(os.path.join(rag_root, "**", "*.jsonl"), recursive=True)):
        if f"{os.sep}_index{os.sep}" in path:
            continue
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    chunks.append(json.loads(line))
    return chunks

def tokenize(text):
    return re.findall(r"[a-z0-9]+", text.lower())

def main(rag_root):
    chunks = load_chunks(rag_root)
    print(f"Loaded {len(chunks)} chunks from {rag_root}")

    docs = [Counter(tokenize(c["text"])) for c in chunks]
    lens = [sum(d.values()) for d in docs]
    df = Counter(t for d in docs for t in d)
    index = {"k1": K1, "b": B, "avgdl": (sum(lens) / len(lens)) if lens else 0.0,
             "df": df, "docs": docs, "lens": lens}

    out_dir = os.path.join(rag_root, "_index")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "bm25.json"), "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False)
    with open(os.path.join(out_dir, "meta.jsonl"), "w", encoding="utf-8") as f:
        for c in chunks:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")

    print(f"Wrote BM25 index over {len(chunks)} chunks to {out_dir}/bm25.json")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "RAG_LIBRARY")
