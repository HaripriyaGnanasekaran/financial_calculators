import pandas as pd
from calculation.variables import levels as l


class Dataset:
    data = {
        l.financial_df: pd.DataFrame(),
        l.market_df: pd.DataFrame(),
        l.monte_carlo_df: pd.DataFrame(),
        l.metrics_dict: {},
    }
