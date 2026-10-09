# Staged updates manifest
Producer: weekly review 2026-10-08 (dispatched worker, subagent item4). Nothing installed. Root $V/PENDING.md is a different file.

## android-termux-operator -> skill-updates/2026-10-08/android-termux-operator/ (user-owned, category a; install = copy over ~/.claude/skills/android-termux-operator)
- obs 0004 -> Safety -> redact secrets when inspecting config (sed command NOT RUN)
- obs 0025 -> Safety -> operator-shell fit, fail closed on empty secret
- obs 0009 -> Safety -> edit only verified-false lines; handoff note is not authorisation
No .skill bundle packed (worker run, no packer step); install by directory copy.

## ~/.claude/CLAUDE.md additions -> skill-updates/2026-10-08/claude-md/CLAUDE.md.additions.md (paste by hand)
- A absence claims (0007, 0016, 0024, 0008-pt3); B subagent progress-file writer + delegation (0023, 0028); C auto-merge preflight (0026); D long-CI preflight (0027); E durable-not-scratchpad (0008)

## Hook specs -> skill-updates/2026-10-08/proposals/hooks-spec.md (design only; operator decides which to build)
- 0017, 0005, 0012, 0023, 0028, 0024, 0006

## Upstream draft -> skill-updates/2026-10-08/proposals/task-observer-upstream.md (0015; not sent)
