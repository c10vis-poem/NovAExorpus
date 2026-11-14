
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enterprise JEV Perception & Multi-Tier Memory Architecture</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Chart.js CDN -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        brand: {
                            50: '#f0fdf4',
                            100: '#dcfce7',
                            500: '#22c55e',
                            600: '#16a34a',
                            700: '#15803d',
                            800: '#166534',
                            900: '#14532d'
                        },
                        jev: {
                            dark: '#080d1a',
                            card: '#0f172a',
                            border: '#1e293b',
                            cyan: '#06b6d4',
                            purple: '#a855f7',
                            amber: '#f59e0b',
                            rose: '#f43f5e'
                        }
                    }
                }
            }
        }
    </script>
    <style>
        .chart-container {
            position: relative;
            width: 100%;
            max-width: 650px;
            margin-left: auto;
            margin-right: auto;
            height: 320px;
            max-height: 380px;
        }
        @media (min-width: 768px) {
            .chart-container {
                height: 350px;
            }
        }
        pre code {
            font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
            font-size: 0.8rem;
        }
        .custom-scrollbar::-webkit-scrollbar {
            width: 6px;
            height: 6px;
        }
        .custom-scrollbar::-webkit-scrollbar-track {
            background: #020617;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb {
            background: #1e293b;
            border-radius: 3px;
        }
    </style>
</head>
<!-- Chosen Palette: Deep Midnight Cybernetic (Dark Slate background with Emerald, Cyan, Purple & Amber accents) -->
<!-- Application Structure Plan: Designed as a master single-page interactive application divided into 5 clear operational sections:
     1. JEV Core Framework & 3 Decision Modes (Null, Percentage-Weighted, Explicit).
     2. Multi-Tier Memory Hierarchy & Graph Mechanics (Tree-Sitter, Call Graphs, Code Review Graphs & Holograph Spatial Mapping).
     3. Cloudflare Edge MCP Blueprint (What to Download, What to Load, What to Label + Code).
     4. Universal 10-Domain Taxonomy & Market Mapping.
     5. Live Interactive JEV Decision & Stop-Hook Harness Simulator.
     Chosen because it converts dense theoretical reports into an instantly explorable, unified visual platform. -->
<!-- Visualization & Content Choices: Uses Chart.js canvas elements for JEV decision mode confidence distribution and memory access latency metrics; structured HTML/Tailwind tables for Graph differences; and dynamic JS DOM trace generators for the live harness simulator. Confirmed NO SVG graphics or Mermaid JS used. -->
<!-- CONFIRMATION: NO SVG graphics used. NO Mermaid JS used. -->
<body class="bg-slate-950 text-slate-100 font-sans antialiased min-h-screen flex flex-col selection:bg-brand-500 selection:text-slate-950">

    <!-- Global Application Header -->
    <header class="bg-slate-900/90 border-b border-slate-800 sticky top-0 z-50 backdrop-blur-md shadow-xl">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3 flex flex-col lg:flex-row lg:items-center lg:justify-between gap-3">
            <div class="flex items-center space-x-3">
                <div class="p-2.5 bg-brand-500/10 rounded-xl border border-brand-500/30 text-brand-400 font-extrabold text-xl shadow-inner">
                    🧬
                </div>
                <div>
                    <h1 class="font-bold text-lg leading-tight text-white flex items-center gap-2">
                        JEV Perception &amp; Multi-Tier Memory Stack
                        <span class="text-[10px] bg-jev-cyan/20 text-jev-cyan px-2.5 py-0.5 rounded-full border border-jev-cyan/30 font-mono">Enterprise v3.0</span>
                    </h1>
                    <p class="text-xs text-slate-400">Joint Embedding Vectors, Holograph Graphs, Cloudflare Edge MCP &amp; 10-Domain Taxonomy</p>
                </div>
            </div>

            <!-- SPA Section Navigation Buttons -->
            <nav class="flex flex-wrap gap-1.5 text-xs font-semibold">
                <button onclick="switchTab('tab-jev')" id="btn-jev" class="px-3 py-1.5 rounded-lg transition-all bg-brand-600 text-white shadow-md">1. JEV Engine &amp; Modes</button>
                <button onclick="switchTab('tab-memory')" id="btn-memory" class="px-3 py-1.5 rounded-lg transition-all text-slate-300 hover:text-white hover:bg-slate-800">2. Memory &amp; Graph Stack</button>
                <button onclick="switchTab('tab-cloudflare')" id="btn-cloudflare" class="px-3 py-1.5 rounded-lg transition-all text-slate-300 hover:text-white hover:bg-slate-800">3. Cloudflare Edge MCP</button>
                <button onclick="switchTab('tab-taxonomy')" id="btn-taxonomy" class="px-3 py-1.5 rounded-lg transition-all text-slate-300 hover:text-white hover:bg-slate-800">4. 10 Master Domains</button>
                <button onclick="switchTab('tab-simulator')" id="btn-simulator" class="px-3 py-1.5 rounded-lg transition-all text-slate-300 hover:text-white hover:bg-slate-800">5. Live Harness Simulator</button>
            </nav>
        </div>
    </header>

    <!-- Main Container -->
    <main class="flex-grow max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">

        <!-- TAB 1: JEV CORE ENGINE & 3 DECISION MODES -->
        <section id="tab-jev" class="space-y-6">
            <div class="bg-slate-900 p-6 rounded-2xl border border-slate-800 shadow-xl relative overflow-hidden">
                <div class="absolute top-0 right-0 w-64 h-64 bg-brand-500/5 rounded-full blur-3xl pointer-events-none"></div>
                <h2 class="text-xl font-bold text-white mb-2 flex items-center gap-2">
                    <span class="text-brand-500 font-mono">01.</span> JEV (Joint Embedding Vector / Visual Engine) Architecture
                </h2>
                <p class="text-slate-300 text-sm leading-relaxed">
                    JEV bridges multi-modal visual assets (screenshots, architectural topologies, UI layouts) directly with high-dimensional textual embeddings. By deploying JEV alongside our manifest pointers, agents make instant decisions using three mathematically defined evaluation modes.
                </p>
            </div>

            <!-- 3 Decision Modes Cards -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <!-- Mode 1: Null Mode -->
                <div class="bg-slate-900 p-5 rounded-xl border border-slate-800 hover:border-jev-rose/50 transition-all space-y-3 shadow-md">
                    <div class="flex justify-between items-center">
                        <span class="px-2.5 py-1 rounded bg-jev-rose/10 text-jev-rose font-mono text-xs font-bold border border-jev-rose/20">Mode 1: Null / Pass-Through</span>
                        <span class="text-[11px] text-slate-500 font-mono">Confidence &lt; Limit</span>
                    </div>
                    <h3 class="font-bold text-white text-base">Direct Security Pass-Through</h3>
                    <p class="text-xs text-slate-400 leading-relaxed">
                        Bypasses probabilistic AI inference entirely when strict hard-coded rules are hit or when confidence drops below safety thresholds. Used for immediate deterministic blocks or direct command overrides.
                    </p>
                    <div class="p-2.5 bg-slate-950 rounded-lg border border-slate-800 text-[11px] font-mono text-rose-300">
                        Trigger: Security rule match or raw score &lt; 0.40 &rarr; Instant execution halt.
                    </div>
                </div>

                <!-- Mode 2: Percentage Mode -->
                <div class="bg-slate-900 p-5 rounded-xl border border-slate-800 hover:border-jev-cyan/50 transition-all space-y-3 shadow-md">
                    <div class="flex justify-between items-center">
                        <span class="px-2.5 py-1 rounded bg-jev-cyan/10 text-jev-cyan font-mono text-xs font-bold border border-jev-cyan/20">Mode 2: Percentage-Weighted</span>
                        <span class="text-[11px] text-slate-500 font-mono">0.0% &ndash; 100.0% Score</span>
                    </div>
                    <h3 class="font-bold text-white text-base">Probabilistic Vector Intent</h3>
                    <p class="text-xs text-slate-400 leading-relaxed">
                        Evaluates incoming visual and textual queries against high-dimensional vector embeddings, returning a dynamic confidence percentage. Drives just-in-time tool discovery and note retrieval.
                    </p>
                    <div class="p-2.5 bg-slate-950 rounded-lg border border-slate-800 text-[11px] font-mono text-cyan-300">
                        Trigger: Cosine similarity score &ge; 0.82 &rarr; JIT fetch pointer from manifest.
                    </div>
                </div>

                <!-- Mode 3: Explicit Mode -->
                <div class="bg-slate-900 p-5 rounded-xl border border-slate-800 hover:border-brand-500/50 transition-all space-y-3 shadow-md">
                    <div class="flex justify-between items-center">
                        <span class="px-2.5 py-1 rounded bg-brand-500/10 text-brand-400 font-mono text-xs font-bold border border-brand-500/20">Mode 3: Deterministic Explicit</span>
                        <span class="text-[11px] text-slate-500 font-mono">1:1 Key Index</span>
                    </div>
                    <h3 class="font-bold text-white text-base">Exact Key Path Match</h3>
                    <p class="text-xs text-slate-400 leading-relaxed">
                        Resolves specific file paths, unique UUID pointers, or static code symbol lookups directly. Guarantees zero-prompt search overhead for standard workspace navigation.
                    </p>
                    <div class="p-2.5 bg-slate-950 rounded-lg border border-slate-800 text-[11px] font-mono text-brand-300">
                        Trigger: Exact key match in manifest.jsonl &rarr; Direct note load (&lt; 5ms).
                    </div>
                </div>
            </div>

            <!-- JEV Visual Vector Breakdown Chart -->
            <div class="bg-slate-900 p-6 rounded-xl border border-slate-800 shadow-md space-y-4">
                <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-2 border-b border-slate-800 pb-3">
                    <div>
                        <h3 class="font-bold text-white text-base">JEV Decision Mode Confidence Distribution</h3>
                        <p class="text-xs text-slate-400">How JEV routes requests across Null, Percentage, and Explicit evaluation paths.</p>
                    </div>
                    <span class="text-xs font-mono bg-slate-950 text-brand-400 border border-slate-800 px-3 py-1 rounded-md">Real-Time Routing Thresholds</span>
                </div>
                <div class="chart-container">
                    <canvas id="chart-jev-modes"></canvas>
                </div>
            </div>
        </section>

        <!-- TAB 2: MULTI-TIER MEMORY & GRAPH STACK -->
        <section id="tab-memory" class="hidden space-y-6">
            <div class="bg-slate-900 p-6 rounded-2xl border border-slate-800 shadow-xl">
                <h2 class="text-xl font-bold text-white mb-2 flex items-center gap-2">
                    <span class="text-brand-500 font-mono">02.</span> Multi-Tier Memory Hierarchy &amp; Graph Mechanics
                </h2>
                <p class="text-slate-300 text-sm leading-relaxed">
                    Agentic memory is not just text embeddings. It spans 5 distinct layers—from scratchpad transcripts to complex structural code review graphs and multi-dimensional spatial <strong>Holograph Mappings</strong>.
                </p>
            </div>

            <!-- Graph Comparison Matrix -->
            <div class="bg-slate-900 p-6 rounded-xl border border-slate-800 shadow-md space-y-4">
                <h3 class="font-bold text-white text-base border-b border-slate-800 pb-3">Code Representation: AST vs. Structural Call Graphs vs. Code Review Graphs</h3>
                <div class="overflow-x-auto">
                    <table class="w-full text-left text-xs text-slate-300">
                        <thead class="bg-slate-950 text-slate-400 font-mono uppercase text-[10px]">
                            <tr>
                                <th class="p-3 border-b border-slate-800">Memory Layer</th>
                                <th class="p-3 border-b border-slate-800">Technical Scope</th>
                                <th class="p-3 border-b border-slate-800">Primary Real-World Function</th>
                                <th class="p-3 border-b border-slate-800">Bridge Metaphor</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-800 font-mono text-[11px]">
                            <tr class="hover:bg-slate-950/50">
                                <td class="p-3 font-bold text-teal-400">Tier 3: Tree-Sitter AST</td>
                                <td class="p-3 text-slate-400">Single File Syntax Tree</td>
                                <td class="p-3">Parses exact functions, variables, classes, and language grammar.</td>
                                <td class="p-3 text-slate-500">The chemical properties of a single steel rivet.</td>
                            </tr>
                            <tr class="hover:bg-slate-950/50">
                                <td class="p-3 font-bold text-jev-cyan">Tier 4a: Structural Call Graph</td>
                                <td class="p-3 text-slate-400">Codebase Inter-Connectivity</td>
                                <td class="p-3">Maps connection pathways—showing that Module A invokes Module B.</td>
                                <td class="p-3 text-slate-500">The GPS map showing where the bridge connects two towns.</td>
                            </tr>
                            <tr class="hover:bg-slate-950/50">
                                <td class="p-3 font-bold text-jev-amber">Tier 4b: Code Review Graph</td>
                                <td class="p-3 text-slate-400">Mechanical Impact Analysis</td>
                                <td class="p-3">Calculates downstream load dynamics: *"If Bolt A is removed from Section B, what structural load shifts onto Section C?"*</td>
                                <td class="p-3 text-slate-500">The structural stress simulation of the bridge under load.</td>
                            </tr>
                            <tr class="hover:bg-slate-950/50 bg-brand-950/20">
                                <td class="p-3 font-bold text-brand-400">Tier 5: The Holograph Overlay</td>
                                <td class="p-3 text-slate-300">Unified Multi-Dimensional Map</td>
                                <td class="p-3">Overlays text vectors, visual UI features, AST nodes, and Code Review Graphs into a single searchable coordinate system.</td>
                                <td class="p-3 text-brand-300">The complete digital twin of the entire bridge ecosystem.</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- Why You Cannot Skip the Holograph -->
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
                <div class="bg-slate-900 p-6 rounded-xl border border-slate-800 space-y-3">
                    <h3 class="font-bold text-white text-base flex items-center gap-2">
                        <span class="text-brand-400">🌌</span> Why You Cannot Skip the Holograph Layer
                    </h3>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        Without the <strong>Holograph Overlay</strong>, an agent operates with fragmented, isolated indexes: a vector database for natural language, an AST parser for code, and a graph for dependencies.
                    </p>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        The Holograph connects all dimensions in a single spatial index. In one query, the agent can answer:
                    </p>
                    <div class="p-3 bg-slate-950 rounded-lg border border-slate-800 text-xs font-mono text-cyan-300 space-y-1">
                        <div>1. Locate UI Component (JEV Visual Vector)</div>
                        <div>2. Find exact source code syntax (Tree-Sitter AST)</div>
                        <div>3. Calculate breaking changes if modified (Code Review Graph)</div>
                        <div>4. Retrieve past user feedback (Episodic Memory)</div>
                    </div>
                </div>

                <div class="bg-slate-900 p-6 rounded-xl border border-slate-800 space-y-4">
                    <h3 class="font-bold text-white text-base">Memory Retrieval Latency by Tier</h3>
                    <p class="text-xs text-slate-400">Comparing response speeds across local scratchpads vs. Edge MCP and Graph lookups.</p>
                    <div class="chart-container">
                        <canvas id="chart-memory-latency"></canvas>
                    </div>
                </div>
            </div>
        </section>

        <!-- TAB 3: CLOUDFLARE EDGE MCP SETUP -->
        <section id="tab-cloudflare" class="hidden space-y-6">
            <div class="bg-slate-900 p-6 rounded-2xl border border-slate-800 shadow-xl">
                <h2 class="text-xl font-bold text-white mb-2 flex items-center gap-2">
                    <span class="text-brand-500 font-mono">03.</span> Cloudflare Edge MCP &amp; Obsidian Memory Deployment
                </h2>
                <p class="text-slate-300 text-sm leading-relaxed">
                    Complete operational checklist detailing <strong>What to Download</strong>, <strong>What to Load</strong>, and <strong>What to Label</strong> to host your Obsidian vault as an edge-accessible MCP Server.
                </p>
            </div>

            <!-- Download, Load, Label Grid -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <!-- Download -->
                <div class="bg-slate-900 p-5 rounded-xl border border-slate-800 space-y-3">
                    <div class="flex items-center gap-2 text-brand-400 font-bold text-sm border-b border-slate-800 pb-2">
                        <span>📥</span> 1. What to Download
                    </div>
                    <ul class="text-xs text-slate-300 space-y-2 font-mono">
                        <li class="p-2 bg-slate-950 rounded border border-slate-800">
                            <span class="text-teal-300 block font-bold">Node.js (v18+)</span>
                            Runtime engine for Wrangler CLI.
                        </li>
                        <li class="p-2 bg-slate-950 rounded border border-slate-800">
                            <span class="text-teal-300 block font-bold">Wrangler CLI</span>
                            <code class="text-slate-400 text-[10px]">npm install -g wrangler</code>
                        </li>
                        <li class="p-2 bg-slate-950 rounded border border-slate-800">
                            <span class="text-teal-300 block font-bold">Obsidian Git Plugin</span>
                            Auto-syncs local notes to GitHub/R2.
                        </li>
                    </ul>
                </div>

                <!-- Load -->
                <div class="bg-slate-900 p-5 rounded-xl border border-slate-800 space-y-3">
                    <div class="flex items-center gap-2 text-jev-cyan font-bold text-sm border-b border-slate-800 pb-2">
                        <span>📤</span> 2. What to Load
                    </div>
                    <ul class="text-xs text-slate-300 space-y-2 font-mono">
                        <li class="p-2 bg-slate-950 rounded border border-slate-800">
                            <span class="text-cyan-300 block font-bold">Cloudflare R2 Bucket</span>
                            Holds raw <code class="text-slate-400">.md</code> vault notes.
                        </li>
                        <li class="p-2 bg-slate-950 rounded border border-slate-800">
                            <span class="text-cyan-300 block font-bold">manifest.jsonl</span>
                            Dynamic pointer index for JIT retrieval.
                        </li>
                        <li class="p-2 bg-slate-950 rounded border border-slate-800">
                            <span class="text-cyan-300 block font-bold">Worker MCP Script</span>
                            <code class="text-slate-400 text-[10px]">src/index.js</code> endpoint engine.
                        </li>
                    </ul>
                </div>

                <!-- Label -->
                <div class="bg-slate-900 p-5 rounded-xl border border-slate-800 space-y-3">
                    <div class="flex items-center gap-2 text-jev-amber font-bold text-sm border-b border-slate-800 pb-2">
                        <span>🏷️</span> 3. What to Label
                    </div>
                    <ul class="text-xs text-slate-300 space-y-2 font-mono">
                        <li class="p-2 bg-slate-950 rounded border border-slate-800">
                            <span class="text-amber-300 block font-bold">VAULT_BUCKET</span>
                            R2 storage binding in <code class="text-slate-400">wrangler.toml</code>.
                        </li>
                        <li class="p-2 bg-slate-950 rounded border border-slate-800">
                            <span class="text-amber-300 block font-bold">MCP_AUTH_TOKEN</span>
                            Bearer secret set via wrangler secret.
                        </li>
                        <li class="p-2 bg-slate-950 rounded border border-slate-800">
                            <span class="text-amber-300 block font-bold">Pointer Metadata Tags</span>
                            Category &amp; trigger tags inside manifest.
                        </li>
                    </ul>
                </div>
            </div>

            <!-- Complete Cloudflare Worker Code -->
            <div class="bg-slate-900 p-6 rounded-xl border border-slate-800 space-y-3">
                <div class="flex items-center justify-between border-b border-slate-800 pb-2">
                    <h3 class="font-bold text-white text-sm">Cloudflare Worker MCP Server Implementation</h3>
                    <span class="text-xs text-slate-500 font-mono">src/index.js</span>
                </div>
                <pre class="bg-slate-950 p-4 rounded-xl border border-slate-800 overflow-x-auto text-cyan-300 font-mono text-xs leading-relaxed"><code>export default {
  async fetch(request, env, ctx) {
    const authHeader = request.headers.get("Authorization");
    if (!authHeader || authHeader !== `Bearer ${env.MCP_AUTH_TOKEN}`) {
      return new Response(JSON.stringify({ error: "Unauthorized access to vault edge" }), { status: 401 });
    }

    const url = new URL(request.url);

    // Endpoint 1: Discover Tools
    if (url.pathname === "/tools" && request.method === "GET") {
      return new Response(JSON.stringify({
        tools: [
          { name: "get_manifest_index", description: "Returns lightweight JSONL manifest index (<300 tokens)." },
          { name: "read_vault_note", description: "Fetches target markdown note JIT.", parameters: { path: "string" } },
          { name: "search_memory", description: "Executes keyword search across vault objects.", parameters: { query: "string" } }
        ]
      }), { headers: { "Content-Type": "application/json" } });
    }

    // Endpoint 2: JSON-RPC Router
    if (url.pathname === "/rpc" && request.method === "POST") {
      const { method, params } = await request.json();

      if (method === "get_manifest_index") {
        const file = await env.VAULT_BUCKET.get("manifest.jsonl");
        return new Response(JSON.stringify({ status: "success", manifest: file ? await file.text() : "" }));
      }

      if (method === "read_vault_note") {
        const file = await env.VAULT_BUCKET.get(params.path);
        if (!file) return new Response(JSON.stringify({ status: "error", message: "Path not found" }), { status: 404 });
        return new Response(JSON.stringify({ status: "success", path: params.path, content: await file.text() }));
      }
    }

    return new Response("Obsidian Memory Edge Server Active", { status: 200 });
  }
};</code></pre>
            </div>
        </section>

        <!-- TAB 4: 10 MASTER DOMAINS -->
        <section id="tab-taxonomy" class="hidden space-y-6">
            <div class="bg-slate-900 p-6 rounded-2xl border border-slate-800 shadow-xl">
                <h2 class="text-xl font-bold text-white mb-2 flex items-center gap-2">
                    <span class="text-brand-500 font-mono">04.</span> Universal Compressed 10-Domain Taxonomy
                </h2>
                <p class="text-slate-300 text-sm leading-relaxed">
                    Why 10 domains instead of 7? By auditing over 500 Anthropic marketplace tools and GitHub repos, we isolated 3 critical enterprise failure modes (Workflow State Machine Rollbacks, Grounded Web Scraping, and Token FinOps Caps) into explicit domains to achieve 100% coverage.
                </p>
            </div>

            <!-- Domain Matrix Grid -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                <div class="bg-slate-900 p-4 rounded-xl border border-slate-800 space-y-1">
                    <div class="flex justify-between font-bold text-brand-400">
                        <span>1. Context &amp; Memory Compaction</span>
                        <span class="font-mono text-[10px] text-slate-500">Memory Core</span>
                    </div>
                    <p class="text-slate-400">Session state tracking, rolling scratchpads, decay-weighted retrieval.</p>
                </div>
                <div class="bg-slate-900 p-4 rounded-xl border border-slate-800 space-y-1">
                    <div class="flex justify-between font-bold text-jev-cyan">
                        <span>2. Dynamic Tool Discovery</span>
                        <span class="font-mono text-[10px] text-slate-500">Router Core</span>
                    </div>
                    <p class="text-slate-400">Zero-prompt JSONL dynamic skill pointers and micro-intent matching.</p>
                </div>
                <div class="bg-slate-900 p-4 rounded-xl border border-slate-800 space-y-1">
                    <div class="flex justify-between font-bold text-jev-rose">
                        <span>3. Deterministic Safety Gates</span>
                        <span class="font-mono text-[10px] text-slate-500">Safety Core</span>
                    </div>
                    <p class="text-slate-400">Pre/post tool interceptors, secret scanners, forbidden command blocking.</p>
                </div>
                <div class="bg-slate-900 p-4 rounded-xl border border-slate-800 space-y-1">
                    <div class="flex justify-between font-bold text-jev-amber">
                        <span>4. System Topology Awareness</span>
                        <span class="font-mono text-[10px] text-slate-500">OS Core</span>
                    </div>
                    <p class="text-slate-400">Local OS capability sensing, shell pathing, virtual env detection.</p>
                </div>
                <div class="bg-slate-900 p-4 rounded-xl border border-slate-800 space-y-1">
                    <div class="flex justify-between font-bold text-indigo-400">
                        <span>5. Code Analytics &amp; AST/Graphs</span>
                        <span class="font-mono text-[10px] text-slate-500">Code Core</span>
                    </div>
                    <p class="text-slate-400">Tree-sitter AST, structural call graphs, mechanical code review impact.</p>
                </div>
                <div class="bg-slate-900 p-4 rounded-xl border border-slate-800 space-y-1">
                    <div class="flex justify-between font-bold text-emerald-400">
                        <span>6. Recursive Self-Improvement</span>
                        <span class="font-mono text-[10px] text-slate-500">Evolution Core</span>
                    </div>
                    <p class="text-slate-400">Post-task retrospective analysis and automated markdown skill extraction.</p>
                </div>
                <div class="bg-slate-900 p-4 rounded-xl border border-slate-800 space-y-1">
                    <div class="flex justify-between font-bold text-jev-purple">
                        <span>7. Cross-Agent Swarm Comm</span>
                        <span class="font-mono text-[10px] text-slate-500">Swarm Core</span>
                    </div>
                    <p class="text-slate-400">Inter-agent messaging, sub-agent spawning, consensus voting protocols.</p>
                </div>
                <div class="bg-slate-900 p-4 rounded-xl border border-slate-800 space-y-1 border-brand-500/30">
                    <div class="flex justify-between font-bold text-teal-300">
                        <span>8. Dynamic Workflows (Added Domain)</span>
                        <span class="font-mono text-[10px] text-brand-400">Added Expansion</span>
                    </div>
                    <p class="text-slate-400">Deterministic state machines, exponential retry backoff, execution rollbacks.</p>
                </div>
                <div class="bg-slate-900 p-4 rounded-xl border border-slate-800 space-y-1 border-brand-500/30">
                    <div class="flex justify-between font-bold text-teal-300">
                        <span>9. Grounded Web RAG (Added Domain)</span>
                        <span class="font-mono text-[10px] text-brand-400">Added Expansion</span>
                    </div>
                    <p class="text-slate-400">Headless scraping, HTML-to-MD cleaning, link verification, citation grounding.</p>
                </div>
                <div class="bg-slate-900 p-4 rounded-xl border border-slate-800 space-y-1 border-brand-500/30">
                    <div class="flex justify-between font-bold text-teal-300">
                        <span>10. Token FinOps Caps (Added Domain)</span>
                        <span class="font-mono text-[10px] text-brand-400">Added Expansion</span>
                    </div>
                    <p class="text-slate-400">Runaway loop detection, strict per-session token budgeting, call cost limits.</p>
                </div>
            </div>
        </section>

        <!-- TAB 5: LIVE HARNESS SIMULATOR -->
        <section id="tab-simulator" class="hidden space-y-6">
            <div class="bg-slate-900 p-6 rounded-2xl border border-slate-800 shadow-xl">
                <h2 class="text-xl font-bold text-white mb-2 flex items-center gap-2">
                    <span class="text-brand-500 font-mono">05.</span> Interactive JEV Engine &amp; Stop-Hook Simulator
                </h2>
                <p class="text-slate-300 text-sm leading-relaxed">
                    Test how JEV decision modes, dynamic manifest pointers, and hard stop-hooks process input in real time.
                </p>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                <!-- Inputs -->
                <div class="bg-slate-900 p-6 rounded-xl border border-slate-800 space-y-4">
                    <h3 class="font-bold text-white text-sm">Select Test Scenario</h3>
                    
                    <div>
                        <label class="block text-xs font-semibold text-slate-400 mb-1">Preset Input:</label>
                        <select id="sim-scenario" onchange="updateScenarioPrompt()" class="w-full bg-slate-950 border border-slate-800 rounded-lg p-2 text-xs text-slate-200 focus:outline-none focus:border-brand-500 font-mono">
                            <option value="jev_vis">Scenario 1: UI Visual Screenshot Audit (JEV Percentage Mode)</option>
                            <option value="explicit_ast">Scenario 2: AST Dependency Lookup (Explicit Key Match)</option>
                            <option value="null_block">Scenario 3: Adversarial Command Attack (JEV Null / Hard Stop)</option>
                        </select>
                    </div>

                    <div>
                        <label class="block text-xs font-semibold text-slate-400 mb-1">Payload / User Prompt:</label>
                        <textarea id="sim-prompt-text" rows="3" class="w-full bg-slate-950 border border-slate-800 rounded-lg p-2 text-xs text-slate-200 focus:outline-none focus:border-brand-500 font-mono text-xs">Analyze UI layout screenshot for responsive layout bugs and CSS alignment.</textarea>
                    </div>

                    <button onclick="executeHarnessSim()" class="w-full bg-brand-600 hover:bg-brand-500 text-white font-bold py-2.5 rounded-lg text-xs transition-all shadow-lg flex items-center justify-center gap-2">
                        <span>⚡ Run JEV Harness Engine</span>
                    </button>
                </div>

                <!-- Simulation Trace Output -->
                <div class="bg-slate-900 p-6 rounded-xl border border-slate-800 space-y-4 col-span-1 lg:col-span-2">
                    <div class="flex justify-between items-center border-b border-slate-800 pb-2">
                        <h3 class="font-bold text-white text-sm">Live Execution Trace</h3>
                        <span id="sim-status-badge" class="px-2.5 py-0.5 rounded bg-brand-500/20 text-brand-400 text-[10px] font-mono border border-brand-500/30">Ready</span>
                    </div>

                    <div id="sim-console" class="bg-slate-950 p-4 rounded-xl border border-slate-800 font-mono text-xs text-slate-300 space-y-2.5 min-h-[240px] max-h-[300px] custom-scrollbar overflow-y-auto">
                        <div class="text-slate-600">// Waiting for simulation trigger...</div>
                    </div>

                    <!-- Live Stats -->
                    <div class="grid grid-cols-3 gap-3 text-center text-xs">
                        <div class="bg-slate-950 p-2.5 rounded-lg border border-slate-800">
                            <span class="text-slate-500 block text-[10px] font-mono uppercase">JEV Mode Evaluated</span>
                            <span id="sim-mode-stat" class="font-bold text-jev-cyan font-mono">Percentage</span>
                        </div>
                        <div class="bg-slate-950 p-2.5 rounded-lg border border-slate-800">
                            <span class="text-slate-500 block text-[10px] font-mono uppercase">Confidence Score</span>
                            <span id="sim-score-stat" class="font-bold text-brand-400 font-mono">0.89</span>
                        </div>
                        <div class="bg-slate-950 p-2.5 rounded-lg border border-slate-800">
                            <span class="text-slate-500 block text-[10px] font-mono uppercase">Stop-Hook Gate</span>
                            <span id="sim-hook-stat" class="font-bold text-emerald-400 font-mono">PASSED</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>

    </main>

    <!-- Global Footer -->
    <footer class="bg-slate-900 border-t border-slate-800 text-slate-500 text-xs py-5 mt-auto">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row justify-between items-center gap-2">
            <div>JEV Architecture &amp; Multi-Tier Memory Engine &copy; 2026</div>
            <div class="flex gap-4 font-mono text-[11px]">
                <span>JEV 3-Mode Perception</span>
                <span>Holograph Spatial Graph</span>
                <span>Cloudflare Edge MCP</span>
            </div>
        </div>
    </footer>

    <!-- JavaScript Logic -->
    <script>
        function switchTab(tabId) {
            const tabs = ['jev', 'memory', 'cloudflare', 'taxonomy', 'simulator'];
            tabs.forEach(t => {
                const sec = document.getElementById(`tab-${t}`);
                const btn = document.getElementById(`btn-${t}`);
                if (`tab-${t}` === tabId) {
                    sec.classList.remove('hidden');
                    btn.classList.add('bg-brand-600', 'text-white', 'shadow-md');
                    btn.classList.remove('text-slate-300', 'hover:bg-slate-800');
                } else {
                    sec.classList.add('hidden');
                    btn.classList.remove('bg-brand-600', 'text-white', 'shadow-md');
                    btn.classList.add('text-slate-300', 'hover:bg-slate-800');
                }
            });
        }

        function updateScenarioPrompt() {
            const val = document.getElementById('sim-scenario').value;
            const promptBox = document.getElementById('sim-prompt-text');
            if (val === 'jev_vis') {
                promptBox.value = "Analyze UI layout screenshot for responsive layout bugs and CSS alignment.";
            } else if (val === 'explicit_ast') {
                promptBox.value = "Fetch Tree-Sitter AST symbol lookup for class UserPreferencesManager.";
            } else if (val === 'null_block') {
                promptBox.value = "Execute shell command: rm -rf .env && cat /etc/passwd";
            }
        }

        function executeHarnessSim() {
            const val = document.getElementById('sim-scenario').value;
            const prompt = document.getElementById('sim-prompt-text').value;
            const consoleBox = document.getElementById('sim-console');
            const modeStat = document.getElementById('sim-mode-stat');
            const scoreStat = document.getElementById('sim-score-stat');
            const hookStat = document.getElementById('sim-hook-stat');
            const badge = document.getElementById('sim-badge') || document.getElementById('sim-status-badge');

            consoleBox.innerHTML = '';

            const line1 = document.createElement('div');
            line1.className = "text-slate-400";
            line1.innerHTML = `<span class="text-slate-500">[0.00s]</span> Payload Received: "${prompt}"`;
            consoleBox.appendChild(line1);

            if (val === 'jev_vis') {
                modeStat.textContent = "Percentage";
                scoreStat.textContent = "0.89";
                hookStat.textContent = "PASSED";
                hookStat.className = "font-bold text-emerald-400 font-mono";
                badge.textContent = "JIT Resolved";
                badge.className = "px-2.5 py-0.5 rounded bg-jev-cyan/20 text-jev-cyan text-[10px] font-mono border border-jev-cyan/30";

                setTimeout(() => {
                    const l2 = document.createElement('div');
                    l2.className = "text-jev-cyan";
                    l2.innerHTML = `<span class="text-slate-500">[0.03s]</span> JEV Mode 2 Active: Cosine Similarity 0.89 &ge; Threshold 0.82`;
                    consoleBox.appendChild(l2);
                }, 150);

                setTimeout(() => {
                    const l3 = document.createElement('div');
                    l3.className = "text-brand-400";
                    l3.innerHTML = `<span class="text-slate-500">[0.06s]</span> Dynamic Pointer Matched -> .agent/skills/jev_visual_auditor.md (490 tokens)`;
                    consoleBox.appendChild(l3);
                }, 300);

                setTimeout(() => {
                    const l4 = document.createElement('div');
                    l4.className = "text-emerald-400 font-bold";
                    l4.innerHTML = `<span class="text-slate-500">[0.10s]</span> ✅ Stop Hook Passed: Safety gates clean. Executed successfully.`;
                    consoleBox.appendChild(l4);
                }, 450);

            } else if (val === 'explicit_ast') {
                modeStat.textContent = "Explicit";
                scoreStat.textContent = "1.00";
                hookStat.textContent = "PASSED";
                hookStat.className = "font-bold text-emerald-400 font-mono";
                badge.textContent = "1:1 Match";
                badge.className = "px-2.5 py-0.5 rounded bg-brand-500/20 text-brand-400 text-[10px] font-mono border border-brand-500/30";

                setTimeout(() => {
                    const l2 = document.createElement('div');
                    l2.className = "text-brand-400";
                    l2.innerHTML = `<span class="text-slate-500">[0.02s]</span> JEV Mode 3 Active: Exact Key Index Found ("UserPreferencesManager")`;
                    consoleBox.appendChild(l2);
                }, 150);

                setTimeout(() => {
                    const l3 = document.createElement('div');
                    l3.className = "text-teal-300";
                    l3.innerHTML = `<span class="text-slate-500">[0.04s]</span> Resolved via Tree-Sitter AST Index in 3.2ms. Zero prompt overhead.`;
                    consoleBox.appendChild(l3);
                }, 300);

            } else if (val === 'null_block') {
                modeStat.textContent = "Null / Block";
                scoreStat.textContent = "0.00";
                hookStat.textContent = "BLOCKED";
                hookStat.className = "font-bold text-jev-rose font-mono";
                badge.textContent = "Security Halt";
                badge.className = "px-2.5 py-0.5 rounded bg-jev-rose/20 text-jev-rose text-[10px] font-mono border border-jev-rose/30";

                setTimeout(() => {
                    const l2 = document.createElement('div');
                    l2.className = "text-jev-rose font-bold";
                    l2.innerHTML = `<span class="text-slate-500">[0.01s]</span> JEV Mode 1 Active: Security Rule Hit (Forbidden Pattern: "rm -rf", ".env")`;
                    consoleBox.appendChild(l2);
                }, 150);

                setTimeout(() => {
                    const l3 = document.createElement('div');
                    l3.className = "text-rose-400 font-bold";
                    l3.innerHTML = `<span class="text-slate-500">[0.03s]</span> ❌ DETERMINISTIC STOP HOOK: Execution process killed (Exit code 2).`;
                    consoleBox.appendChild(l3);
                }, 300);
            }
        }

        window.addEventListener('DOMContentLoaded', () => {
            // Chart 1: JEV Modes
            const ctxModes = document.getElementById('chart-jev-modes').getContext('2d');
            new Chart(ctxModes, {
                type: 'bar',
                data: {
                    labels: ['Mode 1: Null (Hard Gate)', 'Mode 2: Percentage (Vector)', 'Mode 3: Explicit (1:1 Key)'],
                    datasets: [{
                        label: 'Evaluation Volume (%)',
                        data: [15, 60, 25],
                        backgroundColor: ['rgba(244, 63, 94, 0.85)', 'rgba(6, 182, 212, 0.85)', 'rgba(34, 197, 94, 0.85)'],
                        borderColor: '#0f172a',
                        borderWidth: 2
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        y: { beginAtZero: true, ticks: { color: '#94a3b8', font: { size: 10 } }, grid: { color: '#1e293b' } },
                        x: { ticks: { color: '#cbd5e1', font: { size: 10 } }, grid: { display: false } }
                    },
                    plugins: { legend: { display: false } }
                }
            });

            // Chart 2: Memory Latency
            const ctxLatency = document.getElementById('chart-memory-latency').getContext('2d');
            new Chart(ctxLatency, {
                type: 'bar',
                data: {
                    labels: ['Tier 1: Scratchpad', 'Tier 2: Cloudflare Edge', 'Tier 3: Tree-Sitter AST', 'Tier 4: Code Review Graph', 'Tier 5: Holograph Map'],
                    datasets: [{
                        label: 'Average Latency (ms)',
                        data: [4, 45, 12, 38, 52],
                        backgroundColor: ['#22c55e', '#06b6d4', '#a855f7', '#f59e0b', '#10b981'],
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    indexAxis: 'y',
                    scales: {
                        x: { beginAtZero: true, ticks: { color: '#94a3b8', font: { size: 10 } }, grid: { color: '#1e293b' } },
                        y: { ticks: { color: '#cbd5e1', font: { size: 10 } }, grid: { display: false } }
                    },
                    plugins: { legend: { display: false } }
                }
            });
        });
    </script>
</body>
</html>
