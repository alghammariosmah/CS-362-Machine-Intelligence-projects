from util import *

thresholds = [[1,2,3], ['male','female'], frange(0.5,50,0.5), frange(0.5,5.0,0.5)]
featureTypes = ['DISCRETE','DISCRETE','CONTINIOUS','CONTINIOUS']

"""
This contains a featureId,
thresholdValue and a feature type (discrete or continious)
"""

class Feature:
    def __init__(self, featureId, thresholdValue, featureType):
        self.featureId = featureId
        self.thresholdValue = thresholdValue
        self.featureType = featureType

    @staticmethod
    def getAllFeatures():
        rVal = []
        for fId in range(len(thresholds)):
            for tValue in thresholds[fId]:
                f = Feature(fId, tValue, featureTypes[fId])
                rVal.append(f)
        return rVal

    def __str__(self):
        return str((self.featureId, self.thresholdValue, self.featureType))

