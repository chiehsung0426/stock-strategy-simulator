import pandas as pd

def add_sma_signals(df, short_window=20, long_window=50):
    #Calulate SMA
    df['SMA20'] = df['Close'].rolling(window=20).mean()
    df['SMA50'] = df['Close'].rolling(window=50).mean()

    #Signal
    df['Buy_Signal'] = ((df['SMA20'].shift(1) < df['SMA50'].shift(1)) & (df['SMA20'] > df['SMA50']))
    df['Sell_Signal'] = ((df['SMA20'].shift(1) > df['SMA50'].shift(1)) & (df['SMA20'] < df['SMA50']))

    return df