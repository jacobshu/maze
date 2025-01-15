from cell import Cell
from constants import CELL_SIZE
from line import Line
from point import Point
from window import Window

def main():
    win = Window(800, 600)

    c = Cell(win)
    c.has_left_wall = False
    c.draw(50, 50)

    c = Cell(win)
    c.has_right_wall = False
    c.draw(125, 125)

    c2 = Cell(win)
    c2.has_bottom_wall = False
    c2.draw(225, 225)

    c3 = Cell(win)
    c3.has_top_wall = False
    c3.draw(300, 300)

    c3.draw_move(c2)
    c2.draw_move(c, undo=True)
    

    win.wait_for_close()

if __name__ == '__main__':
    main()
