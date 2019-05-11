import pandas as pd
import numpy as np


df = pd.read_csv('data/btc_hourly_candle_2019.csv')
df['Positive'] = df['close'] > df['open']

print(df['Positive'][:10])
print(df['Positive'].shift(1)[:10])


df.head()

df['test'] = df['Positive'] == df['Positive'].shift(1)
df[['open', 'close', 'Positive', 'test']]
df[['open', 'close', 'Positive', 'test']].dropna(axis=0)

# Which columns are needed for this iteration?
test = df[10:15]
for i, row in test.iterrows():
    row2 = next(row)








'''
Concept: Red candle (1) followed by larger green candle (2)
Question: How do we efficiently find both bull/bear sides?
1. high (1) < high (2)
2. low (1) > low (2)
3. open (1) < close (2)
4. [Bottom candlestick criteria?]
'''
# Criteria 1

# Criteria 2

# Criteria 3
