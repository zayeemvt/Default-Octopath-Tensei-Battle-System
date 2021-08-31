"""

elements.py

A file that contains enums for the various elements used in this game.
These are used as quick indices for lists and arrays.

"""

from enum import IntEnum

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

class GuardElement(IntEnum):
    PHYSICAL = 0
    MAGICAL = 1