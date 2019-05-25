import pandas as pd

class Load:
    # NOTE: we want to apply functions first, then shift
    def __init__(self, filename, **kwargs):
        self.window = kwargs['window']
        self.data = pd.read_csv(filename)
        # self.data = {}
        self._add_columns()

    def _add_columns(self):
        self.green_candle()
        self.body_maxmin()

    # True == green candle
    def green_candle(self):
        self.data['green_candle'] = self.data['close'] > self.data['open']

    def body_maxmin(self):
        body = self.data[['open', 'close']].values
        self.data['max'] = list(map(max, body))
        self.data['min'] = list(map(min, body))

    # def shift(self):
    #     for i in range(0, self.window+1):
    #         self.data['data' + str(i)] = self.data.shift(i)[self.window:]
