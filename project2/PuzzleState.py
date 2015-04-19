import random
import copy
import math

class PuzzleState:
    matrix = None # this is an integer matrix
    emptyIndex = (0,0)
    originalPlaces = {}
    h = None

    def __init__(self, matrix, emptyIndex = None):
        if emptyIndex == None:
            for i,lst in enumerate(matrix):
                for j,value in enumerate(lst):
                    if value == 0:
                        self.emptyIndex = (i,j)
        else:
            self.emptyIndex = emptyIndex

        self.matrix = matrix
        self.setOriginalPlaces()

    @staticmethod
    def getRandomPuzzleState(n):
        allNumbers = range(0, n*n)
        matrix = []
        emptyIndex = (0,0)
        for i in range(n):
            line = []
            for j in range(n):
                index = random.randint(0, len(allNumbers)-1)
                element = allNumbers[index]

                if element == 0:
                    emptyIndex = (i,j)

                line.append(element)
                del allNumbers[index]
            matrix.append(line)
        return PuzzleState(matrix, emptyIndex)

    @staticmethod
    def getSolvablePuzzleState(n, hardness):
        value = 0
        matrix = []
        for i in range(n):
            temp = []
            for j in range(n):
                temp.append(value)
                value = value + 1
            matrix.append(temp)
        p = PuzzleState(matrix)
        arr = [p]
        for i in range(hardness):
            branches = arr[-1].getBranchPuzzleStates()
            b = random.choice(branches)
            while b in arr:
                b =  random.choice(branches)
            arr.append(b)
        return arr[-1]

    def getBranchPuzzleStates(self):
        rVal = []
        n = len(self.matrix)
        idx = self.emptyIndex

        offsets = [(-1,0),(0,-1),(0,1),(1,0)]
        for offset in offsets:
            temp = (idx[0]+offset[0], idx[1]+offset[1])
            if temp[0] >= 0 and temp[1] >= 0 and temp[0] < n and temp[1] < n:
                newEmptyIndex = copy.deepcopy(temp)
                newMatrix = copy.deepcopy(self.matrix)
                newMatrix[idx[0]][idx[1]] = newMatrix[temp[0]][temp[1]]
                newMatrix[temp[0]][temp[1]] = 0
                rVal.append(PuzzleState(newMatrix, newEmptyIndex))
        return rVal

    def isSolved(self):
        n = len(self.matrix)
        value = 0
        for i in range(n):
            for j in range(n):
                if self.matrix[i][j] == value:
                    pass
                else:
                    return False
                value = value + 1
        return True

    def getCost(self):
        misplaced = 0
        Manhattan_distance = 0
        Goal3d = ([0,1,2],[3,4,5],[6,7,8])
        Goal4d = ([0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15])
        coordinate_dict = {}
        coordinate_dict1 = {}
        if len(self.matrix)==3:
            for x,row in enumerate(Goal3d):
                for y,value in enumerate(row):
                    coordinate_dict[value]= (x,y)
            for x,row in enumerate(self.matrix):
                for y,value in enumerate(row):
                    if self.matrix[x][y]!= Goal3d[x][y]:
                        misplaced+=1
                    coordinate_dict1[value]= (x,y)
        else:
            for x,row in enumerate(Goal4d):
                for y,value in enumerate(row):
                    coordinate_dict[value]= (x,y)
            for x,row in enumerate(self.matrix):
                for y,value in enumerate(row):
                    if self.matrix[x][y]!= Goal4d[x][y]:
                        misplaced+=1
                    coordinate_dict1[value]= (x,y)
        del coordinate_dict[0]
        del coordinate_dict1[0]
        if len(self.matrix)==3:
            for i in range(1,9):
                x1,y1 = coordinate_dict[i]
                x2,y2 = coordinate_dict1[i]
                Manhattan_distance+=abs(x1-x2)+abs(y1-y2)
        else:
            for i in range(1,16):
                x1,y1 = coordinate_dict[i]
                x2,y2 = coordinate_dict1[i]
                Manhattan_distance+=abs(x1-x2)+abs(y1-y2)
        h1 =  misplaced-1
        h2 = Manhattan_distance
        sum_h1_h2 = h1 + h2 #It is eithe we can return the sum of h1+h2, or h1 alone, or h2. h2 has the lowest level. while h1 has the lowest total number of visited nodes.
        return h1, h2


    def __lt__(self, other):
        return self.getCost() < other.getCost()

    def __eq__(self, other):
        return self.matrix == other.matrix

    def __hash__(self):
        return hash(str(self.matrix))

    def __str__(self):
        rVal = str(self.emptyIndex) + '\n'
        for line in self.matrix:
            rVal += str(line) + '\n'
        return rVal[:-1]

    def setOriginalPlaces(self):
        n = len(self.matrix)
        temp = 0
        for i in range(n):
            for j in range(n):
                self.originalPlaces[temp] = (i,j)
                temp = temp + 1




# p = PuzzleState([[1,0,2],[3,4,5],[6,7,8]])#misplaced is 1 $ distance is 1
# p1 = PuzzleState([[8,3,4],[7,5,0],[1,6,2]]) #misplaced is 8 $ distance is 17
#p3 = PuzzleState([[7,2,4],[5,0,6],[8,3,1]]) #misplaced is 8 $ distance is 18
# p4 = PuzzleState([[1, 5, 6, 2],[9, 8, 4, 3],[12, 14, 7, 13],[15, 0, 10, 11]])
#suma, h1,h2 = p3.getCost()
# print p1.getCost()
# print p4.getCost()
