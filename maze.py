from cell import Cell
import time
from typing import Optional
from window import Window
import random

class Maze():
    def __init__(self, x: float, y: float, num_rows: int, num_cols: int, cell_size: float, win: Optional[Window], seed=None) -> None:
        self.x = x
        self.y = y
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size = cell_size
        self.win = win

        self.__create_cells()
        self.__break_entrance_and_exit()

    def __create_cells(self):
        self.__cells = []

        for x in range(self.num_cols):
            row = []
            for y in range(self.num_rows):
                offset_x = x * self.cell_size
                offset_y = y * self.cell_size
                c = Cell(self.win, self.x + offset_x, self.y + offset_y, self.cell_size)
                row.append(c)
            self.__cells.append(row)

        for row in self.__cells:
            for cell in row:
                self.__draw_cell(cell)

    def __draw_cell(self, c: Cell):
        if self.win == None:
            return
        c.draw()
        self.__animate()

    def __animate(self):
        if self.win == None:
            return
        self.win.redraw()
        time.sleep(0.02)

    def get_cell(self, x: int, y: int) -> Cell:
        return self.__cells[y][x]

    def __break_entrance_and_exit(self):
        entrance = self.get_cell(0,0)
        entrance.has_top_wall = False
        entrance.draw() 

        exit = self.get_cell(self.num_rows - 1, self.num_cols - 1)
        exit.has_bottom_wall = False
        exit.draw()

    def __break_walls_r(self, x, y):
        c = self.get_cell(x, y)
        c.visited = True
