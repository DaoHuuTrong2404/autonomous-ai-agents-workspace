"""
Local lexical TF-IDF retriever for educational examples.
No embeddings, BM25 implementation, language model or generated answers.
"""

import math
import re
from typing import List, Dict, Any

class DocumentChunk:
    def __init__(self, chunk_id: str, content: str, metadata: Dict[str, Any] = None):
        self.chunk_id = chunk_id
        self.content = content
        self.metadata = metadata or {}
        self.tokens = self._tokenize(content)

    @staticmethod
    def _tokenize(text: str) -> List[str]:
        return re.findall(r"\w+", text.lower())

class HybridRAG:
    """
    Hybrid retriever combining term frequency-inverse document frequency (TF-IDF)
    over tokenized text. The historical class name is retained for compatibility.
    """
    def __init__(self):
        self.documents: List[DocumentChunk] = []
        self.vocab: Dict[str, int] = {}

    def add_document(self, doc_id: str, content: str, metadata: Dict[str, Any] = None):
        chunk = DocumentChunk(doc_id, content, metadata)
        self.documents.append(chunk)
        for token in set(chunk.tokens):
            self.vocab[token] = self.vocab.get(token, 0) + 1

    def search(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        if isinstance(top_k, bool) or not isinstance(top_k, int) or top_k < 0:
            raise ValueError("top_k must be a non-negative integer")
        if top_k == 0:
            return []
        q_tokens = DocumentChunk._tokenize(query)
        if not q_tokens or not self.documents:
            return []

        scores = []
        num_docs = len(self.documents)

        for doc in self.documents:
            score = 0.0
            doc_len = len(doc.tokens) or 1
            for qt in q_tokens:
                if qt in doc.tokens:
                    tf = doc.tokens.count(qt) / doc_len
                    idf = math.log((num_docs + 1) / (self.vocab.get(qt, 1) + 1)) + 1
                    score += tf * idf
            scores.append((score, doc))

        scores.sort(key=lambda x: x[0], reverse=True)
        return [
            {
                "score": round(score, 4),
                "id": doc.chunk_id,
                "content": doc.content,
                "metadata": doc.metadata
            }
            for score, doc in scores[:top_k] if score > 0
        ]

