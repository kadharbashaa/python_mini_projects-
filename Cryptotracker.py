import requests

def get_crypto_price(crypto):
    url = f"https://api.coingecko.com/api/v3/coins/{crypto.lower()}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        
        name = data["name"]
        price = data["market_data"]["current_price"]["usd"]
        high = data["market_data"]["high_24h"]["usd"]
        low = data["market_data"]["low_24h"]["usd"]
        change = data["market_data"]["price_change_percentage_24h"]
        market_cap = data["market_data"]["market_cap"]["usd"]

        print(f"\nName: {name}")
        print(f"Price: ${price:,}")
        print(f"High 24h: ${high:,}")
        print(f"Low 24h: ${low:,}")
        print(f"Change 24h: {change}%")
        print(f"Market Cap: ${market_cap:,}")

    else:
        print("Cryptocurrency not found!")

crypto = input("Enter cryptocurrency (bitcoin/ethereum/doge): ")
get_crypto_price(crypto)
