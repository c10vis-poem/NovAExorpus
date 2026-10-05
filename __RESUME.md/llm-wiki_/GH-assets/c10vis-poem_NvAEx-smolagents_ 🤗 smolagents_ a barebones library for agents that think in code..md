<!-- Converted from c10vis-poem_NvAEx-smolagents_ 🤗 smolagents_ a barebones library for agents that think in code..pdf — 6 pages -->

## Page 1

NvAEx-smolagents
Code Pull requests Agents Actions Projects Wiki Security and quality Insights Settings
Watch 0 Fork 0
🤗 smolagents: a barebones library for agents that think in code.
Apache License 2.0
huggingface.co/docs/smolagents
Code of conduct
Contributing
Security policy
0 stars 0 forks 0 watching 1 branch 0 tags Activity
Public repository · Forked from huggingface/smolagents
m… 1 Branch 0 Tags Go to file T Go to file Add file Code
This branch is up to date with huggingface/smolagents:main . Contribute Sync fork
| ├── .mcp.json |  |  | ← personal MCP config (copy from .mc |
|---|---|---|---|
| hf-security-analysis[bot] Pin GitHub Actions to commit SHAs (huggingface#2830) |  |  | 227ef5e · last week |
| .github | Pin GitHub Actions to commit SHAs (huggin … | last week |  |
| docs | Docs: fix minor wording issues (huggingfac … | 3 months ago |  |
| examples | Fix code formatting in plan customization R … | last month |  |
| src/smolagents | Bump dev version: v1.27.0.dev0 (huggingfac … | 4 months ago |  |
| tests | Remove remote WasmExecutor (huggingfac … | 4 months ago |  |
| .gitignore | Update no-stop-sequence model list to supp … | 9 months ago |  |
| .pre-commit-config.yaml | Add build files | 2 years ago |  |
| AGENTS.md | Add AGENTS.md (huggingface#1701) |  | last year |
| CODE_OF_CONDUCT.md | Add code of conduct and contributing guide | 2 years ago |  |
| CONTRIBUTING.md | Update contribution guidelines (huggingfac … | last month |  |
| LICENSE | Initial commit | 2 years ago |  |
| Makefile | Remove utils dir from Makefile check_dirs ( … |  | last year |
| README.md | Docs: fix minor wording issues (huggingfac … | 3 months ago |  |
| SECURITY.md | Update security policy (huggingface#2495) | 2 months ago |  |
| e2b.toml | Add E2B code interpreter 🥳 | 2 years ago |  |
| pyproject.toml | Fix CI AttributeError: 'str' object has no attrib … | 2 months ago |  |
 
 
 
 
 
 
 
.pre-commit-config.yaml Add build files 2 years ago
 
 
 
LICENSE Initial commit 2 years ago
 
 
 
e2b.toml Add E2B code interpreter 🥳 2 years ago
 
README Code of conduct Contributing More
license Apache-2.0 website online release v 1 . 2 6 . 0 Contributor Covenant v2.0 adoptedAsk DeepWiki

---

## Page 2

### Agents that think in code!
smolagents is a library that enables you to run powerful agents in a few lines of code. It offers:
Simplicity: the logic for agents fits in ~1,000 lines of code (see agents.py). We kept abstractions to their minimal shape above raw code!
First-class support for Code Agents. Our CodeAgent writes its actions in code (as opposed to "agents being used to write code"). To make it secure, we support executing in sandboxed environments via Blaxel, E2B, Modal, or Docker.
🤗 Hub integrations: you can share/pull tools or agents to/from the Hub for instant sharing of the most efficient agents!
🌐 Model-agnostic: smolagents supports any LLM. It can be a local or transformers ollama model, one of many providers on the Hub, or any model from OpenAI, Anthropic and many others via our LiteLLM integration.
👁 Modality-agnostic: Agents support text, vision, video, even audio inputs! Cf this tutorial for vision.
🛠 Tool-agnostic: you can use tools from any MCP server, from LangChain, you can even use a Hub Space as a tool.
Full documentation can be found here.
Note
Check out our launch blog post to learn more about smolagents !
### Quick demo
First install the package with a default set of tools:
pip install "smolagents[toolkit]"
Then define your agent, give it the tools it needs and run it!
from smolagents import CodeAgent, WebSearchTool, InferenceClientModel
model = InferenceClientModel() agent = CodeAgent(tools=[WebSearchTool()], model=model, stream_outputs=True)
agent.run("How many seconds would it take for a leopard at full speed to run through Pont des Arts?")
smolagents_readme_leopard.mp4

---

## Page 3

0:00 / 0:14
You can even share your agent to the Hub, as a Space repository:
agent.push_to_hub("m-ric/my_agent")
# agent.from_hub("m-ric/my_agent") to load an agent from Hub
Our library is LLM-agnostic: you could switch the example above to any inference provider.
InferenceClientModel, gateway for all inference providers supported on HF
LiteLLM to access 100+ LLMs
OpenAI-compatible servers: Together AI
OpenAI-compatible servers: OpenRouter
Local `transformers` model
Azure models
Amazon Bedrock models
### CLI
You can run agents from CLI using two commands: and
smolagent webagent .
is a generalist command to run a multi-step smolagent CodeAgent that can be equipped with various tools.
# Run with direct prompt and options smolagent "Plan a trip to Tokyo, Kyoto and Osaka between Mar 28 and Apr 7." --model-type "InferenceClientModel" --mo
# Run in interactive mode (launches setup wizard when no prompt provided) smolagent
Interactive mode guides you through:

---

## Page 4

Agent type selection (CodeAgent vs ToolCallingAgent)
Tool selection from available toolbox
Model configuration (type, ID, API settings)
Advanced options like additional imports
Task prompt input
Meanwhile webagent is a specific web-browsing agent using helium (read more here).
For instance:
webagent "go to xyz.com/men, get to sale section, click the first clothing item you see. Get the product details, and
### How do Code agents work?
Our CodeAgent works mostly like classical ReAct agents - the exception being that the LLM engine writes its actions as Python code snippets
User Task
Add task to agent.memory
ReAct loop
agent.memory
Memory as chat messages
Generate from agent.model No call to 'final_answer' tool
Parse output to extract code
Actions are now Python code snippets. Hence, tool calls will be performed as Python function calls. For instance, here is how the agent can perform web search over several websites in one single action:
requests_to_search = ["gulf of mexico america", "greenland denmark", "tariffs"] for request in requests_to_search: print(f"Here are the search results for {request}:", web_search(request))
Writing actions as code snippets is demonstrated to work better than the current industry practice of letting the LLM output a dictionary of the tools it wants to call: uses 30% fewer steps (thus 30% fewer LLM calls) and reaches higher performance on difficult benchmarks. Head to our high-level intro to agents to learn more on that.
Since code execution can be a serious security concern (arbitrary code execution!), you should run agent code in a sandbox. We support several options:
E2B, Blaxel, Modal — managed cloud sandboxes, simplest to set up
Docker — self-hosted container isolation
The built-in LocalPythonExecutor is not a security sandbox. It applies some restrictions but can be bypassed and must not be used as a
security boundary.
CodeAgent Alongside , we also provide the standard ToolCallingAgent which writes actions as JSON/text blobs. You can pick whichever
style best suits your use case.

---

## Page 5

## How smol is this library?
We strived to keep abstractions to a strict minimum: the main code in agents.py has <1,000 lines of code. Still, we implement several types CodeAgent of agents: writes its actions as Python code snippets, and the more classic ToolCallingAgent leverages built-in tool calling
methods. We also have multi-agent hierarchies, import from tool collections, remote code execution, vision models...
By the way, why use a framework at all? Well, because a big part of this stuff is non-trivial. For instance, the code agent has to keep a consistent format for code throughout its system prompt, its parser, the execution. So our framework handles this complexity for you. But of course we still encourage you to hack into the source code and use only the bits that you need, to the exclusion of everything else!
## How strong are open models for agentic workflows?
We've created CodeAgent instances with some leading models, and compared them on this benchmark that gathers questions from a few different benchmarks to propose a varied blend of challenges.
Find the benchmarking code here for more detail on the agentic setup used, and see a comparison of using LLMs code agents compared to vanilla (spoilers: code agents works better).
This comparison shows that open-source models can now take on the best closed models!
## Security
Security is a critical consideration when working with code-executing agents. Ensure you are using one of the sandboxed execution options
Releases
No releases published Create a new release
Packages
No packages published Publish your first package
Contributors

---

## Page 6

No contributors
## Languages
Python 100%
## Suggested workflows
Based on your tech stack
Pylint Lint a Python application with pylint.
By GitHub Actions
Python application Create and test a Python application.
By GitHub Actions
Python package Create and test a Python package on multiple Python versions.
By GitHub Actions
More workflows
Configure
Configure
Configure