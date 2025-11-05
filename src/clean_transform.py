import os, pandas as pd
from utils import to_date_id

BASE = os.path.dirname(os.path.dirname(__file__))
RAW = os.path.join(BASE, "data", "raw")
PROC = os.path.join(BASE, "data", "processed")
os.makedirs(PROC, exist_ok=True)

dim_date = pd.read_csv(os.path.join(RAW,"dim_date.csv"), parse_dates=["date"])
dim_store = pd.read_csv(os.path.join(RAW,"dim_store.csv"))
dim_product = pd.read_csv(os.path.join(RAW,"dim_product.csv"))
fact = pd.read_csv(os.path.join(RAW,"fact_transactions.csv"), parse_dates=["date"])

fact["date_id"] = fact["date"].apply(to_date_id)
fact["discount"] = fact["discount"].clip(lower=0)
fact["net_sales"] = fact["net_sales"].clip(lower=0)

out_date = dim_date.copy()
out_date["date_id"] = out_date["date"].apply(to_date_id)
out_date = out_date[["date_id","date","year","quarter","month","day","day_name"]]

dim_store.to_csv(os.path.join(PROC,"dim_store.csv"), index=False)
dim_product.to_csv(os.path.join(PROC,"dim_product.csv"), index=False)
out_date.to_csv(os.path.join(PROC,"dim_date.csv"), index=False)

fact_out = fact[["tx_id","date_id","store_id","product_id","quantity","gross_sales","discount","net_sales","customers"]]
fact_out.to_csv(os.path.join(PROC,"fact_transactions.csv"), index=False)

print("Processed data written to data/processed")
