from .SkillProxyInterface import SkillProxyInterface
from ..Hero import Hero

@SkillProxyInterface.register
class MagicShield(SkillProxyInterface):
    def getChance(self):
        return 0.2

    def __getitem__(self, key: str):
        if key == 'defence' and isinstance(self.getInternalObject(), Hero):
            return self.internalCreature['defence'] * 2
        return self.internalCreature[key]