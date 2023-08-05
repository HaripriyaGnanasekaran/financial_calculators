import pandas as pd
from calculation.variables import file_paths as fp
from calculation.variables.levels import financial_df
from calculation.dataset.dataset import Dataset


class ReadHistoricalExcel:
    def __init__(self):
        self.file = fp.historical_data_file

    def execute(self):
        df = pd.read_excel(self.file)
        Dataset.data[financial_df] = df
