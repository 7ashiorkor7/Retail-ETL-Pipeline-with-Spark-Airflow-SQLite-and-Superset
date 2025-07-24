from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def main():
    # Initialize SparkSession
    spark = SparkSession.builder.appName("RetailETL").getOrCreate()
    
    # Read raw data CSV
    df = spark.read.csv("/data/raw/sales.csv", header=True, inferSchema=True)
    
    # Example transformation: filter orders with quantity > 10
    filtered_df = df.filter(col("quantity") > 10)
    
    # Example aggregation: total quantity per product
    agg_df = filtered_df.groupBy("product_id").sum("quantity").withColumnRenamed("sum(quantity)", "total_quantity")
    
    # Write output to parquet (or CSV)
    agg_df.write.mode("overwrite").parquet("/data/processed/product_totals.parquet")
    
    spark.stop()

if __name__ == "__main__":
    main()
