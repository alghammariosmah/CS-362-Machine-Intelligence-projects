import csv


class Passenger:
    def __init__(self, line):
        self.originalStr = line
        temp = csv.reader([line]).next()
        self.passengerId = int(temp[0])
        self.survived = bool(int(temp[1]))
        self.pClass = int(temp[2])
        self.name = temp[3]
        self.sex = temp[4]
        self.age = None if temp[5] == '' else float(temp[5])
        self.sibSp = int(temp[6])
        self.parch = int(temp[7])
        self.ticket = temp[8]
        self.fare = temp[9]
        self.cabin = temp[10]
        self.embarked = temp[11]

    """
    Only relevant features for survival.
    The order *matters*
    """
    def toFeatureVector(self):
        return [self.pClass, self.sex, self.age, self.sibSp]

    """
    This function takes a feature and return true if this passenger is in the left branch, return false if this passenger is in the right branch.
    """
    def split(self, feature):
        featureVector = self.toFeatureVector()
        if feature.featureType == 'DISCRETE':
            if featureVector[feature.featureId] == feature.thresholdValue:
                return True
            return False
        elif feature.featureType == 'CONTINIOUS':
            if featureVector[feature.featureId] >= feature.thresholdValue:
                return True
            return False

    def __str__(self):
        return 'passengerId:'+ str(self.passengerId) + ',pClass:' + str(self.pClass) + ',sex:' + self.sex + ',age:' + str(self.age)
