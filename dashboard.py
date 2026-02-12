import streamlit as st
import json
from kafka import KafkaConsumer
import time
import pandas as pd

st.set_page_config(page_title="Crypto Tracker", layout="wide")

st.title("💰 Real-Time Crypto Dashboard")
st.markdown("Watching **Bitcoin** & **Ethereum** prices live...")

# Create 3 columns for big numbers
col1, col2 = st.columns(2)
with col1:
    btc_ph = st.empty() # Placeholder for Bitcoin
with col2:
    eth_ph = st.empty() # Placeholder for Ethereum

st.divider()
st.subheader("Price History (Last 10 Updates)")

# Placeholder for the chart
chart_ph = st.empty()

# Setup the Kafka Listener
consumer = KafkaConsumer(
    'crypto_prices',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Lists to hold history
history = []

print("🖥️ Dashboard is running...")

for message in consumer:
    data = message.value
    
    # 1. Update the Big Numbers
    btc_price = data['bitcoin_price']
    eth_price = data['ethereum_price']
    
    with col1:
        btc_ph.metric(label="Bitcoin (USD)", value=f"${btc_price:,.2f}")
    with col2:
        eth_ph.metric(label="Ethereum (USD)", value=f"${eth_price:,.2f}")
        
    # 2. Update the Chart
    history.append(data)
    # Keep only last 20 records so chart doesn't get too squished
    if len(history) > 20:
        history.pop(0)
        
    # Convert list to a table for the chart
    df = pd.DataFrame(history)
    chart_ph.line_chart(df[['bitcoin_price', 'ethereum_price']])
    
    # Sleep a tiny bit to not freeze the browser
    time.sleep(0.1)