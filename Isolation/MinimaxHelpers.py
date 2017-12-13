from GameState import *

def terminal_test(gameState):
    """ Return True if the game is over for the active player
    and False otherwise.
    """
    return len(gameState.get_legal_moves()) == 0


def min_value(gameState):
    """ Return the value for a win (+1) if the game is over,
    otherwise return the minimum value over all legal child
    nodes.
    """
    if terminal_test(gameState):
        return 1

    # Preset to highest possible number as we are looking for the lowest possible number
    value = float("inf")

    # Test each available move
    for move in gameState.get_legal_moves():
        value = min(value, max_value(gameState.forecast_move(move)))

    return value


def max_value(gameState):
    """ Return the value for a loss (-1) if the game is over,
    otherwise return the maximum value over all legal child
    nodes.
    """
    # Check for a termainal state
    if terminal_test(gameState):
        return -1

    # Preset to lowest possible number as we are looking for the highest possible number
    value = float("-inf")

    # Test each available move
    for move in gameState.get_legal_moves():
        value = max(value, min_value(gameState.forecast_move(move)))

    return value