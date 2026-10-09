#!/usr/bin/env python3
"""Query the local BM25 RAG index built by build_rag_index.py.
Usage: python3 query_rag.py "your query here" [top_k] [rag_root]
No network needed -- pure statistical ranking (BM25 Okapi), stdlib only.
"""
import sys, os, json, re, math

def tokenize(text):
    return re.findall(r"[a-z0-9]+", text.lower())

def scores(index, query):
    n, k1, b, avgdl = len(index["docs"]), index["k1"], index["b"], index["avgdl"] or 1.0
    df = index["df"]
    # BM25Okapi idf, with negative idf floored at eps * mean idf (as rank_bm25 does)
    idf = {t: math.log(n - d + 0.5) - math.log(d + 0.5) for t, d in df.items()}
    eps = 0.25 * (sum(idf.values()) / len(idf)) if idf else 0.0
    idf = {t: (v if v >= 0 else eps) for t, v in idf.items()}
    terms = tokenize(query)
    out = []
    for tf, dl in zip(index["docs"], index["lens"]):
        s = 0.0
        for t in terms:
            f = tf.get(t, 0)
            if f:
                s += idf.get(t, 0.0) * f * (k1 + 1) / (f + k1 * (1 - b + b * dl / avgdl))
        out.append(s)
    return out

def main(rag_root, query, top_k):
    idx_dir = os.path.join(rag_root, "_index")
    with open(os.path.join(idx_dir, "bm25.json"), encoding="utf-8") as f:
        index = json.load(f)
    with open(os.path.join(idx_dir, "meta.jsonl"), encoding="utf-8") as f:
        meta = [json.loads(line) for line in f]

    sc = scores(index, query)
    top_indices = sorted(range(len(sc)), key=lambda i: -sc[i])[:top_k]

    for rank, i in enumerate(top_indices, 1):
        m = meta[i]
        md = m.get("metadata") or {}   # condensed chunks nest source/heading under metadata
        src, head = m.get("source") or md.get("source", "?"), m.get("heading") or md.get("heading")
        print(f"\n--- #{rank} (score={sc[i]:.2f}) {src} :: {head or '(no heading)'} ---")
        print(m["text"][:500])

if __name__ == "__main__":
    query = sys.argv[1]
    top_k = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    main(sys.argv[3] if len(sys.argv) > 3 else "RAG_LIBRARY", query, top_k)
