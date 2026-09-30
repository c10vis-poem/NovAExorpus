---
source: raw/nanobot_style_personal_ai_agent_from_scratch_Marktechpost.ipynb.txt
cleaned: 2026-09-09
converter: manual (python3 json parse of notebook cells)
---

```python
import subprocess, sys

def _pip_install(*pkgs):
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-q", *pkgs], check=True)
    except Exception as e:
        print(f"(pip install skipped/failed for {pkgs}: {e})")

_HAVE_OPENAI = False
try:
    import openai
    _HAVE_OPENAI = True
except Exception:
    _pip_install("openai>=1.0.0")
    try:
        import openai
        _HAVE_OPENAI = True
    except Exception:
        _HAVE_OPENAI = False

try:
    import nest_asyncio
    nest_asyncio.apply()
except Exception:
    try:
        _pip_install("nest_asyncio")
        import nest_asyncio
        nest_asyncio.apply()
    except Exception:
        pass

import os
import re
import json
import time
import math
import asyncio
import inspect
import textwrap
import contextlib
import io
from dataclasses import dataclass, field
from typing import Any, Callable, Optional, Awaitable, get_type_hints


def banner(title: str) -> None:
    line = "═" * 78
    print(f"\n{line}\n  {title}\n{line}")


@dataclass
class ToolCall:
    """A normalized request from the model to run one tool."""
    id: str
    name: str
    arguments: dict


@dataclass
class Usage:
    prompt_tokens: int = 0
    completion_tokens: int = 0

    @property
    def total(self) -> int:
        return self.prompt_tokens + self.completion_tokens


@dataclass
class LLMResponse:
    """The single shape every provider must return."""
    content: Optional[str]
    tool_calls: list[ToolCall] = field(default_factory=list)
    finish_reason: str = "stop"
    usage: Usage = field(default_factory=Usage)


class Provider:
    """Base class. A provider turns (messages, tools) into an LLMResponse."""
    name = "base"

    async def complete(self, messages: list[dict], tools: list[dict]) -> LLMResponse:
        raise NotImplementedError


class OpenAICompatibleProvider(Provider):
    """
    Works with OpenAI and every OpenAI-compatible gateway (OpenRouter, DeepSeek,
    Together, vLLM, LM Studio, Ollama's /v1, ...). This mirrors how nanobot speaks
    to most providers under the hood.
    """
    name = "openai-compatible"

    def __init__(self, api_key: str, model: str, base_url: Optional[str] = None):
        from openai import AsyncOpenAI
        self.model = model
        self.client = AsyncOpenAI(api_key=api_key, base_url=base_url)

    async def complete(self, messages: list[dict], tools: list[dict]) -> LLMResponse:
        kwargs: dict[str, Any] = {"model": self.model, "messages": messages}
        if tools:
            kwargs["tools"] = tools
            kwargs["tool_choice"] = "auto"
        resp = await self.client.chat.completions.create(**kwargs)
        choice = resp.choices[0]
        msg = choice.message
        calls: list[ToolCall] = []
        for tc in (msg.tool_calls or []):
            try:
                args = json.loads(tc.function.arguments or "{}")
            except json.JSONDecodeError:
                args = {"_raw": tc.function.arguments}
            calls.append(ToolCall(id=tc.id, name=tc.function.name, arguments=args))
        usage = Usage(
            prompt_tokens=getattr(resp.usage, "prompt_tokens", 0) or 0,
            completion_tokens=getattr(resp.usage, "completion_tokens", 0) or 0,
        )
        return LLMResponse(
            content=msg.content,
            tool_calls=calls,
            finish_reason=choice.finish_reason or "stop",
            usage=usage,
        )


class MockProvider(Provider):
    """
    A deterministic, rule-based "LLM" so this entire tutorial runs with NO API key
    and NO network — letting you watch the agent loop, tool calls, and memory work.

    It imitates the ONE thing that matters for the loop: deciding to emit a tool call
    (in the exact normalized shape a real model would) and then, once tool results
    come back, producing a final natural-language answer. The agent loop cannot tell
    it apart from OpenAI — that's the whole point of the provider contract.
    """
    name = "mock"

    def __init__(self, model: str = "mock-1"):
        self.model = model

    @staticmethod
    def _last_user_text(messages: list[dict]) -> str:
        for m in reversed(messages):
            if m.get("role") == "user":
                c = m.get("content")
                return c if isinstance(c, str) else json.dumps(c)
        return ""

    @staticmethod
    def _already_called(messages: list[dict], tool_name: str) -> bool:
        for m in messages:
            if m.get("role") == "assistant" and m.get("tool_calls"):
                for tc in m["tool_calls"]:
                    if tc["function"]["name"] == tool_name:
                        return True
        return False

    @staticmethod
    def _extract_math(text: str) -> str:
        """Pull the first math-looking chunk out of a sentence (mock-only helper)."""
        t = re.sub(r"square roots? of (\d+(?:\.\d+)?)", r"sqrt(\1)", text)
        t = t.replace("^", "**")
        pattern = (r"(?:sqrt\(\d+(?:\.\d+)?\)|\d+(?:\.\d+)?)"
                   r"(?:\s*(?:\*\*|[\+\-\*\/])\s*(?:sqrt\(\d+(?:\.\d+)?\)|\d+(?:\.\d+)?))*")
        m = re.search(pattern, t)
        return m.group(0).strip() if m else t.strip()

    @staticmethod
    def _scan_memory(messages: list[dict]) -> tuple[Optional[str], Optional[str]]:
        """Read back simple facts from prior USER turns — proves session memory is
        actually being fed to the model (mock-only convenience)."""
        name = love = None
        for m in messages:
            if m.get("role") == "user" and isinstance(m.get("content"), str):
                tx = m["content"].lower()
                nm = re.search(r"my name is (\w+)", tx)
                if nm:
                    name = nm.group(1).title()
                lv = re.search(r"i (?:love|like) (\w+)", tx)
                if lv:
                    love = lv.group(1).title()
        return name, love

    async def complete(self, messages: list[dict], tools: list[dict]) -> LLMResponse:
        await asyncio.sleep(0)
        user = self._last_user_text(messages).lower()
        tool_names = {t["function"]["name"] for t in tools}
        usage = Usage(prompt_tokens=sum(len(str(m)) for m in messages) // 4, completion_tokens=12)

        def call(name, args):
            return LLMResponse(
                content=None,
                tool_calls=[ToolCall(id=f"call_{name}_{int(time.time()*1000)%100000}",
                                     name=name, arguments=args)],
                finish_reason="tool_calls",
                usage=usage,
            )

        has_digit = bool(re.search(r"\d", user))
        wants_math = has_digit and (
            bool(re.search(r"[\+\-\*\/\^]", user)) or "sqrt" in user
            or "square root" in user
            or any(w in user for w in ["calculate", "compute", "evaluate", "what is", "what's"]))
        if "calculator" in tool_names and wants_math and not self._already_called(messages, "calculator"):
            return call("calculator", {"expression": self._extract_math(user)})

        if "get_current_time" in tool_names and not self._already_called(messages, "get_current_time"):
            if any(w in user for w in ["time", "date", "today", "now", "o'clock"]):
                tz = "UTC"
                m = re.search(r"in ([a-zA-Z_\/ ]+)", user)
                if m:
                    cand = m.group(1).strip().title().replace(" ", "_")
                    tz = {"Tokyo": "Asia/Tokyo", "Delhi": "Asia/Kolkata",
                          "New_York": "America/New_York", "London": "Europe/London"}.get(cand, cand)
                return call("get_current_time", {"timezone": tz})

        if "remember_fact" in tool_names and not self._already_called(messages, "remember_fact"):
            m = re.search(r"my favorite (?:programming )?language is (\w+)", user)
            if m:
                return call("remember_fact", {"key": "favorite_language", "value": m.group(1)})

        if "recall_fact" in tool_names and not self._already_called(messages, "recall_fact"):
            if any(w in user for w in ["my favorite", "do you remember", "recall", "what did i tell"]):
                key = "favorite_language" if "language" in user else "note"
                return call("recall_fact", {"key": key})

        if "run_python" in tool_names and not self._already_called(messages, "run_python"):
            py_kw = any(w in user for w in ["fibonacci", "prime", "factorial", "simulate"])
            py_action = "python" in user and any(
                w in user for w in ["run", "write", "code", "print", "execute", "snippet"])
            if py_kw or py_action:
                if "fibonacci" in user:
                    code = ("def fib(n):\n a,b=0,1\n out=[]\n"
                            " for _ in range(n):\n  out.append(a); a,b=b,a+b\n return out\n"
                            "print(fib(12))")
                elif "prime" in user:
                    code = ("primes=[n for n in range(2,50) "
                            "if all(n%d for d in range(2,int(n**0.5)+1))]\nprint(primes)")
                elif "factorial" in user:
                    code = "import math; print(math.factorial(10))"
                else:
                    code = "print(sum(range(1,101)))"
                return call("run_python", {"code": code})

        if "web_search" in tool_names and not self._already_called(messages, "web_search"):
            if any(w in user for w in ["search", "look up", "latest", "news about", "find information"]):
                return call("web_search", {"query": self._last_user_text(messages)})

        if any(p in user for p in ["my name", "who am i", "what do i love", "what i love"]):
            name, love = self._scan_memory(messages)
            bits = []
            if name:
                bits.append(f"your name is {name}")
            if love:
                bits.append(f"you love {love}")
            if bits:
                return LLMResponse(content="From our conversation, " + " and ".join(bits) + ".",
                                   tool_calls=[], finish_reason="stop", usage=usage)

        tool_outputs = [m["content"] for m in messages if m.get("role") == "tool"]
        if tool_outputs:
            joined = " ".join(tool_outputs)
            answer = f"Based on the tool results, here's what I found: {joined}"
        elif any(w in user for w in ["hello", "hi", "hey"]):
            answer = "Hello! I'm a mock nanobot agent. Ask me to calculate, tell time, run Python, or remember things."
        else:
            answer = ("[mock LLM] I would normally reason about this with a real model. "
                      "Set NANOBOT_API_KEY to use a live LLM. For now, try prompts with math, "
                      "time, Python, or memory so you can see the tool loop fire.")
        return LLMResponse(content=answer, tool_calls=[], finish_reason="stop", usage=usage)
```

```python
_PYTYPE_TO_JSON = {str: "string", int: "integer", float: "number", bool: "boolean",
                   list: "array", dict: "object"}


@dataclass
class Tool:
    name: str
    description: str
    parameters: dict
    func: Callable
    is_async: bool

    def spec(self) -> dict:
        """OpenAI-style tool spec the model sees."""
        return {"type": "function",
                "function": {"name": self.name,
                             "description": self.description,
                             "parameters": self.parameters}}

    async def __call__(self, **kwargs) -> str:
        try:
            result = self.func(**kwargs)
            if inspect.isawaitable(result):
                result = await result
            return result if isinstance(result, str) else json.dumps(result, default=str)
        except Exception as e:
            return f"ERROR running tool '{self.name}': {type(e).__name__}: {e}"


def tool(func: Optional[Callable] = None, *, name: Optional[str] = None):
    """
    Decorator that turns a plain function into a Tool, deriving the JSON schema from
    type hints and the first line of the docstring. Param descriptions can be added
    with a simple 'param: description' block in the docstring.

    Example:
        @tool
        def calculator(expression: str) -> str:
            '''Evaluate a math expression and return the result.
            expression: a math expression like "2 + 2 * 3" or "sqrt(16)"'''
            ...
    """
    def make(f: Callable) -> Tool:
        hints = get_type_hints(f)
        sig = inspect.signature(f)
        doc = inspect.getdoc(f) or ""
        summary = doc.split("\n", 1)[0].strip() or f.__name__

        param_docs: dict[str, str] = {}
        for line in doc.splitlines()[1:]:
            m = re.match(r"\s*(\w+)\s*:\s*(.+)", line)
            if m and m.group(1) in sig.parameters:
                param_docs[m.group(1)] = m.group(2).strip()

        props, required = {}, []
        for pname, p in sig.parameters.items():
            if pname == "self":
                continue
            jtype = _PYTYPE_TO_JSON.get(hints.get(pname, str), "string")
            schema = {"type": jtype}
            if pname in param_docs:
                schema["description"] = param_docs[pname]
            props[pname] = schema
            if p.default is inspect.Parameter.empty:
                required.append(pname)

        parameters = {"type": "object", "properties": props, "required": required}
        return Tool(name=name or f.__name__, description=summary,
                    parameters=parameters, func=f, is_async=inspect.iscoroutinefunction(f))

    return make(func) if func else make


class ToolRegistry:
    def __init__(self):
        self._tools: dict[str, Tool] = {}

    def add(self, t: Tool) -> None:
        self._tools[t.name] = t

    def add_function(self, f: Callable) -> None:
        self.add(tool(f))

    def get(self, name: str) -> Optional[Tool]:
        return self._tools.get(name)

    def specs(self) -> list[dict]:
        return [t.spec() for t in self._tools.values()]

    def names(self) -> list[str]:
        return list(self._tools)


@tool
def calculator(expression: str) -> str:
    """Evaluate an arithmetic expression and return the numeric result.
    expression: a math expression, e.g. '2 + 2 * 3', 'sqrt(16)', '2 ** 10'"""
    allowed = {k: getattr(math, k) for k in dir(math) if not k.startswith("_")}
    allowed.update({"abs": abs, "round": round, "min": min, "max": max, "sqrt": math.sqrt})
    expr = expression.replace("^", "**")
    value = eval(expr, {"__builtins__": {}}, allowed)
    return f"{expression} = {value}"


@tool
def get_current_time(timezone: str = "UTC") -> str:
    """Return the current date and time for an IANA timezone name.
    timezone: IANA tz like 'UTC', 'Asia/Tokyo', 'Asia/Kolkata', 'America/New_York'"""
    from datetime import datetime
    try:
        from zoneinfo import ZoneInfo
        now = datetime.now(ZoneInfo(timezone))
    except Exception:
        from datetime import timezone as _tz
        now = datetime.now(_tz.utc)
        timezone = "UTC (fallback)"
    return f"Current time in {timezone}: {now.strftime('%Y-%m-%d %H:%M:%S %Z')}"


@tool
def run_python(code: str) -> str:
    """Execute a short Python snippet in a restricted namespace and return its stdout.
    code: Python source code to run; use print(...) to produce output"""
    safe_builtins = {"print": print, "range": range, "len": len, "sum": sum, "min": min,
                     "max": max, "abs": abs, "sorted": sorted, "enumerate": enumerate,
                     "list": list, "dict": dict, "set": set, "str": str, "int": int,
                     "float": float, "bool": bool, "map": map, "filter": filter,
                     "zip": zip, "all": all, "any": any, "round": round}
    import math as _m
    g = {"__builtins__": safe_builtins, "math": _m}
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            exec(code, g, {})
        out = buf.getvalue().strip()
        return f"stdout:\n{out}" if out else "(ran successfully, no stdout)"
    except Exception as e:
        return f"Python error: {type(e).__name__}: {e}"


@tool
def web_search(query: str) -> str:
    """Search the web for a query and return short result snippets (STUB).
    query: the search query string"""
    return (f"[stub results for '{query}'] (1) Overview article. (2) Official docs. "
            f"(3) Recent discussion. Swap web_search's body for a real API in production.")


def estimate_tokens(messages: list[dict]) -> int:
    """Rough token estimate (~4 chars/token) — good enough for budgeting demos."""
    chars = 0
    for m in messages:
        chars += len(str(m.get("content") or ""))
        for tc in (m.get("tool_calls") or []):
            chars += len(json.dumps(tc))
    return max(1, chars // 4)


class Memory:
    def __init__(self, token_budget: int = 3000):
        self.token_budget = token_budget
        self._sessions: dict[str, list[dict]] = {}

    def history(self, session_key: str) -> list[dict]:
        return self._sessions.setdefault(session_key, [])

    def append(self, session_key: str, message: dict) -> None:
        self.history(session_key).append(message)

    def extend(self, session_key: str, messages: list[dict]) -> None:
        self.history(session_key).extend(messages)

    def compact(self, session_key: str) -> int:
        """Drop oldest messages until under the token budget. Returns #dropped.
        Keeps tool-call/tool-result pairs consistent by trimming from the front in
        whole turns. (nanobot also summarizes; we keep it to trimming for clarity.)"""
        hist = self.history(session_key)
        dropped = 0
        while estimate_tokens(hist) > self.token_budget and len(hist) > 2:
            hist.pop(0)
            dropped += 1
        while hist and hist[0].get("role") == "tool":
            hist.pop(0); dropped += 1
        return dropped
```

```python
@dataclass
class AgentHookContext:
    iteration: int = 0
    messages: list[dict] = field(default_factory=list)
    response: Optional[LLMResponse] = None
    usage: Usage = field(default_factory=Usage)
    tool_calls: list[ToolCall] = field(default_factory=list)
    tool_results: list[str] = field(default_factory=list)
    final_content: Optional[str] = None
    stop_reason: Optional[str] = None
    error: Optional[Exception] = None


class AgentHook:
    """Subclass and override what you need. All async methods are best-effort and
    isolated (one failing hook won't crash the agent)."""
    def wants_streaming(self) -> bool:
        return False

    async def before_iteration(self, context: AgentHookContext) -> None: ...
    async def on_stream(self, context: AgentHookContext, delta: str) -> None: ...
    async def on_stream_end(self, context: AgentHookContext, *, resuming: bool) -> None: ...
    async def before_execute_tools(self, context: AgentHookContext) -> None: ...
    async def after_iteration(self, context: AgentHookContext) -> None: ...

    def finalize_content(self, context: AgentHookContext, content: str) -> str:
        return content


async def _fan_out(hooks: list[AgentHook], method: str, *args, **kwargs) -> None:
    for h in hooks:
        try:
            await getattr(h, method)(*args, **kwargs)
        except Exception as e:
            print(f"  (hook {type(h).__name__}.{method} error: {e})")


@dataclass
class Skill:
    name: str
    description: str
    instructions: str = ""
    tools: list[Tool] = field(default_factory=list)


class MCPServer:
    """Minimal stand-in for an MCP server exposing named tools."""
    def __init__(self, name: str):
        self.name = name
        self._impls: dict[str, dict] = {}

    def register(self, name: str, description: str, parameters: dict, handler: Callable):
        self._impls[name] = {"description": description, "parameters": parameters, "handler": handler}

    def list_tools(self) -> list[dict]:
        return [{"name": n, "description": v["description"], "parameters": v["parameters"]}
                for n, v in self._impls.items()]

    async def call_tool(self, name: str, arguments: dict) -> str:
        impl = self._impls[name]
        res = impl["handler"](**arguments)
        if inspect.isawaitable(res):
            res = await res
        return res if isinstance(res, str) else json.dumps(res, default=str)


def mcp_tools(server: MCPServer) -> list[Tool]:
    """Adapt every tool on an MCP server into our native Tool objects."""
    out: list[Tool] = []
    for spec in server.list_tools():
        nm = spec["name"]

        async def _runner(_nm=nm, **kwargs):
            return await server.call_tool(_nm, kwargs)

        out.append(Tool(name=f"{server.name}__{nm}",
                        description=f"[MCP:{server.name}] {spec['description']}",
                        parameters=spec["parameters"], func=_runner, is_async=True))
    return out


@dataclass
class RunResult:
    content: str
    tools_used: list[str] = field(default_factory=list)
    iterations: int = 0
    usage: Usage = field(default_factory=Usage)
    messages: list[dict] = field(default_factory=list)


class Agent:
    def __init__(self, provider: Provider, registry: ToolRegistry, memory: Memory,
                 system_prompt: str, max_iterations: int = 6, verbose: bool = True):
        self.provider = provider
        self.registry = registry
        self.memory = memory
        self.system_prompt = system_prompt
        self.max_iterations = max_iterations
        self.verbose = verbose

    def _log(self, *a):
        if self.verbose:
            print(*a)

    async def run(self, user_message: str, *, session_key: str = "default",
                  hooks: Optional[list[AgentHook]] = None,
                  extra_instructions: str = "") -> RunResult:
        hooks = hooks or []

        system = self.system_prompt
        if extra_instructions:
            system += "\n\n" + extra_instructions
        self.memory.append(session_key, {"role": "user", "content": user_message})
        dropped = self.memory.compact(session_key)
        if dropped:
            self._log(f"  · memory compaction dropped {dropped} old message(s)")
        messages = [{"role": "system", "content": system}, *self.memory.history(session_key)]

        ctx = AgentHookContext(messages=messages)
        tools_used: list[str] = []
        total = Usage()
        final_text = ""

        for i in range(1, self.max_iterations + 1):
            ctx.iteration = i
            ctx.messages = messages
            await _fan_out(hooks, "before_iteration", ctx)

            response = await self.provider.complete(messages, self.registry.specs())
            ctx.response = response
            total.prompt_tokens += response.usage.prompt_tokens
            total.completion_tokens += response.usage.completion_tokens
            ctx.usage = total

            if response.tool_calls:
                ctx.tool_calls = response.tool_calls
                self._log(f"  [iter {i}] model requested {len(response.tool_calls)} tool call(s)")
                messages.append({
                    "role": "assistant",
                    "content": response.content,
                    "tool_calls": [{"id": tc.id, "type": "function",
                                    "function": {"name": tc.name,
                                                 "arguments": json.dumps(tc.arguments)}}
                                   for tc in response.tool_calls],
                })
                await _fan_out(hooks, "before_execute_tools", ctx)

                results: list[str] = []
                for tc in response.tool_calls:
                    t = self.registry.get(tc.name)
                    if t is None:
                        result = f"ERROR: unknown tool '{tc.name}'"
                    else:
                        result = await t(**tc.arguments)
                    tools_used.append(tc.name)
                    results.append(result)
                    self._log(f"     ↳ {tc.name}({tc.arguments}) -> {result[:120]}")
                    messages.append({"role": "tool", "tool_call_id": tc.id,
                                     "content": result})
                ctx.tool_results = results
                await _fan_out(hooks, "after_iteration", ctx)
                continue

            final_text = response.content or ""
            for h in hooks:
                try:
                    final_text = h.finalize_content(ctx, final_text)
                except Exception as e:
                    print(f"  (hook {type(h).__name__}.finalize_content error: {e})")
            ctx.final_content = final_text
            ctx.stop_reason = response.finish_reason
            await _fan_out(hooks, "after_iteration", ctx)
            self.memory.append(session_key, {"role": "assistant", "content": final_text})
            break
        else:
            final_text = "(stopped: hit max_iterations without a final answer)"

        return RunResult(content=final_text, tools_used=tools_used,
                         iterations=ctx.iteration, usage=total,
                         messages=list(messages))
```

```python
DEFAULT_SYSTEM_PROMPT = (
    "You are nanobot, a concise, helpful personal AI agent. You can call tools when "
    "they help. Prefer using a tool over guessing for math, the current time, running "
    "code, web lookups, or recalling stored facts. After tools run, answer the user "
    "directly and clearly."
)


class Nanobot:
    def __init__(self, provider: Provider, *, system_prompt: str = DEFAULT_SYSTEM_PROMPT,
                 token_budget: int = 3000, max_iterations: int = 6, verbose: bool = True):
        self.registry = ToolRegistry()
        self.memory = Memory(token_budget=token_budget)
        self.skills: dict[str, Skill] = {}
        self._loaded_skills: set[str] = set()
        self._base_system = system_prompt
        self.agent = Agent(provider, self.registry, self.memory,
                           system_prompt, max_iterations=max_iterations, verbose=verbose)
        for t in (calculator, get_current_time, run_python, web_search):
            self.registry.add(t)

    @classmethod
    def auto(cls, **kw) -> "Nanobot":
        """Pick a real provider if an API key is set, else the Mock provider."""
        api_key = os.environ.get("NANOBOT_API_KEY") or os.environ.get("OPENAI_API_KEY")
        model = os.environ.get("NANOBOT_MODEL", "gpt-4o-mini")
        base_url = os.environ.get("NANOBOT_BASE_URL")
        if api_key and _HAVE_OPENAI:
            print(f"→ Using live provider: OpenAI-compatible (model={model}, base_url={base_url or 'api.openai.com'})")
            provider: Provider = OpenAICompatibleProvider(api_key, model, base_url)
        else:
            why = "no API key found" if not api_key else "openai SDK unavailable"
            print(f"→ Using Mock provider ({why}). Set NANOBOT_API_KEY for a live model.")
            provider = MockProvider()
        return cls(provider, **kw)

    def add_tool(self, f: Callable) -> "Nanobot":
        self.registry.add(tool(f) if not isinstance(f, Tool) else f)
        return self

    def register_skill(self, skill: Skill) -> "Nanobot":
        self.skills[skill.name] = skill
        return self

    def load_skill(self, name: str) -> "Nanobot":
        """Activate a skill: append its instructions and register its tools."""
        sk = self.skills[name]
        if name not in self._loaded_skills:
            self.agent.system_prompt += f"\n\n## Skill: {sk.name}\n{sk.instructions}"
            for t in sk.tools:
                self.registry.add(t)
            self._loaded_skills.add(name)
            print(f"  · loaded skill '{name}' (+{len(sk.tools)} tool(s))")
        return self

    def connect_mcp(self, server: MCPServer) -> "Nanobot":
        for t in mcp_tools(server):
            self.registry.add(t)
        print(f"  · connected MCP server '{server.name}' (+{len(server.list_tools())} tool(s))")
        return self

    async def run(self, message: str, *, session_key: str = "sdk:default",
                  hooks: Optional[list[AgentHook]] = None) -> RunResult:
        return await self.agent.run(message, session_key=session_key, hooks=hooks)


class AuditHook(AgentHook):
    """Print every tool the model decides to call."""
    def __init__(self):
        self.calls: list[str] = []

    async def before_execute_tools(self, context: AgentHookContext) -> None:
        for tc in context.tool_calls:
            self.calls.append(tc.name)
            print(f"     [audit] {tc.name}({tc.arguments})")


class TimingHook(AgentHook):
    """Measure how long each LLM iteration takes."""
    def __init__(self):
        self._t = 0.0

    async def before_iteration(self, context: AgentHookContext) -> None:
        self._t = time.perf_counter()

    async def after_iteration(self, context: AgentHookContext) -> None:
        ms = (time.perf_counter() - self._t) * 1000
        print(f"     [timing] iteration {context.iteration} took {ms:.1f} ms")


class CensorHook(AgentHook):
    """finalize_content runs as a pipeline — transform the final text."""
    def finalize_content(self, context: AgentHookContext, content: str) -> str:
        return content.replace("secret", "***") if content else content


async def demo_basic(bot: Nanobot):
    banner("DEMO 1 — Basic chat (no tools needed)")
    r = await bot.run("Hello! Who are you?", session_key="demo-basic")
    print("AGENT:", r.content)
    print(f"(iterations={r.iterations}, tools={r.tools_used}, ~tokens={r.usage.total})")


async def demo_tool_calling(bot: Nanobot):
    banner("DEMO 2 — Tool calling: math, time, and Python")
    for q in ["What is 2 ** 10 + sqrt(144)?",
              "What time is it in Tokyo?",
              "Write Python to list the first 12 Fibonacci numbers."]:
        print(f"\nUSER: {q}")
        r = await bot.run(q, session_key="demo-tools")
        print("AGENT:", r.content)


async def demo_multistep(bot: Nanobot):
    banner("DEMO 3 — Multi-step loop with an audit hook")
    audit = AuditHook()
    q = "Calculate 15 * 23, and also tell me the current time in Asia/Kolkata."
    print(f"USER: {q}")
    r = await bot.run(q, session_key="demo-multistep", hooks=[audit])
    print("AGENT:", r.content)
    print("Tools observed by hook:", audit.calls)


async def demo_memory(bot: Nanobot):
    banner("DEMO 4 — Session memory (independent histories per session_key)")
    await bot.run("My name is Ada and I love Python.", session_key="user-ada")
    await bot.run("My name is Alan and I love Haskell.", session_key="user-alan")
    r1 = await bot.run("What's my name and what do I love?", session_key="user-ada")
    r2 = await bot.run("What's my name and what do I love?", session_key="user-alan")
    print("ADA  session →", r1.content)
    print("ALAN session →", r2.content)
    print("(Each session_key kept its own conversation history — like nanobot.)")


async def demo_skills(bot: Nanobot):
    banner("DEMO 5 — Skills: load a 'research' capability on demand")
    research = Skill(
        name="research",
        description="Web research workflow",
        instructions=("When researching, first search the web, then synthesize the "
                      "snippets into a short, sourced summary."),
        tools=[web_search],
    )
    bot.register_skill(research).load_skill("research")
    r = await bot.run("Search for the latest on retrieval-augmented generation and summarize.",
                      session_key="demo-skills")
    print("AGENT:", r.content)


async def demo_mcp(bot: Nanobot):
    banner("DEMO 6 — MCP-style external tool server")
    server = MCPServer("weather")
    server.register(
        name="forecast",
        description="Get a (stub) weather forecast for a city.",
        parameters={"type": "object",
                    "properties": {"city": {"type": "string"}},
                    "required": ["city"]},
        handler=lambda city: f"Forecast for {city}: 27°C, partly cloudy (stub MCP data).",
    )
    bot.connect_mcp(server)
    print("Registered tools now include:", [n for n in bot.registry.names() if "weather" in n])
    t = bot.registry.get("weather__forecast")
    print("Direct MCP tool call →", await t(city="Delhi"))


async def demo_streaming_and_finalize(bot: Nanobot):
    banner("DEMO 7 — finalize_content pipeline + timing hook")
    q = "Compute sqrt(2) to show the math tool, then reply."
    print(f"USER: {q}")
    r = await bot.run(q, session_key="demo-hooks", hooks=[TimingHook(), CensorHook()])
    print("AGENT:", r.content)


async def demo_capstone(bot: Nanobot):
    banner("DEMO 8 — Capstone: a personal agent juggling tools + memory")
    print("A short multi-turn 'personal assistant' conversation:\n")
    turns = [
        "Remember that my favorite programming language is Python.",
        "What's 144 / 12, and what's my favorite language?",
        "Run Python to print all primes under 50.",
    ]
    for q in turns:
        print(f"USER: {q}")
        r = await bot.run(q, session_key="capstone", hooks=[AuditHook()])
        print("AGENT:", r.content, "\n")
```

```python
_FACTS: dict[str, str] = {}


@tool
def remember_fact(key: str, value: str) -> str:
    """Store a fact in long-term key-value memory.
    key: short identifier
    value: the value to store"""
    _FACTS[key] = value
    return f"Stored {key} = {value}"


@tool
def recall_fact(key: str) -> str:
    """Recall a previously stored fact by key.
    key: the identifier used when storing"""
    return _FACTS.get(key, f"(no fact stored under '{key}')")


async def main():
    banner("🐈  nanobot-from-scratch  —  building & running the core architecture")
    bot = Nanobot.auto(verbose=True)
    bot.add_tool(remember_fact).add_tool(recall_fact)
    print("Registered tools:", bot.registry.names())

    await demo_basic(bot)
    await demo_tool_calling(bot)
    await demo_multistep(bot)
    await demo_memory(bot)
    await demo_skills(bot)
    await demo_mcp(bot)
    await demo_streaming_and_finalize(bot)
    await demo_capstone(bot)

    banner("DONE")
    print(textwrap.dedent("""\
        You just built nanobot's core: a provider-agnostic agent loop with tools,
        token-budgeted session memory, lifecycle hooks, skills, and an MCP-style tool
        server — the same architecture HKUDS/nanobot ships, kept deliberately small.

        ── Run the REAL nanobot ─────────────────────────────────────────────────────
          !pip install nanobot-ai
          # configure a provider + model in ~/.nanobot/config.json, then:
          from nanobot import Nanobot as RealNanobot
          bot = RealNanobot.from_config()
          result = await bot.run("What time is it in Tokyo?")
          print(result.content)
        Docs: https://github.com/HKUDS/nanobot  •  Python SDK: docs/python-sdk.md
    """))


def _go():
    try:
        asyncio.run(main())
    except RuntimeError:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())


if __name__ == "__main__":
    _go()
```

Output:
```

══════════════════════════════════════════════════════════════════════════════
  🐈  nanobot-from-scratch  —  building & running the core architecture
══════════════════════════════════════════════════════════════════════════════
→ Using Mock provider (no API key found). Set NANOBOT_API_KEY for a live model.
Registered tools: ['calculator', 'get_current_time', 'run_python', 'web_search', 'remember_fact', 'recall_fact']

══════════════════════════════════════════════════════════════════════════════
  DEMO 1 — Basic chat (no tools needed)
══════════════════════════════════════════════════════════════════════════════
AGENT: Hello! I'm a mock nanobot agent. Ask me to calculate, tell time, run Python, or remember things.
(iterations=1, tools=[], ~tokens=97)

══════════════════════════════════════════════════════════════════════════════
  DEMO 2 — Tool calling: math, time, and Python
══════════════════════════════════════════════════════════════════════════════

USER: What is 2 ** 10 + sqrt(144)?
  [iter 1] model requested 1 tool call(s)
     ↳ calculator({'expression': '2 ** 10 + sqrt(144)'}) -> 2 ** 10 + sqrt(144) = 1036.0
AGENT: Based on the tool results, here's what I found: 2 ** 10 + sqrt(144) = 1036.0

USER: What time is it in Tokyo?
  [iter 1] model requested 1 tool call(s)
     ↳ get_current_time({'timezone': 'Asia/Tokyo'}) -> Current time in Asia/Tokyo: 2026-06-21 03:58:38 JST
AGENT: Based on the tool results, here's what I found: Current time in Asia/Tokyo: 2026-06-21 03:58:38 JST

USER: Write Python to list the first 12 Fibonacci numbers.
  [iter 1] model requested 1 tool call(s)
     ↳ run_python({'code': 'def fib(n):\n a,b=0,1\n out=[]\n for _ in range(n):\n  out.append(a); a,b=b,a+b\n return out\nprint(fib(12))'}) -> stdout:
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
AGENT: Based on the tool results, here's what I found: stdout:
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

══════════════════════════════════════════════════════════════════════════════
  DEMO 3 — Multi-step loop with an audit hook
══════════════════════════════════════════════════════════════════════════════
USER: Calculate 15 * 23, and also tell me the current time in Asia/Kolkata.
  [iter 1] model requested 1 tool call(s)
     [audit] calculator({'expression': '15 * 23'})
     ↳ calculator({'expression': '15 * 23'}) -> 15 * 23 = 345
  [iter 2] model requested 1 tool call(s)
     [audit] get_current_time({'timezone': 'Asia/Kolkata'})
     ↳ get_current_time({'timezone': 'Asia/Kolkata'}) -> Current time in Asia/Kolkata: 2026-06-21 00:28:38 IST
AGENT: Based on the tool results, here's what I found: 15 * 23 = 345 Current time in Asia/Kolkata: 2026-06-21 00:28:38 IST
Tools observed by hook: ['calculator', 'get_current_time']

══════════════════════════════════════════════════════════════════════════════
  DEMO 4 — Session memory (independent histories per session_key)
══════════════════════════════════════════════════════════════════════════════
ADA  session → From our conversation, your name is Ada and you love Python.
ALAN session → From our conversation, your name is Alan and you love Haskell.
(Each session_key kept its own conversation history — like nanobot.)

══════════════════════════════════════════════════════════════════════════════
  DEMO 5 — Skills: load a 'research' capability on demand
══════════════════════════════════════════════════════════════════════════════
  · loaded skill 'research' (+1 tool(s))
  [iter 1] model requested 1 tool call(s)
     ↳ web_search({'query': 'Search for the latest on retrieval-augmented generation and summarize.'}) -> [stub results for 'Search for the latest on retrieval-augmented generation and summarize.'] (1) Overview article. (2) Of
AGENT: Based on the tool results, here's what I found: [stub results for 'Search for the latest on retrieval-augmented generation and summarize.'] (1) Overview article. (2) Official docs. (3) Recent discussion. Swap web_search's body for a real API in production.

══════════════════════════════════════════════════════════════════════════════
  DEMO 6 — MCP-style external tool server
══════════════════════════════════════════════════════════════════════════════
  · connected MCP server 'weather' (+1 tool(s))
Registered tools now include: ['weather__forecast']
Direct MCP tool call → Forecast for Delhi: 27°C, partly cloudy (stub MCP data).

══════════════════════════════════════════════════════════════════════════════
  DEMO 7 — finalize_content pipeline + timing hook
══════════════════════════════════════════════════════════════════════════════
USER: Compute sqrt(2) to show the math tool, then reply.
  [iter 1] model requested 1 tool call(s)
     ↳ calculator({'expression': 'sqrt(2)'}) -> sqrt(2) = 1.4142135623730951
     [timing] iteration 1 took 0.3 ms
     [timing] iteration 2 took 0.1 ms
AGENT: Based on the tool results, here's what I found: sqrt(2) = 1.4142135623730951

══════════════════════════════════════════════════════════════════════════════
  DEMO 8 — Capstone: a personal agent juggling tools + memory
══════════════════════════════════════════════════════════════════════════════
A short multi-turn 'personal assistant' conversation:

USER: Remember that my favorite programming language is Python.
  [iter 1] model requested 1 tool call(s)
     [audit] remember_fact({'key': 'favorite_language', 'value': 'python'})
     ↳ remember_fact({'key': 'favorite_language', 'value': 'python'}) -> Stored favorite_language = python
  [iter 2] model requested 1 tool call(s)
     [audit] recall_fact({'key': 'favorite_language'})
     ↳ recall_fact({'key': 'favorite_language'}) -> python
AGENT: Based on the tool results, here's what I found: Stored favorite_language = python python 

USER: What's 144 / 12, and what's my favorite language?
  [iter 1] model requested 1 tool call(s)
     [audit] calculator({'expression': '144 / 12'})
     ↳ calculator({'expression': '144 / 12'}) -> 144 / 12 = 12.0
  [iter 2] model requested 1 tool call(s)
     [audit] recall_fact({'key': 'favorite_language'})
     ↳ recall_fact({'key': 'favorite_language'}) -> python
AGENT: Based on the tool results, here's what I found: 144 / 12 = 12.0 python 

USER: Run Python to print all primes under 50.
  [iter 1] model requested 1 tool call(s)
     [audit] run_python({'code': 'primes=[n for n in range(2,50) if all(n%d for d in range(2,int(n**0.5)+1))]\nprint(primes)'})
     ↳ run_python({'code': 'primes=[n for n in range(2,50) if all(n%d for d in range(2,int(n**0.5)+1))]\nprint(primes)'}) -> stdout:
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
AGENT: Based on the tool results, here's what I found: stdout:
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47] 


══════════════════════════════════════════════════════════════════════════════
  DONE
══════════════════════════════════════════════════════════════════════════════
You just built nanobot's core: a provider-agnostic agent loop with tools,
token-budgeted session memory, lifecycle hooks, skills, and an MCP-style tool
server — the same architecture HKUDS/nanobot ships, kept deliberately small.

── Run the REAL nanobot ─────────────────────────────────────────────────────
  !pip install nanobot-ai
  # configure a provider + model in ~/.nanobot/config.json, then:
  from nanobot import Nanobot as RealNanobot
  bot = RealNanobot.from_config()
  result = await bot.run("What time is it in Tokyo?")
  print(result.content)
Docs: https://github.com/HKUDS/nanobot  •  Python SDK: docs/python-sdk.md


```
