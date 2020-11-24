import stock
import movingAverage
import graphics

if __name__ == "__main__":
    # Facebook (FB), Amazon (AMZN), Apple (AAPL),Netflix (NFLX) and Google (GOOG).
    # Define the stocks we want analyse.
    faang = ["FB", "AMZN", "AAPL", "NFLX", "GOOG"]
    #aapl = ["AAPL"]
    # We would like to see the data avaliable between this dates
    start_date = '2020-01-01'
    end_date = '2020-11-20'
    # Define the days average
    short_rolling = 20
    long_rolling = 100
    # Define the column we want analyse
    column = ["Close"]

    stock = stock.Stock(faang)
    stock_values = stock.returnPrices(start_date, end_date)

    movingAverage = movingAverage.MovingAverage(
        stock_values, start_date, end_date)
    shortMovingAverage_values = movingAverage.returnMovingAverage(
        short_rolling)
    longMovingAverage_values = movingAverage.returnMovingAverage(long_rolling)

    graphic = graphics.Graphics(stock_values)
    graphic.returnMovingAveragePlot(
        shortMovingAverage_values, longMovingAverage_values, column)
