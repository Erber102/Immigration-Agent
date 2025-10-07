from __future__ import annotations
from typing import List

from .llm_clients import LLMClient
from .vector_db import VectorDB


def rag_answer(query: str, system_prompt: str = "", top_k: int = 5) -> str:
    vdb = VectorDB()
    contexts = vdb.query(query, top_k=top_k, collection="kb")
    context_text = "\n\n".join([c["text"] for c in contexts])
    prompt = (
        f"System:\n{system_prompt}\n\n"
        f"Context:\n{context_text}\n\n"
        f"User question:\n{query}\n\n"
        f"Answer in Chinese with structured bullet points if appropriate."
    )
    client = LLMClient()
    return client.generate(prompt)
