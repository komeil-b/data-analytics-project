# Operations Analytics Project
Small project to showcase my knowledge of SQL, Power BI, and Python for data generation and cleaning. It uses a SQL schema, and a Power BI dashboard to showcase the data. 

## Stack
- Python, pandas, NumPy
- MySQL Workbench
- Power BI

## What I Did:
1. Generated a synthetic retail style dataset using a Python script to create raw CSVs for date, store, product, and transactions.
2. Cleaned and standardized the data with a second Python script to produce analytics ready tables in a simple star schema.
3. Built a relational model in MySQL Workbench using a schema file with fact and dimension tables.
4. Imported the processed CSVs into MySQL tables and verified row counts for each table.
5. Wrote SQL analysis queries to check data quality and produce summaries like monthly sales, sales by region, and sales by product.
6. Connected Power BI Desktop to the processed CSVs and created relationships between fact and dimension tables.
7. Created DAX measures for key KPIs: Total Sales, Total Customers, and Avg Basket Size.
8. Designed a dashboard with line, bar, and pie charts, plus card visuals, plus slicers for date, region, channel, and product category.