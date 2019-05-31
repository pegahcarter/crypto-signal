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

# -----------------------------------------------------------------------
# Single candle calculations

df['bullish'] = df['close'] > df['open']
df['bearish'] = df['open'] < df['close']

df['hammer'] = df['tail_length'] > df['body_length']*2 & df['wick_length'] < df['body_length']
df['inverted_hammer'] = df['wick_length'] > df['body_length']*2 & df['tail_length'] < df['body_length']

df['bullish_hammer'] = df['bullish'] & df['hammer']
df['bearish_inverted_hammer'] = df['bearish'] & df['inverted_hammer']

# True if candle is larger than previous candle
df['engulfing'] = df['body_length'].shift(1) > df['body_length']

# Determine if there's a space between the last close/next open
df['gap_up'] = df['body_max'] < df['body_min'].shift(1)
df['gap_down'] = df['body_min'] > df['body_max'].shift(1)

# -----------------------------------------------------------------------
# Double candle calculations
bull = pd.DataFrame()
bear = pd.DataFrame()

# Candles that can be either bull/bear
bull['engulfed'] = df['bearish'] & df['bullish'].shift(1) & df['engulfed']
bear['engulfed'] = df['bullish'] & df['bearish'].shift(1) & df['engulfed']

bull['harami'] = df['bearish'] & df['bullish'].shift(1) & df['engulfed']
bear['harami'] = df['bullish'] & df['bearish'].shift(1) & df['engulfed']

bull['kicker'] = df['bearish'] & df['bullish'].shift(1) & df['gap_up']
bear['kicker'] = df['bullish'] & df['bearish'].shift(1) & df['gap_down']

# Candles specific to bull/bear
bear['hanging_man'] = df['bullish'] & df['bearish'].shift(1) & df['gap_up'] & df['hammer']
bear['shooting_star'] = df['bullish'] & df['bearish'].shift(1) & df['gap_up'] & df['inverted_hammer'].shift(1)
