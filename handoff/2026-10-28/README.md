# Handoff 2026-10-28 (phone, session 5fc2c8e1)

Everything built today, where it is, and what is left. Readable from any device once the
branches below are pushed. Earlier sessions today: `earlier-sessions.md` (this folder).
Phone-only working files are archived in the private repo `NvAEx-Recaps`,
`recaps/session-work/2026-10-28/`.

## Repo map (operator, 2026-10-28)
NovAExorpus = vault. NovusAExenti = agent configs, logic, pre-compiled agent packages.
NovAExopia = claw tools, skills, assets, MCP connectors, mods (permanently). Aesop-Xi =
orchestration, routing, hooks, enforcements. CloviX-AEyre = everything voice and vision.
AEthX-AEsc = on-device terminal APK. Hyperion-XI = UI app with its own Chromium.
NvAEx-Recaps = private recaps, secrets, shared memory, archived session-work.

## Built today (branch, commits)
| What | Repo, branch | Commits | Tested |
|---|---|---|---|
| Intake prompt-engineering step (pipeline stage 0): STT repair with a glossary, asks split for fan-out, one brief per ask with route, memory layers and tier hints, YAML handoff | Aesop-Xi `intake-skill` (`skills/intake/`, `docs/intake-pipeline-spec.md`) | b181eea, 1db4258, e511c4a | Structure only; never run on a live prompt |
| Web view tool: drives the phone's Chrome through Chrome DevTools over adb loopback; Gemini web-session and page-to-markdown recipes | NovAExopia `webview-and-mods` (`mcp_connectors/webview/`) | 015a6d2, 26df99b, e94ee5c | Syntax, JSON, connect script exits 3 with no device. Not driven Chrome yet |
| Mods spec (operator's `cc.do.now.txt` and `SPEC.md`) | NovAExopia `webview-and-mods` (`mods/`) | 015a6d2 | n/a |
| Wiki admin tools and skills: converter, independent verify, manifest, Gemini adapter (privacy filter, dry-run, MCP), audit, promote; reference router, W5H, merged ingest/query/lint/repo-docs skills | NovAExopia `wiki-admin-tools` (`tools/wiki-admin/`, `skills/wiki-admin-core/`) | ca13dff, 22d04db | selftest PASS on sample files; Gemini dry-run only |
| Wiki admin agent: the existing `executor-core/file-administrator/` package extended, binding GLM-5.2 -> Gemini | NovusAExenti `wiki-admin` | c295362, f26516a | Not run in a wiki-admin session yet |
| Shared memory (memory-as-skill) and archived session-work | NvAEx-Recaps `memory-as-skill` (`memory/`, `recaps/session-work/2026-10-28/`) | abaef50, 69fce0f, 872d043 | n/a |
| 24 forks synced and cloned (REA, Chrome DevTools MCP, Google ADK/MCP set, skills repos); Playwright, playwright-mcp and Stagehand newly forked | `~/repos` (phone) | n/a | n/a |

## Decisions (operator's words, 2026-10-28)
- Wiki admin stack: "dropping open Wiki tui and instead using open Wiki for Claude and also open Wiki no code in conjunction with obsidian Wiki and attaching the open Wiki skills if there's any overlap ... customize customize customize". Inference on Gemini/Google. Wiki admin is separate from a "Gemini driver".
- STT: Qwen ASR through OpenRouter now (`qwen/qwen3-asr-1.7b`); QAI Hub Whisper-Large-V3-Turbo on device later. All voice/vision in CloviX-AEyre.
- Hooks: "all the fucking hooks disabled until you can actually engineer them right". Done: every Claude Code hook is an exit-0 stub (originals `~/.claude/hooks/<name>.disabled-20261028`); the Stop AUDITOR agent and the task-observer SessionStart entry were removed from `~/.claude/settings.json` (backup `settings.json.bak-20261028-hooksoff`). Only the gitleaks git hooks still run.
- Memory: cross-project memory lives in `NvAEx-Recaps/memory/`; every agent reads `general.md` plus one active project file (pointer in `~/.agents/AGENTS.md`).

## Sources read this session
Vault RESUME.md, NAMING-CANON.md, `handoff/2026-10-24/extracts/wiki-admin-extract.md` lines 1-209, `docs/WIKI-ADMIN-GUIDE.md` (top), Recaps RESUME.md, Aesop-Xi RESUME.md, NovAExopia and NovusAExenti RESUME.md, `~/.claude/hooks/README.md`, `~/.claude/WRAP-UP.md`, `cc.do.now.txt` (Drive), prompt-enhancer plugin, memory-as-skill SKILL.md. Subagents read: Drive `_02.wiki-admn-docs` (33 files), part of `_2#rev.eng.ify_plan-docs`, the full wiki-admin extract, earlier session transcripts.
Not read: the operator's full 140-200 file wiki-admin set (location not confirmed), the Dynamic_workflow_guide and `_config` docs, PENDING.md "Open" in full, `handoff/2026-10-24/README.md` deliverables beyond item 2.
