import crsim.data.CONSTANTS as CONSTANTS
import numpy as np
from crsim.engine.arena.arena import Arena
from crsim.engine.player import Player
from crsim.data.cards import Card, Cards
from crsim.data.enums import CardType

class Deployment:
    def __init__(self, arena, player1, player2):
        self.arena = arena
        self.players = {
            1: player1,
            2: player2
        }

    def deploy(self, player, card_name, x, y):
        # TODO: check if location is deployable and deploy card accordingly. also rn card is an integer it should be the class of the card called

        card = Cards[card_name]

        if card.type == CardType.TROOP:
            if self.isDeployable(player, x, y):
                print("Deployable!")
            else:
                print("Undeployable!")
        else:
            print("Deployable!")

    def is_deployable(self, player, x, y):
        positions = (self.arena.player1Deployable if player.playerNumber == 1 else self.arena.player2Deployable)

        return np.any(np.all(positions == (x,y), axis=1))