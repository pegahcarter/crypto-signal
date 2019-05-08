# Main script for ichimoku cloud
from ichimoku.functions import make_lines, make_spans, extend_df, chart, find_intersections
import pandas as pd
%matplotlib inline

pd.plotting.register_matplotlib_converters()

tenkan_period = 20
kijun_period = 60
senkou_b_period = 120
displacement = 30

df = pd.read_csv('data/btc_hourly_candle_2019.csv')

extend_df(df, displacement)
df['price'] = df['close'].shift(1)

make_lines(df, tenkan=tenkan_period, kijun=kijun_period)
make_spans(df, displacement=displacement, senkou_b_period=senkou_b_period)

df = df[1500:].reset_index(drop=True)
intersections = find_intersections(df)
chart(df, intersections)
