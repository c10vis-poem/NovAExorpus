"""Ask Jev to score three ways of building the D.U.M.B.A.S.S. head to head.

Usage: python3 arch_compare.py
Writes bench/arch-compare.json (request + response). Option descriptions come from the vault's own
docs (BOARD-INTAKE, CONTEXT, handoff/2026-10-24 extracts) and this workspace's measurements; each
option x criterion is its own Score question so no answer can lean on another.
"""
import json
from pathlib import Path

import triage

HERE = Path(__file__).resolve().parent

STATE = {
    "goal": ("One memory and routing system for one operator's agents across an Android phone (Hexagon NPU, "
             "Termux, about 6 GB free RAM), a tablet, a GCP VM on credits, and later a home Jetson. It must route "
             "every prompt, keep episodic memory, retrieve governed facts from a vault of about 4,000 markdown files "
             "growing to tens of thousands, and keep the operator in control: nothing turned off or installed "
             "without the operator naming it, and no third-party stack hijacking prompts."),
    "measurements": ("Measured this session on 3,415 real vault sections: TypeSafe Jev answers 17 typed questions per "
                     "section in a median 0.16 s, about 1,900 input tokens per section, at fractions of a cent. "
                     "On a 40-section labelled benchmark Jev alone was right 68% (rarely wrong, often unsure), Claude "
                     "Haiku 5.5 81%, Claude Sonnet 5.5 94%, and Jev with its unsure cases sent to Sonnet 91% while "
                     "Sonnet saw 31% of the labels."),
    "options": {
        "custom_harness": (
            "The operator's planned system. Third-party stacks are broken into assets and only the useful parts are "
            "folded in. Claude Code is the harness, customised with hooks, skills, subagents and mods. Routing is a "
            "UserPromptSubmit hook that asks Jev typed questions and sends unsure cases to a Sonnet or Opus subagent. "
            "Episodic memory is a Stop hook where Jev decides what to keep and appends it to a markdown file in the "
            "repo. Semantic retrieval uses the vault, its manifest and per-section Jev labels, with grep and Jev "
            "relevance ranking. Graphify and code-review-graph stay as the graph layers. Everything is files in git; "
            "no extra database servers. Much of it is not built yet."),
        "third_party_servers": (
            "Run the third-party servers whole, as their projects ship them: OmniRoute as a localhost gateway that "
            "every prompt passes through, with its own SQLite store; mem0 for episodic memory with Postgres and "
            "Neo4j; OB1 / Terrestrial Brain on Supabase or Postgres with pgvector and LLM-based schema routing; plus "
            "Graphify and code-review-graph. Runs in Docker Compose on the GCP VM, reached from the phone over "
            "Tailscale. The operator earlier found OB1 intrusive and said it attempts to hijack prompts."),
        "baseline_claude_code": (
            "Plain Claude Code with no additions: it reads AGENTS.md and the files it is pointed at, uses its "
            "built-in memory files and subagents, and searches the vault with grep when asked. No Jev, no routing "
            "layer, no memory servers, no graph tools."),
    },
}

CRITERIA = {
    "accuracy": ("How accurately would `options.{o}` route prompts and recall the right memory and facts for this "
                 "operator, given `measurements`?",
                 ["Often routes or recalls wrongly", "Wrong in a noticeable share of cases",
                  "Mostly right with regular misses", "Right in most cases, misses are rare",
                  "Right almost every time"]),
    "scalability": ("How well would `options.{o}` keep working as the vault grows from 4,000 to tens of thousands "
                    "of files and more agents use it?",
                    ["Breaks down or needs a redesign", "Slows sharply and needs heavy tuning",
                     "Copes with some added infrastructure", "Grows with modest work",
                     "Grows with almost no extra work"]),
    "size": ("How much storage, memory and running infrastructure would `options.{o}` need on the operator's "
             "devices and VM?",
             ["Several always-on servers and databases", "A few always-on services",
              "One or two light services", "Files plus occasional API calls",
              "Almost nothing beyond the files themselves"]),
    "cost_effectiveness": ("How much useful routing and memory would `options.{o}` deliver for the money and "
                           "credits it spends?",
                           ["Costly for what it delivers", "Pays for itself only partly",
                            "Fair value", "Good value", "Excellent value for very little spend"]),
    "operator_control": ("How well would `options.{o}` keep the operator in control of what runs and what "
                         "reaches the models?",
                         ["Takes control away from the operator", "Operator control is weak",
                          "Operator control is partial", "Operator controls nearly everything",
                          "Operator controls every step"]),
    "build_effort": ("How little work would `options.{o}` need before it is usable day to day?",
                     ["Months of building", "Weeks of building", "Several days of setup",
                      "About a day of setup", "Usable almost immediately"]),
}


def main():
    questions = {}
    for o in STATE["options"]:
        for c, (text, levels) in CRITERIA.items():
            questions[f"{o}__{c}"] = {"type": "score", "instructions": text.format(o=o), "criteria": levels}
    req, resp = triage.ask_questions(STATE, questions)
    (HERE / "bench").mkdir(exist_ok=True)
    (HERE / "bench" / "arch-compare.json").write_text(json.dumps({"request": req, "response": resp}, indent=1))
    if "error" in resp:
        raise SystemExit(resp["error"])
    a = resp["answers"]
    crit = list(CRITERIA)
    print(f"{'option':22}" + "".join(f"{c[:12]:>14}" for c in crit) + f"{'mean':>8}")
    for o in STATE["options"]:
        s = [a[f"{o}__{c}"]["score"] for c in crit]
        print(f"{o:22}" + "".join(f"{v:>14.2f}" for v in s) + f"{sum(s) / len(s):>8.2f}")
    print("\nscore = expected level, 0 (worst) to 4 (best); per-level probabilities are in bench/arch-compare.json")
    print("input tokens:", resp["usage"]["input_tokens"])


if __name__ == "__main__":
    main()
