import pandas as pd

class Load:
    def __init__(self, file, **kwargs):
        df = pd.read_csv(file)
        for kwarg in kwargs:
            pass

    def color_candle(self, open, close):
        if open > close:
            return 'green'
        else:
            return 'red'
