from __future__ import annotations
from typing import Dict

from .tools import web_search, fetch_page
from .value_assessor import assess
from ..data_structures.page_registry import PageRegistry


def run_task(task: Dict) -> None:
    registry = PageRegistry()
    # simple loop: search terms == goal, then fetch first entry point
    results = web_search(task["goal"], max_results=3)
    for r in results:
        page = fetch_page(r["url"])
        page["score"] = assess(page)
        registry.upsert(page["url"], page)

    for url in task.get("entry_points", []):
        page = fetch_page(url)
        page["score"] = assess(page)
        registry.upsert(url, page)
    registry.save()
