"""

dot_bs_main.py

The main file for the Default Octopath Tensei Battle System. Run this to play the game.

"""

from elements import DamageElement
from boss_enemy import Boss

if __name__ == '__main__':
    test = ["SWD", "LNC", "AXE", "BOW", "DAG", "STA", "FIR", "WAT", "WND", "EAR", "LIG", "SHD"]
    enemy = Boss()

    for type in DamageElement:
        label = str(test[type])
        value = str(enemy.weaknesses[type])
        print(label + ": " + value)