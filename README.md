Real-Time Crypto Data Pipeline

1. Overview
This project implements an end-to-end real-time data processing platform using a modern streaming architecture.  It continuously ingests live cryptocurrency market data (Bitcoin and Ethereum) from the public CoinGecko API, buffers the high-throughput events in a local Apache Kafka cluster, and processes them using Apache Spark Structured Streaming. The live data and processing outcomes are then visualized dynamically on an interactive Streamlit dashboard.

2. Technology Stack
   Data Source:CoinGecko API fetched via Python `requests`.
   Message Broker:Apache Kafka & Zookeeper.
   Stream Processing:Apache Spark Structured Streaming (Spark version 3.5.0 with Scala 2.12).
   Visualization:Streamlit and Pandas.
   Infrastructure / Containerization:Docker and Docker Compose.

3. Infrastructure Configuration
The core message broker infrastructure is containerized and defined within `docker-compose.yml`.
Zookeeper:Utilizes the `confluentinc/cp-zookeeper:7.3.0` image and listens on client port `2181`.
Apache Kafka:Utilizes the `confluentinc/cp-kafka:7.3.0` image, depends on the Zookeeper service, and maps to port `9092`. 
Networking:Configured with `PLAINTEXT` listeners to seamlessly communicate with the Python producer and PySpark consumer over `localhost:9092`.
Data Topic:All cryptocurrency event messages are routed through the `crypto_prices` topic.

4. Deployment Instructions
To run this pipeline locally, ensure you have Python , Docker, and Docker Compose installed on your system. 

Step 1: Set Up the Environment
Create and activate your Python virtual environment, and install the required dependencies (ensure you have `pyspark`, `kafka-python`, `streamlit`, `pandas`, and `requests` installed):
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
