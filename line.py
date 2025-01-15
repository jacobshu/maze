from tkinter import Canvas
from point import Point

class Line:
    def __init__(self, origin: Point, termination: Point) -> None:
        self.origin = origin
        self.termination = termination
       
    def draw(self, canvas: Canvas, fill_color="cyan"):
        canvas.create_line(
            self.origin.x, 
            self.origin.y, 
            self.termination.x, 
            self.termination.y, 
            fill=fill_color, 
            width=2
        )
