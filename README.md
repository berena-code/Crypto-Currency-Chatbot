# 🚀 CryptoBuddy: Your First AI-Powered Financial Sidekick! 🌟

## 📌 Overview

CryptoBuddy is a **rule-based chatbot** built in Python to provide simple investment advice on cryptocurrencies based on **profitability** (e.g., price trends) and **sustainability** (e.g., energy usage, project viability). This chatbot mimics basic AI decision-making using `if-else` logic and responds to user queries with helpful suggestions.

## 🧠 What You'll Learn

- How AI can assist in financial decisions.
- How to design chatbot logic.
- Basic data analysis using dictionaries and conditionals in Python.

## 💡 Features

- Responds to user queries like:
  - *"Which crypto is trending up?"*
  - *"What’s the most sustainable coin?"*
- Recommends coins based on predefined rules:
  - **Profitability**: Coins with rising price trends and high market cap.
  - **Sustainability**: Coins with low energy use and high sustainability scores.

## 🤖 Chatbot Personality

- **Name**: CryptoBuddy
- **Tone**: Friendly and informative
- **Example greeting**:  
  *"Hey there! Ready to explore some smart and sustainable crypto picks? 💰🌱"*

## 📊 Dataset Used

```python
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
````

## 🧠 How It Works

* User inputs a query.
* Chatbot matches keywords like "sustainable" or "trending" using `if` statements.
* Bot evaluates data using predefined logic and responds with a recommendation.

## 🧪 Sample Interaction

```
You: Which crypto should I buy for long-term growth?
CryptoBuddy: Cardano (ADA) is trending up and has a top-tier sustainability score! 🚀

You: What’s the most sustainable coin?
CryptoBuddy: Invest in Cardano! 🌱 It’s eco-friendly and has long-term potential!
```

## 🧰 Tools & Tech

* Language: Python 🐍
* IDE: Visual Studio Code
* No external libraries required
* (Optional) You can extend this with ChatterBot, NLTK, or CoinGecko API.

## ⚠️ Disclaimer

*Crypto is risky—always do your own research before making investment decisions.*

---


