# RESUME.md — Session Ledger
Repository: novae-xorpus
Last session: 2026-09-15

## CORRECTION TO PRIOR SESSION'S CLAIM

The 2026-09-11 entry below claiming "PHASES 1-4 COMPLETE" is **wrong as a
completeness claim**, confirmed by the operator 2026-09-15. 585 files
cleaned is nowhere near real scope — the two original source folders in
`Documents/NovAExorpus/Drive_sync/` total 5,000+ files. What's below is real
work that happened, not a lie — it's just a fraction of the actual job, and
was mislabeled "complete." Do not repeat that mistake: state fraction of
total, not "done," until the whole corpus is ingested.

## WHAT ACTUALLY HAPPENED THIS SESSION (2026-09-15)

Read, not summarized from memory — full source list at the bottom.

- **All 7 base repos pulled current** (aesop-xi, novae-xorpus, novus-aexenti,
  novaexopia, novus-aesc, novus-aeyre, horizons-ui) — local clones were 6-9
  days stale, on an abandoned `restructure/drive-file-tree` branch never
  merged (never even pushed, for this repo). `main` on GitHub was already
  far ahead (operating-rules PRs, full wiki population here on novae-xorpus).
- **RFMC located and fully read** — `Drive_sync/LlmWiki/Repo-Files-Map-core/`,
  7 files, existed for weeks (not "today" — a file-mtime misread corrected
  mid-session). Internally consistent: 8 canonical repos (flat, not nested),
  5+1 tier memory scheme. This is the actual current direction — supersedes
  Document 05's nested-repo model, which nobody deliberately chose (it just
  got half-built by a 2026-09-07 commit).
- **Operator's actual Rule 1 corrected everywhere**: no action — reading,
  searching, anything — without an explicit prompt. (Not just state-changing
  actions, which is what was wrongly documented before.) Live in all 7
  repos' CLAUDE.md/AGENTS.md.
- **PENDING.md created in all 7 repos** — durable backlog, didn't exist
  anywhere before today.
- **GH workflow restored and now consistent across all 7**: feature branch →
  PR → CI → auto-merge on green → main. (A same-session detour to
  "direct-push-to-main" was wrong — reverted. The actual rule: nothing gets
  left stranded on an unmerged branch, not "skip CI.")
- **4 tool forks identified and partially wired**: `mem0` (hosted, already
  cross-device via API token — genuinely working), `honey-for-devs` (active
  all session), `task-observer`/one-skill-to-rule-them-all (installed since
  2026-09-06, now actually triggered via a CLAUDE.md line — wasn't firing
  before), `terrestrial-brain` (real local Postgres+pgvector path built for
  Termux, NOT yet running — see blockers below).
- **horizons-ui wiped and rebuilt from zero** — old repo (38 PRs, "Novus
  Agenti/Omni Claw", predates this corpus effort by ~3 months, broken
  NPU-runtime architecture) deleted. Full history archived first:
  `raw-databank/horizons-ui-full-history.bundle` (git bundle, restorable)
  + `raw-databank/horizons-ui-full/` (current file snapshot) +
  `raw-databank/README-SALVAGE.md` (real post-mortem on what went wrong,
  worth reading before rebuilding: half-finished GenieX migration, four
  separate silently-swallowed exceptions that hid it for months).
- **`novaexopia/horizons-ui/` subfolder flagged, not yet resolved** — built
  from the now-superseded Document 05 nested model, duplicates the fresh
  standalone repo above.
- **Obsidian**: live vault confirmed = `Documents/NovAExorpus/` (NOT the old
  `/storage/emulated/0/OBSIDIAN_VAULT/` path — gone). `obsidian-skills`
  plugin already installed since 2026-08-08, nothing to redo there.

## BLOCKERS — nothing below can proceed without these

1. **`OPENROUTER_API_KEY`** — needed for terrestrial-brain's LLM extraction
   (thought-splitting, metadata tagging) and for the Obsidian plugin sync
   to do anything. Not found anywhere on device. Operator has to supply this
   or set up the account.
2. **Jetson Orin Nano Super reachability from this phone** — unknown.
   Terrestrial-brain (and eventually mem0) should self-host there instead
   of phone-`localhost`, but that migration is blocked on next session's
   Android-Local-Desktop/terminal-APK work making the Jetson manageable.
   Until then, terrestrial-brain runs phone-local (env-var swap later, no
   rebuild needed).
3. **OB1 and reasoning-bank** — mentioned by the operator as tools to wire
   in, not yet verified to exist/what they need. Do not assume shape,
   check before touching.

## PRIORITY ORDER — operator-stated 2026-09-15, do not resequence

1. **Finish wiring the 4 layers operationally** (mem0, honey, task-observer,
   terrestrial-brain) — not just config-present, actually running/verified
   round-trip. This is what makes tool-usage monitoring (a separate
   orchestration/watchdog agent the operator is having Gemini/Spark build,
   external to this repo) actually meaningful.
2. **Run a `/grill` session** (mattpocock-skills:grilling or the base
   grilling skill, "grill with docs") to pressure-test the ingestion plan
   **before** touching the 5,000+ file corpus. Explicit operator instruction,
   don't skip it.
3. **Full ingestion of everything in `Drive_sync/LlmWiki/`** — every file,
   not sampled. Repos need to be built out "to a T" to resemble what's
   actually in there. Consolidated/condensed content goes into the correct
   repo per RFMC's 8-repo model, not left loose.
4. **The original reading backlog, still not fully read**:
   - `__RESUME.md/_RESUME.md(latest)/` — the ~14-file folder and the two
     chat-export folders (`.Claude session 9-13`, `9-09-2026`, ~85 files
     combined) — only the curated docs were read, not the raw numbered
     fragments.
   - `__RESUME.md/Housekeeping/` — 12 files, including a 26-file Markor
     subfolder. Not opened at all.
   - `NovA-Corpus` repo — operator's own 9-15 prompt already says: mine for
     anything valuable, then erase and terminate the repo. Not started.
   - A "scripts folder" the operator wants ported so it actually lives in
     the corpus (not yet identified which folder — ask, don't guess).
   - `__RESUME.md/_PENDING.md/` — ~35 files, not yet gone through.
5. **Build out the 15-20 tools/skills/scripts/plugins** the operator has
   mentioned across the session — no clean consolidated list exists yet of
   exactly which 15-20. Needs to be compiled before this step starts.

## Prior phases (2026-09-11, partial — see correction above)

- Phase 1 ingestion: 585 files cleaned via `tools/clean.py` (mutool for PDF,
  python-docx for DOCX) — a fraction of real scope, not complete.
- Phase 2 RLVR: 172 PASS, 407 WARN, 6 FAIL via `tools/check.py` (disjoint
  extractors: pypdf/zipfile+xml.etree/BeautifulSoup).
- Phase 3: 3135 chunks, `chunk.jsonl` + `manifest.jsonl`.
- Phase 4: `02_wiki_md/` populated, 592 docs, organized by vendor
  (qualcomm/google/anthropic/github/primeintellect/nvidia) + concepts/
  architectures/entities — note this organization doesn't match RFMC's
  `concepts/architectures/entities/indexes` categorization exactly; not
  reconciled.

## Sources actually read this session (not from memory/summary)

`05_FEDERATED_FILE_TREE_TOPOLOGY_MASTER.md`, all 6 repos' RESUME/CLAUDE/AGENTS.md,
7 RFMC files in full, 11-file "Terrestrial Brain, OSTRTA, mem0 and H4D's" folder,
2 previously-skipped Google-AI-Mode chat exports, `TOOLS-SCRIPTS-HOOKS-INVENTORY.md`
(2026-09-10, was uncommitted), `raw-databank/README-SALVAGE.md`, terrestrial-brain's
README/CLAUDE.md/local-db-client.ts/setup.sh, mem0/honey-for-devs/task-observer
READMEs, live GitHub commit history + branch protection state for all 7 repos.

## ENVIRONMENT

- Device: Android aarch64, Termux, kernel 5.15 — this is the device filesystem, not GitHub
- Shell paths with special chars need python os.path.join
- Output with parentheses/numbers gets blanked in terminal — use code blocks
