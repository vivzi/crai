import crsim.data.CONSTANTS as CONSTANTS
from crsim.engine.arena.arena import Arena
from crsim.engine.player import Player
from crsim.data.cards import Card
from crsim.data.enums import CardType

class Deployment:
    def __init__(self, arena=Arena, player1=Player, player2=Player):
        self.arena = arena
        self.player1 = player1
        self.player2 = player2

    def deploy(self, player=Player, card=Card, x=0, y=0):
        # TODO: check if location is deployable and deploy card accordingly. also rn card is an integer it should be the class of the card called

        coords = (x, y)

        if card.type == CardType.TROOP:
            if self.player.playerNumber == 1:
                if coords in self.arena.player1Deployable:
                    print("Deployable!")
                else:
                    print("Undeployable!")
            else:
                if coords in self.arena.player2Deployable:
                    print("Deployable!")
                else:
                    print("Undeployable!")
        else:
            print("Deployable!")