from extract import extract
from transform import transform

df = extract("data/raw/unicorn_companies.csv")

clean_df = transform(df)

print(clean_df.info())
print(clean_df.isna().sum())