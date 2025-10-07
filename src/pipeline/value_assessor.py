from __future__ import annotations
from typing import Dict

from ..core.llm_clients import LLMClient


def assess(page: Dict) -> float:
    # Very simple heuristic + LLM stub for demo
    text = page.get("text", "")
    if not text:
        return 0.0
    if len(text) < 200:
        return 0.1
    client = LLMClient()
    score_text = client.generate(
        "请根据以下内容判断其是否与移民政策更新相关，输出0到1之间的小数作为分值。内容：" + text[:1000]
    )
    # Fallback parsing
    try:
        score = float([s for s in score_text.split() if s.replace('.', '', 1).isdigit()][0])
        return max(0.0, min(1.0, score))
    except Exception:
        return 0.5
