import pandas as pd

def hammer(df):

    # Find midpoint of high/low
    midpoint = (df['high'] + df['low']) / 2

    # Only take top/bottom 25%
    top_25 = (df['high'] - midpoint) / 2
    bottom_25 = (midpoint - df['low']) / 2

    results = (df['open'] > top_25 and df['close'] > top_25 \
               or \
               df['open'] < bottom_25 and df['close'] < bottom_25)
