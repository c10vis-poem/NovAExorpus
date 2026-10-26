"""Every question, option and threshold the triage sends to Jev. Edit wording here only.

Each chunk of a corpus file is sent as state:
  {"file": "<repo-relative path>", "chunk": {"heading": "<nearest heading>", "text": "<section text>"}}
"""

MODEL = "jev-1.14.0"  # pinned: thresholds below were checked on this release
YES, NO = 0.7, 0.3    # Noul above YES reads as yes, below NO as no, between is unsettled

KIND = {
    "type": "choice",
    "instructions": "What kind of writing is `chunk.text`?",
    "criteria": {
        "operator_plan": "The operator's own plan, spec or architecture for their project.",
        "decision_record": "A list or log of decisions and rules the operator has settled.",
        "chat_transcript": "A conversation between the operator and an AI assistant, with turns from both.",
        "research_notes": "The operator's notes or an AI report about a tool, paper or idea being evaluated.",
        "third_party_docs": "A README, guide or article written by another project or author, copied in.",
        "code_or_config": "Source code, a config file, a script or structured data.",
        "index_or_pointer": "A table of contents, link list or pointer to other files.",
    },
}

NOULS = {
    "has_decision": {
        "type": "noul",
        "instructions": "Does `chunk.text` state a decision the operator made about how their project will be built or run?",
        "criteria": {
            "true": "A settled choice, such as 'we use GenieX on the NPU' or 'nothing is turned off without the operator naming it'.",
            "false": "Options under discussion, a description of someone else's tool, or a question still open.",
        },
    },
    "has_open_task": {
        "type": "noul",
        "instructions": "Does `chunk.text` list work on the operator's project that is still to be done?",
        "criteria": {
            "true": "A to-do, next step, missing piece or unfinished item, such as 'still need to wire the voice loop'.",
            "false": "Work described as finished, or steps in a third-party tutorial.",
        },
    },
    "has_re_finding": {
        "type": "noul",
        "instructions": "Does `chunk.text` explain how a specific app, tool or protocol works internally?",
        "criteria": {
            "true": "Internals learned from code, logs or inspection, such as file formats, APIs, ports or startup steps.",
            "false": "Only what the tool is for, how to install it, or marketing copy.",
        },
    },
    "operator_authored": {
        "type": "noul",
        "instructions": "Was `chunk.text` written by or for the operator about their own project?",
        "criteria": {
            "true": "Notes, plans, prompts or reports about the operator's project.",
            "false": "Text copied from another project's README, docs, article or paper.",
        },
    },
}

# One Noul per canon component (NAMING-CANON.md), since a chunk can be about several.
COMPONENTS = {
    "NovAExorpus": "the vault repo and universal data bank (NovÆxorpus)",
    "NovusAExenti": "the agent logic (NovusÆxenti)",
    "NovAExopia": "the agent tools, harness and engine (NovÆxopia)",
    "AEsop-Xi": "the memory layer, context formatting, tool orchestration and agent protocols (Æsop-Xi)",
    "Horizons-Ui": "the user interface app (Horizons-Ui)",
    "AEsc": "the terminal daemon (Æsc)",
    "AEyre": "the voice and vision layer, speech-to-text and text-to-speech (Æyre)",
}
for key, what in COMPONENTS.items():
    NOULS[f"about_{key}"] = {
        "type": "noul",
        "instructions": f"Is `chunk.text` about {what} in the operator's project?",
    }

# Facts the model can't know from a section alone (NAMING-CANON.md); sent as state["project"].
PROJECT = ("The operator is building NovÆxorpus, a personal agent system on an Android phone with components "
           "NovÆxorpus (vault), NovusÆxenti (agent logic), NovÆxopia (tools and harness), Æsop-Xi (memory and "
           "protocols), Horizons-Ui (UI), Æsc (terminal daemon) and Æyre (voice). The corpus also holds copies of "
           "other people's projects that the operator studies; those are not the operator's project.")

# Run 01b compared decision/open-task wordings pointed at `project`: they lost recall on the operator's
# own rules (reverse-engineering/CLAUDE.md "Working rules" 0.72 -> 0.47) and still passed a third-party
# design section. Kept: this question, combined per file in code (triage.py third_party_file).
NOULS["other_project"] = {
    "type": "noul",
    "instructions": "Does `chunk.text` describe a project other than `project`?",
}
THIRD_PARTY_SHARE = 0.5  # a file is a third-party copy when this share of its text has other_project > YES

QUESTIONS = {"kind": KIND, **NOULS}

# Exact lookups stay in code (AGENTS.md "Current stack": dropped, do not set up).
DROPPED = ["OmniRoute", "mem0", "Terrestrial Brain", "OpenWiki", "Qwen3-VL"]
