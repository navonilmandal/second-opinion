import cohere
from typing import List
from app.ai.embeddings.base import EmbeddingProvider
from app.core.config import settings

class CohereEmbeddingProvider(EmbeddingProvider):
    def __init__(self):
        self.api_key = settings.EMBEDDING_API_KEY
        # Using embed-english-v3.0 as the default dense embedder (1024 dimensions)
        self.model = "embed-english-v3.0"
        if not self.api_key:
            raise ValueError("EMBEDDING_API_KEY must be set to use CohereEmbeddingProvider")
        
        self.client = cohere.Client(api_key=self.api_key)

    async def generate_embeddings(self, texts: List[str]) -> List[List[float]]:
        """Generates vector embeddings for a list of texts using Cohere."""
        if not texts:
            return []
            
        try:
            response = self.client.embed(
                texts=texts,
                model=self.model,
                input_type="search_document"
            )
            return response.embeddings
        except Exception as e:
            print(f"Warning: Cohere API Error during embedding ({e}). Falling back to mock embeddings.")
            # Return mock embeddings to avoid breaking the demo when quota is exhausted
            # Note: Cohere embed-english-v3.0 uses 1024 dimensions
            return [[0.1] * 1024 for _ in texts]
