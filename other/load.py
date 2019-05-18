

class Load:
    filename = 'data/btc_hourly_candle_2019.csv'
    # NOTE: we want to apply functions first, then shift
    def __init__(self, window=None **kwargs):
        self.window = window
        self.df = pd.read_csv(self.filename)
        for func, param in kwargs.items():
            getattr(self, func)(param)

    def shift(self, window):
        for i in range(1, window+1):
            # TODO: is this right
            setattr(self, 'df' + str(i)) = df.shift(i)
            self.df[new_column] = df[column].shift(i)

    # True == green candle
    def green_candle(self):
        self.df['green_candle'] = self.df['close'] > self.df['open']

    def body_maxmin(self):
        body = df[['open', 'close']].values
        self.df['max'] = map(max, body)
        self.df['min'] = map(min, body)
