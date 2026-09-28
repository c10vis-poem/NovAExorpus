---
tags: []
created: '2026-09-10'
title: '2026-09-10_log-schema-and-JSONL-strctr'
---



----
//////////// RLVR Log Schema (rlvr_verifiers/YYYYMMDD_eval.jsonl):


{"timestamp": "2026-09-03T17:01:40Z", "task_id": "TASK-104", "verifier_id": "syntax_test", "reward": 1.0, "feedback": "All assertions passed."}




//))))))))  JSONL schema structure 


{
  "id": "UUID-OR-PATH-HASH",
  "path": "relative/path/to/file.ext",
  "tier": 4,
  "category": "extracted_tool",
  "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "tokens": 412,
  "semantic_summary": "CLI utility to extract audio streams from MP4 video containers.",
  "entities_extracted": ["ffmpeg", "audio_processing", "mp4_to_wav"],
  "skills_tools_extracted": [
    {"type": "tool", "name": "extract_audio_stream", "path": "04_skills_runtime/extracted_tools/cli/extract_audio.sh"},
    {"type": "skill", "name": "audio_preprocessing_policy", "path": "04_skills_runtime/prompt_skills/audio_prep.md"}
  ],
  "provenance_source": "01_raw_sources/pdf/media_processing_guide.pdf",
  "last_synced": "2026-09-03T17:05:00Z"
}