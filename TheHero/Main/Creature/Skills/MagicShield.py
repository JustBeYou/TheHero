from .SkillProxyInterface import SkillProxyInterface
from ...Printable import Printable

@SkillProxyInterface.register
@Printable
class MagicShield(SkillProxyInterface):
    @staticmethod
    def getChance():
        return 0.2

    def __getitem__(self, key: str):
        if key == 'defence':
            return self.internalCreature['defence'] * 2
        return self.internalCreature[key]