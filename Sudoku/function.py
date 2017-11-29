from Utils import *

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