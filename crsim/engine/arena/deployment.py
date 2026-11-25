# deployment.py
# currently only spawns troops and on top of that the deploy function is inaccessible due to the lack of a controller class

import crsim.data.CONSTANTS as CONSTANTS
import numpy as np
from crsim.engine.arena.arena import Arena
from crsim.engine.player import Player
from crsim.data.cards import Card, Cards
from crsim.data.enums import CardType, DeployMessage
from crsim.engine.entities.entity.troop import Troop
from crsim.engine.entities.entity_manager import EntityManager

class Deployment:
    def __init__(self, arena, player1, player2, entity_manager):
        self.arena = arena
        self.players = {
            1: player1,
            2: player2
        }
        self.entity_manager = entity_manager

    def deploy(self, player, card_name, x, y):
        card = Cards[card_name]

        # messages possible:
        # OK which means the troop is deployed
        # NO_ELIXIR which means the player doesn't have enough elixir for that specific card
        # NOT_IN_HAND which means the card is not in the player's hand of 4 cards
        # INVALID_ZONE which means those coordinates aren't deployable
         
        message = self.is_deployable(player, x, y, player.elixir, card)
        
        if message == DeployMessage.OK:
            print("Deployable!")
        else:
            return message

        player.elixir -= self.player.elixir # take away elixir from player

        if card.type == CardType.TROOP:
            self.entity_manager.spawn_troop(card, x, y, player)

    # checks if card is deployable, if it is it returns "OK" otherwise it returns any of the other messages
    def is_deployable(self, player, x, y, elixir, card):
        positions = (self.arena.player1Deployable if player.playerNumber == 1 else self.arena.player2Deployable)

        if not np.any(np.all(positions == (x,y), axis=1)):
            return DeployMessage.INVALID_ZONE
        if elixir < card.cost:
            return DeployMessage.NO_ELIXIR
        
        return DeployMessage.OK