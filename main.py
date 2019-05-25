
from strategies.candles.engulfing import engulfing
from strategies.candles.doji import doji
from other.load import Load

filename = 'data/btc_hourly_candle_2019.csv'

def main():
    df = Load(filename, window=1)
    # df.shift()
    df.data['engulfing'] = engulfing(df.data)
    df.data['doji'] = doji(df.data)

if __name__ == "__main__":
    main()
