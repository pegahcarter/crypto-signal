import pandas as pd
import numpy as np


window = 1
param = {
    'columns_to_keep': ['date', 'open', 'close'],
    'functions_to_apply': [
        'maxmin', 'color_candle'
    ]
}

def engulfing(df0, df1):



candle1 = df[period:]
candle2 = df.shift(period)[period:]
df = df[period:]

# Compare candles to only take occurences of the next candle being the opposite color
df['switch color'] = candle2['green'] != candle1['green']

# candle is larger than previous candle
df['> previous'] = abs(candle1['open'] - candle1['close']) < abs(candle2['open'] - candle2['close'])

# open/close of candle > open/close of previous candle
engulf_upper = candle1['max'] <= candle2['max']
engulf_lower = candle1['min'] >= candle2['min']
df['engulfing'] = engulf_upper & engulf_lower
# Only use criteria where candle 2 size is > 2x

conditions = df['switch color'] & df['> previous'] & df['engulfing']
engulfings = conditions.where(conditions == True).dropna()
