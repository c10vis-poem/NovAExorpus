#!/usr/bin/env python3
"""Restore original docx/pdf/mht files (from git history, pre-conversion)
alongside their already-converted .md counterpart, wherever the .md exists
at HEAD. Skips anything that was quarantined as a duplicate (no .md exists
for it at either naming scheme -> its original already lives in
_DUPLICATES_REVIEW/, untouched)."""
import subprocess, os, sys

SOURCE_COMMIT = "c9d23da"
CONVERTIBLE = {".docx", ".doc", ".pdf", ".mht", ".mhtml", ".txt"}

def sniff_ext(commit, relpath):
    r = subprocess.run(["git", "show", f"{commit}:{relpath}"], capture_output=True)
    if r.returncode != 0:
        return None
    tmp = "/tmp/_sniff_tmp"
    with open(tmp, "wb") as f:
        f.write(r.stdout)
    out = subprocess.run(["file", "--mime-type", "-b", tmp], capture_output=True, text=True).stdout.strip()
    if out == "application/pdf":
        return ".pdf"
    if "wordprocessingml" in out:
        return ".docx"
    return None

def main():
    r = subprocess.run(["git", "ls-tree", "-r", SOURCE_COMMIT, "--name-only"], capture_output=True, text=True)
    all_files = [l for l in r.stdout.splitlines() if l.startswith("INBOX/")]

    restored, skipped_dup, skipped_notfound = 0, 0, 0
    for f in all_files:
        rel = f[len("INBOX/"):]  # path relative to vault root, e.g. "#HORIZONS-main/foo.pdf"
        base, ext = os.path.splitext(rel)
        ext_lower = ext.lower()
        real_ext = ext_lower
        if not ext_lower:
            sniffed = sniff_ext(SOURCE_COMMIT, f)
            if not sniffed:
                continue
            real_ext = sniffed
            base = rel  # whole thing was the base

        if real_ext not in CONVERTIBLE:
            continue

        orig_ext_for_md = ext if ext else ""
        candidates = [
            base + orig_ext_for_md + ".md",   # new collision-safe naming
            base + ".md",                      # old bare naming
        ]
        dest_md = None
        for c in candidates:
            if os.path.exists(c):
                dest_md = c
                break

        if dest_md is None:
            skipped_dup += 1
            continue

        # restore original next to it, under its original filename
        dest_orig = rel
        if os.path.exists(dest_orig):
            continue  # already restored or never removed
        os.makedirs(os.path.dirname(dest_orig) or ".", exist_ok=True)
        r2 = subprocess.run(["git", "show", f"{SOURCE_COMMIT}:{f}"], capture_output=True)
        if r2.returncode != 0:
            skipped_notfound += 1
            continue
        with open(dest_orig, "wb") as out:
            out.write(r2.stdout)
        restored += 1

    print(f"Restored: {restored}")
    print(f"Skipped (quarantined duplicate, no .md exists): {skipped_dup}")
    print(f"Skipped (not found in source commit): {skipped_notfound}")

if __name__ == "__main__":
    main()
