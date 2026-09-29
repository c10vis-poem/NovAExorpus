---
source: ob1_mcp_spec.md.pdf
type: pdf
cleaned: 2026-09-11
cleaner: tools/clean.py (mutool)
---

OB1 Protocol Specification: Open Brain Static
Retrieval over MCP

1. System Identity & Overview

The OB1 (Open Brain / Obi-Wan) protocol defines the formal Model Context Protocol (MCP)
server contract for deterministically querying and updating persistent memory across the
federated #d.u.m.b.a.s.s. network.

Unlike dynamic conversational search, OB1 treats memory as an immutable, time-sliced ledger
with cryptographic session forks and verifiable assertions.




2. MCP Tool Interfaces

knowledge.retrieve

Retrieves verified facts, session state, and constraints anchored to specific time slices or
namespaces.

JSON-RPC Input Schema:

{

  "name": "knowledge.retrieve",

  "parameters": {

    "type": "object",

    "required": ["query"],

    "properties": {

      "query": {

        "type": "string",

        "description": "Natural language or keyword target."



      },

      "namespace": {

        "type": "string",

        "description": "Target memory partition (e.g., 'architecture', 'operator_rules',
'hardware_limits').",

        "default": "all"

      },

      "time_slice_proof": {

        "type": "string",

        "description": "Optional ISO timestamp or commit hash to retrieve point-in-time memory."

      },

      "max_results": {

        "type": "integer",

        "default": 5

      }

    }

  }

}

Output Response Format:

{

  "content": [

    {



      "type": "text",

      "text": "{\n  \"records\": [\n    {\n      \"entity_id\": \"entity_01\",\n      \"verdict\": \"VERIFIED\",\n
\"assertion\": \"OmniRoute operates as an inference gateway and token compressor on port
20128.\",\n      \"provenance\":
\"00_DEFINITIVE_MASTER_SPECIFICATION_V3_COMPLETE.md\"\n    }\n  ]\n}"

    }

  ]

}




knowledge.record

Commits a validated fact, architectural rule, or session fork to the persistent store.

JSON-RPC Input Schema:

{

  "name": "knowledge.record",

  "parameters": {

    "type": "object",

    "required": ["assertion", "namespace", "provenance"],

    "properties": {

      "assertion": {

        "type": "string",

        "description": "The exact fact or architectural constraint to persist."

      },

      "namespace": {



        "type": "string",

        "description": "Target subsystem partition."

      },

      "provenance": {

        "type": "string",

        "description": "Source file, commit hash, or operator instruction confirming this assertion."

      },

      "confidence": {

        "type": "number",

        "default": 1.0

      }

    }

  }

}




3. Session Fork & Time-Slice Proof Rules

1.​ Deterministic Forks: Every major agentic session forks with an ob1_fork_id
referencing the latest ledger commit on Node Beta.
2.​ Immutable History: Assertions once confirmed cannot be deleted; they can only be
superseded by a new assertion referencing the older supersedes_id.
3.​ Conflict Resolution: If two models assert contradictory facts during a session, OB1
marks the state as NEEDS_ARBITRATION and routes it to UNRESOLVED.md for human
operator review.
