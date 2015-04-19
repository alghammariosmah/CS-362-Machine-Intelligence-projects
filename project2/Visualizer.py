from Parameters import *
from PuzzleState import *
import Tkinter as tk
import time

# Visualizes a list of PuzzleStates
# usage: Visualizer(puzzleStateList)

class Visualizer:
    puzzleStates = []
    index = 0
    cSize= VISUALIZER_WIDTH
    cellW = 0.0
    widgetIndexes = []

    def __init__(self, puzzleStates):
        self.puzzleStates = puzzleStates
        self.cellW = self.cSize / len(puzzleStates[0].matrix)
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=self.cSize, height=self.cSize)
        self.createWidgets()
        self.canvas.pack()
        self.root.after(0, self.animate)
        self.root.mainloop()

    def make_label(self, master, x, y, ww, hh, *args, **kwargs):
        f = tk.Frame(master, height=hh, width=ww, background='red')
        f.pack_propagate(0) # don't shrink
        f.place(x=x, y=y)
        label = tk.Label(f, *args, **kwargs)
        label.pack(fill=tk.BOTH, expand=1)
        return label

    def createWidgets(self):
        w = self.cellW
        self.widgetIndexes = []

        m = self.puzzleStates[self.index].matrix
        for i in range(len(m)):
            line = []
            for j in range(len(m)):
                value =  m[i][j]

                temp = 0
                if value == 0:
                    temp = self.make_label( self.canvas, j*w, i*w, w, w, text='',
                                            foreground='white', background='white', font=("Helvetica", 48) )
                else:
                    temp = self.make_label( self.canvas, j*w, i*w, w, w, text=str(value),
                                            foreground='white', background='blue', font=("Helvetica",  48) )

                temp.config(highlightbackground='red')
                temp.config(highlightthickness=4)

                line.append(temp)
            self.widgetIndexes.append(line)

    def drawFrame(self):
        m = self.puzzleStates[self.index].matrix
        for i in range(len(m)):
            for j in range(len(m[i])):
                value = m[i][j]
                if value == 0:
                    self.widgetIndexes[i][j].config(text='', foreground='white', background='white')
                else:
                    self.widgetIndexes[i][j].config(text=str(value), foreground='white', background='blue')

                #widgetIndexes[i][j].config(highlightbackground='red')
                #widgetIndexes[i][j].config(highlightthickness=4)

    def nextFrame(self):
        nextIndex = self.index + 1
        if nextIndex < len(self.puzzleStates):
            self.index = nextIndex
            return True
        return False

    def animate(self):
        self.drawFrame()
        if self.nextFrame():
            self.root.after(ANIMATION_DELAY, self.animate)

    def quit(self):
        self.running = False
        self.root.quit()
