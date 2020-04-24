from abc import ABC, abstractmethod

class StatFieldInterface(ABC):
    def __init__(self):
        self.name: str = 'abstract'

    def getName(self) -> str:
        return self.name

    @abstractmethod
    def getCurrentValue(self):
        raise NotImplementedError

    @abstractmethod
    def setCurrentValue(self, value):
        raise NotImplementedError

    @abstractmethod
    def resetValue(self):
        raise NotImplementedError