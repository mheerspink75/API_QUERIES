import dash
import dash_table
import pandas_datareader.data as web
from API_KEYS import ALPHAVANTAGE_API_KEY

API_KEY = 'ALPHAVANTAGE_API_KEY'
stock = ["AAPL", "MSFT", "GOOG", "AMZN", "FB"]

df = web.get_quote_av(stock, api_key=('ALPHAVANTAGE_API_KEY')).reset_index()

app = dash.Dash(__name__)

app.layout = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
)

if __name__ == '__main__':
    app.run_server(debug=True)
