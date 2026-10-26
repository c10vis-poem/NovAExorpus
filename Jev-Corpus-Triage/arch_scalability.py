"""Break "scalability" into concrete judgments and ask Jev each one per option, with measured facts in state.

Usage: python3 arch_scalability.py
Facts were measured in the cloud container on 2026-10-26 (see FACTS); projections to 40,000 files are
linear arithmetic done here, not by the model. Runs twice (options in both orders) and writes
bench/arch-scalability.json.
"""
import json
from pathlib import Path

import arch_compare as A
import questions as Q
import triage

HERE = Path(__file__).resolve().parent
SCALE = 40000 / 4509

FACTS = {
    "vault_today": "4,509 tracked files (2,823 markdown/text), 135 MB tracked, 329 MB of git history.",
    "search_today": ("Full-text grep over every markdown/text file: 5.1 s with a cold disk cache, 0.05 s warm, "
                     "on a 4-core cloud VM. git status 0.02 s. Looking a term up in manifest.jsonl 0.004 s."),
    "search_at_40k": (f"Projected by linear scaling (x{SCALE:.1f}) to 40,000 files: grep about {5.1 * SCALE:.0f} s "
                      f"cold and {0.05 * SCALE:.1f} s warm on the VM, slower on the phone; about 1.2 GB tracked and "
                      "3 GB of git history."),
    "manifest_coverage": "manifest.jsonl lists 585 of the 4,509 files today, so it is not kept current.",
    "jev_per_request": ("Each Jev triage request carries one section of at most 8,000 characters (about 1,900 input "
                        "tokens) against a 32,000-token per-question limit, so request size does not grow with the "
                        "vault. Triage cost grows linearly: 6.4 million tokens for 3,415 sections today."),
    "jev_speed": "Jev answers in a median 0.16 s per request and requests run in parallel.",
    "writers": "Several agents (phone, tablet, cloud sessions) commit to the vault; git merges their changes through pull requests.",
}

ASPECTS = {
    "lookup_fast": "find the files relevant to a prompt within a few seconds at 40,000 files",
    "finds_right_files": "still find the right files, not just matching words, at 40,000 files",
    "index_kept_current": "keep its index or memory current as files are added and edited, without manual work",
    "storage_fits": "fit its storage on the phone and in GitHub at 40,000 files",
    "many_agents": "let several agents read and write at the same time without conflicts or lost writes",
    "runs_on_phone": "still run on the phone at 40,000 files",
    "cost_stays_low": "keep its running cost low as the vault grows to 40,000 files",
}


def ask(options):
    state = {"facts": FACTS, "options": options}
    qs = {f"{o}__{a}": {"type": "noul", "instructions": f"Given `facts`, would `options.{o}` {what}?"}
          for o in options for a, what in ASPECTS.items()}
    return triage.ask_questions(state, qs)


def main():
    opts = A.STATE["options"]
    runs = [ask(opts), ask(dict(reversed(list(opts.items()))))]
    (HERE / "bench" / "arch-scalability.json").write_text(
        json.dumps([{"request": q, "response": r} for q, r in runs], indent=1))
    for _, r in runs:
        if "error" in r:
            raise SystemExit(r["error"])
    p = {k: [r["answers"][k]["noul"] for _, r in runs] for k in runs[0][1]["answers"]}
    mark = lambda v: "yes" if v > Q.YES else "no " if v < Q.NO else " ? "
    print(f"{'aspect':20}" + "".join(f"{o:>26}" for o in opts))
    for a in ASPECTS:
        cells = []
        for o in opts:
            v = p[f"{o}__{a}"]
            m = sum(v) / len(v)
            cells.append(f"{mark(m)} {m:4.2f} ({v[0]:.2f}/{v[1]:.2f})")
        print(f"{a:20}" + "".join(f"{c:>26}" for c in cells))
    print(f"{'expected aspects met':20}" + "".join(
        f"{sum(sum(p[f'{o}__{a}']) / 2 for a in ASPECTS):>26.1f}" for o in opts))
    print("input tokens:", sum(r["usage"]["input_tokens"] for _, r in runs))


if __name__ == "__main__":
    main()
