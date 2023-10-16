import requests

api_key = '81be3324d49a474aaa171305f06c9691'

symbol = 'USD/COP'

api_url = f'https://api.twelvedata.com/exchange_rate?symbol={symbol}&apikey={api_key}'

data = requests.get(api_url).json()

print(f'Hi Juan Pablo, the current exchange rate of {symbol} is {data["rate"]}')

