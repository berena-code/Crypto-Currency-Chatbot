import requests
import re

bot_name = "CryptoBuddy"
greeting = "Hey there! 👋 I'm CryptoBuddy, your AI sidekick for smart crypto advice!"

def fetch_crypto_db():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 50,
        "page": 1,
        "sparkline": "false"
    }
    response = requests.get(url, params=params)
    data = response.json()
    crypto_db = {}
    symbol_lookup = {}
    for coin in data:
        name = coin['name'].lower()
        symbol = coin['symbol'].lower()
        crypto_db[name] = {
            "symbol": coin['symbol'].upper(),
            "price": coin['current_price'],
            "market_cap": coin['market_cap'],
            "price_trend": "rising" if coin['price_change_percentage_24h'] > 0 else "falling",
            "price_change_24h": coin['price_change_percentage_24h'],
        }
        symbol_lookup[symbol] = name
    return crypto_db, symbol_lookup

def find_coin_in_query(user_query, crypto_db, symbol_lookup):
    words = user_query.split()
    for word in words:
        word = word.lower()
        if word in crypto_db:
            return word, crypto_db[word]
        if word in symbol_lookup:
            name = symbol_lookup[word]
            return name, crypto_db[name]
    return None, None

def main():
    print(greeting)
    print("Type 'help' for options or 'exit' to quit.")
    crypto_db, symbol_lookup = fetch_crypto_db()

    while True:
        user_query = input("You: ").lower().strip()
        if user_query in ["exit", "quit"]:
            print(f"{bot_name}: Goodbye! 👋")
            break

        if any(greet in user_query for greet in ["hello", "hi", "hey"]):
            print(f"{bot_name}: {greeting}")

        elif "help" in user_query:
            print(f"""{bot_name}: You can ask me about:
    - Price of a coin (e.g. "price bitcoin" or "price eth")
    - Market cap of a coin (e.g. "market cap ethereum" or "market cap btc")
    - 24h change of a coin (e.g. "change solana")
    - Symbol of a coin (e.g. "symbol dogecoin")
    - Trending/rising coins
    - Top currency or top N currencies (e.g. "top currency", "top 5 currencies")
    - Type 'exit' to quit.
    """)

        elif "top currency" in user_query or "top coin" in user_query:
            # Show the top 1 coin by market cap
            top = sorted(crypto_db.items(), key=lambda x: -x[1]['market_cap'])
            name, info = top[0]
            print(f"{bot_name}: The top currency is {name.title()} (${info['symbol']}), price: ${info['price']:,}, market cap: ${info['market_cap']:,}")

        elif "top" in user_query and ("currenc" in user_query or "coin" in user_query):
            # e.g. "top 5 currencies"
            match = re.search(r'top\s+(\d+)', user_query)
            n = int(match.group(1)) if match else 5
            top = sorted(crypto_db.items(), key=lambda x: -x[1]['market_cap'])[:n]
            print(f"{bot_name}: Top {n} currencies by market cap:")
            for i, (name, info) in enumerate(top, 1):
                print(f"  {i}. {name.title()} (${info['symbol']}): ${info['price']:,} (Market Cap: ${info['market_cap']:,})")

        elif "price" in user_query:
            coin_name, info = find_coin_in_query(user_query, crypto_db, symbol_lookup)
            if info:
                print(f"{bot_name}: {coin_name.title()} (${info['symbol']}): ${info['price']:,}")
            else:
                print(f"{bot_name}: Please specify a coin (e.g. 'price bitcoin').")

        elif "market cap" in user_query:
            coin_name, info = find_coin_in_query(user_query, crypto_db, symbol_lookup)
            if info:
                print(f"{bot_name}: {coin_name.title()} market cap: ${info['market_cap']:,}")
            else:
                print(f"{bot_name}: Please specify a coin (e.g. 'market cap ethereum').")

        elif "change" in user_query:
            coin_name, info = find_coin_in_query(user_query, crypto_db, symbol_lookup)
            if info:
                print(f"{bot_name}: {coin_name.title()} 24h change: {info['price_change_24h']:.2f}% ({info['price_trend']})")
            else:
                print(f"{bot_name}: Please specify a coin (e.g. 'change solana').")

        elif "symbol" in user_query:
            coin_name, info = find_coin_in_query(user_query, crypto_db, symbol_lookup)
            if info:
                print(f"{bot_name}: {coin_name.title()} symbol: {info['symbol']}")
            else:
                print(f"{bot_name}: Please specify a coin (e.g. 'symbol dogecoin').")

        elif "trending" in user_query or "rising" in user_query:
            trending = [name.title() for name, info in crypto_db.items() if info["price_trend"] == "rising"]
            if trending:
                print(f"{bot_name}: These cryptos are rising: {', '.join(trending[:10])} 🚀")
            else:
                print(f"{bot_name}: No trending coins found right now.")

        else:
            print(f"{bot_name}: Sorry, I don't have advice for that. Type 'help' to see what I can do!")

        print("Disclaimer: Crypto is risky—always do your own research! 🚨")

if __name__ == "__main__":
    main()