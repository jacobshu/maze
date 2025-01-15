from constants import CELL_SIZE
from line import Line
from point import Point

class Cell:
    def __init__(self, window) -> None:
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.has_left_wall = True
        self.__x1 = 0
        self.__y1 = 0
        self.__x2 = self.__x1 + CELL_SIZE
        self.__y2 = self.__y1 + CELL_SIZE
        self.__win = window

    def draw(self, x1, y1):
        self.__x1 = x1
        self.__x2 = x1 + CELL_SIZE
        self.__y1 = y1
        self.__y2 = y1 + CELL_SIZE
        nw = Point(self.__x1, self.__y1)
        ne = Point(self.__x2, self.__y1)
        sw = Point(self.__x1, self.__y2)
        se = Point(self.__x2, self.__y2)
        if self.has_top_wall:
            line = Line(nw, ne)
            self.__win.draw_line(line, "cyan")
        if self.has_right_wall:
            line = Line(ne, se)
            self.__win.draw_line(line, "cyan")
        if self.has_bottom_wall:
            line = Line(se, sw)
            self.__win.draw_line(line, "cyan")
        if self.has_left_wall:
            line =  Line(sw, nw)
            self.__win.draw_line(line, "cyan")

    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "gray"
        from_center = Point(
            (self.__x1 + (self.__x2 - self.__x1) / 2),
            (self.__y1 + (self.__y2 - self.__y1) / 2)
        )

        to_center = Point(
            (to_cell.__x1 + (to_cell.__x2 - to_cell.__x1) / 2),
            (to_cell.__y1 + (to_cell.__y2 - to_cell.__y1) / 2)
        )

        line = Line(from_center, to_center)
        self.__win.draw_line(line, color)



