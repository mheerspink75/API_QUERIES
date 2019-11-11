import pandas_datareader.data as web
import urllib.request
from API_KEYS import ALPHAVANTAGE_API_KEY
from TIME_SERIES import get_intraday_time_series

API_KEY = 'ALPHAVANTAGE_API_KEY'

symbol = input('Enter a stock symbol: ')

##### QUOTE SEARCH #####
def get_quote():
    #print('Currently pulling: ', symbol)
    QUOTE_SEARCH = web.get_quote_av(symbol, api_key=(API_KEY))
    return QUOTE_SEARCH

#print(get_quote())

###### TIME_SERIES_INTRADAY ##############
##get_intraday_time_series(symbol)########
##print(get_intraday_time_series(symbol))#
##########################################
