from .Creature.Hero import Hero
from .Creature.WildBeast import WildBeast
from .Creature.HittableCreature import HittableCreature
from .Creature.Skills.SkillProxyInterface import SkillProxyInterface
from random import choices

class Main:
    @staticmethod
    def main():
        print ('--- Simulating a battle in the land of Emagia ---')

        ourHero = Hero('Orderus')
        theBeast = WildBeast('Argyris')

        turns = 0

        ourHeroFirst = True
        if ourHero['speed'] > theBeast['speed']:
            pass
        elif ourHero['speed'] == theBeast['speed']:
            if ourHero['luck'] > theBeast['luck']:
                pass
            else:
                ourHeroFirst = False
        else:
            ourHeroFirst = False

        attacker: HittableCreature = ourHero
        defender: HittableCreature = theBeast
        if not ourHeroFirst:
            attacker, defender = defender, attacker

        while turns < 20 and not ourHero.isDead() and not theBeast.isDead():
            print ('--- Turn {} ---'.format(turns))
            print ('It\'s time for {} to attack.'.format(attacker.getName()))

            attacker = Main.enchant(attacker)
            defender = Main.enchant(defender)

            attacker.attack(defender)

            if isinstance(attacker, SkillProxyInterface):
                attacker = attacker.getInternalObject()
            if isinstance(defender, SkillProxyInterface):
                defender = defender.getInternalObject()

            attacker, defender = defender, attacker
            print ('--- --- ---\n')
            turns += 1

        if ourHero.isDead():
            print('{} has fallen... Curse you {}!'.format(ourHero.getName(), theBeast.getName()))
        elif theBeast.isDead():
            print('Glorious victory!')
        else:
            print('This time {} escaped, but the next time it won\'t have a chance!', theBeast.getName())

    @staticmethod
    def enchant(creature):
        if len(creature.getSkills()):
            totalChance = 1
            skills = creature.getSkills()[::]
            chances = []
            for skill in skills:
                chances.append(skill.getChance())
                totalChance -= skill.getChance()
            skills.append(None)
            chances.append(totalChance)

            chosenSkill = choices(skills, chances)[0]
            if chosenSkill != None:
                enchantedCreature = chosenSkill(creature)
                return enchantedCreature
        return creature

if __name__ == "__main__":
    Main.main()
