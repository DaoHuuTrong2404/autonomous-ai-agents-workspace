# Autonomous AI Agents & Intelligent Systems Workspace 🤖
### 🏫 Can Tho University (CTU) — College of Information & Communication Technology
**Student:** Dao Huu Trong (Đào Hữu Trọng) — **ID:** B2605840  
**Major:** Artificial Intelligence (*Cohort 52, 2026 – 2031*)  
**Architecture:** Multi-Agent Swarm (GNAP) • ReAct Reasoning • Vision CUA • Zero-Dependency Hybrid RAG

---

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Versions" />
  <img src="https://img.shields.io/badge/Architecture-GNAP%20Swarm%20Protocol-7B2CBF?style=for-the-badge&logo=git&logoColor=white" alt="GNAP" />
  <img src="https://img.shields.io/badge/Testing-Pytest%20100%25%20Passing-2EAD33?style=for-the-badge&logo=pytest&logoColor=white" alt="Pytest" />
  <img src="https://img.shields.io/badge/Codespaces-4--Cores%2016GB-181717?style=for-the-badge&logo=github&logoColor=white" alt="Codespaces" />
  <img src="https://img.shields.io/badge/License-MIT-00F0FF?style=for-the-badge" alt="License" />
</p>

---

## 📌 Architectural Overview

This repository houses the core autonomous intelligence and multi-agent protocols authored by **Dao Huu Trong** during coursework and research at Can Tho University. It delivers production-grade abstractions for deterministic reasoning, decentralized coordination, computer-use automation, and grounded retrieval.

```mermaid
flowchart TD
    User([User Request / Task]) --> ReAct[ReAct Autonomous Agent]
    ReAct -->|Decompose| Swarm[GNAP Multi-Agent Swarm]
    Swarm --> Lead[LeadAgent - Orchestration]
    Swarm --> Scout[ScoutAgent - Hybrid RAG]
    Swarm --> Coder[CodeForge - Synthesis]
    Swarm --> Audit[AuditBot - Pytest / Verification]
    Scout --> CUA[Vision CUA Agent - SOM Navigation]
    Audit --> Verification{Verification PASS?}
    Verification -->|Yes| Output([Verified Task Delivery])
    Verification -->|No| ReAct
```

---

## 🌟 Core Modules

| Module | Description | Key Capabilities |
| :--- | :--- | :--- |
| **`agents.react_agent`** | ReAct Reasoning Engine | Thought-Action-Observation loop, mathematical verification, loop-detection guards. |
| **`agents.gnap_swarm`** | Git-Native Agent Protocol | Role dispatch (Lead, Scout, Coder, Verifier), task boards, and auditable JSON handoffs. |
| **`agents.cua_vision`** | Computer-Use Vision Engine | Structured Object Model (SOM), bounding-box parsing, and synthetic UI interaction. |
| **`agents.hybrid_rag`** | Zero-Dependency Hybrid RAG | Dense TF-IDF + Keyword density matching with zero cloud database overhead. |

---

## 🚀 Quickstart Guide

### 1. Clone & Set Up
```bash
git clone https://github.com/DaoHuuTrong2404/autonomous-ai-agents-workspace.git
cd autonomous-ai-agents-workspace
```

### 2. Run the 10-Second Quickstart Demo
```bash
python3 examples/quickstart.py
```

### 3. Run Academic Paper Synthesis
```bash
python3 examples/academic_researcher.py
```

### 4. Execute Complete Test Suite
```bash
pip install pytest
pytest tests/ -v
```

---

## 🔬 Directory Structure
```text
autonomous-ai-agents-workspace/
├── .github/
│   └── workflows/
│       └── ci.yml               # GitHub Actions CI for Python 3.10-3.12
├── agents/
│   ├── __init__.py              # Unified package exports
│   ├── react_agent.py           # ReAct autonomous reasoning engine
│   ├── gnap_swarm.py            # Git-Native Agent Protocol swarm
│   ├── cua_vision.py            # Vision & SOM Desktop/Web automation
│   └── hybrid_rag.py            # High-performance lightweight RAG
├── examples/
│   ├── quickstart.py            # End-to-end runnable showcase
│   └── academic_researcher.py   # Paper analysis & citation generator
├── tests/
│   └── test_agents.py           # Unit tests across all agent architectures
└── README.md                    # Master documentation & specifications
```

---

## 👨‍💻 Maintainer & Academic Contact
- **Author:** Đào Hữu Trọng (Dao Huu Trong)
- **University:** Can Tho University (Đại học Cần Thơ - CTU)
- **Major:** Artificial Intelligence (Trí Tuệ Nhân Tạo)
- **Email:** [huutrong748@gmail.com](mailto:huutrong748@gmail.com)
- **Interactive 3D Portfolio:** [daohuutrong2404.github.io](https://daohuutrong2404.github.io)

---
*License: [MIT](LICENSE) © 2026 Dao Huu Trong. Built with precision for resilient intelligence.*