# Main script for ichimoku cloud
from ichimoku.functions import make_lines, make_spans, extend_df, chart
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

chart(df[1500:])
