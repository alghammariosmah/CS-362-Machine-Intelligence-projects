import time
from Generation import *
from Parameters import *
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1

class God:
    generation = None

    def initializeFirstGeneration(self):
        self.generation = Generation(0)

    def applyEvolution(self):
        empty = []
        empty2 = []#number of stay puts
        for i in range(NUM_GENERATIONS):
            self.generation, normalizedScore, bestScore, number_of_stay_puts = self.generation.applyEvolution()
            print( str(normalizedScore) + ',' + str(bestScore) )
            empty.append(bestScore)
            empty2.append(number_of_stay_puts)

            with open('results.txt', 'a') as file:
                file.write( str(normalizedScore) + ',' + str(bestScore) + '\n')

        plt.plot(empty2,'r-',label='Number of stay puts')
        plt.plot(empty,'b-', label ='Fitness in the population')
        plt.ylabel("Best Fitness in Population")
        plt.xlabel("Generation")
        plt.legend()
        plt.savefig('foo.png')
        plt.show()
