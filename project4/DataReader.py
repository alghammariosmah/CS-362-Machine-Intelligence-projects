from Passenger import *

"""
This is a static class to read from the given
data.csv file.
Usage: passengers = DataReader.read('data.csv')
"""
class DataReader:
    @staticmethod
    def read(path):
        rVal = []
        f = open(path)
        counter = 0
        for line in f:
            rVal.append(Passenger(line.strip()))
            counter +=1
        print 'DataReader: ' + str(counter) + ' items read.'
        return rVal
