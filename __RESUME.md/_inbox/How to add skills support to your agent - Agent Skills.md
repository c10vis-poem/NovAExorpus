<!-- Converted from How to add skills support to your agent - Agent Skills.pdf — 13 pages -->

## Page 1

## AgentSkills
For client implementors How to add skills support to your agent
For client implementors
## Howtoaddskillssupportto
Copy page
## youragent
A guide for adding Agent Skills support to an AI agent or development tool.
This guide walks through how to add Agent Skills support to an AI agent or development
tool. It covers the full lifecycle: discovering skills, telling the model about them, loading their
content into context, and keeping that content effective over time.
The core integration is the same regardless of your agentʼs architecture. The implementation
details vary based on two factors:
Where do skills live? A locally-running agent can scan the userʼs filesystem for skill
directories. A cloud-hosted or sandboxed agent will need an alternative discovery
mechanism — an API, a remote registry, or bundled assets.
How does the model access skill content? If the model has file-reading capabilities, it
can read SKILL.md files directly. Otherwise, youʼll provide a dedicated tool or inject
skill content into the prompt programmatically.
The guide notes where these differences matter. You donʼt need to support every scenario
— follow the path that fits your agent.
Prerequisites: Familiarity with the Agent Skills specification, which defines the SKILL.md
file format, frontmatter fields, and directory conventions.
## Thecoreprinciple: progressivedisclosure
Every skills-compatible agent follows the same three-tier loading strategy:

---

## Page 2

| Agent Tier Skills What ʼ s loaded |  | When | Token cost |
|---|---|---|---|
| 1. Catalog | Name + description | Session start | ~50-100 tokens per skill |
| 2. Instructions | Full SKILL . md body | When the skill is activated | <5000 tokens |
  
      
( recommended
3. Resources Scripts, references, When the instructions Varies assets reference them
The model sees the catalog from the start, so it knows what skills are available. When it
decides a skill is relevant, it loads the full instructions. If those instructions reference
supporting files, the model loads them individually as needed.
This keeps the base context small while giving the model access to specialized knowledge
on demand. An agent with 20 installed skills doesnʼt pay the token cost of 20 full instruction
sets upfront — only the ones actually used in a given conversation.
### Step1: Discoverskills
At session startup, find all available skills and load their metadata.
### Wheretoscan
Which directories you scan depends on your agentʼs environment. Most locally-running
agents scan at least two scopes:
Project-level (relative to the working directory): Skills specific to a project or repository.
User-level (relative to the home directory): Skills available across all projects for a given
user.
Other scopes are possible too — for example, organization-wide skills deployed by an
admin, or skills bundled with the agent itself. The right set of scopes depends on your
agentʼs deployment model.
Within each scope, consider scanning both a client-specific directory and the
.agents/skills/ convention:

---

## Page 3

| Agent Scope Skills | Path | Purpose |
|---|---|---|
| Project | < project >/.<y our - client >/ skills / | Your client ʼ s native location |
| Project | < project >/. agents / skills / | Cross - client interoperability |
| User | ~/.<y our - client >/ skills / | Your client ʼ s native location |
| User | ~/. agents / skills / | Cross - client interoperability |
 
   
  
   
  
# The .agents/skills/ paths have emerged as a widely-adopted convention for cross-
# client skill sharing. While the Agent Skills specification does not mandate where skill
# directories live (it only defines what goes inside them), scanning .agents/skills/ means
# skills installed by other compliant clients are automatically visible to yours, and vice versa.
Some implementations also scan .claude/skills/ (both project-level and user-level) for pragmatic compatibility, since many existing skills are installed there. Other additional locations include ancestor directories up to the git root (useful for monorepos), XDG config directories, and user-configured paths.
# Whattoscanfor
# Within each skills directory, look for subdirectories containing a file named exactly
SKILL.md :
~/.agents/skills/
├── pdf-processing/
| │ ├── SKILL . md |  | ← discovered |
|---|---|---|
| │ └── scripts / |  |  |
| │ | └── e x tract . p y |  |
├──   data - anal y sis /
│   └──   SKILL . md   ←   discovered
└──   README . md   ←   ignored
# Practical scanning rules:
# Skip directories that wonʼt contain skills, such as .git/ and node_modules/

---

## Page 4

Optionally respect .gitignore to avoid scanning build artifacts
## AgentSkills
Set reasonable bounds (e.g., max depth of 4-6 levels, max 2000 directories) to prevent
runaway scanning in large directory trees
## Handlingnamecollisions
When two skills share the same name , apply a deterministic precedence rule.
The universal convention across existing implementations: project-level skills override user-
level skills.
Within the same scope (e.g., two skills named code-review found under both
<project>/.agents/skills/ and <project>/.<your-client>/skills/ ), either first-found
or last-found is acceptable — pick one and be consistent. Log a warning when a collision
occurs so the user knows a skill was shadowed.
## Trustconsiderations
Project-level skills come from the repository being worked on, which may be untrusted (e.g.,
a freshly cloned open-source project). Consider gating project-level skill loading on a trust
check — only load them if the user has marked the project folder as trusted. This prevents
untrusted repositories from silently injecting instructions into the agentʼs context.
## Cloud-hostedandsandboxedagents
If your agent runs in a container or on a remote server, it wonʼt have access to the userʼs
local filesystem. Discovery needs to work differently depending on the skill scope:
Project-level skills are often the easiest case. If the agent operates on a cloned
repository (even inside a sandbox), project-level skills travel with the code and can be
scanned from the repoʼs directory tree.
User-level and organization-level skills donʼt exist in the sandbox. Youʼll need to
provision them from an external source — for example, cloning a configuration
repository, accepting skill URLs or packages through your agentʼs settings, or letting
users upload skill directories through a web UI.

---

## Page 5

Built-in skills can be packaged as static assets within the agentʼs deployment artifact,
## AgentmakingSkillsthem available in every session without external fetching.
Once skills are available to the agent, the rest of the lifecycle — parsing, disclosure,
activation — works the same.
### Step2: Parse SKILL.md files
For each discovered SKILL.md , extract the metadata and body content.
### Frontmatterextraction
A SKILL.md file has two parts: YAML frontmatter between --- delimiters, and a
markdown body after the closing delimiter. To parse:
1. Find the opening --- at the start of the file and the closing --- after it.
2. Parse the YAML block between them. Extract name and description (required), plus
any optional fields.
3. Everything after the closing --- , trimmed, is the skillʼs body content.
See the specification for the full set of frontmatter fields and their constraints.
### HandlingmalformedYAML
Skill files authored for other clients may contain technically invalid YAML that their parsers
happen to accept. The most common issue is unquoted values containing colons:
# Technically invalid YAML — the colon breaks parsing description: Use this skill when: the user asks about PDFs
Consider a fallback that wraps such values in quotes or converts them to YAML block
scalars before retrying. This improves cross-client compatibility at minimal cost.
### Lenientvalidation

---

## Page 6

Warn on issues but still load the skill when possible:
### AgentSkills
Name doesnʼt match the parent directory name → warn, load anyway
Name exceeds 64 characters → warn, load anyway
Description is missing or empty → skip the skill (a description is essential for
disclosure), log the error
YAML is completely unparseable → skip the skill, log the error
Record diagnostics so they can be surfaced to the user (in a debug command, log file, or
UI), but donʼt block skill loading on cosmetic issues.
The specification defines strict constraints on the name field (matching the parent directory, character set, max length). The lenient approach above deliberately relaxes these to improve compatibility with skills authored for other clients.
### Whattostore
At minimum, each skill record needs three fields:
| Field | Description |
|---|---|
| name | From frontmatter |
| description | From frontmatter |
| location | Absolute path to the SKILL . md file |
Field Description
name From frontmatter
description From frontmatter
   
Store these in an in-memory map keyed by name for fast lookup during activation.
You can also store the body (the markdown content after the frontmatter) at discovery time,
or read it from location at activation time. Storing it makes activation faster; reading it at
activation time uses less memory in aggregate and picks up changes to skill files between
activations.
The skillʼs base directory (the parent directory of location ) is needed later to resolve
relative paths and enumerate bundled resources — derive it from location when needed.

---

## Page 7

## Step3: Discloseavailableskillstothemodel
## AgentSkills
Tell the model what skills exist without loading their full content. This is tier 1 of progressive
disclosure.
## Buildingtheskillcatalog
For each discovered skill, include name , description , and optionally location (the path
to the SKILL.md file) in whatever structured format suits your stack — XML, JSON, or a
bulleted list all work:
<available_skills> <skill> <name>pdf-processing</name> <description>Extract PDF text, fill forms, merge files. Use when handling PDF <location>/home/user/.agents/skills/pdf-processing/SKILL.md</location> </skill> <skill> <name>data-analysis</name> <description>Analyze datasets, generate charts, and create summary reports.</ <location>/home/user/project/.agents/skills/data-analysis/SKILL.md</location> </skill> </available_skills>
The location field serves two purposes: it enables file-read activation (see Step 4), and it
gives the model a base path for resolving relative references in the skill body (like
scripts/evaluate.py ). If your dedicated activation tool provides the skill directory path in
its result (see Structured wrapping in Step 4), you can omit location from the catalog.
Otherwise, include it.
Each skill adds roughly 50-100 tokens to the catalog. Even with dozens of skills installed, the
catalog remains compact.
## Wheretoplacethecatalog
Two approaches are common:

---

## Page 8

System prompt section: Add the catalog as a labeled section in the system prompt,
## Agentpreceded bySkillsbrief instructions on how to use skills. This is the simplest approach and works
with any model that has access to a file-reading tool.
Tool description: Embed the catalog in the description of a dedicated skill-activation tool
(see Step 4). This keeps the system prompt clean and naturally couples discovery with
activation.
Both work. System prompt placement is simpler and more broadly compatible; tool
description embedding is cleaner when you have a dedicated activation tool.
### Behavioralinstructions
Include a short instruction block alongside the catalog telling the model how and when to
use skills. The wording depends on which activation mechanism you support (see Step 4):
If the model activates skills by reading files:
The following skills provide specialized instructions for specific tasks. When a task matches a skill's description, use your file-read tool to load the SKILL.md at the listed location before proceeding. When a skill references relative paths, resolve them against the skill's directory (the parent of SKILL.md) and use absolute paths in tool calls.
If the model activates skills via a dedicated tool:
The following skills provide specialized instructions for specific tasks. When a task matches a skill's description, call the activate_skill tool with the skill's name to load its full instructions.
Keep these instructions concise. The goal is to tell the model that skills exist and how to load
them — the skill content itself provides the detailed instructions once loaded.
### Filtering

---

## Page 9

Some skills should be excluded from the catalog. Common reasons:
## AgentSkills
The user has disabled the skill in settings
A permission system denies access to the skill
The skill has opted out of model-driven activation (e.g., via a disable-model-
invocation flag)
Hide filtered skills entirely from the catalog rather than listing them and blocking at
activation time. This prevents the model from wasting turns attempting to load skills it canʼt
use.
## Whennoskillsareavailable
If no skills are discovered, omit the catalog and behavioral instructions entirely. Donʼt show
an empty <available_skills/> block or register a skill tool with no valid options — this
would confuse the model.
## Step4: Activateskills
When the model or user selects a skill, deliver the full instructions into the conversation
context. This is tier 2 of progressive disclosure.
## Model-drivenactivation
Most implementations rely on the modelʼs own judgment as the activation mechanism, rather
than implementing harness-side trigger matching or keyword detection. The model reads
the catalog (from Step 3), decides a skill is relevant to the current task, and loads it.
Two implementation patterns:
File-read activation: The model calls its standard file-read tool with the SKILL.md path
from the catalog. No special infrastructure needed — the agentʼs existing file-reading
capability is sufficient. The model receives the file content as a tool result. This is the
simplest approach when the model has file access.

---

## Page 10

Dedicated tool activation: Register a tool (e.g., activate_skill ) that takes a skill name
## Agentand returnsSkillsthe content. This is required when the model canʼt read files directly, and
optional (but useful) even when it can. Advantages over raw file reads:
Control what content is returned — e.g., strip YAML frontmatter or preserve it (see What
the model receives below)
Wrap content in structured tags for identification during context management
List bundled resources (e.g., references/* ) alongside the instructions
Enforce permissions or prompt for user consent
Track activation for analytics
If you use a dedicated activation tool, constrain the name parameter to the set of valid skill names (e.g., as an enum in the tool schema). This prevents the model from hallucinating nonexistent skill names. If no skills are available, donʼt register the tool at all.
### User-explicitactivation
Users should also be able to activate skills directly, without waiting for the model to decide.
The most common pattern is a slash command or mention syntax ( /skill-name or
$skill-name ) that the harness intercepts. The specific syntax is up to you — the key idea
is that the harness handles the lookup and injection, so the model receives skill content
without needing to take an activation action itself.
An autocomplete widget (listing available skills as the user types) can also make this
discoverable.
### Whatthemodelreceives
When a skill is activated, the model receives the skillʼs instructions. Two options for what
exactly that content looks like:
Full file: The model sees the entire SKILL.md including YAML frontmatter. This is the
natural outcome with file-read activation, where the model reads the raw file. Itʼs also a valid
choice for dedicated tools. The frontmatter may contain fields useful at activation time — for

---

## Page 11

example, compatibility notes environment requirements that could inform how the model
## Agentexecutes theSkillsskillʼs instructions.
Body only (frontmatter stripped): The harness parses and removes the YAML frontmatter,
returning only the markdown instructions. Among existing implementations with dedicated
activation tools, most take this approach — stripping the frontmatter after extracting name
and description during discovery.
Both approaches work in practice.
## Structuredwrapping
If you use a dedicated activation tool, consider wrapping skill content in identifying tags. For
example:
<skill_content name="pdf-processing"> # PDF Processing
## When to use this skill Use this skill when the user needs to work with PDF files...
[rest of SKILL.md body]
Skill directory: /home/user/.agents/skills/pdf-processing Relative paths in this skill are relative to the skill directory.
<skill_resources> <file>scripts/extract.py</file> <file>scripts/merge.py</file> <file>references/pdf-spec-summary.md</file> </skill_resources> </skill_content>
This has practical benefits:
The model can clearly distinguish skill instructions from other conversation content
The harness can identify skill content during context compaction (Step 5)

---

## Page 12

Bundled resources are surfaced to the model without being eagerly loaded
## AgentSkills
## Listingbundledresources
When a dedicated activation tool returns skill content, it can also enumerate supporting files
(scripts, references, assets) in the skill directory — but it should not eagerly read them. The
model loads specific files on demand using its file-read tools when the skillʼs instructions
reference them.
For large skill directories, consider capping the listing and noting that it may be incomplete.
## Permissionallowlisting
If your agent has a permission system that gates file access, allowlist skill directories so the
model can read bundled resources without triggering user confirmation prompts. Without
this, every reference to a bundled script or reference file results in a permission dialog,
breaking the flow for skills that include resources beyond the SKILL.md itself.
## Step5: Manageskillcontextovertime
Once skill instructions are in the conversation context, keep them effective for the duration
of the session.
## Protectskillcontentfromcontextcompaction
If your agent truncates or summarizes older messages when the context window fills up,
exempt skill content from pruning. Skill instructions are durable behavioral guidance —
losing them mid-conversation silently degrades the agentʼs performance without any visible
error. The model continues operating but without the specialized instructions the skill
provided.
Common approaches:
Flag skill tool outputs as protected so the pruning algorithm skips them
Use the structured tags from Step 4 to identify skill content and preserve it during
compaction

---

## Page 13

## Deduplicateactivations
## AgentSkills
Consider tracking which skills have been activated in the current session. If the model (or
user) attempts to load a skill thatʼs already in context, you can skip the re-injection to avoid
the same instructions appearing multiple times in the conversation.
## Subagentdelegation(optional)
This is an advanced pattern only supported by some clients. Instead of injecting skill
instructions into the main conversation, the skill is run in a separate subagent session. The
subagent receives the skill instructions, performs the task, and returns a summary of its
work to the main conversation.
This pattern is useful when a skillʼs workflow is complex enough to benefit from a dedicated,
focused session.
Using scripts