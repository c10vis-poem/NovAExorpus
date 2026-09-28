# Session failure log — 2026-09-09, part 2 (supplements part 1)

Read `session-failures-2026-09-09.md` first — this does not replace it. Sources read this
session before writing this file: that log in full; `mcp__mem0-mcp__get_memories` with
`{"AND":[{"user_id":"default"}]}` (49 memories, all pages — `next:null`); the published
Artifact "NovÆxorpus Manifest" (`58f62bbd-02d8-43a9-ab66-ea1e9aa66247`), read in full via
`Artifact action:"read"`; `~/novae-xorpus/tools/check.py` (read directly, lines 495–534);
`~/novae-xorpus/MASTER-RESUME.md` and `unresolved.md` (grepped, not fully read — see below);
plus direct `find`/`git log --all`/`diff` against the live filesystem for every claim below.

## State of the corpus, verified

- **`raw_database/raw/` top-level file count: 100.** Verified: `find raw/ -maxdepth 1 -type f | wc -l` → 100.
- **`raw_database/raw/` recursive count (incl. nested subfolders): 106.** Verified: `find raw/ -type f | wc -l` → 106. The subfolders are `1 vault_root/`, `5- vault_root/`, `memory-as-skill/`, `memory-as-skill.skill/`, `termux-helper.skill/`, `technical-builder-style.skill/`, `FINAL-Bench/`, `_res/`, `primary:Download/`. **Both 100 and 106 are real numbers measuring different things** — 100 is what's directly in `raw/`, 106 is everything under it including nested dirs. Neither is "wrong"; docs that say 106 without qualifying it are ambiguous, not necessarily false.
- **`raw_database/clean_md/` count: 97, not 98.** Verified: `find clean_md/ -type f` → 97, `find clean_md/ -type f -name "*.md"` → 97, no subdirectories, no hidden files. The brief handed to this session said 98 — that number does not check out; 97 is what's actually on disk as of this write.
- **Confirmed real, on disk:** `~/novae-xorpus/tools/clean.py` (4533 bytes, Aug 27), `~/novae-xorpus/tools/check.py` (33154 bytes, Aug 27), `~/.claude/skills/corpus-batch-processing/SKILL.md`, `~/.claude/skills/parallel-session-orchestration/SKILL.md`. Verified by direct `ls -la`.
- **Confirmed fabricated — `doc_to_skill_and_tool.py`, `htp_partition_calc.py`:** absent from the working tree of both `~/novae-xorpus` and `~/repos/aesop-xi`, and absent from `git log --all --name-only` (all branches, both repos) grepped for both names — zero hits. The published Artifact (`58f62bbd...`) claims both as real and "smoke-tested" with specific paths (`novae-xorpus/tools/doc_to_skill_and_tool.py`, `aesop-xi/tools/htp_partition_calc.py`) — that claim is false.
- **`snapdragon-npu-partitioner` skill: absent.** `find ~/.claude/skills -iname "*snapdragon*" -o -iname "*npu-partition*"` → no hits (one unrelated hit: `aesop-voice-pipeline/references/htp-backend-mismatch.md`, a reference doc, not a skill). Not found verbatim in the 49 mem0 memories or in the artifact's tools section either — it appears to be this same fabricated NPU-partitioning idea (as `htp_partition_calc.py`) described a second way, not a separately-invented third thing. Flagging as unconfirmed-by-exact-name rather than asserting a source I couldn't produce.
- **`honey-for-devs` — mixed, do not flatten this to one verdict.** Two different things share the name:
  1. A mem0 memory (`3afc1a8d...`, `user_id: default`) claims "User imports the 'honey-for-devs' package and uses its eson.stringify function to compress JSON payloads before sending to the LLM" — **this specific usage claim is fabricated.** `~/novae-xorpus` git history has only an empty wiki scaffold stub at that path (commit `3d923cd`, `data_vault/02_wiki_md/harnesses/honey-for-devs/README.md`, contents: "scaffold, awaiting content" — no code, not in current HEAD).
  2. `~/repos/NoVa-honey-for-devs` **is a real repo** (the operator's own fork, `git@github.com:c10vis-poem/NoVa-honey-for-devs.git`) with a real `eso/` module (`index.js`, `ccr.js`, tests) implementing an ESON codec — but `eson.stringify` as a function name doesn't appear in it; the codec's actual verbs are `stash`/`retrieve`/`crush`. This repo has no evident connection to the `raw_database`/`novae-xorpus` corpus project — it's a different, unrelated tool that happens to share a name with the fabricated wiki stub. Per this device's own memory rule ("check `~/repos/` for the user's own fork before pulling from upstream"), don't assume "fabricated" here means "doesn't exist anywhere" — it means "not part of this project," which is a different and more useful thing to know.
- **`check.py`/`corpus-batch-processing` integration bug — confirmed real, root cause located and read directly.** `check.py` line 514 (`~/novae-xorpus/tools/check.py`): `key = fm.get("source", "")` takes the clean file's frontmatter `source:` value verbatim (e.g. `raw/1_COGNITIVE_REPOSITORY_ARCHITECTURE.md`, confirmed by reading actual clean_md frontmatter) and checks it against `sources` (line 506–508), which is built from `os.path.relpath(.... SRC)` — i.e. paths *relative to* `raw/`, with no `raw/` prefix (e.g. `1_COGNITIVE_REPOSITORY_ARCHITECTURE.md`). The prefixed key never matches an unprefixed source, so every file falls to `elif key not in sources: orphans.append(...)` (line 519). This is a real, previously-undiscovered integration bug between two skills, not a data-quality problem.
- **The scratchpad patch did not produce real numbers — check this before trusting anything from that run.** A `check_patched.py` exists at `.../scratchpad/raw_database_verify/check_patched.py` with a one-line fix at line 514 (`key = key[4:] if key.startswith("raw/") else key`). But by file mtime, `check_patched.py` was created *after* `03-check/FINDINGS.jsonl` was already written (`check_patched.py` timestamp 1788996905 vs. `FINDINGS.jsonl` timestamp 1788996866 — the patch is ~39 seconds younger than its own supposed output). **The 03-check/ output in the scratchpad was generated by the unpatched check.py**, and indeed every one of its 106 FINDINGS.jsonl entries reads `"severity": "FAIL", "class": "no counterpart"` — i.e., it reproduces the bug, not a fix. **No real verified pass/fail numbers exist yet for raw_database.** The patch needs to actually be run against the corpus (or, better, turned into a real fix in `check.py` or a documented convention reconciliation with `corpus-batch-processing`'s frontmatter format), and the result re-checked by mtime/content before it's trusted.
- **`spark_recommendations/04_DUPLICATES_AUDITS_AND_LOGS/`** verified present: `00_LEX_NOVI_MASTER_AUDIT_SYNTHESIS.md` + `AUDIT_01` through `AUDIT_11` (11 audits, plus `run_audit.sh`) — real file-by-file disposition work, but for `___Lex-Novi-Æxentis-Copiæ` (a different source tree), not `raw_database/raw/`. Useful as a *method* reference, not as raw_database's own disposition list.
- **`spark_recommendations/03_ALTERNATIVES_PROPOSAL_V2/` and `04_DUPLICATES_LOST_AND_ARCHIVE/`** verified empty: each contains only a `POINTER.md` stub (187–193 bytes), no content.
- **`~/novae-xorpus/MASTER-RESUME.md` and `unresolved.md`** exist (100 and 105 lines) but grepping both for `raw_database|clean_md|corpus-batch|check.py|clean.py` returns zero hits — confirmed not relevant to this task, they're aesop-xi/ECC-hook/DroidDesk/OmniRoute backlog auto-mirrored into novae-xorpus.

## What not to do

**Treating an artifact or memory claim as verified without checking disk/git.** The published
"NovÆxorpus Manifest" artifact states `doc_to_skill_and_tool.py` is "written this session...
smoke-tested" and `htp_partition_calc.py` is a real NPU partition calculator "extracted from
the HTP raw source," each with a specific path. Neither file exists anywhere in either repo's
working tree or its entire git history, on any branch. A polished, specific, confidently-worded
claim in a document is not evidence; `git log --all --name-only | grep` and `find` are. Apply
this to every artifact and every memory equally, including the one that gave you this brief.

**Fabricated claims skew toward impressive jargon; real work trends mundane — that's a tell.**
`htp_partition_calc.py` ("NPU memory partition calculator" for a Snapdragon HTP backend) and
the `snapdragon-npu-partitioner` skill sound sophisticated and technically specific — and this
project never loads a local model or touches the NPU/Hexagon DSP anywhere in its actual scope
(corpus cleaning and disposition of markdown files). Meanwhile the two tools that are actually
real and running — `clean.py` and `check.py` — are unglamorous: a furniture-stripper and an
independent text-diff checker. When a claimed capability sounds more advanced than the project
currently needs, that mismatch is itself worth checking before repeating it.

**Reaching for cross-system search before `ls`-ing the obvious local folder.** This session
initially reached for git history archaeology and memory search to answer questions
(`04_DUPLICATES_AUDITS_AND_LOGS/`, the `03_ALTERNATIVES_PROPOSAL_V2/`/`04_DUPLICATES_LOST_AND_ARCHIVE/`
stubs) that a single `ls`/`find` on the named, self-descriptive folder answered immediately.
Every `POINTER.md` in this tree is an empty "Authority:" stub — it is never where the real
navigation lives; the actual folders and files are. Try the direct local path first.

**Reprocessing a PDF by hand instead of using the operator's own dedicated tool.** LiteDoc (an
installed Android app) is the operator's chosen PDF→markdown converter. `pdftotext` or
Read-tool PDF extraction as a substitute is redundant work product that the operator didn't ask
for and that duplicates what LiteDoc will produce — wait for its output instead of working
around it.

**Trusting a scratchpad "fix" without checking whether it actually ran.** `check_patched.py`
existed in this session's scratchpad, which is necessary but not sufficient evidence that it
produced the FINDINGS.jsonl sitting next to it. The file's own mtime proved it postdated the
run it was assumed to have produced. Compare timestamps (or better, re-run and confirm) before
citing a patched tool's output as real numbers.

**Handoff material for one project scattered across four uncoordinated places, with no index.**
This session's actual prior-session state lived in: a markdown file
(`raw_database/audit/session-failures-2026-09-09.md`), a memory system (mem0, `user_id: default`
— not the MCP connector's own default `user_id`, which returns nothing), a published web
Artifact (which contradicts the markdown file on two tool claims), and a different subproject's
auto-mirrored backlog files (`~/novae-xorpus/MASTER-RESUME.md`, `unresolved.md`) that turned out
to be irrelevant noise for this task. No single document points to all four. That scatter is a
problem independent of any one document's accuracy — the fix is a single next-session pointer
that names all four locations and what each one is actually good for, not more documents.

## Open items for next session

- Turn the `check.py`/`corpus-batch-processing` frontmatter mismatch into a real fix (either
  `check.py` strips a `raw/` prefix natively, or the two skills agree on one convention) and
  re-run it against `raw_database` for real — no verified pass/fail numbers exist yet.
- Reconcile the 100-vs-106 `raw/` count going forward: state explicitly whether "how many raw
  files" means top-level or recursive-including-subfolders, since both are real and this is an
  easy place to reintroduce a false "discrepancy."
- `raw_database/raw/` disposition judgment (port/combine/omit) is still not applied to the bulk
  of the ~100 files — the `spark_recommendations/04_DUPLICATES_AUDITS_AND_LOGS/` audits are a
  usable model for *how*, applied to a *different* tree; this one still needs its own pass.
- Write (or ask the operator to designate) one next-session pointer naming all four scattered
  handoff locations, so this doesn't need re-discovering.
