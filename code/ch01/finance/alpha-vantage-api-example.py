'''
Alpha Vantage: A working quick-start example for Alpha Vantage API

This example demonstrates how to use the Alpha Vantage API to fetch daily stock data for a specific ticker symbol (IBM) over a specified date range.

It uses the requests library to make an API call and fetch the data in JSON format. The example also includes a note about the API key, which is required for authentication.

Must knows about Alpha Vantage API:

Are there usage/frequency limits for the API service?

We are pleased to provide free stock API service covering the majority of our datasets for up to 25 requests per day. If you would like to target a larger API call volume, please visit premium membership.

Alpha Vantage categorize the API calls into 8 categories. For real-time ticker data, you can use the TIME_SERIES_INTRADAY function. For daily historical data, you can use the TIME_SERIES_DAILY function. For weekly or monthly data, you can use the TIME_SERIES_WEEKLY or TIME_SERIES_MONTHLY functions, respectively.

For historical data for analytics purposes, Alpha Vantage has an ad-hoc category called Advanced Analytics (Fixed Window). Refer to: https://www.alphavantage.co/documentation/#analytics-fixed-window

Alpha Vantage's Daily Time Series API returns adjusted prices. For raw ticker data, need to subscribe to their premium service and use the function TIME_SERIES_DAILY_ADJUSTED, read at: https://www.alphavantage.co/documentation/#dailyadj

Website: https://www.alphavantage.co/
Docs: https://www.alphavantage.co/documentation/
Pricing: https://www.alphavantage.co/premium/
'''
import requests
import time
from datetime import datetime

# Time Series Data (Tick Data is not directly supported, using 1min instead)
ticker =    "AAPL,\
            MCD"
api_keys = [
    "MEF6L2RR4BYQBWG5",
    "N30Y6DJI6GL196DF",
    "OL92YFVK4DWQGRVZ",
    "APM1BXJ931SWR6X5",
    "GGGE9JVWZVHBDVKF",
    "3R2B7I8JMB3UCMWB"
]
start_date_str = "2019-01-01"
end_date_str = "2019-10-18"
start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
base_url = 'https://www.alphavantage.co/query'
function = 'TIME_SERIES_DAILY'

for stock in ticker:
    fetched_data = None
    for api_key in api_keys:
        url = f'{base_url}?function={function}&symbol={stock}&outputsize=full&apikey={api_key}&datatype=csv'
        print(f"Attempting to fetch data for {stock} with API key: {api_key}")
        try:
            r = requests.get(url)
            r.raise_for_status()
            data = r.json()
            if 'Time Series (Daily)' in data:
                fetched_data = data['Time Series (Daily)']
                print(f"Successfully fetched data for {stock} with API key: {api_key}")
                break
            elif 'Note' in data:
                print(f"API Note: {data['Note']}")
                if "Our standard API call frequency per API key is 25 requests per day" in data['Note'] or \
                   "Thank you for using Alpha Vantage! Our standard API call frequency per API key is 5 calls per minute" in data['Note']:
                    time.sleep(15)  # Wait before trying the next key
                else:
                    print("Another API error occurred.")
            else:
                print(f"Unexpected response: {data}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    if fetched_data:
        print(f"\n--- Daily Time Series Data for {stock} ({start_date_str} to {end_date_str}) ---")
        for date_str, values in fetched_data.items():
            current_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            if start_date <= current_date <= end_date:
                print(f"Date: {date_str}")
                print(f"  Open: {values['1. open']}")
                print(f"  High: {values['2. high']}")
                print(f"  Low: {values['3. low']}")
                print(f"  Close: {values['4. close']}")
                print(f"  Volume: {values['5. volume']}")
                print("-" * 20)
    else:
        print(f"Failed to fetch data for {stock} after trying all API keys.")