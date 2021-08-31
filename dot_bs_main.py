"""

dot_bs_main.py

The main file for the Default Octopath Tensei Battle System. Run this to play the game.

"""

from elements import attack_dict
from boss_enemy import NORM_MULT, RES_MULT, RPL_MULT, VULN_MULT, WEAK_MULT, Boss

if __name__ == '__main__':
    turncount = 1
    enemy = Boss()

    print("Turn: " + str(turncount))
    print(enemy)

    while True:
        command = input("Command: ").lower().strip()
        attack = attack_dict.get(command)

        if attack == None:
            if command == "end":
                break
            else:
                print("Bad input")
                continue
        else:
            status, damage = enemy.takeDamage(1000, attack)
            print(status + str(damage) + " damage")
            turncount = turncount + 1

            if turncount % 8 - 1 == 0:
                enemy.shuffleWeaknesses()
                print("The boss's elements have changed!")

            print("Turn: " + str(turncount))
            print(enemy)

        
