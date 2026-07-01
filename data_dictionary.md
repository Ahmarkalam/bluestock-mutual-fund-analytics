# Mutual Fund Analytics - Data Dictionary

## 01_fund_master.csv
| Column | Data Type | Description |
|--------|-----------|-------------|
| amfi_code | Integer | Unique AMFI scheme code |
| fund_house | Text | Mutual fund company |
| scheme_name | Text | Name of the scheme |
| category | Text | Fund category |
| sub_category | Text | Fund sub-category |
| plan | Text | Regular/Direct plan |
| launch_date | Date | Scheme launch date |
| benchmark | Text | Benchmark index |
| expense_ratio_pct | Float | Expense ratio (%) |
| exit_load_pct | Float | Exit load (%) |
| min_sip_amount | Integer | Minimum SIP amount |
| min_lumpsum_amount | Integer | Minimum lumpsum amount |
| fund_manager | Text | Fund manager |
| risk_category | Text | Risk level |
| sebi_category_code | Text | SEBI category code |

## 02_nav_history.csv
Stores daily NAV values for each AMFI scheme.

## 03_aum_by_fund_house.csv
Contains Assets Under Management (AUM) details for each fund house.

## 04_monthly_sip_inflows.csv
Monthly SIP inflows and growth statistics.

## 05_category_inflows.csv
Monthly net inflows by mutual fund category.

## 06_industry_folio_count.csv
Industry-wide folio count statistics.

## 07_scheme_performance.csv
Historical returns, ratios and performance metrics.

## 08_investor_transactions.csv
Investor transaction details including transaction type, amount and KYC status.

## 09_portfolio_holdings.csv
Portfolio holdings of mutual fund schemes.

## 10_benchmark_indices.csv
Historical benchmark index closing values.