import crsim.data.CONSTANTS as CONSTANTS
import numpy as np


class Arena:
    def __init__(self, map=CONSTANTS.ARENA):
        self.map = map

        self.deployable = np.argwhere(map == 0)[:, ::-1] + 1
        self.player1Deployable = np.argwhere(map[:14, :] == 0)[:, ::-1] + 1
        self.player2Deployable = np.argwhere(map[16:, :] == 0)[:, ::-1] + 1
        self.player2Deployable[:, 1] += 16