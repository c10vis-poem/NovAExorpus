{

"nbformat": 4, "nbformat\_minor": 0, "metadata": {

"colab": {

"provenance": \[\] }, "kernelspec": {

"name": "python3", "display\_name": "Python 3" }, "language\_info": { "name": "python" } }, "cells": \[

{

"cell\_type": "code", "source": \[

"import subprocess, sys\\n", "\\n", "def \_pip\_install(\*pkgs):\\n", " try:\\n", " subprocess.run(\[sys.executable, \\"-m\\", \\"pip\\", \\"install\\", \\"-q\\", \*pkgs\], check=True)\\n",

" except Exception as e:\\n", " print(f\\"(pip install skipped/failed for {pkgs}: {e})\\")\\n", "\\n", "\_HAVE\_OPENAI = False\\n", "try:\\n", " import openai\\n", " \_HAVE\_OPENAI = True\\n", "except Exception:\\n", " \_pip\_install(\\"openai\>=1.0.0\\")\\n", " try:\\n", " import openai\\n", " \_HAVE\_OPENAI = True\\n", " except Exception:\\n", " \_HAVE\_OPENAI = False\\n", "\\n", "try:\\n", " import nest\_asyncio\\n", " nest\_asyncio.apply()\\n", "except Exception:\\n", " try:\\n", " \_pip\_install(\\"nest\_asyncio\\")\\n", " import nest\_asyncio\\n", " nest\_asyncio.apply()\\n", " except Exception:\\n", " pass\\n", "\\n", "import os\\n", "import re\\n", "import json\\n", "import time\\n", "import math\\n", "import asyncio\\n", "import inspect\\n", "import textwrap\\n", "import contextlib\\n", "import io\\n", "from dataclasses import dataclass, field\\n", "from typing import Any, Callable, Optional, Awaitable, get\_type\_hints\\n", "\\n",

"\\n", "def banner(title: str) -\> None:\\n", " line = \\"â• \\" \* 78\\n", " print(f\\"\\\\n{line}\\\\n {title}\\\\n{line}\\")\\n", "\\n", "\\n", "@dataclass\\n", "class ToolCall:\\n", " \\"\\"\\"A normalized request from the model to run one tool.\\"\\"\\"\\n", " id: str\\n", " name: str\\n", " arguments: dict\\n", "\\n", "\\n", "@dataclass\\n", "class Usage:\\n", " prompt\_tokens: int = 0\\n", " completion\_tokens: int = 0\\n", "\\n", " @property\\n", " def total(self) -\> int:\\n", " return self.prompt\_tokens + self.completion\_tokens\\n", "\\n", "\\n", "@dataclass\\n", "class LLMResponse:\\n", " \\"\\"\\"The single shape every provider must return.\\"\\"\\"\\n", " content: Optional\[str\]\\n", " tool\_calls: list\[ToolCall\] = field(default\_factory=list)\\n", " finish\_reason: str = \\"stop\\"\\n", " usage: Usage = field(default\_factory=Usage)\\n", "\\n", "\\n", "class Provider:\\n", " \\"\\"\\"Base class. A provider turns (messages, tools) into an LLMResponse.\\"\\"\\"\\n",

" name = \\"base\\"\\n", "\\n", " async def complete(self, messages: list\[dict\], tools: list\[dict\]) -\> LLMResponse:\\n",

" raise NotImplementedError\\n", "\\n", "\\n", "class OpenAICompatibleProvider(Provider):\\n", " \\"\\"\\"\\n", " Works with OpenAI and every OpenAI-compatible gateway (OpenRouter, DeepSeek,\\n",

" Together, vLLM, LM Studio, Ollama's /v1, ...). This mirrors how nanobot speaks\\n", " to most providers under the hood.\\n",

" \\"\\"\\"\\n", " name = \\"openai-compatible\\"\\n", "\\n", " def \_\_init\_\_(self, api\_key: str, model: str, base\_url: Optional\[str\] = None):\\n", " from openai import AsyncOpenAI\\n",

" self.model = model\\n", " self.client = AsyncOpenAI(api\_key=api\_key, base\_url=base\_url)\\n", "\\n", " async def complete(self, messages: list\[dict\], tools: list\[dict\]) -\> LLMResponse:\\n",

" kwargs: dict\[str, Any\] = {\\"model\\": self.model, \\"messages\\": messages}\\n",

" if tools:\\n", " kwargs\[\\"tools\\"\] = tools\\n",

" kwargs\[\\"tool\_choice\\"\] = \\"auto\\"\\n", " resp = await self.client.chat.completions.create(\*\*kwargs)\\n", " choice = resp.choices\[0\]\\n", " msg = choice.message\\n", " calls: list\[ToolCall\] = \[\]\\n", " for tc in (msg.tool\_calls or \[\]):\\n", " try:\\n", " args = json.loads(tc.function.arguments or \\"{}\\")\\n", " except json.JSONDecodeError:\\n", " args = {\\"\_raw\\": tc.function.arguments}\\n", " calls.append(ToolCall(id=tc.id, name=tc.function.name, arguments=args))\\n",

" usage = Usage(\\n", " prompt\_tokens=getattr(resp.usage, \\"prompt\_tokens\\", 0) or 0,\\n", " completion\_tokens=getattr(resp.usage, \\"completion\_tokens\\", 0) or 0,\\n",

" )\\n", " return LLMResponse(\\n", " content=msg.content,\\n", " tool\_calls=calls,\\n", " finish\_reason=choice.finish\_reason or \\"stop\\",\\n", " usage=usage,\\n", " )\\n", "\\n", "\\n", "class MockProvider(Provider):\\n", " \\"\\"\\"\\n", " A deterministic, rule-based \\"LLM\\" so this entire tutorial runs with NO API key\\n",

" and NO network â€” letting you watch the agent loop, tool calls, and memory work.\\n", "\\n",

" It imitates the ONE thing that matters for the loop: deciding to emit a tool call\\n", " (in the exact normalized shape a real model would) and then, once tool results\\n",

" come back, producing a final natural-language answer. The agent loop cannot tell\\n", " it apart from OpenAI â€” that's the whole point of the provider contract.\\n",

" \\"\\"\\"\\n", " name = \\"mock\\"\\n", "\\n", " def \_\_init\_\_(self, model: str = \\"mock-1\\"):\\n", " self.model = model\\n", "\\n", " @staticmethod\\n", " def \_last\_user\_text(messages: list\[dict\]) -\> str:\\n", " for m in reversed(messages):\\n", " if m.get(\\"role\\") == \\"user\\":\\n", " c = m.get(\\"content\\")\\n", " return c if isinstance(c, str) else json.dumps(c)\\n", " return \\"\\"\\n", "\\n", " @staticmethod\\n", " def \_already\_called(messages: list\[dict\], tool\_name: str) -\> bool:\\n", " for m in messages:\\n", " if m.get(\\"role\\") == \\"assistant\\" and m.get(\\"tool\_calls\\"):\\n", " for tc in m\[\\"tool\_calls\\"\]:\\n", " if tc\[\\"function\\"\]\[\\"name\\"\] == tool\_name:\\n", " return True\\n", " return False\\n", "\\n", " @staticmethod\\n", " def \_extract\_math(text: str) -\> str:\\n", " \\"\\"\\"Pull the first math-looking chunk out of a sentence (mock-only

helper).\\"\\"\\"\\n",

" t = re.sub(r\\"square roots? of (\\\\d+(?:\\\\.\\\\d+)?)\\", r\\"sqrt(\\\\1)\\", text)\\n", " t = t.replace(\\"^\\", \\"\*\*\\")\\n",

" pattern = (r\\"(?:sqrt\\\\(\\\\d+(?:\\\\.\\\\d+)?\\\\)|\\\\d+(?:\\\\.\\\\d+)?)\\"\\n", " r\\"(?:\\\\s\*(?:\\\\\*\\\\\*|\[\\\\+\\\\-\\\\\*\\\\/\])\\\\s\*(?:sqrt\\\\(\\\\d+ (?:\\\\.\\\\d+)?\\\\)|\\\\d+(?:\\\\.\\\\d+)?))\*\\")\\n",

" m = re.search(pattern, t)\\n", " return m.group(0).strip() if m else t.strip()\\n", "\\n", " @staticmethod\\n", " def \_scan\_memory(messages: list\[dict\]) -\> tuple\[Optional\[str\], Optional\[str\]\]:\\n",

" \\"\\"\\"Read back simple facts from prior USER turns â€” proves session memory is\\n",

" actually being fed to the model (mock-only convenience).\\"\\"\\"\\n", " name = love = None\\n", " for m in messages:\\n", " if m.get(\\"role\\") == \\"user\\" and isinstance(m.get(\\"content\\"), str):\\n", " tx = m\[\\"content\\"\].lower()\\n",

" nm = re.search(r\\"my name is (\\\\w+)\\", tx)\\n", " if nm:\\n", " name = nm.group(1).title()\\n", " lv = re.search(r\\"i (?:love|like) (\\\\w+)\\", tx)\\n", " if lv:\\n", " love = lv.group(1).title()\\n", " return name, love\\n", "\\n", " async def complete(self, messages: list\[dict\], tools: list\[dict\]) -\> LLMResponse:\\n",

" await asyncio.sleep(0)\\n", " user = self.\_last\_user\_text(messages).lower()\\n", " tool\_names = {t\[\\"function\\"\]\[\\"name\\"\] for t in tools}\\n", " usage = Usage(prompt\_tokens=sum(len(str(m)) for m in messages) // 4, completion\_tokens=12)\\n",

"\\n", " def call(name, args):\\n", " return LLMResponse(\\n", " content=None,\\n", " tool\_calls= \[ToolCall(id=f\\"call\_{name}\_{int(time.time()\*1000)%100000}\\",\\n",

" name=name, arguments=args)\],\\n", " finish\_reason=\\"tool\_calls\\",\\n", " usage=usage,\\n", " )\\n", "\\n", " has\_digit = bool(re.search(r\\"\\\\d\\", user))\\n", " wants\_math = has\_digit and (\\n", " bool(re.search(r\\"\[\\\\+\\\\-\\\\\*\\\\/\\\\^\]\\", user)) or \\"sqrt\\" in user\\n", " or \\"square root\\" in user\\n", " or any(w in user for w in \[\\"calculate\\", \\"compute\\", \\"evaluate\\", \\"what is\\", \\"what's\\"\]))\\n",

" if \\"calculator\\" in tool\_names and wants\_math and not self.\_already\_called(messages, \\"calculator\\"):\\n",

" return call(\\"calculator\\", {\\"expression\\": self.\_extract\_math(user)})\\n",

"\\n", " if \\"get\_current\_time\\" in tool\_names and not self.\_already\_called(messages, \\"get\_current\_time\\"):\\n",

" if any(w in user for w in \[\\"time\\", \\"date\\", \\"today\\", \\"now\\", \\"o'clock\\"\]):\\n",

" tz = \\"UTC\\"\\n", " m = re.search(r\\"in (\[a-zA-Z\_\\\\/ \]+)\\", user)\\n", " if m:\\n",

" cand = m.group(1).strip().title().replace(\\" \\", \\"\_\\")\\n", " tz = {\\"Tokyo\\": \\"Asia/Tokyo\\", \\"Delhi\\": \\"Asia/Kolkata\\",\\n",

" \\"New\_York\\": \\"America/New\_York\\", \\"London\\": \\"Europe/London\\"}.get(cand, cand)\\n",

" return call(\\"get\_current\_time\\", {\\"timezone\\": tz})\\n", "\\n", " if \\"remember\_fact\\" in tool\_names and not self.\_already\_called(messages, \\"remember\_fact\\"):\\n",

" m = re.search(r\\"my favorite (?:programming )?language is (\\\\w+)\\", user)\\n", " if m:\\n",

" return call(\\"remember\_fact\\", {\\"key\\": \\"favorite\_language\\", \\"value\\": m.group(1)})\\n",

"\\n", " if \\"recall\_fact\\" in tool\_names and not self.\_already\_called(messages, \\"recall\_fact\\"):\\n",

" if any(w in user for w in \[\\"my favorite\\", \\"do you remember\\", \\"recall\\", \\"what did i tell\\"\]):\\n",

" key = \\"favorite\_language\\" if \\"language\\" in user else \\"note\\"\\n",

" return call(\\"recall\_fact\\", {\\"key\\": key})\\n", "\\n", " if \\"run\_python\\" in tool\_names and not self.\_already\_called(messages, \\"run\_python\\"):\\n",

" py\_kw = any(w in user for w in \[\\"fibonacci\\", \\"prime\\", \\"factorial\\", \\"simulate\\"\])\\n",

" py\_action = \\"python\\" in user and any(\\n", " w in user for w in \[\\"run\\", \\"write\\", \\"code\\", \\"print\\", \\"execute\\", \\"snippet\\"\])\\n",

" if py\_kw or py\_action:\\n", " if \\"fibonacci\\" in user:\\n", " code = (\\"def fib(n):\\\\n a,b=0,1\\\\n out=\[\]\\\\n\\"\\n", " \\" for \_ in range(n):\\\\n out.append(a); a,b=b,a+b\\\\n return out\\\\n\\"\\n",

" \\"print(fib(12))\\")\\n", " elif \\"prime\\" in user:\\n", " code = (\\"primes=\[n for n in range(2,50) \\"\\n", " \\"if all(n%d for d in range(2,int(n\*\*0.5)+1))\]\\\\nprint(primes)\\")\\n",

" elif \\"factorial\\" in user:\\n", " code = \\"import math; print(math.factorial(10))\\"\\n", " else:\\n", " code = \\"print(sum(range(1,101)))\\"\\n", " return call(\\"run\_python\\", {\\"code\\": code})\\n", "\\n", " if \\"web\_search\\" in tool\_names and not self.\_already\_called(messages, \\"web\_search\\"):\\n",

" if any(w in user for w in \[\\"search\\", \\"look up\\", \\"latest\\", \\"news about\\", \\"find information\\"\]):\\n",

" return call(\\"web\_search\\", {\\"query\\": self.\_last\_user\_text(messages)})\\n",

"\\n", " if any(p in user for p in \[\\"my name\\", \\"who am i\\", \\"what do i love\\", \\"what i love\\"\]):\\n",

" name, love = self.\_scan\_memory(messages)\\n", " bits = \[\]\\n", " if name:\\n", " bits.append(f\\"your name is {name}\\")\\n", " if love:\\n", " bits.append(f\\"you love {love}\\")\\n", " if bits:\\n", " return LLMResponse(content=\\"From our conversation, \\" + \\" and \\".join(bits) + \\".\\",\\n",

" tool\_calls=\[\], finish\_reason=\\"stop\\",

usage=usage)\\n",

"\\n", " tool\_outputs = \[m\[\\"content\\"\] for m in messages if m.get(\\"role\\") == \\"tool\\"\]\\n",

" if tool\_outputs:\\n", " joined = \\" \\".join(tool\_outputs)\\n", " answer = f\\"Based on the tool results, here's what I found: {joined}\\"\\n",

" elif any(w in user for w in \[\\"hello\\", \\"hi\\", \\"hey\\"\]):\\n", " answer = \\"Hello\! I'm a mock nanobot agent. Ask me to calculate, tell time, run Python, or remember things.\\"\\n",

" else:\\n", " answer = (\\"\[mock LLM\] I would normally reason about this with a real model. \\"\\n",

" \\"Set NANOBOT\_API\_KEY to use a live LLM. For now, try prompts with math, \\"\\n",

" \\"time, Python, or memory so you can see the tool loop fire.\\")\\n",

" return LLMResponse(content=answer, tool\_calls=\[\], finish\_reason=\\"stop\\", usage=usage)"

\], "metadata": {

"id": "tfoii-P4bxrW" }, "execution\_count": null, "outputs": \[\] }, {

"cell\_type": "code", "source": \[

"\_PYTYPE\_TO\_JSON = {str: \\"string\\", int: \\"integer\\", float: \\"number\\", bool: \\"boolean\\",\\n",

" list: \\"array\\", dict: \\"object\\"}\\n", "\\n", "\\n", "@dataclass\\n", "class Tool:\\n", " name: str\\n", " description: str\\n", " parameters: dict\\n", " func: Callable\\n", " is\_async: bool\\n", "\\n", " def spec(self) -\> dict:\\n", " \\"\\"\\"OpenAI-style tool spec the model sees.\\"\\"\\"\\n", " return {\\"type\\": \\"function\\",\\n", " \\"function\\": {\\"name\\": self.name,\\n", " \\"description\\": self.description,\\n", " \\"parameters\\": self.parameters}}\\n", "\\n", " async def \_\_call\_\_(self, \*\*kwargs) -\> str:\\n", " try:\\n", " result = self.func(\*\*kwargs)\\n", " if inspect.isawaitable(result):\\n", " result = await result\\n", " return result if isinstance(result, str) else json.dumps(result, default=str)\\n",

" except Exception as e:\\n", " return f\\"ERROR running tool '{self.name}': {type(e).\_\_name\_\_}: {e}\\"\\n", "\\n", "\\n", "def tool(func: Optional\[Callable\] = None, \*, name: Optional\[str\] = None):\\n", " \\"\\"\\"\\n", " Decorator that turns a plain function into a Tool, deriving the JSON schema

from\\n", " type hints and the first line of the docstring. Param descriptions can be added\\n", " with a simple 'param: description' block in the docstring.\\n",

"\\n", " Example:\\n", " @tool\\n", " def calculator(expression: str) -\> str:\\n", " '''Evaluate a math expression and return the result.\\n", " expression: a math expression like \\"2 + 2 \* 3\\" or \\"sqrt(16)\\"'''\\n", " ...\\n", " \\"\\"\\"\\n", " def make(f: Callable) -\> Tool:\\n", " hints = get\_type\_hints(f)\\n", " sig = inspect.signature(f)\\n", " doc = inspect.getdoc(f) or \\"\\"\\n", " summary = doc.split(\\"\\\\n\\", 1)\[0\].strip() or f.\_\_name\_\_\\n", "\\n", " param\_docs: dict\[str, str\] = {}\\n", " for line in doc.splitlines()\[1:\]:\\n", " m = re.match(r\\"\\\\s\*(\\\\w+)\\\\s\*:\\\\s\*(.+)\\", line)\\n", " if m and m.group(1) in sig.parameters:\\n", " param\_docs\[m.group(1)\] = m.group(2).strip()\\n", "\\n", " props, required = {}, \[\]\\n", " for pname, p in sig.parameters.items():\\n", " if pname == \\"self\\":\\n", " continue\\n", " jtype = \_PYTYPE\_TO\_JSON.get(hints.get(pname, str), \\"string\\")\\n", " schema = {\\"type\\": jtype}\\n", " if pname in param\_docs:\\n", " schema\[\\"description\\"\] = param\_docs\[pname\]\\n", " props\[pname\] = schema\\n", " if p.default is inspect.Parameter.empty:\\n", " required.append(pname)\\n", "\\n", " parameters = {\\"type\\": \\"object\\", \\"properties\\": props, \\"required\\": required}\\n",

" return Tool(name=name or f.\_\_name\_\_, description=summary,\\n", " parameters=parameters, func=f, is\_async=inspect.iscoroutinefunction(f))\\n",

"\\n", " return make(func) if func else make\\n", "\\n", "\\n", "class ToolRegistry:\\n", " def \_\_init\_\_(self):\\n", " self.\_tools: dict\[str, Tool\] = {}\\n", "\\n", " def add(self, t: Tool) -\> None:\\n", " self.\_tools\[t.name\] = t\\n", "\\n", " def add\_function(self, f: Callable) -\> None:\\n", " self.add(tool(f))\\n", "\\n", " def get(self, name: str) -\> Optional\[Tool\]:\\n", " return self.\_tools.get(name)\\n", "\\n", " def specs(self) -\> list\[dict\]:\\n", " return \[t.spec() for t in self.\_tools.values()\]\\n", "\\n", " def names(self) -\> list\[str\]:\\n", " return list(self.\_tools)\\n", "\\n", "\\n",

"@tool\\n", "def calculator(expression: str) -\> str:\\n", " \\"\\"\\"Evaluate an arithmetic expression and return the numeric result.\\n", " expression: a math expression, e.g. '2 + 2 \* 3', 'sqrt(16)', '2 \*\* 10'\\"\\"\\"\\n",

" allowed = {k: getattr(math, k) for k in dir(math) if not k.startswith(\\"\_\\")}\\n",

" allowed.update({\\"abs\\": abs, \\"round\\": round, \\"min\\": min, \\"max\\": max, \\"sqrt\\": math.sqrt})\\n",

" expr = expression.replace(\\"^\\", \\"\*\*\\")\\n", " value = eval(expr, {\\"\_\_builtins\_\_\\": {}}, allowed)\\n", " return f\\"{expression} = {value}\\"\\n", "\\n", "\\n", "@tool\\n", "def get\_current\_time(timezone: str = \\"UTC\\") -\> str:\\n", " \\"\\"\\"Return the current date and time for an IANA timezone name.\\n", " timezone: IANA tz like 'UTC', 'Asia/Tokyo', 'Asia/Kolkata', 'America/New\_York'\\"\\"\\"\\n",

" from datetime import datetime\\n", " try:\\n", " from zoneinfo import ZoneInfo\\n", " now = datetime.now(ZoneInfo(timezone))\\n", " except Exception:\\n", " from datetime import timezone as \_tz\\n", " now = datetime.now(\_tz.utc)\\n", " timezone = \\"UTC (fallback)\\"\\n", " return f\\"Current time in {timezone}: {now.strftime('%Y-%m-%d %H:%M:%S %Z')}\\"\\n",

"\\n", "\\n", "@tool\\n", "def run\_python(code: str) -\> str:\\n", " \\"\\"\\"Execute a short Python snippet in a restricted namespace and return its stdout.\\n",

" code: Python source code to run; use print(...) to produce output\\"\\"\\"\\n", " safe\_builtins = {\\"print\\": print, \\"range\\": range, \\"len\\": len, \\"sum\\": sum, \\"min\\": min,\\n",

" \\"max\\": max, \\"abs\\": abs, \\"sorted\\": sorted, \\"enumerate\\": enumerate,\\n",

" \\"list\\": list, \\"dict\\": dict, \\"set\\": set, \\"str\\": str, \\"int\\": int,\\n",

" \\"float\\": float, \\"bool\\": bool, \\"map\\": map, \\"filter\\": filter,\\n",

" \\"zip\\": zip, \\"all\\": all, \\"any\\": any, \\"round\\": round}\\n", " import math as \_m\\n",

" g = {\\"\_\_builtins\_\_\\": safe\_builtins, \\"math\\": \_m}\\n", " buf = io.StringIO()\\n", " try:\\n", " with contextlib.redirect\_stdout(buf):\\n", " exec(code, g, {})\\n", " out = buf.getvalue().strip()\\n", " return f\\"stdout:\\\\n{out}\\" if out else \\"(ran successfully, no stdout)\\"\\n",

" except Exception as e:\\n", " return f\\"Python error: {type(e).\_\_name\_\_}: {e}\\"\\n", "\\n", "\\n", "@tool\\n", "def web\_search(query: str) -\> str:\\n", " \\"\\"\\"Search the web for a query and return short result snippets (STUB).\\n", " query: the search query string\\"\\"\\"\\n", " return (f\\"\[stub results for '{query}'\] (1) Overview article. (2) Official docs. \\"\\n",

" f\\"(3) Recent discussion. Swap web\_search's body for a real API in production.\\")\\n",

"\\n", "\\n", "def estimate\_tokens(messages: list\[dict\]) -\> int:\\n", " \\"\\"\\"Rough token estimate (\~4 chars/token) â€” good enough for budgeting demos.\\"\\"\\"\\n",

" chars = 0\\n", " for m in messages:\\n", " chars += len(str(m.get(\\"content\\") or \\"\\"))\\n", " for tc in (m.get(\\"tool\_calls\\") or \[\]):\\n", " chars += len(json.dumps(tc))\\n", " return max(1, chars // 4)\\n", "\\n", "\\n", "class Memory:\\n", " def \_\_init\_\_(self, token\_budget: int = 3000):\\n", " self.token\_budget = token\_budget\\n", " self.\_sessions: dict\[str, list\[dict\]\] = {}\\n", "\\n", " def history(self, session\_key: str) -\> list\[dict\]:\\n", " return self.\_sessions.setdefault(session\_key, \[\])\\n", "\\n", " def append(self, session\_key: str, message: dict) -\> None:\\n", " self.history(session\_key).append(message)\\n", "\\n", " def extend(self, session\_key: str, messages: list\[dict\]) -\> None:\\n", " self.history(session\_key).extend(messages)\\n", "\\n", " def compact(self, session\_key: str) -\> int:\\n", " \\"\\"\\"Drop oldest messages until under the token budget. Returns \#dropped.\\n",

" Keeps tool-call/tool-result pairs consistent by trimming from the front in\\n",

" whole turns. (nanobot also summarizes; we keep it to trimming for clarity.)\\"\\"\\"\\n",

" hist = self.history(session\_key)\\n", " dropped = 0\\n", " while estimate\_tokens(hist) \> self.token\_budget and len(hist) \> 2:\\n", " hist.pop(0)\\n", " dropped += 1\\n", " while hist and hist\[0\].get(\\"role\\") == \\"tool\\":\\n", " hist.pop(0); dropped += 1\\n", " return dropped" \], "metadata": {

"id": "W6AkHJ\_abxg9" }, "execution\_count": null, "outputs": \[\] }, {

"cell\_type": "code", "source": \[

"@dataclass\\n", "class AgentHookContext:\\n", " iteration: int = 0\\n", " messages: list\[dict\] = field(default\_factory=list)\\n", " response: Optional\[LLMResponse\] = None\\n", " usage: Usage = field(default\_factory=Usage)\\n", " tool\_calls: list\[ToolCall\] = field(default\_factory=list)\\n", " tool\_results: list\[str\] = field(default\_factory=list)\\n", " final\_content: Optional\[str\] = None\\n", " stop\_reason: Optional\[str\] = None\\n", " error: Optional\[Exception\] = None\\n",

"\\n", "\\n", "class AgentHook:\\n", " \\"\\"\\"Subclass and override what you need. All async methods are best-effort and\\n",

" isolated (one failing hook won't crash the agent).\\"\\"\\"\\n", " def wants\_streaming(self) -\> bool:\\n", " return False\\n", "\\n", " async def before\_iteration(self, context: AgentHookContext) -\> None: ...\\n", " async def on\_stream(self, context: AgentHookContext, delta: str) -\> None: ...\\n",

" async def on\_stream\_end(self, context: AgentHookContext, \*, resuming: bool) -\> None: ...\\n",

" async def before\_execute\_tools(self, context: AgentHookContext) -\> None: ...\\n",

" async def after\_iteration(self, context: AgentHookContext) -\> None: ...\\n", "\\n", " def finalize\_content(self, context: AgentHookContext, content: str) -\> str:\\n", " return content\\n", "\\n", "\\n", "async def \_fan\_out(hooks: list\[AgentHook\], method: str, \*args, \*\*kwargs) -\> None:\\n", " for h in hooks:\\n", " try:\\n", " await getattr(h, method)(\*args, \*\*kwargs)\\n", " except Exception as e:\\n", " print(f\\" (hook {type(h).\_\_name\_\_}.{method} error: {e})\\")\\n", "\\n", "\\n", "@dataclass\\n", "class Skill:\\n", " name: str\\n", " description: str\\n", " instructions: str = \\"\\"\\n", " tools: list\[Tool\] = field(default\_factory=list)\\n", "\\n", "\\n", "class MCPServer:\\n", " \\"\\"\\"Minimal stand-in for an MCP server exposing named tools.\\"\\"\\"\\n", " def \_\_init\_\_(self, name: str):\\n", " self.name = name\\n", " self.\_impls: dict\[str, dict\] = {}\\n", "\\n", " def register(self, name: str, description: str, parameters: dict, handler: Callable):\\n",

" self.\_impls\[name\] = {\\"description\\": description, \\"parameters\\": parameters, \\"handler\\": handler}\\n",

"\\n", " def list\_tools(self) -\> list\[dict\]:\\n", " return \[{\\"name\\": n, \\"description\\": v\[\\"description\\"\], \\"parameters\\": v\[\\"parameters\\"\]}\\n",

" for n, v in self.\_impls.items()\]\\n", "\\n", " async def call\_tool(self, name: str, arguments: dict) -\> str:\\n", " impl = self.\_impls\[name\]\\n", " res = impl\[\\"handler\\"\](\*\*arguments)\\n", " if inspect.isawaitable(res):\\n", " res = await res\\n", " return res if isinstance(res, str) else json.dumps(res, default=str)\\n", "\\n", "\\n", "def mcp\_tools(server: MCPServer) -\> list\[Tool\]:\\n", " \\"\\"\\"Adapt every tool on an MCP server into our native Tool objects.\\"\\"\\"\\n",

" out: list\[Tool\] = \[\]\\n", " for spec in server.list\_tools():\\n", " nm = spec\[\\"name\\"\]\\n", "\\n", " async def \_runner(\_nm=nm, \*\*kwargs):\\n", " return await server.call\_tool(\_nm, kwargs)\\n", "\\n", " out.append(Tool(name=f\\"{server.name}\_\_{nm}\\",\\n", " description=f\\"\[MCP:{server.name}\] {spec\['description'\]}\\",\\n",

" parameters=spec\[\\"parameters\\"\], func=\_runner, is\_async=True))\\n",

" return out\\n", "\\n", "\\n", "@dataclass\\n", "class RunResult:\\n", " content: str\\n", " tools\_used: list\[str\] = field(default\_factory=list)\\n", " iterations: int = 0\\n", " usage: Usage = field(default\_factory=Usage)\\n", " messages: list\[dict\] = field(default\_factory=list)\\n", "\\n", "\\n", "class Agent:\\n", " def \_\_init\_\_(self, provider: Provider, registry: ToolRegistry, memory: Memory,\\n",

" system\_prompt: str, max\_iterations: int = 6, verbose: bool = True):\\n", " self.provider = provider\\n", " self.registry = registry\\n", " self.memory = memory\\n", " self.system\_prompt = system\_prompt\\n", " self.max\_iterations = max\_iterations\\n", " self.verbose = verbose\\n", "\\n", " def \_log(self, \*a):\\n", " if self.verbose:\\n", " print(\*a)\\n", "\\n", " async def run(self, user\_message: str, \*, session\_key: str = \\"default\\",\\n", " hooks: Optional\[list\[AgentHook\]\] = None,\\n", " extra\_instructions: str = \\"\\") -\> RunResult:\\n", " hooks = hooks or \[\]\\n", "\\n", " system = self.system\_prompt\\n", " if extra\_instructions:\\n", " system += \\"\\\\n\\\\n\\" + extra\_instructions\\n", " self.memory.append(session\_key, {\\"role\\": \\"user\\", \\"content\\": user\_message})\\n",

" dropped = self.memory.compact(session\_key)\\n", " if dropped:\\n", " self.\_log(f\\" Â· memory compaction dropped {dropped} old message(s)\\")\\n",

" messages = \[{\\"role\\": \\"system\\", \\"content\\": system}, \*self.memory.history(session\_key)\]\\n",

"\\n", " ctx = AgentHookContext(messages=messages)\\n", " tools\_used: list\[str\] = \[\]\\n", " total = Usage()\\n", " final\_text = \\"\\"\\n", "\\n", " for i in range(1, self.max\_iterations + 1):\\n", " ctx.iteration = i\\n", " ctx.messages = messages\\n",

" await \_fan\_out(hooks, \\"before\_iteration\\", ctx)\\n", "\\n", " response = await self.provider.complete(messages, self.registry.specs())\\n",

" ctx.response = response\\n", " total.prompt\_tokens += response.usage.prompt\_tokens\\n", " total.completion\_tokens += response.usage.completion\_tokens\\n", " ctx.usage = total\\n", "\\n", " if response.tool\_calls:\\n", " ctx.tool\_calls = response.tool\_calls\\n", " self.\_log(f\\" \[iter {i}\] model requested {len(response.tool\_calls)} tool call(s)\\")\\n", " messages.append({\\n", " \\"role\\": \\"assistant\\",\\n", " \\"content\\": response.content,\\n", " \\"tool\_calls\\": \[{\\"id\\": tc.id, \\"type\\": \\"function\\",\\n", " \\"function\\": {\\"name\\": tc.name,\\n", " \\"arguments\\": json.dumps(tc.arguments)}}\\n",

" for tc in response.tool\_calls\],\\n", " })\\n", " await \_fan\_out(hooks, \\"before\_execute\_tools\\", ctx)\\n", "\\n", " results: list\[str\] = \[\]\\n", " for tc in response.tool\_calls:\\n", " t = self.registry.get(tc.name)\\n", " if t is None:\\n", " result = f\\"ERROR: unknown tool '{tc.name}'\\"\\n", " else:\\n", " result = await t(\*\*tc.arguments)\\n", " tools\_used.append(tc.name)\\n", " results.append(result)\\n", " self.\_log(f\\" â†³ {tc.name}({tc.arguments}) -\> {result\[:120\]}\\")\\n",

" messages.append({\\"role\\": \\"tool\\", \\"tool\_call\_id\\": tc.id,\\n", " \\"content\\": result})\\n",

" ctx.tool\_results = results\\n", " await \_fan\_out(hooks, \\"after\_iteration\\", ctx)\\n", " continue\\n", "\\n", " final\_text = response.content or \\"\\"\\n", " for h in hooks:\\n", " try:\\n", " final\_text = h.finalize\_content(ctx, final\_text)\\n", " except Exception as e:\\n", " print(f\\" (hook {type(h).\_\_name\_\_}.finalize\_content error: {e})\\")\\n",

" ctx.final\_content = final\_text\\n", " ctx.stop\_reason = response.finish\_reason\\n", " await \_fan\_out(hooks, \\"after\_iteration\\", ctx)\\n", " self.memory.append(session\_key, {\\"role\\": \\"assistant\\", \\"content\\": final\_text})\\n",

" break\\n", " else:\\n", " final\_text = \\"(stopped: hit max\_iterations without a final answer)\\"\\n", "\\n", " return RunResult(content=final\_text, tools\_used=tools\_used,\\n", " iterations=ctx.iteration, usage=total,\\n", " messages=list(messages))" \], "metadata": {

"id": "25IovyoUbxab"

}, "execution\_count": null, "outputs": \[\] }, {

"cell\_type": "code", "source": \[

"DEFAULT\_SYSTEM\_PROMPT = (\\n", " \\"You are nanobot, a concise, helpful personal AI agent. You can call tools when \\"\\n",

" \\"they help. Prefer using a tool over guessing for math, the current time, running \\"\\n",

" \\"code, web lookups, or recalling stored facts. After tools run, answer the user \\"\\n",

" \\"directly and clearly.\\"\\n", ")\\n", "\\n", "\\n", "class Nanobot:\\n", " def \_\_init\_\_(self, provider: Provider, \*, system\_prompt: str = DEFAULT\_SYSTEM\_PROMPT,\\n",

" token\_budget: int = 3000, max\_iterations: int = 6, verbose: bool = True):\\n", " self.registry = ToolRegistry()\\n",

" self.memory = Memory(token\_budget=token\_budget)\\n", " self.skills: dict\[str, Skill\] = {}\\n", " self.\_loaded\_skills: set\[str\] = set()\\n", " self.\_base\_system = system\_prompt\\n", " self.agent = Agent(provider, self.registry, self.memory,\\n", " system\_prompt, max\_iterations=max\_iterations, verbose=verbose)\\n",

" for t in (calculator, get\_current\_time, run\_python, web\_search):\\n", " self.registry.add(t)\\n", "\\n", " @classmethod\\n", " def auto(cls, \*\*kw) -\> \\"Nanobot\\":\\n", " \\"\\"\\"Pick a real provider if an API key is set, else the Mock provider.\\"\\"\\"\\n",

" api\_key = os.environ.get(\\"NANOBOT\_API\_KEY\\") or os.environ.get(\\"OPENAI\_API\_KEY\\")\\n",

" model = os.environ.get(\\"NANOBOT\_MODEL\\", \\"gpt-4o-mini\\")\\n", " base\_url = os.environ.get(\\"NANOBOT\_BASE\_URL\\")\\n", " if api\_key and \_HAVE\_OPENAI:\\n", " print(f\\"â†’ Using live provider: OpenAI-compatible (model={model}, base\_url={base\_url or 'api.openai.com'})\\")\\n",

" provider: Provider = OpenAICompatibleProvider(api\_key, model, base\_url)\\n",

" else:\\n", " why = \\"no API key found\\" if not api\_key else \\"openai SDK unavailable\\"\\n",

" print(f\\"â†’ Using Mock provider ({why}). Set NANOBOT\_API\_KEY for a live model.\\")\\n",

" provider = MockProvider()\\n", " return cls(provider, \*\*kw)\\n", "\\n", " def add\_tool(self, f: Callable) -\> \\"Nanobot\\":\\n", " self.registry.add(tool(f) if not isinstance(f, Tool) else f)\\n", " return self\\n", "\\n", " def register\_skill(self, skill: Skill) -\> \\"Nanobot\\":\\n", " self.skills\[skill.name\] = skill\\n", " return self\\n", "\\n", " def load\_skill(self, name: str) -\> \\"Nanobot\\":\\n", " \\"\\"\\"Activate a skill: append its instructions and register its

tools.\\"\\"\\"\\n",

" sk = self.skills\[name\]\\n", " if name not in self.\_loaded\_skills:\\n", " self.agent.system\_prompt += f\\"\\\\n\\\\n\#\# Skill: {sk.name}\\\\n{sk.instructions}\\"\\n",

" for t in sk.tools:\\n", " self.registry.add(t)\\n", " self.\_loaded\_skills.add(name)\\n", " print(f\\" Â· loaded skill '{name}' (+{len(sk.tools)} tool(s))\\")\\n", " return self\\n", "\\n", " def connect\_mcp(self, server: MCPServer) -\> \\"Nanobot\\":\\n", " for t in mcp\_tools(server):\\n", " self.registry.add(t)\\n", " print(f\\" Â· connected MCP server '{server.name}' (+ {len(server.list\_tools())} tool(s))\\")\\n",

" return self\\n", "\\n", " async def run(self, message: str, \*, session\_key: str = \\"sdk:default\\",\\n", " hooks: Optional\[list\[AgentHook\]\] = None) -\> RunResult:\\n", " return await self.agent.run(message, session\_key=session\_key, hooks=hooks)\\n",

"\\n", "\\n", "class AuditHook(AgentHook):\\n", " \\"\\"\\"Print every tool the model decides to call.\\"\\"\\"\\n", " def \_\_init\_\_(self):\\n", " self.calls: list\[str\] = \[\]\\n", "\\n", " async def before\_execute\_tools(self, context: AgentHookContext) -\> None:\\n", " for tc in context.tool\_calls:\\n", " self.calls.append(tc.name)\\n", " print(f\\" \[audit\] {tc.name}({tc.arguments})\\")\\n", "\\n", "\\n", "class TimingHook(AgentHook):\\n", " \\"\\"\\"Measure how long each LLM iteration takes.\\"\\"\\"\\n", " def \_\_init\_\_(self):\\n", " self.\_t = 0.0\\n", "\\n", " async def before\_iteration(self, context: AgentHookContext) -\> None:\\n", " self.\_t = time.perf\_counter()\\n", "\\n", " async def after\_iteration(self, context: AgentHookContext) -\> None:\\n", " ms = (time.perf\_counter() - self.\_t) \* 1000\\n", " print(f\\" \[timing\] iteration {context.iteration} took {ms:.1f} ms\\")\\n", "\\n", "\\n", "class CensorHook(AgentHook):\\n", " \\"\\"\\"finalize\_content runs as a pipeline â€” transform the final text.\\"\\"\\"\\n",

" def finalize\_content(self, context: AgentHookContext, content: str) -\> str:\\n", " return content.replace(\\"secret\\", \\"\*\*\*\\") if content else content\\n", "\\n", "\\n", "async def demo\_basic(bot: Nanobot):\\n", " banner(\\"DEMO 1 â€” Basic chat (no tools needed)\\")\\n", " r = await bot.run(\\"Hello\! Who are you?\\", session\_key=\\"demo-basic\\")\\n", " print(\\"AGENT:\\", r.content)\\n", " print(f\\"(iterations={r.iterations}, tools={r.tools\_used}, \~tokens= {r.usage.total})\\")\\n",

"\\n", "\\n", "async def demo\_tool\_calling(bot: Nanobot):\\n",

" banner(\\"DEMO 2 â€” Tool calling: math, time, and Python\\")\\n", " for q in \[\\"What is 2 \*\* 10 + sqrt(144)?\\",\\n", " \\"What time is it in Tokyo?\\",\\n", " \\"Write Python to list the first 12 Fibonacci numbers.\\"\]:\\n", " print(f\\"\\\\nUSER: {q}\\")\\n", " r = await bot.run(q, session\_key=\\"demo-tools\\")\\n", " print(\\"AGENT:\\", r.content)\\n", "\\n", "\\n", "async def demo\_multistep(bot: Nanobot):\\n", " banner(\\"DEMO 3 â€” Multi-step loop with an audit hook\\")\\n", " audit = AuditHook()\\n", " q = \\"Calculate 15 \* 23, and also tell me the current time in Asia/Kolkata.\\"\\n",

" print(f\\"USER: {q}\\")\\n", " r = await bot.run(q, session\_key=\\"demo-multistep\\", hooks=\[audit\])\\n", " print(\\"AGENT:\\", r.content)\\n", " print(\\"Tools observed by hook:\\", audit.calls)\\n", "\\n", "\\n", "async def demo\_memory(bot: Nanobot):\\n", " banner(\\"DEMO 4 â€” Session memory (independent histories per session\_key)\\")\\n",

" await bot.run(\\"My name is Ada and I love Python.\\", session\_key=\\"user- ada\\")\\n", " await bot.run(\\"My name is Alan and I love Haskell.\\", session\_key=\\"user- alan\\")\\n",

" r1 = await bot.run(\\"What's my name and what do I love?\\", session\_key=\\"user- ada\\")\\n", " r2 = await bot.run(\\"What's my name and what do I love?\\", session\_key=\\"user- alan\\")\\n",

" print(\\"ADA session â†’\\", r1.content)\\n", " print(\\"ALAN session â†’\\", r2.content)\\n", " print(\\"(Each session\_key kept its own conversation history â€” like nanobot.)\\")\\n",

"\\n", "\\n", "async def demo\_skills(bot: Nanobot):\\n", " banner(\\"DEMO 5 â€” Skills: load a 'research' capability on demand\\")\\n", " research = Skill(\\n", " name=\\"research\\",\\n", " description=\\"Web research workflow\\",\\n", " instructions=(\\"When researching, first search the web, then synthesize the \\"\\n",

" \\"snippets into a short, sourced summary.\\"),\\n", " tools=\[web\_search\],\\n", " )\\n", " bot.register\_skill(research).load\_skill(\\"research\\")\\n", " r = await bot.run(\\"Search for the latest on retrieval-augmented generation and summarize.\\",\\n",

" session\_key=\\"demo-skills\\")\\n", " print(\\"AGENT:\\", r.content)\\n", "\\n", "\\n", "async def demo\_mcp(bot: Nanobot):\\n", " banner(\\"DEMO 6 â€” MCP-style external tool server\\")\\n", " server = MCPServer(\\"weather\\")\\n", " server.register(\\n", " name=\\"forecast\\",\\n", " description=\\"Get a (stub) weather forecast for a city.\\",\\n", " parameters={\\"type\\": \\"object\\",\\n", " \\"properties\\": {\\"city\\": {\\"type\\": \\"string\\"}},\\n", " \\"required\\": \[\\"city\\"\]},\\n", " handler=lambda city: f\\"Forecast for {city}: 27Â°C, partly cloudy (stub MCP data).\\",\\n",

" )\\n", " bot.connect\_mcp(server)\\n", " print(\\"Registered tools now include:\\", \[n for n in bot.registry.names() if \\"weather\\" in n\])\\n",

" t = bot.registry.get(\\"weather\_\_forecast\\")\\n", " print(\\"Direct MCP tool call â†’\\", await t(city=\\"Delhi\\"))\\n", "\\n", "\\n", "async def demo\_streaming\_and\_finalize(bot: Nanobot):\\n", " banner(\\"DEMO 7 â€” finalize\_content pipeline + timing hook\\")\\n", " q = \\"Compute sqrt(2) to show the math tool, then reply.\\"\\n", " print(f\\"USER: {q}\\")\\n", " r = await bot.run(q, session\_key=\\"demo-hooks\\", hooks=\[TimingHook(), CensorHook()\])\\n",

" print(\\"AGENT:\\", r.content)\\n", "\\n", "\\n", "async def demo\_capstone(bot: Nanobot):\\n", " banner(\\"DEMO 8 â€” Capstone: a personal agent juggling tools + memory\\")\\n", " print(\\"A short multi-turn 'personal assistant' conversation:\\\\n\\")\\n", " turns = \[\\n", " \\"Remember that my favorite programming language is Python.\\",\\n", " \\"What's 144 / 12, and what's my favorite language?\\",\\n", " \\"Run Python to print all primes under 50.\\",\\n", " \]\\n", " for q in turns:\\n", " print(f\\"USER: {q}\\")\\n", " r = await bot.run(q, session\_key=\\"capstone\\", hooks=\[AuditHook()\])\\n", " print(\\"AGENT:\\", r.content, \\"\\\\n\\")" \], "metadata": {

"id": "FW6R7LBEbxXm" }, "execution\_count": null, "outputs": \[\] }, {

"cell\_type": "code", "execution\_count": 1, "metadata": {

"colab": {

"base\_uri": "https://localhost:8080/" }, "id": "CQMM2xI9Zd9D", "outputId": "d8a2d4f8-b378-4f1b-83ed-263c29e3e736" }, "outputs": \[

{

"output\_type": "stream", "name": "stdout", "text": \[ "\\n",

"â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â

• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• \\n",

" ðŸ ˆ nanobot-from-scratch â€” building & running the core architecture\\n",

"â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â

• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• \\n",

"â†’ Using Mock provider (no API key found). Set NANOBOT\_API\_KEY for a live model.\\n",

"Registered tools: \['calculator', 'get\_current\_time', 'run\_python', 'web\_search', 'remember\_fact', 'recall\_fact'\]\\n",

"\\n",

"â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â

• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• \\n",

" DEMO 1 â€” Basic chat (no tools needed)\\n",

"â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â

• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• \\n",

"AGENT: Hello\! I'm a mock nanobot agent. Ask me to calculate, tell time, run Python, or remember things.\\n",

"(iterations=1, tools=\[\], \~tokens=97)\\n", "\\n",

"â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â

• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• \\n",

" DEMO 2 â€” Tool calling: math, time, and Python\\n",

"â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â

• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• \\n",

"\\n", "USER: What is 2 \*\* 10 + sqrt(144)?\\n", " \[iter 1\] model requested 1 tool call(s)\\n", " â†³ calculator({'expression': '2 \*\* 10 + sqrt(144)'}) -\> 2 \*\* 10 + sqrt(144) = 1036.0\\n",

"AGENT: Based on the tool results, here's what I found: 2 \*\* 10 + sqrt(144) = 1036.0\\n",

"\\n", "USER: What time is it in Tokyo?\\n", " \[iter 1\] model requested 1 tool call(s)\\n", " â†³ get\_current\_time({'timezone': 'Asia/Tokyo'}) -\> Current time in Asia/Tokyo: 2026-06-21 03:58:38 JST\\n",

"AGENT: Based on the tool results, here's what I found: Current time in Asia/Tokyo: 2026-06-21 03:58:38 JST\\n",

"\\n", "USER: Write Python to list the first 12 Fibonacci numbers.\\n", " \[iter 1\] model requested 1 tool call(s)\\n", " â†³ run\_python({'code': 'def fib(n):\\\\n a,b=0,1\\\\n out=\[\]\\\\n for \_ in range(n):\\\\n out.append(a); a,b=b,a+b\\\\n return out\\\\nprint(fib(12))'}) -\> stdout:\\n",

"\[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89\]\\n", "AGENT: Based on the tool results, here's what I found: stdout:\\n", "\[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89\]\\n", "\\n",

"â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â

• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• \\n",

" DEMO 3 â€” Multi-step loop with an audit hook\\n",

"â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â

• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• \\n",

"USER: Calculate 15 \* 23, and also tell me the current time in Asia/Kolkata.\\n", " \[iter 1\] model requested 1 tool call(s)\\n", " \[audit\] calculator({'expression': '15 \* 23'})\\n", " â†³ calculator({'expression': '15 \* 23'}) -\> 15 \* 23 = 345\\n", " \[iter 2\] model requested 1 tool call(s)\\n", " \[audit\] get\_current\_time({'timezone': 'Asia/Kolkata'})\\n", " â†³ get\_current\_time({'timezone': 'Asia/Kolkata'}) -\> Current time in Asia/Kolkata: 2026-06-21 00:28:38 IST\\n",

"AGENT: Based on the tool results, here's what I found: 15 \* 23 = 345 Current time in Asia/Kolkata: 2026-06-21 00:28:38 IST\\n",

"Tools observed by hook: \['calculator', 'get\_current\_time'\]\\n", "\\n",

"â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â

• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• \\n",

" DEMO 4 â€” Session memory (independent histories per session\_key)\\n",

"â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â

• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• \\n",

"ADA session â†’ From our conversation, your name is Ada and you love Python.\\n",

"ALAN session â†’ From our conversation, your name is Alan and you love Haskell.\\n", "(Each session\_key kept its own conversation history â€” like nanobot.)\\n",

"\\n",

"â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â

• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• \\n",

" DEMO 5 â€” Skills: load a 'research' capability on demand\\n",

"â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â

• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• \\n",

" Â· loaded skill 'research' (+1 tool(s))\\n", " \[iter 1\] model requested 1 tool call(s)\\n", " â†³ web\_search({'query': 'Search for the latest on retrieval-augmented generation and summarize.'}) -\> \[stub results for 'Search for the latest on retrieval- augmented generation and summarize.'\] (1) Overview article. (2) Of\\n",

"AGENT: Based on the tool results, here's what I found: \[stub results for 'Search for the latest on retrieval-augmented generation and summarize.'\] (1) Overview article. (2) Official docs. (3) Recent discussion. Swap web\_search's body for a real API in production.\\n",

"\\n",

"â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â

• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• \\n",

" DEMO 6 â€” MCP-style external tool server\\n",

"â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â

• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• \\n",

" Â· connected MCP server 'weather' (+1 tool(s))\\n", "Registered tools now include: \['weather\_\_forecast'\]\\n", "Direct MCP tool call â†’ Forecast for Delhi: 27Â°C, partly cloudy (stub MCP data).\\n",

"\\n",

"â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â

• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• \\n",

" DEMO 7 â€” finalize\_content pipeline + timing hook\\n",

"â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â

• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• \\n",

"USER: Compute sqrt(2) to show the math tool, then reply.\\n", " \[iter 1\] model requested 1 tool call(s)\\n", " â†³ calculator({'expression': 'sqrt(2)'}) -\> sqrt(2) = 1.4142135623730951\\n",

" \[timing\] iteration 1 took 0.3 ms\\n", " \[timing\] iteration 2 took 0.1 ms\\n",

"AGENT: Based on the tool results, here's what I found: sqrt(2) = 1.4142135623730951\\n",

"\\n",

"â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â

• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• \\n",

" DEMO 8 â€” Capstone: a personal agent juggling tools + memory\\n",

"â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â

• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• \\n",

"A short multi-turn 'personal assistant' conversation:\\n", "\\n", "USER: Remember that my favorite programming language is Python.\\n", " \[iter 1\] model requested 1 tool call(s)\\n", " \[audit\] remember\_fact({'key': 'favorite\_language', 'value': 'python'})\\n", " â†³ remember\_fact({'key': 'favorite\_language', 'value': 'python'}) -\> Stored favorite\_language = python\\n",

" \[iter 2\] model requested 1 tool call(s)\\n", " \[audit\] recall\_fact({'key': 'favorite\_language'})\\n", " â†³ recall\_fact({'key': 'favorite\_language'}) -\> python\\n", "AGENT: Based on the tool results, here's what I found: Stored favorite\_language = python python \\n",

"\\n", "USER: What's 144 / 12, and what's my favorite language?\\n", " \[iter 1\] model requested 1 tool call(s)\\n", " \[audit\] calculator({'expression': '144 / 12'})\\n", " â†³ calculator({'expression': '144 / 12'}) -\> 144 / 12 = 12.0\\n", " \[iter 2\] model requested 1 tool call(s)\\n", " \[audit\] recall\_fact({'key': 'favorite\_language'})\\n", " â†³ recall\_fact({'key': 'favorite\_language'}) -\> python\\n", "AGENT: Based on the tool results, here's what I found: 144 / 12 = 12.0 python \\n",

"\\n", "USER: Run Python to print all primes under 50.\\n", " \[iter 1\] model requested 1 tool call(s)\\n", " \[audit\] run\_python({'code': 'primes=\[n for n in range(2,50) if all(n%d for d in range(2,int(n\*\*0.5)+1))\]\\\\nprint(primes)'})\\n",

" â†³ run\_python({'code': 'primes=\[n for n in range(2,50) if all(n%d for d in range(2,int(n\*\*0.5)+1))\]\\\\nprint(primes)'}) -\> stdout:\\n",

"\[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47\]\\n", "AGENT: Based on the tool results, here's what I found: stdout:\\n", "\[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47\] \\n", "\\n", "\\n",

"â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â

• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• \\n",

" DONE\\n",

"â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â

• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• â• \\n",

"You just built nanobot's core: a provider-agnostic agent loop with tools,\\n", "token-budgeted session memory, lifecycle hooks, skills, and an MCP-style tool\\n",

"server â€” the same architecture HKUDS/nanobot ships, kept deliberately small.\\n",

"\\n", "â”€â”€ Run the REAL nanobot â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â” €â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€\\n",

" \!pip install nanobot-ai\\n",

" \# configure a provider + model in \~/.nanobot/config.json, then:\\n", " from nanobot import Nanobot as RealNanobot\\n", " bot = RealNanobot.from\_config()\\n", " result = await bot.run(\\"What time is it in Tokyo?\\")\\n", " print(result.content)\\n", "Docs: https://github.com/HKUDS/nanobot â€¢ Python SDK: docs/python-sdk.md\\n", "\\n" \] } \], "source": \[

"\_FACTS: dict\[str, str\] = {}\\n", "\\n", "\\n", "@tool\\n", "def remember\_fact(key: str, value: str) -\> str:\\n", " \\"\\"\\"Store a fact in long-term key-value memory.\\n", " key: short identifier\\n", " value: the value to store\\"\\"\\"\\n", " \_FACTS\[key\] = value\\n", " return f\\"Stored {key} = {value}\\"\\n", "\\n", "\\n", "@tool\\n", "def recall\_fact(key: str) -\> str:\\n", " \\"\\"\\"Recall a previously stored fact by key.\\n", " key: the identifier used when storing\\"\\"\\"\\n", " return \_FACTS.get(key, f\\"(no fact stored under '{key}')\\")\\n", "\\n", "\\n", "async def main():\\n", " banner(\\"ðŸ ˆ nanobot-from-scratch â€” building & running the core architecture\\")\\n",

" bot = Nanobot.auto(verbose=True)\\n", " bot.add\_tool(remember\_fact).add\_tool(recall\_fact)\\n", " print(\\"Registered tools:\\", bot.registry.names())\\n", "\\n", " await demo\_basic(bot)\\n", " await demo\_tool\_calling(bot)\\n", " await demo\_multistep(bot)\\n", " await demo\_memory(bot)\\n", " await demo\_skills(bot)\\n", " await demo\_mcp(bot)\\n", " await demo\_streaming\_and\_finalize(bot)\\n", " await demo\_capstone(bot)\\n", "\\n", " banner(\\"DONE\\")\\n", " print(textwrap.dedent(\\"\\"\\"\\\\\\n", " You just built nanobot's core: a provider-agnostic agent loop with tools,\\n", " token-budgeted session memory, lifecycle hooks, skills, and an MCP-style tool\\n", " server â€” the same architecture HKUDS/nanobot ships, kept deliberately small.\\n", "\\n",

" â”€â”€ Run the REAL nanobot â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â” €â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€\\n",

" \!pip install nanobot-ai\\n", " \# configure a provider + model in \~/.nanobot/config.json, then:\\n", " from nanobot import Nanobot as RealNanobot\\n", " bot = RealNanobot.from\_config()\\n", " result = await bot.run(\\"What time is it in Tokyo?\\")\\n", " print(result.content)\\n", " Docs: https://github.com/HKUDS/nanobot â€¢ Python SDK: docs/python-

sdk.md\\n", " \\"\\"\\"))\\n",

"\\n", "\\n", "def \_go():\\n", " try:\\n", " asyncio.run(main())\\n", " except RuntimeError:\\n", " loop = asyncio.get\_event\_loop()\\n", " loop.run\_until\_complete(main())\\n", "\\n", "\\n", "if \_\_name\_\_ == \\"\_\_main\_\_\\":\\n", " \_go()" \] } \] }