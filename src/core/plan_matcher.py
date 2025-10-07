from __future__ import annotations
from typing import Dict, Any, List

from .vector_db import VectorDB


def profile_to_text(profile: Dict[str, Any]) -> str:
    parts: List[str] = []
    for k, v in profile.items():
        parts.append(f"{k}: {v}")
    return ", ".join(parts)


def match_plans(profile: Dict[str, Any], top_k: int = 3) -> List[Dict[str, Any]]:
    vdb = VectorDB()
    text = profile_to_text(profile)
    return vdb.query_plans(text, top_k=top_k)
