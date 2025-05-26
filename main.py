import yfinance as yf
from strategy import add_sma_signals
from backtest import run_backtest, summarize_performance
from plot import plot_signals, plot_equity_curve

#Download data
ticker = "TSLA"
df = yf.download(ticker, start="2021-01-01", end="2025-5-20", auto_adjust=False)
df.reset_index(inplace=True)
df.columns = [col[0] if isinstance(col, tuple) else col for col in df.columns]

#Apply strategy
df = add_sma_signals(df)

#Plot signals
plot_signals(df)

#Run backtest
trade_df = run_backtest(df)
trade_df = summarize_performance(trade_df)

#Plot equity curve
plot_equity_curve(trade_df)