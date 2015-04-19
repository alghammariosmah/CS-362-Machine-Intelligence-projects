from Parameters import *
from Session import *
from Grid import *
import copy

class MultipleSessions:
    robby = None

    def __init__(self, robby):
        self.robby = robby
        if not hasattr(MultipleSessions, 'grids'):
            self.refreshGrids()

    @staticmethod
    def refreshGrids():
        MultipleSessions.grids = []
        for i in range(NUM_SESSIONS):
            grid = Grid.getRandomGrid()
            MultipleSessions.grids.append(grid)

    def run(self):
        totalScore = 0.0
        for grid in MultipleSessions.grids:
            session = Session(self.robby, copy.deepcopy(grid))
            score = session.run()
            self.robby.clean()
            totalScore = totalScore + score
        return ( totalScore / len(MultipleSessions.grids) )
