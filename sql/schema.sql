CREATE DATABASE IF NOT EXISTS ops_analytics;
USE ops_analytics;

DROP TABLE IF EXISTS dim_store;
DROP TABLE IF EXISTS dim_product;
DROP TABLE IF EXISTS dim_date;
DROP TABLE IF EXISTS fact_transactions;

CREATE TABLE dim_store (
  store_id INT PRIMARY KEY,
  store_name VARCHAR(100),
  region VARCHAR(50),
  channel VARCHAR(30)
);

CREATE TABLE dim_product (
  product_id INT PRIMARY KEY,
  product_name VARCHAR(100),
  category VARCHAR(50),
  unit_price DECIMAL(10,2)
);

CREATE TABLE dim_date (
  date_id INT PRIMARY KEY,
  date DATE,
  year INT,
  quarter INT,
  month INT,
  day INT,
  day_name VARCHAR(10)
);

CREATE TABLE fact_transactions (
  tx_id BIGINT PRIMARY KEY,
  date_id INT,
  store_id INT,
  product_id INT,
  quantity INT,
  gross_sales DECIMAL(12,2),
  discount DECIMAL(12,2),
  net_sales DECIMAL(12,2),
  customers INT
);
