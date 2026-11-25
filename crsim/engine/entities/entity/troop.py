# troop.py
# doesn't do much right now, will contain behavior generic to all troops soon when deployment is actually finished

import crsim.data.CONSTANTS as CONSTANTS

class Troop:
    def __init__(self, card, x, y, player):
        self.card = card
        self.x = x
        self.y = y
        self.player = player


        