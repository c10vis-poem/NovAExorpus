# PENDING.md — NovAExorpus

Durable cross-session backlog. Not rewritten each session — items persist until resolved or explicitly dropped.

## Routines
last-housekeeping: 2026-10-23
- Roll _recaps/ older than 30 days into a monthly summary, delete the originals
- Audit repos: uncommitted / unpushed / stray branches → merge or discard with the builder
- Review the task-observer observation log
- Check cloud billing (VM disks)
- Builder reminders: (add here)


## Open
Moved here at the 2026-10-23 wrap-up (everything not finished). Long-term threads stay in [[BOARD-INTAKE]]; reports in `handoff/2026-10-23/`.

**Operator to run / decide**
- Secrets (plain Termux tab, one at a time): `nvaex-secret set OPENROUTER_API_KEY` (old key lost with ~/.openwiki; make a new one at openrouter.ai/settings/keys), `HF_TOKEN`, `QAI_HUB_API_TOKEN`, `TYPESAFE_API_KEY`; then commit + push `NvAEx-Recaps` (branch, PR, auto-merge).
- Deletes (operator): `~/storage/shared/Documents/_models/models-npu/qwen3_vl_4b_…_8_elite` (458 MB partial), `~/downloads` DeepChat / SocketSweep / llama-macos tarballs (keep or delete `Claude Setup.exe`: undecided), `~/repos/happy-ending/.agents/skills/happy-ending.bak-preSymlink` (older subset of the live skill). Drive: Qwen3-VL zip.
- Starter principles: pick numbers to import from `handoff/2026-10-23/principles-match.md` (2 full matches, 6 partial, 21 none).
- Hook 3 (list newest sessions across all `~/.claude/projects/*` at start; obs 0012): build or drop.
- Small calls: task-observer upstream draft (send or drop); 4 missing tool references (`htp_partition_calc.py` etc.); OmniGlyph (switch on or drop); pick one auto-capture memory (MemVault / claude-mem / agentmemory / pmm); Gemma 4 E4B LiteRT (`litert-community/gemma-4-E4B-it-litert-lm`, no QAT/NPU file listed): download or not.
- Answers owed: "babbly" STT name; graphify NotebookLM plugin link; tablet age public key; `~/.credential-quarantine-2026-08-17/` delete or keep; import `~/.hermes/.env` keys or not; what `NvAExinandroid` is for.
- Infrastructure: retire the VM, second age key, NotebookLM login on the tablet (steps in BOARD-INTAKE infrastructure thread).
- Leave alone: `Horizon-s-home-grid` PR #1 (operator 2026-10-23).

**Agent work (next session)**
- NPU: read the proof-run summary in `~/.claude/session-work/2026-10-23/npu-proof-*.log` (script `~/tools/npu-proof.sh`, started 13:00, still running at wrap-up); then the plan's steps 8-16: Qwen3.5 2B/4B A/B, InternVL bundles vs Qwen3.5-4B vision bench, Distil-Whisper QNN vs TFLite vs ONNX (`_models/stt/distil_whisper/`, Moonshine control), K-quant placement on v0.9.3. The six smaller NPU-ON-DEVICE.md corrections need the operator's OK each (`handoff/2026-10-23/npu-install-plan.md` §5).
- Jev: review fork `c10vis-poem/NvAEx-Jev.skills` (what it sends to TypeSafe, which key) before any install; REA fork `NvAEx-rea` likewise.
- Observations open: 0038 (value review before delete offers), 0039 (never bundle a turn-off), 0040 (subagent scope clause), 0041 (encode delete ordering in the command). Each proposes a rule or check; build in Aesop-Xi.

## Closed 2026-10-23
- End of session 2026-10-23: hooks #67/#69/#71 installed; auditor #72 installed + fixed (#74, #75: 8-line transcript pages); AGENTS.md/CLAUDE.md split installed (MISSING: 0); absence-gate #76 and state-guard/settings-guard/build-doc-gate/agent-type-gate/delegation-tripwire #77 installed live (settings-guard verified blocking); crg #2 merged; 23 bot branches archived as `archive/*` tags then deleted; 3 salvage files in `recovered/2026-10-23/`; 11 workflows wrongly disabled then re-enabled (0 disabled, verified); Qwen3.5-4B + mmproj downloaded (sha OK); GenieX v0.9.3 downloaded (sha OK), unpacked, skel link; NPU-ON-DEVICE.md line 8 replaced; 16 cross-cutting principles written; Download duplicates (13.6 GB) and ~/openwiki deleted; forks synced (ai-hub-models, GenieX, generative-ai); Qwen3-VL removed from docs (#73). Dropped for good: OpenWiki, Terrestrial Brain, mem0, OmniRoute, Qwen3-VL, `_agents.md` installer hunt.
- PRs merged: Aesop-Xi #66 (git-gate test), #67 (check-in list labels, obs 0037), #68 (Kokoro lexicon + WAV writer, tested 2.7 s), #69 (staged skill updates surfaced, stop-gate), #70 (aesopd auth/frame cap/localhost, llamad -fa on); ECC #7; TB #7. code-review-graph fork #2 (skip ignored paths before stat) auto-merging.
- Later 2026-10-23: Aesop-Xi #71 (H7 mention vs command, item 23) merged; ai-hub-apps #4 (v0.39.1 + GenieX Chat workflow, item 5, no force-push) merged; forks created (MemVault, claude-mem, agentmemory, oak-memory-plugin, pmm-plugin) and synced (notebooklm-py, headroom, context7 x2) (items 9, 24); AGENTS.md split redrafted (item 20, `agents-md-v2/`); secrets inventory + import script (`secrets-report.md`); models located (`models-report.md`, item 41); voice research (item 17); remote access (item 9); Anthropic auditor/advisor/model research (items 12, 18, 19, 38).
- android-termux-operator staged update installed (obs 0004, 0025, 0009; redaction sed fixed for JSON).
- Reviews done: 6 remote commits (`session-work/2026-10-23/remote-commits-review.md`), NPU audit, vault PDFs/duplicates, ai-hub-apps fork (one deliberate customization: build-geniex-chat.yml), branch audit (161 repos).
- Dropped: Render MCP (21); NvAEx-agentk org (10); Tailscale install (8, installed on phone and tablet); dsh until Acode + Jetson (34); mem0/TB re-test superseded by strip-and-judge (18); six-repo sync superseded by pointers (32); ECC unified-memory and ECC fork upkeep (31); CLAUDE.md success-tracking (33, moved to board).
- Operator-only setup instructions given in session (6 VM retire, 7 second age key, 9 notebooklm login); tracked in [[BOARD-INTAKE]] infrastructure thread.

## Closed 2026-10-22
- test-ship-v2 fails 14/18: done (18 passed, 0 failed; Aesop-Xi #50, #55)
- H8 required check vs job names: done (Aesop-Xi #52)
- Enable Actions on honey fork: done (actions enabled; honey #3, #6 merged)
- Repo renames (Aesop-Xi, NovusAExenti, AEsc, AEyre): done (Aesop-Xi #49/#60; repo list)
- Delete NovA-Corpus: done (not in repo list)
- Delete 44 old branches / operator branches: done (30 operator branches cleaned 2026-10-22; Aesop-Xi 10 branches)
- repos/ mirrors replace MASTER-*; recaps into NvAEx-Recaps: done (Aesop-Xi #50, #51; Recaps #1, #2)
- MASTER-SKILLS concat vs index (#11): stale (MASTER-* replaced by mirrors)
- Hooks not registered (sync-forks/ship-session): done (settings.json SessionEnd/PreToolUse/SessionStart entries)
- Session-end discipline unenforced: done (stop-gate.sh, SubagentStop gate Aesop-Xi #59, H9 Aesop-Xi #53 merged)
- Other six repos CLAUDE.md to AGENTS.md: done
- Fold `*unresolved*` files: done 2026-10-09
- Disk bloat 22 GB / gemma dup ggufs: done (uv cache 30K, npm 78M, one gguf each)
- OpenWiki upstream PR (#5): stale (OpenWiki retired 2026-10-02)
- ECC dashboard via SSH tunnel (#13): stale (ECC parked)
- Rename repo to NovAEcorpus: stale (conflicts with naming canon, no such repo)
- Obsidian Git plugin: stale (superseded by GitSync)
- Parked skill-observation review resume / "Task-observer review outstanding": stale (review completed 2026-10-08; remaining parked files in Open)
- sherpa-onnx 8 upstream cron workflows: done (149 fork Actions disabled)
- Aesop-Xi clone uncommitted bootstrap.sh/aesop-tmux.sh: done (clean, main...origin/main)
- ECC-aesop 18 unpushed commits: stale (now 1 ahead, 415 behind; decision in Open)
- code-review-graph MCP proot venv (#16): stale (MCP tools live)
- GitSync stuck loop; GitSync DNS retry; OpenWiki replacement; nested mirror; CLAUDE.md-to-AGENTS: done/stale (resolved 2026-09-30 to 2026-10-05)
- Open PRs Aesop-Xi #53 #54 #61 #62, honey #3 #6, Hyperion-XI #4, NvAEx-OmniRoute #1: done (merged 2026-10-22)
- rclone Drive migration / gdrive remote: done (remote deleted 2026-10-22; Drive-only script in Open)
- Done 2026-09-30 section (PR #21, PR #7, branches to main, GitSync main, AGENTS.md corrections): done (history)
- Missing tools boot.sh, smart-grep-hook.sh: done (exist)

- pm-claude-skills fork: done/moot (fork 5 ahead = own weekly-digest ledger commits, 293 behind upstream; no PR to make)
- trusted-firmware-a fork: moot (3 ahead qti commits, 1181 behind qcom-next; no c10vis PRs; sync only if you build it)
- Node 22+ for OmniRoute: done (node v26.4.0; engines `>=22.22.2 <23 || >=24 <27`)
- TB Obsidian-plugin `tsc: not found`: done (`node_modules/.bin/tsc --noEmit` rc=0 in NovA-terrestrial-brain/obsidian-plugin)
- happy-ending plugin hand-registration: done (in installed_plugins.json, enabled, cache present, skill loads in session)
- vault-ci.yml: stale (vault has `.github/workflows/ci.yml` + `security.yml`)
- Obsidian skills load twice: moot for Claude Code (`~/.claude/skills` holds only `obsidian-vault`, distinct from the plugin's defuddle/json-canvas/knap/obsidian-*; the duplicate links are in `~/.agents/skills`, not read by Claude Code)
## 2026-10-28 (sessions 5fc2c8e1 and earlier; details in handoff/2026-10-28/)
**Operator to run / decide**
- Secrets: `nvaex-secret set GEMINI_API_KEY` (wiki admin) and `nvaex-secret set OPENROUTER_API_KEY` (STT).
- Pair wireless debugging for the web view tool; run the two classifier-blocked builds (`node scripts/post-build.ts` in `~/repos/NvAEx-chrome-devtools-mcp`; `npm ci && npm run build` in `~/repos/NovA-openrouter-mcp`) or add a permission rule.
- Wiki admin: where the 140-200 file set lives; decide E6 (chunk schema) and E10 (frontmatter schema).
- Hooks: which to re-engineer first; whether the gitleaks git hook stays on. A keyword or setting to switch gates off (Claude Code's built-in `disableAllHooks` setting was mentioned in session 6a9c6cdb, never recorded).
- Task-observer model pin (session 5da28487): `model: claude-sonnet-5` sits in `~/repos/aesop-task-observer/SKILL.md` and the vault's `.claude/skills/task-observer/SKILL.md`; fork branch `task-observer-sonnet` (de9c313, c58839f) is not pushed, no PR, never confirmed. Keep or drop.
- Mem0 and code-review-graph are still in `~/.claude.json` though the operator asked to remove or disable them; the removal command was given and not run.

**Work**
- Plugin-injection switch-off (session 5da28487) is half applied: `disable-injections-2.sh` did not run; settings.json still has 477 `@synced` keys.
- plugin-fork-sync rule: sync only the operator's own forks the session touches, never Anthropic-marketplace plugins.
- Repo-wide rule: in each repo, CLAUDE.md becomes a pointer to AGENTS.md (Aesop-Xi hook rules move to AGENTS.md); RESUME only covered `~/CLAUDE.md`.
- Re-engineer hooks before re-enabling (resume-gate first, observation 0051).
- Wiki admin: harvest the skills and scripts in the operator's wiki-admin file set; Gemini live run; profile YAML, housekeeper, chunker, semantic lint not built.
- Web view tool: headless / own-Chromium mode for Hyperion-XI and AEthX-AEsc; search tool; marketplace entry.
- STT: build OpenRouter MCP, default `qwen/qwen3-asr-1.7b`; later QAI Hub Whisper-Large-V3-Turbo on device. Lives in CloviX-AEyre.
- Mods (spec `NovAExopia/mods/`): none built except the old plugins-panel.
- Intake: install and live-run; build pipeline stages 1-4.
