# RESUME.md — Session Ledger
Repository: NovAExorpus
Last session: 2026-09-18

## WHAT LANDED THIS SESSION

- **Router-guard output style** rewritten from 93-line skeleton to 148-line
  full spec matching `~/storage/shared/Documents/9-18-26/output-style.md`.
  6-layer mandatory pipeline, OmniRoute fallback, multi-write protocol,
  secondary tools, Continual Harness anchors, enforcement rules.
- **Pipeline constraints added to AGENTS.md** — model-agnostic version of
  the full pipeline (layer table, multi-write protocol, secondary tools,
  enforcement). Works for Codex, dsh, Prime Agent, any engine.
- **OmniRoute added to `.mcp.json`** — was missing entirely. Now first
  entry with env vars `OMNIROUTE_MCP_URL` / `OMNIROUTE_API_KEY`.
- **CLAUDE.md cleaned** — removed stale `localhost:20128` reference,
  stripped duplicated memory infrastructure section, now points to
  AGENTS.md as canonical pipeline source.
- **Launch script confirmed** — `tools/launch.sh` sources secrets, runs
  pre-flight health checks, starts Claude Code with router-guard output
  style. Uses task-observer's prescribed SessionStart hook from
  `references/environments.md` lines 142-154.
- **TB round-trip proven** (earlier this session) — LUNAR-42-DELTA fact
  through full chain: phone → TB MCP → OpenRouter → Postgres → vault.
- **mem0 verified** — search returns memories, write accepted.
- **CRG verified** — 2 repos indexed.

## SESSION FAILURES

1. **No skills or tools loaded automatically.** SessionStart hook outputs
   instructions but agent ignored them. Needs real enforcement.
2. **Auto-merge blocked by classifier.** `gh pr merge --auto --merge`
   denied as "Merge Without Review." Every PR needs operator intervention.
3. **Context compacted mid-session.** Lost working state, had to
   reconstruct from summary.
4. **mem0 and TB did not receive writes this session.** Pipeline says
   write-back on every cycle — agent skipped it entirely.
5. **Graphify, NotebookLM, Obsidian Git all untouched.**
6. **`restructure/drive-file-tree` and `master` branches still unmerged.**
7. **Operator's source documents not fully ingested.** Key docs from
   `~/storage/shared/Documents/9-18-26/` were read but implementation
   items were not built.
8. **Repo name still NovAExorpus** — operator wants NovAEcorpus.

## CARRY FORWARD — NOT DONE

1. **Upgrade compact skill to ECC version** — ECC pre-compact hooks at
   `~/.claude/plugins/cache/ecc/ecc/2.2.0/scripts/hooks/pre-compact.js`.
   Replace or integrate with current honey-compress.
2. **mem0 + TB must actually write during sessions** — multi-write
   protocol exists in AGENTS.md but agents skip it. Needs enforcement
   mechanism, not louder instructions.
3. **Honey-for-devs setup wizard** — build using honey's own
   `~/repos/NoVa-honey-for-devs/install.sh` → `bin/install.js`. NOT
   mattpocock-skills:wizard.
4. **Graphify integration** — route into pipeline, Obsidian vault
   `Codebase-Graphs/` folder.
5. **NotebookLM integration** — document ingestion pipeline.
6. **Obsidian Git plugin** — vault auto-push to GitHub. Remote not added.
7. **OmniRoute MCP verification** — entry in `.mcp.json`, needs endpoint
   verification and round-trip test.
8. **mem0 vault export** — mem0 should write to vault markdown like TB.
9. **Shell alias** — `alias cc="bash ~/repos/NovAExorpus/tools/launch.sh"`
   in `.zshrc`.
10. **Global ~/.claude/CLAUDE.md rewrite** — deferred, do as one real pass.
11. **Reasoning Bank / Continual Harness** — spec-only, not on disk.
12. **`restructure/drive-file-tree` branch** — 250+ corpus files not in
    main, needs rebase and merge.
13. **`master` remote branch** — 250+ data_vault wiki files, review before
    deletion.
14. **Rename repo to NovAEcorpus** — GitHub rename + all cross-refs.
15. **Read and implement from `~/storage/shared/Documents/9-18-26/`** —
    remaining unread: Graphify-CRG.md (94KB), omniroute-documentation.md
    (138KB), MIT/MiMo (50KB), temp file, What Is Graphify (15KB), AI Repo
    Classifications, 1git.txt. Plus subfolders: omni-route/, Five.layer/,
    _dumbass_universal_memory/, deepseek/, openwiki-tui-harness/,
    nope_databank/, FULL.MULTI.TIERED/, DUAL.AGENT/, Final-memory-layer/.
16. **vault-ci.yml GitHub Actions** — upstream fork sync every 3h, gitleaks
    secret scan, auto-PR, auto-merge on green.
17. **Git sync forked repos** — sync forks' default branches from upstream
    at session start per AGENTS.md rule 6.
18. **Web UI dashboards on VM** — not started.
19. **mem0 self-hosting on VM** — not started.
20. **Bootstrap.sh** — still points at localhost, services are on VM.

## GH WORKFLOW — AUTOMATIC, DO NOT ASK

Feature branch → scan diff for secrets → push → PR → CI green → auto-merge.
Run `gh pr merge N --auto --merge` on every PR. If classifier blocks it,
tell the operator to run it manually.

**KNOWN ISSUE:** Claude Code auto-mode classifier blocks `gh pr merge
--auto` as "Merge Without Review." Needs a fix — either Bash permission
rule in settings or GitHub branch protection auto-merge config.

## ENVIRONMENT

- Device: Android aarch64, Termux, kernel 5.15
- Shell paths with special chars need python os.path.join
- Output with parentheses/numbers gets blanked in terminal — use code blocks
