"""

io_handler.py

The module for facilitating input/output through either the console or the Discord bot.

"""

def getInput(text = ""):
    return input(text)

def displayOutput(text):
    print(text)

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