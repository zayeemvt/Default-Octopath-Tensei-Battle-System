"""

battle_manager.py

The module that manages each individual battle for the game.

"""

from boss_enemy import Boss
from player import Player
from io_handler import *
from elements import DamageElement, action_dict

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

        ko_this_turn = False
        weakness_exploited = False

        # Player Phase
        while len(player.action_queue) > 0:
            player.useBP()
            action = player.action_queue.pop(0)

            if (action < DamageElement.PHYSICAL): # Player is attacking
                attack_message = list(action_dict.keys())[list(action_dict.values()).index(action)]

                if action < DamageElement.FIRE: # Weapon attacks
                    displayOutput("\nPlayer strikes with a %s." % (attack_message))
                else:
                    displayOutput("\nPlayer casts a %s-element spell." % (attack_message))

                multiplier, attack_status = enemy.checkWeakness(action)
                
                if (attack_status == "rpl"):
                    damage = calculateDamage(1)
                    player.takeDamage(damage)
                    displayOutput(damage_dict[attack_status] + "Player takes %d damage." % damage)

                    if (player.ko == True):
                        player.action_queue.clear()
                        ko_this_turn = True
                else:
                    if (attack_status == "vuln" or attack_status == "weak") and (weakness_exploited == False):
                        player.refundBP(1)
                        weakness_exploited = True
                    damage = calculateDamage(multiplier)
                    enemy.takeDamage(damage)
                    displayOutput(damage_dict[attack_status] + "Enemy takes %d damage." % damage)
            
            elif (action < DamageElement.HEAL): # Player is guarding
                guard_applied = player.useGuard(action)

                if(not guard_applied):
                    player.refundBP(1)
                    displayOutput("\nGuard already applied!")
                elif(action == DamageElement.PHYSICAL):
                    displayOutput("\nReady to parry the enemy's attack.")
                else:
                    displayOutput("\nReflective barrier activated.")
            
            else: # Player is healing
                heal = calculateHeal(1)
                player.restoreHealth(heal)
                displayOutput("\nPlayer uses a healing spell.")
                displayOutput("Player restored %d health." % heal)

        # Enemy Phase
        if (player.ko == False): # If player dies from repel, don't bother with enemy turn
            element = enemy.determineAttackType() # choose enemy attack type
            displayOutput("\nEnemy uses a %s attack." % ("physical" if (element == DamageElement.PHYSICAL) else "magical"))

            defend_status = player.checkGuardStatus(element)
            if defend_status == "hit":
                damage = calculateDamage(1)
                player.takeDamage(damage)
                displayOutput("Player takes %d damage." % damage)

                if (player.ko == True):
                    ko_this_turn = True
            elif defend_status == "repelled":
                damage = calculateDamage(1)
                enemy.takeDamage(damage)
                displayOutput("Repelled! Enemy takes %d damage." % damage)
        
        player.removeGuard()

        if player.ko != True: # Restore BP when player is alive
            player.replenishBP()
        else:
            if (ko_this_turn == False): # Player is dead, but didn't die on this turn
                player.revive()
                player.replenishBP()
            else: # Player just died on this turn
                displayOutput("Defeated! Player will revive next turn.")

        self.turncount = self.turncount + 1

        if self.turncount % SWITCH_TURNCOUNT - 1 == 0:
            enemy.shuffleWeaknesses()
            displayOutput("The boss's elements have changed!")

        print("\n===================================================")
        displayOutput("Turn: %d" % self.turncount)
        displayOutput(player)
        displayOutput(enemy)

    def registerAction(self, action):
        self.player.queueAction(action)