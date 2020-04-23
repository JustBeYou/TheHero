from .StatFieldInterface import StatFieldInterface
from random import randint

@StatFieldInterface.register
class StatNumericField(StatFieldInterface):
    currentValue: int = 0

    def __init__(self, name: str, minValue: int, maxValue: int):
        self.name = name
        self.minValue = minValue
        self.maxValue = maxValue
        self.resetValue()

    def resetValue(self):
        self.currentValue = randint(self.minValue, self.maxValue)

    def getCurrentValue(self) -> int:
        return self.currentValue

    def setCurrentValue(self, value: int):
        self.currentValue = value