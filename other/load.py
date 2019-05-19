

class Load:
    # NOTE: we want to apply functions first, then shift
    def __init__(self, filename, **kwargs):
        self.window = window
        self.df = pd.read_csv(filename)
        self.data = {}

    def add_columns(self):
        self.green_candle()
        self.body_maxmin()

    # True == green candle
    def green_candle(self):
        self.df['green_candle'] = self.df['close'] > self.df['open']

    def body_maxmin(self):
        body = df[['open', 'close']].values
        self.df['max'] = map(max, body)
        self.df['min'] = map(min, body)

    def extend_date(self, displacement):
        self.df['date'] = [datetime.strptime(hr, '%Y-%m-%d %H:%M:%S') for hr in df['date']]
        last_date = self.df['date'].at[len(df)-1]
        dates = [last_date + timedelta(hours=i+1) for i in range(displacement)]
        self.df = self.df.append({'date': dates}, ignore_index=True, sort=False)

    def shift(self, window):
        for i in range(0, window+1):
            self.data['df' + str(i)] = self.df.shift(i)[window:]
