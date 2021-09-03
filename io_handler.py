"""

io_handler.py

The module for facilitating input/output through either the console or the Discord bot.

"""

from elements import action_dict

command_list = [ "end", "attack" ]

def getInput(text = ""):
    return input(text)

def displayOutput(text):
    print(text)

def parseCommand(command):
    command = command.lower().strip()

    if (command in action_dict) or (command in command_list):
        return command
    else:
        return "invalid"


def helpMenu():
    print("")
    print("===================================================")
    print("============= DEFAULT OCTOPATH TENSEI =============")
    print("============== BATTLE SYSTEM LOADED ===============")
    print("===================================================")
    print("")
    print("===================================================")
    print("Deal as much damage to the boss as you can!")
    print("You have six weapons and six magic spells at your disposal.")
    print("Figure out which weapon or spell the boss is weak to by attacking the boss.")
    print("")
    print("Use battle points to perform attacks. Each attack consumes one battle point.")
    print("Type in the name of a weapon or spell to register it.")
    print("When you're ready to attack, type \"attack\" to finish your turn.")
    print("")
    print("After your turn, the boss will use either a physical or magical attack.")
    print("Use battle points to activate guards on your turn. Each guard has a specific type.")
    print("Parries are good against physical attacks, and reflects are good against magical attacks.")
    print("Use the right guard and the boss's attack will fail, dealing damage back to it!")
    print("")
    print("If you take damage, you can use battle points to heal a small portion of your health.")
    print("If your health reaches 0, you will be KO'd and cannot take any actions or gain battle points next turn.")
    print("Afterward, you will be revived back to full health.")
    print("")
    print("The boss's weaknesses will change after a certain amount of turns.")
    print("Striking a boss's weakness or vulnerability will not only deal bonus damage...")
    print("You'll also gain a battle point when you first hit an enemy's weakness on that turn!")
    print("But if you attack with the wrong weapon or spell, the boss might repel the damage back to you...")
    print("")
    print("===================================================")
    print("Weapons - sword, lance, axe, bow, dagger, staff")
    print("Magic - fire, water, wind, earth, light, shadow")
    print("Guards - parry, reflect")
    print("Other - heal, attack")
    print("===================================================")
    print("")
    print("===================================================")
    print("             <<<Press ENTER to start>>>            ")
    print("===================================================")
    input()
    print("")
    print("================== BATTLE START ==================")