# P6 progress
## Plan
- [x] read BRIEF, work-order
- [x] hooks of all 13 plugins with hooks (all dirs renamed hooks.off-20261028)
- [x] read audit_staging.py, verify.py (full)
- [ ] check.py outline; read rag-evaluation, llm-secure-patterns, skill-gate (skills)
- [ ] write P6-checks-hooks.md
## Last action
2026-10-30: counted hooks: 13 plugins, 40 matcher groups, 43 commands (not 16). read-cache.js blocks Read (rule 8 conflict).
## Findings
- /security-review skill refused (cwd not a git repo); applying injection-quarantine by hand.
## Blocked
- none

## Update 2026-10-30 (after coordinator path correction)
- [x] read TOOLS.md, corpus-ingest.md in full; rag-evaluation bodies read in full
- [x] deliverable written: P6-checks-hooks.md (+ P6-hooks.json, P6-wa-hook.draft.sh, P6-guards.draft.py, P6-quarantine.draft.py)
- Not fully read: 5 llm-secure-patterns skill bodies, isolated_pipeline.py, check.py bulk (stated in md section 8)

## Update 3 (second pass): reading 5 llm-secure-patterns skills + isolated_pipeline.py in full
- [ ] agent-action-surface  [ ] llm-endpoint-hardening  [ ] output-validation  [ ] system-prompt-design  [ ] report  [ ] isolated_pipeline.py
- [ ] fold signals into quarantine draft, rerun 6-file test
- [ ] re-check citations, update md
- [x] agent-action-surface read in full (313 lines)
- [x] llm-endpoint-hardening read in full (368 lines; HTTP route auth/rate limit/denial-of-wallet; nothing for wiki)
- [x] output-validation read in full (363). Signal to add: md links with javascript:/data: scheme (SKILL.md:150-151)
- [x] system-prompt-design read in full (295). Signal to add: forged UNTRUSTED_* delimiter tags in a document (skill :104-105; sanitize_web_content.py:379-386)
- [x] report read in full (403): code-audit writer; cut. :85,:89,:309-311 say LLM04 data poisoning is NOT addressed by the plugin
- [x] isolated_pipeline.py read in full (620). Signals: forged UNTRUSTED_* tags (:316,:340), cred patterns AKIA/github_pat_/Bearer/password= (:367-374) missing from audit_staging.SECRETS. Concept: trusts_input_from stage rule (:96-101) -> P3 design rule, not code
- [x] quarantine draft updated (+forged-delimiter, script-link, exfil-image, mixed-script[Cyrillic only]); planted test: 10 files -> 9 flagged, benign clean; vault 555 -> see md
- [~] citation re-check: found cat -n numbering carried across concatenated files (verify.py, pointer_gate.py, lane_commons_gate.py, git-autocommit.sh, suggest-lint.sh); fixing
- [x] citations re-checked per file; fixed offsets in verify.py (-153), pointer_gate (-132), lane_commons_gate (-51), git-autocommit (-8), suggest-lint (-17), check.py PK/find_dirs, read-cache contextignore (301-305)
- [x] second pass DONE 2026-10-30. md: 1.2 verdicts full-read, section 5 signals+evidence, section 8 status
