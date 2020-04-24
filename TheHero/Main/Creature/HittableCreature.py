from .CreatureInterface import CreatureInterface
from ..Stats.StatsStore import StatsStore
from random import choices

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

    def attack(self, enemy):
        miss = [True, False]
        luck = [enemy['luck'] / 100, 1 - enemy['luck'] / 100]
        missed = choices(miss, luck)[0]

        damage = self.stats['strength'] - enemy['defence']
        if damage > 0 and not missed:
            enemy.removeFromStat('health', damage)
            return (True, damage)

        return False

    def isDead(self) -> bool:
        return self.stats['health'] <= 0