from .Creature.CreatureInterface import CreatureInterface
from .Creature.Skills.SkillProxyInterface import SkillProxyInterface

def Printable(originalClass):
    if issubclass(originalClass, CreatureInterface):
        originalInit = originalClass.__init__
        def __init__(self, *args, **kws):
            originalInit(self, *args, **kws)
            print ("{} appeared on the battle field...".format(self.getName()))
            stats = ['health', 'strength', 'defence', 'speed', 'luck']
            for stat in stats:
                print ("{}: {}".format(stat, self[stat]))
            print ()

        originalAttack = originalClass.attack
        def attack(self, enemy, *args, **kws):
            result = originalAttack(self, enemy, *args, **kws)
            if result:
                print ("What a strike! {} suffered -{} health points. Left: {}".format(enemy.getName(), result[1], enemy['health']))
            else:
                print ("Terrible miss...")


        originalClass.__init__ = __init__
        originalClass.attack = attack

    if issubclass(originalClass, SkillProxyInterface):
        originalInit = originalClass.__init__
        def __init__(self, *args, **kws):
            originalInit(self, *args, **kws)
            print('{} spell was invoked by {}!'.format(originalClass.__name__, self.getInternalObject().getName()))
        originalClass.__init__ = __init__

    return originalClass
