from isolation import Board
from sample_players import (RandomPlayer, HumanPlayer, GreedyPlayer, center_score, improved_score)
from game_agent import (MinimaxPlayer, AlphaBetaPlayer)

# create an isolation board (by default 7x7)
player1 = MinimaxPlayer()
player2 = GreedyPlayer()
game = Board(player1, player2)


winner, history, outcome = game.play()
print("\nWinner: {}\nOutcome: {}".format(winner, outcome))
print(game.to_string())
print("Move history:\n{!s}".format(history))


"""
import timeit

player1 = AlphaBetaPlayer(score_fn=improved_score, search_depth=1)
player2 = GreedyPlayer()
game = Board(player1, player2, 9, 9)

game._board_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 57]

time_millis = lambda: 1000 * timeit.default_timer()
move_start = time_millis()
time_left = lambda : 1500 - (time_millis() - move_start)

player1.time_left = time_left

moves = []

for a in range(1):
    moves.append(player1.alphabeta(game, 2))

moves.sort()

print(game.to_string())
print(moves)
"""