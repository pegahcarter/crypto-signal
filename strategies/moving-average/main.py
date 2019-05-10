import ccxt
import pandas as pd
from itertools import combinations
from twilio.rest import Client
from api import account_sid, auth_token, twilio_number, recipients, coins


averages = [8, 25, 99, 200]
avg_pairs = list(combinations(averages, 2))
message = ''

def fetch_data(coin):
    binance = ccxt.binance()
    try:
        ticker = coin + '/USDT'
        data = binance.fetch_ohlcv(ticker, '1h')
    except:
        ticker = coin + '/BTC'
        data = binance.fetch_ohlcv(ticker, '1h')
    return ticker, data


for coin in coins:
    ticker, data = fetch_data(coin)
    df = pd.DataFrame(
        columns=['timestamp','open', 'high', 'low', 'close', 'volume'],
        data=data
    )

    for average in averages:
        df.loc[:, average] = df['close'].rolling(window=average).mean()
        # df.loc[:, average] = df['close'].ewm(span=average).mean()

    daily = df.loc[-24:, averages]

    averages_crossed = sum([1 for avg1, avg2 in avg_pairs
                         if True and False in (daily[avg1] > daily[avg2])])

    sentiment = None
    if averages_crossed == len(avg_pairs):
        last_avg = daily.iloc[-1].pct_change().dropna()
        if len(last_avg) == len(last_avg[last_avg < 0]): # BEARISH
            sentiment = 'BEARISH'
        elif len(last_avg) == len(last_avg[last_avg > 0]): # BULLISH
            sentiment = 'BULLISH'

    if sentiment is not None:
        message += sentiment + ':   ' + ticker + '\n'


# Send the text message
client = Client(account_sid, auth_token)
if len(message) > 0:
    print(message)
    for recipient in recipients:
        client.messages.create(
            from_=twilio_number,
            body=message,
            to=recipient
        )
