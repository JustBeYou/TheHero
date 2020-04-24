from unittest import TestCase
from ..Main.Creature.Hero import Hero
from ..Main.Creature.WildBeast import WildBeast
from ..Main.Creature.HittableCreature import HittableCreature
from ..Main.Stats.StatNumericField import StatNumericField
from ..Main.Stats.StatsStore import StatsStore
from ..Main.Creature.Skills.MagicShield import MagicShield
from ..Main.Creature.Skills.RapidStrike import RapidStrike

class TestCreature(TestCase):
    def test_createCreatures(self):
        hero = Hero('test')
        beast = WildBeast('test')

        self.assertEqual(hero.getName(), 'test')
        self.assertTrue(beast['health'] >= 60 and beast['health'] <= 90)

    def test_creatureAlterStats(self):
        hero = Hero('test')

        hero.removeFromStat('defence', hero['defence'])
        self.assertEqual(hero['defence'], 0)
        hero.addToStat('defence', 10)
        self.assertEqual(hero['defence'], 10)

    def test_attackAndDeath(self):
        zeus = HittableCreature('Zeus', StatsStore([
            StatNumericField('health', 10000, 10001),
            StatNumericField('strength', 10000, 10001),
            StatNumericField('defence', 10000, 10001),
            StatNumericField('speed', 10000, 10001),
            StatNumericField('luck', 100, 100),
        ]))

        orpheus = HittableCreature('Orpheus', StatsStore([
            StatNumericField('health', 1, 1),
            StatNumericField('strength', 1, 1),
            StatNumericField('defence', 1, 1),
            StatNumericField('speed', 1, 1),
            StatNumericField('luck', 1, 1),
        ]))

        zeus.attack(orpheus)
        zeus.attack(orpheus)
        self.assertTrue(orpheus.isDead())

    def test_nestedSkills(self):
        zeus = HittableCreature('Zeus', StatsStore([
            StatNumericField('health', 10000, 10001),
            StatNumericField('strength', 10000, 10001),
            StatNumericField('defence', 10000, 10001),
            StatNumericField('speed', 10000, 10001),
            StatNumericField('luck', 100, 100),
        ]))

        proxified = MagicShield(RapidStrike(zeus))
        self.assertEqual(proxified.getInternalObject(), zeus)

    def test_skillEfect(self):
        zeus = HittableCreature('Zeus', StatsStore([
            StatNumericField('health', 10000, 10000),
            StatNumericField('strength', 10000, 10000),
            StatNumericField('defence', 10000, 10000),
            StatNumericField('speed', 10000, 10000),
            StatNumericField('luck', 100, 100),
        ]))
        orpheus = HittableCreature('Orpheus', StatsStore([
            StatNumericField('health', 1, 1),
            StatNumericField('strength', 1, 1),
            StatNumericField('defence', 1, 1),
            StatNumericField('speed', 1, 1),
            StatNumericField('luck', 1, 1),
        ]))

        proxified = RapidStrike(zeus)
        proxified.attack(orpheus)
        self.assertEqual(orpheus['health'], 1 - zeus['strength'] * 2 + orpheus['defence'] * 2)