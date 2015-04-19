import os
from Parameters import *
from MultipleSessions import *
from Robby import *
import random
#import matplotlib.pyplot as plt

class Generation:
    robots = []

    def __init__(self, id, robots=None):
        self.id = id
        if robots == None:
            for i in range(POPULATION_SIZE):
                self.robots.append(Robby.getRandomRobby())
        else:
            self.robots = robots
    #  (TODO #4)
    # Uses roulette wheel selection logic.
    # Picks a number depending on the rankings probabilistically.
    def getRouletteWheelSelection(self, count):
        population_number = count
        empty = [] # a list of the most probabilistic numbers
        population_list = range(population_number+1)
        for i in population_list:
            k = [population_list[i]]*population_number
            population_number-=1
            for n in k:
                empty.append(n)
        choose = random.choice(empty) # Picks a number depending on the probabilistic rankings
        return choose

    def getScore(self):
        rVal = 0.0
        for i in range(len(self.robots)):
            m = MultipleSessions(self.robots[i])
            rVal = rVal + m.run()
        return rVal / len(self.robots)

    def applyEvolution(self):
        tuples = []
        totalScore = 0.0

        MultipleSessions.refreshGrids()
        for i in range(len(self.robots)):
            m = MultipleSessions(self.robots[i])
            score = m.run()
            totalScore = totalScore + score
            tuples.append( (self.robots[i], score) )

        tuples.sort(key=lambda x: x[1], reverse=True)
        normalizedScore = totalScore / len(self.robots)
        bestScore = tuples[0][1]

        childRobots = []
        # (TODO #5)
        # fill the childRobots array with POPULATION_SIZE children
        # using getRouletteWheelSelection() and Robby.giveBirth()
        for new in range(POPULATION_SIZE):
            father = tuples[self.getRouletteWheelSelection(POPULATION_SIZE)][0]
            mother = tuples[self.getRouletteWheelSelection(POPULATION_SIZE)][0]
            [child1,child2] = father.giveBirth(mother)
            childRobots.append(child1)
            childRobots.append(child2)
        number_of_stay_puts = 0
        for number in tuples:
            k = number[0].gene
            for nu in k:
                if nu == ACTIONS.STAY_PUT:
                    number_of_stay_puts+=1

        print tuples[0][0].gene

        return (Generation(self.id + 1, childRobots), normalizedScore, bestScore, number_of_stay_puts)
#g = Generation(0)
#print g.applyEvolution()
