from utils import *

grid1 = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
grid2 = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
grid3 = '.................................................................................'

print("\n")

values = grid_values(grid1)
display(values)

print("\n")

values = reduce_puzzle(values)
display(values)


print("\n")
print("\n")

values = grid_values(grid2)
display(values)

print("\n")
print("\n")

values = grid_values(grid3)
display(values)

print("\n")

values = search(values)
display(values)