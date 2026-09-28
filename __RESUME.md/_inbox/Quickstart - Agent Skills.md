<!-- Converted from Quickstart - Agent Skills.pdf — 4 pages -->

## Page 1

## AgentSkills
For skill creators Quickstart
For skill creators
QuickstartCopy page
### Create your first Agent Skill and see it work in VS Code.
In this tutorial, youʼll create a skill that gives an agent the capability to roll dice using a
random number generator.
## Prerequisites
VS Code with GitHub Copilot
This tutorial uses VS Code, but Agent Skills are an open format. The same skill works in any compatible agent, including Claude Code and OpenAI Codex.
## Createtheskill
A skill is a folder containing a SKILL.md file. VS Code looks for skills in .agents/skills/
by default. Create .agents/skills/roll-dice/SKILL.md in your project:

---

## Page 2

.agents/skills/roll-dice/SKILL.md
### AgentSkills
ked to roll a die (d6, d20, etc.), roll dice, or generate a random dice roll.
mber from 1
a standard
Thatʼs it — one file, under 20 lines. Hereʼs what each part does:
name — A short identifier for the skill. Must match the folder name.
description — Tells the agent when to use this skill. This is how the agent decides
whether to activate it.
The body — Instructions the agent follows when the skill activates. Here, the agent is
instructed to generate a random number using a terminal command, substituting the
number of sides from the userʼs request.
### Tryitout
1. Open your project in VS Code.
2. Open the Copilot Chat panel.
3. Select Agent mode from the mode dropdown at the bottom of the chat panel.

---

## Page 3

4. Type /skills to confirm that roll-dice appears in the list. If it doesnʼt, check that
## Agentthe fileSkillsis at .agents/skills/roll-dice/SKILL.md relative to your project root.
5. Ask: “Roll a d20”
The agent should activate the roll-dice skill. It may ask for permission to run a terminal
command — allow it. It will run the command and return a random number between 1 and
20.
Tool-use reliability varies across models — some follow skill instructions and run commands consistently, while others may attempt to answer on their own. If the agent responds without running a terminal command, try selecting a different model from the model dropdown.
### Howitworks
Hereʼs what happened behind the scenes:
1. Discovery — When the chat session started, the agent scanned default skill directories
and found your skill. It read only the name and description , just enough to know
when the skill might be relevant.
2. Activation — When you asked about rolling dice, the agent matched your question to
the skillʼs description and loaded the full SKILL.md body into context.
3. Execution — The agent followed the instructions in the body, adapting the terminal
command to the number of sides in your request.
This process uses progressive disclosure to let the agent access many skills without
loading all their instructions up front.
### Nextsteps
Youʼve created a working Agent Skill. From here:
Best practices — How to write skills that are well-scoped and effective.
Optimizing skill descriptions — Test and improve your skillʼs description so it activates
on the right prompts.

---

## Page 4

reference
Specification — The complete format
## AgentSkills
Example skills — Browse real-world skills
Client Showcase
for SKILL.md files.
on GitHub.
Best practices