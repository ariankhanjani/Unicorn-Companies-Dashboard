import sqlite3
import pandas as pd

def load(df: pd.DataFrame, db_path: str) -> None:
    conn = sqlite3.connect(db_path)

    df.to_sql(
        "unicorn_companies",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()