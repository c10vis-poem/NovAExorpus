# RESUME — NÆX Review & Canon Correction Session

**Session:** 2026-09-04 → 2026-09-05 (Claude Opus 4.7)
**Location:** `__NÆX-Review-OUTPUT/` (Drive, alongside `__NovÆxorpus(NÆX)` and `___Lex-Novi-Æxentis-Copiæ`)
**Convention:** Full rewrite, not append (per `aesop-xi/CLAUDE.md`). This file is a snapshot of state, not a running log.

---

## What this session did

1. **Read all 30 files in `__NovÆxorpus(NÆX)/1- TARGET DOCs/`** — GLM prelim + S-tier + A-tier + Findings + CLOSE_2_TARGET. Produced 3 audit versions: `AUDIT-01-TARGET-DOCs.md` (v1 skeleton), `AUDIT-01-TARGET-DOCs-v2-COMPLETE.md` (kill-list lens), `AUDIT-01-TARGET-DOCs-v3-GOLD-EXTRACTION.md` (unique-contribution lens per operator reframe). v3 is canonical.
2. **Wrote Master Doc 01** — `00-MASTER-COPIES/01B-VAULT-ROOT-and-DEFINITIVE-MASTER-SPEC.md`: S6 Definitive Master Spec integrated substantially verbatim + F6 5+1 tier reconciliation + 13 appendices covering every folder-1 doc that contributes.
3. **Reviewed the background agent's output** (`__NovÆxorpus_LIVING_MASTER_CANON/` — 8 canon docs + 6-repo tree + `data_vault/` with 5+1 tier subfolders) + (`__LEX-NOVI-Review-OUTPUT/` — 11 numbered audits + master synthesis + `run_audit.sh`). Wrote `REVIEW-CANON-AND-BUILDERS-GUIDE.md` with 20+ specific deltas.
4. **Verified BUILDERS_GUIDE dup status** against `novae-xorpus/02-clean/` (93 cleaned files). Confirmed ~60-70% of "unopened" BUILDERS_GUIDE files ARE already in the corpus. Only 4 files genuinely need opening: `___Will This Work?` PDF (701KB), `nanobot notebook` (56KB), `Operation Launchpad` PDF, `Gemma 4 12B ONNX` Gdoc (495KB).
5. **Produced two iterations of the update proposal:**
   - `PROPOSAL-UPDATE-and-ALTERNATIVE-RECOMMENDATION.md` (v1 — underspecified, cosmetic alternative)
   - `PROPOSAL-V2-CORRECTED-WIKI-TERMINOLOGY-AND-ALTERNATIVE.md` (v2 — corrected wiki tree, real Aggressive alternative, terminology glossary, MAP.md vs manifest.jsonl definitive spec)
6. **Landed the vendor-workspace pattern** across two rounds — first generic template, then "derive-from-function" per-vendor. Qualcomm shape locked as the reference example.

---

## Operator decisions locked (apply to canon going forward)

1. **OmniRoute = memory extraction layer** (agent was wrong to overrule; operator was right). Extraction is primary; routing is consequence. Runs at `localhost:20128/v1`.
2. **Red Agent stricter isolation** — pull `.red/` out of the visible tree entirely (sibling directory, not `05_episodic_logs/.incognito_red_sandbox/`). Only surface: `red_verdict: pass|fail|n/a` field on trajectory records. Discoverability test: fresh agent reading visible tree cannot conclude Red Auditor exists.
3. **Beginner-Proof Standard** = real invariant (add as AGENTS.md hard rule 8). Test: could a third-rate model or beginner dev pick up your work and resume it? If not, code is broken.
4. **5+1 tier** for regular project repo wikis. **Master wiki** (`novae-xorpus/data_vault/02_wiki_md/`) gets a MUCH richer interior — see Part 3 of proposal v2 for the full tree with vendors/, weights/, harnesses/, agents/, runtimes/, engines/, protocols/, scripts/, tools/, skills/, memory-subsystem/, projects/, entities/, architectures/, runbooks/, references/, operator-log/, indexes/.
5. **POCKET-35B dropped** entirely. >8GB is impossible on-device (7GB is already pushing it).
6. **Gemma 4 12B** on the roster (Node Beta candidate).
7. **`novaexopia` with `x`, not `c`** — global fix; folder tree was already correct, only prose drifted.
8. **README everywhere** — every folder gets 3 files at root: `README.md` (human), `MAP.md` (agent nav — the "JSONL manifest for humans"), `manifest.jsonl` (machine RAG).
9. **Vendor workspace shape derives from function, not template.** Qualcomm = workbenches/sdks/runtimes/hardware/models/deploy-per-repo (SILICON+SDK vendor). Google = accounts/services/credits/projects/expirations (ACCOUNT ecosystem). Nvidia/GitHub/Anthropic each get their own function-derived shape when built.
10. **Google gets prolific top-level visibility** — promoted out from under `red_auditor`. Qualcomm/Nvidia/GitHub same.
11. **Hybrid repo structure** = Balanced (6 canonical entity repos: aesop-xi, novus-aexenti, novaexopia, skills-and-capabilities, data_vault + broken-out top-level vendor dirs: google/, qualcomm/, nvidia/, github/, anthropic/, primeintellect/, deepseek/, tools/).

---

## What's in Drive right now

**`__NÆX-Review-OUTPUT/`** (this session's workspace, id `1U98knXRlLthxBOyi-ZmQ6s5WP8VcP5bt`):
- 9 pre-created subfolders (01-TARGET-DOCs through 07-DEFINITIONS + 00-MASTER-COPIES + 99-PROPOSALS-FINAL + 98-CROSS-SYNTHESIS)
- Audits + reviews + proposals as listed in "What this session did" above
- `RESUME.md` (this file)

**`__NovÆxorpus_LIVING_MASTER_CANON/`** (background agent's output, id `1xv0yKrUnlzUqLBUfDIlHo0uWFv-KqTBV`):
- 8 canon docs (00_DEFINITIVE_MASTER_SPECIFICATION_V3_COMPLETE through 05_FEDERATED_FILE_TREE_TOPOLOGY_MASTER + README + RESUME)
- 6-repo scaffolded tree: aesop-xi, novus-aexenti, novaexopia, vendor-corpora, skills-and-capabilities, data_vault (with 01_raw_sources through 05_episodic_logs subfolders), tools
- STATUS: solid architecture package, but needs the 11 operator-decisions applied (see above). Not yet corrected.

**`__LEX-NOVI-Review-OUTPUT/`** (Lex-Novi audit output, id `114WRVZlfe_n4Owlz2jyJj7SDptZ4I-aQ`):
- Master synthesis + 11 numbered audits + `run_audit.sh`
- 10 Landmark Breakthroughs cataloged (see synthesis doc)
- Duplicate copies at shared-drive root — should be trashed

**Originals untouched** — every file in `__NovÆxorpus(NÆX)` and `___Lex-Novi-Æxentis-Copiæ` is 100% intact.

---

## Immediate next targets (in strict order)

**Tonight's focus (operator-declared):**

1. **DroidDesk install** on phone + tablet (Termux:X11 rendering, standalone desktops per device). Success = both boot into real desktop with OpenWiki TUI usable.
2. **Æsc terminal daemon setup** — salvage from old Horizons APK per Part 10 salvage philosophy: keep the 5 salvage targets (NPU loader, ADB loopback client, Chromium integration, terminal render, model router), junk everything else to `horizons-legacy-junkyard/` with `SALVAGE-NOTES.md`. Rewire the broken Watchdog daemon using ForegroundService + START_STICKY.
3. **Fold Termux-era work into Æsc** — walk `~/repos/aesop-xi/` for Termux-specific setup scripts, rewrite for Æsc native (no sandbox).

**Do NOT start yet (post-tonight):**
- Grill session with docs
- New repo build-out (the Hybrid 12-top-level tree)
- Œræcle on-device oracle wiring
- Model weights wired into novaexopia
- DeepSeek harness spec (whenever DeepSeek is ready)
- `vendor-workspace` skill implementation

---

## Unresolved (still open for discussion or later work)

1. **OB1 vs Postgres schema drift** — how `OB1 Protocol` maps onto actual Postgres tables on Node Beta not yet spec'd
2. **Œræcle canonization** — operator implicitly OK'd (Part 4 of proposal v2 treats as first-class), but not yet added to `NAMING-CANON.md`
3. **NopeDataBank** — mentioned throughout but no standalone spec section written; needs one in `02_DUMBASS_UNIVERSAL_MEMORY_SPEC.md`
4. **DeepSeek harness** — operator flagged it as "hot run soon"; full spec TBD when it lands
5. **`___Will This Work?` PDF (701KB)** — genuinely un-opened; may be untruncated source of `part-1-lex-1-drive-text-extract-truncated.md`
6. **`Gemma 4 12B ONNX` Gdoc (495KB)** — genuinely un-opened; HIGH PRIORITY given Gemma 4 12B on roster
7. **`nanobot notebook` (56KB)** — AUDIT-03 claims extracted; target folder empty. Needs real extraction to `novaexopia/modular_harnesses/local-nanobots/`
8. **`Operation Launchpad` PDF (189KB)** — un-opened; may contain launch procedures
9. **UI rebuild direction** — operator wants modern/crisp, not terminal-feel. Jetpack Compose candidate. Not started.
10. **Cost-checking loop** — spec written (proposal v2 Part 7); not implemented
11. **Modular hot-swap for harnesses** — spec written (proposal v2 Part 8); not implemented
12. **Existing `unresolved.md` items** in `novae-xorpus/unresolved.md` (13 items, cross-repo backlog) — carry forward per that file's discipline

---

## Resume trigger for next session

Paste this at the top of the next session:

```
Resume NÆX review session.

Read these Drive files first (in order):
1. __NÆX-Review-OUTPUT/RESUME.md                              (this file)
2. __NÆX-Review-OUTPUT/PROPOSAL-V2-CORRECTED-WIKI-TERMINOLOGY-AND-ALTERNATIVE.md
3. __NÆX-Review-OUTPUT/REVIEW-CANON-AND-BUILDERS-GUIDE.md
4. __NÆX-Review-OUTPUT/AUDIT-01-TARGET-DOCs-v3-GOLD-EXTRACTION.md
5. __NÆX-Review-OUTPUT/00-MASTER-COPIES/01B-VAULT-ROOT-and-DEFINITIVE-MASTER-SPEC.md

Also load: novae-xorpus/AGENTS.md, NAMING-CANON.md, unresolved.md
And: aesop-xi/RESUME.md (for on-device pipeline context)

Current state: architecture proposal v2 landed with 11 operator decisions locked.
Vendor-workspace pattern locked (Qualcomm shape = reference).
Awaiting execution of tonight's checklist (DroidDesk / Æsc salvage / Termux fold-in).

Next action: whatever operator says. If unspecified, start with tonight's checklist Step 1 (DroidDesk install).
```

---

## Provenance (all deliverables from this session)

Every file below sits in `__NÆX-Review-OUTPUT/`:

| File | Purpose |
|---|---|
| `RESUME.md` | This file |
| `AUDIT-01-TARGET-DOCs.md` (v1) | Initial skeleton — superseded, kept for provenance |
| `AUDIT-01-TARGET-DOCs-v2-COMPLETE.md` | Kill/merge lens — superseded |
| `AUDIT-01-TARGET-DOCs-v3-GOLD-EXTRACTION.md` | **CANONICAL folder-1 audit** — unique-contribution lens |
| `00-MASTER-COPIES/01B-VAULT-ROOT-and-DEFINITIVE-MASTER-SPEC.md` | Master Doc 01 (S6 + F6 + 13 appendices) |
| `REVIEW-CANON-AND-BUILDERS-GUIDE.md` | Scrutiny of background agent's output + BUILDERS_GUIDE integration status |
| `PROPOSAL-UPDATE-and-ALTERNATIVE-RECOMMENDATION.md` (v1) | Superseded by v2 |
| `PROPOSAL-V2-CORRECTED-WIKI-TERMINOLOGY-AND-ALTERNATIVE.md` | **CANONICAL proposal** — corrected wiki tree, terminology glossary, real Aggressive alt |

**Rule (from AGENTS.md hard rule 5):** nothing in this list self-certifies. Every claim in every doc traces to a source doc in `__NovÆxorpus(NÆX)` or `___Lex-Novi-Æxentis-Copiæ` or `novae-xorpus/02-clean/`, or is an operator decision preserved verbatim in this file's "Operator decisions locked" section.
