# CONSTANTS FOR THE CLASH SIM

import numpy as np

# Grid dimensions
GRID_WIDTH = 18
SIDE_GRID_HEIGHT = 14
TOTAL_GRID_HEIGHT = 30


# Arena
# 0 -> Grass
# 1 -> River
# 2 -> Bridge
# 3 -> Princess Tower
# 4 -> King Tower

ARENA = np.zeros((TOTAL_GRID_HEIGHT, GRID_WIDTH), dtype=np.int8) # initialise a fully grass grid

# River
ARENA[14:16, :] = 1

# Bridges
ARENA[14:16, 3:5] = 2
ARENA[14:16, 14:16] = 2

# Princess Towers
ARENA[4:7, 2:5] = 3
ARENA[4:7, 13:16] = 3
ARENA[23:26, 2:5] = 3
ARENA[23:26, 13:16] = 3

# King Towers
ARENA[0:4, 7:11] = 4
ARENA[26:30, 7:11] = 4

# COORDINATES

BRIDGE_COORDS = [
    [(4, 15), (4, 16)],
    [(15, 15), (15, 16)]
]


TOWER_COORDS = [
    [(x, y) for y in range(5, 8) for x in range(3, 6)],
    [(x, y) for y in range(5, 8) for x in range(14, 17)],
    [(x, y) for y in range(24, 27) for x in range(3, 6)],
    [(x, y) for y in range(24, 27) for x in range(14, 17)]
]

CROWN_TOWER_COORDS = [
    [(x, y) for y in range(1, 5) for x in range(8, 12)],
    [(x, y) for y in range(27, 31) for x in range(8, 12)]
]

# Simulation
GAME_TICKS = 1800
TIME_PER_TICK = 0.1
GAME_DURATION = GAME_TICKS * TIME_PER_TICK
TOWER_HP = 3052
KING_TOWER_HP = 4824


# Combat
TOTAL_ELIXIR = 10
TIME_PER_ELIXIR = 2.8
ELIXIR_2X_TICKS = 600
DOUBLE_ELIXIR_TICK = 1200
TIME_PER_ELIXIR_2X = 1.4
DECK = ["Knight", "Archers", "Minions", "Arrows", "Fireball", "Giant", "Mini P.E.K.K.A", "Musketeer"]

