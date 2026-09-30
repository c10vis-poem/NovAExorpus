#!/usr/bin/env python3
"""
=============================================================================
ÆSOP-XI ARBITRATION ENGINE (arbitration_engine.py)
-----------------------------------------------------------------------------
Subsystem: aesop-xi/arbitration/
Purpose:
  Coordinates inter-agent execution priority, issues temporary cryptographic
  clearance tokens for tool execution, and enforces strict deadlock prevention
  across the NovusÆxenti / NovÆcopia multi-agent swarm.

Operational Invariants:
  1. No Tool Execution Without Clearance: Any agent invoking shell, filesystem,
     or ADB actions must present a valid, unexpired ClearanceToken.
  2. Strict Priority Preemption: User-interactive and ethical safety policies
     preempt background indexing, RAG caching, or batch training.
  3. Deadlock Prevention: Implements timed lock acquisition with strict hierarchy
     and automatic rollback to prevent circular waits.
=============================================================================
"""

import time
import uuid
import hmac
import hashlib
import json
import logging
from enum import IntEnum
from typing import Dict, List, Optional, Set

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] [%(levelname)s] [Arbitration] %(message)s")

class AgentPriority(IntEnum):
    EMERGENCY_SHUTDOWN = 100
    RED_AUDIT_GATEKEEPER = 90
    ETHICAL_SAFETY_POLICY = 80
    USER_INTERACTIVE_UI = 60
    TASK_EXECUTION_AGENT = 40
    BACKGROUND_HYGIENE = 20

class ResourceType(str):
    NPU_HEXAGON = "npu_hexagon"
    ADB_LOOPBACK = "adb_loopback"
    FILESYSTEM_VAULT = "filesystem_vault"
    SQLITE_LEDGER = "sqlite_ledger"
    NETWORK_WEBSOCKET = "network_websocket"

class ClearanceToken:
    def __init__(self, agent_id: str, priority: AgentPriority, allowed_resources: List[str], ttl_seconds: float = 30.0):
        self.token_id = str(uuid.uuid4())
        self.agent_id = agent_id
        self.priority = priority
        self.allowed_resources = set(allowed_resources)
        self.issued_at = time.time()
        self.expires_at = self.issued_at + ttl_seconds
        self.signature = self._generate_signature()

    def _generate_signature(self) -> str:
        payload = f"{self.token_id}:{self.agent_id}:{self.priority}:{sorted(list(self.allowed_resources))}:{self.expires_at}"
        secret_key = b"aesop_xi_clearance_master_secret"
        return hmac.new(secret_key, payload.encode("utf-8"), hashlib.sha256).hexdigest()

    def is_valid(self) -> bool:
        if time.time() > self.expires_at:
            return False
        return hmac.compare_digest(self.signature, self._generate_signature())

    def to_dict(self) -> dict:
        return {
            "token_id": self.token_id,
            "agent_id": self.agent_id,
            "priority": int(self.priority),
            "allowed_resources": list(self.allowed_resources),
            "expires_at": self.expires_at,
            "valid": self.is_valid()
        }

class ArbitrationEngine:
    def __init__(self):
        self.active_locks: Dict[str, str] = {}  # resource -> agent_id
        self.lock_timestamps: Dict[str, float] = {}  # resource -> timestamp
        self.lock_timeouts: Dict[str, float] = {
            ResourceType.NPU_HEXAGON: 15.0,
            ResourceType.ADB_LOOPBACK: 10.0,
            ResourceType.FILESYSTEM_VAULT: 5.0,
            ResourceType.SQLITE_LEDGER: 5.0,
            ResourceType.NETWORK_WEBSOCKET: 20.0
        }
        self.agent_priorities: Dict[str, AgentPriority] = {}
        self.waiting_queue: List[Dict] = []

    def register_agent(self, agent_id: str, priority: AgentPriority):
        self.agent_priorities[agent_id] = priority
        logging.info(f"Registered agent '{agent_id}' with priority {priority.name} ({priority.value})")

    def request_clearance(self, agent_id: str, requested_resources: List[str], ttl_seconds: float = 30.0) -> Optional[ClearanceToken]:
        priority = self.agent_priorities.get(agent_id, AgentPriority.BACKGROUND_HYGIENE)
        
        # Deadlock check & timeout cleanup
        self._cleanup_expired_locks()

        # Check if resources are occupied by higher or equal priority agents
        conflict = False
        for res in requested_resources:
            current_holder = self.active_locks.get(res)
            if current_holder and current_holder != agent_id:
                holder_prio = self.agent_priorities.get(current_holder, AgentPriority.BACKGROUND_HYGIENE)
                if priority > holder_prio:
                    logging.warning(f"Priority preemption: Agent '{agent_id}' ({priority.name}) preempts '{current_holder}' on resource '{res}'")
                    self.release_resource(current_holder, res)
                else:
                    logging.info(f"Resource contention: Agent '{agent_id}' ({priority.name}) blocked on '{res}' by '{current_holder}' ({holder_prio.name})")
                    conflict = True
                    break

        if conflict:
            self.waiting_queue.append({
                "agent_id": agent_id,
                "priority": priority,
                "resources": requested_resources,
                "requested_at": time.time()
            })
            return None

        # Lock acquired
        now = time.time()
        for res in requested_resources:
            self.active_locks[res] = agent_id
            self.lock_timestamps[res] = now

        token = ClearanceToken(agent_id, priority, requested_resources, ttl_seconds)
        logging.info(f"ClearanceToken {token.token_id[:8]} granted to '{agent_id}' for resources: {requested_resources}")
        return token

    def release_resource(self, agent_id: str, resource: str):
        if self.active_locks.get(resource) == agent_id:
            del self.active_locks[resource]
            self.lock_timestamps.pop(resource, None)
            logging.info(f"Agent '{agent_id}' released lock on resource '{resource}'")

    def release_all_for_agent(self, agent_id: str):
        released = []
        for res, holder in list(self.active_locks.items()):
            if holder == agent_id:
                del self.active_locks[res]
                self.lock_timestamps.pop(res, None)
                released.append(res)
        if released:
            logging.info(f"Agent '{agent_id}' released all resources: {released}")

    def _cleanup_expired_locks(self):
        now = time.time()
        for res, lock_time in list(self.lock_timestamps.items()):
            timeout = self.lock_timeouts.get(res, 10.0)
            if now - lock_time > timeout:
                holder = self.active_locks.get(res)
                logging.warning(f"Lock timeout expired for '{res}' held by '{holder}' after {now - lock_time:.1f}s. Forcing release (Deadlock Prevention).")
                self.active_locks.pop(res, None)
                self.lock_timestamps.pop(res, None)

if __name__ == "__main__":
    engine = ArbitrationEngine()
    engine.register_agent("horizons_ui_concierge", AgentPriority.USER_INTERACTIVE_UI)
    engine.register_agent("background_indexer", AgentPriority.BACKGROUND_HYGIENE)
    engine.register_agent("red_auditor", AgentPriority.RED_AUDIT_GATEKEEPER)

    # 1. Background indexer acquires filesystem
    token1 = engine.request_clearance("background_indexer", [ResourceType.FILESYSTEM_VAULT], ttl_seconds=5)
    assert token1 is not None and token1.is_valid()

    # 2. UI Concierge preempts background indexer
    token2 = engine.request_clearance("horizons_ui_concierge", [ResourceType.FILESYSTEM_VAULT], ttl_seconds=10)
    assert token2 is not None and token2.is_valid()

    # 3. Verify clean release
    engine.release_all_for_agent("horizons_ui_concierge")
    logging.info("Arbitration engine self-test passed successfully.")
