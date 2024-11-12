import yfinance as yf
import sys
import os

# Define the stock symbol (e.g., AAPL for Apple Inc.)
tickerLog = []
count = [
    'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'META', 'NVDA', 'NFLX', 'BABA', 'V',
    'JPM', 'JNJ', 'PG', 'DIS', 'UNH', 'HD', 'MA', 'PYPL', 'XOM', 'KO',
    'PFE', 'MRK', 'PEP', 'NKE', 'INTC', 'CSCO', 'T', 'WMT', 'VZ', 'CVX',
    'ADBE', 'ORCL', 'COST', 'QCOM', 'AMD', 'CRM', 'IBM', 'SBUX', 'GS', 'CAT',
    'BA', 'GE', 'MMM', 'HON', 'LOW', 'TXN', 'DHR', 'LIN', 'MDT', 'AMGN',
    'AVGO', 'BMY', 'GILD', 'ABT', 'VRTX', 'REGN', 'SPGI', 'BLK', 'TMO', 'ADI',
    'NOW', 'FIS', 'ISRG', 'ATVI', 'MU', 'ILMN', 'AMAT', 'SHOP', 'ZM', 'DOCU',
    'SNOW', 'PLTR', 'SQ', 'ROKU', 'RBLX', 'AFRM', 'TTD', 'OKTA', 'TEAM', 'CRWD',
    'DDOG', 'ZS', 'NET', 'MDB', 'ZSAN', 'PINS', 'UBER', 'LYFT', 'DASH', 'TWLO',
    'FVRR', 'BIDU', 'JD', 'NTES', 'SINA', 'CHWY', 'ETSY', 'SE', 'MELI', 'GRUB'
]

ticker_list = [[ticker, 0] for ticker in count]

class SilentError:
    def __enter__(self):
        self._original_stderr = sys.stderr
        sys.stderr = open(os.devnull, 'w')  # Redirect stderr to null
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stderr.close()
        sys.stderr = self._original_stderr  # Restore original stderr


def testGrab(testTicker):
    try:
        with SilentError():  # Suppress error messages
            # Attempt to download stock data
            stock = yf.Ticker(testTicker)
            data = stock.history(period="1d")

        # Check if data is empty (could be delisted or invalid)
        if data.empty:
            raise ValueError(f"{testTicker}: possibly delisted; no data found; Try Again \n")

        # If data is valid, return the latest closing price
        return 1

    except ValueError as ve:
        # Specific handling for ValueError (empty data)
        print(ve)
        return None

    except Exception as e:
        # General exception handling
        print(f"An unexpected error occurred: {e}")
        return None


def updateCount(currentTicker):
    currentTicker = currentTicker.upper()
    index = next((idx for idx, item in enumerate(ticker_list) if item[0] == currentTicker), -1)
    ticker_list[index][1] += 1


def displayData(amount, live = True, day = False):
    # Sort the list based on the value inside the nested list
    # Sort the original list in-place
    ticker_list.sort(key=lambda x: x[1], reverse=True)
    tickerLog = []
    if amount > 5:
        amount = 5
    for i in range(amount):
        tickerLog.append(ticker_list[i])
        stock = yf.Ticker(ticker_list[i][0])
        price = stock.history(period="1d", interval="1m")
        if day:
            print(price)
        if live:
            live_price = price['Close'].iloc[-1]
            print(f"The current price of {ticker_list[i][0]} is: {live_price}")





def userStocks():
    while True:
        try:
            tickerAmount = int(input("How Many Stock Prices would you Like to Look at Today? "))
            break
        except ValueError:
            print("You must provide an integer value. Try Again")

    for i in range(tickerAmount):
        while True:
            grab = str(input("What stock price would you like to view today? "))
            if testGrab(grab) == 1:
                break
        updateCount(grab)

    displayData(tickerAmount)

def main():
    userStocks()

if __name__ == '__main__':
    main()


    # live_price = price['Close'].iloc[-1]
    # print(f"The current price of {ticker} is: {live_price}")



