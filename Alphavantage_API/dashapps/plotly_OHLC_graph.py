from datetime import datetime
import urllib.request
import pandas as pd
import plotly.graph_objects as go

from API_KEYS import ALPHAVANTAGE_API_KEY

API_KEY = 'ALPHAVANTAGE_API_KEY'

symbol = 'AAPL'
datatype = 'csv'  # ['json', 'csv']
daily = 'TIME_SERIES_DAILY'

##### TIME_SERIES_DAILY #####
DAILY_OHLC = ('https://www.alphavantage.co/query?') + ('function=' + daily) + \
    ('&symbol=' + symbol) + ('&apikey=' + API_KEY) + ('&datatype=' + datatype)

df = pd.read_csv(DAILY_OHLC)
print(df)

fig = go.Figure(data=[go.Candlestick(x=df['timestamp'],
                                     open=df['open'],
                                     high=df['high'],
                                     low=df['low'],
                                     close=df['close'])])

fig.show()
