from Utils import *

def only_choice(values):
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
