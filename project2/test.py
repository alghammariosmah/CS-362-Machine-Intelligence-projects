from PuzzleState import *
from Visualizer import *
from BFSSolver import *
from DFSSolver import *
from AStarSolver import *

print('hello..')

start_time = time.time()

#p = PuzzleState.getRandomPuzzleState(4)
#p = PuzzleState.getSolvablePuzzleState(3, 30)
#p = PuzzleState([[1,0,2],[3,4,5],[6,7,8]]) # easyCase
p = PuzzleState([[8,3,4],[7,5,0],[1,6,2]]) # moderateCase
#p = PuzzleState([[1, 5, 6, 2],[9, 8, 4, 3],[12, 14, 7, 13],[15, 0, 10, 11]]) # hardCase
#p = PuzzleState([[0,2,1],[3,4,5],[6,7,8]]) # no solution :(




#print('---')
#branches = p.getBranchPuzzleStates()
#for b in branches:
#	print(b)
#	print('-')

#print(p.getCost())

#arr = BFSSolver.solve(p)
arr = DFSSolver.solve(p)
# arr = AStarSolver.solve(p)
#arr = Iterative_DFSSolver(p)


print time.time() - start_time, "seconds"
print('bye ..')



if arr is not None:
    Visualizer(arr)

