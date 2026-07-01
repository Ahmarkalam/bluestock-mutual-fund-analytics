import os
import pandas as pd

RAW_PATH = "project/data/raw"
PROCESSED_PATH = "project/data/processed"

os.makedirs(PROCESSED_PATH, exist_ok=True)


nav = pd.read_csv(os.path.join(RAW_PATH, "02_nav_history.csv"))


nav["date"] = pd.to_datetime(nav["date"])


nav = nav.sort_values(["amfi_code", "date"])


nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()


nav = nav.drop_duplicates()


nav = nav[nav["nav"] > 0]


nav.to_csv(
    os.path.join(PROCESSED_PATH, "02_nav_history_clean.csv"),
    index=False
)

print("NAV History cleaned successfully.")
print("Rows:", len(nav))



transactions = pd.read_csv(os.path.join(RAW_PATH, "08_investor_transactions.csv"))

transactions["transaction_date"] = pd.to_datetime(transactions["transaction_date"])

transactions["transaction_type"] = (
    transactions["transaction_type"]
    .str.strip()
    .str.title()
)

valid_types = ["Sip", "Lumpsum", "Redemption"]
transactions = transactions[
    transactions["transaction_type"].isin(valid_types)
]

transactions = transactions[
    transactions["amount_inr"] > 0
]

print("\nUnique KYC Status:")
print(transactions["kyc_status"].unique())

transactions.to_csv(
    os.path.join(PROCESSED_PATH, "08_investor_transactions_clean.csv"),
    index=False
)

print("\nInvestor Transactions cleaned successfully.")
print("Rows:", len(transactions))



performance = pd.read_csv(
    os.path.join(RAW_PATH, "07_scheme_performance.csv")
)

return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct"
]

for col in return_columns:
    performance[col] = pd.to_numeric(performance[col], errors="coerce")

print("\nAnomalies in Return Columns:")
print(performance[return_columns].isnull().sum())

performance = performance[
    (performance["expense_ratio_pct"] >= 0.1) &
    (performance["expense_ratio_pct"] <= 2.5)
]

performance.to_csv(
    os.path.join(PROCESSED_PATH, "07_scheme_performance_clean.csv"),
    index=False
)

print("\nScheme Performance cleaned successfully.")
print("Rows:", len(performance))