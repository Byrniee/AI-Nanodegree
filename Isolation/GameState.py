from copy import deepcopy

xSize = 3
ySize = 2

class GameState:

    # Player 0 is the AI.
    # Player 1 is the Human.

    # board - list
    # The board state. 2D array, accessed board[y][x]
    
    # playerLocations - List of touple
    # The current location of each player. 
    # [(0, 0), (0, 1)] where playerLocations[0] is player 0
    
    # currentPlayer - int
    # The current players turn


    def __init__(self):
        self.board = [[0 for x in range(xSize)] for y in range(ySize)]
        self.board[1][2] = 1

        self.playerLocations = [None, None]
        self.currentPlayer = 0

        print(self.board)

    
    def forecast_move(self, move):
        """ Return a new board object with the specified move
        applied to the current game state.
        
        Parameters
        ----------
        move: tuple
            The target position for the active player's next move (x, y)
        """
        if move not in self.get_legal_moves():
            return False

        newGameState = deepcopy(self)
        newGameState.board[move[1]][move[0]] = 1 # Set the box to taken
        newGameState.playerLocations[newGameState.currentPlayer] = move
        newGameState.currentPlayer = 1 - newGameState.currentPlayer # Flip the play

        return newGameState


    
    def get_legal_moves(self):
        """ Return a list of all legal moves available to the
        active player.  Each player should get a list of all
        empty spaces on the board on their first move, and
        otherwise they should get a list of all open spaces
        in a straight line along any row, column or diagonal
        from their current position. (Players CANNOT move
        through obstacles or blocked squares.) Moves should
        be a pair of integers in (column, row) order specifying
        the zero-indexed coordinates on the board.
        """
        
        emptyBoxes = [(x, y) for y in range(ySize) for x in range(xSize) if self.board[y][x] == 0]

        # Check for first turn
        if self.playerLocations[self.currentPlayer] == None:
            return emptyBoxes

        moves = []
        rays = [(1, 0), (1, -1), (0, -1), (-1, -1),
                (-1, 0), (-1, 1), (0, 1), (1, 1)]

        for deltaX, deltaY in rays:
            x = self.playerLocations[self.currentPlayer][1]
            y = self.playerLocations[self.currentPlayer][0]

            while 0 <= x + deltaX < xSize and 0 <= y + deltaY < ySize:
                x += deltaX
                y += deltaY

                if self.board[y][x] == 1:
                    break

                moves.append((x, y))

        return moves
        