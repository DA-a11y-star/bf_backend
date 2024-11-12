import yfinance as yf
import pandas as pd

# Fetch historical data for Apple Inc. (AAPL) for the last 30 days
ticker_symbol = "AAPL"
stock_data = yf.Ticker(ticker_symbol)
historical_data = stock_data.history(period="5d", interval = "1m")  # You can adjust the period as needed

# Display the historical data
print(historical_data.head())

import matplotlib.pyplot as plt

# Plotting the closing prices
plt.figure(figsize=(12, 6))
plt.plot(historical_data.index, historical_data['Close'], label='Closing Price', color='blue')
plt.title(f"{ticker_symbol} Closing Prices Over Last 30 Days")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.xticks(rotation=45)  # Rotate date labels for better readability
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(12, 6))
plt.bar(historical_data.index, historical_data['Volume'], label='Volume', color='gray')
plt.title(f"{ticker_symbol} Trading Volume Over Last 30 Days")
plt.xlabel("Date")
plt.ylabel("Volume")
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.show()

historical_data['SMA_10'] = historical_data['Close'].rolling(window=10).mean()  # 10-day moving average

plt.figure(figsize=(12, 6))
plt.plot(historical_data.index, historical_data['Close'], label='Closing Price', color='blue')
plt.plot(historical_data.index, historical_data['SMA_10'], label='10-Day SMA', color='orange')
plt.title(f"{ticker_symbol} Closing Prices with 10-Day SMA")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.show()