'''
YFinance: A working quick-start example for Yahoo Finance API
This example demonstrates how to use the Yahoo Finance API to fetch historical stock data for a specific ticker symbol (AAPL) over a specified date range.
It uses the yfinance library to download the data and pandas to manipulate it. The example also includes a note about the auto_adjust parameter, which determines whether to fetch adjusted close prices or raw close prices.

Must knows about Yahoo Finance API:

Website: https://finance.yahoo.com/
Docs: https://yfinance-python.org/
'''

import yfinance as yf
import pandas as pd
from bs4 import BeautifulSoup
import requests

# Time Series Data (Tick Data is not directly supported, using 1min instead)
ticker = "AAPL"
start_date = "2018-10-18"
end_date = "2019-10-18"

'''
Notes on auto_adjust:

Yfinance has a parameter called auto_adjust which is set to True by default.
It fetches adjusted close prices, which means it adjusts the historical prices for dividends and stock splits.
If you set auto_adjust to False, it will return the raw close prices without any adjustments.
This is useful if you want to analyze the raw data without any adjustments.
'''

data = yf.download(ticker, 
                   start=start_date, 
                   end=end_date, 
                   interval="1d", 
                   threads=8, 
                   proxy="http://127.0.0.1:10808", 
                   auto_adjust=False)

if data is not None and not data.empty:
    data.info()
    print(data.tail())
else:
    print("No data available for the specified period.")
