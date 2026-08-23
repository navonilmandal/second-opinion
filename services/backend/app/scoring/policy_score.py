from typing import Dict, Any
from app.scoring.normalization import Normalizer

class PolicyScorer:
    def calculate_score(self, metrics: Dict[str, Any], ai_risk_score: int = None, analysis_text: str = "") -> Dict[str, Any]:
        """
        Deterministic policy-level scoring separate from LLM analysis.
        Uses structured factors like claim settlement, complaint rates, etc.
        Blends with ai_risk_score if provided (40% Base / 60% AI Document).
        """
        if not metrics:
            return {"overall_score": 0, "verdict": "UNKNOWN", "confidence": "low", "trap_count": 0}
            
        claim_pct = float(metrics.get("claim_settlement_pct", 0))
        complaint_rate = float(metrics.get("complaint_rate", 0))
        claim_volume = int(metrics.get("claim_volume", 0))
        
        # Scan for traps in AI analysis
        text_lower = analysis_text.lower()
        trap_categories = [
            ["proportionate deduction", "pro-rata deduction"],
            ["disease-specific sub-limit", "disease-specific sub-limits", "capped ailment"],
            ["consumables", "standard list of non-payable items"],
            ["compulsory co-payment", "aggregate deductible", "co-payment"],
            ["zone-based copay", "zonal pricing", "zone-based co-payment"]
        ]
        
        trap_count = 0
        for trap_list in trap_categories:
            if any(keyword in text_lower for keyword in trap_list):
                trap_count += 1
                
        # Dynamic Weights (Base Provider Score Formula):
        # Base starts at: Claim Settlement 65%, Complaints 30%, Hidden 5%
        # For each trap: Hidden +3%, CS -1%, Comp -2%
        cs_weight = 0.65 - (trap_count * 0.01)
        comp_weight = 0.30 - (trap_count * 0.02)
        hidden_weight = 0.05 + (trap_count * 0.03)
        
        # Calculate individual normalized scores
        trust_score_raw = Normalizer.normalize_min_max(claim_pct, 60, 100)
        complaints_score_raw = Normalizer.normalize_min_max(complaint_rate, 0, 5, inverse=True)
        # Hidden charges score based on traps (0 traps = 100, 5 traps = 0)
        hidden_charges_score_raw = Normalizer.normalize_min_max(trap_count, 0, 5, inverse=True)
        
        # The true base score uses the dynamic weights directly
        base_score = (trust_score_raw * cs_weight) + (complaints_score_raw * comp_weight) + (hidden_charges_score_raw * hidden_weight)
        
        # For the UI presentation:
        trust_score_ui = trust_score_raw
        total_transparency_weight = comp_weight + hidden_weight
        if total_transparency_weight > 0:
            transparency_score_ui = ((complaints_score_raw * comp_weight) + (hidden_charges_score_raw * hidden_weight)) / total_transparency_weight
        else:
            transparency_score_ui = 0
        
        # Blend AI Risk Score if provided (40% Base / 60% AI Document)
        if ai_risk_score is not None:
            document_score = 100 - ai_risk_score
            overall_score = round((base_score * 0.40) + (document_score * 0.60), 1)
        else:
            overall_score = round(base_score, 1)
        
        confidence = Normalizer.calculate_confidence(1, claim_volume)
        
        if overall_score >= 90:
            verdict = "GO FOR IT WITHOUT ANY THOUGHT"
        elif overall_score >= 80:
            verdict = "VERY GOOD"
        elif overall_score >= 70:
            verdict = "NICE PLAN"
        elif overall_score >= 60:
            verdict = "GOOD"
        elif overall_score >= 50:
            verdict = "MODERATE"
        else:
            verdict = "HIGH_RISK"
            
        return {
            "overall_score": overall_score,
            "trust_score": round(trust_score_ui, 1),
            "transparency_score": round(transparency_score_ui, 1),
            "verdict": verdict,
            "confidence": confidence,
            "trap_count": trap_count,
            "claim_settlement_pct": claim_pct
        }
