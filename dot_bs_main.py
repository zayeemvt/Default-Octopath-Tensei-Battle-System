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
    displayOutput(game.player)
    displayOutput(game.enemy)

    while True:
        if (game.player.ko == True):
            game.process()
            continue

        command = parseCommand(getInput("Command: "))

        if command == "end":
            displayOutput("Final damage count: %d" % game.enemy.damageCounter)
            break

        elif command == "attack":
            if len(game.player.action_queue) == 0:
                displayOutput("No actions registered.")
            else:
                game.process()

        elif command in attack_dict:
            if len(game.player.action_queue) == game.player.battle_points:
                displayOutput("Maximum actions registered.")
            else:
                game.registerAction(attack_dict[command])
                displayOutput("Action registered.")

        else:
            displayOutput("Bad input")