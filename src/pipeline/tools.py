from __future__ import annotations
from typing import List, Dict
import httpx
from bs4 import BeautifulSoup


def web_search(query: str, max_results: int = 3) -> List[Dict]:
    # Stub: returns a static list; replace with real search API if needed
    return [{"title": query, "url": "https://example.com"}]


def fetch_page(url: str) -> Dict:
    try:
        resp = httpx.get(url, timeout=10)
        html = resp.text
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text(" ", strip=True)
        return {"url": url, "text": text[:4000]}
    except Exception as e:
        return {"url": url, "text": f"ERROR: {e}"}
