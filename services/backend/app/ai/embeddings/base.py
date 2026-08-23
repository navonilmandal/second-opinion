from typing import Protocol, List

class EmbeddingProvider(Protocol):
    async def generate_embeddings(self, texts: List[str]) -> List[List[float]]:
        """Generates vector embeddings for a list of texts."""
        ...
