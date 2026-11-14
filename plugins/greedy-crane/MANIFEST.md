# greedy-crane manifest (consolidation of the wiki admin, 2026-11-03)

Everything below was COPIED; no source was moved or deleted. Pre-existing greedy-crane files
(agents/, skills/*/SKILL.md, scripts/*, docs/TOOLS.md, docs/corpus-ingest.md, docs/skills.md,
docs/wiki-admin.md, .claude-plugin/plugin.json) were left untouched.

## Added
| Path here | Source | Why |
|---|---|---|
| bin/wiki-admin | `~/bin/wiki-admin` | Launcher. Same behavior (cd ~/wiki-admin, attach the 7 repos via nvaex-repos.sh) plus `--plugin-dir` pointing at this folder (override: `WIKI_ADMIN_PLUGIN_DIR`). The original in ~/bin is unchanged. |
| .claude/settings.json | new | `enabledPlugins: obsidian-wiki@synced` so it loads when Claude starts in this folder. |
| package/file-administrator/{AGENT.md,STATUS.md,manifest.json,wiki-admin.claude-agent.md} | NovusAExenti worktree `~/repos/.wt/NovusAExenti-wiki-admin` (branch wiki-admin), `executor-core/file-administrator/` | The agent package. |
| docs/status/NovusAExenti-file-administrator-STATUS.md | same STATUS.md | Status snapshot (2026-10-28). |
| docs/status/NovAExopia-tools-STATUS.md | NovAExopia worktree (branch wiki-admin-tools) `tools/wiki-admin/STATUS.md` | What was tested vs not. |
| skills/README.md | NovAExopia `skills/wiki-admin-core/README.md` | Skill index (paths in it predate this layout). |
| skills/notebooklm/SKILL.md | `~/wiki-admin/.claude/skills/notebooklm/SKILL.md` (a symlink to `~/repos/notebooklm-py/SKILL.md`; content copied) | Workspace skill. |
| commands/llmwiki-{ingest,lint,query}.md | `~/wiki-admin/.claude/commands/` | The /llmwiki-* commands of the workspace. |
| scripts/wiki_admin.py | `~/wiki-admin/tools/wiki_admin.py` | Manifest builder (path, sha256, size, summary); different from scripts/manifest.py. |
| docs/WIKI-ADMIN-GUIDE.md | vault main `docs/WIKI-ADMIN-GUIDE.md` (read only) | Toolset guide. |
| docs/spec/wiki-admin-extract.md | vault main `handoff/2026-10-24/extracts/wiki-admin-extract.md` (read only) | Prior full spec extract (98 KB). |
| docs/workspace/{AGENTS.md,GRILL-INPUTS.md,MEMORY.md} | `~/wiki-admin/` (GRILL-INPUTS.md as on disk, with its 1 uncommitted line) | The workspace's draft agent spec, grill inputs, memory. |
| docs/homework/* | `~/.claude/session-work/2026-10-29/wiki-admin-homework/` (P1-P7 deliverables, P*-paths, progress-P*, BRIEF, work-order, extraction-index) | Homework results. |
| hooks/drafts/P6-hooks.json.draft, P6-guards.draft.py, P6-quarantine.draft.py, P6-wa-hook.draft.sh, README.md | same homework folder | DRAFTS only. Not registered: no hooks/hooks.json, no `hooks` key in plugin.json. hooks.json renamed to `.draft` so it can't auto-load. |

## Compared, identical (nothing to add)
- skills/{w5h-extraction,wiki-admin-ingest,wiki-admin-lint,wiki-admin-query,wiki-admin-repo-docs,wiki-reference-router}/SKILL.md: byte-identical to NovAExopia `skills/wiki-admin-core/*` (and the ~/wiki-admin/.claude/skills symlinks resolve there).
- scripts/{audit_staging,convert_raw_to_md,gemini_infer,manifest,promote,verify}.py, selftest.sh, README.md: byte-identical to NovAExopia `tools/wiki-admin/*`.

## Conflicts
- agents/wiki-admin.md (greedy-crane) vs NovusAExenti `wiki-admin.claude-agent.md`: differ. greedy-crane's is newer in content (adds skills list, Agent tool, corpus-ingest dispatch, plugin-folder script paths, "direct, not necessarily run on Gemini"). Kept greedy-crane's. The NovusAExenti one is kept as package/file-administrator/wiki-admin.claude-agent.md (older; points at the NovAExopia tools path).
- package/file-administrator/AGENT.md still says Model GLM-5.2 / Delta in its table while manifest.json says Gemini (that was the state at the source; not edited).

## Skipped
- `~/wiki-admin/.claude/skills/convert-documents-to-markdown` (symlink to repo aesop-anydoc): lives in its own repo.
- `~/wiki-admin/.claude/settings.json` / settings.local.json (enabledPlugins for obsidian-wiki@obsidian-wiki, openwiki, llm-wiki-compiler; outputStyle): workspace config, not plugin content; replaced by the new .claude/settings.json requested.
- `~/wiki-admin/{wiki/,raw/,lint_*,questions_*}`: empty stubs of the nocode add-on; `.git`.
- NovAExopia `tools/wiki-admin/__pycache__/*.pyc`: caches.
- `~/wiki-admin/.claude/agents/wiki-admin.md`: symlink to the NovusAExenti file already copied.
- `~/repos/NvAEx-Recaps/memory/active/wiki-admin.md`: read for context only; private repo, not copied.
- progress-P* and other homework files were copied as is (no PDFs/large binaries existed).

## Compiled-in skills from forks
- `skills/gemini-api-cli`, `gemini-api-dev`, `gemini-live-api-dev`, `gemini-omni-flash-api`: copied whole from fork `c10vis-poem/NxAEx-gemini-skills` at `7cfc690ba9c8` (synced with `google-gemini/gemini-skills` 2.4.0), Apache-2.0 (`vendor/LICENSE.gemini-skills`). Update: sync the fork, then re-copy and record the new commit here (`rea-sync` / `rea-customize` for any local change).

- 2026-11-08: greedy-crane hooks are also wired in root `~/.claude/settings.json` (via `~/.claude/hooks/greedy-crane-gate.sh`); the plugin copy steps aside.
