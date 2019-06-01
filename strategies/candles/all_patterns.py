import pandas as pd

df = pd.read_csv('data/btc_hourly_c_2019.csv')

candle_bodies = df[['open', 'close']].values
df['body_max'] = list(map(max, candle_bodies))
df['body_min'] = list(map(min, candle_bodies))

df['body_length'] = abs(df['open'] - df['close'])
df['wick_length'] = df['high'] - df['body_max']
df['tail_length'] = df['body_min'] - df['low']

# -----------------------------------------------------------------------
# Single candle calculations

df['+'] = df['close'] > df['open']
df['-'] = df['open'] < df['close']

df['hammer'] = df['+'] df['tail_length'] > df['body_length']*2 & df['wick_length'] < df['body_length']
df['inverted_hammer'] = df['-'] & df['wick_length'] > df['body_length']*2 & df['tail_length'] < df['body_length']

df['bullish_hammer'] = df['+'] & df['hammer']
df['bearish_inverted_hammer'] = df['-'] & df['inverted_hammer']

# Determine if there's a space between the last close/next open
df['gap_up'] = df['body_min'].shift(1) > df['body_max']
df['gap_down'] = df['body_max'].shift(1) < df['body_min']

# -----------------------------------------------------------------------
# Functions
def engulfed(smaller, larger):
    return smaller['body_length'] < larger['body_length']



# -----------------------------------------------------------------------

c_1 = df[2:]
c_2 = df.shift(1)[2:]
c_3 = df.shift(2)[2:]

candle = c_1[2:]

bull = pd.DataFrame()
bear = pd.DataFrame()

# -----------------------------------------------------------------------
# Bear & Bull candles

bull['engulfed'] = engulfed(c_1, c_2) & c_1['-'] & c_2['+']
bear['engulfed'] = engulfed(c_1, c_2) & c_1['+'] & c_2['-']

bull['harami'] = engulfed(c_2, c_1) & c_1['-'] & c_2['+']
bear['harami'] = engulfed(c_2, c_1) & c_1['+'] & c_2['-']

bull['kicker'] = c_1['-'] & c_2['+'] & c_1['gap_up']
bear['kicker'] = c_1['+'] & c_2['-'] & c_1['gap_down']

bull['tweezer'] = c_1['-'] & c_2['+']
bear['tweezer'] = c_1['+'] & c_2['-']


# Bear-specfic candles
bear['hanging_man'] = c_1['+'] & c_2['-'] & c_1['gap_up'] & c_1['hammer']
bear['shooting_star'] = c_1['+'] & c_2['-'] & c_1['gap_up'] & c_2['inverted_hammer']


# Bull-specfic candles
