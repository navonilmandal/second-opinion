import pandas as pd
from typing import Dict, Any
from pathlib import Path

class BenchmarkLoader:
    def __init__(self, seed_file: str = "../../data/seed/real_seed_corpus.csv"):
        # Resolve path relative to backend root
        base_dir = Path(__file__).resolve().parent.parent.parent
        self.seed_file = base_dir / ".." / ".." / "data" / "seed" / "real_seed_corpus.csv"
        self.data: pd.DataFrame = None

    def load_data(self):
        if self.seed_file.exists():
            self.data = pd.read_csv(self.seed_file)
        else:
            self.data = pd.DataFrame()

    def get_provider_metrics(self, provider_id: str) -> Dict[str, Any]:
        """Returns the benchmark metrics for a specific provider."""
        if self.data is None:
            self.load_data()
        
        if self.data.empty:
            return {}
            
        record = self.data[self.data['policy_id'] == provider_id]
        if not record.empty:
            return record.iloc[0].to_dict()
        return {}
