import yfinance as yf
import matplotlib.pyplot as plt

data = yf.download("AAPL", start="2020-01-01", end="2024-01-01")

data["SMA10"] = data["Close"].rolling(window=10).mean()
data["SMA30"] = data["Close"].rolling(window=30).mean()
data["SMA80"] = data["Close"].rolling(window=80).mean()
data["SMA200"] = data["Close"].rolling(window=200).mean()

#plot of various Close moving averages (10,30,80,200) against Close
'''
data[["Close", "SMA10", "SMA30", "SMA80", "SMA200"]].plot(title = "AAPL Closing Price with moving averages (10,30,80,200)")

plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.show()
'''
data["Signal"] = data["SMA80"] < data["SMA30"]
data["Signal_changed"] = data["Signal"] != data["Signal"].shift(1)

data["Daily_return"] = data["Close"].pct_change()
data["Strategy_return"] = data["Daily_return"] * data["Signal"].shift(1)

data["Cumulative_market"] = (1 + data["Daily_return"]).cumprod()
data["Cumulative_strategy"] = (1+ data["Strategy_return"]).cumprod()

data[["Cumulative_market", "Cumulative_strategy"]].plot(title="Strategy vs Buy-and-Hold")
plt.xlabel("Date")
plt.ylabel("Growth of $1")
plt.show()