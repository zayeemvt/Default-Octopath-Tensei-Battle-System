"""

battle_manager.py

The module that manages each individual battle for the game.

"""

from boss_enemy import Boss

class Battle():
    def __init__(self) -> None:
        self.turncount = 1
        self.enemy = Boss()

    def process(self,command,attack):
        if attack == None:
            if command == "end":
                print("Final damage count: " + str(self.enemy.damageCounter))
                return "stop"
            else:
                print("Bad input")
                return "invalid"
        else:
            status, damage = self.enemy.takeDamage(1000, attack)
            print(status + str(damage) + " damage")
            self.turncount = self.turncount + 1

            if self.turncount % 8 - 1 == 0:
                self.enemy.shuffleWeaknesses()
                print("The boss's elements have changed!")

            print("Turn: " + str(self.turncount))
            print(self.enemy)