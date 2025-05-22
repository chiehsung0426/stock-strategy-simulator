import yfinance as yf
import plotly.graph_objects as go

#Download data
ticker = "TSLA"
df = yf.download(ticker, start="2021-01-01", end="2025-5-20")

df.reset_index(inplace=True)
df.columns = [col[0] if isinstance(col, tuple) else col for col in df.columns]

#Calulate SMA
df['SMA20'] = df['Close'].rolling(window=20).mean()
df['SMA50'] = df['Close'].rolling(window=50).mean()

#Signal
df['Buy_Signal'] = ((df['SMA20'].shift(1) < df['SMA50'].shift(1)) & (df['SMA20'] > df['SMA50']))
df['Sell_Signal'] = ((df['SMA20'].shift(1) > df['SMA50'].shift(1)) & (df['SMA20'] < df['SMA50']))


#Draw the figure
fig = go.Figure()

#Line Chart for Closing Price
fig.add_trace(go.Scatter(
    x=df['Date'],
    y=df['Close'],
    mode='lines',
    name='Closing Price',
    line=dict(color='blue')
))

#Buying Spot
fig.add_trace(go.Scatter(
    x=df[df['Buy_Signal']]['Date'],
    y=df[df['Buy_Signal']]['Close'],
    mode='markers',
    name='Buy Signal',
    marker=dict(symbol='circle', size = 10, color='green'),
    hovertemplate='Buy<br>Date: %{x|%Y-%m-%d}<br>Price: %{y:.2f}<extra></extra>'
))

#Selling Spot
fig.add_trace(go.Scatter(
    x=df[df['Sell_Signal']]['Date'],
    y=df[df['Sell_Signal']]['Close'],
    mode='markers',
    name='Sell Signal',
    marker=dict(symbol='x', size = 10, color='red'),
    hovertemplate='Sell<br>Date: %{x|%Y-%m-%d}<br>Price: %{y:.2f}<extra></extra>'
))

fig.update_layout(
    title="TSLA Stock Price with Buy/Sell Signals (SMA20 vs SMA50)",
    xaxis_title="Date",
    yaxis_title="Price (USD)",
    hovermode="x unified"
)

# Short-term SMA Line
fig.add_trace(go.Scatter(
    x=df['Date'],
    y=df['SMA20'],
    mode='lines',
    name='SMA20',
    line=dict(color='orange', dash='dash')
))

# Long-term SMA Line
fig.add_trace(go.Scatter(
    x=df['Date'],
    y=df['SMA50'],
    mode='lines',
    name='SMA50',
    line=dict(color='purple', dash='dot')
))

fig.show()
