from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from app.ai.rag.orchestrator import RAGOrchestrator
from app.scoring.policy_score import PolicyScorer
from app.scoring.benchmark_loader import BenchmarkLoader
from app.ai.schemas import ClauseAnalysisResult
from typing import Dict, Any, List

router = APIRouter()
orchestrator = RAGOrchestrator()
scorer = PolicyScorer()
benchmark = BenchmarkLoader()

class AnalysisRequest(BaseModel):
    document_id: str
    provider_id: str
    query: Optional[str] = "Identify the major risks, hidden charges, mandatory notification periods, and key exclusions in this insurance policy."

class AnalysisResponse(BaseModel):
    analysis: ClauseAnalysisResult
    policy_score: Dict[str, Any]

@router.post("/analyze", response_model=AnalysisResponse)
async def analyze_text(request: AnalysisRequest):
    """
    Analyzes raw text (e.g., from Chrome Extension), runs RAG orchestrator,
    and returns LLM structured output along with deterministic Policy Score.
    """
    try:
        # 1. Run LLM/RAG Analysis on the clause
        analysis_result = await orchestrator.analyze(request.document_id, request.query)
        
        # 2. Fetch benchmark metrics for the provider and calculate score
        metrics = benchmark.get_provider_metrics(request.provider_id)
        
        # Extract text to scan for hidden charge traps
        analysis_text = f"{analysis_result.summary} {analysis_result.why_flagged}"
        
        score = scorer.calculate_score(
            metrics, 
            ai_risk_score=analysis_result.risk_score,
            analysis_text=analysis_text
        )
        
        # 3. Append Dynamic Disclaimer
        trap_count = score.get("trap_count", 0)
        if trap_count > 0:
            disclaimer = "\n\nDisclaimer: Please check the hidden charges that may be applicable."
        else:
            disclaimer = "\n\nDisclaimer: Even though no hidden charges were found in this analysis, please read the whole policy carefully to check for any hidden charges before purchasing."
            
        if analysis_result.recommendation:
            analysis_result.recommendation += disclaimer
        else:
            analysis_result.recommendation = disclaimer

        # 4. Clean up the document from RAM to save memory
        try:
            orchestrator.qdrant.delete_document(request.document_id)
        except Exception as cleanup_err:
            print("Failed to clean up Qdrant document:", cleanup_err)

        return AnalysisResponse(
            analysis=analysis_result,
            policy_score=score
        )
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
