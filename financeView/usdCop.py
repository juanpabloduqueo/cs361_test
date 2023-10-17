import requests
from  datetime import datetime
 
 # API key for the Twelve Data API
api_key = '81be3324d49a474aaa171305f06c9691'

# Exchange rate symbol for USD to COP
symbol = 'USD/COP'

# API URL for the exchange rate symbol
api_url = f'https://api.twelvedata.com/exchange_rate?symbol={symbol}&apikey={api_key}'



data = requests.get(api_url).json()

time = datetime.fromtimestamp(data['timestamp']).strftime("%Y-%m-%d %H:%M:%S")

print(data)

print(f'Hi Juan Pablo, the current exchange rate of {symbol} is {data["rate"]}. The current date and time are {time}')

