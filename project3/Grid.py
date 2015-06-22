import random
import copy
import operator
import sys

class Grid:
    """
    This matrix stores the values in the grid. None is used for empty cells.

    Example grid:

        . 2 . | 8 1 . | 7 4 .
        7 . . | . . 3 | 1 . .
        . 9 . | . . 2 | 8 . 5
        ---------------------
        . . 9 | . 4 . | . 8 7
        4 . . | 2 . 8 | . . 3
        1 6 . | . 3 . | 2 . .
        ---------------------
        3 . 2 | 7 . . | . 6 .
        . . 5 | 6 . . | . . 8
        . 7 6 | . 5 1 | . 9 .

    self.matrix:

        [[None, 2, None, 8, 1, None, 7, 4, None],
         [7, None, None, None, None, 3, 1, None, None],
         [None, 9, None, None, None, 2, 8, None, 5],
         [None, None, 9, None, 4, None, None, 8, 7],
         [4, None, None, 2, None, 8, None, None, 3],
         [1, 6, None, None, 3, None, 2, None, None],
         [3, None, 2, 7, None, None, None, 6, None],
         [None, None, 5, 6, None, None, None, None, 8],
         [None, 7, 6, None, 5, 1, None, 9, None]]

    """
    matrix = []

    boxCorners = [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]

    def __init__(self, matrix):
        if isinstance(matrix, basestring):
            self.matrix = Grid.stringToMatrix(matrix)
        else:
            self.matrix = matrix

    """
    This function should pick the most constrained cell, i.e., the cell which has
    the minimum number of possible values, and return list of grids with these
    possible values in the chosen cell.
    NOTE: Please use fill() after you create the grid to fill one-probability cells.
    Check getRandomBranches() function, your function should look similar with it.
    """
    def getBranches(self):
        tempt= []
        d = {}
        for i in range(9):
            for j in range(9):
                if self.matrix[i][j]==None:
                    tempt.append((i,j))
        for node in tempt:
            possibleValues = self.getPossibles(node[0],node[1])
            d.setdefault(node,possibleValues)
        dd=sorted(d, key=lambda k: len(d[k]))
        for n in dd:
            rVal = []
            possibleValues1 = self.getPossibles(n[0],n[1])
            for value in possibleValues1:
                temp = copy.deepcopy(self.matrix)
                temp[n[0]][n[1]] = value
                grid = Grid(temp)
                grid.fill()
                rVal.append(grid)
            return rVal


    """
    Picks a random empty cell and returns branch (child) grids with all possible values
    for the chosen cell. (Returns list of grids.)
    """
    def getRandomBranches(self):
        rVal = []
        randomEmpty = self.getRandomEmptyCell()
        possibleValues = self.getPossibles(randomEmpty[0], randomEmpty[1])
        for value in possibleValues:
            temp = copy.deepcopy(self.matrix)
            temp[randomEmpty[0]][randomEmpty[1]] = value
            grid = Grid(temp)
            grid.fill()
            rVal.append(grid)
        return rVal

    """
    Returns a random empty cell index as a tuple.
    """
    def getRandomEmptyCell(self):
        temp = []
        for i in range(9):
            for j in range(9):
                if self.matrix[i][j] == None:
                    temp.append( (i,j) )
        return random.choice(temp)

    """
    Check if the grid is a sudoku solution.
    """
    def isSolved(self):
        if self.hasContradiction():
            return False
        for i in range(9):
            if None in self.matrix[i]:
                return False
        return True

    """
    Fills out a cell if and only if that cell can take only one value.
    *Does not* return a new grid, updates the grid.
    Does this iteratively until no cell gets updated.
    """
    def fill(self):
        changed = True
        while(changed):
            changed = False
            for i in range(9):
                for j in range(9):
                    if self.matrix[i][j] == None:
                        possibles = self.getPossibles(i,j)
                        if len(possibles) == 1:
                            self.matrix[i][j] = possibles.pop()
                            changed = True

    """
    Returns true if there is not a *contradiction* in the grid.
    Contradiction occurs if and only if:
    1. There is a a duplicate element in any of row/column/box
    2. If a cell cannot take any value because of the row/column/box constraints
    """
    def hasContradiction(self):
        for i in range(9): #check rows
            temp = set()
            for j in range(9):
                if self.matrix[i][j] != None:
                    if self.matrix[i][j] in temp:
                        return True
                    else:
                        temp.add(self.matrix[i][j])

        for i in range(9): #check cols
            temp = set()
            for j in range(9):
                if self.matrix[j][i] != None:
                    if self.matrix[j][i] in temp:
                        return True
                    else:
                        temp.add(self.matrix[j][i])

        for corner in self.boxCorners: #check boxes
            temp = set()
            for i in range(corner[0],corner[0]+3):
                for j in range(corner[1],corner[1]+3):
                    if self.matrix[i][j] != None:
                        if self.matrix[i][j] in temp:
                            return True
                        else:
                            temp.add(self.matrix[i][j])

        for i in range(9):
            for j in range(9):
                if self.matrix[i][j] == None:
                    if len(self.getPossibles(i,j)) == 0:
                        return True

        return False

    """
    Returns a set of possible values for given cell (r,c).
    Note: Please only use for the 'None' cells.

    If you have the following grid:

        . . . | 7 . . | 8 . .
        . . 6 | . . . | . 3 1
        . 4 . | . . 2 | . . .
        ---------------------
        . 2 4 | . 7 . | . . .
        . 1 . | . 3 . | . 8 .
        . . . | . 6 . | 2 9 .
        ---------------------
        . . . | 8 . . | . 7 .
        8 6 . | . . . | 5 . .
        . . 2 | . . 6 | . . .

    self.getPossibles(0,0) will return

        set([1, 2, 3, 5, 9])

    """
    def getPossibles(self, r, c):
        rVal = set([1,2,3,4,5,6,7,8,9])
        for i in range(9):
            if self.matrix[r][i] != None:
                if self.matrix[r][i] in rVal:
                    rVal.remove(self.matrix[r][i])
            if self.matrix[i][c] != None:
                if self.matrix[i][c] in rVal:
                    rVal.remove(self.matrix[i][c])

        boxCornerR = r - (r%3)
        boxCornerC = c - (c%3)

        for i in range(boxCornerR, boxCornerR+3):
            for j in range(boxCornerC, boxCornerC+3):
                if self.matrix[i][j] != None:
                    if self.matrix[i][j] in rVal:
                        rVal.remove(self.matrix[i][j])
        return rVal

    """
    Converts a line in easy.txt or hard.txt to a python matrix.
    An example line:

        ...9....2.5.1234...3....16.9.8.......7.....9.......2.5.91....5...7439.2.4....7...

    """
    @staticmethod
    def stringToMatrix(line):
        matrix = []
        for i in range(9):
            temp = []
            for j in range(9):
                index = i * 9 + j
                if line[index] == '.':
                    temp.append(None)
                else:
                    temp.append(int(line[index]))
            matrix.append(temp)
        return matrix

    """
    Function to read all sudoku grids in a file,
    check easy.txt and hard.txt for more information.
    """
    @staticmethod
    def getGrids(path):
        rVal = []
        f = open(path)
        lines = f.readlines()
        for line in lines:
            rVal.append(Grid(line.strip()))
        return rVal

    """
    Returns a random grid from the given file.
    Check easy.txt and hard.txt for file structure.
    """
    @staticmethod
    def getRandomGrid(path):
        return random.choice(Grid.getGrids(path))


    """
    Converts grid to string in the following format:

        1 3 7 | 2 5 6 | 8 4 9
        9 2 8 | 3 1 4 | 5 6 7
        4 6 5 | 8 9 7 | 3 1 2
        ---------------------
        6 7 3 | 5 4 2 | 9 8 1
        8 1 9 | 6 7 3 | 2 5 4
        5 4 2 | 1 8 9 | 7 3 6
        ---------------------
        2 5 6 | 7 3 1 | 4 9 8
        3 9 1 | 4 2 8 | 6 7 5
        7 8 4 | 9 6 5 | 1 2 3
    """
    def __str__(self):
        rVal = ''
        for i in range(9):
            if i > 0 and i % 3 == 0:
                rVal += 21*'-' + '\n'
            for j in range(9):
                if j > 0 and j % 3 == 0:
                    rVal += '| '
                if self.matrix[i][j] == None:
                    rVal += '. '
                else:
                    rVal += str(self.matrix[i][j]) + ' '
            if i != 8:
                rVal += '\n'
        return rVal



