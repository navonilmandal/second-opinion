from pydantic import BaseModel, Field
from typing import List

class Evidence(BaseModel):
    source_id: str
    source_name: str
    source_type: str = Field(description="official | corpus | recent_signal")
    excerpt: str
    relevance: str

class ClauseAnalysisResult(BaseModel):
    chunk_id: str
    risk_level: str = Field(description="low | medium | high")
    risk_score: int
    title: str
    summary: str
    why_flagged: str
    recommendation: str
    confidence: str = Field(description="low | medium | high")
    evidence: List[Evidence] = []
