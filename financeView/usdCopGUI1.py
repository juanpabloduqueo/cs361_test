import tkinter as tk
from tkinter import messagebox
import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import pandas as pd

# API endpoint for exchange rate data
api_url = 'https://api.exchangerate-api.com/v4/latest/usd'

# API endpoint for historical exchange rate data
historical_api_url = 'https://api.exchangeratesapi.io/history'

# Function to fetch exchange rate data
def fetch_exchange_rate():
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data['rates']['COP']
    else:
        messagebox.showerror('Error', 'Failed to fetch exchange rate data.')
        return None

# Function to plot last month's daily closing exchange rate
def plot_last_month_exchange_rate():
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)

    params = {
        'start_at': start_date.strftime('%Y-%m-%d'),
        'end_at': end_date.strftime('%Y-%m-%d'),
        'base': 'USD',
        'symbols': 'COP'
    }

    response = requests.get(historical_api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        dates = [datetime.strptime(date, "%Y-%m-%d") for date in data['rates'].keys()]
        closing_rates = [data['rates'][date]['COP'] for date in data['rates']]

        # Create a DataFrame to plot the data
        df = pd.DataFrame({'Date': dates, 'Closing Rate': closing_rates})
        
        # Plot the data
        plt.plot(df['Date'], df['Closing Rate'], marker='o')
        plt.xlabel('Date')
        plt.ylabel('Closing Rate (USD to COP)')
        plt.title('Last Month\'s Daily Closing Exchange Rate (USD to COP)')
        plt.grid(True)
        plt.show()
    else:
        messagebox.showerror('Error', 'Failed to fetch historical exchange rate data.')

# Function to update the real-time exchange rate label
def update_exchange_rate():
    exchange_rate = fetch_exchange_rate()
    if exchange_rate is not None:
        exchange_rate_label.config(text=f'Current USD to COP Exchange Rate: {exchange_rate:.2f}')
    else:
        exchange_rate_label.config(text='Unable to fetch exchange rate.')

# Create the main GUI window
root = tk.Tk()
root.title('USD to COP Exchange Rate Viewer')

# Create labels to display exchange rate and historical data
exchange_rate_label = tk.Label(root, text='', font=('Arial', 14))
exchange_rate_label.pack(pady=10)

# Create a button to plot last month's daily closing exchange rate
plot_button = tk.Button(root, text='Plot Last Month Exchange Rate', command=plot_last_month_exchange_rate, font=('Arial', 12))
plot_button.pack(pady=10)

# Create a button to update the real-time exchange rate
update_button = tk.Button(root, text='Update Exchange Rate', command=update_exchange_rate, font=('Arial', 12))
update_button.pack(pady=10)

# Run the main event loop
root.mainloop()
