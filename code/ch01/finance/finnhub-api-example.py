'''
Must knows about Finnhub API:

Docs: https://finnhub.io/docs/api/introduction
Dashboard: https://finnhub.io/dashboard
Pricing: https://finnhub.io/pricing
'''

import requests
import json
import finnhub

# Variables

# # Assign the API key to a variable
# api_key = "cvkl69hr01qtnb8tbj7gcvkl69hr01qtnb8tbj80"        # API identified as "token" in the Finnhub API documentation
# # Setup client
# finnhub_client = finnhub.Client(api_key=api_key)
ticker = "AAPL"                                             # Ticker symbol for Apple Inc.
# base_url = f"https://finnhub.io/api/v1/quote?symbol={ticker:s}&token={api_key:s}"       # API endpoint for stock profile

# import finnhub
finnhub_client = finnhub.Client(api_key="cvkl69hr01qtnb8tbj7gcvkl69hr01qtnb8tbj80")

print(finnhub_client.quote(f"{ticker:s}"))

current_price = finnhub_client.quote(f"{ticker:s}")["c"]       # Current price
high_price = finnhub_client.quote(f"{ticker:s}")["h"]         # High price
low_price = finnhub_client.quote(f"{ticker:s}")["l"]         # Low price
open_price = finnhub_client.quote(f"{ticker:s}")["o"]       # Open price
previous_close_price = finnhub_client.quote(f"{ticker:s}")["pc"]  # Previous close price
print(f"Ticker: {ticker:s}")
print(f"Current price: {current_price}")
print(f"High price: {high_price}")
print(f"Low price: {low_price}")
print(f"Open price: {open_price}")
print(f"Previous close price: {previous_close_price}")
