No, **you cannot just take a regular reference document and rename it
SKILL.md.** Claude will completely ignore it if you do.

Claude requires a specific **YAML frontmatter block** at the absolute
top of the file so it knows when to trigger the skill. \[1, 2\]

If you want to use a raw reference document, you have two options:

## **Option 1: Turn the document into a Skill (Add Frontmatter)**

You must paste this exact formatting block at the very top of your
document, above your normal text: \[1\]

> ---  
> name: your-skill-name  
> description: Explicitly tell Claude when to open and read this
> specific document.  
> ---  
>   
> \[Paste your raw reference document text here\]

## **Option 2: Put it in a references/ folder (The Better Way)**

If you don't want to change your raw document at all, keep your document
exactly as it is, but structure your files like this: \[1, 3\]

> my-skill-name/  
> ├── SKILL.md  
> └── references/  
> └── your-raw-document.txt

Then, you just write a tiny SKILL.md file that tells Claude to read that
specific document when needed: \[3\]

> ---  
> name: document-reader  
> description: Use when the user asks about the topics inside my
> reference document.  
> ---  
> Read the file located at \`references/your-raw-document.txt\` to
> answer the user's prompt.

Would you like help writing the exact **description** metadata for your
specific document so Claude triggers it correctly? \[1, 4\]

\[1\]
[<u>https://agentskills.io</u>](https://agentskills.io/specification)

\[2\]
[<u>https://www.mdskills.ai</u>](https://www.mdskills.ai/specs/skill-md)

\[3\]
[<u>https://www.skillsdirectory.com</u>](https://www.skillsdirectory.com/docs/using-reference-files)

\[4\]
[<u>https://learn.microsoft.com</u>](https://learn.microsoft.com/en-us/agent-framework/agents/skills)
