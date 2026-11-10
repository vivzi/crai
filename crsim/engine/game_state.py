import crsim.data.CONSTANTS as CONSTANTS

class GameState:
    def __init__(self, player1, player2, maxTicks=CONSTANTS.GAME_TICKS, tick=0):
        self.player1 = player1
        self.player2 = player2
        self.maxTicks = maxTicks
        self.tick = tick
        self.gameStatus = "Not Started"

    def update(self, player1, player2, tick):
        self.player1 = player1
        self.player2 = player2
        self.tick = tick

        if self.tick <= 0:
            self.gameStatus = "Not Started"
        elif self.tick >= self.maxTicks:
            self.gameStatus = "Finished"
        elif self.tick >= CONSTANTS.DOUBLE_ELIXIR_TICK:
            self.gameStatus = "2x Elixir"
        else:
            self.gameStatus = "In Progress"

        return self.returnState()

    def returnState(self):
        return [self.player1, self.player2, self.tick, self.gameStatus]