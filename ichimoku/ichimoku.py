# Main script for ichimoku cloud
from bots.ichimoku.functions import make_lines, make_spans
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
%matplotlib inline
register_matplotlib_converters()


tenkan_period = 20
kijun_period = 60
senkou_b_period = 120
displacement = 30

df = pd.read_csv('data/historical_candles.csv')
df['date'] = [datetime.strptime(i, '%Y-%m-%d %H:%M:%S') for i in df['date']]
last_date = df['date'].at[len(df)-1]

dfEmpty = pd.DataFrame(
    {'date': [last_date + timedelta(hours=i+1) for i in range(displacement)]}
)

df = df.append(dfEmpty, ignore_index=True, sort=False)

make_lines(df, tenkan=tenkan_period, kijun=kijun_period)
make_spans(df, displacement=displacement, senkou_b_period=senkou_b_period)

df2 = df[8500:]

# Span A > Span B == green cloud
# Span A < Span B == red cloud
tenkan = df2['tenkan']
kijun = df2['kijun']
a = df2['senkou_a']
b = df2['senkou_b']
x = df2['date']

fig = plt.plot(x, a, x, b)
plt.fill_between(x, a, b, where=a >= b, facecolor='green', interpolate=True)
plt.fill_between(x, a, b, where=a <= b, facecolor='red', interpolate=True)

plt.plot(x, tenkan, color='yellow')
plt.plot(x, kijun, color='blue')
plt.show()
