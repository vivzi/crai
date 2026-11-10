import crsim.data.CONSTANTS as CONSTANTS

class Player:
    def __init__(self, deck=None, playerNumber=0):
        self.elixir = 0
        self.deck = deck if deck is not None else list(CONSTANTS.DECK) # maybe in future if i decide to create a random deck sim
        self.playerNumber = playerNumber