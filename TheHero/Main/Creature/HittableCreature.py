from .CreatureInterface import CreatureInterface
from ..Stats.StatsStore import StatsStore

@CreatureInterface.register
class HittableCreature(CreatureInterface):
    def __init__(self, name: str, stats: StatsStore):
        self.name = name
        self.stats = stats

        requiredAttrs = ['health', 'strength', 'defence', 'speed', 'luck']
        for attr in requiredAttrs:
            assert attr in self.stats

    def addToStat(self, key: str, value):
        self.stats[key] += value

    def removeFromStat(self, key: str, value):
        self.stats[key] -= value

    def isDead(self) -> bool:
        return self.stats['health'] <= 0