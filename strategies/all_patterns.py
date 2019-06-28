import pandas as pd

df = pd.read_csv('data/btc_hourly_c_2019.csv')

df['+'] = df['close'] > df['open']
df['-'] = df['open'] < df['close']

df['body'] = abs(df['open'] - df['close'])
df['wick'] = df['high'] - df['body_max']
df['tail'] = df['body_min'] - df['low']

df['body_max'] = list(map(max, df[['open', 'close']].values))
df['body_min'] = list(map(min, df[['open', 'close']].values))

df['doji'] = df['body'] < 0.1 * (df['wick'] + df['tail'])

# TODO: better param?
df['hammer'] = df['tail'] > 3 * df['body']
df['inverted_hammer'] = df['wick'] > 3 * df['body']
# -----------------------------------------------------------------------
# Functions
def engulfed(smaller, larger):
    return (smaller['body'] < larger['body'] \
    & smaller['body_min'] > larger['body_min'] \
    & smaller['body_max'] < larger['body_max'])

def gap(up_down, first, second):
    if up_down == 'up':
        return first['body_max'] < second['body_min']
    else:  # up_down == 'down'
        return first['body_min'] > second['body_max']
# -----------------------------------------------------------------------
bull = pd.DataFrame()
bear = pd.DataFrame()

c_1 = df[2:]
c_2 = df.shift(1)[2:]
c_3 = df.shift(2)[2:]
# -----------------------------------------------------------------------

bull['engulfed'] = engulfed(c_1, c_2) & c_1['-'] & c_2['+']
bear['engulfed'] = engulfed(c_1, c_2) & c_1['+'] & c_2['-']

harami = engulfed(c_2, c_1) & c1['open'] < c2['low'] & c1['close'] > c2['high']
bull['harami'] = harami & c_1['-'] & c_2['+']
bear['harami'] = harami & c_1['+'] & c_2['-']

bull['kicker'] = gap('up', c_1, c_2) & c_1['-'] & c_2['+']
bear['kicker'] = gap('down', c_1, c_2) & c_1['+'] & c_2['-']

# Bear-specfic candles
bear['hanging_man'] = c_1['+'] & c_2['-'] & c_1['gap_up'] & c_1['hammer']
bear['shooting_star'] = c_1['+'] & c_2['-'] & c_1['gap_up'] & c_2['inverted_hammer']
