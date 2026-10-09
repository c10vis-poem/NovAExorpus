---
source: Llm wiki/{Why do you.txt, desktop.txt, wiki desktop.txt, wiki marcor obsidian.txt, wiki on desktop.txt, wiki on mobile.txt}
type: condensed
condensed_from: NovA-Corpus/condensed/llm-wiki-drive-folder/llm-wiki-mobile-workflow-notes (2026-08-20)
original_moved_to: Merovingian's_keep/_salvage/NovA-Corpus/originals/llm-wiki-mobile-workflow-notes/
---

# LLM Wiki on mobile — workflow notes (AI Mode research session)

Consolidated from several short Drive files in the same Gemini AI-Mode research session (`wiki on mobile.txt`, `wiki marcor obsidian.txt`, `wiki on desktop.txt`, `wiki desktop.txt`, `desktop.txt`, `Why do you.txt`).

## Why an LLM Wiki "download" isn't needed

"LLM Wiki" is a blueprint/method for structuring notes so an AI doesn't forget them, not software to download and run — irrelevant on a phone with no computer to unpack/run repo code anyway.

**The Android-native setup, no GitHub required**:
1. **Markor** (text creator) — type/paste raw text on the phone, save into a normal folder on Android storage.
2. **Obsidian** (visual interface) — "Open folder as vault," pointed at the same folder Markor saves to; becomes the visual UI with links and graph views.
3. **Claude/ChatGPT** (AI compiler) — copy a messy note, paste into the AI app with a formatting prompt, copy the clean markdown back into Markor.

## The mobile workflow, step by step

1. Set up a dedicated folder in the mobile notes app (Obsidian or plain text folders).
2. Feed the AI: copy-paste raw notes, article links, or document text into the AI chat app.
3. Use a prompt like: *"I am building an LLM Wiki on my phone. Based on the text above, write a new markdown wiki page with [[interlinked_tags]] or update my existing wiki list. Output it in a clean code block so I can copy it on mobile."*
4. Copy the AI's structured output back into the mobile notes app.

## Connecting Claude to Obsidian on mobile

Two options:
- **API-driven plugin**: get an Anthropic API key from the Anthropic Console, install "Copilot" (by Logseq/Community) or "Smart Connections" via Obsidian mobile's Community Plugins, paste the key into plugin settings. Opens a chat sidebar inside the mobile vault — highlight text and ask Claude to "turn this into an LLM Wiki page" or "index this into my concept graph."
- **The "Plugin" route (desktop)**: pair a command-line agent like Claude Code with the `green-dalii/obsidian-llm-wiki` plugin — the CLI modifies/updates notes, the Obsidian Desktop App visually browses/edits the interconnected wiki pages.

Important distinction: a Claude Pro subscription and the Anthropic Developer API are separate billing systems. An API key in Obsidian charges per-token on a developer balance; it does not use the Pro subscription.

## The mobile "split-screen" bridge (Claude Code PWA + Markor)

Since mobile Obsidian can't run terminal commands directly, bridge via the phone's file management:

1. Keep Obsidian/Markor pointed at one folder containing all `.md` wiki files.
2. Open Claude Code in its PWA (Pro-tier browser panel).
3. Split-screen: PWA on one half, Markor on the other.
4. The exchange: tap the file in Markor, select all, copy, paste into the Claude Code panel with a prompt like *"Review this wiki page, update any cross-links, and return the modified code block."* Copy the result, jump back to Markor, paste over the old note.

**Automating it**: Tasker or MacroDroid can macro this — highlighting text in Markor and hitting a custom share button auto-copies the text and switches to the Claude PWA. Gives a computer-free way to use the Pro account without paying for API tokens.

## Dual-app strategy (Markor + Obsidian)

Because both apps read plain-text folders on the phone, point both at the same folder:
- **Markor as the "Raw Inbox"** — a single `Inbox.md` file for fast, instant-load raw-thought dumps.
- **Obsidian as the "Wiki Viewer"** — used to browse the interconnected `[[Wiki Links]]` and the graph visualizer.

## The copy-paste mobile wiki prompt

```
You are the dedicated AI compiler for my personal LLM Wiki. I am working
entirely on a mobile device, so text formatting must stay copy-paste friendly.
Context: I use Markor for my raw text inbox and Obsidian for my final wiki
folders.
Task: Process the raw text provided below.
1. If it introduces a new core concept, person, or project, generate a brand
   new Markdown (.md) wiki page.
2. Ensure you aggressively use [[Double Bracket Wiki Links]] for all major
   entities, nouns, and sub-concepts so they interlink.
3. Keep the layout flat and compact. Do not add conversational fluff.
4. Output the result strictly inside a clean Markdown code block so I can
   easily copy it with one tap on my phone screen.

Here is the raw text to process:
[PASTE YOUR RAW TEXT HERE]
```

## Source notes (verbatim, merged 2026-10-08 so nothing is lost)

### Why do you

```text
Why do you need an LLM Wiki download?
11 sites
Gist +2
1:56AM
I'm still trying to figure out what I
need the LLM Wiki download for and…
Project
#1
lucasastorian/llmwiki
#2 nashsu/llm_wiki
AI Mode All Images Videos News Maps Shopping Books Flights Finance You don't. You are trying to download software built for computers. Because you are working
entirely on a mobile device, your phone cannot unpack or run those files.
The term "LLM Wiki" is just a blueprint or method for how to structure notes so an AI doesn't forget
them. You do not need to download code from GitHub to use this concept.
Your Exact Android Setup (Use This Instead)
Since you want to use Markor and Obsidian, you already have everything you need. You don't need
GitHub at all.
1. Markor (Your Text Creator): Use this app to quickly type or paste raw text on your phone. Save
these text files into a normal folder on your Android storage.
2. Obsidian (Your Visual Interface): Open the mobile Obsidian app and choose "Open folder as
vault." Point it to the exact same folder where Markor saves its text. Now, Obsidian becomes your
visual user interface, showing you all your links and graph views.
3. Claude / ChatGPT (Your AI Compiler): When you have a messy note, copy the text, open your
normal AI app, paste the text into it using the mobile prompt from earlier, and let the AI format it
into markdown. Then, copy the clean text back into Markor.
Would you like help finding a file syncing app on Android so your folder updates everywhere, or
would you like to focus on writing your first notes using Markor and Obsidian?
Gist +2
GitHub -
nashsu/…
LLM Wiki is a
cross-…
GitHub
lucasastor
Open…
LLM Wiki
features…
GitHub
This
Open-…
This Open-
Source App…
Medium
llm-wiki ·
GitHub
Your
repository…
Gist
llmwiki -
AI Agen…
Install. Clone
the repo an…
AI Skills Marketp…
You cannot access your Claude Pro account's Claude Code CLI directly inside mobile Obsidian
using an API key.
Your Claude Pro subscription and the Anthropic Developer API are completely separate billing
systems. If you put an API key into Obsidian, it will charge you per word (token) on a developer
balance; it will not see or use your Pro account.
9 sites
Medium·… +4
1:59AM
So, I have Claude code. It's on the side
panel of my PWA, so it's only in the …
AI Mode All Images Videos News Maps Shopping Books Flights Finance Because you are entirely on a mobile phone without a computer, you have to use a specific mobile
workflow to bridge your Pro-tier Claude Code PWA with your local markdown files.
The Real Fix: The Mobile "Split-Screen" Workflow
Since you cannot run terminal commands directly inside the Obsidian Android app without a
background computer, you have to use your phone's built-in file management to bridge the
gap.
1. Keep Obsidian/Markor Pointed to One Folder: Make sure your Android local folder contains all
your .md wiki files.
2. Open Claude Code in Your PWA: Go to your Pro account browser panel where you run Claude
Code.
3. Use the Mobile Split-Screen: Open your PWA on one half of your phone screen, and open Markor
on the other half.
4. The Exchange:
When you want Claude to process a file, tap it in Markor, select all, copy, and paste it into your
Claude Code panel.
Use a prompt like: "Review this wiki page, update any cross-links, and return the modified code
block."
Click the "Copy Code" button in your PWA with one tap, jump to Markor, and paste it right back
over the old note.
Can You Automate This on Android?
If you are tired of manually copying and pasting text back and forth between your apps, you can
automate it directly on your phone using Tasker or MacroDroid (popular Android automation
apps):
How to set it up: Create a macro where highlighting text in Markor and hitting a custom share
button automatically copies the text and switches your active app straight to your Claude PWA.
The Result: This gives you a fast, computer-free way to throw text at your Pro account without
paying a single cent for API keys.
Would you like help writing a custom macro blueprint for Android automation apps, or should we
design a master tracking index note inside Markor so you can easily track which files your Claude
PWA has already processed?
Obsidian
code.claude.c…
Medium·Mar…
AI Mode All Images Videos News Maps Shopping Books Flights Finance Overview
- Claude…
Overview. ...
Claude Cod…
Accessing
AI…
This post
explains ho…
Vault
Compan…
Disclosures.
Per…
Does pro
plan…
This is what
claude (…
Cursor and
Cluade API Key …
That's correct, @LiranYzhak. Per…
No, it will not erase your information. Your or
```

### desktop

```text
The Copy-Paste Mobile Wiki Prompt
Since you are on mobile, use this optimized prompt when chatting with the Claude mobile app or the
built-in Obsidian Copilot plugin. It ensures the AI gives you clean, easily copyable blocks that match
the LLM Wiki architecture:
text
You are the dedicated AI compiler for my personal LLM Wiki. I am working entirely on a mobile device, so text form
Context: I use Markor for my raw text inbox and Obsidian for my final wiki folders.
Task: Process the raw text provided below.
1. If it introduces a new core concept, person, or project, generate a brand new Markdown (.md) wiki page.
2. Ensure you aggressively use [[Double Bracket Wiki Links]] for all major entities, nouns, and sub-concepts so they
3. Keep the layout flat and compact. Do not add conversational fluff.
4. Output the result strictly inside a clean Markdown code block so I can easily copy it with one tap on my phone sc
Here is the raw text to process:
[PASTE YOUR RAW TEXT HERE]
Use code with caution.
YouTube·Mik…
Reddit· r/Obs…
AI Mode All Images Videos News Maps Shopping Books Flights Finance Next Steps
To get this running flawlessly on your device:
Do you need help setting up a shared folder on Android so both Markor and Obsidian can see the
same files?
Or would you like to refine the internal structure of your wiki notes (like deciding how to handle
dates or tags)?
Connecting
my Raw…
4. Connecting
Claude to…
Eric Khun
I put
Claude…
Nothing gets
deleted…
Reddit
H
```

### wiki desktop

```text
Alternative Setup (The "Plugin" Route)
If you prefer a standalone desktop software experience over a web UI, you can pair a command-line
agent like Claude Code with the green-dalii/obsidian-llm-wiki Plugin.
You use the CLI to let the AI agent modify and update your notes.
You open the Obsidian Desktop App to visually view, browse, and manually edit the
interconnected wiki pages.
Would you like help with the terminal commands to install and clone the dual CLI/App
repository, or do you need help configuring the prompt instructions for your AI agent?
GitHub +1
GitHub
GitHub
green-
dalii/ob…
... Karpathy
LLM Wiki…
GitHub
GitHub -
Pratiyush/llm-…
What setup does *
Creates raw/ , wiki/ ,…
GitHub
lucasastor
Open…
LLM Wiki
features…
GitHub
LLM Wiki -
GitHub…
At some
point you…
GitHub
That is my mistake. I completely missed that and was focusing way too much on the code side of
things. Since you are working entirely on mobile, running local terminal environments and desktop
clients is completely out of the picture.
You can absolutely still build and manage an LLM Wiki entirely from your phone.
How to Run an LLM Wiki on Mobile
Instead of running local scripts, you rely on mobile-friendly cloud storage and your favorite AI chat
app.
The Storage (Your Wiki): Use a cloud-based markdown notes app with a great mobile interface.
Obsidian is free on iOS and Android, syncs via iCloud/Google Drive, and supports the exact same
interlinked markdown files.
1:51AM
We should know by now that I don't
have a fucking computer, so there's …
AI Mode All Images Videos News Maps Shopping Books Flights Finance The AI (Your Engine): You can use standard AI apps like Claude or ChatGPT as your wiki editor.
The Mobile Workflow
1. Set Up a Mobile Folder: Create a dedicated folder in your mobile notes app (like Obsidian or even
just mobile folders for text files).
2. Feed the AI: Copy-paste your raw notes, article li
```

### wiki marcor obsidian

```text
Connecting Claude to Obsidian on Mobile
To get Claude directly inside your mobile Obsidian app without a computer, use an API-driven
plugin:
1. Get an Anthropic API Key: Go to the Anthropic Console, create a free account, and generate an
API key.
2. Install "Copilot" or "Smart Connections": Open the mobile Obsidian app, go to Settings >
Community Plugins > Browse, and search for Copilot (by Logseq/Community) or Smart
Connections.
16 sites
Eric Khun +4
YouTube·Mik…
1:52AM
Yeah, sure. Also, isn't there a
connector for Claude directly to …
AI Mode All Images Videos News Maps Shopping Books Flights Finance 3. Add Your Key: Paste your Anthropic API key into the plugin settings.
4. How it works: You can open a chat sidebar right inside your mobile vault. You can highlight text in
a note and tell Claude to "turn this into an LLM Wiki page" or "index this into my concept graph."
Supercharging the Workflow with Markor
Markor is an incredible, lightweight Android markdown editor. It reads raw .md text files instantly,
making it much faster than Obsidian for rapid-fire logging on a phone.
Because both Obsidian and Markor just read plain-text folders on your phone, you can point both
apps to the exact same folder.
The Dual-App Strategy
Use Markor as your "Raw Inbox": Keep a single file in Markor called Inbox.md . When you have a
raw thought, an article link, or a text dump, open Markor and paste it into Inbox.md . It opens
instantly without any loading screens.
Use Obsidian as your "Wiki Viewer": Use Obsidian when you want to look at your interconnected
[[Wiki Links]] or view the graph visualizer.
The Copy-Paste Mobile Wiki Prompt
Since you are on mobile, use this optimized prompt when chatting with the Claude mobile app or the
built-in Obsidian Copilot plugin. It ensures the AI gives you clean, easily copyable blocks that match
the LLM Wiki architecture:
text
You are the dedicated AI compiler for my personal LLM Wiki. I a
```

### wiki on desktop

```text
Why this dual setup is ideal
1. Model Context Protocol (MCP) Support: It connects directly to your LLM (like Claude) via MCP.
This allows the AI agent to use your local command-line tools natively to read, write, and index your
4 sites
GitHub +1
1:50AM
I want both.
AI Mode All Images Videos News Maps Shopping Books Flights Finance markdown files.
2. Local and Remote Flexibility: You can choose to run the entire backend locally on your computer
via the command line or host the web application interface separately if you want to access your
wiki across different devices.
Alternative Setup (The "Plugin" Route)
If you prefer a standalone desktop software experience over a web UI, you can pair a command-line
agent like Claude Code with the green-dalii/obsidian-llm-wiki Plugin.
You use the CLI to let the AI agent modify and update your notes.
You open the Obsidian Desktop App to visually view, browse, and manually edit the
interconnected wiki pages.
Would you like help with the terminal commands to install and clone the dual CLI/App
repository, or do you need help configuring the prompt instructions for your AI agent?
GitHub +1
GitHub
GitHub
green-
dalii/ob…
... Karpathy
LLM Wiki…
GitHub
GitHub -
Pratiyush/llm-…
What setup does *
Creates raw/ , wiki/ ,…
GitHub
lucasastor
Open…
LLM Wiki
features…
GitHub
LLM Wiki -
GitHub…
At some
point you…
GitHub
That is my mistake. I completely missed that and was focusing way too much on the code side of
things. Since you are working entirely on mobile, running local terminal environments and desktop
clients is completely out of the picture.
You can absolutely still build and manage an LLM Wiki entirely from your phone.
How to Run an LLM Wiki on Mobile
Instead of running local scripts, you rely on mobile-friendly cloud storage and your favorite AI chat
app.
The Storage (Your Wiki): Use a cloud-based markdown notes app with a great mobile interface.
Obsidian is free on iOS and Android, syncs via iCloud/Google Drive, and supports the exact same
interlinked markdown files.
1:51AM
We should know by now that I don't
have a fucking computer, so there's …
AI Mode All Images Videos News Maps Shopping Books Flights Finance The AI (Your Engine): You can use standard AI apps like Claude or ChatGPT as your wiki editor.
The Mobile Workflow
1. Set Up a Mobile Folder: Create a dedicated folder in your mobile notes app (like Obsidian or even
just mobile folders for text files).
2. Feed the AI: Copy-paste your raw notes, article links, or document text into your AI chat app.
3. Use a Mobile Prompt: Use a prompt like: "I am building an LLM Wiki on my phone. Based on the
text above, write a new markdown wiki page with [[interlinked_tags]] or update my existing wiki list.
Output it in a clean code block so I can copy it on mobile."
4. Copy & Paste: Copy the AI's structured output and paste it into your mobile notes app.
Do you want a specific, copy-pasteable prompt you ca
```

### wiki on mobile

```text
How to Run an LLM Wiki on Mobile
Instead of running local scripts, you rely on mobile-friendly cloud storage and your favorite AI chat
app.
The Storage (Your Wiki): Use a cloud-based markdown notes app with a great mobile interface.
Obsidian is free on iOS and Android, syncs via iCloud/Google Drive, and supports the exact same
interlinked markdown files.
1:51AM
We should know by now that I don't
have a fucking computer, so there's …
AI Mode All Images Videos News Maps Shopping Books Flights Finance The AI (Your Engine): You can use standard AI apps like Claude or ChatGPT as your wiki editor.
The Mobile Workflow
1. Set Up a Mobile Folder: Create a dedicated folder in your mobile notes app (like Obsidian or even
just mobile folders for text files).
2. Feed the AI: Copy-paste your raw notes, article links, or document text into your AI chat app.
3. Use a Mobile Prompt: Use a prompt like: "I am building an LLM Wiki on my phone. Based on the
text above, write a new markdown wiki page with [[interlinked_tags]] or update my existing wiki list.
Output it in a clean code block so I can copy it on mobile."
4. Copy & Paste: Copy the AI's structured output and paste it into your mobile notes app.
Do you want a specific, copy-pasteable prompt you can save on your phone to feed text to the AI
and have it format your wiki pages automatically?
Yes, you can connect Claude directly to Obsidian on mobile, but it requires a very specific
workaround.
Because you don't have a computer, you cannot run standard developer Model Context Protocol
(MCP) servers locally. Instead, you have two primary options: use an Obsidian community plugin that
connects via API keys, or utilize Markor for a seamless, lightning-fast text workflow.
Here is how you can use both apps on your phone to b
```
