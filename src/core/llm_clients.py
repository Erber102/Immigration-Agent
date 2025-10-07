from __future__ import annotations
from typing import Optional

from . import __init__  # noqa: F401
from ..config.settings import settings

try:
    from openai import OpenAI  # type: ignore
except Exception:  # pragma: no cover
    OpenAI = None  # type: ignore


class LLMClient:
    def __init__(self, provider: str | None = None, model: str | None = None, api_key: Optional[str] = None):
        self.provider = provider or settings.llm_provider
        self.model = model or settings.llm_model
        self.api_key = api_key or settings.openai_api_key
        self.client = None
        if self.provider == "openai" and self.api_key and OpenAI is not None:
            self.client = OpenAI(api_key=self.api_key)

    def generate(self, prompt: str) -> str:
        if self.client is None:
            # Deterministic mock to allow local dev without keys
            return f"[MOCK-{self.model}] " + prompt[:200]
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )
        return response.choices[0].message.content or ""
