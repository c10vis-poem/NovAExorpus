"""Draw a stratified benchmark set of real sections from finished triage runs.

Usage: python3 bench_sample.py <n> <run> [<run> ...]
Writes bench/sample.jsonl: one row per section with its exact state (as Jev saw it), Jev's answers,
and empty gold fields to fill by hand. The same states go to every system under test.
"""
import json, random, sys
from pathlib import Path

import triage

HERE = Path(__file__).resolve().parent


def load(run):
    d = HERE / "runs" / run
    reqs = [json.loads(l)["request"]["state"] for l in open(d / "requests.jsonl")]
    rows = [json.loads(l) for l in open(d / "sections.jsonl")]
    triage.classify(rows)
    return [dict(r, state=s, run=run) for r, s in zip(rows, reqs) if "error" not in r]


def main(n, runs):
    pool = [r for run in runs for r in load(run)]
    strata = {
        "own_decision": [r for r in pool if r["decision"]],
        "own_open_task": [r for r in pool if r["open_task"] and not r["decision"]],
        "own_unsettled": [r for r in pool if r["unsettled"] and not (r["decision"] or r["open_task"])],
        "own_no": [r for r in pool if not r["third_party_file"] and not (r["decision"] or r["open_task"] or r["unsettled"])],
        "third_party": [r for r in pool if r["third_party_file"]],
    }
    rnd = random.Random(20261024)
    out, per = [], n // len(strata)
    for name, rows in strata.items():
        for r in rnd.sample(rows, min(per, len(rows))):
            out.append({"id": f"{r['run']}:{r['file']}:{r['i']}", "stratum": name, "state": r["state"],
                        "jev": {k: r[k] for k in ("kind", "has_decision", "has_open_task", "has_re_finding",
                                                  "operator_authored", "other_project")},
                        "gold": {"decision": None, "open_task": None, "other_project": None}})
    (HERE / "bench").mkdir(exist_ok=True)
    with open(HERE / "bench" / "sample.jsonl", "w") as f:
        f.writelines(json.dumps(r, ensure_ascii=False) + "\n" for r in out)
    print({k: min(per, len(v)) for k, v in strata.items()}, "->", len(out), "sections")


if __name__ == "__main__":
    main(int(sys.argv[1]), sys.argv[2:])
