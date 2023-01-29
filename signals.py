import requests
import json
import random
import datetime
import time
from datetime import timedelta
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def get_signals(stock_symbol):
    # Get the stock data for the past year
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={stock_symbol}&apikey=<YOUR_API_KEY>'
    res = requests.get(url)
    data = json.loads(res.text)

    # Prepare the data for analysis
    df = pd.DataFrame(data['Time Series (Daily)']).T
    df.reset_index(inplace=True)
    df.rename(columns={'index':'date'}, inplace=True)
    df.date = pd.to_datetime(df.date)
    df.set_index('date', inplace=True)
    df = df.astype(float)

    # Calculate the moving averages
    df['sma_50'] = df['4. close'].rolling(window=50).mean()
    df['sma_200'] = df['4. close'].rolling(window=200).mean()

    # Generate the trading signals
    signals = []
    for i in range(len(df)):
        if df['sma_50'][i] > df['sma_200'][i]:
            signals.append('Buy')
        else:
            signals.append('Sell')

    # Add the signals to the dataframe
    df['signals'] = signals

    return df

