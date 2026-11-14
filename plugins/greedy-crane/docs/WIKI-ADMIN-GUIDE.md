---
title: Wiki Admin and Corpus Toolkit Guide
tags:
  - guide
  - wiki
  - setup
created: 2026-10-02
updated: 2026-10-02
---

# Wiki Admin and corpus toolkit — user guide

*Written 2026-10-02. Everything here was installed and checked on the phone that day unless marked **(open)** or **(not tested)**.*

**In one line:**
- **`wiki-admin`** starts the files-admin agent with every wiki, document and graph tool loaded.
- **The corpus vault** carries the skills that every session should have, on any device.
- **The global hooks (H1–H7)** apply everywhere, including in the `aesop-xi` repo itself.

---

## 1. The three layers (what loads where)

| Layer | Where it lives | Loads in | What's in it |
|---|---|---|---|
| **Global** | `~/.claude/` (user settings, user skills, user plugins) | every session on this phone, whatever folder | hooks H1–H7, your `CLAUDE.md` rules, Pocock skills, Honey, Happy Ending, mem0, task-observer, **graphify**, **Obsidian skills** |
| **Corpus vault** | `NovAExorpus/.claude/skills/` (and `commands/`, `agents/`) | every session that **has the vault attached**, on any device | **NotebookLM** skill, task-observer, debug-issue, explore-codebase, refactor-safely, review-changes, drive-to-obsidian-migration |
| **wiki-admin** | `~/wiki-admin/.claude/` | only sessions started with `wiki-admin` | obsidian-wiki, OpenWiki for Claude Code, wiki-compiler, `/llmwiki-*`, anydoc, NotebookLM |

**The rule that decides this** (checked in Claude Code's own docs, code.claude.com/docs/en/skills):
- An **attached** folder (`--add-dir`, which is how the vault rides along) loads its `.claude/skills/`, `.claude/commands/` and `.claude/agents/`.
- It does **not** load settings, plugins, hooks or MCP servers. Those load only from the folder you **start** in, or from your user settings.

So skills you want everywhere go in the vault. Plugins, hooks and MCP servers go user-wide or in a launch folder.

**aesop-xi (the orchestration repo):** its `.claude/settings.json` registers all of H1–H7. Any session started inside aesop-xi gets them on any device. On this phone the global copies already run, so the repo copies stand down and nothing fires twice (`deploy/phone/hooks/run-hook.sh`).

---

## 2. Starting the files admin

```
wiki-admin
```

- It opens Claude Code in `~/wiki-admin` with the vault attached. It loads everything global, plus the vault skills, plus the wiki toolkit.
- Pass extra flags after it, e.g. `wiki-admin --continue`.
- A normal `claude` anywhere else **does not** load the wiki toolkit. Checked 2026-10-02: the wiki plugins are on in `~/wiki-admin` and off in `~` and in aesop-xi.

---

## 3. Everything in the wiki-admin toolkit

| Tool | From your fork | Type | What you use |
|---|---|---|---|
| **obsidian-wiki**: 40 skills plus 3 agents, the main vault wiki | `AEsops-obsidian-wiki` | plugin | `/wiki-setup`, `/wiki-ingest`, `/wiki-query`, `/wiki-lint`, `/wiki-status`, `/wiki-dedup`, `/cross-linker`, `/tag-taxonomy`, `/wiki-dashboard`, `/wiki-export`, `/wiki-research`, `/wiki-synthesize`, `/claude-history-ingest`, `/wiki-stage-commit` … |
| **OpenWiki for Claude Code**: replaces OpenWiki outright | `NvAEx-openwiki-for-claude-code` | plugin | `/openwiki:generate`, `/openwiki:update`, `/openwiki:ask`, `/openwiki:schedule` |
| **wiki-compiler**: compiles loose markdown or code into topic pages, with a graph view | `llm-wiki-compiler-NvAEx` | plugin | its `wiki-init`, `wiki-compile`, `wiki-search`, `wiki-capture`… commands. Run them by full name (`/llm-wiki-compiler:wiki-compile`), because some names match obsidian-wiki's. |
| **LLM Wiki nocode**: approval-gated wiki | `NvAEx-llm-wiki-nocode` | commands | `/llmwiki-ingest`, `/llmwiki-query`, `/llmwiki-lint` |
| **anydoc**: Word, PowerPoint, Excel, ODF, RTF, EPUB, CSV, PDF → Markdown | `aesop-anydoc` | skill + `anydoc` command | `anydoc <file>` or `anydoc <file> -o out.md` |
| **NotebookLM** | `notebooklm-py` (v0.8.4) | skill + `notebooklm` command | see §5 |
| **graphify** (global) | `graphify` (v0.9.73) | skill + `graphify` command | `/graphify <path>`, `/graphify <path> --obsidian`, `/graphify query "…"` |
| **Obsidian skills** (global) | `obsidian-skills` (official, kepano) | plugin | load automatically for vault notes, bases, canvas and the Obsidian CLI |

### Same names, different tools
obsidian-wiki, LLM Wiki nocode and wiki-compiler all have ingest/query/lint. **They are different programs that write different page formats**, so each keeps its own wiki:
- **obsidian-wiki** writes the main wiki inside the vault (§4) and owns the plain `/wiki-*` names.
- **LLM Wiki nocode** writes into `~/wiki-admin/` (`raw/` → `wiki/`, with answers and lint fixes waiting in `*_pending/` until you move them to `*_approved/`). That folder is not in the vault, so GitSync doesn't back it up.
- **wiki-compiler:** use its full `/llm-wiki-compiler:…` names.

### OpenWiki without the MCP server
`/openwiki:*` reads and writes each repo's `openwiki/` folder with Claude's own file tools. It needs no MCP server, no `openwiki` command and no API key. It continues existing `openwiki/` folders instead of overwriting them.

---

## 4. One-time setup

1. **obsidian-wiki: point it at its vault folder.** Start `wiki-admin` and say `set up my wiki` (runs `/wiki-setup`, which writes a `.env` with `OBSIDIAN_VAULT_PATH`). **(open)** Decide: the vault root, or a subfolder such as `NovAExorpus/wiki/`. Optional extras live in the same `.env`:
   - `WIKI_STAGED_WRITES=true`: new pages wait in `_staging/` for review.
   - `OBSIDIAN_SOURCES_DIR=`: folders to ingest from.
2. **NotebookLM: log in once.** `notebooklm login` (your Google account), then `notebooklm auth check`.
3. **Retire the last OpenWiki files (yours to run, §7).**

---

## 5. Everyday commands

| You want to… | Type |
|---|---|
| Add a doc, folder, chat export or URL to the vault wiki | `/wiki-ingest <path or URL>` |
| Ask the vault wiki | `/wiki-query <question>` (say "quick answer" for the fast mode) |
| Wiki health check | `/wiki-lint`; `/wiki-lint --consolidate` fixes after a preview |
| Turn a Word/PDF/PowerPoint/Excel/EPUB into Markdown | `anydoc file.docx -o file.md` |
| Generate or refresh a repo's code docs | in that repo: `/openwiki:generate` the first time, `/openwiki:update` after |
| Ask a repo's docs | `/openwiki:ask <question>` |
| Knowledge graph of a folder | `/graphify <path>`; add `--obsidian` to write graph notes into a vault |
| NotebookLM notebooks, sources, chat, audio overviews | ask in plain words ("make a NotebookLM notebook from these PDFs"); the skill drives the `notebooklm` command (`--json`) |
| Approval-gated wiki | `/llmwiki-ingest raw/<file>.md` → `/llmwiki-query …` / `/llmwiki-lint` → move from `*_pending/` to `*_approved/` → `/llmwiki-ingest` |

---

## 6. Installed for later (not switched on)

### OmniGlyph: context as images (59–70% cheaper)
- **Fork:** `NvAEx-OmniGlyph` v1.4.0, built in `~/repos/NvAEx-OmniGlyph`.
- **Command:** `omniglyph` starts the proxy on `http://127.0.0.1:47821`, with its dashboard at that address.
- **Tested 2026-10-02:** the dashboard answered and the proxy logged 11 request events from a test session. A full reply through it wasn't captured. **Nothing is switched over.** No session uses it until you start one through it.
- **It is a proxy, not an MCP server.** To use it for one session:
  ```
  omniglyph &                                        # start the proxy
  ANTHROPIC_BASE_URL=http://127.0.0.1:47821 claude   # this session goes through it
  ```
- **Know before switching on:**
  - It compresses **Claude Fable 5** only by default (`OMNIGLYPH_MODELS`). Other models pass through untouched, with no savings.
  - Features that need a direct connection, **Remote Control** included, can disappear behind any proxy.
  - With a subscription it doesn't lower the bill; it stretches your usage limits about 2–3×.
- **(open) For every agent later:** either set `ANTHROPIC_BASE_URL` user-wide and run `omniglyph` as a background service, or turn on the `omniglyph` engine inside OmniRoute.
- Its own `bin/cli.js` exits silently on Termux, so `omniglyph` runs `dist/node.js` directly.

### Render MCP server
- **Fork:** `NvAEx-render-mcp-server`, cloned to `~/repos/NvAEx-render-mcp-server`. Not built or registered yet.
- It's Render's (render.com) official MCP server: it manages services, deploys, databases and logs on a Render account.
- **To hook up later:** it's written in Go and there's no Go toolchain on the phone yet. Install Go (`pkg install golang`), run `go build -o ~/bin/render-mcp-server .` in the clone, then `claude mcp add render -- ~/bin/render-mcp-server` with your `RENDER_API_KEY`. Follow the fork's README for the exact flags.

---

## 7. OpenWiki retirement

**Done 2026-10-02 (retirement complete):**
- The `openwiki` MCP server is removed from your user config.
- The `openwiki` command is uninstalled.
- The OpenWiki block is gone from the vault's `AGENTS.md`.

- `~/AGENTS.md` and `~/CLAUDE.md` deleted by the operator (backup in `$TMPDIR/ow`). Those two files held only the old OpenWiki block.

**Kept:**
- `~/repos/openwiki`, your fork of OpenWiki's source.
- Any repo's `openwiki/` docs folder.

**(open)**
- `~/.openwiki/` (1.1 GB, the old program's database) can be deleted.
- `~/openwiki` is a second clone of the same fork.

---

## 8. Keeping it updated (all from your forks)

```
gh repo sync c10vis-poem/<repo>          # fork ← upstream
git -C ~/repos/<repo> pull --ff-only     # clone ← fork
```

| Piece | After pulling |
|---|---|
| obsidian-wiki, OpenWiki for Claude Code, wiki-compiler | `claude plugin update <name>@<marketplace>`. Then, because the installed copies lose their Termux fixes on update: `grep -rl '^#!/usr/bin/env' ~/.claude/plugins/cache/<marketplace> \| xargs termux-fix-shebang` |
| graphify | `proot-distro login debian --bind "$HOME:$HOME" -- /root/venvs/graphify/bin/pip install --upgrade ~/repos/graphify`, then copy `graphify/skill.md` → `~/.claude/skills/graphify/SKILL.md` and `graphify/skills/claude/references/` → `~/.claude/skills/graphify/references/` |
| Obsidian skills, anydoc skill | linked to the clones, so a pull is enough |
| NotebookLM | `pip install --upgrade ~/repos/notebooklm-py`, and copy `SKILL.md` to `NovAExorpus/.claude/skills/notebooklm/` (the vault can't hold links) |
| `/llmwiki-*` | recopy from `NvAEx-llm-wiki-nocode/.claude/commands/` into `~/wiki-admin/.claude/commands/`, renaming `wiki-` → `llmwiki-` |
| OmniGlyph | in the clone: `npm install --no-save --no-package-lock --ignore-scripts --legacy-peer-deps typescript@5 esbuild@0.28 @types/node@20 @cloudflare/workers-types gpt-tokenizer@4 && node scripts/build.mjs` |

---

## 9. Where the pieces are

| Piece | Location |
|---|---|
| Launchers | `~/bin/wiki-admin`, `~/bin/anydoc`, `~/bin/omniglyph` |
| wiki-admin settings, commands, skills, rules | `~/wiki-admin/.claude/` (`settings.json`, `commands/`, `skills/`, `CLAUDE.md`) |
| LLM Wiki nocode content | `~/wiki-admin/raw/`, `wiki/`, `questions_*/`, `lint_*/` |
| Corpus-wide skills | `NovAExorpus/.claude/skills/` |
| aesop-xi hook wiring | `aesop-xi/.claude/settings.json`, `aesop-xi/deploy/phone/hooks/` |
| Fork clones | `~/repos/`: `AEsops-obsidian-wiki`, `NvAEx-openwiki-for-claude-code`, `llm-wiki-compiler-NvAEx`, `NvAEx-llm-wiki-nocode`, `aesop-anydoc`, `notebooklm-py`, `graphify`, `obsidian-skills`, `NvAEx-OmniGlyph`, `NvAEx-render-mcp-server` |

---

## 10. Open decisions

1. Where obsidian-wiki writes in the vault (§4).
2. Link `~/wiki-admin`'s memory to the main memory (Claude keeps memory per launch folder).
3. The Obsidian skills load twice: links in `~/.claude/skills/` plus the plugin. Remove the links?
4. OmniGlyph for every agent: user-wide proxy or the OmniRoute engine (§6).
5. Render MCP: install Go, build, add the API key (§6).
6. Delete `~/.openwiki/` (1.1 GB) and the duplicate `~/openwiki` clone (§7).

## Related
- [[NPU-SERVE-USER-GUIDE]]
- [[LOCAL-AI-GUIDE]]
