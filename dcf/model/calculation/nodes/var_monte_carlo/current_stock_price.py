from calculation.base import CalculationNode

from calculation.variables.levels import market_df, metrics_dict
from calculation.variables import computed_variables as cv
from calculation.variables import existing_variables as ev


class CurrentStockPrice(CalculationNode):

    def execute(self):
        self.data[metrics_dict].update({cv.current_stock_price: self.data[market_df][ev.close].iloc[-1]})