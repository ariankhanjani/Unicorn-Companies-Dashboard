from pathlib import Path
import pandas as pd

def extract(filepath: str) -> pd.DataFrame:
    return pd.read_csv(filepath)