from pathlib import Path

from extract import extract
from transform import transform
from load import load


RAW_DATA = Path("data/raw/unicorn_companies.csv")
DB_PATH = Path("database/unicorns.db")


def main():

    df = extract(RAW_DATA)

    clean_df = transform(df)

    load(clean_df, DB_PATH)

    print("ETL completed successfully")


if __name__ == "__main__":
    main()