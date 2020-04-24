from .SkillProxyInterface import SkillProxyInterface
from ...Printable import Printable

@SkillProxyInterface.register
@Printable
class RapidStrike(SkillProxyInterface):
    @staticmethod
    def getChance():
        return 0.1

    def __getitem__(self, key: str):
        return self.internalCreature[key]

    def attack(self, enemy):
        self.internalCreature.attack(enemy)
        self.internalCreature.attack(enemy)