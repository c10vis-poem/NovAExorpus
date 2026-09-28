#!/usr/bin/env python3
"""Content-hash dedup with explicit, auditable precedence.

Keeps exactly one copy of each byte-identical file. Precedence is by
destination tier first, then by shallowest path, then by shortest name.
Everything removed is reported with the path that survived it.
"""
import hashlib, os, subprocess, sys, collections

ROOT = "/workspace/obsidian-master_wiki"

# tier 0 wins over tier 1 wins over tier 2 ...
TIERS = [
    ("canon/",),
    ("aesop/", "horizons-ui/", "skills/", "clis-and-agents/", "termux/",
     "global-documentation-vault/", "reverse-engineering/",
     "file-management-system/", "registries/", "github-ci-cd/",
     "pending-corpora/"),
    ("#Useful_knowledge_/",),
    ("#RESEARCH DOSSIER 1&2/",),
    ("RAG_LIBRARY/", "yJSONL_data.bank_/", "_DUPLICATES_REVIEW/"),
]

def tier(rel):
    for i, prefixes in enumerate(TIERS):
        if any(rel.startswith(p) for p in prefixes):
            return i
    return len(TIERS)

def rank(rel):
    # lower is better: tier, depth, path length
    return (tier(rel), rel.count("/"), len(rel), rel)

def main():
    os.chdir(ROOT)
    by_hash = collections.defaultdict(list)
    for dirpath, dirnames, filenames in os.walk("."):
        if ".git" in dirpath.split(os.sep):
            continue
        dirnames[:] = [d for d in dirnames if d != ".git"]
        for fn in filenames:
            p = os.path.join(dirpath, fn)
            rel = os.path.relpath(p, ".")
            try:
                with open(p, "rb") as fh:
                    h = hashlib.md5(fh.read()).hexdigest()
            except OSError:
                continue
            by_hash[h].append(rel)

    removed = kept = 0
    log = []
    for h, paths in sorted(by_hash.items()):
        if len(paths) < 2:
            continue
        paths.sort(key=rank)
        winner, losers = paths[0], paths[1:]
        kept += 1
        log.append(f"KEEP  {winner}")
        for l in losers:
            log.append(f"  rm  {l}")
            removed += 1

    if "--apply" in sys.argv:
        batch = []
        for h, paths in by_hash.items():
            if len(paths) < 2:
                continue
            paths.sort(key=rank)
            batch.extend(paths[1:])
        for i in range(0, len(batch), 200):
            subprocess.run(["git", "rm", "-q", "--ignore-unmatch", "--"]
                           + batch[i:i+200], check=False)
        # prune emptied dirs
        for dirpath, dirnames, filenames in os.walk(".", topdown=False):
            if ".git" in dirpath.split(os.sep):
                continue
            if not os.listdir(dirpath) and dirpath != ".":
                os.rmdir(dirpath)

    print("\n".join(log[:60]))
    print(f"\n... {len(log)} decision lines total")
    print(f"groups with duplicates: {kept}   files removable: {removed}")

main()
