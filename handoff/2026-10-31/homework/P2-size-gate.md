# P2 Size-gate and tool overhead (reworked 2026-10-30)

Plugin dirs under `/data/data/com.termux/files/home/.claude/plugins/synced/a5d13a90-190b-42eb-ad1b-69c924919b1b_b410cc73-6e72-411c-a9de-4edf62ec27d7/`: headroom=`b9db7a50-7c30-4727-8358-4489e83a15bc`, cco=`43b5eda8-c7e6-41dc-bfa8-8ca26fdfcb09`, cache-guard=`51df6eb1-9f1b-49d5-8bd3-98d19af7f212`, mcp2cli=`3763173a-85f1-4ac5-9206-c24385661940`. Paths below are relative to those. All four are disabled: `~/.claude/settings.json:705` headroom, `:533` cco, `:498` cache-guard, `:743` mcp2cli (all `false`).
Rework note: my first version cited wrong lines (`cat -n` over several files numbers continuously). Every citation below was re-grepped per file.

## Read status (honest)
| Plugin | Status |
|---|---|
| headroom | FULL read, every file (plugin.json, LICENSE, README, SKILL.md, peek.md, peek.py). Ran peek.py on 4 inputs. |
| mcp2cli | FULL read, all 17 text files (plugin.json, CLAUDE.md, LICENSE, README, agent, 3 commands, 3 SKILL.md, 7 references). |
| cache-guard | FULL read of everything except tests: plugin.json, icon.svg, README, SKILL.md, hooks.json, run-python.sh, session_start.py, cache_guard.py (790 lines), handoff.py (609 lines). tests/ (2013 lines, 179 test methods, 31 classes) read as class outline only; .pyc skipped. |
| claude-context-optimizer | NOT a complete full read. Full: plugin.json, marketplace.json, package.json, hooks.off-20261028/hooks.json, all 22 SKILL.md, agent, .contextignore.example, CONTRIBUTING, ROADMAP, benchmark/results.json, scripts/sync-version.js, src/overhead.js, src/tool-costs.js, src/smart-pack.js; src/read-cache.js lines 1-60 and 285-411; src/file-digest.js head; README sections (lines 44-57, 474-491, 565-582 plus greps). Import graph of all 27 src files by grep. NOT read: the other ~20 src/*.js bodies (tracker.js 44 KB, utils.js 37 KB, prompt-coach, dashboard, export, budget, ...), tests/test.js (120 KB), CHANGELOG (31 KB), docs/index.html (55 KB), .cco/patterns.digest.json, rest of README (51 KB). Reason: ~340 KB of JS is ~85k tokens; none of it sits on the path of the verdicts below except tracker/budget, which I judged by import graph and hooks.json. |

## Headline
1. Size gate: outline-first above **20 KB or 400 lines**; mandatory digest above 200 KB. Instruction in a skill, not a hook.
2. headroom: keep `peek.py` (3 KB) and a 15-line SKILL. Three gaps to patch (below).
3. honey-ccr is a different tool from headroom: use it for uniform JSON arrays, headroom for documents/logs/CSV.
4. cco: keep 2 skills (cco-overhead, cco-pack), cut all hooks. cco-tools is cut because it only learns from a hook.
5. `read-cache.js` is off (evidence below). cache-guard: cut its hook. mcp2cli: cut.

## headroom 1.3.2
Source: github.com/petrovicistefan/claude-code-plugins (`.claude-plugin/plugin.json:26`), MIT (`plugin.json:11`, `LICENSE:1`), version `plugin.json:3`. 137K total; `icon.png` 79K is the bloat.
Parts:
- `skills/headroom/SKILL.md`: measure (line 12), read by range (line 20), keep a digest (line 27). KEEP.
- `skills/headroom/scripts/peek.py` (stdlib only): size, lines, outline. KEEP.
- `commands/peek.md`: TRIM (wiki-admin calls the script).
- Hooks: none. MCP: none.
Gaps found by reading and running peek.py:
1. `.txt`/`.md` outline is headings only (`peek.py:19-23`, dispatch `:87-88`). A heading-less transcript printed `Outline (line: heading):` and nothing (tested). Transcripts are the bulk of the corpus: add evenly spaced line previews.
2. `.jsonl` and unknown extensions fall through to `logs()` (`peek.py:93-94`): tested, 300 JSONL rows printed as one pattern `{"id": N, "k": "v"}`, no key structure.
3. JSON is `json.load` whole (`peek.py:50`); the only guard is 200 MB (`:47`). Lower to ~50 MB on this phone. Also for a JSON array it prints only the schema of element `[0]` (tested on 501 rows): it does not show the one `ERROR` row.
Trimmed SKILL (draft):
```
---
name: size-gate
description: "Use before reading any converted file over 20 KB or 400 lines."
---
1. python3 peek.py <file>   (size, lines, outline with line numbers)
2. Read only outline ranges (Read offset/limit) or grep -n. JSON/JSONL arrays >= 20 rows: eson crush < file first. CSV: count/filter by script.
3. Write notes/<sha256>.digest.md: facts + line ranges. Re-read the digest, not the source.
```

## Compared with honey-ccr (loaded with the Skill tool), honey-px, chunk.py
| | headroom peek.py | honey-ccr (`eson crush`) | honey-px | tools/chunk.py |
|---|---|---|---|---|
| Does | outline + line numbers | keeps endpoints/anomalies of a uniform JSON array, caches the rest by hash | renders text as PNG pages | 2048-char chunks + sha256 manifest |
| Lossless | yes (it only points) | no, but `eson retrieve <hash>` restores verbatim | no (silent misreads) | yes |
| Input | md/txt/json/csv/log | uniform JSON array, >=5 items (`SKILL.md:25`), auto-hook >=20 items and >=2k chars (`:51`) | dense read-only bulk >~6k chars (`SKILL.md:30`) | clean_md files |
| Limit | headings only; first element only for JSON | "non-array data" not for it (`SKILL.md:31`) | Fable-class readers only (`:32`); never for editing (`:37`) | broken, see below |
Test (scratchpad, 501-row JSON array, 22,434 bytes, 500 INFO rows + 1 ERROR row):
- `peek.py`: printed `[0] of 501: dict` plus the three keys. No sign of the ERROR row.
- `eson crush < a.json`: 633 bytes out; the output tail contained `{"id":500,"lvl":"ERROR","msg":"boom"}` and `{"_ccr":"<<ccr:dd22066b9cc4c381 486_rows_offloaded>>"}`.
Conclusion: as a size-gate for **huge uniform JSON/list output**, honey-ccr wins (anomaly kept, recoverable). For documents, transcripts, logs and CSV it does nothing; headroom wins. Wiki-admin needs both: route by type. px stays out (wiki pages carry exact strings, `honey-px SKILL.md:8-9`).
chunk.py is not a reader. It is also broken today: `chunk.py:17-22` requires a `Repo*` folder and raises; I ran it: `FileNotFoundError: Repos dir not found` (no `*Repo*` folder in the vault). Chunk size `chunk.py:27-28` (2048 / 200 overlap) is useful as the fan-out slice for P3. Reuse; do not write a new chunker. extraction-index.txt lists `.migrate/build_rag_chunks.py` too (not read).

## Size threshold (judgment, anchored to cco's own numbers)
- cco defaults: soft hint at 200 lines, warning at 500 (`skills/cco-config/SKILL.md:65-66`, keys `mediumFileLines`, `bigFileLines`), and `read-cache.js:326-327` blocks the first full read of a file over 1500 lines (`bigFileThreshold` default).
- Proposal for wiki-admin: **> 20 KB or > 400 lines**: run `peek.py`, then ranged reads. **> 200 KB**: also write a digest and hand 2 KB chunks to workers. JSON/JSONL arrays >= 20 rows or >= 2 KB: `eson crush` first. JSON > 50 MB: `jq`, never `peek.py`.
- Rule 8 (no hook may block Read): the gate is a skill instruction. cco's `read-cache.js` is the opposite design and is cut.

## claude-context-optimizer 4.12.1
Source: github.com/egorfedorov/claude-context-optimizer (`plugin.json:8`), MIT (`plugin.json:9`), version `plugin.json:3`. 2.1M; media ~1.0M in assets/*.png, docs/index.html 55K, tests/test.js 120K, CHANGELOG 31K, README 51K.
Parts: 22 skills, 1 agent (`agents/context-analyzer.md`), 27 `src/*.js`, 1 hooks file, no MCP.
Skill verdicts (all 22 SKILL.md read):
- **KEEP cco-overhead** (`SKILL.md:3`). Baseline mode needs no hook: it reads the first assistant usage record of transcripts under `~/.claude/projects` (`src/overhead.js:94-101`, `:161-165`). Its MCP mode needs tracker data (`overhead.js:254`) and says "not observed, not a verdict" below 5 sessions (`:298-301`, `:324-326`): degraded, still useful for the baseline.
- **KEEP cco-pack** (`SKILL.md:3`, `src/smart-pack.js`). Hook-free parts: prompt-mentioned paths, `git status`, git keyword match (`smart-pack.js:48-52`, `:55-74`, `:115-129`); the "historically useful" part reads tracker output (`:131-154`, `PATTERNS_FILE`). Requires a git repo (`:44-46`); source-code oriented; weaker than peek.py for markdown. Rank 2.
- **CUT cco-tools**: the learned table is filled only by the PostToolUse path (`tool-costs.js` `recordToolCost`, imported by `budget.js:28`), so with hooks off it is empty. Would need a kept PostToolUse tracker hook; not worth it.
- CUT the rest: cco, -anatomy, -budget, -claudemd (CLAUDE.md analyzer), -clean, -coach (ru/en prompt coach), -config, -digest, -doctor, -export, -git, -patterns, -replay, -report, -roi, -shield, -task (overlaps handoff), -templates, smart-loader. Reason: dashboards and cost reports over tracker data, or CLAUDE.md work; none serves ingest.
- Agent `context-analyzer.md`: CUT (reads tracker data).
Scripts needed for the 2 kept skills: `src/overhead.js`, `src/transcript-usage.js`, `src/smart-pack.js`, `src/file-digest.js`, `src/utils.js` (all import it); Node >= 18 (`skills/cco-doctor/SKILL.md:36`); no npm deps (`CONTRIBUTING.md:14`). `utils.js` not read; transitive imports of `config.js` unverified.
Hooks (`hooks.off-20261028/hooks.json`; it has 6 events, 7 matcher groups):
| Event | Line | Runs | Can block? |
|---|---|---|---|
| PreToolUse Read | 3, 9 | read-cache.js | YES: `{decision:'block'}` at `read-cache.js:304,351,408` |
| PreToolUse Read | 13 | context-shield.js | no `block` output found by grep of the file; README says it warns (`README.md:571`) |
| UserPromptSubmit | 18, 23 | prompt-coach.js | not checked |
| PostToolUse Edit/Write | 28, 34 | read-cache.js | not checked |
| PostToolUse Bash/Read/.../mcp__ | 43 | tracker.js + budget.js | not checked |
| PreCompact | 48, 53, 57 | read-cache.js, tracker.js | not checked |
| SessionStart | 62, 67 | tracker.js, tasks.js rehydrate | not checked |
| SessionEnd | 72, 77 | tracker.js, dashboard.js | not checked |
Proposed merged version: none. Zero cco hooks enter hooks.json (rule 8; and the 2 kept skills do not need them).
Conflicts: cco read dedup duplicates honey Lever 3b "do not re-read"; honey wins (no hook). cco-overhead has no honey twin.

### read-cache.js is OFF
- No `hooks/` directory exists in the plugin (`ls hooks` failed); the only hooks file is `hooks.off-20261028/hooks.json`, which wires read-cache.js at `:9`, `:34`, `:53`. `.claude-plugin/plugin.json` has no `hooks` key (grep for "hooks" there matched nothing).
- Plugin disabled: `~/.claude/settings.json:533` `"claude-context-optimizer@synced": false`.
- Caveat: "off" means renamed file plus disabled plugin. I did not launch a session to observe it. Renaming the folder back or enabling the plugin re-arms it. Note it blocks on the first full read of a file over 1500 lines (`read-cache.js:323-353`), so it would have fought the owner's reads.

## cache-guard 1.0.2
Source: github.com/Agulhas-Labs/claude-plugins (`plugin.json:10`), Apache-2.0 (`plugin.json:15`), version `plugin.json:4`. 312K: tests 98K, .pyc 76K are bloat.
Parts: `hooks.off-20261028/hooks.json` (UserPromptSubmit `:3`, SessionStart `:13`), `cache_guard.py`, `session_start.py`, `handoff.py`, `run-python.sh`, `skills/handoff/SKILL.md`. No MCP.
What it does: holds back a prompt once when the cache has expired in a context over 100k tokens (`README.md:12`, `:26`; `cache_guard.py:779` outputs `decision: block`), or after a model/effort change; sending again within 120 s passes. The word `handoff` is intercepted and writes `.claude/handoffs/<ts>.md` by script (`handoff.py:404-409`) and starts a detached background `claude -p` run with no tools (`handoff.py:438-454`, `:457-478`). Fail-open on any error (`cache_guard.py:27-28`, `:762-763`).
Verdicts: CUT the UserPromptSubmit and SessionStart hooks (it blocks the owner's message: rule 8; subagent batch runs have no idle gaps; the owner types in a terminal and the vault wrapup skills already do handoffs). CUT handoff.py and session_start.py. `skills/handoff/SKILL.md` (model-written handoff): CUT, duplicates the `wrapup`/`happy-ending` skills.
Switch-off: `CACHE_GUARD_DISABLE=1` (`cache_guard.py:25,593,703`; `README.md:114`) is read from the process environment, which settings `env` sets (`README.md:99-100`). By inference it takes effect on the next session, not mid-session; not tested. So it fails rule 8's "switchable mid-session".
Hook proposal for the merge: none.

## mcp2cli 0.1.0
Source: github.com/myeolinmalchi/mcp2cli (`plugin.json:17`), MIT (`plugin.json:16`), version `plugin.json:3`. 126K, no media, no hooks, no scripts, no MCP server.
Parts: skills mcp-analyze (+`pattern-classification.md`), mcp-codegen (+5 references: cli-scaffold, porting-cheatsheet, tier-1, tier-2, tier-3), skill-author (+`skill-template.md`); commands `/convert`, `/analyze-mcp`, `/generate-skill`; agent `mcp-analyzer`. All prompt text; output is a TypeScript CLI (`cli-scaffold.md` stack: commander, fetch, tsup).
Claim `README.md:22` "94-96% token savings" is the author's table (`README.md:26-28`), not measured by me.
Verdicts: CUT the plugin from the compiled build. It converts an MCP server's source into a TS CLI; wiki-admin runs engines (P7) and does not convert them. Keep as an out-of-band tool for one case: a self-hosted MCP whose tool schemas weigh heavily (`README.md:11`). `skill-author` overlaps skill-creator (P5); skill-creator wins. Its own tier guide says Memory/Browser servers are poor fits (`pattern-classification.md:31`, `:29`), which is most of our P7 list.

## Not verified
cco: bodies of ~20 src files, utils.js, tests/test.js, CHANGELOG, docs, patterns digest, whether cco-pack/cco-overhead run on this phone (Node present? not run), blocking behaviour of every cco hook except read-cache/context-shield. cache-guard tests/. extraction-index `build_rag_chunks.py`.
