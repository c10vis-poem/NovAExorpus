<!-- Converted from c10vis-poem_AEsopXi-obsidian-tars_ Obsidian tars plugin that supports text generation based on tag suggestions, using services like DeepSeek, Claude, OpenAI, OpenRouter, SiliconFlow, Gemini, Ollama, Kimi, Doubao, Qwen, Zhipu, QianFan & more..pdf — 10 pages -->

## Page 1

AEsopXi-obsidian-tars
Code Pull requests Agents Actions Projects Wiki Security and quality Insights
Settings
Watch 0 Fork 0
## Obsidian tars plugin that supports text generation based on tag suggestions, using services like DeepSeek, Claude,
## OpenAI, OpenRouter, SiliconFlow, Gemini, Ollama, Kimi, Doubao, Qwen, Zhipu, QianFan & more.
MIT License
0 stars 0 forks 0 watching 1 branch 0 tags Activity
Public repository · Forked from TarsLab/obsidian-tars
1 Branch 0 Tags Go to file T Go to file Add file Code
This branch is up to date with TarsLab/obsidian-tars:main . Contribute Sync fork
| ae86jack Merge pull request TarsLab#129 from TarsLab/fix/provider-requests-and … |  |  | 9e95b52 · last month |
|---|---|---|---|
| .github/workflows | ci: attest manifest.json alongside th … | last month |  |
| docs | fix: warn on an emptied tag, and na … | last month |  |
| scripts | test: add a harness that runs the pro … | last month |  |
| src | fix: warn on an emptied tag, and na … | last month |  |
| test/smoke | fix: a split SSE frame no longer ends … | last month |  |
| .editorconfig | chore: Add initial project files and c … | 2 years ago |  |
| .gitignore | test: add a harness that runs the pro … | last month |  |
| .npmrc | chore: Add initial project files and c … | 2 years ago |  |
| .prettierrc | chore: Add initial project files and c … | 2 years ago |  |
| LICENSE | chore: Add initial project files and c … | 2 years ago |  |
| README.md | fix: one control in the model row, no … | last month |  |
| README_zh.md | fix: one control in the model row, no … | last month |  |
| esbuild.config.mjs | chore: align build and release setup … | last month |  |
| esbuild.smoke.mjs | test: add a harness that runs the pro … | last month |  |

---

## Page 2

| eslint.config.mjs | test: add a harness that runs the pro … | last month |
|---|---|---|
| manifest.json | chore: release 3.6.0 | last month |
| package-lock.json | chore: release 3.6.0 | last month |
| package.json | chore: release 3.6.0 | last month |
| styles.css | chore: replace deprecated Setting A … | last month |
| tsconfig.json | test: add a harness that runs the pro … | last month |
| version-bump.mjs | chore: Add initial project files and c … | 2 years ago |
| versions.json | chore: release 3.6.0 | last month |
 
 
 
 
 
 
 
 
README License
## English |
## Tars
Tars is an Obsidian plugin that supports text generation based on tag suggestions, using services like Claude, OpenAI, Gemini, 🔥DeepSeek, 🔥SiliconFlow, 🔥OpenRouter, 🔥MiniMax, 🔥LongCat, Ollama, Kimi, Doubao, Qwen, Zhipu, QianFan & more. The name Tars comes from the robot Tars in the movie "Interstellar". The plugin supports both desktop and mobile devices.
## 🌟 3.1 Multimodal
## 🎨 Image Generation
GPT-Image-1: Supports image generation and editing functions
## 👁 Visual Understanding
Image Analysis: Claude, OpenRouter, SiliconFlow, etc. can interpret images
Document Interpretation: Claude and OpenRouter, etc. support PDF file analysis
Note: Only embedded files (e.g. ![[example.jpg]] ) are supported. External URL links will not
work.

---

## Page 3

# #NewChat ~ #User : A software engineer is writing code on a MacBook. The
MacBook screen prominently displays the "Obsidian TARS" project in large text.
On the desk sits a glossy obsidian stone with a glass-like finish. Next to it stands
TARS, the robot from the movie "Interstellar", in the style of Studio Ghibli.
#Gptimage
### #NewChat ~~ #User
Describe this image in three sentences.
#Sonnet : This illustration shows a person with glasses and dark hair typing on
a laptop that displays "Obsidian TARS" along with what appears to be code on
the screen. To the right of the laptop sits a piece of black rock or mineral,
possibly obsidian, which relates to the software being used. Next to the desk is
a boxy robot-like device with a simple smiling face displayed on a small screen,
### suggesting an Al companion or assistant that works with the Obsidian software)

---

## Page 4

### Major Updates in Version 2.x
#DeepSeek : ) from the command list to generate a response.
🔥 Custom prompt templates, run the "Load template file" command when using for the first time.
🔥 Status bar that displays real-time information about character count, rounds, and time spent.
Type # , use Obsidian's native tag completion, then input space to trigger. On mobile devices where typing # might be inconvenient, you can type the complete tag (without #) to
trigger. Assistant tags will generate AI responses when triggered.

---

## Page 5

## Features
Support for internal links
Export conversations to JSONL dataset, supports ms-swift (Scalable lightWeight Infrastructure for Fine-Tuning)

---

## Page 6

### AI providers
Azure OpenAI
Claude
DeepSeek
Doubao
Gemini
Kimi
LongCat
MiniMax
Ollama
OpenAI
OpenRouter
Qianfan
Qwen
SiliconFlow
X.ai Grok
Zhipu
If the AI provider you want is not in the list above, you can propose a specific plan in the issue.
### Assistant features
Azure: the model field holds the deployment name you chose in the portal, not a model id
🔥DeepSeek: the reasoning model's CoT is output in callout format
Doubao: Supports bot API, Supports DeepSeek web search plugin and knowledge base plugin
🔥LongCat: Reasoning output in callout format
🔥MiniMax: Reasoning output in callout format
🔥SiliconFlow: Supports many models such as DeepSeek V3/R1
🔥Zhipu: Web search option, and reasoning output in callout format for GLM-4.5 / 4.6 / Z1
### How to use
Add an AI assistant in the settings page, set the API key, and configure the model.
Enter a question, like "1+1=?", then select "#User :" from the command list to transform it into - "#User : 1+1=?"
Select an assistant from the command list, like "#Claude :", to trigger the AI assistant to answer the question.
You can also directly type # , enter the tag, and then type a space to trigger the AI assistant.
Follow the conversation order rules of large language models: system messages always appear first (can be omitted), then user and assistant messages alternate like a ping-pong match.
A simple conversation example:

---

## Page 7

#User : 1+1=?（user message） (blank line) #Claude :（trigger）
Conversation order rules:
System message User message Assistant message
If you are not satisfied with the AI assistant's answer and want to retry. Use the plugin command "Select the message at the cursor", select and delete the AI assistant's response content, modify your question, and trigger the AI assistant again. Or select the response content and use a command like "#Claude :" to retrigger the AI assistant, which will delete the previous response and generate a new one.
### Conversations syntax
A paragraph cannot contain multiple messages. Messages should be separated by blank lines.
The conversation messages will send to the configured AI assistant.

---

## Page 8

Callout sections will be ignored. You can write content in the callout without sending it to the AI assistant. Callout is not markdown syntax, it is an obsidian extension syntax.
Start a new conversation with NewChat tag.
Tag commands are based on the paragraph at the cursor or in the selection. A Markdown paragraph can be:
Multiple lines of plain text not separated by empty lines
A code block
With correct syntax, when you input a space after #tag, it will trigger tag completion. For example:
#NewChat
#System :
#User :
#NewChat #System :
#NewChat #User :
#Claude : (AI generate)
## Appearance customization
We recommend using the colored tags plugin.
## FAQ
## How to trigger?
There are several ways:
Select tags from the command palette

---

## Page 9

Type # + tag + space
Directly type the complete tag (without #)
# Can't find the model you want in the settings?
Most providers are asked for their own model list, so the choices come from the API rather than from a list baked into the plugin — a model the provider no longer advertises will not be among them.
Set it under "Override input parameters" as JSON, such as {"model":"your-desired-model"} , which takes
precedence over the model chosen in the picker.
If the list cannot be read at all — an account still awaiting verification, a relay that does not implement it — the row turns into a plain text field and the model can be typed in directly.
# How to view the developer console?
Windows: CTRL + SHIFT + i
MacOS: CMD + OPTION + i
Linux: CTRL + SHIFT + i
Capture console logs
# How to enter the baseUrl when using third-party services?
Modify the baseURL in the settings, copy and paste the corresponding address from the service provider's documentation, and finally check if the URL is complete.
# Which assistant type to choose for third-party service providers?
LLM protocols differ significantly between openAI, claude, and gemini. Make sure to select the correct one. The chain of thought in deepseek-r1 is also different from openAI.
# What do the 404, 400, 4xx numbers in error messages mean?
These are HTTP status codes:
401 means "Unauthorized", possibly due to an incorrect API key.
402 means "Payment Required".
404 means "Not Found", usually due to incorrect baseURL configuration or model name.
400 means "Bad Request", possibly due to incorrect API key, missing user messages, tag parsing failure - leading to missing messages, model errors, etc.
429 means "Too Many Requests", possibly due to high request frequency or service provider rate limits.
# Text generation is very long and complex, causing rendering performance issues or
# app freezing
Try using the default theme. Some third-party themes can negatively impact rendering performance; switch to a more efficient theme.

---

## Page 10

## Releases
No releases published Create a new release
## Packages
No packages published Publish your first package
## Contributors
No contributors
## Languages
TypeScript 93.6% Shell 3.4% JavaScript 1.9% CSS 1.1%
## Suggested workflows
Based on your tech stack
Webpack Build a NodeJS project with npm and webpack.
By GitHub Actions
Datadog Synthetics Run Datadog Synthetic tests within your GitHub Actions workflow
By Datadog
SLSA Generic generator Generate SLSA3 provenance for your existing release workflows
By Open Source Security Foundation (OpenSSF)
More workflows
Configure
Configure
Configure