from strategies.candles.engulfing import engulfing
from strategies.candles.doji import doji
from other.load import Load

filename = 'data/btc_hourly_candle_2019.csv'

def main():
    df = Load(filename, window=1)
    df.shift()
    df.df['engulfing'] = engulfing(df.data['df0'], df.data['df1'])
    df.df['doji'] = doji(df.df)

if __name__ == "__main__":
    main()
