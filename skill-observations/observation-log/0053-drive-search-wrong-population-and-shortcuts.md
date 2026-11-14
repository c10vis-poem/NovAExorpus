---
id: 53
title: "Drive search: filtered on the wrong date field, missed shortcuts, brute-forced listings and searched piecemeal instead of one full query then a cheap filter"
status: open
type: open-source
skill: [drive-find, drive-to-obsidian-migration]
proposes_skill: []
target_file: []
siblings_checked: "no family registry entry; checked drive-to-obsidian-migration (same Drive intake job) and added it; corpus-batch-processing excluded: it starts after files are local"
area: "Drive intake: population selection and search method"
date: 2026-11-03
session_context: "Phone session, Claude Code: operator asked to count and read files shared to the business Drive in the past week, then to find a specific multi-day failure log"
parked_until:
resolved:
resolution:
reference: "~/.claude/session-work/2026-11-03/FAILURE-2026-11-03-drive-read.md"
commands_verified: "run: rclone backend query biz: (non-folder, non-shortcut, modifiedTime > date) returned 6,352 files in one call; run: mcp search_files mimeType = shortcut + modifiedTime returned the operator's 60 new shortcuts"
---

**Issue:** "Recently shared" was read as files' modified date, not share date; the operator shares by adding shortcuts to folders, which no search covered, so the agent reported the folders "not visible". It then ran full recursive listings (34,000+ files, timeouts) and later hunted for one document with one-at-a-time title searches. A parallel worker found the document in minutes with one server-side query of every file in the date window, a local name filter over a wide word list, and full reads of only the shortlist.

**Suggested improvement:** drive-find (now written, knowledge only) states shortcuts, sharedWithMeTime and the two accounts. Add to the Drive intake stage of the ingest worker's TOOLS.md: "1 query that returns the whole candidate population, 2 cheap local filter, 3 read the shortlist, 4 prove the match with quotes; never walk folder trees first".

**Principle:** Get the complete candidate list in one cheap query before reading anything; narrow by filtering, never by guessing search terms one at a time.
