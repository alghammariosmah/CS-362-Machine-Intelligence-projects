from Grid import *
from DFSSolver import *
import os

grids = Grid.getGrids('hard.txt') # gets all sudoku grids from the given file as a list

#grid = Grid.getRandomGrid('easy.txt')
#grid = Grid('...7..8....6....31.4...2....24.7.....1..3..8.....6.29....8...7.86....5....2..6...') #easy
#grid = Grid('4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......') #hard


os.system('cls')

for grid in grids:
    print grid
    print '---'
    solution = DFSSolver.solve(grid)
    print solution
    print '---'
    raw_input('Press enter for the next...')
    os.system('cls')
