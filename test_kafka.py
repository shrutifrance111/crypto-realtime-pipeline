from kafka import KafkaConsumer
import json

print("👂 Listening for crypto prices...")

# connect to the "crypto_prices" tube
consumer = KafkaConsumer(
    'crypto_prices',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest', # Start from the beginning
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    data = message.value
    print(f"Received: Bitcoin is ${data['bitcoin_price']}")