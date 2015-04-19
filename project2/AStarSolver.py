import operator
import bisect
from PuzzleState import *
from Parameters import *
import sys
import matplotlib.pyplot as plt

class AStarSolver:
    @staticmethod
    def solve(initialState):
        solution = AStarSolver.astar(initialState)
        if solution is None:
            return None
        arr = [solution]
        while solution.parent is not None:
            solution = solution.parent
            arr.append(solution)
        reversedArr = arr[::-1]
        return reversedArr

    @staticmethod
    def astar(initialState):
        frontier = [initialState]
        initialState.parent = None
        initialState.level = 0
        visited = {initialState}
        totalVisited = 0
        totalVisited_List = []
        selected_Level_List = []
        frontier_Length_List = []
        while frontier:
            totalVisited = totalVisited + 1
            totalVisited_List.append(totalVisited)
            selected = frontier[0]
            if DEBUG:
                print('level: ' + str(selected.level) + ',totalVisited: ' + str(totalVisited) + ',len(frontier): ' + str(len(frontier)))
                selected_Level_List.append(int(selected.level))
                frontier_Length_List.append(int(len(frontier)))
                sys.stdout.flush()
            del frontier[0]
            if selected.isSolved():
                # plt.plot(totalVisited_List,selected_Level_List)
                # plt.xlabel('Total Unique Visited Nodes')
                # plt.ylabel('Level Depth')
                # plt.title('A* Algorithm with the Hard case')
                # plt.show()
                print('success')
                print('Level: ' + str(selected.level))
                print('Total visited: ' + str(totalVisited))
                return selected
            branches = selected.getBranchPuzzleStates()
            for b in branches:
                if b not in visited:
                    visited.add(b)
                    b.parent = selected
                    b.level = selected.level + 1
                    #frontier.append(b) # If I append the frontier with b, it will be a longer answer. The Selected level will be more and the total visited will be more too.
                    bisect.insort(frontier,b)
        print('no solution. :(')
        print('Total visited: ' + str(totalVisited))


# p = PuzzleState([[0,1,2],[3,4,5],[6,7,8]])
# p1 = PuzzleState([[8,3,4],[7,5,0],[1,6,2]]) # moderateCase
# AStarSolver.solve(p1)




