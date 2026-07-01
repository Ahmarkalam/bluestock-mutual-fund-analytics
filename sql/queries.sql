-- 1. Top 5 Funds by AUM
SELECT fund_house, aum_crore
FROM [03_aum_by_fund_house]
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV per Month
SELECT substr(date,1,7) AS month,
AVG(nav) AS average_nav
FROM [02_nav_history_clean]
GROUP BY month
ORDER BY month;

-- 3. SIP YoY Growth
SELECT month, yoy_growth_pct
FROM [04_monthly_sip_inflows];

-- 4. Transactions by State
SELECT state,
COUNT(*) AS total_transactions
FROM [08_investor_transactions_clean]
GROUP BY state
ORDER BY total_transactions DESC;

-- 5. Funds with Expense Ratio < 1%
SELECT scheme_name,
expense_ratio_pct
FROM [07_scheme_performance_clean]
WHERE expense_ratio_pct < 1;

-- 6. Category-wise Average Returns
SELECT category,
AVG(return_3yr_pct) AS avg_return
FROM [07_scheme_performance_clean]
GROUP BY category;

-- 7. Risk Category Distribution
SELECT risk_grade,
COUNT(*) AS total_funds
FROM [07_scheme_performance_clean]
GROUP BY risk_grade;

-- 8. Top 10 Holdings by Market Value
SELECT stock_name,
market_value_cr
FROM [09_portfolio_holdings]
ORDER BY market_value_cr DESC
LIMIT 10;

-- 9. Fund House Scheme Count
SELECT fund_house,
COUNT(*) AS total_schemes
FROM [01_fund_master]
GROUP BY fund_house
ORDER BY total_schemes DESC;

-- 10. Benchmark Index Average Close
SELECT index_name,
AVG(close_value) AS avg_close
FROM [10_benchmark_indices]
GROUP BY index_name;