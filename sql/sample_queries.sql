SELECT d.year, d.month, SUM(f.net_sales) AS net_sales
FROM fact_transactions f JOIN dim_date d ON f.date_id = d.date_id
GROUP BY d.year, d.month ORDER BY d.year, d.month;