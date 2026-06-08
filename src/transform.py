import pandas as pd

def transform(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # standardize columns
    df.columns = (
        df.columns
          .str.strip()
          .str.lower()
          .str.replace(" ", "_")
    )

    return df