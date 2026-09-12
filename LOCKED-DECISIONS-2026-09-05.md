# NovÆxorpus — Session Resume / Handoff

Full rewrite, 2026-09-05. Owner: c10vis-poem (nav@clovispoem.com). For anything not addressed this session, see `unresolved.md` in this repo.

## What this session did

Comprehensive review of NovÆxorpus architecture, auditing the background agent's LIVING_MASTER_CANON output (8 canon docs + 6-repo tree), cross-referencing LEX-NOVI audit results (11 separate audits), and assessing BUILDERS_GUIDE integration status against the 93-file cleaned corpus.

Three major deliverables:
1. **AUDIT-01-TARGET-DOCs-v3-GOLD-EXTRACTION.md** — canonical folder-1 audit reconciling S6 + F6 findings
2. **REVIEW-CANON-AND-BUILDERS-GUIDE.md** — 20+ deltas (operator directive vs. delivered output), with exact line/file citations
3. **PROPOSAL-V2-CORRECTED-WIKI-TERMINOLOGY-AND-ALTERNATIVE.md** — corrected wiki tree (5+1 tier vault), canonical terminology glossary (13 entries: SDK, Runtime, Engine, MCP Server, Harness, Agent, Model, KV cache vs. SQL, MAP.md vs. manifest.jsonl, OmniRoute, Recall, Strategic, Episodic), hybrid repo structure recommendation, real Aggressive alternative (VENDOR-FIRST organization)

All files currently staged in Google Drive (`__NÆX-Review-OUTPUT/`); **will be moved to this repo** at next session.

## Operator decisions locked this session (11 total)

1. **OmniRoute is absolutely a memory extraction layer** — routing is consequence, not primary role
2. **Red Agent incognito isolation** — pull `~/.red/` entirely out of visible tree, not just hidden directory
3. **Beginner-Proof Standard** — if a third-rate model or beginner dev can't pick up and resume work, code is broken; non-negotiable
4. **5+1 tier vault structure confirmed** — raw sources → wiki → recall cache → skills runtime → episodic logs, plus ephemeral working state
5. **POCKET-35B dropped** — too large for on-device constraints, replaced by Gemma 4 12B on roster
6. **Gemma 4 12B multimodal on model roster** — `gemma-4-12B-it-qat-UD-Q4_K_XL.gguf` confirmed in `~/downloads/`, audio branch available
7. **Spelling: novaexopia (no ligature in URL)** — NOT `novaæxopia`, consistent with novae-xorpus/aesop-xi pattern
8. **README pattern for vendor folders** — include projects, credentials, expirations, TODOs, human accessibility (not just "kid accessibility")
9. **Vendor-workspace derive-from-function design** — each vendor gets its own folder shape derived from what that vendor IS in the stack, not templated; Qualcomm reference implementation locked (workbenches/sdks/runtimes/hardware/models/deploy-per-repo)
10. **Google visibility proliferated** — Google gets first-class status in vendor folders (accounts/credits/services), not buried
11. **Hybrid structure locked** — 12 top-level: aesop-xi/, novus-aexenti/, novaexopia/, skills-and-capabilities/, data_vault/, google/, qualcomm/, nvidia/, github/, anthropic/, primeintellect/, deepseek/, tools/

## BUILDERS_GUIDE corpus status

Scanned 93 cleaned files from `02-clean/`. Result: ~60-70% are duplicates already ingested into prior audit docs; only 4 files genuinely unopened:
- ___Will This Work? (701 KB)
- nanobot notebook (56 KB)  
- Operation Launchpad (189 KB)
- Gemma 4 12B ONNX (495 KB)

Remaining corpus sufficient for archive; no action needed.

## Technical clarity achieved

- **MAP.md** — human nav index (wikilinks, structure)
- **manifest.jsonl** — machine RAG stream (never load whole, JSONL format)
- **Wiki interior structure (proposed)** — vendors/, weights/, runtimes/, engines/, harnesses/, agents/, protocols/, scripts/, tools/, skills/, memory-subsystem/, projects/, entities/, architectures/, runbooks/, references/, operator-log/, indexes/
- **Qualcomm vendor shape (reference)** — workbenches/{qairt-hexagon-htp, geniex-llamacpp-hexagon, litert-android, qat-training}, sdks/{qairt, litert, qai-hub-cli}, runtimes/, hardware/{per-chip-profiles}, models/, deploy-per-repo/{aesc, novaexopia, novus-aexenti}, raw/, clean/, notebook/, runbooks/
- **4 agent operating modes** — Dev-Terminal (ECC only) / Sovereign-Edge (Prime Agent only) / Prime-with-Claude-as-Query (Prime calls Claude subprocess) / Hybrid-Auditor (cross-auditor over combined traces)
- **Modular hot-swap for harnesses** — 4 well-defined interfaces: model via OmniRoute, memory via MCPs, tools via MCPs, output to trajectories

## Immediate next targets (operator-declared strict order)

Do NOT start post-tonight targets until these are complete:

1. **DroidDesk install** — phone + tablet (Termux:X11 rendering, standalone desktops, not phone→tablet mirroring)
2. **Æsc terminal daemon setup** — salvage 5 targets from Horizons (NPU loader, ADB loopback, Chromium integration, terminal render, model router); junk everything else to junkyard; fix Watchdog daemon using ForegroundService
3. **Fold Termux-era work into Æsc** — rewrite scripts for native APK (not proot)

## Post-tonight targets (deferred, do NOT start)

- Grill session with docs
- New repo build-out (Hybrid 12-top-level structure)
- Œræcle on-device oracle wiring
- Model weights into novaexopia
- DeepSeek harness spec
- vendor-workspace skill implementation

## Unresolved items (open for discussion / later)

From `unresolved.md` in this repo:
- Tailscale install status (never re-checked since 2026-07-17)
- T3 infrastructure (Jetson Orin Nano, Rubik Pi) — on hold, hardware not yet procured
- obsidian-skills clone into `~/vault`
- notebooklm proot+VNC login (VNC approach now superseded by DroidDesk decision)
- OpenWiki fork upstream PR status (fork has diverged with own NPU/voice work)
- Open architectural decisions: Auditor isolation vs. cloud GLM-5.2; Recall + Strategic memory backend (shared or separate); Home executive binding (Jetson vs. phone Qwen)
- HTTP/WebSocket server for voice engine (explicitly deferred)
- OmniRoute / OB1 / ReasoningBank routing — genuine design decision needed before build
- Universal skill placement pattern (obsidian-skills model)
- MASTER-SKILLS.md aggregation (design call: full concatenation vs. index table)
- ECC's unified-memory vault vs. #dumbass hand-built approach (design decision not yet made)
- ECC dashboard-on-tablet via SSH tunnel (steps given, never confirmed working)

New items from this session (see proposals for detail):
- Œræcle canonization in NAMING-CANON.md (if moving forward with on-device oracle)
- NopeDataBank standalone spec section (if adopting as vector/episodic store)
- 4 unopened BUILDERS_GUIDE files (lower priority, archive-sufficient)
- UI rebuild direction (Jetpack Compose candidate vs. current Horizons salvage)
- Cost-checking loop implementation (cross-vendor spend tracking)
- Modular hot-swap harness implementation (4-interface spec ready, build TBD)
- Carry forward existing unresolved.md items (no changes, all still live)

## What's currently in Google Drive

All audit/review/proposal docs staged at `__NÆX-Review-OUTPUT/`:
- AUDIT-01-TARGET-DOCs-v3-GOLD-EXTRACTION.md (canonical folder-1 reconciliation)
- REVIEW-CANON-AND-BUILDERS-GUIDE.md (20+ deltas with citations)
- PROPOSAL-V2-CORRECTED-WIKI-TERMINOLOGY-AND-ALTERNATIVE.md (corrected structure + glossary + real alternative)
- MASTER-COPIES/ folder (S6/F6 reconciliation + 13 appendices)
- Reference docs from background agent (LIVING_MASTER_CANON output)

**Action for next session**: Move all to novae-xorpus/ (likely `/REVIEW/` subfolder or root level, TBD with operator).

## Trigger for next session

Pick up exactly where this ended:
1. Confirm which deliverables to move from Drive to novae-xorpus (all of them? prioritize?)
2. If moving all: organize structure in repo (root-level REVIEW/ subfolder? merge into wiki/?))
3. Continue with Immediate Next Targets (DroidDesk, Æsc, Termux fold-in) — these are operator-declared priority, sequenced
4. For each deliverable moved: confirm operator review + lock in any new decisions before downstream builds

---

**Session context**: This session audited the background agent's LIVING_MASTER_CANON output against operator directive, found 11 operator decisions that were either missing or contradicted, produced two corrected proposals (v1 → v2, fixing template autopilot and underspecified wiki tree), and locked all 11 decisions. Terminology standardized; vendor-workspace pattern established; hybrid repo structure finalized. Ready to move deliverables to repo and start implementation phase.

**Provenance**: All audit/review/proposal work by Claude Haiku 4.5 (this session). Background agent output (LIVING_MASTER_CANON, 8 canon docs, 6-repo tree, LEX-NOVI audits) verified against 93-file cleaned corpus and BUILDERS_GUIDE.
