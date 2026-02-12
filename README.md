# Real-Time Cryptocurrency Data Pipeline 💰🚀

## Overview
This is an end-to-end data engineering project that fetches, processes, and visualizes real-time cryptocurrency data. It uses a **Kappa Architecture** to ensure fault tolerance and low latency.

## Architecture
**Source** (CoinGecko API) -> **Ingestion** (Kafka + Zookeeper) -> **Processing** (Spark Structured Streaming) -> **Visualization** (Streamlit Dashboard)

## Technologies Used 🛠️
* **Language:** Python 3.12
* **Message Broker:** Apache Kafka & Zookeeper
* **Processing Engine:** Apache Spark (PySpark)
* **Containerization:** Docker & Docker Compose
* **Visualization:** Streamlit

## Features
* ✅ **Real-Time Streaming:** Fetches Bitcoin & Ethereum prices every 30 seconds.
* ✅ **Fault Tolerance:** Uses Spark Checkpointing and Kafka retention policies.
* ✅ **Interactive Dashboard:** Live-updating charts for price trends.
* ✅ **Scalable:** Built on Docker containers for easy deployment.

## How to Run
1.  Clone the repository:
    ```bash
    git clone [https://github.com/shrutifrance111/crypto-realtime-pipeline.git](https://github.com/shrutifrance111/crypto-realtime-pipeline.git)
    ```
2.  Start the services:
    ```bash
    ./run_pipeline.sh
    ```
