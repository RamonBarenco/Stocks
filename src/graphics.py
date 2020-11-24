import matplotlib.pyplot as plt


class Graphics(object):
    def __init__(self, stockValue):
        self.stockValue = stockValue

    def returnMovingAveragePlot(self, shortMA, longMA, column):
        fig, ax = plt.subplots(figsize=(16, 9))

        for i, col in enumerate(self.stockValue[column]):
            ax.plot(self.stockValue.index, self.stockValue[col], label=col)

        for s, scol in enumerate(shortMA):
            ax.plot(shortMA.index, shortMA[scol],
                    label='Short moving Average '+scol)

        for l, lcol in enumerate(longMA):
            ax.plot(longMA.index, longMA[lcol],
                    label='Long moving Average '+lcol)

        ax.set_xlabel('Date')
        ax.set_ylabel('Adjusted closing price ($)')
        ax.legend()
        plt.show()
