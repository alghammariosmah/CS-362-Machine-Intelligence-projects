from Parameters import *
from Grid import *
from Robby import *
from enum import *
import Tkinter as tk
import time

class Alien:
    running = True
    grid = None
    cSize= 600.0
    cellW = cSize / 12.0
    counter = 0

    def __init__(self, grid):
        self.grid = grid
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=self.cSize, height=self.cSize)
        self.createWidgets()
        self.canvas.pack()
        self.root.after(0, self.animate)
        self.root.mainloop()

    def createWidgets(self):
        self.gridIndexes = []
        w = self.cellW
        for i in range(len(self.grid.matrix)):
            temp = []
            for j in range(len(self.grid.matrix[i])):
                temp.append( self.canvas.create_rectangle(j*w, i*w, (j+1)*w, (i+1)*w, fill='blue'))
            self.gridIndexes.append(temp)
        rr = self.grid.robby.getR()
        rc = self.grid.robby.getC()
        self.robby = self.canvas.create_oval(rc * w, rr * w, (rc + 1) * w, (rr + 1) * w, fill='red')
        self.txtCounter = self.canvas.create_text(self.cSize / 2 - 40, self.cellW / 2, fill = "red")
        self.txtAction = self.canvas.create_text(self.cSize / 2 + 40, self.cellW / 2, fill = "red")

    def drawFrame(self, rr, rc, action, counter):
        w = self.cellW
        for i in range(len(self.grid.matrix)):
            for j in range(len(self.grid.matrix[i])):
                color = None
                if self.grid.matrix[i][j] == OBSTACLES.WALL:
                    color = 'black'
                elif self.grid.matrix[i][j] == OBSTACLES.EMPTY:
                    color = 'white'
                elif self.grid.matrix[i][j] == OBSTACLES.CAN:
                    color = 'blue'
                self.canvas.itemconfig(self.gridIndexes[i][j], fill=color) #change color
        self.canvas.coords(self.robby, rc * w, rr * w, (rc + 1) * w, (rr + 1) * w)
        self.canvas.itemconfig(self.txtAction, text=action)
        self.canvas.itemconfig(self.txtCounter, text=str(counter))

    def animate(self):
        if self.running:
            action = ACTIONS.reverse_mapping[self.grid.robby.getNextAction()]
            self.drawFrame(self.grid.robby.getR(), self.grid.robby.getC(), action, self.grid.robby.moveCount)
            self.root.after(ANIMATION_DELAY, self.animate)
            score = self.grid.robby.move()

            if self.grid.robby.moveCount > NUM_ACTIONS_PER_SESSION:
                self.quit()

    def quit(self):
        self.running = False
        self.root.quit()
