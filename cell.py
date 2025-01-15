from typing import Optional
from line import Line
from point import Point
from window import Window

class Cell:
    def __init__(self, window: Optional[Window], x: float, y: float, size: float) -> None:
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.has_left_wall = True
        self.__x1 = x
        self.__y1 = y
        self.__x2 = self.__x1 + size
        self.__y2 = self.__y1 + size
        self.__win = window
        self.visited = False

    def draw(self):
        nw = Point(self.__x1, self.__y1)
        ne = Point(self.__x2, self.__y1)
        sw = Point(self.__x1, self.__y2)
        se = Point(self.__x2, self.__y2)
        if self.__win == None:
            return
        wall = "cyan"
        no_wall = "black"
        top = Line(nw, ne)
        right = Line(ne, se)
        bottom = Line(se, sw)
        left =  Line(sw, nw)
        if self.has_top_wall:
            self.__win.draw_line(top, wall)
        else:
            self.__win.draw_line(top, no_wall)

        if self.has_right_wall:
            self.__win.draw_line(right, wall)
        else:
            self.__win.draw_line(right, no_wall)

        if self.has_bottom_wall:
            self.__win.draw_line(bottom, wall)
        else:
            self.__win.draw_line(bottom, no_wall)

        if self.has_left_wall:
            self.__win.draw_line(left, wall)
        else:
            self.__win.draw_line(left, no_wall)

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
        if self.__win == None:
            return
        self.__win.draw_line(line, color)



