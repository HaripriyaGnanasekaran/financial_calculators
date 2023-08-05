from calculation.base import CalculationNode
import yfinance as yf
from calculation.variables.levels import market_df
from calculation.variables import computed_variables as cv
from calculation.variables import existing_variables as ev
from calculation.variables import inputs as i


class DailyReturn(CalculationNode):

    def execute(self):
        self.data[market_df] = yf.download(tickers=i.spy, progress=False)
        self.data[market_df][cv.daily_return] = self.data[market_df][ev.close].pct_change()