Fair point. Let’s strip out all the protocol and MCP talk entirely and
focus *strictly* on software architecture definitions. \[1, 2\]

The most concrete, industry-standard definition used by software
engineers is: **Agent = Model + Harness**. \[3, 4\]

The harness is **every piece of code, state management, and execution
logic that wraps *around* the model** to turn a stateless text-generator
into a functioning program. The model is the brain; the harness is the
literal nervous system and body. \[1, 2, 4, 5, 6\]

If you are looking for production reference implementations of a pure
harness, look at **Microsoft's Agent Framework Harness**, **LangChain's
Anatomy of an Agent Harness**, or **Databricks' Omnigent/AgentCore
architecture**. \[4, 7, 8, 9, 10\]

According to these reference models, a pure harness consists of exactly
**three non-negotiable architectural pillars**:

## **1. Loop Control (The State Machine)**

Because LLMs are completely stateless, they forget everything the
millisecond they finish generating text. The harness is the continuous
execution loop (the while loop) that manages state. \[1, 2, 11, 12\]

- 

- **Task State:** Tracking what the agent has already tried, how many
  > steps it has taken, and if it is stuck in an infinite loop.

- **Stop Conditions:** Deciding *when* the agent is actually finished or
  > when to forcefully kill the session because it is failing.

- **Error Interception:** Catching system exceptions, tool crashes, or
  > model timeouts, and formatting them into a message the model can
  > understand to self-correct. \[13, 14, 15, 16\]

- 

## **2. Context Management (The Prompt & Token Layer)**

The harness is the gatekeeper of the model's active memory. It decides
exactly what text goes into the context window on every single turn of
the loop. \[17, 18\]

- 

- **Token Compaction:** When the context window fills up, the harness
  > compresses, summarizes, or deletes older history turns so the model
  > doesn't run out of memory. \[8, 19, 20, 21, 22\]

- **Dynamic Injections:** Injecting system instructions, rules files
  > (like AGENTS.md or CLAUDE.md), and historical context right before
  > sending the payload to the model. \[2, 23\]

- 

## **3. Tool Execution & Gatekeeping (The Action Layer)**

The model can only output text; it cannot physically click a button,
open a file, or execute code. The harness bridges the gap between text
and execution. \[4, 8, 17, 24, 25\]

- 

- **Parsing:** The harness reads the model's text output, detects a
  > request to do an action (via regex, XML, or JSON parsing), and halts
  > the model. \[2, 17, 26, 27, 28\]

- **Permissions & Guardrails:** The harness checks if the model is
  > legally allowed to run that command or access that specific file
  > directory before executing it. \[17, 29\]

- **Result Ingestion:** The harness runs the execution logic, grabs the
  > result, and appends it back into the model's context history. \[17\]

- 

## **In Your Kotlin APK: Where Do You Write This?**

In your specific APK architecture, you would implement this by writing a
core AgentHarness class or background service. \[2\]

It acts as the pure **Orchestration Layer** between your UI and the
outside world:

1.  Your UI captures the user input and creates an instance of the
    > AgentHarness.

2.  The AgentHarness instantiates the state machine, loads the session
    > history, and pulls in the selected system prompt files.

3.  The AgentHarness handles the loop: calling the model endpoint,
    > tracking token counts, catching tool exceptions, and determining
    > when the task is complete.

4.  The AgentHarness exposes a stream of states or tokens back to your
    > UI layer so the user can see what the agent is doing in real-time.
    > \[2, 13\]

Does keeping the focus strictly on this **three-pillar loop structure**
make it easier to map out your Kotlin background service classes?

\[1\]
[<u>https://www.firecrawl.dev</u>](https://www.firecrawl.dev/blog/what-is-an-agent-harness)

\[2\]
[<u>https://addyosmani.com</u>](https://addyosmani.com/blog/agent-harness-engineering/)

\[3\]
[<u>https://addyosmani.com</u>](https://addyosmani.com/blog/agent-harness-engineering/)

\[4\]
[<u>https://www.reddit.com</u>](https://www.reddit.com/r/AI_Agents/comments/1ujigq2/a_lot_of_conversation_around_harness_engineering/)

\[5\]
[<u>https://www.instagram.com</u>](https://www.instagram.com/reel/Da3Do7IjSUI/)

\[6\]
[<u>https://www.instagram.com</u>](https://www.instagram.com/reel/Da3Do7IjSUI/)

\[7\]
[<u>https://www.langchain.com</u>](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness)

\[8\]
[<u>https://learn.microsoft.com</u>](https://learn.microsoft.com/en-us/agent-framework/agents/harness)

\[9\]
[<u>https://www.langchain.com</u>](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness)

\[10\]
[<u>https://medium.com</u>](https://medium.com/@erickmancz/no-code-no-mcp-no-tools-what-agentcore-harness-did-with-a-markdown-file-a2b9631a3ac7)

\[11\]
[<u>https://www.reddit.com</u>](https://www.reddit.com/r/AI_Agents/comments/1ujigq2/a_lot_of_conversation_around_harness_engineering/)

\[12\]
[<u>https://rywalker.com</u>](https://rywalker.com/harness-layer-no-moat)

\[13\]
[<u>https://www.reddit.com</u>](https://www.reddit.com/r/AI_Agents/comments/1prghg1/the_agent_harness_defining_the_behaviors/)

\[14\]
[<u>https://medium.com</u>](https://medium.com/@wasowski.jarek/ai-agent-harness-architecture-7-patterns-that-control-autonomous-agents-in-production-d07a94a9cdcd)

\[15\]
[<u>https://boringbot.substack.com</u>](https://boringbot.substack.com/p/ai-agent-harnesses-explained-architecture)

\[16\]
[<u>https://www.mindstudio.ai</u>](https://www.mindstudio.ai/blog/agent-harness-vs-framework-difference)

\[17\]
[<u>https://boringbot.substack.com</u>](https://boringbot.substack.com/p/ai-agent-harnesses-explained-architecture)

\[18\]
[<u>https://www.dawiso.com</u>](https://www.dawiso.com/glossary/agent-harness-engineering)

\[19\]
[<u>https://www.youtube.com</u>](https://www.youtube.com/watch?v=1a1VXDdIyrk)

\[20\]
[<u>https://medium.com</u>](https://medium.com/@cdcore/the-rise-of-harness-engineering-your-agent-isnt-broken-your-harness-is-8835ad7394ff)

\[21\]
[<u>https://www.mindstudio.ai</u>](https://www.mindstudio.ai/blog/what-is-an-ai-harness-infrastructure-for-agents)

\[22\]
[<u>https://www.dailydoseofds.com</u>](https://www.dailydoseofds.com/p/the-anatomy-of-an-agent-harness/)

\[23\]
[<u>https://addyosmani.com</u>](https://addyosmani.com/blog/agent-harness-engineering/)

\[24\]
[<u>https://www.mindstudio.ai</u>](https://www.mindstudio.ai/blog/ai-agent-harness-qwen-3-6-plus-chat-vs-agentic)

\[25\]
[<u>https://www.reddit.com</u>](https://www.reddit.com/r/ClaudeCode/comments/1syvsz7/the_harness_problem_why_anthropics_models_are/)

\[26\]
[<u>https://www.instagram.com</u>](https://www.instagram.com/reel/Da3Do7IjSUI/)

\[27\]
[<u>https://pub.towardsai.net</u>](https://pub.towardsai.net/agent-model-harness-what-a-coding-agent-harness-actually-is-3149945c26b5)

\[28\]
[<u>https://www.ikangai.com</u>](https://www.ikangai.com/the-agent-harness-everything-except-the-model/)

\[29\]
[<u>https://pub.towardsai.net</u>](https://pub.towardsai.net/agent-model-harness-what-a-coding-agent-harness-actually-is-3149945c26b5)
