import yfinance as yf
import matplotlib.pyplot as plt

data = yf.download("AAPL", start="2020-01-01", end="2024-01-01")

data["SMA10"] = data["Close"].rolling(window=10).mean()
data["SMA30"] = data["Close"].rolling(window=30).mean()
data["SMA80"] = data["Close"].rolling(window=80).mean()
data["SMA200"] = data["Close"].rolling(window=200).mean()

data[["Close", "SMA10", "SMA30", "SMA80", "SMA200"]].plot(title = "AAPL Closing Price with moving averages (10,30,80,200)")

plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.show()
