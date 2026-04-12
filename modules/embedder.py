import hashlib
import numpy as np

def embed_text(text: str) -> np.ndarray:
    """Return a unit-norm float32 embedding vector for `text`."""
    return _hash_embed(text)

def _hash_embed(text: str, dim: int = 384) -> np.ndarray:
    """
    384-dim keyword + bigram + trigram hash vector, L2-normalised.
    """
    vec = np.zeros(dim, dtype=np.float32)
    tokens = text.lower().split()

    # Unigrams (weight 1.0)
    for token in tokens:
        idx = int(hashlib.md5(token.encode()).hexdigest(), 16) % dim
        vec[idx] += 1.0

    # Bigrams (weight 1.5)
    for i in range(len(tokens) - 1):
        bigram = tokens[i] + "_" + tokens[i + 1]
        idx = int(hashlib.md5(bigram.encode()).hexdigest(), 16) % dim
        vec[idx] += 1.5
        
    for i in range(len(tokens) - 2):
        trigram = tokens[i] + "_" + tokens[i + 1] + "_" + tokens[i + 2]
        idx = int(hashlib.md5(trigram.encode()).hexdigest(), 16) % dim
        vec[idx] += 2.0

    norm = np.linalg.norm(vec)
    if norm > 0:
        vec /= norm
    return vec