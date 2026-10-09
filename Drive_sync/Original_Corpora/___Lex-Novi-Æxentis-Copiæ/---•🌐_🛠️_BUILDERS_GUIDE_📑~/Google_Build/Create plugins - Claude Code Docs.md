---
title: "Create plugins - Claude Code Docs"
source: "Drive_sync/Original_Corpora/___Lex-Novi-Æxentis-Copiæ/---•🌐_🛠️_BUILDERS_GUIDE_📑~/Google_Build/Create plugins - Claude Code Docs.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

PLUGINS
Create custom plugins to extend Claude Code with skills, agents, hooks, and MCP servers.
Create plugins
Copy page
Plugins let you extend Claude Code with custom functionality that can be shared across
projects and teams. This guide covers creating your own plugins with skills, agents, hooks, and
MCP servers.
Looking to install existing plugins? See
. For complete technical
specifications, see
.
When to use plugins vs standalone configuration
Claude Code supports two ways to add custom skills, agents, and hooks:
Start with standalone configuration in .claude/ for quick iteration, then
when you’re ready to share.
Quickstart
Approach
Skill names
Best for
Standalone ( .claude/ directory)
/hello
Personal workflows, project-specific
customizations, quick experiments
Plugins (self-contained directories with
skills, agents, hooks, or a .claude-
plugin/plugin.json manifest)
/plugin-
name:hello
Sharing with teammates, distributing
to community, versioned releases,
reusable across projects
Discover and install plugins
Plugins reference
convert to a plugin
Plugins
Create plugins


This quickstart walks you through creating a plugin with a custom skill. You’ll create a manifest
(the configuration file that defines your plugin), add a skill, and test it locally using the --
plugin-dir flag.
Prerequisites
Create your first plugin
Claude Code
Create the plugin directory
Every plugin lives in its own directory containing your skills, agents, or hooks, optionally
alongside a .claude-plugin/plugin.json manifest. The location doesn’t matter for this
quickstart because you’ll point Claude Code at the directory with --plugin-dir in the
test step. Create it anywhere convenient, such as a scratch folder or a projects
directory:
The remaining steps run from the parent directory and reference paths like my-first-
plugin/... relative to it.
1
Create the plugin manifest
The manifest file at .claude-plugin/plugin.json defines your plugin’s identity: its
name, description, and version. Claude Code uses this metadata to display your plugin in
the plugin manager.
Create the .claude-plugin directory inside your plugin folder:
2
mkdir my-first-plugin
mkdir my-first-plugin/.claude-plugin
installed and authenticated


Then create my-first-plugin/.claude-plugin/plugin.json with this content:
For additional fields like homepage , repository , and license , see the
.
my-first-plugin/.claude-plugin/plugin.json
Field
Purpose
name
Unique identifier and skill namespace. Skills are prefixed with this (e.g.,
/my-first-plugin:hello ).
description
Shown in the plugin manager when browsing or installing plugins.
version
Optional. If set, users only receive updates when you bump this field,
except for a
; see
. If omitted, the
version comes from the next source in
.
author
Optional. Helpful for attribution.
Add a skill
Skills live in the skills/ directory. Each skill is a folder containing a SKILL.md file. The
folder name becomes the skill name, prefixed with the plugin’s namespace ( hello/ in a
plugin named my-first-plugin creates /my-first-plugin:hello ).
Create a skill directory in your plugin folder:
3
{
  "name": "my-first-plugin",
  "description": "A greeting plugin to learn the basics",
  "version": "1.0.0",
  "author": {
    "name": "Your Name"
  }
}
mkdir -p my-first-plugin/skills/hello
command source
version management
version management
full manifest
schema


Then create my-first-plugin/skills/hello/SKILL.md with this content:
my-first-plugin/skills/hello/SKILL.md
Test your plugin
Run Claude Code with the --plugin-dir flag to load your plugin:
Once Claude Code starts, try your new skill:
You’ll see Claude respond with a greeting. Run /help and open the Custom commands
tab to see your skill listed under the plugin namespace.
Why namespacing? Plugin skills are always namespaced (like /my-first-
plugin:hello ) to prevent conflicts when multiple plugins have skills with the same
name.
To change the namespace prefix, update the name field in plugin.json .
4
Add skill arguments
5
---
description: Greet the user with a friendly message
disable-model-invocation: true
---
Greet the user warmly and ask how you can help them today.
claude --plugin-dir ./my-first-plugin
/my-first-plugin:hello


The --plugin-dir flag is useful for development and testing. When you’re ready to share your
plugin with others, see
.
Develop a plugin in your skills directory
Instead of passing --plugin-dir on every launch, you can keep a plugin in your skills directory
and have Claude Code load it automatically. claude plugin init scaffolds one:
This creates ~/.claude/skills/my-tool/ with a .claude-plugin/plugin.json manifest and a
starter SKILL.md . On the next session it loads as my-tool@skills-dir with no marketplace
Make your skill dynamic by accepting user input. The $ARGUMENTS placeholder captures
any text the user provides after the skill name.
Update your SKILL.md file:
Run /reload-plugins to pick up the changes. Then try the skill with your name:
Claude will greet you by name. For more on passing arguments to skills, see
.
my-first-plugin/skills/hello/SKILL.md
---
description: Greet the user with a personalized message
---
# Hello Skill
Greet the user named "$ARGUMENTS" warmly and ask how you can help them today. M
/my-first-plugin:hello Alex
claude plugin init my-tool
Skills
Create and distribute a plugin marketplace


or install step.
For the auto-load rules, personal vs. project scope, the workspace-trust requirement, and how
to update or remove one, see
.
Plugin structure overview
You’ve created a plugin with a skill, but plugins can include much more: custom agents, hooks,
MCP servers, LSP servers, and background monitors.
Common mistake: Don’t put commands/ , agents/ , skills/ , or hooks/ inside the .claude-
plugin/ directory. Only plugin.json goes inside .claude-plugin/ . All other directories
must be at the plugin root level.
The plugin root is the individual plugin’s own directory: the one you pass to --plugin-dir or
that contains .claude-plugin/plugin.json . It is never ~/.claude/ . For example, Claude Code
doesn’t read a .mcp.json placed at ~/.claude/.mcp.json .
Directory
Location
Purpose
.claude-plugin/
Plugin root
Contains plugin.json manifest (optional if components
use default locations)
skills/
Plugin root
Skills as <name>/SKILL.md directories
commands/
Plugin root
Skills as flat Markdown files. Use skills/ for new plugins
agents/
Plugin root
Custom agent definitions
hooks/
Plugin root
Event handlers in hooks.json
.mcp.json
Plugin root
MCP server configurations
.lsp.json
Plugin root
LSP server configurations for code intelligence
monitors/
Plugin root
Background monitor configurations in monitors.json
bin/
Plugin root
Executables added to the Bash tool’s PATH while the
plugin is enabled. You can’t include this directory in a
plugin you
settings.json
Plugin root
Default
 applied when the plugin is enabled
Skills-directory plugins
distribute through claude.ai organization
settings
settings


A plugin that ships exactly one skill can place SKILL.md directly at the plugin root instead of
creating a skills/ directory. Claude Code loads it as a single skill and uses the frontmatter
name field for the invocation name. Use the skills/ layout for plugins that may grow to
more than one skill.
Develop more complex plugins
Once you’re comfortable with basic plugins, you can create more sophisticated extensions.
Add Skills to your plugin
Plugins can include
 to extend Claude’s capabilities. Skills are model-invoked:
Claude automatically uses them based on the task context.
Add a skills/ directory at your plugin root with Skill folders containing SKILL.md files:
Each SKILL.md contains YAML frontmatter and instructions. Include a description so
Claude knows when to use the skill:
my-plugin/
├── .claude-plugin/
│   └── plugin.json
└── skills/
    └── code-review/
        └── SKILL.md
---
description: Reviews code for best practices and potential issues. Use when reviewing
---
When reviewing code, check for:
1. Code organization and structure
2. Error handling
3. Security concerns
4. Test coverage
Agent Skills


After you install the plugin, check the install summary: if it reports Run /reload-plugins to
activate. , run that command to load the Skills. For complete Skill authoring guidance
including progressive disclosure and tool restrictions, see
.
Add LSP servers to your plugin
For common languages like TypeScript, Python, and Rust, install the pre-built LSP plugins from
the official marketplace. Create custom LSP plugins only when you need support for languages
not already covered.
LSP (Language Server Protocol) plugins give Claude real-time code intelligence. If you need to
support a language that doesn’t have an official LSP plugin, you can create your own by adding
an .lsp.json file to your plugin:
Users installing your plugin must have the language server binary installed on their machine.
To confirm the server starts, launch Claude Code with the plugin enabled and check the
/plugin Errors tab: a language server that fails to start appears there, for example with
Executable not found in $PATH when the binary isn’t installed. An entry with an invalid
configuration is skipped instead; run claude --debug to see why.
For complete LSP configuration options, see
.
Add background monitors to your plugin
.lsp.json
{
  "go": {
    "command": "gopls",
    "args": ["serve"],
    "extensionToLanguage": {
      ".go": "go"
    }
  }
}
Agent Skills
LSP servers


Background monitors let your plugin watch logs, files, or external status in the background and
notify Claude as events arrive. Claude Code starts each monitor automatically when the
plugin is active, so you don’t need to instruct Claude to start the watch.
Add a monitors/monitors.json file at the plugin root with an array of monitor entries:
Each stdout line from command is delivered to Claude as a notification during the session. For
the full schema, including the when trigger and variable substitution, see
.
Ship default settings with your plugin
Plugins can include a settings.json file at the plugin root to apply default configuration
when the plugin is enabled. Currently, only the agent and subagentStatusLine keys are
supported.
Setting agent activates one of the plugin’s
 as the main thread, applying its
system prompt, tool restrictions, and model. This lets a plugin change how Claude Code
behaves by default when enabled.
monitors/monitors.json
settings.json
[
  {
    "name": "error-log",
    "command": "tail -F ./logs/error.log",
    "description": "Application error log"
  }
]
{
  "agent": "security-reviewer"
}
Monitors
custom agents


This example activates the security-reviewer agent defined in the plugin’s agents/
directory. Settings from settings.json take priority over settings declared in
plugin.json . Unknown keys are silently ignored.
Organize complex plugins
For plugins with many components, organize your directory structure by functionality. For
complete directory layouts and organization patterns, see
.
Test your plugins locally
Use the --plugin-dir flag to test plugins during development. This loads your plugin directly
without requiring installation.
The flag also accepts a .zip archive of the plugin directory.
When a --plugin-dir plugin has the same name as an installed marketplace plugin, the local
copy takes precedence for that session. This lets you test changes to a plugin you already have
installed without uninstalling it first. The exception is plugins that managed settings force-
enable or force-disable: --plugin-dir cannot override those.
As you make changes to your plugin, run /reload-plugins to pick up the updates without
restarting. This reloads plugins, skills, agents, hooks, plugin MCP servers, and plugin LSP
servers. Test your plugin components:
Try your skills with /plugin-name:skill-name
Check that agents appear in /context under Custom Agents, or @-mention one by its
scoped name
Trigger the event each hook matches, such as asking Claude to edit a file for a
PostToolUse hook, and confirm its effect. Claude Code records which hooks matched,
claude --plugin-dir ./my-plugin
claude --plugin-dir ./my-plugin.zip
Plugin directory structure


You can load multiple plugins at once by specifying the flag multiple times:
To test a plugin together with a plugin it depends on, see
.
To test a plugin that is already packaged as a .zip archive and hosted at a URL, such as a CI
build artifact, use --plugin-url instead. Claude Code fetches the archive at startup and
loads it for that session only. If Claude Code can’t fetch the archive, or the archive is invalid, it
starts without the plugin and records a plugin load error that you can review in the /plugin
manager’s Errors tab. The same
 apply as for any plugin source: only point
this flag at archives you control or trust.
To load multiple plugins, repeat the flag for each URL:
Or pass space-separated URLs as one quoted argument:
Debug plugin issues
If your plugin isn’t working as expected:
1. Check the structure: Ensure your directories are at the plugin root, not inside .claude-
plugin/
2. Test components individually: Check each skill, agent, and hook separately
3. Use validation and debugging tools: See
 for CLI
commands and troubleshooting techniques
their exit codes, and their output in the
claude --plugin-dir ./plugin-one --plugin-dir ./plugin-two
claude --plugin-url https://example.com/my-plugin.zip --plugin-url https://example.com
claude --plugin-url "https://example.com/my-plugin.zip https://example.com/other.zip"
debug log
Test a plugin and its dependency
locally
trust considerations
Debugging and development tools


Share your plugins
When your plugin is ready to share:
1. Add documentation: Include a README.md with installation and usage instructions
2. Choose a versioning strategy: Decide whether to set an explicit version or rely on the
fallback described in
.
3. Create or use a marketplace: Distribute through
 for installation
4. Test with others: Have team members test the plugin before wider distribution
Once your plugin is in a marketplace, others can install it using the instructions in
. To keep a plugin internal to your team, host the marketplace in a
.
Submit your plugin to the community marketplace
Anthropic maintains two public marketplaces for Claude Code plugins:
To submit your plugin for community-marketplace review, use one of the in-app forms:
The claude.ai form requires a Team or Enterprise organization and directory management
access; organization Owners have this access by default. Individual authors who aren’t part of
a Team or Enterprise organization can use the Console form instead.
claude-plugins-official : a curated set of plugins maintained by Anthropic. Claude
Code registers it automatically the first time you start Claude Code interactively. If you run
Claude Code non-interactively before that first interactive launch, or a
 blocked an earlier attempt, register it yourself with claude plugin marketplace add
anthropics/claude-plugins-official .
claude-community : the public community marketplace where third-party submissions
land after review. Users add it with /plugin marketplace add anthropics/claude-plugins-
community and install from it as @claude-community .
claude.ai:
Console:
version management
plugin marketplaces
Discover and
install plugins
private
repository
marketplace
policy
claude.ai/admin-settings/directory/submissions/plugins/new
platform.claude.com/plugins/submit


Run claude plugin validate ./your-plugin locally before you submit, replacing ./your-
plugin with the path to your plugin directory. The review pipeline runs the same check on
every submission, along with automated safety screening. When validation passes, Claude
Code prints ✔ Validation passed , or ✔ Validation passed with warnings if there are
warnings. Warnings don’t fail validation; add --strict to treat them as errors.
Approved plugins are pinned to a specific commit SHA in the
 catalog, and CI bumps the pin automatically as you push new commits to your
repository. The public catalog syncs nightly from the review pipeline, so there can be a delay
between approval and your plugin appearing in marketplace.json . To check whether your
plugin is installable yet, search for its name in the
.
The official marketplace, claude-plugins-official , is curated separately. Anthropic decides
which plugins to include at its discretion. There is no application process, and the submission
form does not add plugins to the official marketplace.
If Anthropic lists your plugin in the official marketplace, your CLI can prompt Claude Code
users to install it. See
.
Convert existing configurations to plugins
If you already have skills or hooks in your .claude/ directory, you can convert them into a
plugin for easier sharing and distribution.
Migration steps
Create the plugin structure
Create a new plugin directory in your project root, alongside the existing .claude/
folder, so the relative cp paths in the next step resolve:
Create the manifest file at my-plugin/.claude-plugin/plugin.json :
1
mkdir -p my-plugin/.claude-plugin
anthropics/claude-plugins-
community
community catalog
Recommend your plugin from your CLI


my-plugin/.claude-plugin/plugin.json
Copy your existing files
Copy each configuration directory you have to the plugin root. You might not have all
three: if a directory doesn’t exist, cp prints No such file or directory and copies
nothing, so skip that command or ignore the error.
Your plugin now contains copies of the directories you had under .claude/ . Run ls
my-plugin to confirm: you should see each directory you copied.
2
Migrate hooks
If you have hooks in your settings, create a hooks directory:
Create my-plugin/hooks/hooks.json with your hooks configuration. Copy the hooks
object from your .claude/settings.json or settings.local.json , since the format is
the same. The command receives hook input as JSON on stdin, so use jq to extract the
file path:
3
{
  "name": "my-plugin",
  "description": "Migrated from standalone configuration",
  "version": "1.0.0"
}
cp -r .claude/commands my-plugin/
cp -r .claude/agents my-plugin/
cp -r .claude/skills my-plugin/
mkdir my-plugin/hooks


What changes when migrating
my-plugin/hooks/hooks.json
Test your migrated plugin
Load your plugin to verify everything works:
Test each component: run your commands, check that agents appear in /context , and
trigger the event each hook matches to confirm its effect. Claude Code records which
hooks matched and how they exited in the
.
4
Standalone ( .claude/ )
Plugin
Only available in one project
Can be shared via marketplaces
Files in .claude/commands/
Files in plugin-name/commands/
Hooks in settings.json
Hooks in hooks/hooks.json
Must manually copy to share
Install with /plugin install
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [{ "type": "command", "command": "jq -r '.tool_input.file_path
      }
    ]
  }
}
claude --plugin-dir ./my-plugin
debug log


Was this page helpful?
Yes
No
Discover and install prebuilt plugins
Share session output as artifacts
After migrating, remove the original files from .claude/ to avoid duplicates. Project and user
.claude/agents/ definitions override same-named plugin agents, so the plugin version only
takes effect once the originals are removed. Plugin skills are namespaced as /plugin-
name:skill-name , so the original /skill-name and the plugin copy both remain available
rather than one overriding the other.
Next steps
Now that you understand Claude Code’s plugin system, here are suggested paths for different
goals:
For plugin users
For plugin developers
: browse marketplaces and install plugins
: set up repository-level plugins for your team
: package and share your plugins
: complete technical specifications
Dive deeper into specific plugin components:
: skill development details
: agent configuration and capabilities
: event handling and automation
: external tool integration
Discover and install plugins
Configure team marketplaces
Create and distribute a marketplace
Plugins reference
Skills
Subagents
Hooks
MCP


Company
Anthropic
Careers
Economic Futures
Research
News
Trust center
Transparency
Help and security
Availability
Status
Support center
Learn
Courses
MCP connectors
Customer stories
Engineering blog
Events
Powered by Claude
Service partners
Startups program
Terms and policies
Privacy choices
Privacy policy
Disclosure policy
Usage policy
Commercial terms
Consumer terms
