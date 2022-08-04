from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import random


class MineCell(Label):
    '''represent a Minesweeper cell'''

    def __init__(self, master, coord, isMine, num):
        '''MineCell(master,coord,cellType,num) -> MineCell
        creates a cell at (row,column) that is blank,number,or mine'''
        Label.__init__(self, master, height=1, width=2, bg='white', \
                       bd=3, relief='raised')
        self.coord = coord
        self.isMine = isMine
        self.num = num
        self.isExpose = False
        self.bind('<Button-1>', self.expose_cell)
        self.bind('<Button-3>', self.flag_cell)

    def get_coord(self):
        '''MineCell.get_coord() -> tuple
        return the (row,column) coordinate of the cell'''
        return self.coord

    def is_mine(self):
        '''MineCell.is_mine() -> boolean
        checks if the cell is a mine'''
        return self.isMine

    def is_blank(self):
        '''MineCell.is_blank() -> boolean
        checks if the cell is empty'''
        if isMine == False and num == '':
            return True
        else:
            return False

    def get_num(self):
        '''MineCell.get_num() -> int
        returns the number in a cell'''
        return self.num

    def flag_cell(self, event):
        '''MineCell.flag_cell(event)
        handler funtion for right mouse click
        marks the cell as a mine'''
        if self['text'] == '*':
            self.master.increase_mine(self.coord)
            self['text'] = ''
        elif self['relief'] != 'sunken':
            self['text'] = '*'
            self.master.decrease_mine(self.coord)

        if self.master.numMine.get() == 0:
            self.master.win_game()

    def expose_cell(self, event):
        '''MineCell.expose_cell(event)
        handler function for left mouse click
        shows what the cell is'''
        if self.isMine == True:  # cell is a mine
            self['bg'] = 'red'
            self['text'] = '*'
            self['relief'] = 'sunken'
            self.master.lose_game()  # end the game
        else:  # cell is a number
            colorList = ['', 'blue', 'darkgreen', 'red', 'purple', 'maroon', 'cyan', 'black', 'dim gray']
            self['relief'] = 'sunken'
            self['bg'] = 'grey'
            self.isExpose = True
            if self.num != 0:
                self['fg'] = colorList[self.num]
                self['text'] = str(self.num)
            else:
                self['text'] = ''
                self.master.expose_chunk(self.coord)

    def expose_num(self):
        if isinstance(self.num, int) and self.num != 0:
            self.isExpose = True
            colorList = ['', 'blue', 'darkgreen', 'red', 'purple', 'maroon', 'cyan', 'black', 'dim gray']
            self['fg'] = colorList[self.num]
            self['text'] = str(self.num)
            self['relief'] = 'sunken'
            self['bg'] = 'grey'
        elif isinstance(self.num, int) and self.num == 0:
            self.isExpose = True
            self['text'] = ''
            self['relief'] = 'sunken'
            self['bg'] = 'grey'

    def highlight_mine(self):
        if self.isMine:
            self['bg'] = 'red'
            self['text'] = '*'

    def is_expose(self):
        return self.isExpose