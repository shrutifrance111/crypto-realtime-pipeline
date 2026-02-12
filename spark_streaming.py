import os
import sys

# --- FORCE FIX START ---
# We must clear these variables to stop the "Zombie Spark" (v4.1.1) from loading
if 'SPARK_HOME' in os.environ:
    del os.environ['SPARK_HOME']
if 'PYTHONPATH' in os.environ:
    del os.environ['PYTHONPATH']
# --- FORCE FIX END ---

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

print("🚀 Starting Spark Stream (Standalone Mode)...")

# 1. Create Spark Session
# We use Scala 2.12 and Spark 3.5.0 explicitly
spark = SparkSession.builder \
    .appName("CryptoStream") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0") \
    .config("spark.sql.shuffle.partitions", "2") \
    .getOrCreate()

# Turn off noisy logs
spark.sparkContext.setLogLevel("WARN")

# 2. Define Schema
schema = StructType([
    StructField("timestamp", DoubleType(), True),
    StructField("bitcoin_price", DoubleType(), True),
    StructField("ethereum_price", DoubleType(), True)
])

# 3. Read from Kafka
try:
    df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("subscribe", "crypto_prices") \
        .option("startingOffsets", "earliest") \
        .load()

    # 4. Process
    parsed_df = df.select(
        from_json(col("value").cast("string"), schema).alias("data")
    ).select("data.*")

    # 5. Show Output
    print("✅ Spark is ready! Watching for data...")
    query = parsed_df \
        .writeStream \
        .outputMode("append") \
        .format("console") \
        .start()

    query.awaitTermination()

except Exception as e:
    print(f"❌ Error: {e}")