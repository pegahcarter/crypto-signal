import pandas as pd

class Load:
    # NOTE: we want to apply functions first, then shift
    def __init__(self, filename, **kwargs):
        self.window = kwargs['window']
        self.df = pd.read_csv(filename)
        self.data = {}
        self._add_columns()

    def _add_columns(self):
        self.green_candle()
        self.body_maxmin()

    # True == green candle
    def green_candle(self):
        self.df['green_candle'] = self.df['close'] > self.df['open']

    def body_maxmin(self):
        body = self.df[['open', 'close']].values
        self.df['max'] = list(map(max, body))
        self.df['min'] = list(map(min, body))

    def shift(self):
        for i in range(0, self.window+1):
            self.data['df' + str(i)] = self.df.shift(i)[self.window:]
