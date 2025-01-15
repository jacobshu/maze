import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m = Maze(0, 0, num_rows, num_cols, 10, None)
        self.assertEqual(
            len(m.__cells),
            num_cols,
        )
        self.assertEqual(
            len(m.__cells[0]),
            num_rows,
        )

if __name__ == "__main__":
    unittest.main()
