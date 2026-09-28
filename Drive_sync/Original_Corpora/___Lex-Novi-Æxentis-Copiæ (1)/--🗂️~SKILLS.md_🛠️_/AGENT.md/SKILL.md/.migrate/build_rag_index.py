#!/usr/bin/env python3
"""Build a local BM25 search index over RAG_LIBRARY/*.jsonl chunks.

Uses BM25 (pure statistical ranking, via rank_bm25) instead of neural
embeddings: this environment's network policy blocks HuggingFace's model
storage backend (cas-server.xethub.hf.co) outright, so any
sentence-transformers/embedding model download fails regardless of which
model is picked. BM25 needs no external model or network access at all --
it's a real, widely-used production retrieval method (the standard
baseline/hybrid component in most RAG systems), not a downgrade hack.

Writes:
  RAG_LIBRARY/_index/bm25.pkl   -- pickled BM25Okapi index
  RAG_LIBRARY/_index/meta.jsonl -- one line per chunk, same order,
                                    {source, chunk_index, heading, text}
Query with query_rag.py.
"""
import os, sys, json, glob, pickle, re
from rank_bm25 import BM25Okapi

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

    corpus_tokens = [tokenize(c["text"]) for c in chunks]
    bm25 = BM25Okapi(corpus_tokens)

    out_dir = os.path.join(rag_root, "_index")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "bm25.pkl"), "wb") as f:
        pickle.dump(bm25, f)
    with open(os.path.join(out_dir, "meta.jsonl"), "w") as f:
        for c in chunks:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")

    print(f"Wrote BM25 index over {len(chunks)} chunks to {out_dir}/bm25.pkl")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "RAG_LIBRARY")
