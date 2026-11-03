# Grill session inputs

Start: `/ask-matt` (operator types it; full name `/mattpocock-skills:ask-matt`, from the plugin built from the fork c10vis-poem/NovA-skills), then the Pocock chain: `/setup-matt-pocock-skills` → `/grill-with-docs` → `/to-spec` → `/to-tickets` → `/implement`.

## Priority One (read first)
- `NovAExorpus/__RESUME.md/__Builder-Guide_Directory-/Master_Dumbass_config/_#Repository-layout.txt`: target layout 00-governance … 10-exports.
- `…/Master_Dumbass_config/Master_dumbass_plan-session/` (00-master_config_session + 01–13; 08 = 09).

## Discovery (2026-10-05 subagent readers)
- `Documents/Session-reports/2026-10-05/01-WIKI-SEARCH-RESULTS.md`: synthesis of 11 readers (~1,450 files). §3 = scripts/skills/tools that exist as code, plus the named-but-missing list; §6 = open decisions.
- `Documents/Session-reports/2026-10-05/reader-batches/batch-A…K.md`: per-batch detail with paths (chats listed under "mine later").
- `Documents/Session-reports/2026-10-05/02-VAULT-RESTRUCTURE-PLAN-draft.md`.

## Installed on the device
- `~/.claude/session-work/2026-10-06/TOOL-INVENTORY.md`: every installed skill, plugin, command, agent, hook, MCP server and `~/bin` script, with overlaps and dead links (built 2026-10-06).

## Drafts to settle
- `~/wiki-admin/AGENTS.md`: wiki-admin agent draft (top section).
- `docs/WIKI-ADMIN-GUIDE.md` §10: open decisions (Obsidian skills loading twice, OmniGlyph, Render MCP, `~/.openwiki/`).
- `~/.claude/session-work/2026-10-05/CODE-SPLIT-MAP.md`: Horizons code → Æsc / Æyre / Hyperion-XI.
- `NovAExorpus/PENDING.md` "Added 2026-10-05".

## Grill topics carried in
- Hook-spec decisions (obs review 2026-10-09): which of `skill-updates/2026-10-08/proposals/hooks-spec.md` items 1 to 8 to build (state-file guard 0017, install doc-read preflight 0005, newest-sessions listing 0012, Agent write-access check 0023, delegation trip-wire 0028, absence-claim flag 0024/0007/0016, stop-gate protocol steps 0006, RESUME carry-over cost 0030). Item 2 is half covered by H2.
- D.U.M.B.A.S.S. config: OmniRoute gateway + compression, 4 memory arms (OB1/TB, mem0, code-review-graph, Graphify), Reasoning Bank, Continual Harness, retrieval planner (drafts in `recovered/2026-09-26-ob1/`); orchestration contract = AEsop-Xi PR #18.
- Layering: CLI, plugins, hooks, agents, workflow schema; modular but integrated; separate skill bundles.
- Cross Agent Auditor + intercept step + Success Rate Verification Grade; RLVR traces → training.
- Inference + execution interface (Hyperion-XI) and Æyre: build after the grill.

## Added 2026-10-08 (session 34c3e229)
- Decisions: the vault gets a `repos/` folder with live mirrors of the 6 base repos, replacing the MASTER-* files; `unresolved.md` retired into each repo's own PENDING.md; PDFs live only in `Merovingian's_keep/` unless no text version exists; "canon", POINTER.md and the `NovA-` prefix are removed whenever touched; session recaps + secrets go to the private repo `c10vis-poem/NvAEx-Recaps` (`nvaex-secret`, sops + age).
- Tools fixed or added: vault `tools/clean.py` + `tools/check.py` (run again, mutool installed, `type: condensed` handled), `.migrate/process_folder.py` + `build_rag_chunks.py` restored, `eson` CLI, `sops`, `age`, `mupdf-tools`.
- Hooks: Æsop-Xi `hooks/` (moved from `deploy/phone/hooks/`); `change-log.sh` records every change, `review-changes.sh` + "/ok push" gate every push.
- Corpus moves: 1,034 PDFs to the keep (12 left), NovA-Corpus condensed versions swapped in (17 docs; originals in `_salvage/NovA-Corpus/originals/`), `_quarantine/` to `vault-moved/`. Queue + reports: `~/.claude/session-work/2026-10-08/`.
- TOOL-INVENTORY.md (2026-10-06) predates all of the above.
- Observation review 2026-10-08 (NOT installed, staged for decision): `NovAExorpus/skill-updates/PENDING.md` + `skill-updates/2026-10-08/`: android-termux-operator update (obs 0004, 0009, 0025), CLAUDE.md additions A-E, 7 hook specs (`proposals/hooks-spec.md`), task-observer fix (0015; task-observer and honey are the operator's forks, fix there), `subagent-protocol` skill candidate (0023; one already exists in `c10vis-poem/NvAEx-agentk`). Review: `skill-observations/reviews/2026-10-08/REVIEW.md`.
- aesop-xi PR #18 (orchestration contract v0.1, https://github.com/c10vis-poem/Aesop-Xi/pull/18): a main grill job; left open on purpose. Its branch is 27 commits behind main and needs updating before merge (required secret-scan job).
- Wiki-admin tools added 2026-10-08: `tools/wiki_admin.py` (manifest with sha256 + size); vault `.migrate/` now complete (audit, dedup [runs git rm: operator approval], verify_corpus, build_rag_index + query_rag [pickle replaced by JSON, stdlib BM25], generate_jsonl_markers [independent cross-check for build_rag_chunks]). `convert_raw_to_markdown.py`: code not in the vault (only Drive "Open Tool" links); fetch from Drive.
- Two-by-two verification (operator, 2026-10-08), to orchestrate in the grill: converters A `clean.py` (MuPDF/mutool) and B LiteDoc (fork c10vis-poem/LiteDoc, sync to v3.3.0; CLI drives pdf.js via Playwright in the Debian proot); checkers X `check.py` (pypdf) and Y new `check2.py` (Poppler pdftotext). X checks A, Y checks B, then swapped; checker disagreement is flagged; a file is done only when both checkers pass the kept output; both checkers run the half-cut canary. Same pairing for chunks: `build_rag_chunks.py` vs `generate_jsonl_markers.py`. Also: `~/bin/anydoc` runs upstream `npx @firecrawl/anydoc`, not the fork `aesop-anydoc`: repoint.
- LiteDoc ready (2026-10-08): fork synced (v3.3.1 HEAD, CLI 3.3.0), installed from ~/repos/LiteDoc/cli into proot venv /root/venvs/litedoc + Playwright chromium; Termux command `litedoc` (~/bin/litedoc). Test: 8-page PDF, litedoc 2201 words vs mutool 2195, tables kept. Output: `-o FILE` for one input.
- Context-as-image (2026-10-08): Render MCP DROPPED (it is render.com hosting management, not rendering). Keep forks NvAEx-OmniGlyph + NvAEx-render-mcp-server as is. Direction: compression through OmniRoute (12 engines; `omniglyph` engine = Fable 5 only, direct Anthropic route only, experimental/off by default; RTK/Caveman/LLMLingua-2 for every model). Standalone OmniGlyph proxy and honey-px/pxpipe not pursued. Grill to decide: a vision plugin for other models (Gemini vision, QAI Hub vision models) via an adjusted OmniGlyph fork. Prereqs: OmniRoute clone cleanup (branch 9,302 ahead, 4 dirty files), run as service, direct Anthropic route, one measured before/after.
- Hooks H1-H8 review with the operator in the grill (README: ~/repos/Aesop-Xi/hooks/README.md).
