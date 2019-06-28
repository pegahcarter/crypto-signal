import pandas as pd

param = {
    'columns_to_keep': ['date', 'open', 'close'],
    'functions_to_apply': ['maxmin', 'color_candle']
}

def engulfing(df):
    df_shifted = df.shift(1)[1:]
    df = df[1:]
    # Compare candles to only take occurences of the next candle being the opposite color
    switch_color = df_shifted['green_candle'] != df['green_candle']

    # candle is larger than previous candle
    gt_previous = abs(df['open'] - df['close']) < abs(df_shifted['open'] - df_shifted['close'])

    # open/close of candle >= open/close of previous candle
    engulf_upper = df['max'] <= df_shifted['max']
    engulf_lower = df['min'] >= df_shifted['min']
    engulfed = engulf_upper & engulf_lower

    # TODO: Only use criteria where candle 2 size is > 2x
    results = switch_color & gt_previous & engulfed
    return results
