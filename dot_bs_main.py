"""

dot_bs_main.py

The main file for the Default Octopath Tensei Battle System. Run this to play the game.

"""

from elements import attack_dict
from boss_enemy import NORM_MULT, RES_MULT, RPL_MULT, VULN_MULT, WEAK_MULT, Boss

def helpMenu():
    print("\n===================================================")
    print("============= DEFAULT OCTOPATH TENSEI =============")
    print("============== BATTLE SYSTEM LOADED ===============")
    print("===================================================")
    print("\n")
    print("===================================================")
    print("Deal as much damage to the boss as you can!")
    print("You have six weapons and six magic spells at your disposal.")
    print("Figure out which weapon or spell the boss is weak to by attacking the boss.")
    print("To attack, type in the name of the weapon or spell you want to use.")
    print("The boss's weaknesses will change after a certain amount of turns.")
    print("===================================================")
    print("Weapons - sword, lance, axe, bow, dagger, staff")
    print("Magic - fire, water, wind, earth, light, shadow")
    print("===================================================")
    print("\n===================================================")
    print("             <<<Press ENTER to start>>>            ")
    print("===================================================")
    input()
    print("\n================== BATTLE START ==================")

if __name__ == '__main__':
    helpMenu()

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