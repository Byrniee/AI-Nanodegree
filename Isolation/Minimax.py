from MinimaxHelpers import *


def minimax_decision(gameState):
    """ Return the move along a branch of the game tree that
    has the best possible value.  A move is a pair of coordinates
    in (column, row) order corresponding to a legal move for
    the searching player.
    
    You can ignore the special case of calling this function
    from a terminal state.
    """
    
    # Preset to lowest possible number
    bestScore = float("-inf")
    bestMove = None

    # Loop through each possible move for this game state.
    for move in gameState.get_legal_moves():
        value = min_value(gameState.forecast_move(move))

        # Select the best possible move
        if value > bestScore:
            bestScore = value
            bestMove = move

    return bestMove