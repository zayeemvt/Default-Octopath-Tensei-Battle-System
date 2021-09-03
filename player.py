"""

player.py

An instance of the player character that fights the boss.
The player has their own health pool, as well as a queue for attacks.

"""

from io_handler import displayOutput
from elements import DamageElement

MAX_HEALTH = 5000
BP_RATE = 3

class Player():
    def __init__(self) -> None:
        self.health = MAX_HEALTH
        self.battle_points = BP_RATE
        self.guard = []
        self.action_queue = []
        self.ko = False

    def checkGuardStatus(self, element):
        if (element in self.guard):
            return "repelled"
        else:
            return "hit"

    def useGuard(self, element):
        self.guard.append(element)
        
    def removeGuard(self):
        if DamageElement.PHYSICAL in self.guard: self.guard.remove(DamageElement.PHYSICAL)
        if DamageElement.MAGICAL in self.guard: self.guard.remove(DamageElement.MAGICAL)

    def takeDamage(self, damage):
        self.health = self.health - damage
        if self.health <= 0:
            self.health = 0
            self.ko = True

    def restoreHealth(self, heal):
        self.health = self.health + heal
        if self.health > MAX_HEALTH:
            self.health = MAX_HEALTH

    def revive(self):
        self.ko = False
        self.health = MAX_HEALTH

    def replenishBP(self):
        self.battle_points = self.battle_points + BP_RATE

    def useBP(self):
        self.battle_points = self.battle_points - 1

    def queueAction(self, action):
        self.action_queue.append(action)

    def __str__(self) -> str:
        return "Player Health: %d/%d\nBattle Points: %d" % (self.health, MAX_HEALTH, self.battle_points)
