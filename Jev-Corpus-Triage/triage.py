"""Triage pending corpus folders with Jev: one request per section of each file.

Usage: python3 triage.py <run-name> <folder> [<folder> ...]
Writes runs/<run-name>/requests.jsonl (every payload and response), sections.jsonl
(one row per section with its answers) and REPORT.md. Question wording lives in questions.py.
Auth: TYPESAFE_API_KEY if set (the cloud session proxy also signs requests).
"""
import concurrent.futures as cf, hashlib, json, os, re, subprocess, sys, time, urllib.error, urllib.request, zipfile
from collections import Counter, defaultdict
from pathlib import Path

import questions as Q

URL = "https://api.typesafe.ai/v1/systemone"
HERE = Path(__file__).resolve().parent
REPO = HERE.parent
MAX_CHARS = 8000          # one section per request; keeps state focused (jaggedness: large state)
TEXT_EXT = {".md", ".txt", ".json", ".jsonl", ".yml", ".yaml", ".csv", ".html"}
CODE_EXT = {".tsx", ".ts", ".js", ".jsx", ".vue", ".svelte", ".rs", ".py", ".sh", ".css", ".kt", ".java", ".go"}
SKIP_PARTS = {"canvas-ui-main", "thinking-orbs-main", ".git", "node_modules"}

SECRETS = [  # replaced before anything is sent
    r"sk-[A-Za-z0-9_-]{16,}", r"gh[pousr]_[A-Za-z0-9]{20,}", r"github_pat_[A-Za-z0-9_]{20,}", r"AKIA[0-9A-Z]{16}",
    r"AIza[0-9A-Za-z_-]{30,}", r"xox[abpr]-[A-Za-z0-9-]{10,}", r"hf_[A-Za-z0-9]{30,}",
    r"-----BEGIN [A-Z ]*PRIVATE KEY-----[\s\S]*?-----END [A-Z ]*PRIVATE KEY-----",
    r"(?i:api[_-]?key|token|secret|password)\s*[:=]\s*['\"]?[^\s'\"]{12,}",
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
]
SECRET_RE = re.compile("|".join(f"(?:{p})" for p in SECRETS))


def extract(p: Path):
    """Return (text, note). note explains files handled in code without a request."""
    ext = p.suffix.lower()
    if any(part in SKIP_PARTS for part in p.parts):
        return None, "vendored third-party UI code (skipped)"
    if ext in CODE_EXT:
        return None, f"source code ({ext}), not triaged"
    if len(ext) > 6 or " " in ext:  # a dot inside a long filename, not an extension
        ext = ""
    md = Path(str(p)[: -len(ext)] if ext else str(p)).with_name((p.stem if ext else p.name) + ".md")
    if ext != ".md" and md.exists():
        return None, f"copy of the same-name `{md.name}` (four-artifact convention)"
    with open(p, "rb") as f:
        head = f.read(5)
    try:
        if head.startswith(b"%PDF"):
            return subprocess.run(["pdftotext", "-layout", str(p), "-"], capture_output=True, text=True, timeout=120).stdout, "pdf"
        if ext == ".docx" or head.startswith(b"PK"):
            with zipfile.ZipFile(p) as z:
                xml = z.read("word/document.xml").decode("utf8", "replace")
            xml = re.sub(r"</w:p>", "\n", xml)
            return re.sub(r"<[^>]+>", "", xml), "docx"
        if ext in TEXT_EXT or ext == "":
            raw = p.read_bytes()
            if b"\0" in raw[:4096]:
                return None, "binary file"
            return raw.decode("utf8", "replace"), None
    except Exception as e:  # unreadable file is reported, never guessed at
        return None, f"unreadable: {e}"
    return None, f"binary or unsupported ({ext or 'no extension'})"


def sections(text: str):
    """Split on markdown headings, pack small sections, cut big ones on paragraph breaks."""
    parts, heading, buf = [], "(top of file)", []
    for line in text.splitlines():
        if re.match(r"^#{1,4} \S", line) and sum(map(len, buf)) > 400:
            parts.append((heading, "\n".join(buf))); buf = []
        if re.match(r"^#{1,4} \S", line):
            heading = line.lstrip("# ").strip()[:120]
        buf.append(line)
    parts.append((heading, "\n".join(buf)))
    out = []
    for h, body in parts:
        body = body.strip()
        while len(body) > MAX_CHARS:
            cut = body.rfind("\n\n", 0, MAX_CHARS)
            cut = cut if cut > MAX_CHARS // 2 else MAX_CHARS
            out.append((h, body[:cut])); body = body[cut:].strip()
        if body:
            out.append((h, body))
    return out


def ask(state):
    body = json.dumps({"model": Q.MODEL, "state": state, "questions": Q.QUESTIONS}).encode()
    headers = {"Content-Type": "application/json"}
    if os.environ.get("TYPESAFE_API_KEY"):
        headers["Authorization"] = "Bearer " + os.environ["TYPESAFE_API_KEY"]
    for attempt in range(5):
        try:
            with urllib.request.urlopen(urllib.request.Request(URL, data=body, headers=headers), timeout=60) as r:
                return json.loads(body), json.load(r)
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) and attempt < 4:
                time.sleep(float(e.headers.get("retry-after") or 2 ** attempt)); continue
            return json.loads(body), {"error": f"HTTP {e.code}: {e.read()[:300].decode('utf8', 'replace')}"}
        except Exception as e:
            if attempt < 4:
                time.sleep(2 ** attempt); continue
            return json.loads(body), {"error": repr(e)}


def verdict(p):
    return "yes" if p > Q.YES else "no" if p < Q.NO else "unsettled"


def main(run, folders):
    out = HERE / "runs" / run
    out.mkdir(parents=True, exist_ok=True)
    files, notes, seen = [], {}, {}
    for folder in folders:
        for p in sorted((REPO / folder).rglob("*")):
            if not p.is_file():
                continue
            rel = str(p.relative_to(REPO))
            text, note = extract(p)
            if text is None:
                notes[rel] = note; continue
            text = text.strip()
            digest = hashlib.sha256(re.sub(r"\s+", " ", text).encode()).hexdigest()
            if digest in seen:
                notes[rel] = f"exact duplicate of {seen[digest]}"; continue
            seen[digest] = rel
            if len(text) < 300 and re.fullmatch(r"\s*\S*https?://\S+\s*", text):
                notes[rel] = f"link stub: {text}"; continue
            if not text:
                notes[rel] = "empty"; continue
            files.append((rel, text))

    jobs = []
    for rel, text in files:
        dropped = sorted({d for d in Q.DROPPED if re.search(re.escape(d), text, re.I)})
        for i, (h, body) in enumerate(sections(text)):
            jobs.append({"file": rel, "i": i, "heading": h, "chars": len(body), "dropped": dropped,
                         "state": {"project": Q.PROJECT, "file": rel,
                                   "chunk": {"heading": h, "text": SECRET_RE.sub("[REDACTED]", body)}}})
    print(f"{len(files)} files to triage in {len(jobs)} sections; {len(notes)} handled in code", flush=True)

    rows, tokens, errors = [], 0, 0
    with open(out / "requests.jsonl", "w") as log, cf.ThreadPoolExecutor(8) as pool:
        for n, (job, (req, resp)) in enumerate(zip(jobs, pool.map(lambda j: ask(j["state"]), jobs)), 1):
            log.write(json.dumps({"request": req, "response": resp}) + "\n")
            row = {k: job[k] for k in ("file", "i", "heading", "chars", "dropped")}
            row["first_line"] = next((l.strip() for l in job["state"]["chunk"]["text"].splitlines() if l.strip()), "")[:160]
            if "error" in resp:
                row["error"] = resp["error"]; errors += 1
            else:
                tokens += resp["usage"]["input_tokens"]
                a = resp["answers"]
                row["kind"] = a["kind"]["choice"]; row["kind_p"] = round(a["kind"]["confidence"], 2)
                row.update({k: round(v["noul"], 3) for k, v in a.items() if v["type"] == "noul"})
            rows.append(row)
            if n % 50 == 0:
                print(f"  {n}/{len(jobs)} sections, {tokens} input tokens, {errors} errors", flush=True)
    with open(out / "sections.jsonl", "w") as f:
        f.writelines(json.dumps(r) + "\n" for r in rows)
    report(out, folders, rows, notes, tokens, errors)
    print(f"done: {len(rows)} sections, {tokens} input tokens, {errors} errors -> {out}/REPORT.md")


def classify(rows):
    """Truth table in code: Jev judges each section; the file-level call and what counts are decided here."""
    by_file = defaultdict(list)
    for r in rows:
        by_file[r["file"]].append(r)
    for rs in by_file.values():
        ok = [r for r in rs if "error" not in r]
        total = sum(r["chars"] for r in ok) or 1
        third = sum(r["chars"] for r in ok if r["other_project"] > Q.YES) / total >= Q.THIRD_PARTY_SHARE
        for r in ok:
            own = r["operator_authored"] > Q.YES or not third
            r["third_party_file"] = third
            r["decision"] = own and r["has_decision"] > Q.YES
            r["open_task"] = own and r["has_open_task"] > Q.YES
            r["unsettled"] = own and any(Q.NO <= r[k] <= Q.YES for k in ("has_decision", "has_open_task"))
    return by_file


def report(out, folders, rows, notes, tokens, errors):
    by_file = classify(rows)
    comps = [f"about_{c}" for c in Q.COMPONENTS]
    L = [f"# Jev corpus triage: {out.name}", "",
         f"Model `{Q.MODEL}`, thresholds yes > {Q.YES}, no < {Q.NO}. {len(rows)} sections from {len(by_file)} files, "
         f"{len(notes)} files handled in code, {tokens} input tokens, {errors} failed requests.",
         "Folders: " + ", ".join(f"`{f}`" for f in folders), "",
         "These are Jev's judgments per section, not a reading of the files. Use them to choose what to read.", "",
         "A file is a **third-party copy** when most of its text describes another project; its sections count as",
         "decisions or open work only where Jev rates the section as the operator's own writing.", ""]
    head = ["| File | Sections | Main kind | Decisions | Open work | RE findings | Components | Dropped stack |",
            "|---|---|---|---|---|---|---|---|"]

    def line(f, rs):
        ok = [r for r in rs if "error" not in r]
        weights = Counter()
        for r in ok:
            weights[r["kind"]] += r["chars"]
        kind = weights.most_common(1)[0][0] if weights else "error"
        cs = [c[6:] for c in comps if any(r[c] > Q.YES for r in ok)]
        return (f"| `{f}` | {len(rs)} | {kind} | {sum(r['decision'] for r in ok)} | {sum(r['open_task'] for r in ok)} | "
                f"{sum(r['has_re_finding'] > Q.YES for r in ok)} | {', '.join(cs) or '-'} | {', '.join(rs[0]['dropped']) or '-'} |")

    def weight(kv): return -sum(r.get("decision", 0) + r.get("open_task", 0) for r in kv[1])
    own = sorted(((f, rs) for f, rs in by_file.items() if not rs[0].get("third_party_file")), key=weight)
    third = sorted(((f, rs) for f, rs in by_file.items() if rs[0].get("third_party_file")), key=weight)
    L += [f"## Operator's own files ({len(own)}): read these first", ""] + head + [line(*kv) for kv in own]
    L += ["", f"## Third-party copies ({len(third)}): reference only", ""] + head + [line(*kv) for kv in third]
    ok_rows = [r for r in rows if "error" not in r]
    for title, flag, key in (("Operator decisions", "decision", "has_decision"),
                             ("Open work", "open_task", "has_open_task")):
        hits = sorted((r for r in ok_rows if r[flag]), key=lambda r: -r[key])
        L += ["", f"## {title} ({len(hits)})", ""]
        L += [f"- {r[key]:.2f} `{r['file']}` § {r['heading']}: {r['first_line']}" for r in hits]
    hits = sorted((r for r in ok_rows if r["has_re_finding"] > Q.YES), key=lambda r: -r["has_re_finding"])
    L += ["", f"## How-it-works findings, any source ({len(hits)})", ""]
    L += [f"- {r['has_re_finding']:.2f} `{r['file']}` § {r['heading']}: {r['first_line']}" for r in hits]
    unsettled = [r for r in ok_rows if r["unsettled"]]
    L += ["", f"## Unsettled sections in the operator's own writing ({len(unsettled)})", "",
          "Jev could not settle decision or open work here; read these by hand.", ""]
    L += [f"- `{r['file']}` § {r['heading']}" for r in unsettled]
    L += ["", f"## Handled in code ({len(notes)})", ""] + [f"- `{k}`: {v}" for k, v in sorted(notes.items())]
    if errors:
        L += ["", "## Failed requests", ""] + [f"- `{r['file']}` § {r['heading']}: {r['error']}" for r in rows if "error" in r]
    (out / "REPORT.md").write_text("\n".join(L) + "\n")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2:])
