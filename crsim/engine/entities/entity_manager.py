# entity_manager.py
# it maintains an array of troops and spells and handles spawning, directing and killing troops

from crsim.engine.entities.entity.troop import Troop

class EntityManager:
    def __init__(self):
        # creates an array of troops containing their coordinates 
        self.troops = []

    # adds a troop to the array
    def spawn_troop(self, card, x, y, player):
        troop = Troop(card, x, y, player)
        self.troops.append(troop)
        return troop