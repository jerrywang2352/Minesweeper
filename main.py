from tkinter import *
from MineGrid import MineGrid

root = Tk()
game = MineGrid(root, 25, 25, 75) #plays a game of Minesweeper on a 25 x 25 grid with 100 bombs
root.mainloop()