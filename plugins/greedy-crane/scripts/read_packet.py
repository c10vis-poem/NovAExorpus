#!/usr/bin/env python3
"""read_packet.py -- bulk reader for corpus-ingest workers. Serves every assigned file, batch by batch.

  read_packet.py <folder> <ID> --plan            files, sizes, batch count; suggests a split if too big
  read_packet.py <folder> <ID> --next            print the next batch (full text, line-numbered) and log it
  read_packet.py <folder> <ID> --status          batches served / left
  read_packet.py <folder> <ID> --only <root>     limit this worker to one plugin folder of the packet (for splits)

<folder>/<ID>-paths.txt lists the assigned folders (absolute paths). Same skip rules as
worker_stop_check.py (media, .git, node_modules, lockfiles, licenses). Files over BIG_LINES
are served whole too, in their own batches, split at BATCH_BYTES. Each served file is appended
to <folder>/read-ledger-<ID>.tsv (path, bytes, lines, batch) -- the stop check reads it.
Write your findings for a batch to your progress file BEFORE calling --next again.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from worker_stop_check import assigned  # one definition of "assigned files"

BATCH_BYTES = 60_000      # ~15k tokens per batch
SPLIT_TOKENS = 250_000    # suggest more workers above this


def batches(files):
    out, cur, size = [], [], 0
    for root, rid, rel in files:
        p = os.path.join(root, rel)
        try:
            b = os.path.getsize(p)
        except OSError:
            continue
        if b > BATCH_BYTES:  # oversize: own batches, sliced by bytes
            if cur:
                out.append(cur); cur, size = [], 0
            for off in range(0, b, BATCH_BYTES):
                out.append([(p, off, min(BATCH_BYTES, b - off), b)])
            continue
        if size + b > BATCH_BYTES and cur:
            out.append(cur); cur, size = [], 0
        cur.append((p, 0, b, b)); size += b
    if cur:
        out.append(cur)
    return out


def main(a):
    folder, pid, mode = os.path.expanduser(a[0]), a[1], a[2]
    only = a[a.index("--only") + 1] if "--only" in a else None
    _, _, files = assigned(f"Folder: {folder}\n{pid}-paths.txt")
    if only:
        files = [f for f in files if f[0].rstrip("/") == only.rstrip("/")]
    bs = batches(files)
    tag = "-" + os.path.basename(only.rstrip("/"))[:8] if only else ""
    state = os.path.join(folder, f".read-pos-{pid}{tag}")
    ledger = os.path.join(folder, f"read-ledger-{pid}.tsv")
    pos = int(open(state).read() or 0) if os.path.exists(state) else 0
    if mode == "--plan":
        tot = sum(os.path.getsize(os.path.join(r, f)) for r, _, f in files)
        print(f"{pid}: {len(files)} files, {tot/1e6:.2f} MB (~{tot//4000}k tokens), {len(bs)} batches")
        if tot / 4 > SPLIT_TOKENS:
            roots = {}
            for r, _, f in files:
                roots[r] = roots.get(r, 0) + os.path.getsize(os.path.join(r, f))
            print(f"Too big for one worker: split by folder with --only (one worker per group, ~{SPLIT_TOKENS//1000}k tokens each):")
            for r, s in sorted(roots.items(), key=lambda x: -x[1]):
                print(f"  {s//4000:>5}k  {r}")
        return 0
    if mode == "--status":
        print(f"{pid}{tag}: {pos} of {len(bs)} batches served"); return 0
    if pos >= len(bs):
        print(f"DONE: all {len(bs)} batches of {pid}{tag} served. Finish your deliverable."); return 0
    with open(ledger, "a") as led:
        for p, off, n, total in bs[pos]:
            with open(p, "rb") as f:
                f.seek(off); txt = f.read(n).decode("utf-8", "replace")
            first = open(p, "rb").read(off).count(b"\n") + 1 if off else 1
            part = f" bytes {off}-{off+n} of {total}" if n < total else ""
            print(f"\n===== {p}{part} =====")
            for i, line in enumerate(txt.splitlines(), first):
                print(f"{i:>6}\t{line}")
            if off + n >= total:
                led.write(f"{p}\t{total}\t{txt.count(chr(10))}\t{pos+1}\n")
    open(state, "w").write(str(pos + 1))
    print(f"\n--- batch {pos+1} of {len(bs)} ({pid}{tag}). Write findings to your progress file, then --next. ---")
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(__doc__); sys.exit(1)
    sys.exit(main(sys.argv[1:]))
