import pandas as pd
import strategies.candles.engulfing as engulfing

filename = 'data/btc_hourly_candle_2019.csv'


def main():
    signal_df = pd.DataFrame()
    df = Load(filename)
    dff.add_columns()
    df.shift(1)
    engulfing(df.data['df0'], df.data['df1'])






if __name__ == "__main__":
    main()
