from unittest import TestCase
from ..Main.Stats.StatsStore import StatsStore
from ..Main.Stats.StatNumericField import StatNumericField
from ..Main.Stats.StatFieldInterface import StatFieldInterface

class MockStatField(StatFieldInterface):
    value = 0

    def __init__(self, id: int):
        self.name = 'mock' + str(id)

    def getCurrentValue(self) -> int:
        return self.value

    def setCurrentValue(self, value: int):
        self.value = value

    def resetValue(self):
        self.value = 0

class TestStats(TestCase):
    def test_numericFieldCreation(self):
        obj = StatNumericField('test', 0, 100)
        self.assertEqual(obj.getName(), 'test')
        self.assertEqual(obj.minValue, 0)
        self.assertEqual(obj.maxValue, 100)
        self.assertTrue(obj.getCurrentValue() <= 100 and obj.getCurrentValue() >= 0)

    def test_numericFieldResetValue(self):
        obj = StatNumericField('test', 0, 100)
        obj.resetValue()
        self.assertTrue(obj.getCurrentValue() <= 100 and obj.getCurrentValue() >= 0)

    def test_statsStoreCreation(self):
        obj = StatsStore([MockStatField(1), MockStatField(2)])
        self.assertEqual(len(obj.stats.keys()), 2)

    def test_statsStoreAccess(self):
        obj = StatsStore([MockStatField(1), MockStatField(2)])

        obj['mock1'] = 123
        self.assertEqual(obj['mock1'], 123)

        obj['mock2'] = 321

        obj.resetStats()
        self.assertEqual(obj['mock1'], 0)
        self.assertEqual(obj['mock2'], 0)
