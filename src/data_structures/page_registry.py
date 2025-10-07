from __future__ import annotations
from typing import Dict, Any
import json
import os

from ..config.settings import settings


class PageRegistry:
    def __init__(self, path: str | None = None):
        self.path = path or settings.page_registry_path
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        self.pages: Dict[str, Dict[str, Any]] = {}
        if os.path.exists(self.path):
            try:
                with open(self.path, "r", encoding="utf-8") as f:
                    self.pages = json.load(f)
            except Exception:
                self.pages = {}

    def upsert(self, url: str, data: Dict[str, Any]) -> None:
        self.pages[url] = data

    def get(self, url: str) -> Dict[str, Any] | None:
        return self.pages.get(url)

    def save(self) -> None:
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.pages, f, ensure_ascii=False, indent=2)
