import unittest
from drawing import Point
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(None, Point(0, 0), num_rows, num_cols, 10, 10, seed=1)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(len(m1._cells[0]), num_cols)

    def test_maze_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(None, Point(0, 0), num_rows, num_cols, 10, 10, seed=1)
        self.assertEqual(m1._cells[0][0].top_wall, False)
        self.assertEqual(m1._cells[num_rows - 1][num_cols - 1].bot_wall, False)

    def test_maze_reset_vist_after(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(None, Point(0, 0), num_rows, num_cols, 10, 10, seed=1)
        for i in range(num_rows):
            for j in range(num_cols):
                self.assertEqual(m1._cells[i][j].visited, False)


if __name__ == "__main__":
    unittest.main()
