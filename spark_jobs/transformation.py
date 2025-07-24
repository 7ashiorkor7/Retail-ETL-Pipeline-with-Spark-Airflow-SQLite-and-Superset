from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, to_date

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Retail ETL Pipeline") \
    .getOrCreate()

# Load CSV files (update paths if needed)
stores = spark.read.csv("/opt/app/data/raw/store.csv", header=True, inferSchema=True)
sales = spark.read.csv("/opt/app/data/raw/sales.csv", header=True, inferSchema=True)
products = spark.read.csv("/opt/app/data/raw/product.csv", header=True, inferSchema=True)
inventory = spark.read.csv("/opt/app/data/raw/inventory.csv", header=True, inferSchema=True)
calendar = spark.read.csv("/opt/app/data/raw/calendar.csv", header=True, inferSchema=True)


# Convert string dates to date types
sales = sales.withColumn("TRANS_DT", to_date(col("TRANS_DT"), "yyyy-MM-dd"))
inventory = inventory.withColumn("CAL_DT", to_date(col("CAL_DT"), "yyyy-MM-dd"))
calendar = calendar.withColumn("CAL_DT", to_date(col("CAL_DT"), "yyyy-MM-dd"))

# Filter only active products
products_active = products.filter(col("STATUS_CODE") == 1)

# Join sales with product info
sales_enriched = sales.join(products_active, on="PROD_KEY", how="left")

# Join sales with store info
sales_enriched = sales_enriched.join(stores, on="STORE_KEY", how="left")

# Join sales with calendar for time attributes
sales_enriched = sales_enriched.join(calendar.withColumnRenamed("CAL_DT", "TRANS_DT"), on="TRANS_DT", how="left")

# Calculate Discount Percentage and Gross Margin
sales_transformed = sales_enriched.withColumn(
    "DISCOUNT_PCT", when(col("SALES_AMT") != 0, col("DISCOUNT") / col("SALES_AMT")).otherwise(0)
).withColumn(
    "GROSS_MARGIN", col("SALES_AMT") - col("SALES_COST") - col("SHIP_COST")
)

# Aggregate KPIs by Store and Product Category
sales_summary = sales_transformed.groupBy(
    "STORE_KEY", "STORE_DESC", "CATEGORY_NAME"
).agg(
    {"SALES_AMT": "sum", "SALES_QTY": "sum", "GROSS_MARGIN": "sum"}
).withColumnRenamed("sum(SALES_AMT)", "TOTAL_SALES_AMT") \
 .withColumnRenamed("sum(SALES_QTY)", "TOTAL_SALES_QTY") \
 .withColumnRenamed("sum(GROSS_MARGIN)", "TOTAL_GROSS_MARGIN")

# Show aggregated results
# sales_summary.printSchema()
# sales_summary.show(n=20, truncate=False)

# Save the result for downstream consumption
sales_summary.write.mode("overwrite").parquet("output/sales_summary")

# Stop Spark session
spark.stop()
