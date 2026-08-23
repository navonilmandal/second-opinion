from qdrant_client import AsyncQdrantClient
from qdrant_client.http.models import PointStruct, VectorParams, Distance
from typing import List, Dict, Any
from app.vector.base import VectorStore
from app.core.config import settings
import uuid

class QdrantStore(VectorStore):
    def __init__(self):
        self.client = AsyncQdrantClient(url=settings.VECTOR_DB_URL, api_key=settings.VECTOR_DB_API_KEY)
        
    async def ensure_collection(self, collection: str, size: int = 768):
        if not await self.client.collection_exists(collection):
            await self.client.create_collection(
                collection_name=collection,
                vectors_config=VectorParams(size=size, distance=Distance.COSINE)
            )

    async def upsert(self, collection: str, points: List[Dict[str, Any]]) -> bool:
        await self.ensure_collection(collection)
        qdrant_points = [
            PointStruct(
                id=p.get("id", str(uuid.uuid4())),
                vector=p["vector"],
                payload=p.get("payload", {})
            )
            for p in points
        ]
        await self.client.upsert(collection_name=collection, points=qdrant_points)
        return True

    async def search(self, collection: str, vector: List[float], limit: int = 5) -> List[Dict[str, Any]]:
        results = await self.client.search(
            collection_name=collection,
            query_vector=vector,
            limit=limit
        )
        return [{"id": r.id, "score": r.score, "payload": r.payload} for r in results]
