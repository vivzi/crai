from enum import Enum, auto

class CardType(Enum):
    TROOP = auto()
    SPELL = auto()

class Transport(Enum):
    GROUND = auto()
    AIR = auto()

class AttackType(Enum):
    SINGLE_TARGET = auto()
    AREA_DAMAGE = auto()

class TargetType(Enum):
    GROUND = auto()
    AIR = auto()
    BUILDINGS = auto()
    ALL = auto()

class DeployMessage(Enum):
    NO_ELIXIR = auto()
    NOT_IN_HAND = auto()
    INVALID_ZONE = auto()
    OK = auto()