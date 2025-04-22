'''
Must knows about EODHD API:
    1. You can start with “DEMO” API key to test the data for a few tickers only: AAPL.US, TSLA.US, VTI.US, AMZN.US, BTC-USD.CC and EUR-USD.CC. For these tickers, all of our types of data (APIs), including Real-Time Data, are available without limitations.
    2. Register for the free plan to receive your API key (limited to 20 API calls per day) with access to End-Of-Day Historical Stock Market Data API for any ticker, but within the past year only. Plus a List of tickers per Exchange is available.
    3. We recommend to explore our plans, starting from $19.99, to access the necessary type of data without limitations.
EODHD API Doc: https://eodhd.com/financial-apis/api-for-historical-data-and-volumes#Quick_Start

This simple script demonstrates how to use the EODHD API to fetch historical stock data for a specific ticker symbol (e.g., Apple Inc. - AAPL) within a specified date range. The script retrieves user information and prints the data in a readable format.

For more advanced usage, you can explore the EODHD API documentation to access various types of data, including real-time data, historical data, and more. The API provides a wide range of endpoints for different types of financial data, making it a versatile tool for developers and analysts.
'''
import requests
api_key = "67e95364ebf346.37486961"                                         # API key for EODHD
user_url = f'https://eodhd.com/api/user?api_token={api_key:s}&fmt=json'     # API endpoint for user information
user_data = requests.get(user_url).json()
print(user_data)

ticker = "AAPL.US"                                                          # Ticker symbol for Apple Inc.
base_url = f"https://eodhd.com/api/eod/"
fmt = f"json"
period = f"d"
order = f"a"
start_date = f"2024-01-01"
end_date = f"2024-10-01"
endpoint_url = f'{base_url:s}{ticker:s}?api_token={api_key:s}&fmt={fmt:s}&period={period:s}&order={order:s}&from={start_date:s}&to={end_date:s}'
response = requests.get(endpoint_url)
data = response.json()
print(data)
print(f"Ticker: {ticker:s}")
print(f"Start date: {start_date:s}")
print(f"End date: {end_date:s}")
# print(f"Data: {data}")
print(f"Data length: {len(data):<5,d} records.")
first_record = data[0]
print(f"First record: {first_record}")
last_record = data[-1]
print(f"Last record: {last_record}")
# Print the data
# for item in data:
#     print(f"Date: {item['date']}")
#     print(f"Open: {item['open']}")
#     print(f"High: {item['high']}")
#     print(f"Low: {item['low']}")
#     print(f"Close: {item['close']}")
#     print(f"Volume: {item['volume']}")
#     print()