import pandas as pd


class MovingAverage(object):

    def __init__(self, stockValue, startDate, endDate):
        self.stockValue = stockValue
        self.startDate = startDate
        self.endDate = endDate

    def returnMovingAverage(self, windowMA):
        stock_values_close = self.stockValue["Close"]
        all_weekdays = pd.date_range(
            start=self.startDate, end=self.endDate, freq="B")
        stock_values_close = stock_values_close.reindex(all_weekdays)
        stock_values_close = stock_values_close.fillna(method='ffill')
        return stock_values_close.rolling(window=windowMA).mean()
