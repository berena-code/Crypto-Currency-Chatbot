bot_name = "CryptoBuddy"
greeting = "Hey there! 👋 I'm CryptoBuddy, your AI sidekick for smart crypto advice!"

crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

user_query = input("Ask me anything about crypto: ").lower()

if "sustainable" in user_query:
    recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
    print(f"{bot_name}: Invest in {recommend}! 🌱 It's eco-friendly and has long-term potential!")

elif "trending" in user_query or "rising" in user_query:
    trending_coins = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]
    print(f"{bot_name}: These cryptos are rising: {', '.join(trending_coins)} 🚀")

elif "long-term" in user_query or "growth" in user_query:
    for coin, data in crypto_db.items():
        if data["price_trend"] == "rising" and data["sustainability_score"] > 0.7:
            print(f"{bot_name}: {coin} is trending up and very sustainable. Great for long-term growth! 🚀🌱")
            break

elif "best" in user_query:
    best_coin = None
    for coin, data in crypto_db.items():
        if data["price_trend"] == "rising" and data["market_cap"] == "high":
            best_coin = coin
            break
    if best_coin:
        print(f"{bot_name}: {best_coin} is looking profitable with a strong trend and market cap! 💰")

else:
    print(f"{bot_name}: Sorry, I don't have advice for that. Try asking about trends or sustainability!")
    
print("Disclaimer: Crypto is risky—always do your own research! 🚨")
