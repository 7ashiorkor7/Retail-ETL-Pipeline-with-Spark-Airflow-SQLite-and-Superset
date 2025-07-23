import pandas as pd
import random
from datetime import datetime, timedelta
import os

# Make sure output folder exists
os.makedirs('data/raw', exist_ok=True)

### 1. Calendar Data
start_date = datetime(2020, 1, 1)
calendar_data = []

for i in range(100):
    date = start_date + timedelta(days=i)
    calendar_data.append({
        "CAL_DT": date.strftime("%Y-%m-%d"),
        "CAL_TYPE_DESC": "Fiscal",
        "DAY_OF_WK_NUM": date.weekday() + 1,
        "DAY_OF_WK_DESC": date.strftime("%A"),
        "YR_NUM": date.year,
        "WK_NUM": date.isocalendar()[1],
        "YR_WK_NUM": int(f"{date.year}{date.isocalendar()[1]:02}"),
        "MNTH_NUM": date.month,
        "YR_MNTH_NUM": int(f"{date.year}{date.month}"),
        "QTR_NUM": (date.month - 1) // 3 + 1,
        "YR_QTR_NUM": int(f"{date.year}{(date.month - 1) // 3 + 1}")
    })

pd.DataFrame(calendar_data).to_csv("data/raw/calendar_mid.csv", index=False)

### 2. Product Data
product_data = []
for i in range(1, 101):
    product_data.append({
        "PROD_KEY": i,
        "PROD_NAME": f"Product-{i}",
        "VOL": round(random.uniform(0.5, 5.0), 2),
        "WGT": round(random.uniform(10.0, 50.0), 2),
        "BRAND_NAME": f"brand-{random.randint(1, 20)}",
        "STATUS_CODE": 1,
        "STATUS_CODE_NAME": "active",
        "CATEGORY_KEY": random.randint(1, 5),
        "CATEGORY_NAME": f"category-{random.randint(1, 5)}",
        "SUBCATEGORY_KEY": random.randint(1, 5),
        "SUBCATEGORY_NAME": f"subcategory-{random.randint(1, 5)}"
    })

pd.DataFrame(product_data).to_csv("data/raw/product_mid.csv", index=False)

### 3. Store Data
store_data = []
for i in range(1, 51):
    store_data.append({
        "STORE_KEY": i,
        "STORE_NUM": i,
        "STORE_DESC": f"store_desc{i}",
        "ADDR": f"addr_{i}",
        "CITY": f"city_{i}",
        "REGION": "",
        "CNTRY_CD": "US",
        "CNTRY_NM": "US",
        "POSTAL_ZIP_CD": "",
        "PROV_STATE_DESC": "WI",
        "PROV_STATE_CD": "WI",
        "STORE_TYPE_CD": "ABC",
        "STORE_TYPE_DESC": "ABC",
        "FRNCHS_FLG": random.choice(["Y", "N"]),
        "STORE_SIZE": "",
        "MARKET_KEY": random.randint(1, 10),
        "MARKET_NAME": f"market_{random.randint(1, 10)}",
        "SUBMARKET_KEY": random.randint(1, 5),
        "SUBMARKET_NAME": f"submarket_{random.randint(1, 5)}",
        "LATITUDE": round(random.uniform(35.0, 50.0), 6),
        "LONGITUDE": round(random.uniform(-120.0, -70.0), 6)
    })

pd.DataFrame(store_data).to_csv("data/raw/store_mid.csv", index=False)

### 4. Sales Data
sales_data = []
for i in range(1, 1001):
    prod_key = random.randint(1, 100)
    store_key = random.randint(1, 50)
    date = start_date + timedelta(days=random.randint(0, 99))
    qty = random.randint(1, 10)
    price = round(random.uniform(1.0, 20.0), 2)
    amt = round(qty * price, 2)
    cost = round(amt * 0.9, 2)
    mgrn = round(amt - cost, 2)
    discount = round(random.uniform(0.0, 0.2), 2)

    sales_data.append({
        "TRANS_ID": i,
        "PROD_KEY": prod_key,
        "STORE_KEY": store_key,
        "TRANS_DT": date.strftime("%Y-%m-%d"),
        "TRANS_TIME": random.randint(0, 23),
        "SALES_QTY": qty,
        "SALES_PRICE": price,
        "SALES_AMT": amt,
        "DISCOUNT": discount,
        "SALES_COST": cost,
        "SALES_MGRN": mgrn,
        "SHIP_COST": round(random.uniform(0.5, 5.0), 2)
    })

pd.DataFrame(sales_data).to_csv("data/raw/sales_mid.csv", index=False)

### 5. Inventory Data
inventory_data = []
for i in range(1, 1001):
    prod_key = random.randint(1, 100)
    store_key = random.randint(1, 50)
    date = start_date + timedelta(days=random.randint(0, 99))

    inventory_data.append({
        "CAL_DT": date.strftime("%Y-%m-%d"),
        "STORE_KEY": store_key,
        "PROD_KEY": prod_key,
        "INVENTORY_ON_HAND_QTY": round(random.uniform(0, 100), 2),
        "INVENTORY_ON_ORDER_QTY": round(random.uniform(0, 100), 2),
        "OUT_OF_STOCK_FLG": random.choice([0, 1]),
        "WASTE_QTY": round(random.uniform(0, 10), 2),
        "PROMOTION_FLG": random.choice([True, False]),
        "NEXT_DELIVERY_DT": (date + timedelta(days=random.randint(1, 7))).strftime("%Y-%m-%d")
    })

pd.DataFrame(inventory_data).to_csv("data/raw/inventory_mid.csv", index=False)

print("All dummy datasets generated in 'data/raw/' folder.")
