import unittest
from maze import Maze

class Test(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        cell_size_x = 5
        cell_size_y = 15
        m1 = Maze(0,0,num_rows,num_cols,cell_size_x,cell_size_y,None)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)
        self.assertEqual(m1._cell_size_x, cell_size_x)
        self.assertEqual(m1._cell_size_y, cell_size_y)

if __name__ == "__main__":
    unittest.main()