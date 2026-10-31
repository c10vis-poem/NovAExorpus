#!/usr/bin/env python3
"""worker_stop_check.py -- SubagentStop hook for greedy-crane:corpus-ingest workers only.

A worker may not finish while (a) its progress file or deliverable is missing, or
(b) a file in its assigned paths list (<ID>-paths.txt named in the spawn prompt) was
never opened. Non-text files, .git, node_modules, lockfiles and licenses are skipped.

"Opened" = Read tool on the file, or one Bash command that names both the file's
plugin folder (its id, or first 8 chars of a uuid id) and the file's path inside it.
or a line in <folder>/read-ledger-<ID>.tsv (written by read_packet.py, which serves whole files).
A partial Read/Bash read counts as opened; read_packet.py is the full-read path.

Rules (operator, 2026-10-30): applies only to files the operator assigned; the
operator's word overrides it. Off switches, checked every call:
  env WIKI_ADMIN_HOOKS=off | file ~/.wiki-admin/hooks.off | ~/.wiki-admin/hooks.d/worker-stop.off
Blocks at most MAX_BLOCKS times per worker, then lets it stop (obs 0051: no loops).
Fail-open: any error -> exit 0. Never blocks the operator, prompts, or reads.
Test: worker_stop_check.py --transcript <agent-*.jsonl>  (prints verdict, no counter).
"""
import json, os, re, sys

MAX_BLOCKS = 3
HOME = os.path.expanduser("~")
STATE = os.environ.get("WIKI_ADMIN_HOME", os.path.join(HOME, ".wiki-admin"))
SKIP_DIRS = {".git", ".in_use", "node_modules", "__pycache__", "dist", "build", ".venv"}
SKIP_RE = re.compile(r"(\.(png|jpe?g|gif|webp|svg|ico|mp[34]|m4a|wav|ogg|pdf|zip|gz|tgz|woff2?|ttf|otf|eot|pyc|so|bin|db|sqlite)"
                     r"|(^|/)(LICENSE|LICENCE|COPYING)[^/]*|(^|/)(package-lock\.json|yarn\.lock|pnpm-lock\.yaml|uv\.lock|poetry\.lock)"
                     r"|(^|/)\.(gitignore|gitattributes|DS_Store|npmignore))$", re.I)


def off():
    return (os.environ.get("WIKI_ADMIN_HOOKS") == "off"
            or os.path.exists(os.path.join(STATE, "hooks.off"))
            or os.path.exists(os.path.join(STATE, "hooks.d", "worker-stop.off")))


def load(tp):
    rows = []
    with open(tp) as f:
        for line in f:
            try:
                rows.append(json.loads(line))
            except ValueError:
                pass
    return rows


def text_of(content):
    if isinstance(content, str):
        return content
    return "\n".join(c.get("text", "") for c in content or [] if isinstance(c, dict))


def assigned(spawn):
    """Return (folder, packet_id, [(root, root_id, relpath)])."""
    m = re.search(r"Folder:\s*(\S+)", spawn)
    folder = os.path.expanduser(m.group(1)) if m else ""
    pm = re.search(r"([A-Za-z0-9_]+)-paths\.txt", spawn)
    if not pm:
        return folder, None, []
    pid = pm.group(1)
    pfile = os.path.join(folder, pm.group(0))
    files = []
    for root in re.findall(r"(/\S+)", open(pfile).read()):
        root = root.rstrip("/")
        if not os.path.isdir(root):
            continue
        base = os.path.basename(root)
        rid = base[:8] if re.match(r"^[0-9a-f]{8}-", base) else base
        for d, dirs, names in os.walk(root):
            dirs[:] = [x for x in dirs if x not in SKIP_DIRS]
            for n in names:
                rel = os.path.relpath(os.path.join(d, n), root)
                if not SKIP_RE.search(rel):
                    files.append((root, rid, rel))
    return folder, pid, files


def verdict(rows):
    spawn = next((text_of(r["message"]["content"]) for r in rows if r.get("type") == "user"), "")
    folder, pid, files = assigned(spawn)
    if not pid:
        return None  # not a packet worker: leave it alone
    reads, cmds = set(), []
    for r in rows:
        if r.get("type") != "assistant":
            continue
        for c in r["message"].get("content") or []:
            if not (isinstance(c, dict) and c.get("type") == "tool_use"):
                continue
            i = c.get("input") or {}
            if c.get("name") == "Read" and i.get("file_path"):
                reads.add(os.path.normpath(os.path.expanduser(i["file_path"])))
            elif c.get("name") == "Bash":
                cmds.append(i.get("command", ""))
    led = os.path.join(folder, f"read-ledger-{pid}.tsv")  # files served by read_packet.py
    if os.path.isfile(led):
        reads |= {l.split("\t", 1)[0] for l in open(led) if l.strip()}
    unopened = []
    for root, rid, rel in files:
        if os.path.join(root, rel) in reads:
            continue
        if any(rid in c and rel in c for c in cmds):
            continue
        unopened.append(os.path.join(root, rel))
    problems = []
    if not os.path.isfile(os.path.join(folder, f"progress-{pid}.md")):
        problems.append(f"progress file {folder}progress-{pid}.md is missing")
    if not [n for n in os.listdir(folder) if n.startswith(pid + "-") and n.endswith(".md")] if os.path.isdir(folder) else True:
        problems.append(f"deliverable {pid}-*.md is missing in {folder}")
    return pid, len(files), unopened, problems


def message(pid, total, unopened, problems):
    lines = [f"BLOCKED (greedy-crane worker-stop, packet {pid}):"]
    lines += ["- " + p for p in problems]
    if unopened:
        lines.append(f"- {len(unopened)} of {total} assigned files were never opened:")
        lines += ["  " + u for u in unopened[:60]]
        if len(unopened) > 60:
            lines.append(f"  ... and {len(unopened) - 60} more (same folders)")
    lines.append("Do only this: open those files, then update your progress file and deliverable. Nothing else.")
    lines.append("If the operator told you to skip any of them, the operator wins: list each under ## Blocked with their words.")
    return "\n".join(lines)


def main():
    if "--transcript" in sys.argv:
        v = verdict(load(sys.argv[sys.argv.index("--transcript") + 1]))
        print("not a packet worker" if v is None else
              (message(*v) if (v[2] or v[3]) else f"PASS packet {v[0]}: all {v[1]} assigned files opened"))
        return 0
    if off():
        return 0
    ev = json.load(sys.stdin)
    at = ev.get("agent_type") or ""
    tp = os.path.expanduser(ev.get("agent_transcript_path") or "")
    if not at and tp:
        meta = tp[:-6] + ".meta.json" if tp.endswith(".jsonl") else ""
        if os.path.isfile(meta):
            at = json.load(open(meta)).get("agentType", "")
    if not at.endswith("corpus-ingest") or not os.path.isfile(tp):
        return 0
    v = verdict(load(tp))
    if v is None or not (v[2] or v[3]):
        return 0
    cdir = os.path.join(STATE, "state")
    os.makedirs(cdir, exist_ok=True)
    cfile = os.path.join(cdir, "worker-stop-" + re.sub(r"\W", "_", ev.get("agent_id") or os.path.basename(tp)))
    n = int(open(cfile).read() or 0) if os.path.exists(cfile) else 0
    if n >= MAX_BLOCKS:
        print(json.dumps({"systemMessage": f"greedy-crane worker-stop: packet {v[0]} stopped after {n} blocks with "
                                           f"{len(v[2])} files unopened; check it by hand."}))
        return 0
    open(cfile, "w").write(str(n + 1))
    sys.stderr.write(message(*v) + "\n")
    return 2


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)
