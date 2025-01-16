class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
   
    def __repr__(self) -> str:
        return f"Point( {self.x}, {self.y} )"

class MapPoint:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
   
    def top(self):
        self.y += 1

    def right(self):
        self.x += 1

    def bottom(self):
        self.y -= 1

    def left(self):
        self.x -= 1

    def __repr__(self) -> str:
        return f"MapPoint( {self.x}, {self.y} )"


