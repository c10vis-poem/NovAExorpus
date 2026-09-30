#!/usr/bin/env python3
"""Query the local BM25 RAG index built by build_rag_index.py.
Usage: python3 query_rag.py "your query here" [top_k]
No network needed -- pure statistical ranking, runs anywhere.
"""
import sys, os, json, pickle, re

def tokenize(text):
    return re.findall(r"[a-z0-9]+", text.lower())

def main(rag_root, query, top_k):
    idx_dir = os.path.join(rag_root, "_index")
    with open(os.path.join(idx_dir, "bm25.pkl"), "rb") as f:
        bm25 = pickle.load(f)
    with open(os.path.join(idx_dir, "meta.jsonl"), encoding="utf-8") as f:
        meta = [json.loads(line) for line in f]

    scores = bm25.get_scores(tokenize(query))
    top_indices = sorted(range(len(scores)), key=lambda i: -scores[i])[:top_k]

    for rank, i in enumerate(top_indices, 1):
        m = meta[i]
        print(f"\n--- #{rank} (score={scores[i]:.2f}) {m['source']} :: {m.get('heading') or '(no heading)'} ---")
        print(m["text"][:500])

if __name__ == "__main__":
    query = sys.argv[1]
    top_k = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    main("RAG_LIBRARY", query, top_k)
