"""Check each option in arch_compare.py against the operator's architecture definition, clause by clause.

Usage: python3 arch_conformance.py
The definition is BOARD-INTAKE.md, "Decisions recorded 2026-10-23", item 6, quoted verbatim in state.
One Noul per clause per option; writes bench/arch-conformance.json.
"""
import json
from pathlib import Path

import arch_compare as A
import questions as Q
import triage

HERE = Path(__file__).resolve().parent

DEFINITION = (
    "Architecture (operator, repeated ~10 times; logged verbatim 2026-10-23): files as infrastructure; agents as "
    "packages; plugins as configurations; repos as marketplaces; memory, workflows and data extraction designed as "
    "skills, scripts and hooks. Agent harnesses and agent packages are modular customizable setups, using "
    "Anthropic's own strategies from its customizable mod setup and its dynamic workflow logic, modifiable in "
    "session alongside Anthropic's workflows/harnesses. Names for the split beyond \"skills/capabilities\" still "
    "open. Pointers: text in AGENTS.md, enforced/injected by hooks.")

CLAUSES = {
    "files_as_infrastructure": "keep its state and infrastructure as files rather than in running servers or databases",
    "agents_as_packages": "ship agents as installable packages",
    "plugins_as_configurations": "use plugins as configurations rather than as whole systems that run on their own",
    "repos_as_marketplaces": "use repositories as marketplaces that skills, agents and plugins are installed from",
    "memory_as_skills_hooks": "build memory out of skills, scripts and hooks",
    "workflows_as_skills_hooks": "build workflows out of skills, scripts and hooks",
    "extraction_as_skills_hooks": "build data extraction out of skills, scripts and hooks",
    "modular_harness": "make the agent harness a modular setup the operator can customise",
    "anthropic_mods": "use Anthropic's own customisation mechanisms for Claude Code, such as plugins, mods and hooks",
    "anthropic_dynamic_workflows": "use Anthropic's dynamic workflow logic, such as subagents and workflows",
    "modifiable_in_session": "let the harness be changed during a session alongside Anthropic's own workflows",
    "agents_md_pointers_hooks": "keep pointers as text in AGENTS.md that hooks enforce or inject",
}


def main():
    state = {"architecture_definition": DEFINITION, "options": A.STATE["options"]}
    qs = {f"{o}__{c}": {"type": "noul",
                        "instructions": f"Does `options.{o}` {what}, as `architecture_definition` requires?"}
          for o in state["options"] for c, what in CLAUSES.items()}
    req, resp = triage.ask_questions(state, qs)
    (HERE / "bench" / "arch-conformance.json").write_text(json.dumps({"request": req, "response": resp}, indent=1))
    if "error" in resp:
        raise SystemExit(resp["error"])
    a = resp["answers"]
    opts = list(state["options"])
    mark = lambda p: "yes" if p > Q.YES else "no " if p < Q.NO else " ? "
    print(f"{'clause':28}" + "".join(f"{o:>24}" for o in opts))
    for c in CLAUSES:
        print(f"{c:28}" + "".join(f"{mark(a[f'{o}__{c}']['noul']):>17} {a[f'{o}__{c}']['noul']:5.2f} " for o in opts))
    print(f"{'clauses met (p > 0.7)':28}" + "".join(
        f"{sum(a[f'{o}__{c}']['noul'] > Q.YES for c in CLAUSES):>17} / {len(CLAUSES)}  " for o in opts))
    print(f"{'expected clauses met':28}" + "".join(
        f"{sum(a[f'{o}__{c}']['noul'] for c in CLAUSES):>23.1f} " for o in opts))
    print("input tokens:", resp["usage"]["input_tokens"])


if __name__ == "__main__":
    main()
