Session files: [[AGENTS]] · [[PENDING]] · [[MAP]] · [[GRILL-MANIFEST]] · [[NAMING-CANON]]

# RESUME.md — Session Ledger

Repository: NovÆxorpus (`c10vis-poem/NovAExorpus`) — master wiki + vault.
Last session: 2026-09-27 → 2026-09-28 (phone, Claude Code, Opus 5.5).
Rule: this file is rewritten top to bottom at the end of every session.
Anything unresolved goes to `PENDING.md`.

## NEXT SESSION — START HERE

1. Open Claude Code **in the vault**: `cd ~/storage/shared/Documents/NovAExorpus && claude`
   (Claude Code ≥2.1.277 loads `AGENTS.md` by itself; there is no CLAUDE.md).
2. Operator types: `/setup-matt-pocock-skills` (issues: GitHub,
   `c10vis-poem/NovAExorpus`) → `/cleanmyharness` → `/grill-with-docs` →
   `/to-spec` → `/to-tickets` → `/implement`.
3. The agenda is `GRILL-MANIFEST.md` — nothing is off the table.

Before that, operator still has to (see "Operator to-do" below): switch
GitSync to `vault-sync` and run the first sync, paste the hooks line, paste
the memory-cleanup line.

## WHAT HAPPENED THIS SESSION

### Recovered lost work
The 2026-09-25/26 session's OB1 deep-read notes, three OmniRoute plugin
drafts (Reasoning Bank, Continual Harness, retrieval planner) and the
orchestration contract lived only in a temporary scratchpad and were deleted.
Rebuilt from the session transcript into `recovered/2026-09-26-ob1/`.
A scratchpad-archive hook now copies every session's scratchpad to
`~/.claude/scratchpad-archive/` at session end and before compaction.

### GitHub workflow — now enforced, not just written
Audit: the workflow was never scripted anywhere; direct pushes to `main`
happened in all 7 own repos (raw-databank 9/10). Built:
- `~/bin/sync-forks` — session start: syncs all 129 c10vis-poem forks
  (first run: 126 synced; 3 diverged — pm-claude-skills, trusted-firmware-a,
  ai-hub-apps — now get an upstream PR instead of a force-sync);
  fast-forwards clean local clones.
- `~/bin/ship-session` — session end: commits and pushes everything pending
  in every own repo, opens PRs, auto-merges on green, flags anything that
  can't merge as NEEDS FIX. Keeps branches (AGENTS.md rule). Skips ECC-aesop.
- GitHub (run by operator): all 7 own repos now require a PR into `main`,
  enforce_admins on, auto-merge allowed. `vault-sync` branch created.
- Secret scanning + push protection verified on in every public repo. The
  only 2 open alerts are upstream authors' keys in forks (`c10vis--pi`,
  `NovA-ai-agent-book`) — nothing of the operator's is exposed.

### Vault sync — found broken, fixed
GitSync Portal had **never** synced before 2026-09-27 23:49 (last sync: never): a 534 MB
`model.safetensors` aborted every run. 7,951 vault files had never reached
GitHub. Ignore list now adds `QAIRT-QNN/`, `*.safetensors`,
`/NovAExorpus/` (on-device repo mirror) and `Large_plan-PDF's/` (personal
records, Drive only). `Drive_sync/` stays synced by choice. First sync is
now 6,201 files, 0.85 GB, nothing over 50 MB. GitSync set to sync on
startup only (no on-save, no hourly); branch → `vault-sync`, which
`ship-session` merges into `main` through a PR.

### Instruction files
- AGENTS.md is the single instruction file for every engine; the vault's
  CLAUDE.md was deleted. Added Rule 3 (docs 00–05 contain inconsistencies
  and incorrect statements), Rule 4 (<~150 corpus files honestly read,
  1,000+ remain, no read record exists), the current GH workflow, Task
  Observer and Launch sections.
- `NAMING-CANON.md`: NovusÆxenti confirmed; repo names never all lowercase —
  targets `NovusAExenti`, `AEsop-Xi`, `AEsc`, `AEyre`, `Horizons-Ui`.
- `GRILL-MANIFEST.md` written: 11 topics + the operator's 4-MCP fan-out
  table (Mem0 / OB1 / Graphify / code-review-graph, plus ReasoningBank,
  Continual Harness, Task Observer).

### Decisions this session
- OB1 is the memory backbone; Supabase runs locally on the Jetson Orin
  Nano Super (not Supabase cloud). OB1 not installed yet.
- OpenWiki is being replaced by a Claude Code skills plugin
  (`jatinmayekar/openwiki-for-claude-code`, fork first).
- ECC is never wired as a harness; skills only if copied in before a session.
- Harness direction (grill topic 4): Hermes, DeepSeek Harness and
  Antigravity manage; Claude Code becomes a builder tool.
- Nothing may sit unmerged — merged or flagged.
- The operator will keep an own MEMORY.md (enterprise-wide, separate from
  Claude's), and all session-persistence files (RESUME, AGENTS, MEMORY,
  PENDING) from the other six base repos will sync into this corpus repo so
  everything is run from one place (grill topic 3).

## OPERATOR TO-DO BEFORE THE GRILL

1. Obsidian → Settings → GitSync Portal: Branch = `vault-sync` →
   Test connection → Run two-way sync now. "Last sync" should show a time.
   Home note = `RESUME.md`.
2. MemVault: set it up; tell the agent its folder if its notes must stay private.
3. Paste in Claude Code (makes sync-forks / ship-session automatic):
   `! f=~/.claude/settings.json; jq '.hooks.SessionStart=[{"hooks":[{"type":"command","command":"jq -r .session_id | { read -r s; nohup ~/bin/sync-forks \"$s\" >/dev/null 2>&1 & }","timeout":10}]}] | .hooks.SessionEnd[0].hooks+=[{"type":"command","command":"jq -r .session_id | { read -r s; nohup ~/bin/ship-session \"$s\" >/dev/null 2>&1 & }","timeout":10}]' $f > $f.tmp && mv $f.tmp $f && jq '.hooks|keys' $f`
4. Paste the memory-cleanup line (archives old Claude memory + ECC rules,
   keeps the 4 new notes) — in the 2026-09-28 session transcript.

## VM REFERENCE

- Instance `omniroute-brain`, zone `us-central1-a`, project
  `project-alchemist-490416`. Control from phone: `~/bin/vm on|off|status|ssh`.
- External IP is **ephemeral** — changes every start (`vm on` prints it).
  `34.31.112.77` in `tools/launch.sh` and `router-guard.sh` is stale.
- Idle auto-off after 30 min; 4 AM backstop.

## ENVIRONMENT NOTES

- `!` prefix works **only inside the Claude Code chat box** (runs the command
  in the session). In a plain Termux shell it does nothing — paste the
  command without the `!`. Give the operator commands in code blocks.
- zsh: never name a loop variable `path` — it overwrites `PATH`.
- GitSync Portal syncs through the GitHub API; the vault's `.git` folder is
  an empty leftover and unrelated.

## HANDOFF SOURCES

Read this session: vault AGENTS.md, CLAUDE.md (now deleted), old RESUME.md,
PENDING.md, NAMING-CANON.md, GRILL-MANIFEST.md, .gitignore,
`tools/launch.sh`, `.claude/hooks/router-guard.sh`, GitSync Portal settings;
transcript of session 18a82005 (2026-09-25/26); orchestration contract §3.2;
GitHub API state of all 139 repos.
Not read: documents 00–05 (only listed), MAP.md, MASTER-CLAUDE.md,
MASTER-RESUME.md, SOURCE-RETRIEVAL-MAP.md, the corpus itself.
