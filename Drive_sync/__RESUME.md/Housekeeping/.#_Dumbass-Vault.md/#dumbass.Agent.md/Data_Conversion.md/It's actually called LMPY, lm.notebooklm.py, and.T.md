<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# It's actually called LMPY, lm.notebooklm.py, and.This is what it's called.The repo is called notebooklm.py.

Yes—**you mean `notebooklm-py`**, from `teng-lin/notebooklm-py`. **LMPY** is the nickname/shorthand people use for that NotebookLM Python/CLI/agent-skill tool. [^1][^2]

Use it as the **NotebookLM ingestion/research connector**:

```text
Drive/manual source copy
-> local vault 00-inbox/
-> NotebookLM notebook via notebooklm-py
-> cited answers / reports / exports
-> local vault 02-extractions/notebooklm/
-> reviewed LLM wiki pages in 03-knowledge/
```

Do **not** put it in the LLM-wiki template itself and do not install it directly inside ECC. It is a separate Python package/skill that ECC or Claude Code can call when you approve a NotebookLM task. Its own docs recommend PyPI or a specific release tag, explicitly not the mutable `main` branch. [^2]

Later, on the **tablet Debian**—where the control plane and GUI tools live—you install its stable package in its own isolated Python environment, then install or expose its skill to the orchestration layer. `notebooklm-py` can create notebooks, add documents/URLs/media sources, query content, and generate/download NotebookLM artifacts. [^2]

So your stack is:

```text
ECC              = orchestration/control plane, tablet
notebooklm-py    = NotebookLM connector, tablet isolated environment
Obsidian skills  = vault Markdown/Canvas/Base operations, master vault repo
Graphify         = derived graph/index of selected vault/project folders
LLM-wiki         = your master vault structure and reviewed knowledge pages
Claude Code      = phone worker, controlled by tablet orchestrator
```

<span style="display:none">[^10][^3][^4][^5][^6][^7][^8][^9]</span>

<div align="center">⁂</div>

[^1]: https://pypi.org/project/notebooklm-py/0.1.4/

[^2]: https://github.com/teng-lin/notebooklm-py/blob/main/SKILL.md

[^3]: https://alexandrecaramaschi.com/notebooklm.html

[^4]: https://www.reddit.com/r/notebooklm/comments/1qbopkm/i_built_a_full_python_client_for_notebooklm/

[^5]: https://www.facebook.com/ssktechy/videos/notebooklm-claude-code-mcp-setup-turns-claude-into-a-cited-research-tooladd-yout/1481356680448547/

[^6]: https://github.com/topics/notebooklm-py

[^7]: https://www.instagram.com/p/DXdTdUSHzx3/

[^8]: https://sourceforge.net/projects/notebooklm-py.mirror/

[^9]: https://www.facebook.com/61580659067666/videos/combining-claude-code-with-notebooklm-is-a-complete-cheat-code-that-nobodys-talk/1272161738398398/

[^10]: https://www.facebook.com/theaisurfer/posts/this-combo-is-an-absolute-cheat-code-and-nobodys-talking-about-it-check-the-comm/1264732969177716/

