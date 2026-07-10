import os
import pandas as pd
from sqlalchemy import create_engine

RAW_PATH = "project/data/raw"
PROCESSED_PATH = "project/data/processed"

# Agar tumhara data folder directly project root me hai to ye use karo:
# RAW_PATH = "data/raw"
# PROCESSED_PATH = "data/processed"

engine = create_engine("sqlite:///bluestock_mf.db")

files = [
    "01_fund_master.csv",
    "02_nav_history_clean.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance_clean.csv",
    "08_investor_transactions_clean.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in files:

    if "clean" in file:
        path = os.path.join(PROCESSED_PATH, file)
    else:
        path = os.path.join(RAW_PATH, file)

    df = pd.read_csv(path)

    table_name = file.replace(".csv", "").replace("-", "_")

    df.to_sql(table_name, engine, if_exists="replace", index=False)

    count = pd.read_sql(
        f"SELECT COUNT(*) AS total FROM [{table_name}]",
        engine
    )

    print(f"{table_name} : {count.iloc[0,0]} rows loaded")

print("\nSQLite database created successfully.")