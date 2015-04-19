from Grid import *
from Stack import *
import sys

class DFSSolver:
    @staticmethod
    def solve(initialState):
        frontier = Stack()
        frontier.push(initialState)
        visited = {initialState}
        totalVisited = 0

        while not frontier.isEmpty():
            totalVisited = totalVisited + 1
            selected = frontier.pop()
            if selected.isSolved():
                print('success')
                print('total visited: ' + str(totalVisited))
                return selected
            branches = selected.getBranches()
            #branches = selected.getRandomBranches()
            for b in branches:
                if b not in visited:
                    visited.add(b)
                    if not b.hasContradiction():
                        frontier.push(b)

        print('no solution. :(')
        print('total visited: ' + str(totalVisited))
