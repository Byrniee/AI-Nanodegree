from isolation import Board
from sample_players import (RandomPlayer, HumanPlayer)
from game_agent import (MinimaxPlayer, AlphaBetaPlayer)

# create an isolation board (by default 7x7)
player1 = RandomPlayer()
player2 = MinimaxPlayer()
game = Board(player1, player2)

winner, history, outcome = game.play()
print("\nWinner: {}\nOutcome: {}".format(winner, outcome))
print(game.to_string())
print("Move history:\n{!s}".format(history))