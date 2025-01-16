import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 8
        num_rows = 10
        m = Maze(0, 0, num_rows, num_cols, 10, None)
        print(m)
        self.assertEqual(
            len(m.cells),
            num_cols,
        )
        self.assertEqual(
            len(m.cells[0]),
            num_rows,
        )

    def test_get_adjacent(self):
        m = Maze(0, 0, 4, 6, 10, None)
        c = m.get_cell(1, 1)
        adj = m.get_adjacent_cells(1,1)
        for c in adj:
            print(c)
if __name__ == "__main__":
    unittest.main()
