import pandas as pd
import numpy as np

period = 1

df = pd.read_csv('data/btc_hourly_candle_2019.csv')

# True == green candle
df['green'] = df['close'] > df['open']
df['max'] = map(max, df[['open', 'close']].values)
df['min'] = map(min, df[['open', 'close']].values)

candle1 = df[period:]
candle2 = df.shift(period)[period:]
df = df[period:]

# Compare candles to only take occurences of the next candle being the opposite color
df['switch color'] = candle1['green'] != candle2['green']

# candle is larger than previous candle
df['> previous'] = abs(candle1['open'] - candle1['close']) < abs(candle2['open'] - candle2['close'])

# open/close of candle > open/close of previous candle
engulf_upper = candle1['max'] <= candle2['max']
engulf_lower = candle1['min'] >= candle2['min']
df['engulfing'] = engulf_upper & engulf_lower

df.head()

df = df[['date', 'max', 'min', 'switch color', '> previous']]
for i, row in df.loc[df['switch color'] == True][:20].iterrows():
    pass
