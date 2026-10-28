Session files: [[AGENTS]] · [[PENDING]] · [[MEMORY]] · [[MAP]] · [[NAMING-CANON]] · [[BOARD-INTAKE]]

# RESUME.md: Session Ledger (rewritten every session)

Repository: NovÆxorpus (`c10vis-poem/NovAExorpus`, PUBLIC). Readable from any device, agent or account once synced. Paths marked **(phone only)** live only on the phone; their copies are in the private repo `c10vis-poem/NvAEx-Recaps` under `recaps/session-work/2026-10-28/`.
**Last session: 2026-10-28** (phone, session 5fc2c8e1, Claude Code, Opus 5.5). Built the intake prompt-engineering step, the web view tool, the wiki admin tools and agent, and the shared memory; turned every hook off by operator order. Full handoff: `handoff/2026-10-28/README.md`. Earlier sessions the same day (37dc78ed Drive ingest, 6a9c6cdb gate fixes, 5da28487 task-observer pin): `handoff/2026-10-28/earlier-sessions.md`.

## Read first
1. Shared memory (private): `NvAEx-Recaps/memory/general.md` (repo map, standing rules), then the one `memory/active/<project>.md` you are working on: `wiki-admin`, `intake-pipeline`, `webview-tool`, `mods`, `stt`.
2. `handoff/2026-10-28/README.md`: what was built, on which branch, what was tested.

## NEXT SESSION: START HERE
0. **Merge today's branches** (pushed with PRs at wrap-up, see Shipped below): Aesop-Xi `intake-skill`; NovAExopia `webview-and-mods` and `wiki-admin-tools`; NovusAExenti `wiki-admin`; NvAEx-Recaps `memory-as-skill`. After merge, pull on the phone.
1. **Wiki admin:** find the operator's full wiki-admin file set (140 to 200 files; about three quarters are its execution orders and the corpus designs; location not confirmed, best guess vault `__RESUME.md/__Builder-Guide_Directory-`, 264 files). Read it all and harvest its converting, ingesting, verifying and skill-extraction scripts into the wiki admin, customizing overlaps. Then the operator stores `GEMINI_API_KEY`, `google-genai` is installed, one live draft runs. Operator decides E6 (chunk schema) and E10 (frontmatter schema).
2. **Hooks:** re-engineer before turning any back on (operator order). Start with resume-gate, which looped on an unchanged file (observation 0051).
3. **Web view tool:** operator pairs wireless debugging, then `bash ~/repos/NovAExopia/mcp_connectors/webview/bin/webview-connect --adb 127.0.0.1:<port>`; finish the Chrome DevTools MCP fork build (`node scripts/post-build.ts`, blocked by the auto-mode safety classifier) and test its tool list.
4. **STT (CloviX-AEyre):** OpenRouter key (`nvaex-secret set OPENROUTER_API_KEY`), build the OpenRouter MCP fork (`~/repos/NovA-openrouter-mcp`, build blocked by the classifier), switch its speech-to-text default to `qwen/qwen3-asr-1.7b`.
5. **Mods** (spec `NovAExopia/mods/`): plugins panel with active/available count, agent-configs side panel, Obsidian-style config tree, context and cache-TTL gauge, browser choice cards with a prompt bar, Jev side panel.
6. **Intake pipeline:** install `skills/intake` after merge and run it on a real dictated prompt; then stages 1-4 (`Aesop-Xi/docs/intake-pipeline-spec.md`).
7. **Drive ingest wave 1 (session 37dc78ed):** 10 of 21 batches written; resume per `handoff/2026-10-28/earlier-sessions.md` (workflow script archived in NvAEx-Recaps `recaps/session-work/2026-10-28/workflows-37dc78ed/`). Remove the Check stage first (operator: "they just need to be read").
8. **Older open items:** plugin cleanup (one `manifest.jsonl`, chosen plugins as a flat folder); Ctrl-to-send check; `handoff/2026-10-24/README.md` deliverables; staged updates in `skill-updates/PENDING.md` (Hook specs, Upstream draft); the eight unrecorded items now in PENDING.md under 2026-10-28.

## STATE (verified 2026-10-28)
- **Hooks: all off.** Every Claude Code hook registered in `~/.claude/settings.json` is an exit-0 stub; originals sit beside them as `~/.claude/hooks/<name>.disabled-20261028` (links into `~/repos/Aesop-Xi/hooks/`). The Stop AUDITOR agent hook and task-observer's SessionStart entry were removed from settings.json (backup `~/.claude/settings.json.bak-20261028-hooksoff`). Only the gitleaks git hooks (`~/.config/git/hooks/`) still run. Plugin hooks were already off (`hooks.off-20261028`).
- **Auto-mode safety classifier** blocks running downloaded code (npm builds, starting MCP servers from forks). The operator runs those with `!` or adds a permission rule.
- **No adb device** paired; Chrome's DevTools socket is reachable only through adb.
- **Secrets not stored:** `OPENROUTER_API_KEY`, `GEMINI_API_KEY` (only `VAULT_DISPATCH_TOKEN` in `nvaex-secret list`).
- **Observations:** 0049 (repo map and decisions not loaded across projects), 0050 (build started without the existing package and prior spec), 0051 (resume-gate loop) new.
- Risks carried over: a claude.ai re-sync can restore plugin hooks in `synced/`; `~/CLAUDE.md` is stale and should point to `~/.agents/AGENTS.md`; lost observation `0045-read-token-limit-friction.md` (no header).

## Operator rules restated 2026-10-28
- Put each build in the repo its layer names (map in shared memory); never put new builds in NvAEx-Recaps unasked.
- Check work against the source documents, not only the operator's words.
- Inventory what exists (packages, prior specs, branches) before building.
- No multiple-choice menus; approval is per item.

## Shipped
(filled at the end of wrap-up)

## SOURCES
Read this session: listed in `handoff/2026-10-28/README.md` "Sources read this session". Not read: the 140-200 file wiki-admin set, Dynamic_workflow_guide and `_config` docs, PENDING.md "Open" in full.

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
