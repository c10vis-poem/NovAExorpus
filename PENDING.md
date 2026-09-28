# PENDING.md — NovAExorpus

Durable cross-session backlog. Not rewritten each session — items persist until resolved or explicitly dropped.

- **RESUME.md's "PHASES 1-4 COMPLETE" is wrong.** 585 files cleaned is nowhere near real scope — the two original source folders in `Drive_sync` total 5,000+ files. Needs correction and a real re-ingestion pass, not just a status-line fix.
- **Other 6 repos still POINTER.md stubs.** `novus-aexenti`, `NovAExopia`, `aesop-xi`, `horizons-ui`, `novus-aesc`, `novus-aeyre` haven't had their own ingestion pass — only `NovAExorpus` itself has real `clean_md`/`wiki_md` content.
- **`NovAExopia/horizons-ui/` was built from Document 05** (the nested-repo model), which is superseded now that RFMC (flat 8-repo model, `Drive_sync/LlmWiki/Repo-Files-Map-core/`) is the actual direction. Needs reconciling once the new standalone Horizons UI repo exists.
- **Terrestrial-brain backend location** — currently phone-local Postgres (works today via env vars in `.mcp.json`), migrating to self-hosted on the Jetson Orin Nano Super once the terminal-APK/Android-Local-Desktop work (next session) makes that device reachable and manageable.
- **QNN-QAIRT SDK (3035 files) and canvas-ui-main (416 files)** — sitting in `__RESUME.md/whatisit-/` on device, not yet ingested.

## Added 2026-09-28

- **Session-end discipline isn't enforced.** RESUME.md must be rewritten top to bottom every session and unresolved items moved here — no hook checks it. Needs a structural check (grill topic 11 / launch script).
- **Operator's own MEMORY.md** — enterprise-wide, separate from Claude's memory; RESUME / AGENTS / MEMORY / PENDING from the other six base repos to sync into this corpus repo (grill topic 3).
- **Hooks not registered yet** — `sync-forks` / `ship-session` need the operator's paste (classifier blocks the agent).
- **Old Claude memory + ECC rules** — archive line not run yet.
- **Other six repos: CLAUDE.md → AGENTS.md** and GitHub renames to `NovusAExenti`, `AEsop-Xi`, `AEsc`, `AEyre`, `Horizons-Ui` — after the grill.
- **OpenWiki replacement** — fork + read `jatinmayekar/openwiki-for-claude-code`, install, remove OpenWiki MCP/TUI/workflow.
- **OB1 Obsidian plugin + OmniRoute Obsidian plugin** — none exist; build (grill topics 5/7).
- **MemVault** — operator setting up; decide if its folder is public.
- **Nested `/NovAExorpus/` repo mirror in the vault (3.1 GB)** — ignored for now; replace with maps/links to every repo.
- **Stale VM IP `34.31.112.77`** in `tools/launch.sh`, `router-guard.sh`, `.mcp.json` defaults.
- **OmniRoute on the VM runs the npm build, not the c10vis-poem fork.**
- **Terrestrial Brain VM unit file has the OpenRouter key in plaintext, world-readable** — rotate the key.
- **Recovered plugin drafts** (`recovered/2026-09-26-ob1/omni-feat/`) never pushed; orchestration contract = Æsop-Xi draft PR #18.
- **3 diverged forks** — pm-claude-skills, trusted-firmware-a, ai-hub-apps get upstream PRs on next `sync-forks`.
- **ECC-aesop has 18 unpushed local commits on main** — skipped by ship-session (ECC off-limits); operator to decide.

## Carried from RESUME.md 2026-09-18 (not re-verified this session)

- Qwen3.5-2B on phone NPU (geniex-bench, HTP v79) not wired; OmniRoute backend for it.
- `feat/vm-lifecycle-2026-09-18` branch never pushed.
- sherpa-onnx: 8 inherited upstream cron workflows still active.
- dsh workspace selection; OpenRouter key on VM; passwordless sudo on VM.
- mem0 + TB actually writing during sessions; mem0 vault export; mem0 self-hosting on VM.
- Honey-for-devs setup wizard; Graphify integration; NotebookLM integration.
- OmniRoute MCP round-trip test; web UI dashboards on VM; `bootstrap.sh` still points at localhost.
- `restructure/drive-file-tree` branch (250+ corpus files); `master` remote branch — review before deletion.
- Source docs in `~/storage/shared/Documents/9-18-26/` unread.
- `vault-ci.yml` workflow; shell alias `cc`; global `~/.claude/CLAUDE.md` rewrite.
- "Rename repo to NovAEcorpus" — conflicts with NAMING-CANON (NovÆxorpus / `NovAExorpus`); confirm or drop.
- "Obsidian Git plugin" — superseded by GitSync Portal; drop unless wanted.
- **MemVault server** — waits for the Jetson; fork `dreamor/MemVault` → c10vis-poem and build the image from the fork (not `ghcr.io/dreamor/memvault`). Decide in grill topic 7 whether it earns a place next to Mem0 and OB1.
