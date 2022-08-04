from tkinter import filedialog
from tkinter import messagebox
import random
import MineCell

class MineGrid(Frame):
    '''object for a minesweeper grid'''

    def __init__(self, master, width, height, numBombs):
        '''MineGrid(master,x,y,numMine)
        creates a new minesweeper grid'''
        Frame.__init__(self, master)
        self.grid()
        self.cell = []
        self.width = width
        self.height = height
        self.coordDict = {}
        for row in range(self.height):
            for column in range(self.width):
                self.coordDict[(row, column)] = 0

        for i in range(numBombs):  # place all the mines
            coord = random.choice([coord for coord in list(self.coordDict) if self.coordDict[coord] == 0])
            self.coordDict[coord] = MineCell(self, coord, True, '')
            self.coordDict[coord].grid(row=coord[0], column=coord[1])

        for key in self.coordDict:
            if self.coordDict[key] == 0:  # if coordinate does not have a mine
                numMine = 0
                for row2 in [key[0] - 1, key[0], key[0] + 1]:
                    for column2 in [key[1] - 1, key[1], key[1] + 1]:
                        newCoord = (row2, column2)
                        if newCoord in self.coordDict and self.coordDict[newCoord] != 0 and self.coordDict[
                            newCoord].is_mine():
                            numMine += 1
                self.coordDict[key] = MineCell(self, (key[0], key[1]), False, numMine)
                self.coordDict[key].grid(row=key[0], column=key[1])
        self.numMine = IntVar()
        self.numMine.set(numBombs)

        self.mineLabel = Label(self, bg='white', textvariable=self.numMine, font=(None, 15))
        self.mineLabel.grid(row=self.height, column=0, columnspan=self.width)

    def lose_game(self):
        messagebox.showerror('Minesweeper', 'KABOOM! You lose.', parent=self)
        for key in self.coordDict:
            self.coordDict[key].highlight_mine()

    def expose_chunk(self, exposeCoord):
        for row in [exposeCoord[0] - 1, exposeCoord[0], exposeCoord[0] + 1]:
            for column in [exposeCoord[1] - 1, exposeCoord[1], exposeCoord[1] + 1]:
                if (row, column) in self.coordDict and self.coordDict[(row, column)].get_num() == 0 and self.coordDict[
                    (row, column)].is_expose() == False:
                    self.coordDict[(row, column)].expose_num()
                    self.expose_chunk((row, column))
                if (row, column) in self.coordDict:
                    self.coordDict[(row, column)].expose_num()

    def decrease_mine(self, coord):
        if self.coordDict[coord].is_mine():
            self.numMine.set(self.numMine.get() - 1)

    def increase_mine(self, coord):
        if self.coordDict[coord].is_mine():
            self.numMine.set(self.numMine.get() + 1)

    def win_game(self):
        messagebox.showinfo('Minesweeper', 'Congratulations -- you won!', parent=self)

