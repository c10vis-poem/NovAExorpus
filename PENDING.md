# PENDING.md — NovAExorpus

Durable cross-session backlog. Not rewritten each session — items persist until resolved or explicitly dropped.

- **RESUME.md's "PHASES 1-4 COMPLETE" is wrong.** 585 files cleaned is nowhere near real scope — the two original source folders in `Drive_sync` total 5,000+ files. Needs correction and a real re-ingestion pass, not just a status-line fix.
- **Other 6 repos still POINTER.md stubs.** `novus-aexenti`, `NovAExopia`, `aesop-xi`, `horizons-ui`, `novus-aesc`, `novus-aeyre` haven't had their own ingestion pass — only `NovAExorpus` itself has real `clean_md`/`wiki_md` content.
- **`NovAExopia/horizons-ui/` was built from Document 05** (the nested-repo model), which is superseded now that RFMC (flat 8-repo model, `Drive_sync/LlmWiki/Repo-Files-Map-core/`) is the actual direction. Needs reconciling once the new standalone Horizons UI repo exists.
- **Terrestrial-brain backend location** — currently phone-local Postgres (works today via env vars in `.mcp.json`), migrating to self-hosted on the Jetson Orin Nano Super once the terminal-APK/Android-Local-Desktop work (next session) makes that device reachable and manageable.
- **QNN-QAIRT SDK (3035 files) and canvas-ui-main (416 files)** — sitting in `__RESUME.md/whatisit-/` on device, not yet ingested.
