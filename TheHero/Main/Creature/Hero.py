from .HittableCreature import HittableCreature
from ..Stats.StatsStore import StatsStore
from ..Stats.StatNumericField import StatNumericField

class Hero(HittableCreature):
    def __init__(self, name: str):
        super().__init__(name, StatsStore([
            StatNumericField('health', 70, 100),
            StatNumericField('strength', 70, 80),
            StatNumericField('defence', 45, 55),
            StatNumericField('speed', 40, 50),
            StatNumericField('luck', 10, 30),
        ]))