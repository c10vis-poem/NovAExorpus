You have hit on a critical design trade-off in agent architecture. The
answer is **yes and no**: while you should use the *same core structural
harness*, you must make it highly **dynamic and configurable** based on
the model's capabilities, size, and context limits. \[1\]

If you write completely different harness code for every model, your APK
will quickly become a nightmare to maintain. Instead, you should build a
single **polymorphic harness** that adapts its behavior on the fly
depending on the active model.

Here is exactly how your Kotlin harness needs to adapt based on model
characteristics:

## **1. Function Calling Capabilities (Native vs. Prompt-Engineered)**

- **High-Capability Models (e.g., Claude 3.5 Sonnet, GPT-4o):** These
  > support native tool calling. Your harness can send structured JSON
  > schemas, and the model will respond with a clean, native tool-call
  > object. \[2\]

- **Smaller/Local Models (e.g., Llama 3 8B, Phi-3):** These often
  > struggle with native tool definitions. For these, your harness must
  > switch to **Prompt-Engineered Tools**. The harness injects a massive
  > system prompt instructing the model: *"You must respond in exactly
  > this XML format to call a tool."* The harness then uses text-parsing
  > regex instead of a JSON parser to catch the tool calls. \[3\]

## **2. Context Window and Size Management (The Truncation Strategy)**

- **Large Cloud Models:** You can blindly pass 100k+ tokens of
  > conversation history and MCP tool schemas. Your harness can be
  > "lazy" about context management.

- **Small On-Device Models:** Memory is a premium. If a local model only
  > supports 4k or 8k context, a single large MCP tool schema could eat
  > up half its brain. Your harness must actively prune history,
  > summarize past turns, or **dynamically hide tool definitions** that
  > aren't relevant to the current user prompt. \[4, 5\]

## **3. Latency and Token Throughput (The Control Loop Speed)**

- **Fast/Local Models:** The loop is instantaneous. The harness can
  > afford to do rapid, multi-step thoughts (e.g., an internal "Chain of
  > Thought" loop) before showing anything to the user.

- **Slow Fallback Backends:** If a cloud backend is lagging, your
  > harness needs to stream tokens aggressively to the UI to keep the
  > user engaged, and gracefully handle connection timeouts.

## **How to Implement This in Your Kotlin APK**

Instead of writing ClaudeHarness.kt and LlamaHarness.kt, use a
**Strategy Pattern**. Define a ModelProfile data class in Kotlin that
tells your single harness how to behave.

> data class ModelProfile(  
> val name: String,  
> val maxContextTokens: Int,  
> val toolCallingStyle: ToolStyle, *// NATIVE_JSON, XML_PROMPT, or
> NONE*  
> val systemPromptTemplate: String,  
> val maxConsecutiveToolCalls: Int *// Prevents small models from
> getting stuck in infinite loops*  
> )  
>   
> enum class ToolStyle { NATIVE_JSON, XML_PROMPT, NONE }

When the user selects a model in your UI, you load its ModelProfile into
your harness. The harness loop remains exactly the same, but it uses
these properties to format the payload, decide how much history to trim,
and choose how to parse the response.

If you'd like, we can look at how to structure this **Model Profile
router** in Kotlin, or dive into how the harness should dynamically
format **MCP schemas** for smaller models. Which direction would help
most?

\[1\]
[<u>https://pydantic.dev</u>](https://pydantic.dev/articles/what-makes-a-good-harness)

\[2\]
[<u>https://www.mindstudio.ai</u>](https://www.mindstudio.ai/blog/tokens-vs-harnesses-work-layer-ai-strategy)

\[3\]
[<u>https://levelup.gitconnected.com</u>](https://levelup.gitconnected.com/your-ai-agent-isnt-broken-your-harness-is-fab18bc94420)

\[4\]
[<u>https://lightning.ai</u>](https://lightning.ai/blog/blog-what-is-agent-harness)

\[5\]
[<u>https://platform.uno</u>](https://platform.uno/blog/agentic-harness-demystified/)
