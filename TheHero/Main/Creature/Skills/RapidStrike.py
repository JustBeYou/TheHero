from .SkillProxyInterface import SkillProxyInterface

@SkillProxyInterface.register
class RapidStrike(SkillProxyInterface):
    def getChance(self):
        return 0.1

    def __getitem__(self, key: str):
        return self.internalCreature[key]

    def attack(self, enemy):
        self.internalCreature.attack(enemy)
        self.internalCreature.attack(enemy)