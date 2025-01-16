from typing import Optional
from line import Line
from point import MapPoint
from point import Point
from window import Window

class Cell:
    def __init__(self, window: Optional[Window], coords_x: int, coords_y: int, display_x: float, display_y: float, size: float) -> None:
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.has_left_wall = True
        self.coordinates = MapPoint(coords_x, coords_y)
        self.__x1 = display_x
        self.__y1 = display_y
        self.__x2 = self.__x1 + size
        self.__y2 = self.__y1 + size
        self.__win = window
        self.visited = False

    def get_coordinates(self) -> MapPoint:
        return self.coordinates

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


    def __str__(self) -> str:
        tw = " "
        rw = " "
        bw = " "
        lw = " "
        if self.has_top_wall:
            tw = "↑"
        if self.has_right_wall:
            rw = "→"
        if self.has_bottom_wall:
            bw = "↓"
        if self.has_left_wall:
            lw = "←"
        return f"""Cell:
            origin  = {self.coordinates.x}, {self.coordinates.y}
            walls:  = {tw}{rw}{bw}{lw}
            display = ({self.__x1}, {self.__y1}) -> ({self.__x2}, {self.__y2})
            visited = {self.visited}
        """
