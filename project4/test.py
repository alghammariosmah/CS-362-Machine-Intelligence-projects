from DataReader import *
from Passenger import *
from Node import *
from Feature import *

passengers = DataReader.read('data2.csv')

node = Node(passengers)


print node.bestFeature
print node.survivalProbability()
print node.isLeaf()
print node.branches[0].getBestFeature() 
print node.branches[0].survivalProbability()
print node.branches[1].getBestFeature() 
print node.branches[1].survivalProbability()


