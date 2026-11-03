# NovusÆxenti-Housekeeper

**Slug:** `file-administrator` · **Role:** vault file administration · **Tier:** admin

## What problem this solves

Keeps the vault tidy: naming canon enforcement, MAP.md regeneration, manifest.jsonl compaction, dead-link sweeps.

## Binding

| Field | Value |
|---|---|
| Model | GLM-5.2 (cloud, OpenRouter) |
| Node | Delta |
| Memory scope | Declarative + Strategic |
| Tool allowance | full vault write, git |
| Harness | see `harnesses/` |

## Data flow

1. Trigger arrives (operator, schedule, or upstream agent).
2. Agent reads `MAP.md` first — non-negotiable, every session, every agent.
3. Retrieval: `manifest.jsonl` query -> targeted leaf notes. Never load a whole tier.
4. Work happens under the harness's control loop.
5. Trajectory written to `05_episodic_logs/` with speaker attribution intact.

## Failure mode

_To be filled from first real run. Do not guess it here._

## Open questions

_Track in `novae-xorpus/unresolved.md`, not inline._

---

## Wiki admin (added 2026-10-28)

This package is also the operator's **wiki admin**: the files administrator that turns a raw document dump into clean Markdown, a reviewed LLM wiki and JSONL indexes. Same agent, same data-flow rules above (MAP.md first, manifest.jsonl retrieval, never load a whole tier). Claude Code is the build tool and the session shell; the heavy model work runs on Gemini.

### Binding change
| Field | Old value (2026-09-06, commit 71e90e8) | New value (2026-10-28) | Reason |
|---|---|---|---|
| Model | GLM-5.2 (cloud, OpenRouter) | Gemini via Google AI (`gemini-3.8-flash` bulk, `gemini-4-argon` large context; env `GEMINI_MODEL`, `GEMINI_MODEL_LARGE`) | Operator order 2026-10-28: wiki-admin inference (bulk extraction, drafting, large-context queries) runs on Gemini/Google |
| Node | Delta | Alpha (phone) for the session; Gemini API for inference | Runs from the `wiki-admin` launcher on the phone |

### Operator decisions applied
- OpenWiki TUI / LangChain `openwiki` CLI is **dropped** (and the "OpenWiki TUI File Executor" role). Records: vault `handoff/2026-10-24/extracts/latest-config-extract.md` L219 (OP L9913), `docs/WIKI-ADMIN-GUIDE.md` sections 3 and 7.
- Used instead: OpenWiki for Claude Code, openwiki-skills, llm-wiki-nocode, obsidian-wiki. Where they overlap, one customized skill replaces them (below).
- New material goes to `01-inbox/` until reviewed (`~/wiki-admin/AGENTS.md`). Nothing is promoted without the operator naming it.

### Flow (capture -> stage -> verify -> promote)
1. `convert_raw_to_md.py RAW OUT` (reports EMPTY/ERROR/unsupported by name)
2. `verify.py OUT --raw RAW` (vault `tools/check.py`, independent extractors, canary first; the converter never judges itself)
3. `manifest.py build` (JSONL index, full sha256, deterministic retrieval tokens, per-tier)
4. `gemini_infer.py draft|w5h|ask` (privacy filter refuses private/pii/credential files; dry-run without a key) -> `01-inbox/`
5. `audit_staging.py 01-inbox --wiki WIKI` (Cross-Auditor six checks: duplicates, orphans, naming canon, ADR contradictions, missing MAP.md, credential leakage)
6. operator approves by name -> `promote.py PAGE --approved-by NAME`
Scripts: NovAExopia `tools/wiki-admin/` (branch `wiki-admin-tools`). Skills: NovAExopia `skills/wiki-admin-core/`.

### Attached toolset (checked 2026-10-28 with `claude plugin list` run in ~/wiki-admin, and file listings)
| Tool | Path | Loads in a `wiki-admin` session? |
|---|---|---|
| launcher | `~/bin/wiki-admin` (Claude Code in `~/wiki-admin`, vault + repos attached) | yes |
| OpenWiki for Claude Code | `~/repos/NvAEx-openwiki-for-claude-code/plugins/openwiki` | yes: enabled by project settings (user setting disabled) |
| openwiki skill | `~/.claude/skills/openwiki` | yes (user skill) |
| openwiki-skills | fork `c10vis-poem/NvAEx-openwiki-skills` | no: not installed; merged into `wiki-admin-repo-docs` |
| obsidian-wiki | `~/repos/AEsops-obsidian-wiki` | yes: enabled (project) |
| llm-wiki-compiler | `~/repos/llm-wiki-compiler-NvAEx/plugin` | yes: enabled (project) |
| llm-wiki-nocode `/llmwiki-*` | `~/wiki-admin/.claude/commands/llmwiki-{ingest,query,lint}.md` (fork `~/repos/NvAEx-llm-wiki-nocode`) | yes (project commands) |
| anydoc | `~/wiki-admin/.claude/skills/convert-documents-to-markdown` -> `~/repos/aesop-anydoc`; `~/bin/anydoc` | yes |
| NotebookLM | `~/wiki-admin/.claude/skills/notebooklm`, `notebooklm` CLI | yes; first use needs `notebooklm login` |
| corpus-verify | `~/.claude/skills/corpus-verify` (+ vault `tools/check.py`) | yes (user skill) |
| corpus-batch-processing | `~/.claude/skills/corpus-batch-processing` | yes (user skill) |
| wiki-admin-core (6 skills) | NovAExopia `skills/wiki-admin-core/` | not yet: link into `~/wiki-admin/.claude/skills/` after merge |

### Customized skills and what they replace for this agent
| Skill | Replaces |
|---|---|
| `wiki-admin-ingest` | `/llmwiki-ingest`, obsidian-wiki `/wiki-ingest` + `/wiki-stage-commit`, llm-wiki-compiler `/wiki-ingest` |
| `wiki-admin-query` | `/llmwiki-query`, obsidian-wiki `/wiki-query`, `/openwiki:ask`, llm-wiki-compiler `/wiki-query` |
| `wiki-admin-lint` | `/llmwiki-lint`, obsidian-wiki `/wiki-lint`, llm-wiki-compiler `/wiki-lint` |
| `wiki-admin-repo-docs` | `/openwiki:generate`, `/openwiki:update`, `/openwiki-init`, `/openwiki-update` |
| `wiki-reference-router`, `w5h-extraction` | (new; operator texts) |

### Failure mode
First real runs (2026-10-28, sample files): scanned PDFs extract no text (reported EMPTY, need OCR); a converter that shares the checker's library is refused (NOT-INDEPENDENT). Live Gemini output not yet seen: no key stored.
