from dataclasses import dataclass
from typing import Optional

from crsim.data.enums import (
    AttackType,
    CardType,
    TargetType,
    Transport
)

@dataclass(frozen=True)
class Card:
    name:str
    cost:int
    type:CardType

    # Troop attributes
    hp: Optional[int] = None
    speed: Optional[int] = None
    count: int = 1
    transport: Optional[Transport] = None

    # Attack attributes
    attack_type: Optional[AttackType] = None
    target_type: Optional[TargetType] = None
    damage: Optional[int] = None # ik right now all the cards in deck do damage but maybe in future if we get the full clash royale deck
    crown_tower_damage: Optional[int] = None
    attack_speed: Optional[float] = None # same reasoning as above
    range: Optional[float] = None

    # Additional attributes
    projectile_speed: Optional[float] = None
    radius: Optional[int] = None
    deploy_time: float = 1.0

Cards = {
    "Giant": Card(
        name = "Giant",
        cost = 5,
        type = CardType.TROOP,

        # Troop Attributes
        hp = 3968,
        speed = 45,
        count = 1,
        transport = Transport.GROUND,

        # Attack Attributes
        attack_type=AttackType.SINGLE_TARGET,
        target_type=TargetType.BUILDINGS,

        damage = 253,
        attack_speed = 1.5,
        range = 1.2,

        # Additional Attributes
        deploy_time = 1.0
    ),
    "MiniPEKKA": Card (
        name = "Mini P.E.K.K.A.",
        cost = 4,
        type = CardType.TROOP,

        # Troop Attributes
        hp = 1390,
        speed = 90, 
        count = 1,
        transport = Transport.GROUND,

        # Attack Attributes
        attack_type = AttackType.SINGLE_TARGET,
        target_type = TargetType.GROUND,

        damage = 755,
        attack_speed = 1.6,
        range = 0.8,

        # Other Attributes
        deploy_time = 1.0
    ),
    "Knight": Card(
        name="Knight",
        cost=3,
        type=CardType.TROOP,
        hp=1766,
        speed=60,
        count=1,
        transport=Transport.GROUND,
        attack_type=AttackType.SINGLE_TARGET,
        target_type=TargetType.GROUND,
        damage=202,
        attack_speed=1.2,
        range=1.2,
        deploy_time=1.0,
    ),
    "Archers": Card(
        name="Archers",
        cost=3,
        type=CardType.TROOP,
        hp=304,
        speed=75,
        count=2,
        transport=Transport.GROUND,
        attack_type=AttackType.SINGLE_TARGET,
        target_type=TargetType.ALL,
        damage=112,
        attack_speed=0.9,
        range=5,
        projectile_speed=600,
        deploy_time=1.0,
    ),
    "Minions": Card(
        name="Minions",
        cost=3,
        type=CardType.TROOP,
        hp=230,
        speed=90,
        count=3,
        transport=Transport.AIR,
        attack_type=AttackType.SINGLE_TARGET,
        target_type=TargetType.ALL,
        damage=107,
        attack_speed=1.2,
        range=2.5,
        projectile_speed=1000,
        deploy_time=1.0,
    ),
    "Musketeer": Card(
        name="Musketeer",
        cost=4,
        type=CardType.TROOP,
        hp=721,
        speed=60,
        count=1,
        transport=Transport.GROUND,
        attack_type=AttackType.SINGLE_TARGET,
        target_type=TargetType.ALL,
        damage=217,
        attack_speed=1,
        range=6,
        projectile_speed=1000,
        deploy_time=1.0,
    ),
    "Arrows": Card(
        name="Arrows",
        cost=3,
        type=CardType.SPELL,
        speed=1100,
        count=3,
        attack_type=AttackType.AREA_DAMAGE,
        target_type=TargetType.ALL,
        damage=122,
        crown_tower_damage=31,
        attack_speed=0.5,
        radius=3.5,
        deploy_time=0,
    ),
    "Fireball": Card(
        name="Fireball",
        cost=4,
        type=CardType.SPELL,
        speed=600,
        count=1,
        attack_type=AttackType.AREA_DAMAGE,
        target_type=TargetType.ALL,
        damage=688,
        crown_tower_damage=159,
        attack_speed=0.5,
        radius=2.5,
        deploy_time=0,
    ),}





"""
class Knight:
    def __init__(self):
        # Basic attributes
        self.name = "Knight"
        self.cost = 3
        self.hp = 1766
        self.speed = 60
        self.count = 1
        self.type = "Troop"
        self.transport = "Ground"

        # Attack
        self.attack_type = "Single Target"
        self.target_type = "Ground"

        self.damage = 202
        self.attack_speed = 1.2
        self.range = 1.2

        # Others
        self.deploy_time = 1.0
        

class Archers:
    def __init__(self):
        # Basic attributes
        self.name = "Archers"
        self.cost = 3
        self.hp = 304
        self.speed = 75
        self.count = 2
        self.transport = "Ground"
        self.type = "Troop"

        # Attack
        self.attack_type = "Single Target"
        self.target_type = "Air, Ground"
        
        self.damage = 112
        self.attack_speed = 0.9
        self.range = 5

        self.projectile_speed = 600

        # Others
        self.deploy_time = 1.0
        

class Minions:
    def __init__(self):
        # Basic attributes
        self.name = "Minions"
        self.cost = 3
        self.hp = 230
        self.count = 3
        self.speed = 90
        self.transport = "Air"
        self.type = "Troop"

        # Attack
        self.attack_type = "Single Target"
        self.target_type = "Air, Ground"
        
        self.damage = 107
        self.attack_speed = 1.2
        self.range = 2.5

        self.projectile_speed = 1000

        # Others
        self.deploy_time = 1.0

class Musketeer:
    def __init__(self):
        # Basic attributes
        self.name = "Musketeer"
        self.cost = 4
        self.hp = 721
        self.speed = 60
        self.count = 1
        self.transport = "Ground"
        self.type = "Troop"

        # Attack
        self.attack_type = "Single Target"
        self.target_type = "Air, Ground"
        
        self.damage = 217
        self.attack_speed = 1
        self.range = 6

        self.projectile_speed = 1000

        # Others
        self.deploy_time = 1.0

class Arrows:
    def __init__(self):
        # Basic attributes
        self.name = "Arrows"
        self.cost = 3
        self.speed = 1100
        self.count = 3
        self.type = "Spell"

        # Attack
        self.attack_type = "Area Damage"
        self.target_type = "Air, Ground"
        
        self.damage = 122
        self.crown_tower_damage = 31
        self.attack_speed = 0.5
        self.radius = 3.5

        # Others
        self.deploy_time = 0

class Fireball:
    def __init__(self):
        # Basic attributes
        self.name = "Fireball"
        self.cost = 4
        self.speed = 600
        self.count = 1
        self.type = "Spell"

        # Attack
        self.attack_type = "Area Damage"
        self.target_type = "Air, Ground"
        
        self.damage = 688
        self.crown_tower_damage = 159
        self.attack_speed = 0.5
        self.radius = 2.5

        # Others
        self.deploy_time = 0

"""