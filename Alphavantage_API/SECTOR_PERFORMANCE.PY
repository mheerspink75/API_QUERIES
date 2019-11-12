import pandas_datareader.data as web
from API_KEYS import ALPHAVANTAGE_API_KEY

API_KEY = 'ALPHAVANTAGE_API_KEY'

def get_sector_performance():
    return web.get_sector_performance_av(api_key=API_KEY)

# print(get_sector_performance())