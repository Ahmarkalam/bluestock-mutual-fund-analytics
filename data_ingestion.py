import os
import pandas as pd

DATA_PATH = "project/data/raw"

csv_files = [f for f in os.listdir(DATA_PATH) if f.endswith(".csv")]

print(f"\nTotal CSV Files Found: {len(csv_files)}")

for file in csv_files:
    print("\n" + "=" * 60)
    print(f"Dataset: {file}")

    file_path = os.path.join(DATA_PATH, file)
    df = pd.read_csv(file_path)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\n" + "=" * 60)
print("FUND MASTER EXPLORATION")
print("=" * 60)

fund_master = pd.read_csv(os.path.join(DATA_PATH, csv_files[0]))

print("\nColumns:")
print(fund_master.columns.tolist())

print("\nFirst 5 Rows:")
print(fund_master.head())

print("\nUnique Fund Houses:")
print(fund_master["fund_house"].unique())

print("\nCategories:")
print(fund_master["category"].unique())

print("\nSub Categories:")
print(fund_master["sub_category"].unique())

print("\nRisk Grades:")
print(fund_master["risk_category"].unique())

print("\n" + "=" * 60)
print("AMFI CODE VALIDATION")
print("=" * 60)

nav_history = pd.read_csv(os.path.join(DATA_PATH, "02_nav_history.csv"))

fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = fund_codes - nav_codes

print(f"Total Fund Master Codes : {len(fund_codes)}")
print(f"Total NAV Codes         : {len(nav_codes)}")

if len(missing_codes) == 0:
    print("\nAll AMFI codes exist in nav_history.")
else:
    print("\nMissing AMFI Codes:")
    print(missing_codes)