# The Hero

Please use Python 3.6 or later and install the dependencies: `pip install -r requirements.txt --user`.
1. Run `./run.sh` to simulate a battle.
2. Run `./test.sh` to run unit tests.

## Application design
The code is designed to be as extensible as possible. There are 3 important components:
- Main class, simulating the battle
- Creature module, for managing the behaviour of game entities like the hero and the beasts
- Stats module, generic handler for any type for stats a creature could have

1. Stats module
**Observation: I know that `stats` is uncountable, but `stat` just looked like the right name**

This module's principal class is `StatsStore`. It is a wrapper for a dictionary of strings to objects that implement `StatFieldInterface`. This interface provides a simple way to manage different properties that a creature could have.

For example, `StatNumericField` implements the functionalities for a numeric property like health, strenght, etc... It supports minimum and maximum valid values, genereating a value in the specified range and altering the value. In the same manner other `Stat` classes could be implemented with very little effort and without changing `StatsStore` logic.

For example, we could implement `StatInventoryField` easily and by overloading `+` and `-` operators working with it would be easy and very natural.

2. Creature module
Any creature should implement the base interface `CreatureInterface`. It provides methods usual actions of a creature like attacking and altering internal properties like health. `HittableCreature` is a concrete implementation of the interface with the behaviour according to the provided instructions. `Hero` and `WildBeast` are inherited from the hittable creature and they are used to store specific stats values for their types as stated in the instructions.

3. Skills implementation
In order to implement an extensible skills system, I used the Proxy design pattern. Every skill must implement the interface `SkillProxyInterface`. Using this approach, we can "activate" certain skills by encapsulating the creature object inside the skill object. For example, we have our `hero = Hero()` and our skill class `RapidStrike`. We apply the skill: `enchancedHero = RapidStrike(hero)` and now the skill proxy will handle the attack method of our hero, calling it twice.

4. Output
The user interface should never be implemented in the same place with the application logic. So, to respect that, I implemented a decorator `Printer` that can be applied to creatures and skills. It will add print functionality to methods like `__init__` and `__attack__` without chaning anything in the original classes code.

**Observation: When running tests the `Printer` will overlap with `unittest` output. I did not deactivated it for testing, but I don't think it's such a big deal for a proof of concept**

## Tests and coverage
```
Ran 9 tests in 0.009s

Name                                                  Stmts   Miss  Cover
-------------------------------------------------------------------------
TheHero\Main\Creature\CreatureInterface.py               21      6    71%
TheHero\Main\Creature\Hero.py                            12      1    92%
TheHero\Main\Creature\HittableCreature.py                26      1    96%
TheHero\Main\Creature\Skills\MagicShield.py              12      4    67%
TheHero\Main\Creature\Skills\RapidStrike.py              13      2    85%
TheHero\Main\Creature\Skills\SkillProxyInterface.py      23      6    74%
TheHero\Main\Creature\Skills\__init__.py                  0      0   100%
TheHero\Main\Creature\WildBeast.py                        8      0   100%
TheHero\Main\Creature\__init__.py                         0      0   100%
TheHero\Main\Printable.py                                27      4    85%
TheHero\Main\Stats\StatFieldInterface.py                 15      4    73%
TheHero\Main\Stats\StatNumericField.py                   16      0   100%
TheHero\Main\Stats\StatsStore.py                         16      0   100%
TheHero\Main\Stats\__init__.py                            0      0   100%
TheHero\Main\__init__.py                                  0      0   100%
TheHero\Tests\Creature.py                                36      0   100%
TheHero\Tests\Main.py                                     9      0   100%
TheHero\Tests\Stats.py                                   38      0   100%
TheHero\Tests\__init__.py                                 0      0   100%
TheHero\__init__.py                                       0      0   100%
-------------------------------------------------------------------------
```

## App output
```
--- Simulating a battle in the land of Emagia ---
Orderus appeared on the battle field...
health: 71
strength: 80
defence: 45
speed: 47
luck: 10

Argyris appeared on the battle field...
health: 62
strength: 89
defence: 53
speed: 49
luck: 37

--- Turn 0 ---
It's time for Argyris to attack.
What a strike! Orderus suffered -44 health points. Left: 27
--- --- ---

--- Turn 1 ---
It's time for Orderus to attack.
What a strike! Argyris suffered -27 health points. Left: 35
--- --- ---

--- Turn 2 ---
It's time for Argyris to attack.
MagicShield spell was invoked by Orderus!
Terrible miss...
--- --- ---

--- Turn 3 ---
It's time for Orderus to attack.
What a strike! Argyris suffered -27 health points. Left: 8
--- --- ---

--- Turn 4 ---
It's time for Argyris to attack.
What a strike! Orderus suffered -44 health points. Left: -17
--- --- ---

Orderus has fallen... Curse you Argyris!
```
