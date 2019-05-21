from strategies.candles.engulfing import engulfing
from other.load import Load

filename = 'data/btc_hourly_candle_2019.csv'

def main():
    df = Load(filename, window=1)
    df.shift()
    engulf_col = engulfing(df.data['df0'], df.data['df1'])
    print(engulf_col)

if __name__ == "__main__":
    main()
