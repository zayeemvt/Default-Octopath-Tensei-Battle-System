"""

dot_bs_main.py

The main file for the Default Octopath Tensei Battle System. Run this to play the game.

"""

from elements import attack_dict
from io_handler import *
from battle_manager import Battle

if __name__ == '__main__':
    helpMenu()

    game = Battle()

    displayOutput("Turn: %d" % (game.turncount))
    displayOutput(game.enemy)

    while True:
        command = getInput("Command: ").lower().strip()
        attack = attack_dict.get(command)

        if attack == None:
            if command == "end":
                displayOutput("Final damage count: %d" % game.enemy.damageCounter)
                break
            else:
                displayOutput("Bad input")
        else:
            game.process(attack)