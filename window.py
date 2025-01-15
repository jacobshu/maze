from tkinter import Tk, BOTH, Canvas
from line import Line

class Window:
    def __init__(self, width, height) -> None:
        self.__root = Tk()
        self.__root.wm_title("winder")
        self.__canvas = Canvas(self.__root, bg="black", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def close(self):
        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
    
    def draw_line(self, line: Line, fill_color="cyan"):
        line.draw(self.__canvas, fill_color)

    def draw_cell(self, cell, fill_color):
        cell.draw(self.__canvas, fill_color)
