import yfinance as yf

class Stock(object):

    def __init__(self, ticker):
        self.ticker = ticker        

    def returnPrices(self, startDate, endDate):
        return yf.download(self.ticker, start=startDate, end=endDate)
