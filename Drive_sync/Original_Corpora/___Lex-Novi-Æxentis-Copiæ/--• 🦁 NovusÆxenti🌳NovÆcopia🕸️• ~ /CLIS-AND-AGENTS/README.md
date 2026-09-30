# clis-and-agents

Documentation for the CLI tools and coding agents in the stack. **Code does not
live here** — this folder holds what each tool *is*, why it was pulled in, and
where its source actually lives.

## Why the code was removed

The vault carried **441 vendored source files** — two complete code checkouts
(`OpenWiki`, TypeScript; `llm-wiki`, Rust) plus compiled `.so`/`.dylib`/`.dll`
binaries and vendored `llama-cli` / `llama-server` / `llama-quantize` executables
— sitting inside a *documentation* corpus. That is 34% of the vault's file count
carrying no documentation value, and it defeats the corpus's own conventions:

- the four-artifact convention (`original` + `.md` + `.jsonl` + `skills.md`) is
  meaningless for a `.tsx` file,
- the basename audit would have to carve out a permanent exemption for them,
- and a checkout in a vault goes stale silently, with no CI and no upstream link.

**Corpus holds knowledge; repos hold code.** The checkouts were deleted; every
document inside them was rescued first (see below).

## What was rescued

Nothing readable was thrown away. Before deletion, every `.md`, `.jsonl`, `.txt`,
`.pdf`, `.mht`, `.skill`, and extensionless text file was moved out:

| Destination | Files | Includes |
|---|---|---|
| `open-wiki/` | 3 | `openwiki.md`, `openwiki.jsonl`, repo description |
| `llm-wiki/` | 27 | READMEs (EN/CN/JA/KO), Termux setup notes + SKILL, `2510.14823v1.md` (paper), `LICENSE`, `SHA256SUMS`, two `.mht` captures, `memory-as-skill.skill` |

## Tools

### `open-wiki/`
A CLI that writes and maintains agent documentation for a codebase.
- Fork: `c10vis-poem/openwiki`
- Role in the stack: candidate for `file-management-system/tier-2-structural/`
  — generating the `llm_wiki.md` layer the section kit requires.

### `llm-wiki/`
Rust CLI + browser-extension pair for LLM-assisted wiki capture; ships its own
`llama-cli`/`llama-server` binaries.
- Fork: `c10vis-poem/llm_wiki`
- Role: the Termux-side capture path. The setup notes and SKILL are the
  load-bearing part; the vendored `llama-*` binaries are **not** the project's
  LLM path (see the Superseded table in `Horizons-UI/CLAUDE.md`).

## Status

All entries here are `designed-only` with respect to *this* stack — they are
forked and documented, not integrated. See `../canon/STATE-OF-EXISTENCE.md`.

## Still to be filed here

From `(AESOP.]build/`: `#AIDER_AGENT`, `#HERMES_AGENT`, `#CLAUDE.CODE_ANDROID-CLI`,
`#OPEN-CLAUDE_ANDROID`, `#CLAUDE_Ai` (67 files, needs per-file triage).
Per `NOVA-CORPUS-PLAN.md` §9 these are **candidates, not redundancy to prune** —
which one wins is decided by use, not by tidying.
