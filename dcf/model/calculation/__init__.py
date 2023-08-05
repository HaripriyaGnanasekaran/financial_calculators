from .preprocess import Preprocess
from .nodes.var_monte_carlo import VARMonteCarlo


class Calculation:

    @staticmethod
    def execute():
        Preprocess.execute()
        VARMonteCarlo.execute()
