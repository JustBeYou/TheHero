from .HittableCreature import HittableCreature
from ..Stats.StatsStore import StatsStore
from ..Stats.StatNumericField import StatNumericField

class WildBeast(HittableCreature):
    def __init__(self, name: str):
        super().__init__(name, StatsStore([
            StatNumericField('health', 60, 90),
            StatNumericField('strength', 60, 90),
            StatNumericField('defence', 40, 60),
            StatNumericField('speed', 40, 60),
            StatNumericField('luck', 25, 40),
        ]))