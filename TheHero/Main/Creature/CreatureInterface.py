from abc import ABC, abstractmethod
from ..Stats.StatsStore import StatsStore

class CreatureInterface(ABC):
    def __init__(self):
        self.name: str = 'abstract'
        self.stats: StatsStore = StatsStore([])

    def getName(self) -> str:
        return self.name

    def getSkills(self):
        return []

    def __getitem__(self, key: str):
        return self.stats[key]

    @abstractmethod
    def addToStat(self, key: str, value):
        raise NotImplementedError

    @abstractmethod
    def removeFromStat(self, key: str, value):
        raise NotImplementedError

    @abstractmethod
    def attack(self, enemy):
        raise NotImplementedError