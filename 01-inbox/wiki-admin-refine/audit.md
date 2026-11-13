---
status: staged
source: wiki-admin session 3c1dfa47, contract A2 task E
date: 2026-11-11
---
# Audit: greedy-crane wiki admin setup (read-only)

**Read in full this session:** `agents/wiki-admin.md`, `agents/corpus-ingest.md`, `docs/wiki-admin.md`, `docs/TOOLS.md`,
`scripts/README.md`, `skills/README.md`, `skills/wiki-admin-ingest/SKILL.md`, `skills/cli-tools/SKILL.md`, `MANIFEST.md`,
`hooks/hooks.json`, `hooks.json` (plugin root), NovAExopia `plugins/nvaex-wiki-admin/README.md`.
**Listed only (names, sizes):** `scripts/` (30 files), `skills/` (23 skills, 2,669 lines total), `docs/`, `hooks/`.
**Not read:** the other 21 SKILL.md bodies, every script body, `docs/WIKI-ADMIN-GUIDE.md`, `docs/spec/`, `docs/homework/`,
`docs/workspace/`, `package/`, `SOURCES.md`, `skills.json`, `skill-provenance.json`, `tests/`, `hooks/*.sh`.
Part 2 reads those before any edit.

Fix codes: **K** keep, **E** edit, **M** merge, **D** delete. Every item waits for the owner's approval by number.

## Spec and agent file
| # | Finding | Where | Fix |
|---|---|---|---|
| 1 | Spec title and role are the old Housekeeper ("NovusÆxenti-Housekeeper", slug `file-administrator`) | docs/wiki-admin.md:1-3 | E: retitle as the wiki admin |
| 2 | Spec binds the agent to Gemini API ("Gemini via Google AI", "Gemini API for inference"); agent file says it need not run on Gemini; owner (2026-11-11): CLI with account credits, never the API | docs/wiki-admin.md:13-14, 39, 44; agents/wiki-admin.md:40 | E: route table (CLI first: `agy`, local models, OpenRouter for frontier) |
| 3 | Spec points at old homes: NovAExopia `tools/wiki-admin/`, `skills/wiki-admin-core/`, `~/wiki-admin` launcher, `~/wiki-admin/AGENTS.md` | docs/wiki-admin.md:50, 59, 64-75 | E: plugin `scripts/`, `skills/`; launcher `crane` |
| 4 | Spec flow (6 steps) lacks size gate, injection scan, crush, ledger, 4-worker pool, extract_artifacts, dedup, skill factory | docs/wiki-admin.md:52-58 vs skills/wiki-admin-ingest/SKILL.md:17-31 | E: spec points to the ingest skill instead of copying it |
| 5 | Spec skill table lists 6 skills; agent names 19; plugin has 23 | docs/wiki-admin.md:77-84; agents/wiki-admin.md:42 | E |
| 6 | Failure mode never filled; "no key stored" dated 2026-10-28 | docs/wiki-admin.md:29, 87 | E from part 2's route tests |
| 7 | Agent file: "Gemini app and Spark agents" and "Google Cloud projects" named, no route says how to reach them | agents/wiki-admin.md:40 | E: name `agy` (Antigravity CLI, `/swarm`) per research.md |
| 8 | Agent file: Gemini embeddings "through the API" and "`gemini-api` command is not installed yet"; on-device route named "EmbeddingGemma" | agents/wiki-admin.md:46 | E: EmbeddingGemma 2 LiteRT (text 270M first), API only if owner names it |
| 9 | Agent preloads 8 skills; 11 named in its body are not preloaded (w5h-extraction, wiki-admin-repo-docs, llm-wiki, wiki-dedup, ...) | agents/wiki-admin.md:4-12, 42 | owner decides: K (load on demand) or E |
| 10 | `skills/README.md` titled "wiki-admin-core", names agent `NovusAExenti executor-core/wiki-admin/`, indexes 6 of 23 skills | skills/README.md:1-3, 5-12 | E: index all 23 |
| 11 | `scripts/README.md` names agent `NovusAExenti executor-core/file-administrator/`; MCP command uses `<repo>/tools/wiki-admin/`; indexes 7 of 30 scripts | scripts/README.md:3, 21, 5-13 | E |

## Workers and tools
| # | Finding | Where | Fix |
|---|---|---|---|
| 12 | corpus-ingest preloads `honey` and `honey-px`; not found in `~/.claude/skills`, the vault `plugins/` or NovAExopia `plugins/` (find, depth 3) | agents/corpus-ingest.md:7-8 | owner decides: point at their real home, or drop |
| 13 | TOOLS.md: OCR "open: no OCR tool chosen yet"; scanned PDFs come out EMPTY | docs/TOOLS.md:12; docs/wiki-admin.md:87 | part 2: pick OCR (Gemini 3.8 Flash via `agy`, or local Qwen 3.5 0.8B, which is vision-language) |
| 14 | TOOLS.md fan-out: `gemini_infer.py` (API) is the Gemini lane | docs/TOOLS.md:14 | E: `agy -p` headless lane, API as named fallback |
| 15 | cli-tools: web search only via `pplx` (needs `PERPLEXITY_API_KEY`, "do not fall back"); Gemini "needs `GEMINI_API_KEY`" | skills/cli-tools/SKILL.md:10-17, 34 | E: add `agy`, OpenRouter, local routes; owner decides whether Bing/claw stays barred (DuckDuckGo blocked this session) |
| 16 | TOOLS.md says "checked 2026-10-29"; references `~/.claude/session-work/2026-10-29/...` index (session scratch path) | docs/TOOLS.md:3 | E: move the index into the plugin `docs/` or re-check |

## Hooks
| # | Finding | Where | Fix |
|---|---|---|---|
| 17 | MANIFEST says hooks are drafts only, "no hooks/hooks.json"; `hooks/hooks.json` now registers quarantine + stop-gate | MANIFEST.md:23 vs hooks/hooks.json:1-10 | E MANIFEST |
| 18 | MANIFEST: "the plugin copy steps aside" (root-settings wiring); the step-aside switch was removed 2026-11-09 | MANIFEST.md:45; NovAExopia PENDING.md:27 | E |
| 19 | Root `hooks.json` is an AGY hook set (`read_file|view_file`, `PreInvocation`) beside `hooks/hooks.json` (Claude) | hooks.json:1-10 | K, but name it in MANIFEST as the AGY copy |
| 20 | Same quarantine + stop-gate hooks also ship in NovAExopia `nvaex-wiki-admin` (with kill switches) | nvaex-wiki-admin/README.md:20-26; PENDING.md:42 | see #21 |

## Duplicate plugin
| # | Finding | Where | Fix |
|---|---|---|---|
| 21 | NovAExopia `plugins/nvaex-wiki-admin` is the "Frankenstein" source greedy-crane was built from: same pipeline, same scripts, same agents (`wiki-admin`, `corpus-ingest`), still has kill switches (`~/.nvaex-hooks-off`), selftest 20 checks passed 2026-11-05; greedy-crane's ingest skill credits it | nvaex-wiki-admin/README.md:3-11, 20-26, 32-54; skills/wiki-admin-ingest/SKILL.md:47; PENDING.md:64 | owner decides: D (greedy-crane is current) or keep as frozen source; first diff its scripts against greedy-crane's |

## Stray and doubled files
| # | Finding | Where | Fix |
|---|---|---|---|
| 22 | `wa_quarantine.py.bak` beside `wa_quarantine.py` | scripts/ | D after a diff shows the .py is newer |
| 23 | `__pycache__/` (check, wa_quarantine .pyc) in the vault, a public repo | scripts/__pycache__/ | D + `.gitignore` entry; first check whether git tracks them |
| 24 | Two manifest builders: `manifest.py` and `wiki_admin.py` ("different from scripts/manifest.py") | MANIFEST.md:18 | M or K after reading both |
| 25 | `killswitch.sh` still in scripts (switches were removed elsewhere on owner order) | scripts/killswitch.sh | read it; D if nothing calls it |
| 26 | Uncommitted kill-switch removal in the 2026-11-10 NovAExorpus clone breaks greedy-crane selftest | NvAEx-Recaps handoff/2026-11-11/handoff.md:41-43 | owner decides: revert or finish |

## Not checked yet (part 2)
Script bodies (dead code, stale model ids in `gemini_infer.py`), the 21 unread skills, `skills.json` and `skill-provenance.json`
freshness, `package/file-administrator/AGENT.md` (GLM-5.2 / Delta, MANIFEST.md:31), `docs/WIKI-ADMIN-GUIDE.md`, `commands/llmwiki-*`.
