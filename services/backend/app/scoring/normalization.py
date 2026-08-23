import math

class Normalizer:
    @staticmethod
    def normalize_min_max(value: float, min_val: float, max_val: float, inverse: bool = False) -> float:
        """
        Normalizes a value between 0 and 100 based on min and max.
        If inverse is True, lower values score higher (e.g., for complaint rates).
        """
        if max_val == min_val:
            return 50.0 # Default fallback
            
        normalized = max(0.0, min(100.0, ((value - min_val) / (max_val - min_val)) * 100))
        return 100.0 - normalized if inverse else normalized
        
    @staticmethod
    def calculate_confidence(sample_size: int, claim_volume: int) -> str:
        """
        Dynamic confidence calculator.
        High claim volume -> more reliable statistics.
        """
        if claim_volume > 100000:
            return "high"
        elif claim_volume > 20000:
            return "medium"
        return "low"
