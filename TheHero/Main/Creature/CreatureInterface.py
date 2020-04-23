from abc import ABC, abstractmethod
from ..Stats.StatsStore import StatsStore

class CreatureInterface(ABC):
    name: str = 'abstract'
    stats: StatsStore = StatsStore([])

    def getName(self) -> str:
        return self.name

    def getStats(self) -> StatsStore:
        return self.stats

    @abstractmethod
    def addToStat(self, key: str, value):
        raise NotImplementedError

    @abstractmethod
    def removeFromStat(self, key: str, value):
        raise NotImplementedError