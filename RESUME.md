Session files: [[AGENTS]] · [[PENDING]] · [[MEMORY]] · [[MAP]] · [[NAMING-CANON]] · [[BOARD-INTAKE]]

# RESUME.md: Session Ledger (rewritten every session)

Repository: NovÆxorpus (`c10vis-poem/NovAExorpus`, PUBLIC).
**Last session: 2026-11-05** (phone, session d984de02, Claude Code). Reviewed the Frankenstein build, recovered the skills-layout sources, and started redefining the JEV and REA servers.

## Read first, in full
1. This file, [[PENDING]], and `handoff/2026-11-05/README.md`.
2. Re-read [[AGENTS]] and [[MEMORY]] if the handoff says they changed.
3. Shared memory: `NvAEx-Recaps/memory/general.md`, then `memory/active/frankenstein.md`.
4. Phone notes: `~/.claude/session-work/2026-11-05/START-NEXT.md` and the write-ups it lists.

## NEXT SESSION: START HERE
1. **Review:** the operator goes item by item down Frankenstein-Review (Drive folder Frankenstein-Review-Pack) and says what to fix. Fix each, ask only to clarify. Then ship `frankenstein-v2` through a PR. First item fixed so far: nvaex-jev-core.
2. **Redefine the servers:** JEV (router and auditor) and REA (real Reverse Engineer Anything, own server) from the write-ups. Decide the capability card fields (11 vs 9).
3. **Build the missing sub-agent harness plugin:** directions, settings, hooks; task log before tool calls; stop hooks check it against real tool history; script enforces, Jev scores.
4. **Jev client fixes:** see JEV-sdk-notes.md (argmax, none_of_the_above, request id, Retry-After, fail closed on 401/403/422 in a tool gate).
5. **Skills layout:** test `claude plugin init` (Anthropic's answer on issue 18192), then `skills.json` pointers and the router.
6. **Plug in:** after the PR, install, clear stub hooks, test each rule live.

## STATE (verified 2026-11-05)
- **Nothing is installed or pushed.** Build is commit 23e7e9c plus 8e53eb3 on `frankenstein-v2` in `~/repos/.wt/novaexopia-frankenstein2`. Self-tests after the last changes: nvaex-jev-core 91, claw-mcp 163, nvaex-memory 41 passed, 0 failed. Other packages not rerun.
- **Hooks are stubs.** ship-session and subagent-stop-gate exit 0 (order of 2026-10-28). Only the corpus-ingest worker gate is live.
- **Settings:** main model sonnet, subagent default sonnet. The advisor is still on until the operator runs `/advisor off`.
- **Plugins:** 64 stock plugins on, mostly from the Nov 3 keep-list script. All 520 entries were off on Oct 31.
- **No TypeSafe key on the phone,** so real Jev has never answered. **TinyFish key** must be rotated (printed in a transcript).
- **Google two-account plugin** is on but its server is missing. Files shared from the second account can show up in nav searches; five files in Claude-skills-config did not.

## Decisions (operator, 2026-11-05)
- OB1, mem0 and OmniRoute were never dropped: reverse engineer all three; only running them stock is out.
- JEV is a router and an auditor. RLM comes out of Prime Agent into the operator's own package. pxpipe stays optional.
- The three-server limit was only a blueprint choice: use as many as needed. REA and JEV get separate servers, connected by the Pattern 02 card.
- Advisor mode declined. Sonnet by default, Haiku for plain lookups, Opus for builds.
- QAI Hub compiled models use QAIRT, GenieX and the HTP SDK; llama.cpp is only for the rest.
- `nvaex-memory-vnext` renamed `nvaex-memory`. Code graph is required in REA's loop, not optional.
- Full-read jobs go to corpus-ingest.

## Shipped
(filled at the end of wrap-up)

## SOURCES
Read: see `handoff/2026-11-05/README.md`. Not read: list there too.
