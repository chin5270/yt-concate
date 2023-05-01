from abc import ABC
from abc import abstractmethod

class Step(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def process(self,data,inputs,utils): # inputs是字典
        pass


class StepException(Exception):
    pass