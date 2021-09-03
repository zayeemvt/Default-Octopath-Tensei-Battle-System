"""

player.py

An instance of the player character that fights the boss.
The player has their own health pool, as well as a queue for attacks.

"""

from io_handler import displayOutput
from elements import DamageElement, GuardElement
from enum import IntEnum

MAX_HEALTH = 5000
BP_RATE = 3

class Player():
    def __init__(self) -> None:
        self.health = MAX_HEALTH
        self.battle_points = BP_RATE
        self.status = {}
        self.attack_queue = {}
        self.ko = False

    def checkGuardStatus(self, element):
        if not self.ko:
            if (element in self.status):
                return "repelled"
            else:
                return "hit"
        else:
            self.ko = False
            self.health = MAX_HEALTH
            return "reviving"
        
    def removeGuard(self):
        self.status = [x for x in self.status if x is not (GuardElement.PHYSICAL or GuardElement.MAGICAL)]

    def takeDamage(self, damage):
        self.health = self.health - damage
        if self.health <= 0:
            self.health = 0
            self.ko = True

    def __str__(self) -> str:
        return "Player Health: %d/%d\nBattle Points: %d" % (self.health, MAX_HEALTH, self.battle_points)
