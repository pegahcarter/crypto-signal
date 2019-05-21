import pandas as pd

# NOTE: does not require shifted candles
df = pd.read_csv('data/btc_hourly_candle_2019.csv')

df.head()

candle_vol = (df['high'] - df['low']) / df['low']
candle_body_vol = abs(df['open'] - df['close']) / df['close']

candle_std = candle_vol.std()
candle_body_std = candle_body_vol.std()

# Let's say candle body is < 1/4 sdevs and entire candle > 1.5 sdev
large_candle = candle_vol >= candle_std * 1.5
small_candle_body = candle_body_vol < candle_body_std * 0.25

results = large_candle & small_candle_body
# 22 results when body < 1/4 and candle > 1.5 (standard deviations)
len(results.where(results == True).dropna())
