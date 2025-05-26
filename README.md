# Stock Strategy Simulator 📈

This project simulates a stock trading strategy using SMA (Simple Moving Average) crossovers.

It downloads historical TSLA stock data, calculates SMA20 and SMA50, identifies buy/sell signals, runs a backtest, and visualizes both the signals and the capital growth.

---

## 📦 Features

✅ Download TSLA historical data using `yfinance`  
✅ Calculate SMA indicators and identify golden/death cross signals  
✅ Run backtest and report total return, win rate, max gain/loss  
✅ Plot buy/sell points on interactive price chart  
✅ Plot capital growth (equity curve) over trades

---

## 🔧 Requirements

- Python 3.8+
- `pandas`
- `plotly`
- `yfinance`

Install them with:

```bash
pip install -r requirements.txt
```

## 📂 File Structure

- `main.py`: Entry point, orchestrates the workflow  
- `strategy.py`: Defines the SMA calculation and buy/sell signal logic  
- `backtest.py`: Runs backtesting and performance summarization  
- `plot.py`: Plots price charts and capital growth charts

## 🌟 Future Improvements

- Add parameter tuning (adjust SMA window)
- Support more strategies (e.g., RSI, MACD)
- Export reports to CSV/Excel/PDF
- Build Streamlit web interface
