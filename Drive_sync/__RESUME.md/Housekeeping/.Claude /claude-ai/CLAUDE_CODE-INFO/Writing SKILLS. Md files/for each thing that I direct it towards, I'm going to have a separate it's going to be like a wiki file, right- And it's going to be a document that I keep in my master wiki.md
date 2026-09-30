**No, everything does not have to be Markdown.**

The instructions inside your **SKILL.md file must be Markdown**, but the
wiki and reference documents inside your folders can be almost any text
format you want. \[1\]

Claude has file-reading tools that can natively scan .md, .txt, .csv,
.json, .yaml, and even code files. \[1\]

## **How to Structure Your Wiki Folders**

You can drop your exact raw wiki files into a references/ folder without
changing a single line of text. \[2\]

Here is how you structure your four master wiki skills:

> termux-builder/  
> ├── SKILL.md \<-- (Markdown format)  
> └── references/  
> └── termux_wiki.txt \<-- (Any text or raw format)  
>   
> aesop-protocols/  
> ├── SKILL.md \<-- (Markdown format)  
> └── references/  
> └── aesop_protocols.md \<-- (Can be markdown or raw text)  
>   
> horizons-ui/  
> ├── SKILL.md \<-- (Markdown format)  
> └── references/  
> └── horizons_frontend.json \<-- (Can be JSON, Markdown, etc.)  
>   
> qairt-backend/  
> ├── SKILL.md \<-- (Markdown format)  
> └── references/  
> └── qairt_runtime.txt \<-- (Any text or raw format)

## **How the SKILL.md File Points to Your Wiki**

Inside the SKILL.md file, you write standard Markdown instructions
telling Claude exactly which file path to read: \[3\]

> ---  
> name: aesop-protocols  
> description: Use when the user asks about the AESOP memory layer or
> protocols.  
> ---  
> \# AESOP Protocols Skill  
>   
> 1. Look inside the \`references/aesop_protocols.md\` wiki file.  
> 2. Read the protocols and answer the user's question exactly as
> specified in that file.

Claude will find the SKILL.md first, see your instruction, and then use
its built-in tools to read whatever wiki file you pointed it to. \[4\]

Are your wiki files currently formatted as **individual .md files**, or
are they all combined into **one massive document**?

\[1\]
[<u>https://platform.claude.com</u>](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)

\[2\]
[<u>https://bibek-poudel.medium.com</u>](https://bibek-poudel.medium.com/the-skill-md-pattern-how-to-write-ai-agent-skills-that-actually-work-72a3169dd7ee)

\[3\]
[<u>https://www.webfuse.com</u>](https://www.webfuse.com/agent-skills-cheat-sheet)

\[4\]
[<u>https://platform.claude.com</u>](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
