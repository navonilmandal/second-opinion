import json
import httpx
from typing import Dict, Any
from app.ai.llm.base import LLMProvider
from app.core.config import settings

class OpenRouterLLMProvider(LLMProvider):
    def __init__(self):
        self.api_key = settings.LLM_API_KEY
        # Fallback to OPENROUTER_MODEL if LLM_MODEL isn't correctly mapped
        self.model = getattr(settings, "OPENROUTER_MODEL", settings.LLM_MODEL)
        self.url = "https://openrouter.ai/api/v1/chat/completions"

    async def analyze_clause(self, prompt: str) -> Dict[str, Any]:
        """Calls OpenRouter API to analyze a document clause."""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://second-opinion-black.vercel.app", 
            "X-Title": "PolicyReviewAI"
        }
        
        system_prompt = """
        You are an expert insurance policy analyzer. You must output raw JSON only, with no markdown formatting or backticks.
        Analyze the provided clause and return a JSON object with EXACTLY these keys:
        - risk_level: string (low, medium, high)
        - risk_score: number (0 to 100)
        - title: string (short title of the clause)
        - summary: string (brief explanation)
        - why_flagged: string (reason for risk level)
        - recommendation: string (actionable advice)
        
        Important Industry Context for Risk Scoring:
        
        1. The "Bad" Features (High Risk & Heavy Penalty - flag as High Risk):
        - Room rent sub-limits (1% or 2%) & proportionate deductions.
        - Co-payment clauses.
        - Disease-specific sub-limits.
        - Excessive waiting periods (>36 months).
        - Exclusion of consumables.
        - Zone-based restrictions without discounts.

        2. The "Good" Features (Low Risk - lower the risk score closer to 0):
        - No room rent caps or single private A/C room allowed.
        - 100% Restoration benefits / Reassurance benefits.
        - Super NCB (No Claim Bonus).
        - Zero co-payment.
        - Included pre/post hospitalization coverage.
        - Consumables cover.
        - Day 1 New Born Coverage.
        - Free health check-ups.

        3. The "Standard" Features (Neutral Risk - DO NOT heavily penalize):
        - 30-day initial waiting period.
        - 24 to 36 month waiting periods for pre-existing diseases.
        - 2-year specific ailment wait.
        - Daycare coverage.
        - Basic road ambulance cover.
        - Free annual health check-ups.
        
        Score the clause based on the presence of these features. If a clause contains mostly "Good" features, drop the risk_score drastically (e.g. 10-30). If it contains "Bad" features, raise it moderately (e.g. 50-70), but do NOT penalize heavily (80-100) unless there are numerous severe violations. "Standard" features should not increase the risk score significantly.
        """
        
        print(f"DEBUG OPENROUTER: Using model '{self.model}' with key starting with '{self.api_key[:10]}'")

        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            "response_format": {"type": "json_object"},
            "temperature": 0.0
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(self.url, headers=headers, json=payload, timeout=30.0)
            response.raise_for_status()
            
            data = response.json()
            content = data["choices"][0]["message"]["content"]
            
            try:
                import re
                # Find the first { and the last } to extract JSON even if wrapped in thinking process
                match = re.search(r'\{.*\}', content, re.DOTALL)
                if not match:
                    raise json.JSONDecodeError("No JSON object found", content, 0)
                
                json_str = match.group(0)
                result = json.loads(json_str)
                
                result["chunk_id"] = "live-chunk"
                result["confidence"] = "high"
                result["evidence"] = [] # To be hydrated by orchestrator
                return result
            except json.JSONDecodeError:
                # Fallback format if LLM fails to return strict JSON
                return {
                    "chunk_id": "error",
                    "risk_level": "medium",
                    "risk_score": 50,
                    "title": "Parsing Error",
                    "summary": "LLM failed to return structured JSON.",
                    "why_flagged": content[:100],
                    "recommendation": "Review manually.",
                    "confidence": "low",
                    "evidence": []
                }
