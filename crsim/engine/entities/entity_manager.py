from crsim.engine.entities.entity.troop import Troop

class EntityManager:
    def __init__(self):
        self.troops = []

    def spawn_troop(self, card, x, y, player):
        troop = Troop(card, x, y, player)
        self.troops.append(troop)
        return troop