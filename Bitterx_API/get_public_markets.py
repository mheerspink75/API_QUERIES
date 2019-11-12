import urllib.request
import pandas as pd

get_public_markets = 'https://api.bittrex.com/api/v1.1/public/getmarkets'
                    
url = urllib.request.urlopen(get_public_markets)
df = pd.read_json(url)

print(df)