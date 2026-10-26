#!/usr/bin/env python3
"""
Local search over two manually supplied paper descriptions.
Does not fetch papers, generate citations, or synthesize research.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agents.hybrid_rag import HybridRAG

def run_academic_synthesis():
    rag = HybridRAG()
    
    # Ingest research corpus
    rag.add_document(
        "yao-2022",
        "ReAct: Synergizing Reasoning and Acting in Language Models (Yao et al., 2022). "
        "Demonstrates that interleaving reasoning traces and task-specific actions leads to superior decision making.",
        {"venue": "ICLR 2023"}
    )
    rag.add_document(
        "schick-2023",
        "Toolformer: Language Models Can Teach Themselves to Use Tools (Schick et al., 2023). "
        "Self-supervised learning of external API calls including calculators, QA systems, and search engines.",
        {"venue": "NeurIPS 2023"}
    )

    query = "language models reasoning tools"
    hits = rag.search(query, top_k=2)

    print("🎓 Academic Agent Research Brief:")
    for h in hits:
        print(f" - [{h['id']}] Score: {h['score']} | {h['content'][:120]}...")

if __name__ == "__main__":
    run_academic_synthesis()

