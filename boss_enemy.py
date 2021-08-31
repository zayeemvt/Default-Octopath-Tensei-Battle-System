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

class Boss():
    def __init__(self):
        self.damageCounter = 0
        self.weaknesses = [3, 2, 2, 2, 1, 1, 1, 1, 0.5, 0.5, 0.5, -1]
        self.attackType = GuardElement.PHYSICAL

        shuffle(self.weaknesses)

    
