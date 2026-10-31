Session files: [[AGENTS]] · [[PENDING]] · [[MEMORY]] · [[MAP]] · [[NAMING-CANON]] · [[BOARD-INTAKE]]

# RESUME.md: Session Ledger (rewritten every session)

Repository: NovÆxorpus (`c10vis-poem/NovAExorpus`, PUBLIC). **(phone only)** paths live only on the phone.
**Last session: 2026-10-29 to 10-30** (phone, session 5fc2c8e1, Claude Code, Opus 5.5; wrapped 2026-10-31 in 07d9a60a). Built the wiki admin plugin **greedy-crane** in the vault and ran homework packets P1-P7 as `greedy-crane:corpus-ingest` workers. The 5-hour usage limit cut it off at 07:32 UTC on 10-30 with P1 and P3 unfinished.

## Read first
1. Shared memory (private): `NvAEx-Recaps/memory/general.md`, then `memory/active/wiki-admin.md` (decisions, work order, operator answers, stop-hook rule).
2. Homework folder **(phone only)**: `~/.claude/session-work/2026-10-29/wiki-admin-homework/`. `BRIEF.md`, `work-order.md`, `P*-paths.txt`, then each deliverable `P1..P7-*.md` and its `progress-P*.md`.
3. Plugin: `plugins/greedy-crane/` on branch `session-2026-10-29` (agents, docs, scripts, skills).

## NEXT SESSION: START HERE
1. **Finish P1** (intake/convert) second pass: read watch-video, add file:line cites, rewrite `P1-intake-convert.md` with read depth and the new findings in `progress-P1.md`.
2. **Finish P3** (fan-out) second pass, step 4: re-check every file:line cite in `P3-fan-out.md`.
3. **Worker stop check** (waiting on operator go): stop hook that fires only for `greedy-crane:corpus-ingest` workers; it compares files the worker opened with its paths list (skips media), requires the progress and deliverable files, switches off with an off-file or `WIKI_ADMIN_HOOKS=off`, gives up after N tries (obs 0051). Script in `plugins/greedy-crane/scripts/`. **Operator rule (2026-10-30):** the full-read requirement covers files the operator assigned. A worker stopped by the hook does nothing more unless the operator says so, and the operator's word overrides the hook. Make it subagent-specific now; the wiki admin agent will get similar stop hooks later.
4. **Operator questions:** name of the master compilation folder; wiki links as `[[page]]` or relative links.
5. **Final compile into greedy-crane:** wiki-admin agent definition, skills, workflows, scripts, and hooks that can be switched off. Inputs: P1-P7 deliverables. P6 drafts: `P6-hooks.json` (merged hooks, none block), `P6-quarantine.draft.py`, `P6-guards.draft.py`, `P6-wa-hook.draft.sh`.
6. **Vault fixes from P4:** 519 of 537 `02_wiki_md` pages are copies of clean files; `manifest.jsonl` hashes the clean file, not the raw source (rebuild); create `01-inbox/`; patch `audit_staging.py` so it accepts sources listed the work-order way, and add the AKIA, `github_pat_`, Bearer and `password=` patterns (P6).
7. **Older items** (from the 2026-10-28 ledger, not touched): Gemini key + `google-genai` + one live draft; E6/E10 schemas; re-engineer hooks before turning any on (resume-gate first, obs 0051); web view tool (adb pairing); STT OpenRouter MCP; mods; intake live run; Drive ingest wave 1 (10 of 21 batches); plugin cleanup. Details: `handoff/2026-10-28/README.md`, PENDING.md.

## STATE (verified 2026-10-31)
- Packets: **done** P2 (size gate), P4 (wiki core), P5 (extract skills/tools), P6 (checks and merged hooks), P7 (MCP). **Partial** P1, P3 (see above). No workers are running; they belonged to session 5fc2c8e1 and can't be resumed from a new session.
- P6 counted 43 hook commands in 13 plugins (40 matcher groups), not 16. Plugin hooks still sit in `hooks.off-20261028`. `read-cache.js` blocks Read (conflicts with work-order rule 8).
- Hooks: all Claude Code hooks are still exit-0 stubs (operator order 2026-10-28). `~/.claude/hooks/ship-session.sh` is disabled too, so shipping is by hand.
- Vault: branch `session-2026-10-29` (worktree `~/repos/.wt/vault-session`) holds greedy-crane plus this wrap-up. Phone main checkout still holds local commit 044d369 (already on main as #61); don't reset it.
- Observations new: 0052 (workers skip full reads on first pass; fix = read ledger checked before accepting a packet), 0053 (after /clear, asked instead of recovering).
- Secrets not stored: `GEMINI_API_KEY`, `OPENROUTER_API_KEY`.

## Operator rules restated 2026-10-28 (still in force)
- Put each build in the repo its layer names (map in shared memory); never put new builds in NvAEx-Recaps unasked.
- Check work against the source documents, not only the operator's words.
- Inventory what exists (packages, prior specs, branches) before building.
- No multiple-choice menus; approval is per item.
- Approval cards for new skills/tools go in a file, not chat (2026-10-29).

## SOURCES
Read in the wrap-up (2026-10-31): transcript tail of 5fc2c8e1 (10-30 03:00-07:33 UTC, operator and assistant text), all seven `progress-P*.md`, the homework folder listing, `memory/active/wiki-admin.md`, observation 0052, old RESUME.md, vault PENDING tail, git state of the vault and NvAEx-Recaps.
Not read: the P1-P7 deliverables themselves, `BRIEF.md`, `work-order.md`, greedy-crane files, the 140-200 file wiki-admin set.

## Operator dictation (2026-10-28, kept verbatim)
THESE'L TAKE A BACK SEAT UNTIL THESE HOOKS AND STOP GATES HAND OFF AND MERGING PROTOCOLS ARE ALL RE-ENGINEERED TO ACTUALLY WORK THEN AFTER THAT WE'RE GOING TO RE-ENGINEER THESE PLUGINS SO THAT THEY CAN ACTUALLY COEXIST 

FIRST I NEED YOU TO START WITH CREATING A DYNAMIC WORKFLOW AND YOU EITHER UTILIZE SPECIFIC SKILL OR YOU CAN CREATE ONE. WE CAN UTILIZE THE ANTHROPIC WORKFLOWS DYNAMIC WORKFLOWS LOGIC AND ARCHITECTURE PLANS. 
FIRST UPON FIRST TASK THERE NEEDS TO BE A PROMPT ENGINEERING SUB PROCESS. AT THIS POINT IT WOULD BE SOMEWHAT OF A FAN OUT PROCESS WHERE THE WORKPLACE DIRECTORIES AND RESUME,AGENTS PENDING MD ETC WILL BE RED AND STANDARD FASHION AND AN AGENT WILL SPIN UP LOWER LEVEL SUBAGENTS FOR ALL ORGANIZED EXECUTIONS AND ROUTING 

THE MAIN AGENT WILL CALL ON A JEV AND EVALUATE WHICH SKILLS SCRIPTS TOOLS OR ORCHESTRATION OR OUTPUT STYLE DEPENDING ON THE PROMPT 

  THE MAIN AGENT WILL PLAN A COURSE OF ACTION WHICH TOOLS SKILLS SCRIPTS AGENT CONFIGS ROUTING AVENUES AND TASK LISTS AND PROPOSE TO THE BUILDER, IT WILL ALSO RECOMMEND A DYNAMIC WORKFLOW, WORKSPACE MARKETPLACE, PRE XONFIGURED AGENT PACKAGE, QUERY SALASH EXECUTIONS MODEL ROUT, STRAIGHT EXECUTION ROUTE OR ANOTH6 REASONED COURSE OF ACTION.
 THIS WILL BE AUDITID BY A  SUBAGENT THE SAME WAY CLAUDES SUB AGENT TASK AUDITOR WORKFLOWS DO. EXCEPT THIS SUB AGENT WILL ALSO UTILIZE JEV SEE IF THERE WAS ANY ANGLES MISSED BY THE ORCHESTRATIONS AGENT 
 
THESE WILL BE GOVERNED NOT ONLY BY THE TASK AUDITING SUB AGENTS BUT BY STRICT STOP GATE HOOKS WRITTEN IN SETTINGS THESE SOFT HOOKS WILL NOT CONTAIN ANY OF THE FLAWS OF THESE PAST SHIT SHOW THE ENGINEERED CORRECTLY WITH THE BUILDERS SHUT OFF CAPABILITIES AND BUILT INTO THEM AND ANY CONFLICT THREATS OVERRIDES DESIGNED TO IGNORE ANY OUTSIDE THIRD PARTY OR ANTHROPIC REGARDLESS IF IT WASN'T PRE-COMPILED OR ADDED TO THE IMMEDIATE SESSIONS WORK ENVIRONMENT AS A SESSION MARKETPLACE OR AGENT PACKAGE OR SPECIFIC CUSTOMIZED WORKFLOW FOR THAT SESSION 

WE'LL ALSO DEVELOP A THOROUGH PROTOCOLS FOR GITHUB AND SESSION DATA LOGGING THE HOUSEKEEPING THROUGHOUT THE ENTERPRISE AND THE SESSION ROUNDUP WRAP UP THERE AND THE HOOKS AND SUB AGENT TASKING THAT'S INVOLVED WITH THIS. 

THIS IS JUST THE BASIC BEGINNER LEVEL WHEN WE REALLY GET INTO THIS THIS IS GOING TO CONSIST OF A LOT MORE THAN JUST SOME SMALL PRE-TASK PROMPT ENGINEERING THIS IS GOING TO ENTAIL COMPACTION FANNING OUT TO MULTIPLE DATA LAYERS HAVING MULTIPLE DATA STORAGE VECTORS CREATING A REVERSE ENGINEERING FLOW FOR ASSET PROCUREMENT AND DEPLOYMENT A LOT OF  JEV INVOLVEMENT IN ROUTING ENTIRELY REVERSE ENGINEERED COMPACTION ROUTING AND EPISODIC/STATIC MEMORY GOVERNING RECALL AS WELL AS WEB ACCESS INTERFACE ACCESS MODULAR AGENT PACKAGES AND DYNAMIC WORKFLOWS CONTINUAL HARNESS ASPECT FOR WORKFLOW IMPROVEMENTS MID-SESSION PROTOCOLS THAT CALL ON AND UTILIZE GRAPHIFY AND OBSIDIAN NOTEBOOK LM MIND RESOURCES THAT WE'VE REVERSE ENGINEERED MIND FOR REPOSITORIES THAT WE STRIPPED OF ASSETS AND TURNED INTO MARKETPLACES OUR OWN CUSTOM MCP ROUTING LAYERS. A RECURSIVE PIPELINE THROUGH REASONING BANK AND TASK OBSERVER ALL THE WAY TO THE CROSS AUDITOR M O E HOME NODE DESIGN TO THE RED AUDITOR AGENT CLOUD DESIGN ALL UTILIZING STOP HOOKS AND IN THE SETTINGS AND ORCHESTRATION STYLES SCRIPTS AND OUTPUT STYLE OPTIONS, SUB AGENT DATA COLLECTION AND LOGGING  SUB AGENT TASK AUDITING ETC 
BUT FOR NOW IT'S JUST GOING TO BE THE BASIC STUFF THE SESSION WILL JUST FOCUS ON GETTING THE HOOKS CONGRUENT AND ACTUALLY USABLE THE BASIC WORKFLOWS DOWN THE BASIC DYNAMIC WORKFLOW ADAPTATION CONFIGURED AND WILL START DISSECTING PLUGINS AND REPOSITORIES OUR OWN CUSTOM TOOLS AND SCRIPTS THAT ALREADY EXIST EVERYTHING THAT ANTHROPIC HAS ON ITS END AND START TO COMBINE CUSTOMIZED MCP PLUGINS AND AGENT CONFIGURATIONS AND SKILL PLUG-IN PACKAGES FOR DIFFERENT WORKFLOWS ETC ONCE WE GET GOOD AT THIS WE CAN START POINTING THESE CONFIGURATIONS AND AGENT PACKAGES AT THINGS LIKE THE LLM WIKI ADMIN AND THE ORCHESTRATIONS CEO AGENT ARE BOARD OF DIRECTORS THE ACTUAL GRILL SESSION MASTER SESSIONS PROJECTS WITH ALL OF ITS SESSION THREADS AND COMPILATION OF THE DUMBASS ITSELF AND THEN WE CAN GET TO OTHER THINGS LIKE REVERSE ENGINEERING DIFFERENT ASPECTS OF THE ASSETS THAT WE WANT THE APPS THAT WE WANT THE AGENT OPERATING SYSTEM THAT I WANT THE APKS WERE GOING TO BUILD THE CODING AGENT ITSELF AND THE CONFIGURATION OF THE HYBRIDIZED ON DEVICE ASSISTANT AGENT LOGIC AND ALL OF THAT 

SO YEAH ALL THAT OTHER BULLSHIT LITTLE MAMSEY PANSY HOUSEKEEPING SHIT THAT'S ALWAYS NEVER ENDING AND ALWAYS TAKES CLAUDE FOREVER TO END I'M GOING TO FIGURE OUT A WAY TO SYNCHRONIZE A BUNCH OF THAT SHIT AUTOMATE A BUNCH OF THAT SHIT AND SEND THAT OFF TO SOME LOWER LEVELS OF AGENTS DIFFERENT SOURCES THAT WE HAVE LIKE OPEN ROUTER AND GEMINI SPARK AND SHIT LIKE THAT SO THAT THESE CAN GET DONE CONGRUENTLY ALSO A PART OF THIS NEEDS TO BE AN ADVISOR MODE ALWAYS EVEN THE SUB AGENT PROCESSES NEED TO BE AN ADVISOR MODE AND THE SUB AGENTS NEED TO HAVE THEIR CASH PROMPT TTL'S SET TO 1 HOUR FOR A LONG TASKS 

AND IN A CERTAIN POINT WHEN WE GET FAR ENOUGH ALONG I WANT TO GET A GOOD AMOUNT OF DATA ACCUMULATED AND GOOD ENOUGH REASON TO RUN IT WE CAN STAGE EVERYTHING FOR A FABLE FIVE LIGHTNING SESSION AND THAT THING CAN GET LIKE TWO OR THREE DAYS WORTH OF WORK DONE AND AN HOUR I'VE SEEN IT HAPPEN BEFORE IT'S PRETTY REMARKABLE ESPECIALLY IF WE SET THE TABLE OF CORRECTLY I HAVE A LOT OF GOOD DOCUMENTS AND A LOT OF GOOD DIRECTIONS TO GO WITH A LOT OF DIFFERENT THINGS me
