"""

boss_enemy.py

An instance of the boss/enemy that the teams will fight against.
The boss has a list of weaknesses/resistances that will shuffle every set number of turns.
Each turn, the boss will use either a physical or magical attack.
The boss has no HP and instead keeps a rolling counter of how much damage was done to it over the course of battle.

"""

from elements import DamageElement, GuardElement, element_abbrvs
from random import shuffle, randint

# Weakness multipliers
VULN_MULT = 4
WEAK_MULT = 2
NORM_MULT = 1
RES_MULT = 0.5
RPL_MULT = 0

# Dictionaries
mult_dict = { VULN_MULT : "vuln", WEAK_MULT : "weak", NORM_MULT : "norm", RES_MULT : "res", RPL_MULT : "rpl"}
weakness_dict = {VULN_MULT : "VUL", WEAK_MULT : "WEA", NORM_MULT : "NOR",
                 RES_MULT : "RES", RPL_MULT : "RPL"} # mapping to weakness display

class Boss():
    def __init__(self):
        self.damageCounter = 0
        self.weaknesses = [VULN_MULT, WEAK_MULT, WEAK_MULT, WEAK_MULT, NORM_MULT, NORM_MULT, NORM_MULT, NORM_MULT, RES_MULT, RES_MULT, RES_MULT, RPL_MULT]
        self.weakReveal = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # determines which elements have been hit/revealed

        self.shuffleWeaknesses()

    def checkWeakness(self, element):
        # Indicate that element has been revealed
        self.weakReveal[element] = 1

        multiplier = self.weaknesses[element]

        # Return multiplier and status message
        return multiplier, mult_dict[multiplier]

    def takeDamage(self, damage):
        self.damageCounter = self.damageCounter + damage

    def determineAttackType(self):
        return randint(GuardElement.PHYSICAL, GuardElement.MAGICAL)

    def attack(self):
        return self.attackType

    def shuffleWeaknesses(self):
        shuffle(self.weaknesses)

        self.weakReveal = [0 for i in self.weakReveal] # reset reveal list

    def displayWeaknesses(self):
        values = ""
        display = ""

        for type in DamageElement:
            # Replace weakness multiplier with weakness label if revealed, otherwise display weakness as unknown
            values = values + (weakness_dict[self.weaknesses[type]] if self.weakReveal[type] == 1 else " ? ") + " "
            display = display + element_abbrvs[type] + " " # add element abbreviation to display string

        display = values + "\n" + display
        
        return display


    def __str__(self) -> str:
        return "Enemy Damage: %d" % (self.damageCounter) + "\n" + self.displayWeaknesses() + "\n"
