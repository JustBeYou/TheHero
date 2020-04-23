from typing import List, Dict
from .StatFieldInterface import StatFieldInterface

class StatsStore:
    stats: Dict[str, StatFieldInterface] = {}

    def __init__(self, config: List[StatFieldInterface]):
        for configElem in config:
            self.stats[configElem.name] = configElem

    def resetStats(self):
        for statName in self.stats:
            self.stats[statName].resetValue()

    def __getitem__(self, key: str):
        return self.stats[key].getCurrentValue()

    def __setitem__(self, key: str, value):
        self.stats[key].setCurrentValue(value)