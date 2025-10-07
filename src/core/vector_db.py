from __future__ import annotations
from typing import List, Dict, Any
import os

from ..config.settings import settings

try:
    import chromadb  # type: ignore
except Exception:  # pragma: no cover
    chromadb = None  # type: ignore


class VectorDB:
    def __init__(self):
        self.use_chroma = chromadb is not None
        self.memory_store: List[Dict[str, Any]] = []
        if self.use_chroma:
            os.makedirs(settings.chroma_db_path, exist_ok=True)
            self.client = chromadb.PersistentClient(path=settings.chroma_db_path)
            self.kb = self.client.get_or_create_collection(settings.chroma_collection_kb)
            self.plans = self.client.get_or_create_collection(settings.chroma_collection_plans)
        else:
            self.client = None
            self.kb = None
            self.plans = None

    def add_documents(self, docs: List[Dict[str, Any]], collection: str = "kb") -> None:
        if self.use_chroma:
            col = self.kb if collection == "kb" else self.plans
            ids = [d.get("id") or str(len(docs) + i) for i, d in enumerate(docs)]
            col.add(ids=ids, documents=[d["text"] for d in docs], metadatas=[d.get("metadata", {}) for d in docs])
        else:
            for d in docs:
                self.memory_store.append({"collection": collection, **d})

    def query(self, text: str, top_k: int = 5, collection: str = "kb") -> List[Dict[str, Any]]:
        if self.use_chroma:
            col = self.kb if collection == "kb" else self.plans
            res = col.query(query_texts=[text], n_results=top_k)
            results: List[Dict[str, Any]] = []
            for i in range(len(res["ids"][0])):
                results.append({
                    "id": res["ids"][0][i],
                    "text": res["documents"][0][i],
                    "metadata": res["metadatas"][0][i],
                })
            return results
        else:
            # naive contains search for dev
            results = [d for d in self.memory_store if d.get("collection") == collection and text.lower() in d.get("text", "").lower()]
            return results[:top_k]

    def query_plans(self, profile_text: str, top_k: int = 3) -> List[Dict[str, Any]]:
        return self.query(profile_text, top_k=top_k, collection="plans")
