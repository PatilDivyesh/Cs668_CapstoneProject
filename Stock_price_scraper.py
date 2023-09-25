import requests
import csv
from datetime import datetime, timedelta

# Define API access key
api_access_key = ''  

# Defining  list of stock symbols 
stock_symbols = ['NVDA', 'TSLA', 'AMD', 'AAPL']

# Calculate the end date (today)
end_date = datetime.now().strftime('%Y-%m-%d')

# Define the start date (April 1st of the current year)
start_date = datetime(datetime.now().year, 1, 1).strftime('%Y-%m-%d')

# Initialize an empty list to store data from all requests
data_list = []

# Make 10 requests for each stock symbol
for symbol in stock_symbols:
    # Define parameters for the API request with the date range and specific symbol
    params = {
        'access_key': api_access_key,
        'symbols': symbol,  # Single stock symbol for each request
        'limit': 1000,  # Limit the number of data points per request
        'sort': 'desc',  # Sort data in descending order (most recent first)
        'date_from': start_date,
        'date_to': end_date
    }

    # Make the API request to fetch historical stock price data for the current symbol
    api_result = requests.get('http://api.marketstack.com/v1/eod', params=params)

    # Check if the request was successful
    if api_result.status_code == 200:
        api_response = api_result.json()
        
        # Append the data from the current request to the data_list
        for stock_data in api_response['data']:
            data_list.append([
                stock_data["date"],  # Date
                stock_data["symbol"],  # Add Symbol
                stock_data["high"], # Add high price
                stock_data["low"],  # Add low price
                stock_data["volume"]  # Add volume
            ])
    else:
        print(f'API request failed for symbol {symbol}. Check your API key and parameters.')

# Define the CSV file name
csv_file_name = 'stock_price_data_Jan_to_sept.csv'

# Write the data to a CSV file
with open(csv_file_name, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Date', 'Symbol', 'High', 'Low', 'Volume'])  # Write header row
    csv_writer.writerows(data_list)
         
    csv_writer.writerows(data_list)  # Write the stock price data

print(f'Data from April 1st to September 22nd has been saved to {csv_file_name}')
