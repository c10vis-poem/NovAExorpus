---
source: How Your Forked Repos (The MCP Tools) Move into the APK.txt
type: condensed
condensed_from: NovA-Corpus/condensed/native-apk-forked-repos-integration (2026-08-20)
original_moved_to: Merovingian's_keep/_salvage/NovA-Corpus/originals/
---

# How forked repos (the MCP tools) move into a native Kotlin APK

## The Direct Answer

Ditching Termux for the core system is correct — it is a sandboxed environment that restricts performance. Termux is isolated via Android's user-space permissions, cutting off direct, low-overhead access to the Android Media SDK, the Video Game SDK, and critical system folders.

By building a Kotlin/Java UI APK, the application acts as the native system layer. The APK can communicate directly with the Qualcomm Genie X SDK / QNN / QAIRT SDK runtimes to execute inference on the Hexagon NPU with zero translation layers.

## 1. The Native APK Architecture (No Termux)

Instead of running node or python scripts inside a Termux container, the Kotlin APK runs everything natively. The MCP architecture shifts from command-line processes to In-Process Modules or Local IPC Services running inside the application's lifecycle.

```
┌────────────────────────────────────────────────────────────────────────┐
│                        YOUR CUSTOM KOTLIN UI APK                       │
├────────────────────────────────────────────────────────────────────────┤
│   ┌──────────────────────────┐          ┌──────────────────────────┐   │
│   │   SCREEN VISION SYSTEM   │          │     AUDIO INPUT/TTS      │   │
│   │   (Android Media SDK)    │          │    (Android Media SDK)   │   │
│   └────────────┬─────────────┘          └────────────┬─────────────┘   │
│                ▼                                     ▼                 │
│   ┌────────────────────────────────────────────────────────────────┐   │
│   │            QUALCOMM QNN / QAIRT SDK ENGINE (HEXAGON NPU)       │   │
│   │            - Qwen 3.5 0.8B (Query Model classification)       │   │
│   │            - Qwen 3.5 9B   (Executive Model code engine)       │   │
│   └───────────────────────────────┬────────────────────────────────┘   │
│                     ┌─────────────┴─────────────┐                      │
│                     ▼                           ▼                      │
│       ┌───────────────────────────┐┌───────────────────────────┐       │
│       │    OMNIROUTE ROUTING      ││     KAG MEMORY MESH       │       │
│       │   (Native Kotlin Class)   ││ (Graphify / Mem0 Ported)  │       │
│       └─────────────┬─────────────┘└────────────┬──────────────┘       │
│                     ▼                           ▼                      │
│   ┌────────────────────────────────────────────────────────────────┐   │
│   │           NATIVE ANDROID MCP HANDLER (Kotlin / Java)           │   │
│   │   Translates JSON-RPC Tool requests into Android OS Actions    │   │
│   └───────────────────────────────┬────────────────────────────────┘   │
│                                   ▼                                    │
│             ┌──────────────────────────────────────────┐               │
│             │ NATIVE SYSTEM OPERATIONS                 │               │
│             │ - Read/Write Files Directly              │               │
│             │ - Direct Video Game SDK Inputs           │               │
│             │ - Local Cache / SD Card Access           │               │
│             └──────────────────────────────────────────┘               │
└────────────────────────────────────────────────────────────────────────┘
```

## 2. How Forked Repos (The MCP Tools) Move into the APK

Since Termux isn't running Python or Node, GitHub repos aren't run as external command-line apps — their logic is extracted and translated into native assets or background functions inside the Kotlin app.

- **code-review-graph / graphify**: don't run Node.js — port the graph logic into a lightweight local SQLite database (compiled with an Android Graph extension) or a native Java/Kotlin graph library (e.g. JGraphT). The database lives inside the APK's private data folder (`/data/data/your.package.name/databases/`), giving the Qwen models unrestricted file-indexing speeds over local storage.
- **mem0 + ob1**: ported directly into native Kotlin classes. ob1 handles standard P2P network sockets; mem0 stores long-term memory key-values inside an encrypted local SQLite database.
- **Perplexity Search Substitution**: instead of a Python script, the Kotlin app uses `java.net.HttpURLConnection` or OkHttp for direct web API calls to Perplexity, formats the text natively into Markdown tokens, and appends it to the NPU context buffer.

## 3. The Native OmniRoute & Context Setup

In a pure native APK, OmniRoute stops being a web proxy script and becomes the core controller class of the intelligence pipeline — managing token constraints before passing data arrays to the Qualcomm QNN libraries.

Meta-Prompt compilation, natively in Kotlin, inside a Foreground Service:

```kotlin
class NativeOmniRouteController(private val context: Context) {
    private val memoryMesh = LocalKagMemoryMesh(context)
    private val codeGraph = NativeCodeIntelligenceGraph(context)

    fun compileMetaPrompt(userVoicePrompt: String, rawFrameBuffer: ByteArray): String {
        // 1. Query the native graph tool to find the exact code context needed
        val relevantCodeSnippets = codeGraph.findSnippetsForTask(userVoicePrompt)

        // 2. Fetch episodic entities from the local ported Mem0 database
        val userEntities = memoryMesh.getMem0Entities(userVoicePrompt)

        // 3. Compress tokens and build the structured Meta-Prompt layout
        val metaPrompt = """
            [SYSTEM: SYSTEM_RECOVERY_ACTIVE]
            [HARDWARE: QUALCOMM_HEXAGON_NPU]
            [EPISODIC_MEMORY: $userEntities]
            [CODE_INTELLIGENCE: $relevantCodeSnippets]
            [USER_INTENT: $userVoicePrompt]
        """.trimIndent()

        return metaPrompt
    }
}
```

## The Payoff of This Approach

1. **Total Freedom** — models are no longer blind; running natively gives direct Android file permissions to folders, tutorials, and repositories.
2. **Hardware Efficiency** — input audio and Screen Vision frames pass cleanly through memory variables into the Hexagon NPU, no terminal wrappers or network hops.
3. **Complete Sovereignty** — the entire execution plane compiles into one standalone `.apk`.
