# P4 · Wiki core and structure

Author: Sonnet, 2026-10-30. Read-only; no installs, pushes, or edits outside this folder.
Paths: `LW` = `~/.claude/plugins/synced/a5d13a90-…_b410cc73-…/a37bed19-f9ad-42b8-858c-cc6cd62f79d7` (llm-wiki); `WW` = `…/cc779a20-…` (wiki-wonka); `SF` = `…/e40abd7f-…` (create-smartfolder); `ON` = `…/3cacb896-…` (obsidian-notes); `CW` = `…/5c75f9c6-…` (cut-weight); `PS` = `…/ed4e6728-…` (project-scaffolder); `OS` = `~/.claude/plugins/cache/local-zips/obsidian-sync/0.1.0`; `VAULT` = `/storage/emulated/0/Documents/NovAExorpus`; `GC` = `~/repos/.wt/vault-session/plugins/greedy-crane`.
Read marks: FULL = read start to end; PART = outline plus named sections; DESC = manifest or description only.

## Read status (pass 2, after the coordinator asked for a full read)

Total non-media text in the 7 plugins is about 2.2 MB (llm-wiki 1.5 MB, smartfolder 0.29, scaffolder 0.14, obsidian-notes 0.14, wonka 0.07, cut-weight 0.06, sync 0.03). I could not read all of it in one context. What I did read in full, and what I did not:

| Plugin | Full read | Not read (bytes) | Why it does not change the verdict |
|---|---|---|---|
| wiki-wonka | all 3 skills, the agent file, README, SCHEMA, sample wiki, all 6 hooks, CONTRIBUTING, SECURITY, .vscode, .gitignore | `CODE_OF_CONDUCT.md` (5 KB), `.github/agents/wiki-wonka.agent.md` (6 KB, a copy of the agent file) | boilerplate and a duplicate |
| cut-weight | SKILL.md, all 7 references, README | `scripts/inventory.py` body (14 KB): outline and a grep for side effects only | only write is `open(out, "x")` at line 269 |
| obsidian-sync | SKILL.md, command, plugin.json | `sync_to_obsidian.py` (15 KB): outline only | cut on the command and mode text |
| obsidian-notes | SKILL.md, README, AGENTS.md, CLAUDE.md, MAINTENANCE.md, evergreen.json, setup.md, `vault_lint.py` lines 56-72, 275-372, 409-640 | RESEARCH, CHANGELOG, LEARNINGS, TESTS, evals, test_vault_lint.py, ai-docs (about 90 KB) | self-maintenance files, all cut |
| project-scaffolder | wiki-gc, wrap, both hooks, SKILL.md lines 1-200, 280-320, 520-545, README 151-165 | 18 other commands, 6 other skills (about 73 KB), SKILL.md rest | the packet scopes this plugin to the 4 rules and `/wiki-gc` |
| create-smartfolder | SKILL.md lines 1-480, kit script headers | `DEPOSIT_SPEC.md`, `UPGRADE_PATH.md`, `VERSION_HISTORY.md` (31 KB), kit examples (175 KB), repo docs (47 KB) | kit and specs for building a human archive; cut |
| llm-wiki | SKILL.md, 7 of 10 references (architecture, agent-memory, graph, ingest, query, lint, page-conventions; scaling-playbook lines 1-60), `wiki_lint.py` lines 82-300, `wiki_search.py` outline and key sections, command wrapper for ingest | `wiki_evolve*.py` (113 KB), `integrations/` (507 KB), `eval/` (410 KB), `docs/` text (115 KB), README/CHANGELOG/CONTRIBUTING (62 KB), `wiki_graph_*.py` (48 KB), `init_wiki.py`, `setup_wiki.py` after line 80, `wiki_stats.py`, `evolution-workflow.md`, `retrieval-setup.md` after line 30 | all of these are on the cut list for other reasons (another product's plugin, test fixtures, docs site, evolve loop that belongs to P5) |

I did not read these by choice of verdict; I read the others to decide. If you want the cut parts read line by line anyway, say so and I will do it in separate passes (llm-wiki `integrations/` and `eval/` alone are 0.9 MB).

## 0. Summary

1. **llm-wiki is the core. Keep, heavily trimmed** (5.4 MB to about 0.3 MB). Cut `evolve*`, `integrations/paperclip`, `docs/`, `eval/`. It has no hooks and no MCP server.
2. **wiki-wonka: cut, except a few ideas.** Its three skills duplicate llm-wiki and `wiki-admin-*`. Its 6 hooks are already switched off (the folder is `hooks.off-20261028/`). Keep only the callout vocabulary, `overview.md` and the language setting.
3. **create-smartfolder: trim to the tier idea** (`_README.md` per folder, `As of` line, provenance, decay). Cut the interview, the naming rules and the kit.
4. **obsidian-notes: keep only `vault_lint.py`.** It uses the standard library only. There is a link-form conflict with llm-wiki, decided in section 4.
5. **obsidian-sync: cut.** Its command hardcodes `D:\` paths, and symlink mode moves files into the vault, which breaks "raw is read-only".
6. **cut-weight: keep the idea, cut the repo.** Its archive-outside-the-tree recovery protocol maps to `_archive/`. Use it for the corpus-wide dedupe pass, not as a plugin.
7. **project-scaffolder: take only the 4 rules and `/wiki-gc`.** Both are tiny and map onto rules the work order already has.
8. **Vault finding that changes the plan:** `02_wiki_md/` is not a synthesized wiki. 519 of its 537 pages are byte-identical copies of cleaned files (check in section 5). Its `manifest.jsonl` hashes the cleaned file, not the raw source, which breaks the work order section 3 contract. See section 5.

## 1. llm-wiki (core)

**Source:** github.com/praneybehl/llm-wiki-plugin, v3.2.0, MIT (`LW/.claude-plugin/plugin.json:3,8`). 5.4 MB, of which `docs/` is 3.2 MB (one 3.09 MB PNG, `docs/public/assets/llm-wiki-explained.png`), `integrations/` 0.86 MB, `eval/` 0.67 MB, `skills/` 0.45 MB (`du -sk`).

**Read:** FULL `skills/llm-wiki/SKILL.md` (187 lines); FULL `references/page-conventions.md`; PART `scaling-playbook.md` (thresholds 1 to 5); FULL `ingest-workflow.md`, `query-workflow.md`, `lint-workflow.md`; PART `retrieval-setup.md` (first 30 lines); PART `scripts/wiki_search.py` (header, `collect_pages`, `sync_vector_index`, argparse); PART `setup_wiki.py` (1 to 80); PART `commands/wiki/ingest.md`; header of `wiki_lint.py`. DESC only: `wiki_evolve*.py`, the `integrations/paperclip` code, `graph-workflow.md`, `architecture.md`. The coordinator asked for a full read of every plugin; for most plugins I read key files and outlines, not every line. Gaps are listed in section 11.

### Parts and verdicts

| Part | What it does | Verdict |
|---|---|---|
| `skills/llm-wiki/SKILL.md` (23 KB) | The pattern: raw, wiki, schema; ingest, query, lint; atomic pages (soft cap 400 lines, hard cap 800), index-first reading, sharded indexes | **Trim** to about 4 KB (draft below) |
| `scripts/wiki_search.py` (33 KB) | Section-level BM25, plus optional local vector search (bge-small, sqlite-vec) fused by RRF; filters by type, tag and date; `--backlinks`, `--top-linked`, `--json`, `--cache` | **Keep**, with 2 small patches (section 6) |
| `scripts/wiki_lint.py` (15 KB) | Orphans, broken wikilinks, page-size caps, frontmatter fields, stale pages, duplicate slugs; reports only, never edits | **Keep** |
| `scripts/wiki_stats.py` (6 KB) | Page counts by type, link density | **Keep** (small) |
| `scripts/init_wiki.py` + `assets/*.template` | Creates the folders and templates, then forces model setup | **Cut**. `SCHEMA.md` is written once by hand (section 3). Its forced setup needs `fastembed`, which is not installed here |
| `scripts/setup_wiki.py` | Installs fastembed, sqlite-vec and pyyaml, downloads the model, builds the vector index | **Cut for now** (needs installs; semantic search is optional later) |
| `scripts/wiki_graph_{extract,lint,query}.py` (48 KB) + `graph-workflow.md` | Typed graph in `wiki/graph/`, built from frontmatter `graph:` blocks | **Cut for now**. Stage 2 after the wiki exists (SKILL.md:44 says: no ontology file, no graph step) |
| `scripts/wiki_evolve*.py` (112 KB), `commands/wiki/{learn,evolve}.md`, `references/evolution-workflow.md` | Learn from tasks, propose skill changes | **Cut**. Belongs to P5's extraction loop (skill-provenance, compounded) |
| `commands/wiki/{ingest,query,lint}.md` | Slash wrappers | **Cut**. Replaced by `wiki-admin-ingest`, `-query`, `-lint` (`GC/skills/`) |
| `integrations/paperclip` (0.86 MB), `docs/` (3.2 MB), `eval/` (0.67 MB), `research/`, `pnpm-lock.yaml`, `.github/` | Another product's plugin, the VitePress site, test fixtures | **Cut** (about 5.1 MB) |
| `references/{page-conventions,scaling-playbook,architecture}.md` | Rules and thresholds | **Keep** page-conventions and scaling-playbook (about 12 KB). Skip the rest for now |

**Hooks:** none (no `hooks/` folder; `find -iname '*hook*'` returns nothing).
**MCP:** none (no `.mcp.json`).
**Scripts needed:** `wiki_search.py`, `wiki_lint.py`, `wiki_stats.py`. Dependencies: Python 3.10+ standard library only for `--no-embed`. The header lists `fastembed==0.8.0` and `sqlite-vec==0.1.9` (`wiki_search.py:5-6`) and `uv` is on PATH, but `import fastembed` and `import sqlite_vec` both fail on this phone, so vector search is untested here.

**Measured:** `python3 -I wiki_search.py "hexagon NPU" --wiki VAULT/02_wiki_md --no-embed --top 3` returned results in 1.45 s over the vault's 537 pages. No index is built and nothing is written to the vault.

**Docs claim vs code:** `page-conventions.md` says the scripts resolve frontmatter `sources:` like wikilinks. `grep` of `wiki_lint.py` shows no such handling (the only `sources` hit in `wiki_search.py` is a passthrough at line 655). That means sha256 values in `sources:` cannot cause false "broken link" findings.

### Trimmed draft: `wiki-admin-core/SKILL.md` (about 45 lines)

```markdown
---
name: wiki-core
description: Page rules, folder layout and local search for the corpus wiki. Load before writing, reading or linting wiki pages.
---
# Wiki core
Wiki root: VAULT/02_wiki_md. Schema: 02_wiki_md/SCHEMA.md (read first; it wins over this file).
1. Raw is read-only. Pages are written only to 01-inbox/ and reach the wiki through promote.py.
2. One page = one concept/entity/source. Soft cap 400 lines, hard cap 800; split, don't grow.
3. Read order: MAP.md -> indexes/<section>.md -> page. Never grep the whole wiki first.
4. Frontmatter on every page (see SCHEMA.md). `sources:` lists the sha256 of each raw source.
   A claim with no source hash is not written.
5. Edit surgically (str_replace). Never rewrite a whole page.
6. Never delete. Mark `status: superseded`, set `superseded_by`, leave a stub, move to _archive/YYYY-MM/.
7. Disagreement between sources: write both, add `> [!contradiction]`. Do not pick a winner.
8. Search: `python3 -I scripts/wiki_search.py "<terms>" --wiki 02_wiki_md --no-embed --json --top 8`
   Filters: --type, --tag, --since. Links: --backlinks <slug>. Hubs: --top-linked N.
9. After each batch run the rebuild checklist (P4-wiki-core.md section 6).
```

**Conflicts and winner:**
- llm-wiki lint requires `type,title,tags,created,updated` (`wiki_lint.py:346`). `audit_staging.py:19` requires `id,type,created,updated,sources`. Winner: the union in section 4. Run lint with `--required-fm` set to the union.
- `GC/skills/wiki-admin-ingest` step 4 sets `tier: 2` and `author: wiki-admin`. Those are kept.
- llm-wiki's `sources:` means source-page slugs (`page-conventions.md`). Ours means sha256. Ours wins, because the work order section 3 requires it.

**Bloat to strip:** about 5.1 MB (`docs/` 3.2, `integrations/` 0.86, `eval/` 0.67, lockfiles and the rest). Kept: about 0.3 MB.

## 2. wiki-wonka

**Source:** github.com/cooperacode/wiki-wonka, v1.0.2, MIT (`WW/.claude-plugin/plugin.json`, `WW/LICENSE:1`). 3.8 MB, of which `assets/imgs/logo.png` is 3.67 MB.
**Read:** FULL (see the read-status table): all three skills, the orchestrator agent, README, `wiki/SCHEMA.md`, the sample wiki, all hooks. Not read: `CODE_OF_CONDUCT.md`, the `.github/agents` copy.

| Part | What it does | Verdict |
|---|---|---|
| `skills/ingest` (232 lines) | 7 steps, with a "discuss with the user before writing" step (Step 2) and a "confirm the page list" step (Step 4) | **Cut**. Both steps stall a batch of 25 or more files, and `wiki-admin-ingest` already has the gate (convert, verify, stage, audit, approve) |
| `skills/lint` (222 lines) | Reads the whole index, then orphans, missing index entries, broken links, missing fields, stubs, contradictions, stale overview; presents items one by one | **Cut**. `wiki_lint.py` plus `audit_staging.py` cover the deterministic checks. The semantic pass is already `wiki-admin-lint` Phase 2 |
| `skills/query` (138 lines, full read) | 6 steps: restate the question, read `wiki/index.md`, read pages (2 levels of links), answer with `[[wikilinks]]`, offer to file the answer, suggest one follow-up; never opens `raw/` (`SKILL.md:135`) | **Cut** (duplicates `wiki-admin-query`; its rules are a subset) |
| `agents/wiki-wonka-orchestrator.agent.md` (158 lines, full read) | Frontmatter `memory: project`, `user-invocable: false`; startup reads `config.md`, `index.md`, last 5 log entries; routes to ingest/query/lint as `Agent` subagents; ingest is two-phase (analysis inline, write in a subagent). Has a hard limit "pause after ~20 file changes" (line 146) | **Cut**. The 20-change pause is the one idea kept (a batch guard; `wiki-admin-ingest` batches of 25 already imply it) |
| `wiki/SCHEMA.md` | Folder rules, three page templates, callouts, `index.md` and `log.md` formats | **Trim** into our `SCHEMA.md`: keep the callout vocabulary |
| `wiki/config.md` language setting | Prose language per wiki | **Cut**. `wiki-admin-ingest` already says English only |
| `assets/imgs/logo.png`, `.vscode`, CoC, CONTRIBUTING, `wiki/*.md` sample | Packaging | **Cut** (3.7 MB) |

**Keep from wonka (4 ideas, no files):**
- Callouts `> [!contradiction]`, `> [!outdated]`, `> [!gap]`, `> [!deprecated]` (`WW/wiki/SCHEMA.md` "Callouts"). Never resolve one without the operator.
- `wiki/overview.md` as a one-page synthesis of the domain, updated after each batch.
- `log.md` newest-first with `## [YYYY-MM-DD] ingest | title` headings (its own `SCHEMA.md` "log.md format"). Note: `promote.py:55-57` appends `- stamp promote …` lines at the end, so the two formats differ. Pick one (recommended: keep `promote.py`'s append format; the format is cheap to change in `promote.py`).
- "Never create pages outside the declared folders" (SCHEMA.md "What the LLM must never do").

**Hooks (6, all disabled):** `hooks.off-20261028/hooks.json` has PreToolUse `protect-raw.sh`, PostToolUse `git-autocommit.sh`, FileChanged (a jq echo), SessionStart `restore-context.sh`, Stop `suggest-lint.sh`, Stop (a desktop notification). Details:
- Only `protect-raw.sh` can block: it exits 2 on any Write or Edit to a path containing `raw/` (it blocks the agent's write, not reading). The other five exit 0 on every path: `git-autocommit.sh`, the FileChanged echo, `restore-context.sh` (prints the index and last 5 log entries after compaction), `suggest-lint.sh` (prints a nudge when 5 or more ingests have happened since the last lint), and a desktop notification. The work order rule 8 forbids hooks that block "the owner's direction", and the hook has no switch.
- `git-autocommit.sh` commits from `$CLAUDE_PLUGIN_ROOT`. The vault repo is public and synced by GitSync; an automatic commit per page write is wrong for the vault.
- Every command path uses `"$CLAUDE_PROJECT_DIR"/hooks/…`, so even if re-enabled it would look in the user's project, not in the plugin.
- Proposed merged version: **none from wonka.** Optional later: a SessionStart reminder to read `MAP.md`, not a blocker. Raw protection is better done with file permissions or a vault `.gitattributes` rule than with a hook.

**MCP:** none. **Scripts:** none. **Bloat:** 3.7 MB.
**Conflict:** wonka and llm-wiki both provide `ingest`, `query` and `lint`. Winner: `wiki-admin-*` (`GC/skills/`).

## 3. create-smartfolder

**Source:** github.com/idea2go2go/smartfolder-skill, v6.6.0, license "CC-BY-4.0 AND MIT" (`SF/.claude-plugin/plugin.json`). Prose is CC BY 4.0 (needs attribution if copied); the `.py` files are MIT (`SKILL.md` header comment).
**Read:** PART `SKILL.md` lines 1-220 plus the heading outline (550 lines in total). Docstring heads only for `gen_readmes.py`, `filing_integrity.py`, `smartfolder_watch.py`. DESC only: `DEPOSIT_SPEC.md`, the other kit examples.

| Part | What it does | Verdict |
|---|---|---|
| Tier model (`SKILL.md:112-121`) | Tier 1 `CLAUDE.md` (under 150 lines), Tier 2 `_README.md` per folder as a local router, Tier 3 sidecars and syntheses, then raw | **Keep as an idea**. It is the folder-guide rule the work order wants ("folder guides") and matches `wiki-reference-router` (MAP.md then target) |
| "Every derived surface is dated and ranked" (`SKILL.md:147`) | `As of YYMMDD` line, provenance, decay condition, "raw beats derived" | **Keep as a rule**: maps to `updated`, `sources`, `as_of` in section 4 |
| Sidecar summary `<stem>_Summary.md` (`SKILL.md:190`) | A cache for long files | **Cut**. A wiki `sources/` page already is the sidecar |
| Interview (7 dials, `SKILL.md:221-263`) and 7-phase build with review gates (`:332-454`), a monthly network version check deposited into every folder (`:105`), naming scheme (`YYMMDD_Theme_…`), SmartFolder kit (`assets/kit`, 0.2 MB), `references/*` | Customised build for a human's archive | **Cut**. The vault already has its own naming canon (`NAMING-CANON.md`) |
| `gen_readmes.py` (30 KB) | Writes `_README.md` per folder, with a body-hash marker so human edits are never overwritten | **Cut as code** (hardcodes "Rowan, Tess and Shared" archives). **Keep the body-hash marker idea** for generated `MAP.md` files |
| `filing_integrity.py`, `smartfolder_watch.py` | Snapshot/scan a tree for added, changed, removed, moved files | **Cut**. `manifest.py build` plus sha256 compare does the same job (`GC/scripts/manifest.py`) |

**Trimmed draft (folder-guide rule, goes into `SCHEMA.md`):**
```markdown
Every wiki folder has a MAP.md: one line per child, `[title](path): when to read it`, under 200 lines.
MAP.md starts with `As of YYYY-MM-DD`, names its derivation (e.g. "generated from manifest.jsonl"),
and says when it may be wrong (decay). Raw/source files beat pages; pages beat MAP.md.
A generated MAP.md ends with <!-- body-sha256:… -->; a human-edited one is skipped on regeneration.
```
**Hooks:** none. **MCP:** none. **Bloat:** 0.2 MB kit plus 36 KB skill. **Conflict:** `MAP.md` (vault routers, `wiki-reference-router` step 1) vs `_README.md` (smartfolder). Winner: `MAP.md`, because the vault, `AGENTS.md` and the router skill already use it.

## 4. obsidian-notes and obsidian-sync

**obsidian-notes** — github.com/m4bwav/obsidian-notes (work order P4 table), v0.2.1, MIT (`ON/.claude-plugin/plugin.json`). 0.7 MB, of which `icon.png` is 0.4 MB.
**Read:** FULL `skills/obsidian-notes/SKILL.md`; docstring head of `vault_lint.py` (40 lines). DESC only: `RESEARCH.md`, `MAINTENANCE.md`, `evals/`, `ai-docs/`, `setup.md`.

| Part | What it does | Verdict |
|---|---|---|
| `scripts/vault_lint.py` (27 KB, standard library only, Python 3.9+) | Reports broken or case-mismatched links, ambiguous wikilinks, orphans, duplicate basenames, folders with no index, bad frontmatter; `--fix-index` writes `INDEX.md`; `--to-markdown-links` rewrites wikilinks | **Keep** as an auditor. **Do not** run its `--to-markdown-links` or `--fix-index` on `02_wiki_md` without the operator (see conflict) |
| `SKILL.md` Steps 0-4 | Step 0 reads `evergreen.json` and demands `evergreen-refresh`; Step 4 is vault setup and the Obsidian CLI | **Trim** to Steps 2 and 3 (about 15 lines). Cut Step 0 (needs the evergreen plugin) and Step 4 |
| `test_vault_lint.py`, `evals/`, `RESEARCH.md`, `CHANGELOG.md`, `LEARNINGS.md`, `TESTS.md`, `ai-docs/`, `evergreen.json`, `.github/` | Self-maintenance | **Cut** (about 0.15 MB), plus the 0.4 MB icon |

**Conflict (needs the operator):** obsidian-notes writes relative markdown links (`SKILL.md` intro: "this skill takes the opposite rule" to wikilinks). llm-wiki, `wiki_lint.py`, `wiki_search.py --backlinks`, `audit_staging.py` (regex `LINK`, line 29), and the existing `02_wiki_md/INDEX.md` all use `[[wikilinks]]`. **Recommendation: wikilinks win in `02_wiki_md`** (the vault is an Obsidian vault with `.obsidian/` at the root; four tools already depend on them). Use `vault_lint.py` read-only for its link-resolution report. If GitHub rendering of the wiki ever matters, run `--to-markdown-links` as a one-off export, not in place.
**Hooks:** none. **MCP:** none (`vault_lint.py --probe` only checks for an Obsidian CLI).
**Safety checked in the code:** a plain run is read-only (`scan` and `report`, `vault_lint.py:275-408`); only `--fix-index` (`:409`), `--to-markdown-links` (`:472`) and `--vault-init` (`:499`) write. `--to-markdown-links` rewrites files in place with no backup. `evergreen.json` (`worth.skills.obsidian-notes`) says the owner parked this skill on 2026-10-01 (no interactive use in 60 days); unpark only for the lint script.

**obsidian-sync** — repo not listed; v0.1.0, MIT (`OS/LICENSE`). 28 KB, PART read: FULL `SKILL.md` and `commands/obsidian-sync.md`, outline of `sync_to_obsidian.py`.
- Verdict: **cut all.** `commands/obsidian-sync.md` hardcodes `D:\Obsidian\obsidian-sync\…` (Windows). Default mode is "Moves files to vault, creates symlinks in project" (`SKILL.md` "Modes"), which would move raw files and break the read-only rule; flattening paths (`a/b/c/file.md` to `a-b-c/file.md`) would also break source paths. The vault is already synced by GitSync, so this has no job here.
- Hooks: none. MCP: none. Bloat: all 28 KB.

## 5. cut-weight and project-scaffolder

**cut-weight** — github.com/enoevol81/enoevol-plugins, v0.4.5, MIT (`CW/.claude-plugin/plugin.json`). 133 KB, no hooks, no MCP.
**Read:** PART `SKILL.md` (lines 1-60), heading outline of `references/quarantine-protocol.md`, first 25 lines of `scripts/inventory.py`. DESC only: the other four references.

| Part | Verdict |
|---|---|
| Recovery protocol (`references/quarantine-protocol.md`, full read): graveyard outside every Git worktree, `manifest.json` with `source, action, reason, bytes, sha256, backup, status`, copy then verify size and sha256 before removing, re-hash the source just before changing it and stop if it changed, states `planned / copied / applied / failed` | **Keep as a rule** for any corpus cleanup (dedupe, supersede, archive). It matches `promote.py`'s hash re-check (`promote.py:43`) |
| The grouped-questions conversation (`SKILL.md` §2), 60-day review trigger, tooling retention rules (`agent-artifacts.md`, `entry-points.md`), `intent-review.md`, `evidence-signals.md` | **Cut**. They are built for sanitising a code repo with a human in the loop; a corpus batch has no such conversation |
| `scripts/inventory.py` (14 KB, stdlib, writes only `--out`) | **Keep**, optional: lists Markdown residue read-only. Use `manifest.py build` for the wiki itself; this is for repos |
| The rest (`references/*`, icon, README) | **Cut** |

Fit with the vault: the pass would apply to the 82 `_N.md` duplicates `corpus-verify` already reports (`corpus-verify/SKILL.md` "Known issues"). Pages are not deleted; they get `status: superseded` and move to `_archive/` (the work order section 3 rule).

**project-scaffolder (only the Karpathy rules and `/wiki-gc`)** — github.com/valsecchi75/project-scaffolder, v3.0.4, MIT (`PS/.claude-plugin/plugin.json`). Hooks: 2, in `hooks.off-20261028/hooks.json` (PreToolUse `deny-dangerous.sh` on Bash, PostToolUse `auto-format.sh` on Edit or Write): **cut both** (not wiki work). Read in full: `deny-dangerous.sh` does not hard-block; it returns `permissionDecision: ask` (a prompt) for matches in two pattern files and always exits 0; `auto-format.sh` runs prettier/black/gofmt on code files, skips `.md`, and exits 0. Neither would stop a read, but the first adds permission prompts to every Bash call and has no off switch. No MCP.
**Read:** FULL `commands/wiki-gc.md`; grep of the rules at `skills/project-scaffolder/SKILL.md:529-534`; README lines 151-165.

- **The four rules** (`skills/project-scaffolder/SKILL.md:529-534`): Think Before Coding, Simplicity, Surgical, Goal-driven. They are the work order's own section 6 rules 1 to 4, so nothing new to add. Put them in the plugin's `rules/` once (P8).
- **Where the work order's "superseded + `_archive/`" rule comes from:** `skills/project-scaffolder/SKILL.md:541` ("History is never destroyed: `~~superseded~~` markers + `wiki/_archive/`"); the `last-verified` header rule is at `:300-302`; `/wrap` (`commands/wrap.md` step 4) flags pages over 30 days old.
- **`/wiki-gc`** (`commands/wiki-gc.md`, 24 lines): scan pages whose `last-verified` is older than 30 days, plus `~~superseded~~` sections; present a plan; wait for confirmation; append to `wiki/_archive/YYYY-MM/<file>.md`; leave a one-line stub (`> Archived {date}: see wiki/_archive/YYYY-MM/{file}#{section}`); never touch `log.md` or decisions; regenerate `index.md`. **Trim and keep**: it is the archive mechanism the contract needs. Adaptations: use `updated` instead of `last-verified` (30 days is too short for a corpus; propose 18 months, as `wiki-admin-lint` already uses); archive whole pages, not sections; write `superseded_by`; require the operator's named approval (matches `promote.py`).
- Everything else in `PS` (19 slash commands, 7 skills, 12-page project wiki, persona-lab, cortex) is **cut**. Bloat: about 0.27 MB.

## 6. What the vault actually contains (read before designing)

Facts, with the check that produced each:

| Fact | Evidence |
|---|---|
| `02_wiki_md/` has 5 sections plus `INDEX.md`: architectures 43, concepts 144, entities 18, references 1 (a `POINTER.md`), vendors 331 across anthropic, github, google, nvidia, primeintellect, qualcomm | `find … -type f \| wc -l` per folder; total 538 files incl. INDEX.md |
| `wiki_md/` holds only `POINTER.md`, which points at `novae-xorpus/wiki_md` (a path that no longer exists in this layout) | `VAULT/wiki_md/POINTER.md:1-6` |
| `MAP.md` is a 5-line stub (repo name and authority only) | `VAULT/MAP.md:1-5` |
| `02_wiki_md/INDEX.md` lists 585 `[[wikilinks]]` under "vendors/qualcomm (160 documents)" and so on, with no summaries; 585 differs from the 537 pages on disk | `INDEX.md:1-9`; file count above |
| Pages are cleaned copies, not synthesis: 519 of 537 are byte-identical (sha256) to a clean file in the root manifest | python check against `VAULT/manifest.jsonl` |
| Page frontmatter is `source / type / cleaned / cleaner` (no `id`, `sources`, `tags`, `title`); only 2 files contain a `sources:` line | `head` of two pages; `grep -l '^sources:'` |
| `VAULT/manifest.jsonl` has 585 rows: `{file, source, type, sha256, chunks, bytes}`; all 585 sha256 distinct | python check |
| That `sha256` is the hash of the **cleaned** file, not the raw source (verified true against `clean_md/<file>` and the copy in `02_wiki_md/vendors/qualcomm/`) | python check on row 2 |
| 500 of 585 `source` names match some file name under `raw/`, `raw_database/`, `01_raw_sources/` or `Drive_sync/` (name match only, no hash comparison) | python check |
| `raw_database/manifest.jsonl` is a 5-line stub; `VAULT/chunk.jsonl` has 3,135 lines | `wc -l` |
| `01-inbox/` (staging in `wiki-admin-ingest` step 5) does not exist in the vault root | `ls -d 01-inbox` error |
| `.wiki-cache` and `01-inbox` are not in `.gitignore` (66 lines) | `grep -n` on `.gitignore` returned nothing |
| `wiki_lint.py` run read-only over `02_wiki_md` (python3 -I, no flags): 538 pages, 14 orphans, 98 broken wikilinks, 29 pages over the 800-line hard cap, 30 over the 400-line soft cap, 538 "missing frontmatter" (every page, incl. `INDEX.md`, lacks `type,title,tags,created,updated`) | command output |
| Duplicate-suffix pages (`_1`, `_2`) return as separate search hits for the same content | the `hexagon NPU` search above: 3 hits, all copies of one grill session |

**Consequence:** the work order contract needs `sha256` of the **raw** bytes. The 585 existing rows can't claim that. Recommendation: treat them as `legacy`. Add `clean_sha256` to the manifest; fill `sha256` (raw) only after a backfill job resolves each page's `source:` to a raw file by hash (`check.py` already resolves `source:` this way, per `corpus-verify` "Pairing"). Do not guess hashes. Until then, legacy pages stay as they are, with no `sources:` line, and lint reports them as `legacy` rather than failing them.

## 7. Final wiki folder layout (the extra task)

Decision I need from the operator, with my recommendation:
- **Q1.** Physical wiki root: the contract writes `wiki/<section>/…` (`GC/docs/corpus-ingest.md:22`), the vault has `02_wiki_md/`. Recommendation: **keep `02_wiki_md/`** (537 pages, `INDEX.md`, and the router skill's text all use it) and write `md_path` as `02_wiki_md/<section>/<slug>.md`. The contract's `wiki/` is read as "the wiki root".
- **Q2.** `raw/<sha256>.<ext>`: the vault root has `raw/` (3 items) and `raw_database/raw`. P1/P2 own intake; I assume `VAULT/raw/` as in the contract.

```
VAULT/
  MAP.md                       router: one line per top-level folder (rewrite the 5-line stub)
  manifest.jsonl               one line per ingested file (work order section 3 schema)
  raw/<sha256>.<ext>           read-only, content-addressed
  clean_md/                    converted Markdown, one per raw file (unchanged)
  01-inbox/                    staging: new/changed pages only; outside 02_wiki_md so never searched
  02_wiki_md/                  THE WIKI
    SCHEMA.md                  conventions (section 4 + callouts); read first
    MAP.md                     folder router, As-of line
    index.md                   tiny directory of shards (under 50 lines)
    log.md                     append-only: promote.py lines + batch lines
    overview.md                one-page domain synthesis (from wonka)
    indexes/<section>.md       one line per page: [[slug]] - summary (generated)
    sources/                   one page per raw source (type: source)
    entities/                  people, tools, projects, vendors' products
    concepts/                  patterns, methods
    architectures/             existing, keep (43 pages)
    vendors/<vendor>/          existing, keep (331 pages)
    references/                existing, keep
    synthesis/                 query results the operator approved
    skills/  tools/  artifacts/   extracted-item pages (P5), pointing at the real files
    _archive/YYYY-MM/          superseded pages (never deleted)
    .wiki-cache/               search cache; add to .gitignore
  questions_pending/ questions_approved/ lint_pending/ lint_approved/   from wiki-admin-query/-lint
```
Rules: no pages outside these folders (wonka `SCHEMA.md`, "must never do"); `sources/` is new, because llm-wiki needs one page per source to hang entity and concept citations on. Existing sections stay as they are; the 537 legacy pages move only with a separate migration plan (not proposed here).

## 8. Page frontmatter schema (with `sources:` sha256)

```yaml
---
id: kebab-case-slug            # equals the filename stem; unique across the wiki
title: "Human title"
type: source | entity | concept | architecture | reference | vendor | synthesis | skill | tool | artifact
tier: 2
tags: [a, b]                   # flat; taxonomy declared in SCHEMA.md
sources: ["<64-hex sha256 of raw bytes>", "..."]   # quote each; every hash must exist in manifest.jsonl
created: 2026-10-30
updated: 2026-10-30
author: wiki-admin
status: draft | accepted | superseded    # draft until promoted
superseded_by: other-slug      # only when status: superseded
as_of: 2026-10-30              # date the facts were last checked against sources
extracted_skills: []
extracted_tools: []
aliases: []                    # optional
---
## Context & Definition
## Architectural Interfaces
## References                  # [[sources/slug]] links; the hashes above are the machine form
```
- Required by tools today: `id,type,created,updated,sources` (`audit_staging.py:19`), `type,title,tags,created,updated` (`wiki_lint.py:346`). Union above.
- `sources:` is a quoted hex list. Reason: an unquoted all-digit hash with one `e` would parse as a number in YAML 1.1. `audit_staging.py:118` strips quotes, so quoting is safe.
- Source pages hold their own sha in `sources:`; entity and concept pages hold the sha of every source they draw on.
- **Required patch (we do not edit originals; new file in P8):** `audit_staging.py:118-121` treats every `sources` item as a path and blocks promotion with "sources not found". Replace with: item must be 64 hex chars and appear as `sha256` in `manifest.jsonl`. Without this, no page can pass the gate.
- Legacy pages (no `sources:`) are tagged `status: legacy` in `wiki-pages.jsonl`, not failed.

## 9. How search is rebuilt after each batch (search starts local)

What the tools really do: `wiki_search.py` has **no persistent index by default**. It parses every page and builds BM25 on every run (`collect_pages`, line 212; the playbook says this is fine "up to a few thousand pages"). `--cache` adds an incremental parse cache keyed by page sha256 (`wiki_search.py:26`, `playbook` Threshold 4). Vectors exist only with `fastembed` + `sqlite-vec`, via `setup_wiki.py`.

**Therefore a batch needs no "rebuild" for search at this size** (measured 1.45 s over 537 pages). The per-batch sequence is about keeping the index files and the cache honest:

1. `promote.py … --approved-by <name>` for each approved page (existing; `GC/scripts/promote.py`). It appends to `log.md`.
2. `python3 -I wiki_lint.py 02_wiki_md --required-fm id,type,title,tags,created,updated --json`. Zero errors on new pages; legacy reported separately.
3. `python3 manifest.py build 02_wiki_md --out 02_wiki_md/wiki-pages.jsonl` (existing; gives title, summary, retrieval tokens per page, with full sha256). **Name the output `wiki-pages.jsonl`**, not `manifest.jsonl`, so it never collides with the ingest manifest.
4. Regenerate `indexes/<section>.md` (and the counts in `index.md`) from step 3. **Gap:** no script found that does this. Searched `extraction-index.txt` (274 entries) for index/map/readme/gen/toc/backlink/lint/frontmatter names. Hits: `.migrate/build_rag_index.py` (BM25 over `chunks.jsonl`, not wiki pages), `clean-my-ai-harness/scripts/render_harness_map.py` (harness maps only), none for wiki indexes. A new `build_indexes.py` of about 30 lines is justified (reads `wiki-pages.jsonl`, writes one line per page).
5. Check every `sources:` hash exists in the ingest `manifest.jsonl` (the patched audit does it at promotion; this re-check catches later manifest edits).
6. Local search is now current. Smoke test: `wiki_search.py "<term from a new page>" --wiki 02_wiki_md --no-embed --top 3` must return the new page.
7. When the wiki passes about 2,000 pages or a query takes over 3 s: add `--cache` (writes `02_wiki_md/.wiki-cache/search-index.json`; add `.wiki-cache/` to `.gitignore` first). Warm it once at batch end with any query.
8. Optional, later: vector search. Needs installs (`fastembed`, `sqlite-vec`) and a model download; not attempted here. Stays an operator decision.
9. Hosted (Supabase etc.) is out of scope (work order section 2); the handoff is `manifest.jsonl` plus the pages.

Two small patches for the trimmed `wiki_search.py` (it skips only `{"indexes","graph","raw",".wiki-cache",".evolution"}` and top-level `SCHEMA.md, index.md, log.md`, `wiki_search.py:219-222`; `wiki_lint.py:82-83` skips `SCHEMA.md, index.md, log.md, README.md` and `indexes, graph, raw, .evolution`, so the same two patches apply there):
- Add `_archive` to the skipped folders (otherwise superseded pages are still searched and linted).
- Add `MAP.md` and `INDEX.md` to the skipped top-level files (the vault uses upper-case `INDEX.md`, so today it is searched as a page).
- `01-inbox/` is outside `02_wiki_md`, so it is already not searched.

## 9b. Reconciliation with TOOLS.md

`GC/docs/TOOLS.md` (stage "Wiki and search"): **use first** the `wiki-admin-ingest`, `-query`, `wiki-reference-router` skills plus `manifest.py build/query`; **fallback** the `llm-wiki` plugin. So:
- Page-level lookup stays `manifest.py query <words> --manifest 02_wiki_md/wiki-pages.jsonl` (first choice).
- llm-wiki's `wiki_search.py` is the section-level step after that (`wiki-admin-query` step 2 greps sections today). Using it routinely turns the TOOLS.md fallback into a standing tool, so the operator should confirm it; it is not a silent substitution.
- llm-wiki's own ingest/query/lint workflows are not used (their "discuss with the user" step and file-back conflict with the staged gate). Only scripts and page rules are kept.
- llm-wiki source pages use `raw: "raw/<slug>.<ext>"`, `entities:`, `concepts:` and `sources: [source-slug]` (`ingest-workflow.md` Step 5, 7). Ours replaces `raw:` with the hash in `sources:`; `entities`/`concepts` stay as optional bare-slug lists.
- llm-wiki's query workflow runs `wiki_search.py --cache --json` by default (Step 2); at 537 pages we skip `--cache` (section 9, point 7).

**If the graph layer is ever enabled:** `graph-workflow.md` ("What the graph captures", edge class 3) builds `sourced_from` edges from each non-source page's `sources:` slugs and `summarizes_raw` edges from a source page's `raw:` field. Sha256 values in `sources:` would not resolve to pages. Before enabling the graph, add `raw: raw/<sha256>.<ext>` and `source_pages: [slug]` to the schema and point the extractor at those. Not needed now.

## 10. Overlaps and reuse (nothing new unless named)

| Need | Existing tool | New? |
|---|---|---|
| convert, verify, audit, promote, page index | `GC/scripts/{convert_raw_to_md,verify,audit_staging,promote,manifest}.py` | no |
| lint, search, stats | llm-wiki `wiki_lint.py`, `wiki_search.py`, `wiki_stats.py` | no |
| link audit | obsidian-notes `vault_lint.py` (read-only use) | no |
| archive / supersede | PS `/wiki-gc` logic, cut-weight protocol | one small script `archive_page.py` (about 25 lines: move, stub, `superseded_by`, manifest `status`) |
| index shards | none found | `build_indexes.py` (about 30 lines) |
| sha256 `sources` check | `audit_staging.py` | patch, not a new tool |

## 11. Not verified / limits

- See the read-status table at the top for exactly what was and was not read.
- Did not run `fastembed`, `setup_wiki.py` or the vector path (not installed; no installs allowed).
- `wiki_lint.py` and `wiki_search.py` were run read-only on the vault, once each, with `python3 -I`; no cache or output file was written to the vault.
- The "500 of 585 source names found" figure is a name match only (no hash comparison).
- obsidian-sync's repo is not listed in its plugin.json or the work order; I did not find one. obsidian-notes' repo is `github.com/m4bwav/obsidian-notes` (work order P4 table; its README install section uses the same path).
- Citations in this file are per file (`file:line`); the files named in the path prefixes at the top. Where I wrote a bare `SKILL.md:NNN` the plugin is named in the same row.
