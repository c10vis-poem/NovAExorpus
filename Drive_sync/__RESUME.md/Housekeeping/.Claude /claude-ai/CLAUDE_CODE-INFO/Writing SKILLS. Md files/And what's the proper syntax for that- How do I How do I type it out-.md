To type out a Claude custom skill, you must use **exact uppercase
formatting for the SKILL.md file name**, start with a YAML frontmatter
block bound by triple dashes (---), and follow it directly with standard
Markdown instructions. \[1, 2\]

The exact file syntax, variable rules, and structural layout are
detailed below. \[3\]

## **Complete SKILL.md Syntax Blueprint**

> ---  
> name: pull-request-helper  
> description: Generates clean, well-formatted PR descriptions. Use when
> the user asks to write a pull request description, create a PR, or
> summarize branch changes.  
> version: 1.0.0  
> allowed-tools: read, grep, execute  
> ---  
>   
> \# Pull Request Helper  
>   
> \## Overview  
> This skill automates the creation of a clear pull request
> description.  
>   
> \## Instructions  
> 1. Analyze the uncommitted or recently committed changes in the
> workspace.  
> 2. Identify the core components of the changes, focusing on logic
> updates.  
> 3. Replace placeholders with dynamic inputs using the context from
> your request.  
>   
> \## Arguments and Live Context  
> \* Main Argument: Use \`\$ARGUMENTS\` to fetch the ticket number or
> extra developer context.  
> \* Active Branch Name: \`! git branch --show-current\`  
>   
> \## Output Format  
> Structure your response exactly using these three headers:  
> \### 🚀 Summary  
> \### 🛠️ Changes Made  
> \### 🧪 Verification Steps

## **Breakdown of Key Syntax Components**

## **1. The YAML Frontmatter (Required)**

The metadata block controls how and when Claude activates your skill. It
must sit at the absolute top of the file: \[1, 2, 4\]

- 

- name: Must be strictly lowercase, kebab-case only, and match your
  > containing folder's name exactly. This becomes your explicit manual
  > slash command (e.g., /pull-request-helper). \[3, 5, 6\]

- description: The most critical field. You must describe **what it
  > does** and explicitly state **trigger phrases** (e.g., *"Use when
  > the user asks..."*). Claude scans this metadata to auto-trigger the
  > skill during normal chat. \[5, 6, 7\]

- allowed-tools: (Optional) Restricts or explicitly allows specific tool
  > permissions when this skill executes. \[8, 9\]

- 

## **2. Live Context and Variable Syntax**

You can inject dynamic inputs directly into the body text using two
distinct syntaxes: \[10\]

- 

- **Dynamic Arguments:** Use \$ARGUMENTS (or shorthand \$0, \$1). If you
  > type /pull-request-helper API-404, Claude will automatically swap
  > \$ARGUMENTS out for API-404 before processing.

- **Live Shell Context:** Use the **! command** syntax enclosed in
  > backticks to query live workspace info. When Claude reads your file,
  > it executes the shell command immediately and inserts the raw
  > terminal output directly into the prompt text before evaluating it.
  > \[10, 11\]

- 

## **3. Markdown Body Instructions**

Beneath the frontmatter, write the rest of the file like an onboarding
manual. Keep rules structured with Markdown headers (#, \##) and
numbered lists so Claude treats them as high-priority, sequential steps.
\[3, 12, 13\]

For a complete step-by-step video tutorial demonstrating how to type,
save, and test this file structure locally:

If you want, let me know:

- 

- What specific **workflow or task** are you trying to automate?

- Do you need help formatting a **live shell command (!)** for your
  > workspace?

- 

\[1\]
[<u>https://www.youtube.com</u>](https://www.youtube.com/watch?v=Qo6UveKgvHU)

\[2\]
[<u>https://codemeetai.substack.com</u>](https://codemeetai.substack.com/p/how-to-create-a-claude-code-skill)

\[3\]
[<u>https://www.skillsdirectory.com</u>](https://www.skillsdirectory.com/docs/skill-md-format)

\[4\]
[<u>https://www.agensi.io</u>](https://www.agensi.io/learn/skill-md-format-reference)

\[5\]
[<u>https://resources.anthropic.com</u>](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf)

\[6\]
[<u>https://code.claude.com</u>](https://code.claude.com/docs/en/skills)

\[7\]
[<u>https://www.mdskills.ai</u>](https://www.mdskills.ai/learn/how-to-create-a-claude-code-skill)

\[8\]
[<u>https://agentfactory.panaversity.org</u>](https://agentfactory.panaversity.org/docs/General-Agents-Foundations/claude-code-teams-cicd/custom-skills-with-frontmatter)

\[9\]
[<u>https://www.reddit.com</u>](https://www.reddit.com/r/PromptEngineering/comments/1uggx0r/claude_code_has_a_skills_system_most_people_dont/)

\[10\]
[<u>https://sherlock.xyz</u>](https://sherlock.xyz/post/how-to-write-skills-for-claude-code-and-cowork)

\[11\]
[<u>https://www.damiandemasi.com</u>](https://www.damiandemasi.com/blog/claude-code-skills-deep-dive)

\[12\]
[<u>https://resources.anthropic.com</u>](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf)

\[13\]
[<u>https://bibek-poudel.medium.com</u>](https://bibek-poudel.medium.com/the-skill-md-pattern-how-to-write-ai-agent-skills-that-actually-work-72a3169dd7ee)
