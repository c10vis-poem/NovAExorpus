"""Score every system's answers on bench/sample.jsonl against bench/gold.json.

Usage: python3 bench_score.py [claude-haiku.json claude-sonnet.json ...]
"Unsure" (or a Jev Noul between the thresholds) is counted separately, never as right.
"""
import json, sys
from pathlib import Path

import questions as Q
import triage

HERE = Path(__file__).resolve().parent
LABELS = ("decision", "open_task", "other_project")


def jev_answers(rows):
    """Jev as the triage uses it: section Nouls plus the file-level truth table in code."""
    by_run = {}
    for r in rows:
        run, f, i = r["id"].split(":", 2)
        by_run.setdefault(run, []).append((f, int(i)))
    full = {}
    for run in by_run:
        d = HERE / "runs" / run
        secs = [json.loads(l) for l in open(d / "sections.jsonl")]
        triage.classify(secs)
        full.update({(run, s["file"], s["i"]): s for s in secs})
    out = []
    for r in rows:
        run, f, i = r["id"].split(":", 2)
        s = full[(run, f, int(i))]
        def v(flag, p):
            return "yes" if flag else ("unsure" if Q.NO <= p <= Q.YES and not s["third_party_file"] else "no")
        out.append({"decision": v(s["decision"], s["has_decision"]),
                    "open_task": v(s["open_task"], s["has_open_task"]),
                    "other_project": "yes" if s["other_project"] > Q.YES else "no" if s["other_project"] < Q.NO else "unsure"})
    return out


def score(name, answers, gold):
    line = [f"{name:14}"]
    total = [0, 0, 0, 0]
    for k, label in enumerate(LABELS):
        right = wrong = unsure = n = 0
        for a, g in zip(answers, gold):
            if g[k] == "?":
                continue
            n += 1
            got = a[label]
            if got == "unsure":
                unsure += 1
            elif (got == "yes") == (g[k] == "T"):
                right += 1
            else:
                wrong += 1
        total = [t + x for t, x in zip(total, (right, wrong, unsure, n))]
        line.append(f"{label}: {right}/{n} right, {wrong} wrong, {unsure} unsure")
    line.append(f"ALL: {total[0]}/{total[3]} right ({total[0] / total[3]:.0%}), {total[1]} wrong, {total[2]} unsure")
    print(" | ".join(line))


def main(files):
    rows = [json.loads(l) for l in open(HERE / "bench" / "sample.jsonl")]
    gold = json.load(open(HERE / "bench" / "gold.json"))["gold"]
    score("jev-1.14.0", jev_answers(rows), gold)
    for f in files:
        ans = sorted(json.load(open(HERE / "bench" / f)), key=lambda a: a["n"])
        assert len(ans) == len(rows), f"{f}: {len(ans)} answers"
        score(Path(f).stem, ans, gold)


if __name__ == "__main__":
    main(sys.argv[1:])
