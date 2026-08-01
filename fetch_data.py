import yfinance as yf
import matplotlib.pyplot as plt

data = yf.download("AAPL", start="2020-01-01", end="2024-01-01")
data["Close"].plot(title = "AAPL Closing Price")
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()
