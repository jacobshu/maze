from cell import Cell
from point import MapPoint
from typing import Dict, Optional
from window import Window
import random
import time

class Maze():
    def __init__(self, x: float, y: float, num_rows: int, num_cols: int, cell_size: float, win: Optional[Window], seed=None) -> None:
        self.x = x
        self.y = y
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size = cell_size
        self.win = win
        self.seed = seed
        random.seed(self.seed)

        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_cells()

    def __create_cells(self):
        self.cells = []

        for v in range(self.num_cols):
            row = []
            for h in range(self.num_rows):
                offset_x = h * self.cell_size
                offset_y = v * self.cell_size
                c = Cell(self.win, h, v, self.x + offset_x, self.y + offset_y, self.cell_size)
                row.append(c)
            self.cells.append(row)

        for row in self.cells:
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
        time.sleep(0.015)

    def get_cell(self, point: MapPoint) -> Optional[Cell]:
        if point.x > self.num_cols - 1 or point.y > self.num_rows - 1 or point.x < 0 or point.y < 0:
            return None
        return self.cells[point.y][point.x]

    def __break_entrance_and_exit(self):
        entrance = self.get_cell(MapPoint(0,0))
        if entrance == None:
            return
        entrance.has_top_wall = False
        entrance.draw() 

        exit = self.get_cell(MapPoint(self.num_rows - 1, self.num_cols - 1))
        if exit == None:
            return
        exit.has_bottom_wall = False
        exit.draw()

    def get_adjacent_cells(self, x, y) -> Dict[str, Cell]:
        cells = {}
        o = MapPoint(x, y)
        o.top()
        cells["top"] = self.get_cell(o)
        o.bottom()
        o.right()
        cells["right"] = self.get_cell(o)
        o.left()
        o.bottom()
        cells["bottom"] = self.get_cell(o)
        o.top()
        o.left()
        cells["left"] = self.get_cell(o)
        return cells

    def __break_walls_r(self, x, y):
        #time.sleep(0.75)
        c = self.get_cell(MapPoint(x, y))
        if c == None:
            return
        print(f"visiting: {c}")
        c.visited = True
        while True:
            adjacent = self.get_adjacent_cells(x, y)
            unvisited = 0
            for cell in adjacent.values():
                if cell != None and cell.visited == False:
                    unvisited += 1
            print(f"{unvisited} unvisited cells next to {c.get_coordinates()}\n")
            if unvisited == 0:
                c.draw()
                return
            else:
                directions = []
                for kv in adjacent.items():
                    if kv[1] != None:
                        directions.append(kv[0])
               
                direction = random.choice(directions)
                #direction = "top"
                next = adjacent[direction]
                next_coords = next.get_coordinates()
                if next.visited:
                    print(f"cell at {next_coords} already visited")
                self.break_wall(next_coords, direction)
                self.__break_walls_r(next_coords.x, next_coords.y)


    def break_wall(self, mp: MapPoint, dir: str):
        if dir not in ["top", "right", "left", "bottom"]:
            raise Exception(f"invalid direction: {dir}")
        
        next = MapPoint(mp.x, mp.y)
        if dir == "top":
            next.top()
        elif dir == "right":
            next.right()
        elif dir == "bottom":
            next.bottom()
        elif dir == "left":
            next.left()

        current_cell = self.get_cell(mp)
        next_cell = self.get_cell(next)
        if next_cell == None or current_cell == None:
            return

        if dir == "top":
            current_cell.has_top_wall = False
            next_cell.has_bottom_wall = False
        elif dir == "right":
            current_cell.has_right_wall = False
            next_cell.has_left_wall = False
        elif dir == "bottom":
            current_cell.has_bottom_wall = False
            next_cell.has_top_wall = False
        elif dir == "left":
            current_cell.has_left_wall = False
            next_cell.has_right_wall = False


    def __reset_cells(self):
        for v in self.cells:
            for cell in v:
                cell.visited = False


    def __str__(self) -> str:
        s =  f"{self.num_rows}x{self.num_cols} maze\n{len(self.cells) * len(self.cells[0])} total cells\n"
        for row in self.cells:
            row_str = "| "
            for cell in row:
                c = cell.get_coordinates()
                row_str += f"({c.x},{c.y}) "
            row_str += " |\n"
            s += row_str
        return s
