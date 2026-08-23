from typing import Protocol, List, Dict, Any

class VectorStore(Protocol):
    async def upsert(self, collection: str, points: List[Dict[str, Any]]) -> bool:
        ...
        
    async def search(self, collection: str, vector: List[float], limit: int = 5) -> List[Dict[str, Any]]:
        ...
