"""

battle_manager.py

The module that manages each individual battle for the game.

"""

from boss_enemy import Boss
from player import Player
from io_handler import *

from random import randint

BASE_DAMAGE = 1000

# Damage variance ranges
LOWER_RAND = -150
UPPER_RAND = 350

damage_dict = { "vuln" : "Vulnerable! ", "weak" : "Weak! ", "norm" : "",
                "res" : "Resisted! " , "rpl" : "Repelled! "} # mapping to damage messages

def calculateDamage(multiplier):
    calculatedDamage = (BASE_DAMAGE * multiplier)

    if calculatedDamage != 0:
        calculatedDamage = calculatedDamage + randint(LOWER_RAND, UPPER_RAND)

    return calculatedDamage

class Battle():
    def __init__(self) -> None:
        self.turncount = 1
        self.enemy = Boss()
        self.player = Player()

    def process(self,attack):
        enemy = self.enemy
        player = self.player

        # Player Phase
        multiplier, attack_status = enemy.checkWeakness(attack)
        damage = calculateDamage(multiplier)
        enemy.takeDamage(damage)
        displayOutput(damage_dict[attack_status] + "Enemy takes %d damage" % damage)

        # Enemy Phase
        element = enemy.determineAttackType() # choose enemy attack type
        defend_status = player.checkGuardStatus(element)
        if defend_status == "hit":
            damage = calculateDamage(1)
            player.takeDamage(damage)
            displayOutput("Player takes %d damage" % damage)
            if player.ko == True:
                displayOutput("Defeated! Player will revive next turn.")
        elif defend_status == "repelled":
            damage = calculateDamage(1)
            enemy.takeDamage(damage)
            displayOutput("Repelled! Enemy takes %d damage" % damage)
        
        player.removeGuard()

        if player.ko != True:
            pass # replenish BP

        self.turncount = self.turncount + 1

        if self.turncount % 8 - 1 == 0:
            enemy.shuffleWeaknesses()
            displayOutput("The boss's elements have changed!")

        displayOutput("Turn: %d" % self.turncount)
        displayOutput(player)
        displayOutput(enemy)