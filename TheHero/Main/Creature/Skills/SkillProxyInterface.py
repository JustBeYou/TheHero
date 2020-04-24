from abc import ABC, abstractmethod
from ..CreatureInterface import CreatureInterface

class SkillProxyInterface(ABC):
    def __init__(self, creatureObject):
        self.internalCreature = creatureObject

    @staticmethod
    def getChance(self):
        raise NotImplementedError

    @abstractmethod
    def __getitem__(self, key: str):
        raise NotImplementedError

    def getInternalObject(self):
        if isinstance(self.internalCreature, SkillProxyInterface):
            return self.internalCreature.getInternalObject()
        return self.internalCreature

    def getName(self) -> str:
        return self.internalCreature.getName()

    def addToStat(self, key: str, value):
        self.internalCreature.addToStat(key, value)

    def removeFromStat(self, key: str, value):
        self.internalCreature.removeFromStat(key, value)

    def attack(self, enemy):
        self.internalCreature.attack(enemy)