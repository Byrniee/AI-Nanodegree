from Utils import *

def grid_values(grid):
    """Convert grid string into {<box>: <value>} dict with '.' value for empties.

    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '.' if it is empty.
    """

    possibleValues = []
    everyPossibleValue = '123456789'

    for c in grid:
        if c == '.':
            possibleValues.append(everyPossibleValue)
        else:
            possibleValues.append(c)
    
    assert len(possibleValues) == 81
    return dict(zip(boxes, possibleValues))
