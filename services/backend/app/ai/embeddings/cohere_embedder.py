import cohere
from typing import List
from app.ai.embeddings.base import EmbeddingProvider
from app.core.config import settings

class CohereEmbeddingProvider(EmbeddingProvider):
    def __init__(self):
        self.api_key = settings.EMBEDDING_API_KEY
        if not self.api_key:
            raise ValueError("EMBEDDING_API_KEY must be set to use CohereEmbeddingProvider")
        
        self.client = cohere.AsyncClient(self.api_key)
        self.model = "embed-english-v3.0"

    async def generate_embeddings(self, texts: List[str]) -> List[List[float]]:
        """Generates vector embeddings using Cohere API."""
        if not texts:
            return []
            
        try:
            response = await self.client.embed(
                texts=texts,
                model=self.model,
                input_type="search_document"
            )
            return response.embeddings
        except Exception as e:
            print(f"Error during Cohere embedding generation: {e}")
            raise e
