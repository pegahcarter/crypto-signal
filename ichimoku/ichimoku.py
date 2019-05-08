# Main script for ichimoku cloud
from ichimoku.functions import make_lines, make_spans, extend_df
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
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

# Span A > Span B == green cloud
# Span A < Span B == red cloud
df = df[1500:]
price = df['price']
tenkan = df['tenkan']
kijun = df['kijun']
senkou_a = df['senkou_a']
senkou_b = df['senkou_b']
x = df['date']

fig, ax = plt.subplots(figsize=(20, 20))
plt.plot(x, senkou_a, color='green', linewidth=0.5)
plt.plot(x, senkou_b, color='red', linewidth=0.5)
plt.plot(x, tenkan, color='blue')
plt.plot(x, kijun, color='maroon')
plt.plot(x, price, color='black', linewidth=1)

ax.set(xlabel='Date', ylabel='BTC price ($)', title='2019 BTC/USD price (Bitmex)')
plt.rc('axes', labelsize=20)
plt.rc('font', size=16)
ax.xaxis.set_major_locator(mdates.WeekdayLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
plt.xticks(rotation=45)
plt.legend()
plt.fill_between(
    x, senkou_a, senkou_b,
    where=senkou_a >= senkou_b,
    facecolor='limegreen',
    interpolate=True
)
plt.fill_between(
    x, senkou_a, senkou_b,
    where=senkou_a <= senkou_b,
    facecolor='salmon',
    interpolate=True
)

plt.show()
