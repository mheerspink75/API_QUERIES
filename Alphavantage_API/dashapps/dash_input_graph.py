import pandas as pd
import urllib.request
from pandas_datareader import data
import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from API_KEYS import ALPHAVANTAGE_API_KEY

API_KEY = 'ALPHAVANTAGE_API_KEY'


#############################
##### symbol = 'AAPL' #######
##### TIME_SERIES_DAILY #####
#############################


app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.Div(children='''
        Symbol to graph:
    '''),
    dcc.Input(id='input', value='', type='text'),
    html.Div(id='output-graph'),
])


@app.callback(
    Output(
        component_id='output-graph',
        component_property='children'
    ),
    [
        Input(
            component_id='input',
            component_property='value'
        )]
     )

def update_value(input_data):
    daily = 'TIME_SERIES_DAILY'
    datatype = 'csv'  # ['json', 'csv']
    DAILY_OHLC = ('https://www.alphavantage.co/query?') + ('function=' + daily) + \
        ('&symbol=' + input_data) + \
        ('&apikey=' + API_KEY) + ('&datatype=' + datatype)
    df = pd.read_csv(DAILY_OHLC)

    return dcc.Graph(
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
                'title': 'CHART'
            }
        })


if __name__ == '__main__':
    app.run_server(debug=True)
