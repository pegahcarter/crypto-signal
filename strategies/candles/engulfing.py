import pandas as pd
import numpy as np


param = {
    'columns_to_keep': ['date', 'open', 'close'],
    'functions_to_apply': ['maxmin', 'color_candle']
}

def engulfing(df0, df1):
    # Compare candles to only take occurences of the next candle being the opposite color
    switch_color = df1['green'] != df0['green']

    # candle is larger than previous candle
    gt_previous = abs(df0['open'] - df0['close']) < abs(df1['open'] - df1['close'])

    # open/close of candle >= open/close of previous candle
    engulf_upper = df0['max'] <= df1['max']
    engulf_lower = df0['min'] >= df1['min']
    engulfed = engulf_upper & engulf_lower

    # TODO: Only use criteria where candle 2 size is > 2x
    return switch_color & gt_previous & engulfed
