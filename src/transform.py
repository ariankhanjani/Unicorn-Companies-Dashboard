import pandas as pd

def money_to_billions(value):
    '''
    Build Conversion Function'''
    

    if pd.isna(value):
        return None

    value = value.replace("$", "")

    if "B" in value:
        return float(
            value.replace("B", "")
        )

    if "M" in value:
        return (
            float(
                value.replace("M", "")
            ) / 1000
        )

    return None


def transform(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Main Transform Function'''
    
    df = df.copy()


    # standardize columns
    df.columns = (
        df.columns
          .str.strip()
          .str.lower()
          .str.replace(" ", "_")
    )
    
    
    # missing values
    df.fillna("Unknown")
    
    
    # convert datatype
    df["date_joined"] = pd.to_datetime(
    df["date_joined"]
)
    
    
    # create joined year feature
    df["joined_year"] = (
    df["date_joined"]
    .dt.year
)
    
    
    # create company age feature
    CURRENT_YEAR = 2026

    df["company_age"] = (
    CURRENT_YEAR
    - df["year_founded"]
)


    # drop duplicates
    df.drop_duplicates()
    
    
    # convert valuation
    df["valuation_billion"] = (
    df["valuation"]
    .apply(money_to_billions)
)
    
    
    # convert funding
    df["funding_billion"] = (
    df["funding"]
    .apply(money_to_billions)
)
    
    # Apply the title() method to the columns value for capitalization
    df["industry"] = df["industry"].str.title()
    
    return df