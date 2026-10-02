Session files: [[AGENTS]] · [[PENDING]] · [[MAP]] · [[GRILL-MANIFEST]] · [[NAMING-CANON]]

# RESUME.md — Session Ledger (rewritten every session)

Repository: NovÆxorpus (`c10vis-poem/NovAExorpus`, PUBLIC), the master wiki and vault.
**Last session: 2026-10-02** (phone, Claude Code, Opus 5.5, personal account). It covered the NPU server's vision path, the device cleanup, H1–H7 on aesop-xi, the wiki-admin toolkit and the OpenWiki retirement. Full ledger: `~/.claude/session-work/2026-10-02/SESSION-LOG.md`.

## NEXT SESSION — START HERE
The Stop gate requires a status for each numbered item: `resume-item <n> done|blocked "<evidence / what's needed>"`.

0. **FIRST: fix GitSync (stuck in a "remote changing" loop 2026-10-02; nothing since 04:38 reached GitHub) and push today's vault work.**
1. **Planning session in the wiki-admin agent.** Start it with `wiki-admin`. Activate the wiki toolkit (obsidian-wiki `/wiki-setup` once: decide where `OBSIDIAN_VAULT_PATH` points) and the LLM Wiki agent (`/llmwiki-*`). The operator runs the Pocock chain by typed slash command: `/setup-matt-pocock-skills` → `/grill-with-docs` → `/to-spec` → `/to-tickets` → `/implement`. Guide: `docs/WIKI-ADMIN-GUIDE.md`.
2. **Close the wiki-admin open decisions** (guide §10): memory link for `~/wiki-admin`; the Obsidian skills loading twice; OmniGlyph attach point (user-wide proxy vs OmniRoute engine); Render MCP build (Go + API key); delete `~/.openwiki/` (1.1 GB).
3. **Restart the NPU work one model at a time WITH the operator**, per `docs/NPU-FINDINGS-2026-10-02.md` §4. Reboot first and check the CPU clock caps. First add InternVL 2B: the X Elite bundle ran 27.5 tok/s here.
4. **Housekeeping (due since end of week):** roll up `_recaps/`, repo audit (unmerged branches), observation-log review (open: 0001, 0002, 0004–0009, 0012, 0015, 0016, 0019–0021; 0018 is an empty file), cloud billing, disk bloat (~22 GB: uv/npm caches, Gemma 12B and E2B copies; PENDING "afternoon").

## STATE (verified 2026-10-02)
- **Enforcement:** H1–H7 live user-wide on the phone *and* attached to aesop-xi (`.claude/settings.json` → `deploy/phone/hooks/run-hook.sh`; stands down where the global copy exists). Operator override = `#skip-enforce`, typed by the user only.
- **What loads where** (Claude Code docs, skills page): an attached folder (`--add-dir`, e.g. this vault) loads its `.claude/skills/`, `commands/` and `agents/` only, never its settings, plugins, hooks or MCP. Corpus-wide skills therefore go in `NovAExorpus/.claude/skills/` (as copies; shared storage can't hold links). NotebookLM is there now.
- **wiki-admin** (`~/bin/wiki-admin` → `~/wiki-admin` + vault attached):
  - Project-scope plugins: obsidian-wiki (fork AEsops-obsidian-wiki), OpenWiki for Claude Code (fork NvAEx-openwiki-for-claude-code), wiki-compiler (fork llm-wiki-compiler-NvAEx).
  - `/llmwiki-*` = the nocode commands with a prefix, so they don't clash with obsidian-wiki's `/wiki-*`.
  - anydoc (`~/bin/anydoc`, runs in the Debian proot); NotebookLM.
  - Global: graphify 0.9.73 (fork), Obsidian skills (fork), Pocock (25/35 skills load; the planning chain is typed-slash only).
  - Plugin scripts needed `termux-fix-shebang` on Termux. Redo it after plugin updates.
- **OpenWiki retired:** MCP removed, CLI uninstalled, vault `AGENTS.md` block removed. `~/AGENTS.md` and `~/CLAUDE.md` deleted by the operator (backup in `$TMPDIR/ow`).
- **NPU server** `npu-serve <name>` → `127.0.0.1:18181/v1`, GenieX v0.7.1. All 6 models accept images (OpenAI `image_url`). Decode on the clock-capped phone: smolvlm2 23 · internvl3.5-4b QAIRT ~16 (AI Hub 16.0–16.4) · gemma-4-e4b 9.7 · internvl3.5-8b 5.9 · qwen3.5 0.8B/2B ~3 (CPU-placed Q5_K weights). Guide: `docs/NPU-SERVE-USER-GUIDE.md`.
- **Installed for later, not on:** OmniGlyph proxy (`~/bin/omniglyph`, v1.4.0 from the fork; it's a proxy, not MCP; Fable 5 only by default); Render MCP fork cloned (render.com service management; needs Go).
- **Cleanup:** about 9 GB freed (byte-identical copies, `~/kokoro` JS package, Gemma E2B + MTP). Kokoro v1.1 deleted by mistake; v1.0 kept (the v1.1-zh card says it isn't a strict upgrade).

## DECISIONS 2026-10-02
- Wiki toolkit lives in a separate launch folder so normal sessions stay lean. Skills meant for every session go in the vault.
- Same-named skills: obsidian-wiki owns `/wiki-*`; nocode becomes `/llmwiki-*` with its own wiki tree in `~/wiki-admin`; wiki-compiler is used by its full plugin names.
- Cleanup rules: dedup by model identity (name/chip/version + inner weights + byte-diff count), not by whole-file hash; never cut the newer version; ambiguous assent ≠ approval of separate questions.
- Fix small defects in-session; "later" needs a named reason.
- Commands for the operator: `!` works only at the Claude Code prompt, one per line. For a plain terminal, give them without `!`.

## OPEN ITEMS, IN ORDER
1. The START HERE items above.
2. Ship (this wrap-up): aesop-xi `feat/npu-serve-model-switching` (7 commits, incl. 1627b3f hooks and 751fb79 docs) and the older `feat/stop-gate-resume-enforce` worktree branch.
3. Operator: `notebooklm login`.
4. npu-serve: tool calls, multi-image; Kokoro TTS script fix.
5. The grill-session agenda (unchanged): H5/H6 per-tool blocks, H7 auto-classifier, post-task flagging, keyword false triggers, Hermes/dsh/terrestrial-brain, OmniRoute config, PR #18, wiki agent home (now partly answered by wiki-admin).
6. Everything else in `PENDING.md`.

## HANDOFF SOURCES
Read this session (post-compaction):
- Code and config: `~/tools/geniex-serve/{shim.c,server.py,models.json}`, `geniex-v0.7.1.h` (VLM sections), GenieX `cli/cmd/geniex/infer.go` (inferVLM), `docs/en/models/supported.mdx` (local bundle), `~/bin/npu-serve`.
- Repos and toolkit: aesop-xi hook files and settings, every SKILL.md of the OpenWiki plugin, obsidian-wiki ingest/query/lint (first ~45 lines each), `.env.example`, `SETUP.md`, the llm-wiki-nocode BOOTSTRAP / CLAUDE / commands, anydoc and NotebookLM SKILL.md, the wiki-compiler hooks, OmniGlyph README sections + package.json + build script, Claude Code docs (skills page, add-dir section).
- State files: vault RESUME.md, PENDING.md, `docs/NPU-FINDINGS-2026-10-02.md`, `LOCAL-AI-GUIDE.md` (to line 160), `ENFORCEMENTS.md`, hooks README, `WRAP-UP.md`, memory files edited, the GitSync state.

Not read: the full obsidian-wiki skills (40) and docs, the Render MCP README, OmniGlyph docs beyond the README, wiki-compiler commands, the rest of aesop-xi `CLAUDE.md`, vault docs 00–05.
