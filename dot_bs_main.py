"""

dot_bs_main.py

The main file for the Default Octopath Tensei Battle System. Run this to play the game.

"""

from random import randint
from elements import DamageElement
from boss_enemy import NORM_MULT, RES_MULT, RPL_MULT, VULN_MULT, WEAK_MULT, Boss

if __name__ == '__main__':
    attack_dict = {"sword" : DamageElement.SWORD, "lance" : DamageElement.LANCE, "axe" : DamageElement.AXE,
                    "bow" : DamageElement.BOW, "dagger" : DamageElement.DAGGER, "staff" : DamageElement.STAFF,
                    "fire" : DamageElement.FIRE, "water" : DamageElement.WATER, "wind" : DamageElement.WIND,
                    "earth" : DamageElement.EARTH, "light" : DamageElement.LIGHT, "shadow" : DamageElement.SHADOW,
                    "swd" : DamageElement.SWORD, "lnc" : DamageElement.LANCE,
                    "dag" : DamageElement.DAGGER, "sta" : DamageElement.STAFF,
                    "fir" : DamageElement.FIRE, "wat" : DamageElement.WATER, "wnd" : DamageElement.WIND,
                    "ear" : DamageElement.EARTH, "lig" : DamageElement.LIGHT, "shd" : DamageElement.SHADOW}

    turncount = 1
    enemy = Boss()

    print("Turn: " + str(turncount))
    print(enemy)

    while True:
        attack = input("Attack: ").lower().strip()
        attack = attack_dict.get(attack)

        if attack == None:
            print("Bad input")
            continue
        else:
            status, damage = enemy.takeDamage(1000, attack)
            print(status + str(damage) + " damage")
            turncount = turncount + 1

            if turncount % 8 - 1 == 0:
                enemy.shuffleWeaknesses()

            print("Turn: " + str(turncount))
            print(enemy)

        
