"""
Comprehensive Unit Tests for Autonomous Agent Architectures
"""

import pytest
from agents.react_agent import ReActAgent, tool_calculator, tool_knowledge_lookup
from agents.gnap_swarm import GNAPSwarm, AgentRole
from agents.cua_vision import VisionCUAAgent, SOMElement
from agents.hybrid_rag import HybridRAG

def test_calculator_tool():
    res = tool_calculator("15 * 6 + 10")
    assert res == "100"

def test_calculator_tool_safety():
    res = tool_calculator("__import__('os').system('ls')")
    assert "Error: Invalid characters" in res

def test_knowledge_lookup_tool():
    res = tool_knowledge_lookup("What is ReAct?")
    assert "REACT" in res

def test_react_agent_execution():
    agent = ReActAgent()
    result = agent.solve("Tính 40 * 2")
    assert result["status"] == "COMPLETED"
    assert "80" in result["final_answer"]

def test_gnap_swarm_workflow():
    swarm = GNAPSwarm("TestProject")
    task_id = swarm.dispatch_task("Run Security Audit", "AuditBot", {"target": "auth.py"})
    assert task_id.startswith("GNAP-")
    swarm.record_handoff("CodeForge", "AuditBot", "auth.py", True)
    manifest = swarm.get_swarm_manifest()
    assert manifest["total_tasks"] == 1
    assert manifest["total_handoffs"] == 1

def test_cua_vision_som():
    cua = VisionCUAAgent()
    raw = [
        {"label": "Submit Order", "type": "button", "bbox": [100, 200, 200, 250]},
        {"label": "Search Box", "type": "input", "bbox": [50, 50, 400, 90]}
    ]
    elements = cua.parse_mock_som(raw)
    assert len(elements) == 2
    
    action = cua.click_element_by_label("Submit")
    assert action is not None
    assert action["coordinates"] == (150, 225)

def test_hybrid_rag_retrieval():
    rag = HybridRAG()
    rag.add_document("doc1", "Can Tho University is located in the Mekong Delta of Vietnam.")
    rag.add_document("doc2", "Deep learning algorithms power modern speech and visual recognition.")
    
    hits = rag.search("Mekong Delta Vietnam")
    assert len(hits) > 0
    assert hits[0]["id"] == "doc1"
