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

# -----------------------------
# Clean Fund Master
# -----------------------------

fund = pd.read_csv(os.path.join(RAW_PATH, "01_fund_master.csv"))

# Convert launch date
fund["launch_date"] = pd.to_datetime(fund["launch_date"])

# Remove duplicates
fund = fund.drop_duplicates()

# Trim text columns
text_cols = [
    "fund_house",
    "scheme_name",
    "category",
    "sub_category",
    "plan",
    "benchmark",
    "fund_manager",
    "risk_category",
    "sebi_category_code"
]

for col in text_cols:
    fund[col] = fund[col].str.strip()

fund.to_csv(
    os.path.join(PROCESSED_PATH, "01_fund_master_clean.csv"),
    index=False
)

print("Fund Master cleaned successfully.")
print("Rows:", len(fund))

# -----------------------------
# Clean AUM by Fund House
# -----------------------------

aum = pd.read_csv(os.path.join(RAW_PATH, "03_aum_by_fund_house.csv"))

aum["date"] = pd.to_datetime(aum["date"])

aum = aum.sort_values("date")

aum = aum.drop_duplicates()

aum = aum[aum["aum_crore"] > 0]

aum.to_csv(
    os.path.join(PROCESSED_PATH, "03_aum_by_fund_house_clean.csv"),
    index=False
)

print("AUM cleaned successfully.")
print("Rows:", len(aum))

# -----------------------------
# Clean SIP Inflows
# -----------------------------

sip = pd.read_csv(os.path.join(RAW_PATH, "04_monthly_sip_inflows.csv"))

sip = sip.drop_duplicates()

sip["month"] = pd.to_datetime(sip["month"])

sip = sip[sip["sip_inflow_crore"] > 0]

sip.to_csv(
    os.path.join(PROCESSED_PATH, "04_monthly_sip_inflows_clean.csv"),
    index=False
)

print("SIP Inflows cleaned successfully.")
print("Rows:", len(sip))

# -----------------------------
# Clean Category Inflows
# -----------------------------

category = pd.read_csv(os.path.join(RAW_PATH, "05_category_inflows.csv"))

category["month"] = pd.to_datetime(category["month"])

category = category.drop_duplicates()

category["category"] = category["category"].str.strip()

category.to_csv(
    os.path.join(PROCESSED_PATH, "05_category_inflows_clean.csv"),
    index=False
)

print("Category Inflows cleaned successfully.")
print("Rows:", len(category))

# -----------------------------
# Clean Industry Folio Count
# -----------------------------

folio = pd.read_csv(os.path.join(RAW_PATH, "06_industry_folio_count.csv"))

folio["month"] = pd.to_datetime(folio["month"])

folio = folio.drop_duplicates()

folio = folio[folio["total_folios_crore"] > 0]

folio.to_csv(
    os.path.join(PROCESSED_PATH, "06_industry_folio_count_clean.csv"),
    index=False
)

print("Industry Folio cleaned successfully.")
print("Rows:", len(folio))

# -----------------------------
# Clean Portfolio Holdings
# -----------------------------

holdings = pd.read_csv(os.path.join(RAW_PATH, "09_portfolio_holdings.csv"))

holdings["portfolio_date"] = pd.to_datetime(holdings["portfolio_date"])

holdings = holdings.drop_duplicates()

holdings = holdings[holdings["weight_pct"] >= 0]

holdings = holdings[holdings["market_value_cr"] > 0]

holdings.to_csv(
    os.path.join(PROCESSED_PATH, "09_portfolio_holdings_clean.csv"),
    index=False
)

print("Portfolio Holdings cleaned successfully.")
print("Rows:", len(holdings))

# -----------------------------
# Clean Benchmark Indices
# -----------------------------

benchmark = pd.read_csv(os.path.join(RAW_PATH, "10_benchmark_indices.csv"))

benchmark["date"] = pd.to_datetime(benchmark["date"])

benchmark = benchmark.sort_values("date")

benchmark = benchmark.drop_duplicates()

benchmark = benchmark[benchmark["close_value"] > 0]

benchmark.to_csv(
    os.path.join(PROCESSED_PATH, "10_benchmark_indices_clean.csv"),
    index=False
)

print("Benchmark cleaned successfully.")
print("Rows:", len(benchmark))

