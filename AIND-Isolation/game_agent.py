"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random


class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass


def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!
    return weighted_chances_heuristic(game, player)


def custom_score_2(game, player):
    return my_moves_heuristic(game, player)


def custom_score_3(game, player):
    return my_moves_heuristic(game, player)


def my_moves_heuristic(game, player):
    return len(game.get_legal_moves(player))

def weighted_chances_heuristic(game, player):
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    myMoves = len(game.get_legal_moves(player))
    opponentMoves = len(game.get_legal_moves(game.get_opponent(player)))

    return (1.5 * myMoves * myMoves) - (opponentMoves * opponentMoves)

def aggressive_heuristic(game, player):
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    myMoves = len(game.get_legal_moves(player))
    opponentMoves = len(game.get_legal_moves(game.get_opponent(player)))

    return myMoves - 1.5 * opponentMoves


class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    ********************  DO NOT MODIFY THIS CLASS  ********************

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout


class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************

        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            return self.minimax(game, self.search_depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    def minimax(self, game, depth):
        """Implement depth-limited minimax search algorithm as described in
        the lectures.

        This should be a modified version of MINIMAX-DECISION in the AIMA text.
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        bestScore = float("-inf")
        bestMove = None

        # Loop through each possible move for this game state.
        for move in game.get_legal_moves():
            value = self.min_value(game.forecast_move(move), depth - 1)

            # Select the best possible move
            if value > bestScore:
                bestScore = value
                bestMove = move

        return bestMove


    def terminal_test(self, gameState):
        """ Return True if the game is over for the active player
        and False otherwise.
        """
        return len(gameState.get_legal_moves()) == 0


    def min_value(self, gameState, depth):
        """ Return the value for a win (+1) if the game is over,
        otherwise return the minimum value over all legal child
        nodes.
        """

        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        # Check for a termainal state
        if self.terminal_test(gameState) or depth == 0:
            return self.score(gameState, gameState.active_player)

        # Preset to highest possible number as we are looking for the lowest possible number
        value = float("inf")

        # Test each available move
        for move in gameState.get_legal_moves():
            value = min(value, self.max_value(gameState.forecast_move(move), depth - 1))

        return value


    def max_value(self, gameState, depth):
        """ Return the value for a loss (-1) if the game is over,
        otherwise return the maximum value over all legal child
        nodes.
        """

        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        # Check for a termainal state
        if self.terminal_test(gameState) or depth == 0:
            return self.score(gameState, gameState.active_player)

        # Preset to lowest possible number as we are looking for the highest possible number
        value = float("-inf")

        # Test each available move
        for move in gameState.get_legal_moves():
            value = max(value, self.min_value(gameState.forecast_move(move), depth - 1))

        return value


class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.

        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            for depth in range(1, game.width * game.height):
                    best_move = self.alphabeta(game, depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        if best_move == (-1, -1) and len(game.get_legal_moves()) > 0:
            best_move = game.get_legal_moves[random.randint(0, len(game.get_legal_moves) - 1)]

        # Return the best move from the last completed search iteration
        return best_move


    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.

        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        bestScore = float("-inf")
        bestMove = None

        # Loop through each possible move for this game state.
        for move in game.get_legal_moves():
            value = self.min_value(game.forecast_move(move), depth - 1, alpha, beta)

            # Select the best possible move
            if value > bestScore:
                bestScore = value
                bestMove = move

        return bestMove

    def terminal_test(self, gameState):
        """ Return True if the game is over for the active player
        and False otherwise.
        """
        return len(gameState.get_legal_moves()) == 0

    def min_value(self, gameState, depth, alpha, beta):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        
        # Check for a termainal state
        if self.terminal_test(gameState) or depth == 0:
            return self.score(gameState, gameState.active_player)

        # Preset to highest possible number as we are looking for the lowest possible number
        value = float("inf")

        # Test each available move
        for move in gameState.get_legal_moves():
            value = min(value, self.max_value(gameState.forecast_move(move), depth - 1, alpha, beta))
            
            if value <= alpha:
                return value

            beta = min(value, beta)

        return value

    
    def max_value(self, gameState, depth, alpha, beta):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        # Check for a termainal state
        if self.terminal_test(gameState) or depth == 0:
            return self.score(gameState, gameState.active_player)

        # Preset to lowest possible number as we are looking for the highest possible number
        value = float("-inf")

        # Test each available move
        for move in gameState.get_legal_moves():
            value = max(value, self.min_value(gameState.forecast_move(move), depth - 1, alpha, beta))

            if value >= beta:
                return value

            alpha = max(value, alpha)

        return value


