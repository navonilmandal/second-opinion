import json
from typing import Dict, Any
from app.ai.llm.base import LLMProvider

class MockLLMProvider(LLMProvider):
    async def analyze_clause(self, prompt: str) -> Dict[str, Any]:
        """Mock provider returning a deterministic response for testing without keys."""
        return {
            "chunk_id": "mock-chunk-123",
            "risk_level": "medium",
            "risk_score": 50,
            "title": "Mock Exclusions Clause",
            "summary": "This is a simulated analysis response.",
            "why_flagged": "Contains generic restrictive language.",
            "recommendation": "Review exclusions carefully.",
            "confidence": "high",
            "evidence": [
                {
                    "source_id": "mock-irdai",
                    "source_name": "IRDAI Guidelines",
                    "source_type": "official",
                    "excerpt": "Standard clauses must not contain hidden restrictions.",
                    "relevance": "Direct match"
                }
            ]
        }
