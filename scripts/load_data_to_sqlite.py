import sqlite3
import pandas as pd
import os

# Create DB connection
conn = sqlite3.connect("retail_oltp.db")

# Define file paths
DATA_DIR = "data/raw"

# Map table names to CSV filenames
tables = {
    "calendar": "calendar_mid.csv",
    "product": "product_mid.csv",
    "store": "store_mid.csv",
    "sales": "sales_mid.csv",
    "inventory": "inventory_mid.csv"
}

# Load and write each CSV to the DB
for table, filename in tables.items():
    path = os.path.join(DATA_DIR, filename)
    if os.path.exists(path):
        df = pd.read_csv(path)
        df.to_sql(table, conn, if_exists='replace', index=False)
        print(f" Loaded: {table}")
    else:
        print(f" Missing: {filename}")

# Close DB connection
conn.close()

print("\n All data loaded into retail_oltp.db")
