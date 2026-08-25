from typing import List
from fastembed import TextEmbedding
from app.ai.embeddings.base import EmbeddingProvider
from app.core.config import settings

class FastEmbedProvider(EmbeddingProvider):
    def __init__(self):
        self.model_name = settings.EMBEDDING_MODEL
        print(f"Loading FastEmbed model: {self.model_name}")
        self.model = TextEmbedding(model_name=self.model_name)

    async def generate_embeddings(self, texts: List[str]) -> List[List[float]]:
        """Generates vector embeddings for a list of texts using FastEmbed ONNX runtime."""
        if not texts:
            return []
            
        try:
            # fastembed embed() returns a generator of numpy arrays
            embeddings_generator = self.model.embed(texts)
            # Convert to list of lists of floats
            return [emb.tolist() for emb in embeddings_generator]
        except Exception as e:
            print(f"Error during FastEmbed generation ({e}).")
            # Return empty list or fallback if absolutely necessary, but fastembed shouldn't fail
            raise e
