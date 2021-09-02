"""

battle_manager.py

The module that manages each individual battle for the game.

"""

from boss_enemy import Boss
from io_handler import *

damage_dict = { "vuln" : "Vulnerable! ", "weak" : "Weak! ", "norm" : "",
                "res" : "Resisted! " , "rpl" : "Repelled! "} # mapping to damage messages

class Battle():
    def __init__(self) -> None:
        self.turncount = 1
        self.enemy = Boss()

    def process(self,attack):
        status, damage = self.enemy.takeDamage(1000, attack)
        displayOutput(damage_dict[status] + "%d damage" % damage)
        self.turncount = self.turncount + 1

        if self.turncount % 8 - 1 == 0:
            self.enemy.shuffleWeaknesses()
            displayOutput("The boss's elements have changed!")

        displayOutput("Turn: %d" % self.turncount)
        displayOutput(self.enemy)