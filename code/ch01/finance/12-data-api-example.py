'''
Must knows about 12 data API:   

Website: https://twelvedata.com/
Docs: https://twelvedata.com/docs
Dashboard: https://twelvedata.com/account
12data API Playground: https://twelvedata.com/account/api-playground
'''

import requests
from twelvedata import TDClient

params = {
    "ticker": "AAPL",
    "interval": "1day",
    "outputsize": 10,
    "timezone": "America/New_York",
    "country": "US",
    "exchange": "NASDAQ",
    "start_date": "2019-01-01",
    "end_date": "2019-10-30",
    "api_key": "d4522b10443143b08e2d38b44a582203"
}

# Initialize client - apikey parameter is requiered
td = TDClient(apikey=f"{params['api_key']:s}")

# Construct the necessary time series
ts = td.time_series(
    symbol=params["ticker"],
    interval=params["interval"],
    outputsize=params["outputsize"],
    timezone=params["timezone"],
    country=params["country"],
    exchange=params["exchange"],
    start_date=params["start_date"],
    end_date=params["end_date"]
    # format="json",
)

# Returns pandas.DataFrame
ts.as_pandas()

print(ts.as_pandas())