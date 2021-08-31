"""

boss_enemy.py

An instance of the boss/enemy that the teams will fight against.
The boss has a list of weaknesses/resistances that will shuffle every set number of turns.
Each turn, the boss will use either a physical or magical attack.
The boss has no HP and instead keeps a rolling counter of how much damage was done to it over the course of battle.

"""

from elements import DamageElement
from elements import GuardElement
from random import shuffle
from random import randint

VULN_MULT = 4
WEAK_MULT = 2
NORM_MULT = 1
RES_MULT = 0.5
RPL_MULT = -1

class Boss():
    def __init__(self):
        self.damageCounter = 0
        self.weaknesses = [VULN_MULT, WEAK_MULT, WEAK_MULT, WEAK_MULT, NORM_MULT, NORM_MULT, NORM_MULT, NORM_MULT, RES_MULT, RES_MULT, RES_MULT, RPL_MULT]
        self.weakReveal = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.attackType = GuardElement.PHYSICAL

        shuffle(self.weaknesses)

    def takeDamage(self, damage, element):
        calculatedDamage = (damage * self.weaknesses[element]) if (self.weaknesses[element] != RPL_MULT) else 0
        if calculatedDamage != 0:
            calculatedDamage = calculatedDamage + randint(-150, 350)
            self.damageCounter = self.damageCounter + calculatedDamage
        self.weakReveal[element] = 1

        damage_dict = { VULN_MULT : "Vulnerable! ", WEAK_MULT : "Weak! ", NORM_MULT : "", RES_MULT : "Resisted! " , RPL_MULT : "Repelled! "}

        return damage_dict[self.weaknesses[element]], calculatedDamage

    def determineAttackType(self):
        self.attackType = randint(GuardElement.PHYSICAL, GuardElement.MAGICAL)

    def attack(self):
        return self.attackType

    def shuffleWeaknesses(self):
        shuffle(self.weaknesses)

        self.weakReveal = [0 for i in self.weakReveal]

    def displayWeaknesses(self):
        values = ""
        text = ["SWD", "LNC", "AXE", "BOW", "DAG", "STA", "FIR", "WAT", "WND", "EAR", "LIG", "SHD"]
        display = ""

        weakness_dict = {VULN_MULT : "VUL", WEAK_MULT : "WEA", NORM_MULT : "NOR", RES_MULT : "RES", RPL_MULT : "RPL"}

        for type in DamageElement:
            values = values + (weakness_dict[self.weaknesses[type]] if self.weakReveal[type] == 1 else " ? ") + " "
            display = display + text[type] + " "

        display = values + "\n" + display
        
        return display


    def __str__(self) -> str:
        return "Damage: " + str(self.damageCounter) + "\n" + self.displayWeaknesses() + "\n"
