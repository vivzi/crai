import crsim.data.CONSTANTS as CONSTANTS
from crsim.engine.player import Player
import math
import time
from crsim.engine.game_state import GameState
from crsim.engine.player import Player
from crsim.engine.arena.arena import Arena

class Game:
    def __init__(self, player1, player2, maxTicks=CONSTANTS.GAME_TICKS):
        self.player1 = player1
        self.player2 = player2
        self.maxTicks = maxTicks
        self.tick = 0
        self.arena = Arena(CONSTANTS.ARENA)

        self.gameState = GameState(self.player1, self.player2, CONSTANTS.GAME_TICKS, self.tick)

        print(self.arena.player1Deployable)
    def step(self):

        # TODO: Implement all dynamic systems change with tick
        if self.tick % 28 == 0:
            amount = 2 if self.tick >= CONSTANTS.DOUBLE_ELIXIR_TICK else 1
            self.player1.elixir = min(CONSTANTS.TOTAL_ELIXIR, self.player1.elixir + amount)
            self.player2.elixir = min(CONSTANTS.TOTAL_ELIXIR, self.player2.elixir + amount)

        self.tick += 1

        return self.gameState.update(self.player1, self.player2, self.tick)

    def run(self):
        try:
            while self.tick < self.maxTicks:
                start = time.monotonic()
                self.step()
                elapsed = time.monotonic() - start
                remaining = CONSTANTS.TIME_PER_TICK - elapsed
                if remaining > 0:
                    time.sleep(remaining)
        finally:
            self.end()

    def end(self):
        print("game over byebye")
        return

if __name__ == "__main__":
    game = Game(Player(CONSTANTS.DECK, 1), Player(CONSTANTS.DECK, 2), CONSTANTS.GAME_TICKS)
    game.run()
    
