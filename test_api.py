import requests
import time

# URL for CoinGecko API
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"

print("🚀 Starting to fetch prices... (Press Ctrl+C to stop)")

while True:
    try:
        # Get data from the internet
        response = requests.get(url)
        
        # Check if the website is happy (Status code 200 means OK)
        if response.status_code == 200:
            data = response.json()
            
            # Check if 'bitcoin' is actually in the data
            if 'bitcoin' in data:
                print(f"💰 Bitcoin: ${data['bitcoin']['usd']}")
                print(f"💎 Ethereum: ${data['ethereum']['usd']}")
                print("-----------------------------")
            else:
                # If we get data but no bitcoin, print what we got
                print("⚠️  We got data, but no prices. Here is what CoinGecko sent:")
                print(data)
                
        elif response.status_code == 429:
            print("🛑  Too many requests! We need to wait longer.")
            time.sleep(60) # Wait an extra minute
            
        else:
            print(f"❌  Error from website: Status Code {response.status_code}")

    except Exception as e:
        print(f"💥  Crash report: {e}")

    # Wait 30 seconds (Increased from 10 to stop getting blocked)
    print("... sleeping for 30 seconds ...")
    time.sleep(30)