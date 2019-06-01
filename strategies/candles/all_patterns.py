# File that references candlestick functions from https://github.com/cm45t3r/candlestick/blob/master/src/candlestick.js
import pandas as pd

candle = pd.read_csv('data/btc_hourly_candle_2019.csv')

candle_bodies = candle[['open', 'close']].values
candle['body_max'] = list(map(max, candle_bodies))
candle['body_min'] = list(map(min, candle_bodies))

candle['body_length'] = abs(candle['open'] - candle['close'])
candle['wick_length'] = candle['high'] - candle['body_max']
candle['tail_length'] = candle['body_min'] - candle['low']

# -----------------------------------------------------------------------
# Single candle calculations

candle['bullish'] = candle['close'] > candle['open']
candle['bearish'] = candle['open'] < candle['close']

candle['hammer'] = candle['bullish'] candle['tail_length'] > candle['body_length']*2 & candle['wick_length'] < candle['body_length']
candle['inverted_hammer'] = candle['bearish'] & candle['wick_length'] > candle['body_length']*2 & candle['tail_length'] < candle['body_length']

candle['bullish_hammer'] = candle['bullish'] & candle['hammer']
candle['bearish_inverted_hammer'] = candle['bearish'] & candle['inverted_hammer']

# True if candle is larger than previous candle
candle['engulfing'] = candle['body_length'].shift(1) > candle['body_length']

# Determine if there's a space between the last close/next open
candle['gap_up'] = candle['body_min'].shift(1) > candle['body_max']
candle['gap_down'] = candle['body_max'].shift(1) < candle['body_min']

# -----------------------------------------------------------------------

candle_2 = candle.shift(1)[2:]
candle_3 = candle.shift(2)[2:]
candle = candle[2:]

bull = pd.DataFrame()
bear = pd.DataFrame()

# -----------------------------------------------------------------------

# Bear & Bull candles
bull['engulfed'] = candle['bearish'] & candle_2['bullish'] & candle['engulfed']
bear['engulfed'] = candle['bullish'] & candle_2['bearish'] & candle['engulfed']

bull['harami'] = candle['bearish'] & candle_2['bullish'] & candle['engulfed']
bear['harami'] = candle['bullish'] & candle_2['bearish'] & candle['engulfed']

bull['kicker'] = candle['bearish'] & candle_2['bullish'] & candle['gap_up']
bear['kicker'] = candle['bullish'] & candle_2['bearish'] & candle['gap_down']

bull['tweezer'] = candle['bearish'] & candle_2['bullish']
bear['tweezer'] = candle['bullish'] & candle_2['bearish']


# Bear-specfic candles
bear['hanging_man'] = candle['bullish'] & candle_2['bearish'] & candle['gap_up'] & candle['hammer']
bear['shooting_star'] = candle['bullish'] & candle_2['bearish'] & candle['gap_up'] & candle_2['inverted_hammer']


# Bull-specfic candles
