import requests
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime

# API endpoint for exchange rate data
api_url = 'https://api.exchangerate-api.com/v4/latest/usd'

# Initialize lists to store data
timestamps = []
exchange_rates = []

# Function to fetch exchange rate data
def fetch_exchange_rate():
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data['rates']['COP']
    else:
        print('Failed to fetch exchange rate data.')
        return None

# Function to update the graph with the current exchange rate
def update_graph(num):
    timestamp = datetime.now()
    exchange_rate = fetch_exchange_rate()

    if exchange_rate is not None:
        timestamps.append(timestamp)
        exchange_rates.append(exchange_rate)

        plt.clf()
        plt.plot(timestamps, exchange_rates, label='USD to COP')
        plt.xlabel('Time')
        plt.ylabel('Exchange Rate')
        plt.title('USD to COP Exchange Rate Over Time')
        plt.legend()

# Create a figure and axis for the graph
fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, update_graph, interval=30000, cache_frame_data=False)  # Update every minute

# Display the graph
plt.show()