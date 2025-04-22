'''
Must knows about FMP API:

Pricing: https://site.financialmodelingprep.com/developer/docs/pricing
Dashboard: https://site.financialmodelingprep.com/developer/docs/dashboard
Docs: https://site.financialmodelingprep.com/developer/docs
'''

import requests
import json

# Assign the API key to a variable
api_key = "FjQRZUlggeaIZiv0MOtrrfuRZIdVAGi8"
# Assign the stock ticker to a variable
ticker = "AAPL"

# Define url
url = f"https://financialmodelingprep.com/stable/search-symbol?query={ticker:s}&apikey={api_key:s}"

# Check url format
print(f"URL is: {url:s}")

# Fetch url
response = requests.get(url)

# Check URL Status
print(f"URL returned: {response.status_code:<5,d}.")

# Stores json as dict
data = response.json()

# Assign new values fetched
ticker = data[0]["symbol"]
name = data[0]["name"]
currency = data[0]["currency"]
exchange = data[0]["exchange"]

# Print the data
print(f"The ticker symbol is: {{ {ticker:s} }}.")
print(f"The name of the company is: {{ {name:s} }}.")
print(f"The currency is: {{ {currency:s} }}.")
print(f"The exchange is: {{ {exchange:s} }}.")