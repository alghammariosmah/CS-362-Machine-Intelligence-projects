from Parameters import *
from Passenger import *
from Feature import *
import math
import copy

"""
This class respresents a node of a decision tree.
Usage: node = Node(list_of_passengers)
node.isLeaf() returns whether the node is leaf.
"""
class Node:
    """
    Node constructor class.
    You may need to modify this function.
    Hint:	Adding an entropy criterion to stop splitting
    """
    def __init__(self, passengers, level=0):
        self.passengers = passengers
        self.level = level
        if self.level < MAX_DEPTH and len(passengers) > MIN_ITEMS:
            self.bestFeature = self.getBestFeature()
            self.split(self.bestFeature)

    """
    Returns whether this node has any branches.
    Three reasons not having any branches:
    (1. MAX_DEPTH, 2. MIN_ITEMS, 3. ENTROPY GAIN)
    """
    def isLeaf(self):
        if self.branches == None or len(self.branches) == 0:
            return True
        return False

    def survivalProbability(self):
        survived, died = 0,0
        for p in self.passengers:
            if p.survived:
                survived += 1
            else:
                died += 1
        return float(survived) / (survived + died)

    """
    Returns number of passengers in this node.
    """
    def getNumSamples(self):
        return len(self.passengers)

    def getBranches(self):
        return self.branches

    def split(self, feature):
        branch1 = []
        branch2 = []
        for p in self.passengers:
            result = p.split(feature)
            if result:
                branch1.append(copy.deepcopy(p))
            else:
                branch2.append(copy.deepcopy(p))
        self.branches = (Node(branch1,self.level+1), Node(branch2,self.level+1))

    """
    This function finds the best feature which has the maximum entropy
    gain ratio.
    """
    def getBestFeature(self):
        bestFeature = None
        Hishest_info_gain = 0
        features = Feature.getAllFeatures()
        counter = 0
        for pa in self.passengers:
            if pa.survived:
                counter+=1
        a = (float(counter)/float(self.getNumSamples()))
        b = (float(float(self.getNumSamples())- float(counter))/float(self.getNumSamples()))
        entro_father = self.getEntropy(a,b)

        for i in range(len(features)):
            branch1 = []
            branch2 = []
            counter1 = 0
            for j in range(len(self.passengers)):
                p = self.passengers[j]
                f = features[i]
                result = p.split(f)
                if result:
                    branch1.append(copy.deepcopy(p))
                    #print f.thresholdValue, "branch1", p, result
                    counter1+=1
                else:
                    branch2.append(copy.deepcopy(p))
                    #print f.thresholdValue, "branch2", p, result

            #print "feature:", f.thresholdValue, "how many true members",counter1,"out of", self.getNumSamples(), "the rest = ",(int(self.getNumSamples())-int(counter1))

            surviving_counter1 = 0
            for pure in branch1:
                surviving = pure.survived
                if surviving:
                    surviving_counter1+=1
            #print "survived = ",float(surviving_counter1),"out of", float(len(branch1)),"the rest = ",(float(len(branch1))-float(surviving_counter1))

            if surviving_counter1 == 0:#if there is 0 survivals ignore
                continue
            else:
                a_child_1 = (float(surviving_counter1)/float(len(branch1)))
                b_child_1 = (float(len(branch1))-float(surviving_counter1))/float(len(branch1))
            child_1_entro = self.getEntropy(a_child_1,b_child_1)


            surviving_counter2 = 0
            for impure in branch2:
                surviving2 = impure.survived
                if not surviving2:
                    surviving_counter2+=1
            #print "survived = ",float(surviving_counter2),"out of", float(len(branch2)),"the rest = ",(float(len(branch2))-float(surviving_counter2))

            if surviving_counter2 == 0:
                continue
            else:
                a_child_2 = (float(surviving_counter2)/float(len(branch2)))
                b_child_2 = (float(len(branch2))-float(surviving_counter2))/float(len(branch2))
            child_2_entro = self.getEntropy(a_child_2,b_child_2)

            average_entro_children = ((float(len(branch1))/float(self.getNumSamples()))*child_1_entro)+((float(len(branch2))/float(self.getNumSamples()))*child_2_entro)
            information_gain = (float(entro_father) - float(average_entro_children))
            if information_gain > Hishest_info_gain:
                Hishest_info_gain = information_gain
                bestFeature = features[i]
        return bestFeature




    @staticmethod
    def getEntropy(a,b):
        if a == 0 or b == 0:
            return 0
        return -(a*math.log(a) + b*math.log(b))
