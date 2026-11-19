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
        # TODO: check if location is deployable and deploy card accordingly. also rn card is an integer it should be the class of the card called

        card = Cards[card_name]

        message = self.is_deployable(player, x, y, player.elixir, card)
        
        if message == DeployMessage.OK:
            print("Deployable!")
        else:
            return message

        player.elixir -= self.player.elixir
        if card.type == CardType.TROOP:
            self.entity_manager.spawn_troop(card, x, y, player)
        
    def is_deployable(self, player, x, y, elixir, card):
        positions = (self.arena.player1Deployable if player.playerNumber == 1 else self.arena.player2Deployable)

        if not np.any(np.all(positions == (x,y), axis=1)):
            return DeployMessage.INVALID_ZONE
        if elixir < card.cost:
            return DeployMessage.NO_ELIXIR
        
        return DeployMessage.OK