from maze import Maze
from window import Window

def main():
    num_rows = 8
    num_cols = 8
    margin = 50
    cell_size = 50
    screen_x = (cell_size * num_cols) + (2 * margin)
    screen_y = (cell_size * num_rows) + (2 * margin)
    print(f"screen: {screen_x}, {screen_y}")
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size, win)
    
    win.wait_for_close()

if __name__ == '__main__':
    main()
