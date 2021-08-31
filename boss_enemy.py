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

class Boss():
    def __init__(self):
        self.damageCounter = 0
        self.weaknesses = [3, 2, 2, 2, 1, 1, 1, 1, 0.5, 0.5, 0.5, -1]
        self.weakReveal = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.attackType = GuardElement.PHYSICAL

        shuffle(self.weaknesses)

    def takeDamage(self, damage):
        self.damageCounter = self.damageCounter + damage

    def determineAttackType(self):
        self.attackType = randint(GuardElement.PHYSICAL, GuardElement.MAGICAL)

    def attack(self):
        return self.attackType

    def displayWeaknesses(self):
        values = ""
        text = ["SWD", "LNC", "AXE", "BOW", "DAG", "STA", "FIR", "WAT", "WND", "EAR", "LIG", "SHD"]
        display = ""

        weakness_dict = {3 : "VUL", 2 : "WEA", 1 : "NOR", 0.5 : "RES", -1 : "RPL"}

        for type in DamageElement:
            values = values + (weakness_dict[self.weaknesses[type]] if self.weakReveal[type] == 1 else " ? ") + " "
            display = display + text[type] + " "

        display = values + "\n" + display
        
        return display


    def __str__(self) -> str:
        return "Damage: " + str(self.damageCounter) + "\n" + self.displayWeaknesses() + "\n"
