import pandas as pd

'''
To-do
- Calculate % logic for how many results should fit candle/candle body
- What additional conditions are we looking for to utilize doji?
- Backtest for optimal doji (after we include conditional logic)
'''

def doji(df):

    candle_vol = (df['high'] - df['low']) / df['low']
    candle_body_vol = abs(df['open'] - df['close']) / df['close']

    candle_std = candle_vol.std()
    candle_body_std = candle_body_vol.std()

    # 951 results
    large_candle = candle_vol >= candle_std * .75
    # len(candle_vol.where(candle_vol > candle_std * .75).dropna())

    # 489 results
    small_candle_body = candle_body_vol < candle_body_std * 0.1
    # len(candle_body_vol.where(candle_body_vol < candle_body_std * 0.1).dropna())

    # Combining the two conditions (39 results)
    results = large_candle & small_candle_body
    # len(results.where(results == True).dropna())

    return results
