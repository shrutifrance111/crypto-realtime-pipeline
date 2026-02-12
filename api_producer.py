from kafka import KafkaProducer
import requests
import json
import time

# 1. Setup the Kafka "Sender"
# This tells Python where the tube is (localhost:9092)
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# 2. URL for CoinGecko
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"

print("🚀 Producer started! Sending prices to Kafka...")

while True:
    try:
        # Get data from the internet
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            
            # Check if we actually got the data
            if 'bitcoin' in data:
                # Create the message package
                message = {
                    'timestamp': time.time(),
                    'bitcoin_price': data['bitcoin']['usd'],
                    'ethereum_price': data['ethereum']['usd']
                }
                
                # Send it into the 'crypto_prices' tube
                producer.send('crypto_prices', value=message)
                
                print(f"✅ Sent: Bitcoin ${message['bitcoin_price']}")
            else:
                print("⚠️  Got data but no Bitcoin price found.")
                
        elif response.status_code == 429:
            print("🛑  Too many requests! Waiting 60 seconds...")
            time.sleep(60)

    except Exception as e:
        print(f"❌  Error: {e}")

    # Wait 30 seconds before sending the next price
    time.sleep(30)