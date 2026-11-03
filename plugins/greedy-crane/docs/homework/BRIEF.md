# Wiki-admin homework: shared brief (all packets)

Read `work-order.md` in this folder first, in full. It is your task. Sections 6 (rules) and "What every packet hands back" are binding. Your packet is in section 7.

Context the work order lacks (operator, 2026-10-29):
- Wiki-admin is an AGENT PACKAGE (modular, launchable from anywhere), normally launched from the corpus (vault) worktree in the local terminal. It is not only a merged plugin. Judge each part by what that agent needs.
- The corpus and the wiki both live in the vault: /storage/emulated/0/Documents/NovAExorpus (GitHub c10vis-poem/NovAExorpus). Search starts local.
- The wiki admin directs extraction; it does not have to run on Gemini. It needs reach: web tools, Google Cloud projects, frontier apps, the Gemini app and Spark agents.
- A first build exists; reuse it, don't redo it: scripts ~/repos/.wt/novaexopia-wiki/tools/wiki-admin/ (convert_raw_to_md, verify, manifest, gemini_infer, audit_staging, promote), skills ~/repos/.wt/novaexopia-wiki/skills/wiki-admin-core/, agent ~/repos/NovusAExenti/executor-core/file-administrator/.
- Read plugins from the LOCAL paths in your `P<n>-paths.txt`, not GitHub. Repos are cloned under ~/repos.
- `extraction-index.txt` lists 274 existing extraction scripts and skills across the vault and repos. Before proposing any new script, check it for one that already does the job, and name it.

Equipment: load these skills with the Skill tool before reading: `honey-superpowers` (terse output), `corpus-verify` (check claims against sources). For huge files use `honey-px` or read by outline. Plus the packet-specific tools in your prompt.

Progress file (mandatory): write `progress-P<n>.md` in this folder FIRST, before any reading, with `## Plan` (checkboxes), `## Last action` (timestamp + what), `## Findings`, `## Blocked`. Update it after every step.

Deliverable: `P<n>-<name>.md` in this folder. No installs, no pushes, no edits outside this folder. Cite file:line for every claim and say full read vs description only.
