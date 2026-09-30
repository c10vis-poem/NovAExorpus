#!/usr/bin/env python3
"""Mechanical verification of the corpus. Reports facts, never a status claim."""
import os, collections, hashlib, sys

ROOT = "/workspace/obsidian-master_wiki"
os.chdir(ROOT)

ORIGINALS = {".pdf", ".docx", ".mht", ".doc", ".pptx", ".xlsx"}
SKIP_KIT = {"canon", "pending-corpora"}   # kits added in a later pass

files, dirs = [], []
for dp, dn, fn in os.walk("."):
    if ".git" in dp.split(os.sep):
        continue
    dn[:] = [d for d in dn if d != ".git"]
    rel = os.path.relpath(dp, ".")
    if rel != ".":
        dirs.append(rel)
    for f in fn:
        files.append(os.path.relpath(os.path.join(dp, f), "."))

print(f"FILES: {len(files)}   DIRS: {len(dirs)}\n")

# 1 — every original has a sibling .md (same basename, same folder)
missing = []
for f in files:
    stem, ext = os.path.splitext(f)
    if ext.lower() in ORIGINALS:
        # accept  foo.pdf -> foo.md   or  foo.pdf.md
        if not (os.path.exists(stem + ".md") or os.path.exists(f + ".md")):
            missing.append(f)
print(f"[1] originals without a sibling .md: {len(missing)}")
for m in sorted(missing)[:25]:
    print(f"      {m}")
if len(missing) > 25:
    print(f"      ... and {len(missing)-25} more")

# 2 — no basename under two different folders
byname = collections.defaultdict(set)
for f in files:
    byname[os.path.basename(f)].add(os.path.dirname(f))
cross = {n: d for n, d in byname.items() if len(d) > 1}
print(f"\n[2] basenames appearing in >1 folder: {len(cross)}")
for n, d in sorted(cross.items())[:12]:
    print(f"      {n}")
    for x in sorted(d):
        print(f"         {x}/")
if len(cross) > 12:
    print(f"      ... and {len(cross)-12} more")

# 3 — byte-identical duplicates remaining
byhash = collections.defaultdict(list)
for f in files:
    try:
        byhash[hashlib.md5(open(f, "rb").read()).hexdigest()].append(f)
    except OSError:
        pass
dups = {h: p for h, p in byhash.items() if len(p) > 1}
print(f"\n[3] byte-identical duplicate groups remaining: {len(dups)}")
for h, p in list(sorted(dups.items()))[:8]:
    for x in p:
        print(f"      {x}")
    print()

# 4 — top-level folders missing README.md
tops = sorted({d.split(os.sep)[0] for d in dirs})
noreadme = [t for t in tops if not os.path.exists(os.path.join(t, "README.md"))]
print(f"[4] top-level folders without README.md: {len(noreadme)}/{len(tops)}")
for t in noreadme:
    print(f"      {t}/")

# 5 — section kit completeness on top-level folders
KIT = ["README.md", "CLAUDE.md", "llm_wiki.md", "skill_manifest.json"]
print(f"\n[5] section-kit completeness (top level):")
for t in tops:
    have = [k for k in KIT if os.path.exists(os.path.join(t, k))]
    mark = "OK " if len(have) == 4 else f"{len(have)}/4"
    print(f"      {mark}  {t}/  missing: {[k for k in KIT if k not in have] or '-'}")

# 6 — canon conformance
print(f"\n[6] canon/ conformance:")
for dp, dn, fn in os.walk("canon"):
    for f in sorted(fn):
        if not f.endswith(".md"):
            continue
        p = os.path.join(dp, f)
        t = open(p, encoding="utf-8", errors="replace").read()
        checks = {
            "operator-quote": "**Operator:" in t or "Operator**" in t,
            "artifact":       "![" in t or "**Artifact:" in t,
            "ledger":         "Status ledger" in t or "status:" in t,
        }
        bad = [k for k, v in checks.items() if not v]
        print(f"      {'OK ' if not bad else 'XX '} {p}  {'missing: '+str(bad) if bad else ''}")

print(f"\n[7] file-count reconciliation")
print(f"      start 1305  ->  now {len(files)}")
print(f"      excised code: 441 (vendored) + 89 (APK Kotlin) = 530")
print(f"      dedup removed: 194")
print(f"      1305 - 530 - 194 = {1305-530-194}  (delta {len(files)-(1305-530-194):+d})")
