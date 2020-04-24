from typing import List, Dict
from .StatFieldInterface import StatFieldInterface

class StatsStore:
    def __init__(self, config: List[StatFieldInterface]):
        self.stats: Dict[str, StatFieldInterface] = {}
        for configElem in config:
            self.stats[configElem.name] = configElem

    def resetStats(self):
        for statName in self.stats:
            self.stats[statName].resetValue()

    def __getitem__(self, key: str):
        return self.stats[key].getCurrentValue()

    def __setitem__(self, key: str, value):
        self.stats[key].setCurrentValue(value)

    def __contains__(self, key: str):
        return key in self.stats