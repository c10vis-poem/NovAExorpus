# Termux

The on-device shell layer. Part of the body: sits between nodes and skills.

## Status

See **[`../canon/STATE-OF-EXISTENCE.md`](../canon/STATE-OF-EXISTENCE.md)** — the
single ledger that says what is actually built. Nothing in this folder asserts
its own build state.

## Conventions

This folder follows the corpus conventions in
[`../NOVA-CORPUS-PLAN.md`](../NOVA-CORPUS-PLAN.md):

- organised by **domain** (one axis on disk)
- four-artifact document convention, joined on shared basename
- section kit: `README.md` + `CLAUDE.md` + `llm_wiki.md` + `skill_manifest.json`

## Rules that apply here

All seven zero-trust rules, in particular:

- **Rule 4 — Mechanical verification.** Claims about this folder are checked by
  the basename audit, never by an agent's self-report.
- **Rule 6 — Designed != Built.** Every component carries a state tag.
- **Rule 7 — Metaphor != Implementation.** The operator's analogies are interface
  and config-file design language, not specifications for enforcement code.
