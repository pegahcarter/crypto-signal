import pandas as pd
from datetime import datetime, timedelta
import ccxt

mex = ccxt.bitmex()

start_date = datetime(year=2019,month=1,day=1)
end_date = datetime.now()

data = []
while start_date < end_date:
    candles = mex.fetch_ohlcv('BTC/USD', '1h', since=start_date.timestamp()*1000, limit=500)
    data += candles
    start_date += timedelta(hours=len(candles))

df = pd.DataFrame(data=data, columns=['date', 'open', 'high', 'low', 'close', 'volume'])

df['date'] /= 1000
df['date'] = [datetime.fromtimestamp(i) for i in df['date']]
df.to_csv('data/btc_hourly_candle_2019.csv', index=False)
