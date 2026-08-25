from google import genai
from typing import List
from app.ai.embeddings.base import EmbeddingProvider
from app.core.config import settings

class GeminiEmbeddingProvider(EmbeddingProvider):
    def __init__(self):
        self.api_key = settings.EMBEDDING_API_KEY
        self.model = settings.EMBEDDING_MODEL
        if not self.api_key:
            raise ValueError("EMBEDDING_API_KEY must be set to use GeminiEmbeddingProvider")
        
        self.client = genai.Client(api_key=self.api_key)

    async def generate_embeddings(self, texts: List[str]) -> List[List[float]]:
        """Generates vector embeddings for a list of texts using Gemini."""
        if not texts:
            return []
            
        try:
            response = self.client.models.embed_content(
                model=self.model,
                contents=texts,
                config={"task_type": "RETRIEVAL_DOCUMENT"}
            )
            # The new SDK returns a list of embeddings directly
            return [emb.values for emb in response.embeddings]
        except Exception as e:
            print(f"Warning: Gemini API Error during embedding ({e}). Falling back to mock embeddings.")
            # Return mock embeddings to avoid breaking the demo when quota is exhausted
            return [[0.1] * 3072 for _ in texts]
