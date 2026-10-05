# MEMORY.md — NovAExorpus (the vault)
Durable facts about this repo. Dated; newest first. Updated at session wrap-up.

## 2026-10-05
- **Private files were removed** from the public repo (PR #34); old commits still hold them until the operator runs the fresh-repo step (RESUME item 0b). `main`, `vault-sync` and GitSync's `lastSyncedCommit` were aligned 2026-10-05.
- **Private material never goes in here.** Personal memory, legal/financial, unfiled designs, billing → `Documents/private-memory/` (outside the vault, never synced). `*BILLING*.csv` is gitignored.
- **MASTER-AGENTS.md / MASTER-RESUME.md** are built on GitHub by `.github/workflows/master-files.yml` (`tools/build_masters.sh`) whenever a base repo's AGENTS.md or RESUME.md changes on main (base repos' `notify-vault.yml`, secret `VAULT_DISPATCH_TOKEN`). No timer. Never hand-edit them. `MASTER-CLAUDE.md` is retired.
- **AGENTS.md is the only instruction file** (no CLAUDE.md in any base repo).
- **Target layout:** `__RESUME.md/__Builder-Guide_Directory-/Master_Dumbass_config/_#Repository-layout.txt` (00-governance … 10-exports), PRIORITY ONE together with `Master_dumbass_plan-session/`. `__RESUME.md/` is the work queue and dissolves into the layout during/after the grill. Docs 00–05 at the root are wrong (AGENTS Rule 3).
- **Device vault = exact mirror of this repo** (end goal): no nested copies, duplicates or extras. `Documents/Zip/` is a full backup copy (refreshed 2026-10-05). The nested mirror was moved to `Documents/NovAExorpus-nested-mirror/`.
- **GitSync** syncs on Obsidian startup only (no timer). It writes `*.conflict-android-*` copies when a file changes on both sides.
