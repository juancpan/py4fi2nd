import requests
import pandas as pd

# Alpha Vantage API parameters
base_url = 'https://www.alphavantage.co/query'
function = 'TIME_SERIES_DAILY'
stock = 'AAPL'  # Example stock symbol
outputsize = 'full'
api_key = 'MEF6L2RR4BYQBWG5'  # Replace with your actual Alpha Vantage API key
datatype = 'csv'
filename = f'{stock}_daily.csv'

# Construct the API URL
url = f'{base_url}?function={function}&symbol={stock}&outputsize={outputsize}&apikey={api_key}&datatype={datatype}'

try:
    # 1. Successfully fetched the data using requests package.
    print(f"Fetching data from: {url}")
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes

    # Check if the response content is not empty
    if not response.content:
        print("Error: Received empty content from the API.")
    else:
        # 2. Download and save the CSV file to local.
        print(f"Saving data to: {filename}")
        with open(filename, 'wb') as f:
            f.write(response.content)

        # 3. Read and load the file as a pandas data frame structure.
        print(f"Loading data into pandas DataFrame from: {filename}")
        try:
            df = pd.read_csv(filename)

            # 4. Parse the data and print out the first and the last few lines of the data frame.
            print("\n--- First 5 rows of the DataFrame ---")
            print(df.head())

            print("\n--- Last 5 rows of the DataFrame ---")
            print(df.tail())

        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")
        except pd.errors.EmptyDataError:
            print(f"Error: The CSV file '{filename}' is empty.")
        except Exception as e:
            print(f"An error occurred while reading the CSV file: {e}")

except requests.exceptions.RequestException as e:
    print(f"Error fetching data from Alpha Vantage API: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")