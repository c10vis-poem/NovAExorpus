https://arxiv.org/html/2512.24601v3

Skip to main content
archive
Report Issue
Back to Abstract
Download PDF
Contents
Reading mode

Colour theme
License: CC BY 4.0
arXiv:2512.24601v3 [cs.AI] 11 May 2026
Recursive Language Models
Alex L. Zhang
†Correspondence to Alex L. Zhang, Omar Khattab <altzhang@mit.edu, okhattab@mit.edu>.
MIT CSAIL
altzhang@mit.edu
Tim Kraska
MIT CSAIL
kraska@mit.edu
Omar Khattab
MIT CSAIL
okhattab@mit.edu
Abstract
We study allowing large language models (LLMs) to process arbitrarily long prompts through the lens of inference-time scaling. We propose Recursive Language Models (RLMs), a general inference paradigm that treats long prompts as part of an external environment and allows the LLM to programmatically examine, decompose, and recursively call itself over snippets of the prompt. We find that RLMs can successfully process inputs more than an order of magnitude beyond model context window limits and, even for shorter prompts, dramatically outperform the quality of vanilla frontier LLMs and common long-context and coding scaffolds (e.g., on GPT-5 by a median across the evaluated benchmarks of 
26
%
 against compaction, 
130
%
 against CodeAct with sub-calls, and 
13
%
 against Claude Code) across four diverse long-context tasks while having comparable cost. At a small scale, we post-train the first model around the RLM. Our model, RLM-Qwen3-8B, outperforms the underlying Qwen3-8B model by a median of 
28
%
 and even approaches the quality of vanilla GPT-5 on three long-context tasks. Code is available at https://github.com/alexzhang13/rlm.

1Introduction

Figure 1:A comparison of GPT-5 and a corresponding RLM(recursion depth=1) using GPT-5 on three long-context tasks of increasing complexity: S-NIAH, OOLONG, and OOLONG-Pairs. For each task, we scale the input length from 
2
13
 to 
2
20
. GPT-5 performance degrades significantly as a function of both input length and task complexity, while the RLM maintains strong performance. Inputs beyond the red region do not fit in GPT-5’s context window of 272K tokens, but the RLM handles them effectively. Additional experiments across other models and benchmarks are in §3.
Frontier reasoning models have limited context windows and, even within their limits, tend to exhibit context rot (Hong et al., 2025), a phenomenon illustrated in Figure 1 where quality degrades steeply as prompts get longer. Though we expect context lengths to steadily rise through improvements to training, architecture, and infrastructure, we are interested in whether it is possible to scale the context size of general-purpose LLMs by orders of magnitude. This is increasingly urgent as LLMs begin to be widely adopted for long-horizon tasks, in which they must routinely process tens if not hundreds of millions of tokens.

We study this question through the lens of scaling inference-time compute. We are inspired by the way that reasoning models, another inference strategy, have become the fundamental interface to LLMs, resulting not only in empirical gains but also additional theoretical expressive power (Merrill and Sabharwal, 2024) compared to vanilla Transformers. Though most inference-time methods for dealing with long context are task-specific (Wu et al., 2021; Chang et al., 2024), the most popular general approach is context condensation or compaction (Khattab et al., 2021; Smith, 2025; OpenAI, 2025a; Wu et al., 2025), where context from user requests or agent trajectories is repeatedly summarized once it exceeds a length threshold. Unfortunately, compaction is rarely expressive enough for tasks that require dense access throughout the prompt. It presumes that some details that appear early in the prompt can safely be forgotten to make room for new content.

Refer to caption
Figure 2:A Recursive Language Model (RLM) treats prompts as part of the environment. It loads the input prompt as a variable inside a REPL environment 
ℰ
 and writes code to peek into, decompose, and invoke itself recursively over programmatic snippets of the variable.
We introduce Recursive Language Models (RLMs), a general-purpose inference paradigm for dramatically scaling the effective input and output lengths of LLMs. The key insight is that arbitrarily long user prompts should not be fed into the neural network (e.g., Transformer) directly but should instead be treated as part of the environment that the LLM is tasked to symbolically and recursively interact with. This system serves as an abstracted “language model” without context limitations.

As Figure 2 shows, an RLM exposes the same external interface as an LLM or a reasoning model: it accepts a string prompt of arbitrary structure and produces a string response. Given a prompt 
P
, the RLM initializes a Read-Eval-Print Loop (REPL) programming environment in which 
P
 is set as the value of a variable. It then offers the LLM general context about the REPL environment (e.g., the length of the string 
P
), and permits it to write code that peeks into and decomposes 
P
, and to iteratively observe any side effects from execution. Crucially, RLMs encourage the LLM to understand, transform, and execute the input prompt by writing symbolic programs that invoke the LLM itself on as many slices of the input as necessary.

By treating the prompt itself as an external object and enabling symbolic recursion, RLMs tackle limitations of expressive power in recent work on coding agents, retrieval agents, and sub-agent delegation. In particular, prior coding agents and retrieval agents treat some designated external data source (e.g., a filesystem or a corpus of search documents) as an environment for fetching snippets. However, they can only fill up the underlying LLM’s context window with snippets before facing compaction. Similarly, prior self-delegation approaches (Anthropic, 2025; Sentient AI, 2025; Schroeder et al., 2025; Sun et al., 2025) allow LLMs to invoke themselves as sub-agents. However, they are handicapped by the underlying LLM’s limited output lengths because they are designed to verbalize sub-calls autoregressively rather than producing them programmatically.

We evaluate RLMs using a frontier closed model (GPT-5; Singh et al. 2025) and a frontier open model (Qwen3-Coder-480B-A35B; Qwen Team 2025b) across four tasks with varying levels of complexity: deep research (Chen et al., 2025), information aggregation (Bertsch et al., 2025), code repository understanding (Bai et al., 2025), and a synthetic pairwise reasoning task where even frontier models fail catastrophically. We compare RLMs against direct LLM calls as well as context compaction, retrieval tool-use agents, and code-generation agents with and without sub-calls.

We find that RLMs demonstrate extremely strong performance even at the 10M+ token scale, and substantially outperform other approaches at long-context processing, in many cases by double-digit percentage gains while maintaining comparable cost. In particular, as demonstrated in Figure 1, RLMs exhibit far less severe degradation for longer contexts and more sophisticated tasks.

Finally, at a small scale, we post-train the first natively recursive language model, demonstrating that RLMs can be improved quickly with little additional training. While a small open model (Qwen3-8B; Yang et al. 2025) struggles to solve long context tasks even in an RLM scaffold, our simple general-purpose training recipe uses only 1,000 samples from unrelated domains to improve its performance by a median of 
28.3
%
 across the four evaluation tasks.

2Recursive Language Models
Given a base neural language model 
ℳ
 with maximum context size 
K
, a Recursive Language Model (RLM) is an inference-time scaffold around 
ℳ
 that treats the user prompt as part of the environment without giving up the ability to densely process its content through different calls to 
ℳ
. Given an arbitrary-length prompt string 
P
∈
Σ
⋆
, an RLM interacts with a persistent external environment 
ℰ
 and returns a response string 
Y
∈
Σ
⋆
 (Figure 2). We would like effectively unbounded input tokens (
|
P
|
≫
K
), unbounded output tokens, and an unbounded semantic horizon, e.g. the ability to do 
Ω
⁡
(
|
P
|
)
 or 
Ω
⁡
(
|
P
|
2
)
 semantic work.

Algorithm 1 describes how an RLM achieves this. Given a prompt 
P
, the RLM initializes a persistent REPL programming environment with a variable containing the user prompt as a string and a function for invoking a sub-RLM with a new prompt. Then, it starts the RLM loop. In the first iteration, the algorithm invokes the root neural model 
ℳ
 with only (constant-size) metadata about the user prompt, like its length, a short prefix, and how to access parts of it.

The root is instructed via prompting (Appendix C) and/or fine-tuning (Appendix A) to operate like an RLM: that is, to generate code that helps it understand and transform parts of its prompt 
P
, and to build up intermediate values and the final response into new variables, potentially by invoking the sub-RLM within loops. In Section 4, we find that existing LLMs can be prompted to do this and that training an 8B model to be natively recursive is promising.

Each iteration of the RLM loop executes code in the REPL, updates REPL state (intermediate variables), and collects in stdout any printed text. Only (constant-size) metadata about stdout, like a short prefix and length, is appended to 
ℳ
’s history for the next iteration.1 Once the RLM sets the variable Final inside the REPL, iteration stops and the value in Final is returned as the response.

RLMs make three simple design choices that are missing from many existing scaffolds. To highlight these, we include Algorithm 2 to illustrate a deceptively “similar” algorithm that is far less expressive. Both algorithms support some notion of sub-calls, external objects, and code execution, but they differ in terms of where the prompt and intermediate values live and where recursion occurs.

Algorithm 1 A recursive language model, around LLM 
ℳ
, which itself acts as a “language model”.
Input: prompt 
P
Output: response 
Y
state 
←
 InitREPL(prompt=P)
state 
←
 AddFunction(state,  sub_RLMM)
hist 
←
[
Metadata(state)
]
while True do
     code 
←
 LLMM(hist)
     (state, stdout) 
←
 REPL(state, code)
     hist 
←
 hist 
∥
 code 
∥
 Metadata(stdout)
     if state[Final] is set then
          return state[Final]
Algorithm 2 Alternate scaffold with standard (poor) design choices.
Input: prompt 
P
Output: response 
Y
actions 
←
{
Finish
,
Exec
,
Search
,
sub_LLM
ℳ
}
hist 
←
[
Metadata(actions)
,
P
]
 Flaw #1
while True do
     (action, val) 
←
 LLMM(hist)
     if action is Finish then
          return val Flaw #2
     out 
←
 RUN(action, val) Flaw #3
     hist 
←
 hist 
∥
 (action, val, out)
     if Tok(hist) > K then
          hist 
←
 Compact(hist)
First, an RLM must give the underlying LLM 
ℳ
 a symbolic handle to the user prompt 
P
, so the model can manipulate it without copying text into the root context window. Instead, ineffective Algorithm 2 starts by putting the user prompt 
P
 into the LLM context window (hist), inheriting the window limitations of 
ℳ
 and falling back to heuristics like context compaction. Even though the scaffold can access external data with, say, a Search action, it is bounded with respect to user input.

Second, ineffective Algorithm 2 asks 
ℳ
 to generate the output directly, via a Finish action. This may seem innocuous, but it means outputs cannot be longer than the context window of 
ℳ
.

Third, and perhaps most importantly, an RLM requires symbolic recursion. That is, code running inside 
ℰ
 must be able to invoke 
ℳ
 on programmatically constructed transformations of 
P
 (e.g., inside arbitrarily large loops), storing intermediate results symbolically. Though Algorithm 2 includes both a code execution action and a “sub-LLM” action separately, it is not able to invoke the sub-LLM programmatically and hence can only delegate a few explicitly verbalized tasks rather than writing short programs that can, say, loop over slices of the prompt and launch 
Ω
⁡
(
|
P
|
)
 or even 
Ω
⁡
(
|
P
|
2
)
 processes to understand or transform all parts of 
P
.

We implement our RLM definition in Algorithm 1 as follows: we equip an LLM with a Python REPL, where all tools, including sub-LM or sub-RLM calls, are available as modules. The initial prompt is stored as a variable in the REPL. The LLM interacts in a loop until it provides a final answer, which can be from either a variable in the REPL, or from the LLM itself. The LLM can also print from the REPL, but it is truncated to prevent overflowing the context too quickly.

3Scaling Long Context Tasks
We hypothesize that the effective context window (Hsieh et al., 2024; Goldman et al., 2025; Hong et al., 2025) of an LLM cannot be understood independently of the specific task. That is, more “complex” problems will exhibit degradation at even shorter lengths than simpler ones. Because of this, we must characterize tasks in terms of how their complexity scales with prompt length.

For example, needle-in-a-haystack (NIAH) problems generally keep ‘needles’ constant as prompt length is scaled. As a result, frontier models can now reliably solve these tasks in RULER (Hsieh et al., 2024) in the 1M+ token settings but struggle at far shorter lengths on OOLONG (Bertsch et al., 2025), a task where the answer depends explicitly on almost every line in the prompt.2

3.1Tasks
We design our evaluation around tasks where we can vary the lengths of the prompts, so we can consider problems whose difficulties scale differently with context length.

S-NIAH. Following the single needle-in-the-haystack task in RULER (Hsieh et al., 2024), we consider a set of 50 single tasks that require finding a specific phrase or number in a large set of unrelated text. Here, the information being sought scales as 
O
⁡
(
1
)
 with respect to input length.

BrowseComp-Plus (1K documents) (Chen et al., 2025). A multi-hop question-answering benchmark for DeepResearch (OpenAI, 2025b) questions that requires reasoning over multiple different documents in an offline corpus. Following Sun et al. (2025), we use 150 randomly sampled instances as our evaluation set; we provide 
1000
 randomly chosen documents as input, in which the gold and evidence documents are guaranteed to exist. We report the percentage of correct answers. The answer to each task requires piecing together information from several documents, making this harder than S-NIAH despite also requiring a constant number of documents.

OOLONG (Bertsch et al., 2025). A long reasoning benchmark that requires semantically labeling and aggregating these labels to form a final answer. We focus specifically on the trec_coarse split, a set of 
50
 tasks over a dataset of questions with semantic labels. Each task requires using nearly all dataset questions, and therefore scales linearly in processing complexity relative to the input length.

OOLONG-Pairs. A modified variant of the trec_coarse split of OOLONG with 
20
 queries that specifically require aggregating pairs of chunks to construct the final answer. We report F1 scores over the answer, which is a list of entries. Each task requires using nearly all pairs of entries of the dataset, and therefore requires processing quadratically-many items relative to the input length. In Appendix D.1, we list all queries in this benchmark.

LongBench-v2 CodeQA (Bai et al., 2025). A multi-choice code repository understanding split from LongBench-v2 that is challenging for modern frontier models. Each instance requires reasoning over a fixed number of files in a codebase to find the right answer.

3.2Methods and Baselines
We compare RLMs against commonly used task-agnostic inference methods, using two modern LMs, GPT-5 with medium reasoning (Singh et al., 2025) and default sampling parameters, and Qwen3-Coder-480B-A35B (Yang et al., 2025) using the sampling parameters described in Qwen Team (2025b). For Qwen3-Coder-480B-A35B, we compute costs based on the compute provider Fireworks (Fireworks AI, 2025). In addition to evaluating the base model on all tasks, we also evaluate the following methods and baselines:

CodeAct. We compare directly to a CodeAct (Wang et al., 2024) agent that can execute code inside of a ReAct (Yao et al., 2023) loop. Unlike an RLM, CodeAct does not offload the user prompt to the code environment, and instead provides it directly to the LM. We consider two variants: (1) a version following Jimenez et al. (2024); Chen et al. (2025) where we equip this agent with a BM25 (Robertson and Zaragoza, 2009) retriever; (2) a version with a sub-call tool inside of the REPL. Compared to RLMs, this method loads the context directly into the model.

Compaction agent. Following Sun et al. (2025); Wu et al. (2025); Yu et al. (2025), we consider an iterative agent that compacts the context as it is filled. For example, given a corpus of documents, it will iteratively accumulate the documents and summarize when full. In cases where a single document exceeds the model window, the agent will chunk the document and iteratively compact it. For the GPT-5 experiments, due to the extremely high cost of applying this strategy to millions of tokens, we use GPT-5-nano for compaction and GPT-5 to provide the final answer.

Coding agents. We compare against commonly used coding agents like OpenCode (Anomaly, 2026) and Claude Code (Anthropic, 2025). We consider two variants, one where the context is offloaded to a file, and another where it is directly used as the initial prompt. Closed source agents like Claude Code are designed around a corresponding model, so we use Claude Opus 4.1 with Claude Code v2.0.0 (released around the same time as the GPT-5 model we use in our main results) for this baseline.

RLM. We implement an RLM with a Python REPL environment, which loads a module for querying a sub-LM and uses a system prompt presented in Appendix C. For the GPT-5 experiments, we use GPT-5-mini for the recursive LMs and GPT-5 for the root LM, as we found this choice to strike a good balance between the capabilities of RLMs and the cost of the recursive calls. We also evaluate several different max recursion depths allowable to the RLM, from 0-3. Max recursion depth 0 is an RLM without sub-calling capabilities. Max recursion depth 1 allows sub-calling LLMs, while max depth >1 allows sub-calling RLMs. We notate a RLM with max recursion depth 
N
 using a model as RLM(model, depth=
N
), e.g. RLM(GPT-5, depth=2), and assume depth=1 if not stated otherwise.

Fine-tuning. To create RLM-Qwen3-8B, we fine-tune Qwen3-8B on 1,000 filtered trajectories of Qwen3-Coder-480B-A35B as an RLM with Qwen3-8B sub-calls on LongBenchPro (Chen et al., 2026) tasks. We use sampling parameters described in Qwen Team (2025a), and evaluate the fine-tuned RLM-Qwen3-8B as an RLM. The key insight for training is that being an effective sub-call model is roughly similar to being a general purpose reasoning model, so we can make the training much more tractable at small scale by focusing on improving the root model’s ability to manipulate the REPL and to launch recursive calls. We provide more training details in Appendix A.

4Results and Discussion
Table 1 reports our main evaluation results. We additionally explore how vanilla frontier model and RLM performance degrade as input contexts grow in Figure 1.

Table 1:Performance comparison of different methods across long-context benchmarks of varying complexity. In gray is the average API cost 
±
 the standard deviation of each method on each task. ∗ indicates runs where a method (sometimes) ran into input context limits. Provider costs were computed under OpenAI for GPT-5, under Fireworks for Qwen3 models, and under Anthropic for Claude Opus 4.1. All non-zero scores are rounded to at least 
0.1
.
Model	CodeQA	BrowseComp+ (1K)	OOLONG	OOLONG-Pairs
Task Length 
N
 (tokens)	23K-4.2M	6M-11M	131K	32K
GPT-5 (with RLM sub-calls to GPT-5-mini)
Base *Model**

*******