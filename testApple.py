import requests
from bs4 import BeautifulSoup

# URL of the website with stock data (make sure it's a legal site to scrape)
url = "https://finance.yahoo.com/quote/AAPL"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the current price (may vary depending on the site's structure)
price = soup.find('fin-streamer', {'data-field': 'regularMarketPrice'}).text

print(f"Current price of Apple (AAPL): {price}")