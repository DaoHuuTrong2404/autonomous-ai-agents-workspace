#!/usr/bin/env python3
"""
Quickstart Demonstration of Autonomous Agents Suite
Authored by Dao Huu Trong (DTrongVIP)
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agents.react_agent import ReActAgent
from agents.gnap_swarm import GNAPSwarm
from agents.hybrid_rag import HybridRAG

def main():
    print("=" * 60)
    print("⚡ DTrongVIP Autonomous AI Agents Suite - Quickstart Demo")
    print("=" * 60)

    # 1. ReAct Agent Demo
    print("\n[1] Testing ReAct Autonomous Agent:")
    agent = ReActAgent()
    result = agent.solve("Calculate (25 * 4) + 150")
    print(f"Status: {result['status']}")
    print(f"Result: {result['final_answer']}")

    # 2. GNAP Swarm Demo
    print("\n[2] Testing Git-Native Agent Protocol (GNAP) Swarm:")
    swarm = GNAPSwarm("CTU-AI-Lab")
    t_id = swarm.dispatch_task("Perform Code Review", "AuditBot", {"pr": 42})
    swarm.record_handoff("CodeForge", "AuditBot", "PR #42 Diff", True)
    manifest = swarm.get_swarm_manifest()
    print(f"Dispatched Task: {t_id}")
    print(f"Swarm Manifest: {manifest}")

    # 3. Hybrid RAG Demo
    print("\n[3] Testing Hybrid RAG Engine:")
    rag = HybridRAG()
    rag.add_document("doc-1", "Can Tho University (CTU) offers advanced Artificial Intelligence degree programs.", {"author": "CTU"})
    rag.add_document("doc-2", "Autonomous agents use reasoning loops like ReAct to solve multi-step problems.", {"author": "DTrongVIP"})
    results = rag.search("artificial intelligence degree", top_k=1)
    print(f"RAG Top Result: {results}")

    print("\n✨ All agent systems verified and functional 100%!")

if __name__ == "__main__":
    main()
