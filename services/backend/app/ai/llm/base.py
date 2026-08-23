from typing import Protocol, Dict, Any

class LLMProvider(Protocol):
    async def analyze_clause(self, prompt: str) -> Dict[str, Any]:
        """Analyzes a single clause and returns a structured dictionary matching the schema."""
        ...
