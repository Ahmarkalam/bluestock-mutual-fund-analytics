import pandas as pd


# Load datasets

performance = pd.read_csv(
    "project/data/processed/07_scheme_performance_clean.csv"
)

fund = pd.read_csv(
    "project/data/processed/01_fund_master_clean.csv"
)


# Merge performance with fund details

data = performance.merge(
    fund[
        [
            "amfi_code",
            "scheme_name",
            "risk_category"
        ]
    ],
    on="amfi_code"
)


def recommend_fund(risk):

    filtered = data[
        data["risk_category"].str.lower()
        ==
        risk.lower()
    ]


    recommendation = (
        filtered
        .sort_values(
            "sharpe_ratio",
            ascending=False
        )
        .head(3)
    )


    return recommendation[
    [
        "scheme_name_y",
        "risk_category",
        "sharpe_ratio",
        "return_3yr_pct"
    ]
].rename(
    columns={
        "scheme_name_y": "scheme_name"
    }
)



risk = input(
    "Enter Risk Appetite (Low / Moderate / High): "
)


print(
    "\nTop 3 Recommended Funds:\n"
)


print(
    recommend_fund(risk)
)