#!/usr/bin/env python3
"""Jev triage of the owner's planning documents: which memory-system topics each document covers.

Judgments from Jev (one Noul per topic, since a document can cover several); decisions in code (thresholds below).
Uses jev-core's client (redaction, https-only endpoint, deadline). Output: jev-triage.jsonl + JEV-TRIAGE.md.
Run: python3 jev_triage.py <clean_md dir> [workers]
"""
import json, os, sys, glob, concurrent.futures as cf

sys.path.insert(0, "/data/data/com.termux/files/home/repos/NovAExopia-main/plugins/nvaex-jev-core/scripts")
import jev_route as J  # noqa: E402

YES, NO = 0.7, 0.3          # Noul thresholds (skill guidance); between = unsettled
HEAD = 6000                 # characters of each document sent as state
TOPICS = {  # all question wording in one place
    "router": "Does `document` describe how requests are routed between models, tools or agents (for example OmniRoute, Jev routing, a small local router model, OpenRouter)?",
    "episodic": "Does `document` describe episodic memory: a record of sessions, events or actions over time (for example mem0 or an execution timeline)?",
    "semantic_static": "Does `document` describe static or semantic memory: settled facts, rules or governing principles kept long term (for example OB1, Terrestrial Brain, a facts store)?",
    "sha256_postgres": "Does `document` describe storing content by SHA-256 hash or in Postgres / Supabase tables?",
    "code_graph": "Does `document` describe parsing code into a graph or syntax tree (for example tree-sitter, code-review-graph, AST)?",
    "knowledge_graph": "Does `document` describe a knowledge graph over notes or documents (for example Graphify, Obsidian graph, NotebookLM)?",
    "rlm_vectors": "Does `document` describe recursive fragmentation of large inputs, vector embeddings, or vector-graph categorization (for example RLM, Prime Agent, holograph, EmbeddingGemma)?",
    "harness_identity": "Does `document` describe the agent's core harness or identity layer (for example a continual harness, a reasoning bank, or an agent package that keeps state outside the model)?",
    "wiki_admin": "Does `document` describe the wiki admin agent (greedy-crane): ingesting documents, converting them, staging and promoting wiki pages?",
    "enforcement": "Does `document` describe rules, stop gates, hooks or audits that force an agent to follow a protocol?",
    "cloud_storage": "Does `document` describe hosting or storage on a cloud service (for example Cloudflare, Google Cloud buckets, Docker, Supabase)?",
    "vendor_product_doc": "Is `document` a vendor's own product documentation (for example TypeSafe Jev API docs or SDK reference), rather than the owner's own plan or design?",
}

def questions():
    return {k: {"type": "noul", "instructions": v} for k, v in TOPICS.items()}

def ask(path, root, key):
    rel = os.path.relpath(path, root)
    with open(path, encoding="utf-8", errors="replace") as f:
        text = f.read()
    clean, n = J.redact_outbound(text[:HEAD])
    body = json.dumps({"model": os.environ.get("TYPESAFE_DEFAULT_MODEL") or J.MODEL,
                       "state": {"document": {"path": rel, "text": clean}},
                       "questions": questions()}).encode()
    try:
        data, rid = J.post(body, key, 30)
        a = json.loads(data)["answers"]
        p = {k: round(float(a[k]["noul"]), 3) for k in TOPICS}
        return {"path": rel, "chars": len(text), "request_id": rid, "redacted": n, "p": p,
                "yes": [k for k, v in p.items() if v >= YES],
                "unsettled": [k for k, v in p.items() if NO < v < YES]}
    except Exception as e:  # a failed call is an error, never a "no"
        return {"path": rel, "error": getattr(e, "reason", type(e).__name__)}

def main():
    root = sys.argv[1]
    workers = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    key = J.api_key()
    if not key:
        sys.exit("no TYPESAFE_API_KEY")
    files = sorted(p for p in glob.glob(os.path.join(root, "**", "*.md"), recursive=True) if "/_reports/" not in p and os.path.isfile(p))
    out = os.path.join(os.path.dirname(root.rstrip("/")), "jev-triage.jsonl")
    rows = []
    with cf.ThreadPoolExecutor(workers) as ex:
        for r in ex.map(lambda p: ask(p, root, key), files):
            rows.append(r)
    with open(out, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")
    errs = [r for r in rows if "error" in r]
    ok = [r for r in rows if "error" not in r]
    lines = ["# Jev triage of the planning documents", "",
             f"{len(files)} documents, {len(ok)} answered, {len(errs)} errors. Noul yes >= {YES}, no <= {NO}.", "",
             "## Documents per topic (yes)", ""]
    for k in TOPICS:
        hits = [r["path"] for r in ok if k in r["yes"]]
        lines.append(f"### {k} ({len(hits)})")
        lines += [f"- {h}" for h in hits] or ["- none"]
        lines.append("")
    lines += ["## Owner's own docs that hit no topic", ""]
    lines += [f"- {r['path']}" for r in ok if not r["yes"]] or ["- none"]
    lines += ["", "## Errors", ""] + ([f"- {r['path']}: {r['error']}" for r in errs] or ["- none"])
    md = os.path.join(os.path.dirname(out), "JEV-TRIAGE.md")
    with open(md, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"{len(ok)} ok, {len(errs)} errors -> {out}, {md}")

if __name__ == "__main__":
    main()
