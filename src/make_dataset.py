import os, numpy as np, pandas as pd
from datetime import datetime
from utils import to_date_id

BASE = os.path.dirname(os.path.dirname(__file__))
RAW = os.path.join(BASE, "data", "raw")
os.makedirs(RAW, exist_ok=True)

np.random.seed(7)

dates = pd.date_range('2024-01-01','2024-12-31',freq='D')
dim_date = pd.DataFrame({
    "date": dates
})
dim_date["date_id"] = dim_date["date"].apply(to_date_id)
dim_date["year"] = dim_date["date"].dt.year
dim_date["quarter"] = dim_date["date"].dt.quarter
dim_date["month"] = dim_date["date"].dt.month
dim_date["day"] = dim_date["date"].dt.day
dim_date["day_name"] = dim_date["date"].dt.day_name()

stores = [
    (1,"Central","Region A","retail"),
    (2,"Harbour","Region A","retail"),
    (3,"Web North","Region B","digital"),
    (4,"West Mall","Region C","retail"),
    (5,"Web East","Region C","digital")
]
dim_store = pd.DataFrame(stores, columns=["store_id","store_name","region","channel"])

products = [
    (101,"Daily Ticket","Lottery","3.00"),
    (102,"Weekly Max","Lottery","5.00"),
    (201,"Gift 25","Gift","25.00"),
    (202,"Gift 50","Gift","50.00")
]
dim_product = pd.DataFrame(products, columns=["product_id","product_name","category","unit_price"])
dim_product["unit_price"] = dim_product["unit_price"].astype(float)

rows = []
tx_id = 1
for d in dates:
    for sid in dim_store["store_id"]:
        base = 90 if sid in [1,2,4] else 130
        if d.weekday() >= 5:
            base = int(base * 1.25)
        customers = max(int(np.random.normal(base, base*0.15)), 5)
        for _, p in dim_product.iterrows():
            mix = 0.6 if p["category"]=="Lottery" else 0.12
            if "Web" in str(dim_store.loc[dim_store.store_id==sid,"store_name"].values[0]):
                mix *= 1.15
            qty = np.random.poisson(mix * customers)
            if qty <= 0:
                continue
            gross = qty * p["unit_price"]
            disc_rate = np.random.choice([0.0,0.02,0.05], p=[0.7,0.2,0.1])
            discount = round(gross * disc_rate, 2)
            net = round(gross - discount, 2)
            rows.append({
                "tx_id": tx_id,
                "date": d,
                "store_id": sid,
                "product_id": int(p["product_id"]),
                "quantity": int(qty),
                "gross_sales": round(gross,2),
                "discount": discount,
                "net_sales": net,
                "customers": customers
            })
            tx_id += 1

fact = pd.DataFrame(rows)
dim_date.to_csv(os.path.join(RAW,"dim_date.csv"), index=False)
dim_store.to_csv(os.path.join(RAW,"dim_store.csv"), index=False)
dim_product.to_csv(os.path.join(RAW,"dim_product.csv"), index=False)
fact.to_csv(os.path.join(RAW,"fact_transactions.csv"), index=False)
print("Raw data created in data/raw")
