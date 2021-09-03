"""

elements.py

A file that contains enums and lists for the various elements used in this game.
These are used as quick indices for lists and maps.

"""

from enum import IntEnum

# Enumeration for boss weakness types
class DamageElement(IntEnum):
    # Physical elements
    SWORD = 0
    LANCE = 1
    AXE = 2
    BOW = 3
    DAGGER = 4
    STAFF = 5

    # Magical elements
    FIRE = 6
    WATER = 7
    WIND = 8
    EARTH = 9
    LIGHT = 10
    SHADOW = 11

    # Player actions
    PHYSICAL = 20
    MAGICAL = 21
    HEAL = 30
    
element_abbrvs = ["SWD", "LNC", "AXE", "BOW", "DAG", "STA", "FIR", "WAT", "WND", "EAR", "LIG", "SHD"] # abbreviations for elements

# Input to element mapping
action_dict = {"sword" : DamageElement.SWORD, "lance" : DamageElement.LANCE, "axe" : DamageElement.AXE,
                "bow" : DamageElement.BOW, "dagger" : DamageElement.DAGGER, "staff" : DamageElement.STAFF,
                "fire" : DamageElement.FIRE, "water" : DamageElement.WATER, "wind" : DamageElement.WIND,
                "earth" : DamageElement.EARTH, "light" : DamageElement.LIGHT, "shadow" : DamageElement.SHADOW,
                "swd" : DamageElement.SWORD, "lnc" : DamageElement.LANCE,
                "dag" : DamageElement.DAGGER, "sta" : DamageElement.STAFF,
                "fir" : DamageElement.FIRE, "wat" : DamageElement.WATER, "wnd" : DamageElement.WIND,
                "ear" : DamageElement.EARTH, "lig" : DamageElement.LIGHT, "shd" : DamageElement.SHADOW,
                "parry" : DamageElement.PHYSICAL, "reflect" : DamageElement.MAGICAL, "heal" : DamageElement.HEAL}