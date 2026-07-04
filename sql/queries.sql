SELECT fund_house, aum_crore
FROM [03_aum_by_fund_house]
ORDER BY aum_crore DESC
LIMIT 5;

SELECT substr(date,1,7) AS month,
AVG(nav) AS average_nav
FROM [02_nav_history_clean]
GROUP BY month
ORDER BY month;

SELECT month, yoy_growth_pct
FROM [04_monthly_sip_inflows];

SELECT state,
COUNT(*) AS total_transactions
FROM [08_investor_transactions_clean]
GROUP BY state
ORDER BY total_transactions DESC;

SELECT scheme_name,
expense_ratio_pct
FROM [07_scheme_performance_clean]
WHERE expense_ratio_pct < 1;

SELECT category,
AVG(return_3yr_pct) AS avg_return
FROM [07_scheme_performance_clean]
GROUP BY category;

SELECT risk_grade,
COUNT(*) AS total_funds
FROM [07_scheme_performance_clean]
GROUP BY risk_grade;

SELECT stock_name,
market_value_cr
FROM [09_portfolio_holdings]
ORDER BY market_value_cr DESC
LIMIT 10;

SELECT fund_house,
COUNT(*) AS total_schemes
FROM [01_fund_master]
GROUP BY fund_house
ORDER BY total_schemes DESC;

SELECT index_name,
AVG(close_value) AS avg_close
FROM [10_benchmark_indices]
GROUP BY index_name;