import abc
from calculation.dataset.dataset import Dataset


class CalculationNode(metaclass=abc.ABCMeta):
    data = Dataset.data

    @abc.abstractmethod
    def execute(self):
        pass
