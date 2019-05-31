# File that references candlestick functions from https://github.com/cm45t3r/candlestick/blob/master/src/candlestick.js
import pandas as pd

bullish_patterns = ['engulfing', 'harami', 'kicker', 'hammer', 'inverted_hammer']
bearish_patterns = ['engulfing', 'harami', 'kicker', 'hanging_man', 'shooting_star']

df = pd.read_csv('data/btc_hourly_candle_2019.csv')

candle_bodies = df[['open', 'close']].values
df['body_max'] = list(map(max, candle_bodies))
df['body_min'] = list(map(min, candle_bodies))

df['body_length'] = abs(df['open'] - df['close'])
df['wick_length'] = df['high'] - df['body_max']
df['tail_length'] = df['body_min'] - df['low']

df['bullish'] = df['close'] > df['open']
df['bearish'] = df['open'] < df['close']

df['hammer'] = df['tail_length'] > df['body_length']*2 & df['wick_length'] < df['body_length']
df['inverted_hammer'] = df['wick_length'] > df['body_length']*2 & df['tail_length'] < df['body_length']
