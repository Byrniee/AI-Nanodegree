rows = 'ABCDEFGHI'
cols = '123456789'


boxes = cross(rows, cols)

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
unitlist = row_units + column_units + square_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)


def cross(a, b):
    return [s+t for s in a for t in b]


def onlyChoice(values):
    """Finalize all values that are the only choice for a unit.

    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """
    
    # All the posible didgets in the sudoku
    allDidgets = "123456789"

    # Loop through each unit in the puzzel
    for unit in unitlist:
        # Loop through each didget in all possible didgets
        for didget in allDidgets:
            # This list will contain each box occurance in the unit of the didget
            didgetOccurencesInUnit = []

            # Add each occurance of the didget to the list
            for box in unit:
                if didget in values[box]:
                    didgetOccurencesInUnit.append(box)
            
            # if the didget only occues once, set that box to the didget
            if len(didgetOccurencesInUnit) == 1:
                values[didgetOccurencesInUnit[0]] = didget

    return values


def eliminate(values):
    """Eliminate values from peers of each box with a single value.

    Go through all the boxes, and whenever there is a box with a single value,
    eliminate this value from the set of values of all its peers.

    Args:
        values: Sudoku in dictionary form.
    Returns:
        Resulting Sudoku in dictionary form after eliminating values.

    """
    # find all of the boxes which only have 1 number in them
    solvedValues = []

    # find all of the boxes which only have 1 number in them
    for box in values.keys():
        if len(values[box]) == 1:
            solvedValues.append(box)

    # loop through each solved box and remove the solved didget from its peers
    for box in solvedValues:
        solvedDidgit = values[box]

        # loop through this boxes peers and remove the solved didget
        for peer in peers[box]:
            values[peer] = values[peer].replace(solvedDidgit, '')

    return values


def grid_values(grid):
    """Convert grid string into {<box>: <value>} dict with '123456789' value for empties.

    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '123456789' if it is empty.
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


def display(values):
    """
    Display the values as a 2-D grid.
    Input: The sudoku in dictionary form
    Output: None
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '') for c in cols))
        if r in 'CF': print(line)
    return