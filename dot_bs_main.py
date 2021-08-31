"""

dot_bs_main.py

The main file for the Default Octopath Tensei Battle System. Run this to play the game.

"""

from random import randint
from elements import DamageElement
from boss_enemy import Boss

if __name__ == '__main__':
    test = ["SWD", "LNC", "AXE", "BOW", "DAG", "STA", "FIR", "WAT", "WND", "EAR", "LIG", "SHD"]
    enemy = Boss()
    
    for i in range(0,12):
        enemy.weakReveal[i] = randint(0,1)

    print(enemy.weakReveal)
    print(enemy.weaknesses)

    print(enemy)