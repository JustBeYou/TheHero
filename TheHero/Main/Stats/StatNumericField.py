from .StatFieldInterface import StatFieldInterface
from random import randint

@StatFieldInterface.register
class StatNumericField(StatFieldInterface):

    def __init__(self, name: str, minValue: int, maxValue: int):
        self.name = name
        self.currentValue = 0
        self.minValue = minValue
        self.maxValue = maxValue
        self.resetValue()

    def resetValue(self):
        self.currentValue = randint(self.minValue, self.maxValue)

    def getCurrentValue(self) -> int:
        return self.currentValue

    def setCurrentValue(self, value: int):
        self.currentValue = value