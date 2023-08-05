from .daily_return import DailyReturn
from .historical_return_std import HistoricalReturnStd
from .historical_return_mean import HistoricalReturnMean
from .historical_return_t_params import HistoricalReturnTParams
from .current_stock_price import CurrentStockPrice
from .populate_montecarlo_df import PopulateMonteCarloDF

# sequential node graph
nodes = [DailyReturn, CurrentStockPrice, HistoricalReturnMean, HistoricalReturnStd, HistoricalReturnTParams, PopulateMonteCarloDF]


class VARMonteCarlo:

    @staticmethod
    def execute():
        for node in nodes:
            node().execute()