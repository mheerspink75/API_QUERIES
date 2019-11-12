import pandas_datareader.data as web
from API_KEYS import ALPHAVANTAGE_API_KEY

stock = ["AAPL", "MSFT", "GOOG", "AMZN", "FB"]

pd = web.get_quote_av(stock, api_key=('ALPHAVANTAGE_API_KEY')).reset_index()
print(pd)
