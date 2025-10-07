from __future__ import annotations
from typing import Dict, Any

from ..core.rag_core import rag_answer

# Minimal in-memory session store for demo purposes
SESSION_STORE: Dict[str, Dict[str, Any]] = {}


class QnAAgent:
    def __init__(self):
        pass

    def register_session(self, session_id: str, profile: Dict[str, Any]) -> None:
        SESSION_STORE[session_id] = {"profile": profile}

    def ask(self, session_id: str, question: str) -> str:
        session = SESSION_STORE.get(session_id, {"profile": {}})
        profile = session.get("profile", {})
        system_prompt = (
            "你是一名移民与留学顾问。基于用户的基本画像，给出清晰、客观、可操作的建议。"
            f" 用户画像: {profile}"
        )
        return rag_answer(question, system_prompt=system_prompt)
