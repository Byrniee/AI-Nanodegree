from utils import *

def search(values):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)

    if values == False:
        return False
    
    if all(len(values[s]) == 1 for s in boxes): 
        return values 

    # Choose one of the unfilled squares with the fewest possibilities
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)

    # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
    for value in values[s]:
        newSudoku = values.copy()
        newSudoku[s] = value
        attempt = search(newSudoku)

        if attempt:
            return attempt