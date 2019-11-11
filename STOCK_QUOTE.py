import pandas_datareader.data as web
from API_KEYS import ALPHAVANTAGE_API_KEY

stock = ["AAPL", "MSFT", "GOOG", "AMZN", "FB"]

def get_quote(stock):
    print('Currently pulling: ', stock)
    stock_quote = web.get_quote_av( stock, api_key=('ALPHAVANTAGE_API_KEY'))
    return stock_quote

print(get_quote(stock))