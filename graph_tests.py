import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import pandas as pd

filename = 'data/btc_hourly_candle_2019.csv'

df = pd.read_csv(filename)[:50]
candles = go.Candlestick(x = df['date'], open=df['open'], high=df['high'], low=df['low'], close=df['close'])

data = [candles]


iplot(data)
