# Tools, Scripts, Hooks & Skills — Verified Inventory

Compiled 2026-09-10, by direct inspection (Read/Bash/find, not inferred from docs).
Every entry below was opened and confirmed to exist at the stated path — this is
not a summary of what a spec *says* should exist. Where a doc claims something
and reality disagrees, reality wins and the doc claim is noted as stale.

---

## 1. Skills

### Vendor skills (installed, connected)
| Skill | Where | Status |
|---|---|---|
| `honey` + 13 satellites (`honey-ccr`, `honey-chat`, `honey-compress`, `honey-debt`, `honey-design`, `honey-eco`, `honey-gain`, `honey-hive`, `honey-loop`, `honey-memory`, `honey-px`, `honey-review`, `honey-superpowers`) | `~/.claude/skills/honey*` | Active, plugin installed |
| `code-review-graph` (MCP, 30 tools) | MCP connector | Connected. Registered repos: `aesop-xi`, `NovA-terrestrial-brain` only — **not** `novae-xorpus` |
| `mem0` (MCP + plugin) | MCP connector + `~/.claude/skills/` | Connected. Live entities incl. `novaexorpus-corpus`, `novaexorpus-test` (created 2026-09-09) |
| `reverse-skill` / your fork `NoVa-reverse-skill` | `~/repos/NoVa-reverse-skill` | Not a Claude skill/MCP — a routing repo read via its own `AGENTS.md`/`RULES.md` when a reverse-engineering task starts |

### Project-specific skills (7, confirmed real, not filler)
| Skill | Location |
|---|---|
| `corpus-batch-processing` | `~/.claude/skills/corpus-batch-processing/SKILL.md` (global) |
| `corpus-verify` | `~/.claude/skills/corpus-verify/SKILL.md` (global) |
| `drive-to-obsidian-migration` | `~/repos/NovA-Corpus/.claude/skills/` |
| `openspec-apply-change` | `~/repos/NovA-terrestrial-brain/.claude/skills/` |
| `openspec-archive-change` | same repo |
| `openspec-explore` | same repo |
| `openspec-propose` | same repo |

### False leads — ruled out, don't re-chase
- `technical-builder-style` — real, but a Claude writing-style skill unrelated to this project. Canonical copy: `/storage/emulated/0/archive/technical-builder-style.SKILL.md`.
- `~/repos/novae-xorpus/skills-and-capabilities/{code-review-graph,notebook-lmpy,obsidian-skills}` — empty directories, placeholder only.
- ECC (`ecc:code-reviewer`, `ecc:planner`, etc.) — **intentionally uninstalled by the operator 2026-09-09.** Plugin removed, hooks stripped from `~/.claude/settings.json`, marketplace deregistered. Do not re-raise as a gap.

---

## 2. Tools / Scripts (25 total, confirmed by opening each file)

### `aesop-xi/tools/` + `novaexopia/tools/` (6 scripts — real, but **uncommitted**, SD-card only)
Not present in `~/repos/aesop-xi` or `~/repos/novaexopia` — only in the SD-card mirror
`/storage/emulated/0/Documents/NovÆxorpus/NovÆxorpus_Repo's/{aesop-xi,novaexopia}/tools/`.

| Script | What it does |
|---|---|
| `run_audit.sh` | "Incognito Red Auditor" daemon — watches `.incognito_red_sandbox/incoming/` for JSONL batches, validates, moves to `approved/`/`quarantined/`. This is the standalone red-auditor entity a prior session confirmed doesn't exist as a design — but the code exists anyway. |
| `divergence_detector.py` | Flags tool-bypass and protected-path violations; logs to `05_episodic_logs/divergence_incidents/` |
| `cross_auditor_orchestrator.py` | Ties `tool_call_interceptor` + `divergence_detector` + `nanoclaw_router` together, issues `ClearanceToken`s, SQLite audit ledger at `/tmp/novae_sqlite/audit_ledger.db` |
| `tool_call_interceptor.py` | Telemetry dashboard on `:8088`, intercepts tool calls, risk-scores them |
| `nanoclaw_router.py` | Routes prompts to hot-loaded skills/tools by keyword match; **hardcoded skill/tool registries are stale placeholders**, not the real skill list above |
| `htp_partition_calc.py` | Computes Snapdragon Hexagon NPU domain split (`D=HTP0,HTP1,...`) for models >3.5GB |

### `raw_database/tools/` (12 scripts — real, voice/agent-scaffolding, uncommitted)
`voice_bot.py`, `live_voice_loop.py`, `kokoro_tts.py`, `stt_test.sh`, `nanobot_from_scratch.py`,
`validate_repo_integrity.py`, `crawl_agent_vault.py`, `setup-aesop.sh`,
`gcp_cross_account_handshake.sh`, `scaffold_cognitive_repository_architecture.sh`,
`failures.sh`, `gemini-code-1777423316551.sh`, `gemini-code-1788194504002.sh`

### `.migrate/` pipeline (7 scripts — real, already synced via Drive_sync)
`Drive_sync/___Lex-Novi-Æxentis-Copiæ/.../SKILL.md/.migrate/`:
`process_folder.py`, `dedup.py`, `build_rag_chunks.py`, `build_rag_index.py`,
`query_rag.py`, `verify_corpus.py`, `audit.py` — the actual Drive→vault migration
pipeline the `drive-to-obsidian-migration` skill documents.

### Placed this session
- `~/repos/novaexopia/aesc/scripts/agent_panel.sh` — mobile workspace control panel (sync/log/grep menu). Pulled from Drive `3-FILES-MGMT16-SCRIPTS-(16-files)/`, placed 2026-09-10. Repo was genuinely empty before this.

### Known real gap — not yet found anywhere
- `system_housekeeper.sh` (named in `05_FEDERATED_FILE_TREE_TOPOLOGY_MASTER.md` as belonging in `novaexopia/aesc/scripts/`) — only a *patch fragment* to append to it was found (the Obsidian-vault-sweeper addendum, in Drive `OBSIDIAN /MARKOR-SWEEPER PATCH.TXT`). The base script itself has not been located. Don't assume it doesn't exist — check Drive/SD-card more before concluding that.

---

## 3. Hooks

**Every `hooks/` folder in all 8 federated repos is an empty `POINTER.md` stub** — confirmed by
`find` across the whole SD-card mirror (aesop-xi, horizons-ui, novae-xorpus, novaexopia,
novus-aesc, novus-aexenti, novus-aeyre, raw_database). This is real, not a placeholder-only
appearance — but a POINTER.md pointing to "Authority: 00-05" is a lead to follow, not a dead end:

- **The real git post-commit hook already exists and works**: `~/repos/aesop-xi/.git/hooks/post-commit`
  calls `~/novae-xorpus/tools/regenerate_masters.sh` after every commit. Functionally equivalent
  to (simpler than) the version `02_DUMBASS_UNIVERSAL_MEMORY_SPEC.md` §4 describes. Don't overwrite it.
- Installed Claude Code plugin hooks (the only other real hooks on this device): `honey` (active),
  `mem0` (active), `claude-video/watch` (installed). `ecc`'s cached hooks are stale/inert since
  ECC was uninstalled.

---

## 4. Verification notes — read before trusting anything copied to Drive today

A spot-check (2026-09-10) of the `NovÆxorpus_Repo's` → Google Drive mirror done this session
found it is **not always byte-perfect**:
- `aesop-xi/tools/cross_auditor_orchestrator.py`: local 5,955 bytes vs. uploaded 5,756 bytes —
  emoji (✓, 🚨) were swapped for ASCII (`[OK]`, `[DIVERGENCE DETECTED]`) when retyped. Logic identical.
- `aesop-xi/raw/AESOP XI Architecture Blueprint Update.md`: local 88,251 bytes vs. uploaded
  54,756 bytes — this one **was condensed/paraphrased**, not copied verbatim (page markers
  dropped, repeated phrasing tightened). If exact wording of that Gemini transcript matters,
  re-pull it from Drive `3-FILES-MGMT16-SCRIPTS-(16-files)/` or re-upload from the local file directly.

Only these 2 of the ~200+ uploaded files were checked. Treat the rest as unverified until spot-checked.

---

## 5. Where the real corpora actually live (don't re-derive this either)

- `~/repos/novae-xorpus` — **the real git repo**, canonical root, has docs 00-05 + `AGENTS.md`/`CLAUDE.md`/`NAMING-CANON.md`/`RESUME.md`.
- `~/novae-xorpus` — a **separate, diverged checkout** (different HEAD). Has its own `MASTER-CLAUDE.md`/`MASTER-RESUME.md`/`GRILL-MANIFEST.md`. Not reconciled with `~/repos/novae-xorpus` — flag to the operator before treating either as sole truth.
- `~/repos/novae-xorpus`'s own corpus pipeline: `01-sources/` → `02-clean/` → `03-check/`, via `tools/clean.py` + `tools/check.py`.
- SD-card `raw_database` (`/storage/emulated/0/Documents/NovÆxorpus/NovÆxorpus_Repo's/raw_database/`) — a **separate** corpus, `raw/` → `clean_md/`, 106→97 files as of last check. Different numbers from the repo's own pipeline — don't conflate the two.
- SD-card `NovÆxorpus_Repo's/` folder itself is a one-way content mirror (no `.git`) of the real repos, for apps (Obsidian, Gemini) that can't reach Termux's private storage. Last full local→Drive sync: 2026-09-10, this session (see §4 above for fidelity caveats).
</content>
