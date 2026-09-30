---
title: State of the Union — 2026-07-27
---

# State of the Union — 2026-07-27

## Active Projects

### Horizons (Android App)
**Status: HomeGrid UI complete, backend routing next.**

HomeGrid v5 finished — layout, typography, starfield, colors validated on device. Commit `984b061` on `claude/homegrid-v5-tuned` (PR #31).

Key decisions: static font instances (Orbitron 800, Google Sans Code 400), plain O (no Ø — missing glyph), dp not sp for brand type, V5 colors inline in HomeGrid.kt.

Startup crash fix pushed (Breadcrumb.kt tail-window read) — not confirmed on device.

**Next:** Backend router for on-device agent. Kotlin-accessible llama.cpp hitting HTP through app vendor libs.

### Aesop (Deploy Stack)
**Status: Termux daemons operational, architecture documented.**

llamad (8081) + aesopd (8765) under runit. Gemma 4 12B Q4_0 production model. Critical correction landed: Termux cannot reach Hexagon DSP.

### OpenWiki (Documentation CLI)
**Status: Fork with custom features.** `openwiki/SKILL.md` convention is the defining feature.

### notebooklm-py
**Status: Active.** Async Python client for Google NotebookLM batchexecute RPC.

## Architecture

```
┌─────────────────────────────────────────────┐
│                Snapdragon 8 Elite            │
│  ┌──────────────────┐  ┌─────────────────┐  │
│  │   Horizons App   │  │     Termux      │  │
│  │  :8080 ort_engine │  │  :8081 llamad   │  │
│  │  :8091 media      │  │  :8765 aesopd   │  │
│  └────────┬─────────┘  └────────┬────────┘  │
│           └── 127.0.0.1 ────────┘            │
└─────────────────────────────────────────────┘
```

## Skills Inventory

| Skill | Type |
|-------|------|
| termux-helper | Utility — Termux ops |
| memory-as-skill | Utility — session memory |
| horizons-wiki | Project wiki |
| aesop-wiki | Project wiki |

**Convention:** `<project>-wiki` for project-specific, descriptive name for cross-project utilities. Project wikis reference utility skills, never duplicate.

## Lessons Learned

1. Variable fonts + Compose = pain. Cut static instances with fontTools.
2. Missing glyphs fail silently — Android substitutes a fallback face per character.
3. build-apk.yml on `branches: '**'` + shared release tag = clobber.
4. Always `git branch -a` — the active branch may not be main.
5. dp not sp for brand type — device font-scale clips oversized sp.
6. Termux + Hexagon = impossible. Route through the app.