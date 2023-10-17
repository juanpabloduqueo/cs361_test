import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def plot_exchange_rate(ticker, start_date, end_date):
    # Fetch historical data for the given ticker symbol and date range
    data = yf.download(ticker, start=start_date, end=end_date)
    
    # Extract the 'Close' prices
    close_prices = data['Close']
    
    # Plot the daily closing exchange rate
    plt.figure(figsize=(12, 6))
    plt.plot(close_prices, label=f'{ticker} Closing Exchange Rate')
    plt.xlabel('Date')
    plt.ylabel('Exchange Rate')
    plt.title(f'Daily Closing Exchange Rate of {ticker} for the Last 1 Month')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Ticker symbol for USD to COP exchange rate
    usd_cop_ticker = 'USDCOP=X'

    # Calculate start and end dates for the last 1 month
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)

    # Plot the exchange rate for the last 1 month
    plot_exchange_rate(usd_cop_ticker, start_date, end_date)
