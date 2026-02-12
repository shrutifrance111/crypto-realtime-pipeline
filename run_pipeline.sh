#!/bin/bash

echo "🚀 Starting the Data Pipeline..."

# 1. Activate the environment
source venv/bin/activate

# 2. Start Zookeeper & Kafka (in case they aren't running)
echo "   [1/4] Checking Docker..."
docker compose up -d
sleep 5  # Wait for it to wake up

# 3. Start the Producer (Hidden in background)
echo "   [2/4] Starting API Producer..."
nohup python api_producer.py > producer.log 2>&1 &
PRODUCER_PID=$!
echo "         Producer running with PID: $PRODUCER_PID"

# 4. Start Spark (Hidden in background)
echo "   [3/4] Starting Spark Processor..."
nohup python spark_streaming.py > spark.log 2>&1 &
SPARK_PID=$!
echo "         Spark running with PID: $SPARK_PID"

# 5. Start the Dashboard (Visible!)
echo "   [4/4] Launching Dashboard..."
streamlit run dashboard.py

# When you press Ctrl+C on the dashboard, kill the other hidden programs
kill $PRODUCER_PID
kill $SPARK_PID
echo "🛑 Pipeline stopped."