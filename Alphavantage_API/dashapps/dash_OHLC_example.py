import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
from API_KEYS import ALPHAVANTAGE_API_KEY

API_KEY = 'ALPHAVANTAGE_API_KEY'

symbol = 'AAPL'
##### TIME_SERIES_DAILY #####

daily = 'TIME_SERIES_DAILY'
datatype = 'csv'  # ['json', 'csv']

DAILY_OHLC = ('https://www.alphavantage.co/query?') + ('function=' + daily) + ('&symbol=' + symbol) + ('&apikey=' + API_KEY) + ('&datatype=' + datatype)
df = pd.read_csv(DAILY_OHLC)
# print(df)


app.layout = html.Div(
    dcc.Graph(
        id='graph', 
        figure={
            'data': [
                {
                    'x': df.timestamp, 
                    'open': df.open, 
                    'high': df.high, 
                    'low': df.low, 
                    'close': df.close, 
                    'type': 'ohlc', 
                    'name': 'chart'},
            ],
            'layout': {
                'title': {'text': symbol},
                'yaxis': {
                    'title': {'text': 'Price (USD)'},
                },
                "plot_bgcolor": "rgb(234,234,242)", 
                "paper_bgcolor": "white", 
            }
        }              
    )
)


if __name__ == '__main__':
    app.run_server(debug=True)