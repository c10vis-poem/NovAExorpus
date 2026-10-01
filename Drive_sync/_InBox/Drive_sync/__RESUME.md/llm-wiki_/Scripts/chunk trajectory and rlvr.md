---
tags: []
created: '2026-09-10'
title: '2026-09-10_chunk trajectory and rlvr'
---



----
//////////// Chuck Schema (03_recall_cache/jsonl/*.jsonl)=


{"chunk_id": "CHK-8901", "parent_doc": "02_wiki_md/concepts/rlvr.md", "tokens": 256, "content": "RLVR verifiers score execution traces against deterministic unit tests...", "metadata": {"tier": 2, "topic": "rlvr"}}




/////////////Trajectory Schema (trajectories/YYYYMMDD_session.jsonl):


{"timestamp": "2026-09-03T17:01:35Z", "step": 1, "task_id": "TASK-104", "prompt_hash": "a1b2c3", "tool_call": "run_linter", "exit_code": 0, "response_snippet": "OK"}




//////////// RLVR Log Schema (rlvr_verifiers/YYYYMMDD_eval.jsonl):


{"timestamp": "2026-09-03T17:01:40Z", "task_id": "TASK-104", "verifier_id": "syntax_test", "reward": 1.0, "feedback": "All assertions passed."}