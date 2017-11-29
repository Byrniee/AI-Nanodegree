from utils import *

def reduce_puzzle(values):
    stalled = False
    
    while not stalled:
        # Check how many boxes have a determined value
        solvedValuesBefore = len([box for box in values.keys() if len(values[box]) == 1])

        # Your code here: Use the Eliminate Strategy
        values = eliminate(values)

        # Your code here: Use the Only Choice Strategy
        values = onlyChoice(values)

        # Check how many boxes have a determined value, to compare
        solvedValuesAfter = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solvedValuesBefore == solvedValuesAfter
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False

    return values
