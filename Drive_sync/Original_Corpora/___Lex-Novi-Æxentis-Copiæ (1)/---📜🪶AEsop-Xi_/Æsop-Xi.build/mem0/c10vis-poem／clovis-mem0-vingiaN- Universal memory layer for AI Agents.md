# c10vis-poem／clovis-mem0-vingiaN: Universal memory layer for AI Agents

Watch
0
Universal memory layer for AI Agents
Apache License 2.0
mem0.ai
Contributing
Security policy
0 stars
0 forks
0 watching
1 branch
0 tags
Activity
Public repository · Forked from mem0ai/mem0
1 Branch
0 Tags
Go to file
Go to file
Add file
Code
This branch is up to date with mem0ai/mem0:main .
Contribute
Sync fork
Himanshu-Sangshetti and kartik-mem0 feat(integrations): n8n community node for Mem0 (mem0ai#6517)
d4869d2 · 9 hours ago
.agents/plugins
refactor: consolidate agent/editor plugins u…
last month
.claude-plugin
fix(mem0-plugin): store assistant-authored …
2 weeks ago
.codex-plugin
refactor: consolidate agent/editor plugins u…
last month
.cursor-plugin
fix(mem0-plugin): store assistant-authored …
2 weeks ago
.github
feat(integrations): n8n community node for …
9 hours ago
cli
chore: update changelog, bump SDK version…
2 weeks ago
docs
feat(integrations): n8n community node for …
9 hours ago
evaluation @ 4b61c5d
chore: retire in-repo evaluation/ in favor of …
last month
examples
fix(deps): patch js-yaml, ai, python-dotenv vu…
last month
integrations
feat(integrations): n8n community node for …
9 hours ago
mem0-ts
chore(release): Python SDK v2.0.14, TypeScr…
5 days ago
mem0
fix(milvus): guard text field in update() with …
last week
scripts
Oss qdrant hosted memories to platform mi…
2 months ago
server
fix(dashboard): clear the LLM API key on pro…
last week
skills
docs: remove criteria retrieval docs for non-…
2 weeks ago
tests
fix(milvus): guard text field in update() with …
last week
.gitignore
refactor(opencode): use existing mem0 SDK…
last month
.gitmodules
chore: retire in-repo evaluation/ in favor of …
last month
.pre-commit-config.yaml
Code Formatting (mem0ai#1828)
2 years ago
AGENTS.md
feat(integrations): n8n community node for …
9 hours ago
c10vis-poem
clovis-mem0-vingiaN
Code
Pull requests
Agents
Actions
Projects
Security and quality
Insights
Settings
Fork
0
m
T


CLAUDE.md
feat: add AGENTS.md for AI coding agent in…
3 months ago
CONTRIBUTING.md
chore: remove OpenMemory from the mono…
17 hours ago
LICENSE
Add: Licence (mem0ai#1605)
2 years ago
LLM.md
chore: consolidate cookbooks/ into an index…
last month
Makefile
chore(release): Python SDK v2.0.14, TypeScr…
5 days ago
README.md
docs: update README benchmarks to curre…
3 weeks ago
SECURITY.md
chore: remove OpenMemory from the mono…
17 hours ago
marketplace.json
refactor: consolidate agent/editor plugins u…
last month
poetry.lock
fix(transformers): upgrade to >=5.3.0 (GHSA…
3 weeks ago
pyproject.toml
chore: remove OpenMemory from the mono…
17 hours ago
GITHUB TRENDING
#1 Repository Of The Day
1
Learn more · Join Discord · Demo
Discord
Discord
downloads
downloads rate limited by upstream service
rate limited by upstream service
commit activity 107/month
pypi package
pypi package v2.0.14
v2.0.14
npm
npm v3.1.2
v3.1.2
Y Combinator S24
📄 Benchmarking Mem0's token-efficient memory algorithm →
Benchmark
Old
New
Tokens
Latency p50
LoCoMo
71.4
92.5
7.0K
0.88s
LongMemEval
67.8
94.4
6.8K
1.09s
BEAM (1M)
—
64.1
6.7K
1.00s
BEAM (10M)
—
48.6
6.9K
1.05s
All benchmarks run on the same production-representative model stack. Single-pass retrieval (one call, no agentic loops) at a top_200 retrieva
budget. Scores reflect Mem0's managed platform, which includes proprietary optimizations not available in the open-source SDK; open-source
users should expect directionally similar gains but not identical numbers.
What changed:
Single-pass ADD-only extraction -- one LLM call, no UPDATE/DELETE. Memories accumulate; nothing is overwritten.
Agent-generated facts are first-class -- when an agent confirms an action, that information is now stored with equal weight.
Entity linking -- entities are extracted, embedded, and linked across memories for retrieval boosting.
Multi-signal retrieval -- semantic, BM25 keyword, and entity matching scored in parallel and fused.
New Memory Algorithm (April 2026)
README
Contributing
License
Security


Temporal Reasoning -- time-aware retrieval that ranks the right dated instance for queries about current state, past events, and upcoming
plans.
See the migration guide for upgrade instructions. The evaluation framework is open-sourced so anyone can reproduce the numbers.
92.5 on LoCoMo -- +21 points over the previous algorithm
94.4 on LongMemEval -- +27 points, with 98.2 on assistant memory recall
64.1 on BEAM (1M) -- production-scale memory evaluation at 1M tokens
Read the full paper
Mem0 ("mem-zero") enhances AI assistants and agents with an intelligent memory layer, enabling personalized AI interactions. It remembers
user preferences, adapts to individual needs, and continuously learns over time—ideal for customer support chatbots, AI assistants, and
autonomous systems.
Core Capabilities:
Multi-Level Memory: Seamlessly retains User, Session, and Agent state with adaptive personalization
Developer-Friendly: Intuitive API, cross-platform SDKs, and a fully managed service option
Applications:
AI Assistants: Consistent, context-rich conversations
Customer Support: Recall past tickets and user history for tailored help
Healthcare: Track patient preferences and history for personalized care
Productivity & Gaming: Adaptive workflows and environments based on user behavior
AI agents can mint a working Mem0 API key in under five seconds — no email, no dashboard, no OTP. Four commands end-to-end:
The human owner can claim the account later with mem0 init --email <their-email> — same key, memories preserved. Full guide: Sign up
as an agent.
Library
Self-Hosted Server
Cloud Platform
Best for
Testing, prototyping
Teams running on their own infrastructure
Zero-ops production use
Setup
pip install mem0ai
docker compose up
Sign up at app.mem0.ai
Dashboard
--
Yes
Yes
Auth & API Keys
--
Yes
Yes
Research Highlights
Introduction
Key Features & Use Cases
🚀 Quickstart Guide
Sign up as an agent
# 1. Install
npm install -g @mem0/cli      # or: pip install mem0-cli
# 2. Sign up as an agent (replace `claude-code` with your name)
mem0 init --agent --agent-caller claude-code
# 3. Add a memory
mem0 add "I am using mem0"
# 4. Search
mem0 search "am I using mem0"


Library
Self-Hosted Server
Cloud Platform
Advanced Features
--
Teasers
All included
Just testing? Use the library. Building for a team? Self-hosted. Want zero ops? Cloud.
For enhanced hybrid search with BM25 keyword matching and entity extraction, install with NLP support:
Install sdk via npm:
Note: Self-hosted auth is on by default. Upgrading from a pre-auth build? Set ADMIN_API_KEY , register an admin through the wizard, or
AUTH_DISABLED=true for local dev only. See upgrade notes.
See the self-hosted docs for configuration.
1. Sign up on Mem0 Platform
2. Embed the memory layer via SDK or API keys
3. Using hosted Qdrant vectors? See the Platform migration guide to import them into Mem0 Platform.
Manage memories from your terminal:
See the CLI documentation for the full command reference.
Teach your AI coding assistant (Claude Code, Codex, Cursor, Windsurf, OpenCode, OpenClaw, and any tool that supports the skills standard)
how to build with Mem0. Two categories:
Reference skills — always on (SDK knowledge loaded into the assistant's context):
Library (pip / npm)
pip install mem0ai
pip install mem0ai[nlp]
python -m spacy download en_core_web_sm
npm install mem0ai
Self-Hosted Server
# Recommended: one command — start the stack, create an admin, issue the first API key.
cd server && make bootstrap
# Manual: start the stack and finish setup via the browser wizard.
cd server && docker compose up -d    # http://localhost:3000
Cloud Platform
CLI
npm install -g @mem0/cli   # or: pip install mem0-cli
mem0 init
mem0 add "Prefers dark mode and vim keybindings" --user-id alice
mem0 search "What does Alice prefer?" --user-id alice
Agent Skills
npx skills add https://github.com/mem0ai/mem0 --skill mem0
npx skills add https://github.com/mem0ai/mem0 --skill mem0-cli
npx skills add https://github.com/mem0ai/mem0 --skill mem0-vercel-ai-sdk


Pipeline skills — run on demand (execute an end-to-end workflow in an existing repo):
Use /mem0-integrate to wire Mem0 into an existing repo via a test-first pipeline, then /mem0-test-integration to verify. Use /mem0-oss-
to-platform to migrate an existing project from Mem0 OSS to the hosted Platform SDK. See the skills catalog or Vibecoding with Mem0 for
the full picture.
Mem0 requires an LLM to function, with gpt-5-mini from OpenAI as the default. However, it supports a variety of LLMs; for details, refer to
our Supported LLMs documentation.
Mem0 uses text-embedding-3-small from OpenAI as the default embedding model. For best results with hybrid search (semantic + keyword
+ entity boosting), we recommend using at least Qwen 600M or a comparable embedding model. See Supported Embeddings for configuration
details.
First step is to instantiate the memory:
For detailed integration steps, see the Quickstart and API Reference.
ChatGPT with Memory: Personalized chat powered by Mem0 (Live Demo)
Browser Extension: Store memories across ChatGPT, Perplexity, and Claude (Chrome Extension)
Langgraph Support: Build a customer bot with Langgraph + Mem0 (Guide)
CrewAI Integration: Tailor CrewAI outputs with Mem0 (Example)
npx skills add https://github.com/mem0ai/mem0 --skill mem0-integrate
npx skills add https://github.com/mem0ai/mem0 --skill mem0-test-integration
npx skills add https://github.com/mem0ai/mem0 --skill mem0-oss-to-platform
Basic Usage
from openai import OpenAI
from mem0 import Memory
openai_client = OpenAI()
memory = Memory()
def chat_with_memories(message: str, user_id: str = "default_user") -> str:
    # Retrieve relevant memories
    relevant_memories = memory.search(query=message, filters={"user_id": user_id}, top_k=3)
    memories_str = "\n".join(f"- {entry['memory']}" for entry in relevant_memories["results"])
    # Generate Assistant response
    system_prompt = f"You are a helpful AI. Answer the question based on query and memories.\nUser Memories:\n{memori
    messages = [{"role": "system", "content": system_prompt}, {"role": "user", "content": message}]
    response = openai_client.chat.completions.create(model="gpt-5-mini", messages=messages)
    assistant_response = response.choices[0].message.content
    # Create new memories from the conversation
    messages.append({"role": "assistant", "content": assistant_response})
    memory.add(messages, user_id=user_id)
    return assistant_response
def main():
    print("Chat with AI (type 'exit' to quit)")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        print(f"AI: {chat_with_memories(user_input)}")
if __name__ == "__main__":
    main()
🔗 Integrations & Demos


Full docs: https://docs.mem0.ai
Community: Discord · X (formerly Twitter)
Contact: founders@mem0.ai
We now have a paper you can cite:
Releases
No releases published
Create a new release
Packages
No packages published
Publish your first package
Contributors
No contributors
Languages
TypeScript 48.7%
Python 48.2%
Shell 1.8%
JavaScript 0.6%
CSS 0.3%
Makefile 0.2%
Other 0.2%
Suggested workflows
Based on your tech stack
SLSA Generic generator
Generate SLSA3 provenance for your existing release workflows
By Open Source Security Foundation (OpenSSF)
Configure
Python application
Create and test a Python application.
By GitHub Actions
Configure
Python Package using Anaconda
Create and test a Python package on multiple Python versions using Anaconda for package management.
By GitHub Actions
Configure
More workflows
📚 Documentation & Support
Citation
@article{mem0,
  title={Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory},
  author={Chhikara, Prateek and Khant, Dev and Aryan, Saket and Singh, Taranjeet and Yadav, Deshraj},
  journal={arXiv preprint arXiv:2504.19413},
  year={2025}
}
⚖️ License
