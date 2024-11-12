import yfinance as yf
import time

def get_realtime_price(ticker):
    """Fetches the latest price of the given stock ticker."""
    stock = yf.Ticker(ticker)
    data = stock.history(period='1d', interval='1m')

    if not data.empty and 'Close' in data.columns:
        # Use iloc to get the last closing price
        return data['Close'].iloc[-1]
    else:
        print(f"No data available for {ticker}. It may be delisted or invalid.")
        return None

ticker = 'AAPL'  # Change this to your desired ticker

try:
    while True:
        current_price = get_realtime_price(ticker)
        if current_price is not None:
            print(f"Current price of {ticker}: {current_price}")
        time.sleep(1)  # Wait for 1 second
except KeyboardInterrupt:
    print("Stopped fetching data.")