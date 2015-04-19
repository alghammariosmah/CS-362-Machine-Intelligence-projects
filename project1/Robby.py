import random
from enum import *
from Parameters import *

def getIndex(current, north, east, south, west):
    return current + 3 * north + 3**2 * east + 3**3 * south + 3**4 * west

def getRandomMoveAction():
    temp = [ACTIONS.MOVE_NORTH, ACTIONS.MOVE_EAST, ACTIONS.MOVE_SOUTH, ACTIONS.MOVE_WEST]
    return random.choice(temp)

def getRandomAction():
    temp = [ACTIONS.MOVE_NORTH, ACTIONS.MOVE_EAST, ACTIONS.MOVE_SOUTH, ACTIONS.MOVE_WEST, ACTIONS.MOVE_RANDOM, ACTIONS.STAY_PUT, ACTIONS.PICK_UP_CAN]
    return random.choice(temp)

class Robby:
    gene = [] # length should be 3^5
    grid = None
    positionR = 1
    positionC = 1
    moveCount = 0

    def __init__(self, gene):
        self.gene = gene

    def setGrid(self, grid):
        self.grid = grid

    def clean(self):
        self.grid = None
        self.positionR = 1
        self.positionC = 1
        self.moveCount = 0

    def getR(self):
        return self.positionR

    def getC(self):
        return self.positionC

    @staticmethod
    # (TODO #0)
    # Creates a random robot by creating a random DNA sequence: 1D array of 3**5 actions
    def getRandomRobby():
        gene_list = [0,1,2,3,4,5,6]
        rVal = []
        actionslength = 3**5
        for i in range(actionslength):
            c = random.choice(gene_list)
            rVal.append(c)# appending the empty list with the random gene values
        return Robby(rVal) # it returns Robby with a variable.

    @staticmethod
    def getRobbyFromFile(fileName):
        file = open(fileName, "r")
        strArr = file.read().split(',')
        intArr = map(int, strArr)
        return Robby(intArr)

    def moveDirection(self, current, north, east, south, west, action):
        score = 0

        if(action == ACTIONS.MOVE_NORTH):
            if(north == OBSTACLES.WALL):
                score = score - 5
            else:
                self.positionR = self.positionR - 1
        elif(action == ACTIONS.MOVE_EAST):
            if(east == OBSTACLES.WALL):
                score = score - 5
            else:
                self.positionC = self.positionC + 1
        elif(action == ACTIONS.MOVE_SOUTH):
            if(south == OBSTACLES.WALL):
                score = score - 5
            else:
                self.positionR = self.positionR + 1
        elif(action == ACTIONS.MOVE_WEST):
            if(west == OBSTACLES.WALL):
                score = score - 5
            else:
                self.positionC = self.positionC - 1

        return score


    # (TODO #1)
    # This function moves the robot by checking its five sites and retrieving the appropriate action from the DNA sequence.
    def getNextAction(self):

        current = self.grid[self.positionR][self.positionC]
        north = self.grid[self.positionR-1][self.positionC]
        east = self.grid[self.positionR][self.positionC+1]
        south = self.grid[self.positionR+1][self.positionC]
        west = self.grid[self.positionR][self.positionC-1]


        list_of_actions = [ACTIONS.MOVE_NORTH, ACTIONS.MOVE_EAST, ACTIONS.MOVE_SOUTH, ACTIONS.MOVE_WEST, ACTIONS.MOVE_RANDOM, ACTIONS.STAY_PUT, ACTIONS.PICK_UP_CAN]
        find_the_index = getIndex(current,north, east, south, west)
        actions = self.gene[find_the_index]
        action = list_of_actions[actions]
        return action




    def move(self):
        score = 0
        self.moveCount = self.moveCount + 1

        action = self.getNextAction()

        current = self.grid[self.positionR][self.positionC]
        north = self.grid[self.positionR-1][self.positionC]
        east = self.grid[self.positionR][self.positionC+1]
        south = self.grid[self.positionR+1][self.positionC]
        west = self.grid[self.positionR][self.positionC-1]

        if(action == ACTIONS.MOVE_NORTH or action == ACTIONS.MOVE_EAST or action == ACTIONS.MOVE_SOUTH or action == ACTIONS.MOVE_WEST):
            score = self.moveDirection(current, north, east, south, west, action)
        elif(action == ACTIONS.MOVE_RANDOM):
            score = self.moveDirection(current, north, east, south, west, getRandomMoveAction())
        elif(action == ACTIONS.STAY_PUT):
            pass
        elif(action == ACTIONS.PICK_UP_CAN):
            if(current == OBSTACLES.EMPTY):
                score = score - 1
            elif(current == OBSTACLES.CAN):
                score = score + 10
                self.grid.pickupCan(self.positionR, self.positionC)

        return score

    # (TODO 3)
    #Mutates a DNA sequence with a given mutation probability (MUTATION PROBABILITY).
    def mutate(self, gene):
        gene = self.gene
        lista = [0,1,2,3,4,5,6]
        for i in range(len(gene)):
            if MUTATION_PROBABILITY > random.random():
                gene[i] = random.choice(lista)
        return gene


    # (TODO 4)
    #This functions takes another robot instance as an input (its mate) and produces two children from them.
    #it makes the cross-over logic and call the mutation function.
    def giveBirth(self, otherRobot):
        value = self.gene
        value2 = otherRobot.gene

        midpoint = random.randint(0,len(value))
        new_robot = value[:midpoint] + value2[midpoint:]
        new_robot1= value[midpoint:] + value2[:midpoint]

        robby_rob = self.mutate(new_robot)
        robby_rob1= self.mutate(new_robot1)

        robot1 = Robby(robby_rob)
        robot2 = Robby(robby_rob1)

        return [robot1, robot2]


    def save(self, fileName):
        outfile = open(fileName, "w")
        outfile.write(','.join(str(number) for number in self.gene))


#c = Robby

#gene = c.getRandomRobby()
#print gene

#ca = Robby(gene)
#gene2 = ca.mutate(gene)
#print gene2
#birth = ca.giveBirth(gene)
#print birth
