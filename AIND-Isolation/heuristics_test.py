"""Estimate the strength rating of a student defined heuristic by competing
against fixed-depth minimax and alpha-beta search agents in a round-robin
tournament.

NOTE: All agents are constructed from the student CustomPlayer implementation,
so any errors present in that class will affect the outcome.

The student agent plays a number of "fair" matches against each test agent.
The matches are fair because the board is initialized randomly for both
players, and the players play each match twice -- once as the first player and
once as the second player.  Randomizing the openings and switching the player
order corrects for imbalances due to both starting position and initiative.
"""
import itertools
import random
import warnings

from collections import namedtuple

from isolation import Board
from sample_players import (RandomPlayer, open_move_score,
                            improved_score, center_score)
from game_agent import (MinimaxPlayer, AlphaBetaPlayer, my_moves_heuristic,
                        maximise_player_moves, minimise_opponent_moves,
                        maximise_ratio_of_player_to_opponent_moves,
                        minimise_ratio_of_player_to_opponent_moves)

NUM_MATCHES = 25  # number of matches against each opponent
TIME_LIMIT = 150  # number of milliseconds before timeout

DESCRIPTION = """
This script evaluates the performance of the custom_score evaluation
function against a baseline agent using alpha-beta search and iterative
deepening (ID) called `AB_Improved`. The three `AB_Custom` agents use
ID and alpha-beta search with the custom_score functions defined in
game_agent.py.
"""

Agent = namedtuple("Agent", ["player", "name"])


def play_match(player1, player2):
    """
    Play a "fair" set of matches between two agents by playing two games
    between the players, forcing each agent to play from randomly selected
    positions. This should control for differences in outcome resulting from
    advantage due to starting position on the board.
    """
    num_wins = {player1: 0, player2: 0}
    num_timeouts = {player1: 0, player2: 0}
    num_invalid_moves = {player1: 0, player2: 0}
    games = [Board(player1, player2), Board(player2, player1)]

    # initialize both games with a random move and response
    for _ in range(2):
        move = random.choice(games[0].get_legal_moves())
        games[0].apply_move(move)
        games[1].apply_move(move)

    # play both games and tally the results
    for game in games:
        winner, _, termination = game.play(time_limit=TIME_LIMIT)

        if player1 == winner:
            num_wins[player1] += 1

            if termination == "timeout":
                num_timeouts[player2] += 1
            else:
                num_invalid_moves[player2] += 1

        elif player2 == winner:

            num_wins[player2] += 1

            if termination == "timeout":
                num_timeouts[player1] += 1
            else:
                num_invalid_moves[player1] += 1

    if sum(num_timeouts.values()) != 0:
        warnings.warn(TIMEOUT_WARNING)

    return num_wins[player1], num_wins[player2]


def update(total_wins, wins):
    for player in total_wins:
        total_wins[player] += wins[player]
    return total_wins


def play_matches(cpu_agents, test_agents, num_matches):
    
    for testAgent in test_agents:
        print("*************************")
        print("Test: " + testAgent.name)
        print("*************************")
        print()
        print("Playing Matches:")
        print("----------------")
        print()

        wins = 0.
        total = 0.

        for index, cpuAgent in enumerate(cpu_agents[:-1]):
            print("  Match {}: {!s:^45} vs {!s:^11}".format(index + 1, testAgent.name, cpuAgent.name), end=' ')

            counts = {testAgent.player: 0., cpuAgent.player: 0.}

            # Each player takes a turn going first
            for p1, p2 in itertools.permutations((testAgent.player, cpuAgent.player)):
                for a in range(num_matches):
                    score_1, score_2 = play_match(p1, p2)
                    counts[p1] += score_1
                    counts[p2] += score_2
                    total += score_1 + score_2

            wins += counts[testAgent.player]

            print("\tResult: {} to {}".format(int(counts[testAgent.player]), int(counts[cpuAgent.player])))

        win_ratio = 100. * wins / total

        print("\n\nResults:")
        print("----------")
        print("{!s:<15}{:>10.2f}%".format(testAgent.name, win_ratio))
        print()


def main():

    # Define two agents to compare -- these agents will play from the same
    # starting position against the same adversaries in the tournament
    test_agents = [
        Agent(AlphaBetaPlayer(score_fn=improved_score), "AB_Improved"),
        Agent(AlphaBetaPlayer(score_fn=my_moves_heuristic), "my_moves_heuristic"),
        Agent(AlphaBetaPlayer(score_fn=maximise_player_moves), "maximise_player_moves"),
        Agent(AlphaBetaPlayer(score_fn=minimise_opponent_moves), "minimise_opponent_moves"),
        Agent(AlphaBetaPlayer(score_fn=maximise_ratio_of_player_to_opponent_moves), "maximise_ratio_of_player_to_opponent_moves"),
        Agent(AlphaBetaPlayer(score_fn=minimise_ratio_of_player_to_opponent_moves), "minimise_ratio_of_player_to_opponent_moves")
    ]

    # Define a collection of agents to compete against the test agents
    cpu_agents = [
        Agent(RandomPlayer(), "Random"),
        Agent(MinimaxPlayer(score_fn=open_move_score), "MM_Open"),
        Agent(MinimaxPlayer(score_fn=center_score), "MM_Center"),
        Agent(MinimaxPlayer(score_fn=improved_score), "MM_Improved"),
        Agent(AlphaBetaPlayer(score_fn=open_move_score), "AB_Open"),
        Agent(AlphaBetaPlayer(score_fn=center_score), "AB_Center"),
        Agent(AlphaBetaPlayer(score_fn=improved_score), "AB_Improved")
    ]

    print(DESCRIPTION)
    print("{:^74}".format("*************************"))
    print("{:^74}".format("Playing Matches"))
    print("{:^74}".format("*************************"))
    print()
    play_matches(cpu_agents, test_agents, NUM_MATCHES)


if __name__ == "__main__":
    main()
