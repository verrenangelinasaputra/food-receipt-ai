import json
import os
import numpy as np
from typing import Optional


def _cosine(a: np.ndarray, b: np.ndarray) -> float:
    denom = np.linalg.norm(a) * np.linalg.norm(b)
    return float(np.dot(a, b) / denom) if denom != 0 else 0.0
class VectorDB:
    def __init__(self, path: str = "data/vector_db.json"):
        self.path = path
        self.store: dict[str, dict] = {}
        os.makedirs(os.path.dirname(path), exist_ok=True)
        self._load()

    def _load(self):
        if os.path.exists(self.path):
            with open(self.path) as f:
                raw = json.load(f)
            self.store = {
                k: {**v, "vector": np.array(v["vector"])}
                for k, v in raw.items()
            }

    def save(self):
        with open(self.path, "w") as f:
            json.dump(
                {k: {**v, "vector": v["vector"].tolist()}
                 for k, v in self.store.items()},
                f,
                indent=2,
                ensure_ascii=False,
            )

    # CRUD
    def upsert(self, doc_id: str, vector: np.ndarray, metadata: dict = {}):
        self.store[doc_id] = {"vector": vector, "metadata": metadata}

    def delete(self, doc_id: str):
        self.store.pop(doc_id, None)

    def clear(self):
        self.store = {}
        self.save()

    # query
    def query(self, query_vec: np.ndarray, top_k: int = 5) -> list[tuple]:
        """Return [(id, score, metadata), ...] sorted by descending similarity."""
        if not self.store:
            return []
        scores = [
            (doc_id, _cosine(query_vec, item["vector"]), item["metadata"])
            for doc_id, item in self.store.items()
        ]
        return sorted(scores, key=lambda x: -x[1])[:top_k]

    def get_all_metadata(self) -> list[dict]:
        """Return all metadata dicts (for building AI context)."""
        return [v["metadata"] for v in self.store.values()]