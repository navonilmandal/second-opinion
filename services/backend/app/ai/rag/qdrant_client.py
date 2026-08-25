from qdrant_client import QdrantClient
from qdrant_client.http import models as rest
from typing import List, Dict, Any
import logging
from app.core.config import settings

logger = logging.getLogger(__name__)

_qdrant_client_instance = None

def get_qdrant_client():
    global _qdrant_client_instance
    if _qdrant_client_instance is None:
        _qdrant_client_instance = QdrantClient(location=":memory:")
    return _qdrant_client_instance

class QdrantService:
    def __init__(self, collection_name: str = "documents"):
        self.collection_name = collection_name
        
        # Use local disk storage
        self.client = get_qdrant_client()
        self._ensure_collection_exists()

    def _ensure_collection_exists(self):
        try:
            collections = self.client.get_collections()
            collection_names = [col.name for col in collections.collections]
            
            if self.collection_name not in collection_names:
                self.client.create_collection(
                    collection_name=self.collection_name,
                    vectors_config=rest.VectorParams(
                        size=1024, 
                        distance=rest.Distance.COSINE
                    ),
                )
                logger.info(f"Created Qdrant collection: {self.collection_name}")
        except Exception as e:
            logger.error(f"Error checking/creating Qdrant collection: {e}")

    def upsert_chunks(self, document_id: str, chunks: List[Dict[str, Any]], embeddings: List[List[float]]):
        """
        Upsert document chunks into Qdrant.
        Chunks should have 'chunk_id', 'text', 'page_number'.
        """
        import uuid
        points = []
        for i, chunk in enumerate(chunks):
            # Qdrant requires UUID string or int ID. Let's use a new UUID
            point_id = str(uuid.uuid4())
            
            payload = {
                "document_id": document_id,
                "text": chunk.get("text", ""),
                "page_number": chunk.get("page_number", 1)
            }
            
            points.append(
                rest.PointStruct(
                    id=point_id,
                    vector=embeddings[i],
                    payload=payload
                )
            )
            
        self.client.upsert(
            collection_name=self.collection_name,
            points=points
        )
        logger.info(f"Upserted {len(points)} chunks for document {document_id}")

    def search_chunks(self, document_id: str, query_vector: List[float], limit: int = 5) -> List[Dict[str, Any]]:
        """
        Search for most relevant chunks for a specific document.
        """
        search_result = self.client.search(
            collection_name=self.collection_name,
            query_vector=query_vector,
            query_filter=rest.Filter(
                must=[
                    rest.FieldCondition(
                        key="document_id",
                        match=rest.MatchValue(value=document_id)
                    )
                ]
            ),
            limit=limit
        )
        
        return [hit.payload for hit in search_result]

    def delete_document(self, document_id: str):
        """
        Deletes all chunks associated with a specific document_id.
        """
        self.client.delete(
            collection_name=self.collection_name,
            points_selector=rest.FilterSelector(
                filter=rest.Filter(
                    must=[
                        rest.FieldCondition(
                            key="document_id",
                            match=rest.MatchValue(value=document_id)
                        )
                    ]
                )
            )
        )
        logger.info(f"Deleted chunks for document {document_id} from memory.")
