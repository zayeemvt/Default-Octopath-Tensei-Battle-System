"""

battle_manager.py

The module that manages each individual battle for the game.

"""

from boss_enemy import Boss
from player import Player
from io_handler import *

from random import randint

SWITCH_TURNCOUNT = 4

# Base calculation values
BASE_DAMAGE = 1000
BASE_HEAL = BASE_DAMAGE/2

# Variance ranges
DAMAGE_LOW = -150
DAMAGE_HIGH = 350
HEAL_LOW = -50
HEAL_HIGH = 550

damage_dict = { "vuln" : "Vulnerable! ", "weak" : "Weak! ", "norm" : "",
                "res" : "Resisted! " , "rpl" : "Repelled! "} # mapping to damage messages

def calculateDamage(multiplier):
    damage = (BASE_DAMAGE * multiplier)

    if damage != 0:
        damage = damage + randint(DAMAGE_LOW, DAMAGE_HIGH)

    return damage

def calculateHeal(multiplier):
    heal = (BASE_HEAL * multiplier) + randint(HEAL_LOW, HEAL_HIGH)

    return heal
    

class Battle():
    def __init__(self) -> None:
        self.turncount = 1
        self.enemy = Boss()
        self.player = Player()

    def process(self):
        enemy = self.enemy
        player = self.player

        # Player Phase
        while len(player.action_queue) > 0:
            player.useBP()
            action = player.action_queue.pop(0)
            if (action < DamageElement.PHYSICAL):
                multiplier, attack_status = enemy.checkWeakness(action)
                if (attack_status == "rpl"):
                    damage = calculateDamage(1)
                    player.takeDamage(damage)
                    displayOutput(damage_dict[attack_status] + "Player takes %d damage" % damage)
                else:
                    damage = calculateDamage(multiplier)
                    enemy.takeDamage(damage)
                    displayOutput(damage_dict[attack_status] + "Enemy takes %d damage" % damage)
            elif (action < DamageElement.HEAL):
                player.useGuard(action)
            else:
                heal = calculateHeal(1)
                player.restoreHealth(heal)
                displayOutput("Player restored %d health" % heal)

        # Enemy Phase
        element = enemy.determineAttackType() # choose enemy attack type
        defend_status = player.checkGuardStatus(element)
        if defend_status == "hit":
            damage = calculateDamage(1)
            player.takeDamage(damage)
            displayOutput("Player takes %d damage" % damage)
        elif defend_status == "repelled":
            damage = calculateDamage(1)
            enemy.takeDamage(damage)
            displayOutput("Repelled! Enemy takes %d damage" % damage)
        
        player.removeGuard()

        if player.ko != True:
            player.replenishBP()
        else:
            displayOutput("Defeated! Player will revive next turn.")

        self.turncount = self.turncount + 1

        if self.turncount % SWITCH_TURNCOUNT - 1 == 0:
            enemy.shuffleWeaknesses()
            displayOutput("The boss's elements have changed!")

        displayOutput("Turn: %d" % self.turncount)
        displayOutput(player)
        displayOutput(enemy)

    def registerAction(self, action):
        self.player.queueAction(action)